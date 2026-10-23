"""Data loading. Synthetic generator for smoke runs + CSV loader for real OHLCV.

Panel format: long DataFrame with columns
  date (datetime64), ticker (str), open, high, low, close, volume
sorted by (ticker, date). One row = one bar, known at that bar's close.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

REQUIRED = ["date", "ticker", "open", "high", "low", "close", "volume"]


def synthetic_panel(n_tickers: int = 8, n_days: int = 1500, seed: int = 0,
                    signal_strength: float = 0.02) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Regime-switching GBM-like panel with a *weak*, *point-in-time* predictable component.

    Returns (ohlcv, news) where `news` is a latent daily 'news sentiment' observed at
    the close of day t (it is public at t). It weakly predicts the t+1.. drift, so an
    honest point-in-time tagger that reads it can add (small) information. This lets
    the smoke run exercise H3 without any real LLM. Effect sizes are synthetic and
    carry NO implication about real markets.
    """
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range("2012-01-02", periods=n_days)
    rows, news_rows = [], []
    for k in range(n_tickers):
        tk = f"SYN{k:02d}"
        regime = 0
        price = 100.0
        news_prev = 0.0
        for t, d in enumerate(dates):
            if rng.random() < 0.01:
                regime = 1 - regime
            vol = 0.01 if regime == 0 else 0.02
            news = 0.7 * news_prev + rng.normal(0, 1)
            # drift for day t depends on news observed at t-1 (public before t's open)
            drift = signal_strength * vol * np.tanh(news_prev)
            ret = drift + vol * rng.standard_t(5) / np.sqrt(5 / 3)
            o = price * np.exp(rng.normal(0, vol / 4))
            c = price * np.exp(ret)
            hi = max(o, c) * np.exp(abs(rng.normal(0, vol / 2)))
            lo = min(o, c) * np.exp(-abs(rng.normal(0, vol / 2)))
            v = rng.lognormal(13, 0.3) * (1.5 if regime else 1.0)
            rows.append((d, tk, o, hi, lo, c, v))
            news_rows.append((d, tk, news))
            price, news_prev = c, news
    df = pd.DataFrame(rows, columns=REQUIRED)
    nw = pd.DataFrame(news_rows, columns=["date", "ticker", "news"])
    return df, nw


def load_csv(path: str) -> pd.DataFrame:
    """Load a long-format OHLCV CSV (columns: REQUIRED). Prices must be split/dividend
    adjusted *as of each date* or raw+adjustment factors; survivorship-free universe is
    the user's responsibility."""
    df = pd.read_csv(path, parse_dates=["date"])
    missing = set(REQUIRED) - set(df.columns)
    if missing:
        raise ValueError(f"missing columns: {missing}")
    df = df.sort_values(["ticker", "date"]).reset_index(drop=True)
    if df.duplicated(["ticker", "date"]).any():
        raise ValueError("duplicate (ticker,date) rows")
    return df
