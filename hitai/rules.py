"""Frozen human hypothesis rules (the 'Human-Informed' part).

Rules are written BEFORE looking at any evaluation data and frozen by hash.
Changing any rule changes RULES_VERSION; results must report it.
Each rule outputs a vote in {-1, 0, +1} using only bars <= t.
"""
from __future__ import annotations
import hashlib
import inspect
import numpy as np
import pandas as pd


def r_trend(g):        # H-rule 1: medium-term trend persistence
    return np.sign(g["ma_gap_20_100"]).fillna(0)


def r_meanrev(g):      # H-rule 2: short-term oversold/overbought reversal
    return pd.Series(np.where(g["rsi_14"] < 30, 1, np.where(g["rsi_14"] > 70, -1, 0)), index=g.index)


def r_breakout(g):     # H-rule 3: 55-day breakout (Donchian)
    return pd.Series(np.where(g["dist_hi_55"] >= -1e-12, 1, np.where(g["dist_lo_55"] <= 1e-12, -1, 0)), index=g.index)


def r_volconfirm(g):   # H-rule 4: abnormal volume confirms the 5-day move
    return (np.sign(g["ret_5"]) * (g["vol_z"] > 1)).fillna(0)


RULES = {"rule_trend": r_trend, "rule_meanrev": r_meanrev,
         "rule_breakout": r_breakout, "rule_volconfirm": r_volconfirm}
RULE_FEATURES = list(RULES)
RULES_VERSION = hashlib.sha256("".join(inspect.getsource(f) for f in RULES.values()).encode()).hexdigest()[:12]


def add_rules(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for name, fn in RULES.items():
        out[name] = fn(out).astype(float)
    out["rule_vote"] = out[RULE_FEATURES].sum(axis=1)
    return out
