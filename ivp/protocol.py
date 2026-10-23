"""Leakage-safe, nested out-of-sample test of whether a candidate indicator adds predictive value.

Target y[t,i] = sum_{k=1..h} r[t+k,i]. Indicator x[t,i] uses data <= t only (audited separately).
Expanding walk-forward: test blocks of `test_size` dates; training set = dates whose label window ends
before the first test date (purge of h dates). Within each fold, x is winsorised/standardised with
training statistics only. Benchmark = training mean of y (constant); augmented = pooled OLS y ~ 1 + x.
Losses are averaged across tickers per date (handles cross-sectional dependence); the primary statistic is
the Clark-West (2007) adjusted MSPE difference with Newey-West HAC standard error, one-sided.
"""
import math, warnings
warnings.filterwarnings("ignore", message="Mean of empty slice")
import numpy as np
from scipy import stats

def forward_sum(R, h):
    T, N = R.shape
    c = np.vstack([np.zeros((1, N)), np.nancumsum(np.nan_to_num(R), axis=0)])
    y = np.full((T, N), np.nan)
    y[: T - h] = c[h + 1 : T + 1] - c[1 : T - h + 1]
    # invalidate windows touching missing returns
    m = np.isnan(R).astype(float)
    cm = np.vstack([np.zeros((1, N)), np.cumsum(m, axis=0)])
    bad = np.full((T, N), True)
    bad[: T - h] = (cm[h + 1 : T + 1] - cm[1 : T - h + 1]) > 0
    y[bad] = np.nan
    return y

def nw_lag(n, h):
    return int(max(h, math.ceil(4 * (n / 100.0) ** (2.0 / 9.0))))

def hac_tstat(d, lag):
    d = np.asarray(d, float); d = d[np.isfinite(d)]
    n = len(d); mu = d.mean(); e = d - mu
    s = e @ e / n
    for k in range(1, lag + 1):
        s += 2 * (1 - k / (lag + 1)) * (e[k:] @ e[:-k]) / n
    se = math.sqrt(max(s, 1e-300) / n)
    return mu / se, n

def folds(T, train_min, test_size, h):
    out = []; start = train_min
    while start < T - h:
        end = min(start + test_size, T - h)
        tr_end = start - h  # labels of train rows end at <= start-1
        if tr_end > 20:
            out.append((tr_end, start, end))
        start = end
    return out

def _std_fit(x):
    lo, hi = np.nanpercentile(x, [1, 99])
    xc = np.clip(x, lo, hi); return lo, hi, np.nanmean(xc), np.nanstd(xc) + 1e-12

def evaluate(R, X, h=5, train_min=252, test_size=126, return_series=False, score_from=0):
    """X: T x N indicator. Returns dict with CW t, one-sided p, DM t, OOS R2, IC."""
    y = forward_sum(R, h)
    T, N = R.shape
    pb = np.full((T, N), np.nan); pa = np.full((T, N), np.nan)
    for tr_end, s, e in folds(T, train_min, test_size, h):
        xt, yt = X[:tr_end], y[:tr_end]
        ok = np.isfinite(xt) & np.isfinite(yt)
        if ok.sum() < 30: continue
        lo, hi, m, sd = _std_fit(xt[ok])
        z = (np.clip(xt[ok], lo, hi) - m) / sd; yy = yt[ok]
        mu = yy.mean()
        beta = ((z - z.mean()) @ (yy - mu)) / ((z - z.mean()) @ (z - z.mean()) + 1e-12)
        alpha = mu - beta * z.mean()
        zs = (np.clip(X[s:e], lo, hi) - m) / sd
        pb[s:e] = mu; pa[s:e] = alpha + beta * zs
    ok = np.isfinite(pb) & np.isfinite(pa) & np.isfinite(y)
    ok[:score_from] = False  # holdout scoring: only dates >= score_from
    eb = np.where(ok, (y - pb) ** 2, np.nan); ea = np.where(ok, (y - pa) ** 2, np.nan)
    adj = np.where(ok, (pb - pa) ** 2, np.nan)
    rows = ok.any(axis=1)
    cw = np.nanmean(eb - (ea - adj), axis=1)[rows]
    dm = np.nanmean(eb - ea, axis=1)[rows]
    lag = nw_lag(rows.sum(), h)
    t_cw, n = hac_tstat(cw, lag); t_dm, _ = hac_tstat(dm, lag)
    r2 = 1 - np.nansum(ea) / np.nansum(eb)
    # per-date cross-sectional IC is undefined for N<3; use pooled corr of forecast with outcome
    out = dict(t_cw=t_cw, p_cw=1 - stats.norm.cdf(t_cw), t_dm=t_dm, p_dm=1 - stats.norm.cdf(t_dm),
               oos_r2=r2, n_dates=int(n), n_obs=int(ok.sum()), lag=lag)
    if return_series: out["cw_series"] = cw
    return out

def naive_pooled_ttest(R, X, h=5):
    """Common shortcut: full-sample pooled OLS of overlapping h-day y on x, iid OLS standard errors."""
    y = forward_sum(R, h); ok = np.isfinite(X) & np.isfinite(y)
    x = X[ok]; yy = y[ok]
    xc = x - x.mean(); b = xc @ (yy - yy.mean()) / (xc @ xc)
    res = yy - yy.mean() - b * xc
    se = math.sqrt((res @ res) / (len(yy) - 2) / (xc @ xc))
    t = b / se
    return dict(t=t, p=1 - stats.norm.cdf(t))

def holm(p):
    p = np.asarray(p, float); m = len(p); o = np.argsort(p); adj = np.empty(m); run = 0
    for k, i in enumerate(o):
        run = max(run, min(1.0, (m - k) * p[i])); adj[i] = run
    return adj
