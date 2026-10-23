import pandas as pd, numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
d=pd.read_csv(__import__("os").environ.get("GRID", "../results_ivp/power_grid.csv")); m=d[d.rho==0.3].copy(); m["rej"]=m.p_cw<0.05
fig,ax=plt.subplots(1,4,figsize=(12,3),sharey=True)
for a,n in zip(ax,[5,10,25,50]):
    for ic in [0,0.0025,0.005,0.01,0.02]:
        g=m[(m.n==n)&(m.ic==ic)].groupby("years").rej.mean(); a.plot(g.index,g.values,marker="o",label=f"IC={ic}")
    a.axhline(.8,ls=":",c="k"); a.axhline(.05,ls="--",c="grey"); a.set_title(f"N={n} tickers"); a.set_xlabel("years of history"); a.set_xscale("log"); a.set_xticks([3,5,10,20]); a.set_xticklabels([3,5,10,20])
ax[0].set_ylabel("rejection rate (one-sided 5%)"); ax[-1].legend(fontsize=7); plt.tight_layout(); plt.savefig(__import__("os").path.join(__import__("os").environ.get("PAPER_OUT", "."), "fig_ivp_power.pdf"))
