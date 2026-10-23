"""Classic indicators computed from adjusted close up to and including day t (point-in-time)."""
import numpy as np, pandas as pd

def rsi(close, n=14):
    d = close.diff(); up = d.clip(lower=0); dn = (-d).clip(lower=0)
    au = up.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()
    return 100 - 100 / (1 + au / ad)

def macd_hist(close, f=12, s=26, sig=9):
    m = close.ewm(span=f, adjust=False, min_periods=s).mean() - close.ewm(span=s, adjust=False, min_periods=s).mean()
    return (m - m.ewm(span=sig, adjust=False, min_periods=sig).mean()) / close

def momentum_12_1(close):
    return np.log(close.shift(21) / close.shift(252))

def reversal_1m(close):
    return -np.log(close / close.shift(21))

def realized_vol(close, n=21):
    return np.log(close).diff().rolling(n, min_periods=n).std() * np.sqrt(252)

def ma200_gap(close):
    return np.log(close / close.rolling(200, min_periods=200).mean())

CLASSIC = {"RSI14": rsi, "MACDhist": macd_hist, "MOM12_1": momentum_12_1,
           "REV1M": reversal_1m, "RVOL21": realized_vol, "MA200gap": ma200_gap}

# Deliberately leaky constructions used only in the leakage-detection demonstrations
def leaky_centered_ma_gap(close, n=10):
    return np.log(close / close.rolling(2 * n + 1, center=True, min_periods=2 * n + 1).mean())

def leaky_fullsample_z(close):
    r = np.log(close).diff(); return (r.rolling(5).sum() - r.mean()) / r.std()  # full-sample stats

def leaky_next_day(close):
    return np.log(close).diff().shift(-1).rolling(5, min_periods=1).mean()

LEAKY = {"centeredMA": leaky_centered_ma_gap, "fullsampleZ": leaky_fullsample_z, "nextDay": leaky_next_day}

def pit_audit(fn, close, n_checks=25, seed=0, min_hist=300, tol=1e-9):
    """Truncation audit: indicator at t computed on close[:t+1] must equal value computed on the full series.
    Returns fraction of checked dates with mismatch (0 => no look-ahead detected)."""
    rng = np.random.default_rng(seed)
    full = fn(close)
    idx = rng.choice(np.arange(min_hist, len(close) - 30), size=n_checks, replace=False)
    bad = 0
    for t in idx:
        v_full = full.iloc[t]; v_tr = fn(close.iloc[: t + 1]).iloc[-1]
        if (np.isnan(v_full) != np.isnan(v_tr)) or (np.isfinite(v_full) and abs(v_full - v_tr) > tol * (1 + abs(v_full))):
            bad += 1
    return bad / n_checks
