"""Power curve figure from code/results/power/power_runs.csv (no hand-entered numbers)."""
import pandas as pd, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
D = pd.read_csv("../results/power/power_runs.csv")
fig, ax = plt.subplots(1, 3, figsize=(9, 2.8), sharey=True)
for j, h in enumerate(["H1", "H3a", "H3b"]):
    for d, m in [(1200, "o-"), (2400, "s-")]:
        x = D[D.n_days == d].groupby("n_tickers")[h].mean()
        ax[j].plot(x.index, x.values, m, label=f"{d} days")
    ax[j].set_title(h, fontsize=9); ax[j].set_xticks([6, 12, 24]); ax[j].set_xlabel("tickers"); ax[j].set_ylim(-0.05, 1.05)
ax[0].set_ylabel("share of seeds, Holm p<0.05"); ax[0].legend(fontsize=7); plt.tight_layout(); plt.savefig("fig_powercurve.pdf")
