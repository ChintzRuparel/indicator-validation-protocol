#!/usr/bin/env python3
"""Download the 38 frozen ETFs (UNIVERSE_FROZEN.md) from Yahoo via yfinance into data/prices/<SYM>.csv.
Yahoo data are for personal use; they are not redistributed with this repo.
End date is pinned to the paper's data (bars through 2026-10-20; yfinance `end` is exclusive)."""
import argparse, os, pandas as pd, yfinance as yf
ap = argparse.ArgumentParser(); ap.add_argument("--out", default="data/prices")
ap.add_argument("--start", default="2000-01-01"); ap.add_argument("--end", default="2026-10-21")
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
syms = open(os.path.join(os.path.dirname(__file__), "..", "UNIVERSE_FROZEN.md")).read().split("Symbols (38):")[1].split()[:38]
for s in syms:
    df = yf.download(s, start=a.start, end=a.end, auto_adjust=False, progress=False)
    if df.empty: raise SystemExit(f"no data for {s}")
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    df.reset_index().to_csv(os.path.join(a.out, f"{s}.csv"), index=False); print("saved", s, len(df))
