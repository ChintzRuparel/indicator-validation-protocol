"""Time-series splitting: untouched holdout, anchored walk-forward, purged K-fold with embargo.
All splits are by DATE (panel-safe): every ticker on a date falls in the same fold.

Purging (Lopez de Prado 2018, ch.7 idea): a training row t is dropped if its label window
[t+1, label_end_date_t] overlaps the test date range. Embargo: additionally drop training
rows whose decision date falls within `embargo` business days AFTER the test range.
"""
from __future__ import annotations
import numpy as np
import pandas as pd


def holdout_split(df: pd.DataFrame, frac: float = 0.2, gap_days: int | None = None):
    """Return (dev, holdout). The last `frac` of dates is the untouched holdout.
    Dev rows whose label window reaches into the holdout are purged."""
    dates = np.sort(df["date"].unique())
    cut = dates[int(len(dates) * (1 - frac))]
    dev = df[(df["date"] < cut) & (df["label_end_date"] < cut)]
    hold = df[df["date"] >= cut]
    return dev.copy(), hold.copy(), pd.Timestamp(cut)


def _purge(train_mask, df, t0, t1, embargo_days):
    lab_end = df["label_end_date"]
    d = df["date"]
    overlap = (d <= t1) & (lab_end >= t0)              # label window intersects [t0,t1]
    emb_end = t1 + pd.offsets.BDay(embargo_days)
    embargoed = (d > t1) & (d <= emb_end)
    return train_mask & ~overlap & ~embargoed & lab_end.notna()


def walk_forward(df: pd.DataFrame, n_splits: int = 5, min_train_frac: float = 0.4,
                 embargo_days: int = 5):
    """Anchored expanding-window walk-forward. Yields (train_idx, test_idx)."""
    dates = np.sort(df["date"].unique())
    start = int(len(dates) * min_train_frac)
    edges = np.linspace(start, len(dates), n_splits + 1).astype(int)
    for a, b in zip(edges[:-1], edges[1:]):
        t0, t1 = pd.Timestamp(dates[a]), pd.Timestamp(dates[b - 1])
        test = (df["date"] >= t0) & (df["date"] <= t1)
        train = _purge(df["date"] < t0, df, t0, t1, embargo_days)
        yield np.flatnonzero(train.to_numpy()), np.flatnonzero(test.to_numpy())


def purged_kfold(df: pd.DataFrame, k: int = 5, embargo_days: int = 5):
    """Purged K-fold with embargo (for hyper-parameter selection inside dev only)."""
    dates = np.sort(df["date"].unique())
    edges = np.linspace(0, len(dates), k + 1).astype(int)
    for a, b in zip(edges[:-1], edges[1:]):
        t0, t1 = pd.Timestamp(dates[a]), pd.Timestamp(dates[b - 1])
        test = (df["date"] >= t0) & (df["date"] <= t1)
        train = _purge(~test, df, t0, t1, embargo_days)
        yield np.flatnonzero(train.to_numpy()), np.flatnonzero(test.to_numpy())


def calib_split(train_df: pd.DataFrame, frac: float = 0.2, embargo_days: int = 5):
    """Split a TRAIN set into (fit, calibrate) by time, purged; calibrator never sees test."""
    dates = np.sort(train_df["date"].unique())
    cut = pd.Timestamp(dates[int(len(dates) * (1 - frac))])
    cal = train_df["date"] >= cut
    fit = (train_df["date"] < cut) & (train_df["label_end_date"] < cut)
    return np.flatnonzero(fit.to_numpy()), np.flatnonzero(cal.to_numpy())
