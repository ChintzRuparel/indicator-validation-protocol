"""Evaluation statistics: forecast quality, calibration, Sharpe inference,
data-snooping-robust tests, and multiple-testing control."""
from __future__ import annotations
import numpy as np
from scipy import stats as st


def brier(p, y):
    return float(np.mean((p - y) ** 2))


def log_loss(p, y, eps=1e-6):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def ece(p, y, bins=10):
    b = np.minimum((p * bins).astype(int), bins - 1)
    return float(sum(abs(p[b == i].mean() - y[b == i].mean()) * (b == i).mean()
                     for i in range(bins) if (b == i).any()))


def auc(p, y):
    r = st.rankdata(p)
    n1 = y.sum(); n0 = len(y) - n1
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)) if n1 and n0 else np.nan


def sharpe(r, periods=252):
    r = np.asarray(r, float)
    s = r.std(ddof=1)
    return float(r.mean() / s * np.sqrt(periods)) if s > 0 else 0.0


def psr(r, sr_star=0.0):
    """Probabilistic Sharpe ratio (per-period SR; Bailey & Lopez de Prado)."""
    r = np.asarray(r, float); n = len(r)
    sd = r.std(ddof=1) if n > 1 else 0.0
    if not np.isfinite(sd) or sd == 0:
        return float("nan")             # flat strategy: PSR undefined
    sr = r.mean() / sd
    g3, g4 = st.skew(r), st.kurtosis(r, fisher=False)
    den = np.sqrt(max(1e-12, 1 - g3 * sr + (g4 - 1) / 4 * sr ** 2))
    return float(st.norm.cdf((sr - sr_star) * np.sqrt(n - 1) / den))


def deflated_sharpe(r, sr_trials_var, n_trials):
    """DSR: PSR against the expected max SR of n_trials under the null
    (Bailey & Lopez de Prado 2014, JPM). sr_trials_var = variance of per-period SRs across trials."""
    emc = 0.5772156649
    if n_trials < 2:
        return psr(r, 0.0)
    sr0 = np.sqrt(sr_trials_var) * ((1 - emc) * st.norm.ppf(1 - 1 / n_trials)
                                    + emc * st.norm.ppf(1 - 1 / (n_trials * np.e)))
    return psr(r, sr0)


def stationary_bootstrap_idx(n, B, mean_block=10, seed=0):
    rng = np.random.default_rng(seed)
    p = 1 / mean_block
    idx = np.empty((B, n), int)
    for b in range(B):
        i = rng.integers(n)
        for t in range(n):
            idx[b, t] = i
            i = rng.integers(n) if rng.random() < p else (i + 1) % n
    return idx


def reality_check_spa(loss_bench, loss_models, B=500, mean_block=10, seed=0):
    """White (2000) RC and Hansen (2005) SPA (consistent version) p-values.
    d_k = loss_bench - loss_model_k (positive = model better). H0: no model beats benchmark."""
    d = loss_bench[:, None] - loss_models          # T x K
    T, K = d.shape
    dbar = d.mean(0)
    idx = stationary_bootstrap_idx(T, B, mean_block, seed)
    boot = np.stack([d[i].mean(0) for i in idx])   # B x K
    omega = np.sqrt(T) * boot.std(0, ddof=1) + 1e-12
    # RC
    stat_rc = np.sqrt(T) * dbar.max()
    rc_null = np.sqrt(T) * (boot - dbar).max(1)
    # SPA_c: recentre only non-binding models
    thr = -np.sqrt(2 * np.log(np.log(T))) * omega / np.sqrt(T)
    mu_c = np.where(dbar >= thr, dbar, 0.0)
    stat_spa = max(0.0, (np.sqrt(T) * dbar / omega).max())
    spa_null = np.maximum(0, (np.sqrt(T) * (boot - mu_c) / omega).max(1))
    return {"rc_p": float((rc_null >= stat_rc).mean()), "spa_p": float((spa_null >= stat_spa).mean())}


def bonferroni(p):
    p = np.asarray(p, float)
    return np.minimum(1, p * len(p))


def benjamini_hochberg(p):
    p = np.asarray(p, float); m = len(p)
    o = np.argsort(p)
    q = p[o] * m / np.arange(1, m + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    out = np.empty(m); out[o] = np.minimum(q, 1)
    return out


def diebold_mariano(l1, l2, h=1):
    """DM test on loss differential l1-l2 with Newey-West(h-1) variance. Returns (stat, two-sided p)."""
    d = np.asarray(l1) - np.asarray(l2); T = len(d)
    dc = d - d.mean()
    v = dc @ dc / T
    for k in range(1, h):
        v += 2 * (1 - k / h) * (dc[k:] @ dc[:-k]) / T
    s = d.mean() / np.sqrt(v / T)
    return float(s), float(2 * (1 - st.norm.cdf(abs(s))))


def spiegelhalter_z(p, y):
    """Spiegelhalter (1986) calibration test; H0: forecasts calibrated. Returns (z, two-sided p).
    NOTE: assumes independent outcomes; with overlapping labels use as descriptive only
    or apply to non-overlapping subsample (every h-th date)."""
    p = np.clip(np.asarray(p, float), 1e-6, 1 - 1e-6); y = np.asarray(y, float)
    num = np.sum((y - p) * (1 - 2 * p))
    den = np.sqrt(np.sum((1 - 2 * p) ** 2 * p * (1 - p)))
    z = num / den
    return float(z), float(2 * (1 - st.norm.cdf(abs(z))))


def holm(p):
    p = np.asarray(p, float); m = len(p); o = np.argsort(p)
    adj = np.maximum.accumulate((m - np.arange(m)) * p[o])
    out = np.empty(m); out[o] = np.minimum(adj, 1)
    return out


def max_drawdown(r):
    """Max drawdown of cumulative log-return path (returned as a negative number)."""
    c = np.cumsum(np.asarray(r, float))
    return float((c - np.maximum.accumulate(np.concatenate([[0.0], c]))[1:]).min()) if len(c) else 0.0
