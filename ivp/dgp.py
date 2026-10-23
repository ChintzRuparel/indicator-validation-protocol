"""Synthetic panel with a planted indicator of known daily information coefficient (IC)."""
import numpy as np

def simulate(n_tickers, n_days, ic, rho=0.3, phi=0.95, df=5, garch=(0.02, 0.08, 0.90), seed=0, burn=250):
    """Return (R, X): log returns R[t,i] (T x N) and indicator X[t,i] known at close of t.
    r[t+1,i] = b * x[t,i] + sigma[t+1,i] * e[t+1,i];  e = sqrt(rho) f + sqrt(1-rho) u, f,u ~ std t(df).
    x is AR(1) (phi) with unit variance, independent across tickers. b chosen so corr(x_t, r_{t+1}) ~= ic.
    """
    rng = np.random.default_rng(seed)
    T = n_days + burn; N = n_tickers
    def std_t(size):
        z = rng.standard_t(df, size=size)
        return z / np.sqrt(df / (df - 2))
    x = np.zeros((T, N)); x[0] = rng.standard_normal(N)
    sx = np.sqrt(1 - phi ** 2)
    for t in range(1, T):
        x[t] = phi * x[t - 1] + sx * rng.standard_normal(N)
    f = std_t(T); u = std_t((T, N))
    e = np.sqrt(rho) * f[:, None] + np.sqrt(1 - rho) * u
    w, a, g = garch
    h = np.full(N, w / (1 - a - g)); sig = np.zeros((T, N))
    for t in range(T):
        sig[t] = np.sqrt(h)
        h = w + a * (sig[t] * e[t]) ** 2 + g * h
    sig = sig / np.sqrt(w / (1 - a - g))  # unconditional unit variance
    ic = float(ic)
    b = ic / np.sqrt(max(1e-12, 1 - ic ** 2))
    r = np.zeros((T, N))
    r[1:] = b * x[:-1] + sig[1:] * e[1:]
    r = r * 0.01  # ~1% daily vol
    return r[burn:], x[burn:]
