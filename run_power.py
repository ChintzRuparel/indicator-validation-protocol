import itertools, json, sys, numpy as np, pandas as pd
from multiprocessing import Pool
import ivp
from ivp import dgp, protocol as P
ICS=[0,0.0025,0.005,0.01,0.02]; NS=[5,10,25,50]; YRS=[3,5,10,20]
def job(a):
    ic,n,yr,rho,seed=a
    cell=hash((ic,n,yr,rho))%10**6
    R,X=dgp.simulate(n,252*yr,ic,rho=rho,seed=seed*1000003+int(ic*1e4)*101+n*7+yr*13+int(rho*10))
    o=P.evaluate(R,X); row=dict(ic=ic,n=n,years=yr,rho=rho,seed=seed,t_cw=o['t_cw'],p_cw=o['p_cw'],p_dm=o['p_dm'],oos_r2=o['oos_r2'])
    if ic==0: row['p_naive']=P.naive_pooled_ttest(R,X)['p']
    return row
if __name__=="__main__":
    jobs=[(ic,n,yr,0.3,s) for ic,n,yr in itertools.product(ICS,NS,YRS) for s in range(500 if ic==0 else 200)]
    jobs+=[(ic,25,10,rho,s) for ic in [0,0.005,0.01] for rho in [0.0,0.6] for s in range(200)]
    with Pool(8) as p: rows=p.map(job,jobs,chunksize=20)
    pd.DataFrame(rows).to_csv("results_ivp/power_grid.csv",index=False); print("done",len(rows))
