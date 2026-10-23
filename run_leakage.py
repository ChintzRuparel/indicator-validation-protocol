import json, numpy as np, pandas as pd, glob, os
from multiprocessing import Pool
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold
import ivp
from ivp import dgp, protocol as P, indicators as I
OUT="results_ivp"
def l1(s):
    R,X=dgp.simulate(10,1260,0.0,seed=50000+s)
    return P.naive_pooled_ttest(R,X)['p']<0.05, P.evaluate(R,X)['p_cw']<0.05
def l3(s):
    R,X=dgp.simulate(10,1260,0.0,seed=60000+s); h=5
    y=P.forward_sum(R,h); lag20=pd.DataFrame(R).rolling(20).sum().values
    T,N=R.shape; tt=np.repeat(np.arange(T),N)
    F=np.c_[X.ravel(),lag20.ravel()]; yy=y.ravel(); ok=np.isfinite(F).all(1)&np.isfinite(yy)
    F,yy,tt=F[ok],yy[ok],tt[ok]
    def r2(pred,yv,base): return 1-np.sum((yv-pred)**2)/np.sum((yv-base)**2)
    # shuffled 5-fold (leaky): neighbours in feature space are adjacent days with overlapping labels
    pr=np.zeros_like(yy); bs=np.zeros_like(yy)
    for tr,te in KFold(5,shuffle=True,random_state=s).split(F):
        m=KNeighborsRegressor(50).fit(F[tr],yy[tr]); pr[te]=m.predict(F[te]); bs[te]=yy[tr].mean()
    r_shuf=r2(pr,yy,bs)
    # purged walk-forward
    pr2=[];yv=[];b2=[]
    for tr_end,st,en in P.folds(T,252,126,h):
        tr=tt<tr_end; te=(tt>=st)&(tt<en)
        if tr.sum()<100 or te.sum()==0: continue
        m=KNeighborsRegressor(50).fit(F[tr],yy[tr]); pr2.append(m.predict(F[te])); yv.append(yy[te]); b2.append(np.full(te.sum(),yy[tr].mean()))
    r_wf=r2(np.concatenate(pr2),np.concatenate(yv),np.concatenate(b2))
    return r_shuf,r_wf
LOOKS=[5,10,15,20,30,40,50,60,80,100,120,140,160,180,200,220,240,260,280,300]
def l4(s):
    R,_=dgp.simulate(10,1260,0.0,seed=70000+s)
    cs=pd.DataFrame(R).cumsum()
    ps=[P.evaluate(R,(cs-cs.shift(L)).values)['p_cw'] for L in LOOKS]
    return min(ps)<0.05, P.holm(ps).min()<0.05
def wilson(k,n,z=1.96):
    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; w=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/d; return [k/n,c-w,c+w]
if __name__=="__main__":
    res={}
    with Pool(8) as p:
        a=np.array(p.map(l1,range(200))); res['L1']=dict(naive=wilson(a[:,0].sum(),200),protocol=wilson(a[:,1].sum(),200))
        b=np.array(p.map(l3,range(100))); res['L3']=dict(shuffled_kfold_r2_median=float(np.median(b[:,0])),shuffled_frac_pos=float((b[:,0]>0).mean()),
            wf_r2_median=float(np.median(b[:,1])),wf_frac_pos=float((b[:,1]>0).mean()),shuffled_r2_q=[float(x) for x in np.quantile(b[:,0],[.05,.95])],wf_r2_q=[float(x) for x in np.quantile(b[:,1],[.05,.95])])
        c=np.array(p.map(l4,range(200))); res['L4']=dict(best_unadjusted=wilson(c[:,0].sum(),200),holm=wilson(c[:,1].sum(),200))
    # L2 PIT audit on real SPY prices
    spy=pd.read_csv(os.path.join(os.environ.get("PRICES_DIR","data/prices"),"SPY.csv"),parse_dates=["Date"]).set_index("Date")["Adj Close"]
    res['L2_audit']={k:I.pit_audit(f,spy) for k,f in {**I.CLASSIC,**I.LEAKY}.items()}
    json.dump(res,open(f"{OUT}/leakage.json","w"),indent=1,default=float); print(json.dumps(res,indent=1,default=float))
