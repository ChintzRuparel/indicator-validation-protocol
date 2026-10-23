"""Real-data application. Usage: run_real.py dev | holdout"""
import sys, json, glob, os, numpy as np, pandas as pd
import ivp
from ivp import protocol as P, indicators as I
OUT="results_ivp"; phase=sys.argv[1]
syms=open("UNIVERSE_FROZEN.md").read().split("Symbols (38):")[1].split()[:38]
px=pd.concat({s:pd.read_csv(os.path.join(os.environ.get("PRICES_DIR", "data/prices"), f"{s}.csv"),parse_dates=["Date"]).set_index("Date")["Adj Close"] for s in syms},axis=1).sort_index()
px=px[px.index>="2000-01-01"]
R=np.log(px).diff()
if phase=="dev": px=px[px.index<"2020-01-01"]; R=R[R.index<"2020-01-01"]
else: assert os.path.exists(f"{OUT}/real_dev.json"), "dev first"; open(f"{OUT}/HOLDOUT_USED.lock","w").write(pd.Timestamp.now().isoformat())
audit={k:I.pit_audit(f,px["SPY"]) for k,f in I.CLASSIC.items()}; assert max(audit.values())==0, audit
dates=R.index
def score_from(o_dates_mask, R_, X_, h):
    # evaluate; for holdout keep only test dates >= 2020 by masking the target after computation
    return P.evaluate(R_,X_,h=h)
res={"audit":audit,"n_tickers":len(syms),"start":str(dates[1].date()),"end":str(dates[-1].date())}
for h in [5,21]:
    for k,f in I.CLASSIC.items():
        X=px.apply(f).values
        Rv=R.values.copy()
        if phase=="holdout":
            # walk-forward over full sample; score only test dates >= 2020: blank pre-2020 *predictions* by
            # running evaluate with a test-date mask
            o=P.evaluate(Rv,X,h=h,score_from=int(np.searchsorted(dates,pd.Timestamp("2020-01-01"))))
        else:
            o=P.evaluate(Rv,X,h=h)
        res[f"{k}_h{h}"]={kk:float(v) for kk,v in o.items()}
for h in [5,21]:
    ks=[f"{k}_h{h}" for k in I.CLASSIC]; adj=P.holm([res[k]["p_cw"] for k in ks])
    for k,a in zip(ks,adj): res[k]["p_cw_holm"]=float(a)
json.dump(res,open(f"{OUT}/real_{phase}.json","w"),indent=1)
print(pd.DataFrame({k:v for k,v in res.items() if k.endswith(("h5","h21"))}).T[["t_cw","p_cw","p_cw_holm","t_dm","oos_r2","n_dates","n_obs"]].round(4))
