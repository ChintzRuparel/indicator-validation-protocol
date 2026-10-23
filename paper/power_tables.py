"""Size and power tables of the paper (rejection rates by cell) from results_ivp/power_grid.csv.
Usage: python paper/power_tables.py [grid.csv] [out.csv]"""
import sys, pandas as pd
g = sys.argv[1] if len(sys.argv) > 1 else "results_ivp/power_grid.csv"
out = sys.argv[2] if len(sys.argv) > 2 else "results/paper/power_summary.csv"
d = pd.read_csv(g); d["rej_cw"] = d.p_cw < 0.05
agg = {"rej_cw": "mean", "seed": "count"}
if "p_naive" in d: d["rej_naive"] = d.p_naive < 0.05; agg["rej_naive"] = "mean"
t = d.groupby(["ic", "n", "years", "rho"]).agg(agg).rename(columns={"seed": "reps"}).reset_index().round(4)
t.to_csv(out, index=False); print(t.to_string(index=False))
