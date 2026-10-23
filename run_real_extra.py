import os, json, numpy as np, pandas as pd
from multiprocessing import Pool
import ivp
from ivp import protocol as P, indicators as I
syms=open("UNIVERSE_FROZEN.md").read().split("Symbols (38):")[1].split()[:38]
px=pd.concat({s:pd.read_csv(os.path.join(os.environ.get("PRICES_DIR", "data/prices"), f"{s}.csv"),parse_dates=["Date"]).set_index("Date")["Adj Close"] for s in syms},axis=1).sort_index()
px=px[(px.index>="2000-01-01")&(px.index<"2020-01-01")]; R=np.log(px).diff().values
def semi(a):
    ic,s=a; rng=np.random.default_rng(s); T,N=R.shape
    x=np.zeros((T,N)); x[0]=rng.standard_normal(N)
    for t in range(1,T): x[t]=0.95*x[t-1]+np.sqrt(1-.95**2)*rng.standard_normal(N)
    sd=np.nanstd(R,axis=0); Rp=R.copy(); Rp[1:]+=ic*sd*x[:-1]
    return P.evaluate(Rp,x)["p_cw"]<0.05
if __name__=="__main__":
    out={"leaky_on_real_dev":{k:{kk:float(v) for kk,v in P.evaluate(R,px.apply(f).values).items()} for k,f in I.LEAKY.items()}}
    with Pool(8) as p:
        for ic in [0,0.005,0.01,0.02]:
            r=p.map(semi,[(ic,s) for s in range(100)]); out[f"semi_synthetic_ic{ic}"]=float(np.mean(r))
    json.dump(out,open("results_ivp/real_extra.json","w"),indent=1); print(json.dumps(out,indent=1))
