"""Technical features and labels. Every feature at row t uses bars <= t only.

Timing convention (documented in scope.md):
  - Features/rules/tags are computed at the CLOSE of day t.
  - Position is entered at the OPEN of t+1 and exited at the OPEN of t+1+h.
  - Label y_t = 1[ open_{t+1+h} / open_{t+1} > 1 ], fwd_ret_t = log of that ratio.
  - Label window for row t spans days [t+1, t+1+h]; used by purging.
"""
from __future__ import annotations
import numpy as np
import pandas as pd


def _per_ticker(df: pd.DataFrame, fn) -> pd.DataFrame:
    parts = [fn(g.copy()) for _, g in df.groupby("ticker", sort=False)]
    return pd.concat(parts).sort_values(["ticker", "date"]).reset_index(drop=True)


def _rsi(close: pd.Series, n: int = 14) -> pd.Series:
    d = close.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + up / dn.replace(0, np.nan))


TECH_FEATURES = ["ret_1", "ret_5", "ret_20", "vol_20", "ma_gap_20_100", "rsi_14",
                 "range_z", "vol_z", "dist_hi_55", "dist_lo_55"]


def add_technical(df: pd.DataFrame) -> pd.DataFrame:
    def f(g):
        c, lc = g["close"], np.log(g["close"])
        g["ret_1"] = lc.diff()
        g["ret_5"] = lc.diff(5)
        g["ret_20"] = lc.diff(20)
        g["vol_20"] = g["ret_1"].rolling(20).std()
        g["ma_gap_20_100"] = c.rolling(20).mean() / c.rolling(100).mean() - 1
        g["rsi_14"] = _rsi(c)
        rng_ = np.log(g["high"] / g["low"])
        g["range_z"] = (rng_ - rng_.rolling(60).mean()) / rng_.rolling(60).std()
        lv = np.log(g["volume"])
        g["vol_z"] = (lv - lv.rolling(60).mean()) / lv.rolling(60).std()
        g["dist_hi_55"] = c / g["high"].rolling(55).max() - 1
        g["dist_lo_55"] = c / g["low"].rolling(55).min() - 1
        return g
    return _per_ticker(df, f)


def add_labels(df: pd.DataFrame, horizon: int = 5) -> pd.DataFrame:
    def f(g):
        o = g["open"]
        entry, exitp = o.shift(-1), o.shift(-1 - horizon)
        g["fwd_ret"] = np.log(exitp / entry)
        g["y"] = (g["fwd_ret"] > 0).astype(float).where(g["fwd_ret"].notna())
        # integer position of last day touched by the label (for purging)
        g["label_end_date"] = g["date"].shift(-1 - horizon)
        # 1-day realized return used by the decision layer: position decided at close t,
        # held from open t+1 to open t+2 (no overlap between consecutive daily P&L).
        g["ret_next"] = np.log(o.shift(-2) / o.shift(-1))
        return g
    out = _per_ticker(df, f)
    out.attrs["horizon"] = horizon
    return out
