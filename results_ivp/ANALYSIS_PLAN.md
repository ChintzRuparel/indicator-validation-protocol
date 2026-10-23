# Pre-registered analysis plan — IVP (Paper 6 pivot). Frozen 2026-10-22 before any synthetic grid or real-data run.

## Primary test (applies to every candidate indicator)
- Target: h-day forward log return, h=5 (primary); h=21 (secondary, reported, not confirmatory).
- Expanding walk-forward, train_min=252 dates, test blocks 126 dates, purge = h dates. Winsorise (1/99%) and
  standardise x with training statistics only. Benchmark: training mean; augmented: pooled OLS y ~ 1 + x.
- Statistic: Clark–West adjusted MSPE difference, averaged across tickers per date, Newey–West HAC lag
  max(h, ceil(4(n/100)^(2/9))), one-sided, alpha=0.05. Reported also: DM t, OOS R^2.
- Family of real indicators: Holm adjustment across the 6 classic indicators at h=5.

## Synthetic study (DGP in ivp/dgp.py: AR(1) phi=0.95 indicator, t(5) shocks, GARCH(0.02,0.08,0.90), common factor rho)
- Grid: IC in {0, 0.0025, 0.005, 0.01, 0.02} x N tickers in {5,10,25,50} x years in {3,5,10,20} (252 d/yr), rho=0.3.
  Seeds: 500 per cell for IC=0 (size), 200 per cell otherwise (power). Seeds are 0..S-1, cell-offset deterministic.
- Size claim: protocol is acceptable if null rejection rate's 95% Wilson CI includes 0.05 or lies below it.
  Also report naive pooled iid-SE t-test rejection rate in the same null cells.
- Sensitivity: rho in {0, 0.3, 0.6} at N=25, 10 years, IC in {0, 0.005, 0.01}, 200 seeds.
- "How much data": for each N and IC, smallest years in grid reaching power >= 0.8.

## Leakage demonstrations (null DGP, IC=0, N=10, 5 years, 200 seeds unless stated)
- L1 overlapping labels + iid SE (naive pooled t-test) vs protocol.
- L2 look-ahead indicators (centered MA, full-sample z-score, next-day) : truncation PIT audit flag rate vs classic indicators; plus protocol rejection rate with the leaky feature on real ETF prices.
- L3 random (shuffled) 5-fold CV with a kNN(k=50) regressor on [x, lagged 20d return] vs purged walk-forward, null DGP, 100 seeds: OOS R^2 distribution and fraction > 0.
- L4 specification search: best of 20 lookbacks of a momentum-type indicator chosen by minimum p, unadjusted vs Holm, null DGP built on real-like noise, 200 seeds.

## Real-data application (run ONCE after this file is hashed)
- Universe: the 38-ETF set frozen for Paper 3 (paper3/wide/UNIVERSE_FROZEN.md), Yahoo adjusted close, free.
- Indicators: RSI14, MACDhist (normalised by price), MOM12_1, REV1M, RVOL21, MA200gap (ivp/indicators.py). All pass PIT audit first.
- Development: 2001-01-01..2019-12-31. Holdout: 2020-01-01..end of data, unlocked once after dev results written.
  In the holdout, models are trained on all data up to each test block (walk-forward continues); only test dates >= 2020 are scored.
- No indicator, parameter, or universe change after seeing results. Expected: classic indicators largely fail; that is a valid outcome.
