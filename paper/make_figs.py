"""Figures from code/results (no hand-entered numbers)."""
import pandas as pd, numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2, figsize=(9, 3.2))
H = ["H1", "H2b", "H3a", "H3b", "H3c"]
for j, k in enumerate(["smoke", "null"]):
    P = np.array([[pd.read_csv(f"../results/{k}_s{s}/hypothesis_tests.csv").query("model=='gbt_mono' and hypothesis==@h").p_holm.iloc[0] for h in H] for s in range(5)])
    for s in range(5):
        ax[j].scatter(np.arange(5) + 0.08 * (s - 2), P[s], s=18, label=f"seed {s}")
    ax[j].axhline(0.05, color="r", ls="--", lw=0.8); ax[j].set_xticks(range(5)); ax[j].set_xticklabels(H); ax[j].set_ylim(-0.03, 1.05)
    ax[j].set_title({"smoke": "planted signal (0.25)", "null": "null (signal 0)"}[k], fontsize=9); ax[j].set_ylabel("Holm-adjusted p (gbt_mono)")
ax[0].legend(fontsize=6); plt.tight_layout(); plt.savefig("fig_power.pdf")
