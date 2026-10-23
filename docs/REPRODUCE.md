# HITAI reference implementation

Research code for the HITAI paper. **No profitability claims.** The synthetic smoke run only checks that the pipeline works and that the tests have power. It says nothing about markets.

## Layout
```
hitai/data.py        synthetic panel (+ PIT 'news' series) and CSV loader
hitai/features.py    technical features (bars <= t) and labels (next-open entry, h-day horizon)
hitai/rules.py       4 frozen human rules, RULES_VERSION hash
hitai/llm_tags.py    schema-constrained PIT tags, JSONL cache, masking, shuffle/lag ablations,
                     honest mock, deliberately-leaky mock (positive control), RealLLMTagger stub
hitai/cv.py          untouched holdout, purged walk-forward, purged K-fold + embargo, calib split
hitai/models.py      L2-logit / GBT / monotone GBT + isotonic calibration (train-only)
hitai/stats.py       logloss, Brier, ECE, AUC, Spiegelhalter, Sharpe/PSR/DSR, max DD,
                     White RC + Hansen SPA (stationary bootstrap), DM, Bonferroni/Holm/BH
hitai/experiment.py  end-to-end runner (CLI)
tests/test_hitai.py  18 leakage / correctness tests
```

## Setup (Python ≥ 3.10; tested with 3.13)
```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```
`hitai/__init__.py` sets `OMP_NUM_THREADS=1`. On the development VM, scikit-learn's HistGradientBoosting hung with multithreaded OpenMP. Single-threaded runs are also deterministic.

## Exact run commands
```bash
# 1) tests (≈10 s)
python -m pytest -q tests

# 2) smoke run with planted PIT signal + leaky positive control + one-shot holdout (≈20 s)
python -m hitai.experiment --n-tickers 6 --n-days 1200 --leaky-demo --unlock-holdout --out results/smoke

# 3) null smoke run: no signal; confirmatory tests should NOT be significant (≈15 s)
python -m hitai.experiment --n-tickers 6 --n-days 1200 --signal 0 --out results/smoke_null

# 4) real data (supply your own OHLCV CSV). DEV ONLY first:
python -m hitai.experiment --data /path/ohlcv_long.csv --out results/real_dev
#    cost sensitivity (dev only)
for c in 0 5 10 20 50; do python -m hitai.experiment --data /path/ohlcv_long.csv --cost-bps $c --out results/real_dev_c$c; done
#    ONE-SHOT holdout, only after the analysis plan is frozen:
python -m hitai.experiment --data /path/ohlcv_long.csv --unlock-holdout --out results/real_final
```
Real-data CSV format is long, with columns `date,ticker,open,high,low,close,volume`, one row per ticker per day, and adjusted prices. With `--data <csv>` there is no news series yet, so the mock tagger emits seeded noise tags plus a volatility-derived `regime` tag (H3/H4 are not informative about news; a significant H3b on real data can come from the vol-based regime field) until `RealLLMTagger` is implemented and `news` text is supplied.

## Expected outputs (in `--out`)
| file | content |
|---|---|
| `metrics_dev.csv` | one row per config (feature set × tag variant × model): logloss, Brier, ECE (calibrated and raw), AUC, gross/net Sharpe, PSR, DSR, max DD, turnover, `n_trials` |
| `hypothesis_tests.csv` | H1–H4 statistics, one-sided p-values, Holm/Bonferroni (confirmatory family), BH (all) |
| `reality_check_spa.csv` | White RC and Hansen SPA p-values vs `rules_only` |
| `holdout_metrics.csv` + `HOLDOUT_USED.lock` | only with `--unlock-holdout` |
| `run_manifest.json` | rules hash, tagger version, cache hits, package versions, data hash, all args |
| `REPORT.md` | human-readable summary |
| `tag_cache/*.jsonl` | versioned tag cache (archive with the paper) |

### Smoke results obtained on the build VM (20 Oct 2026, seed 0, synthetic)
- Planted-signal run: H3a p=0.008 and H3b p=0.008 (Holm 0.038 each), so the tags beat both no-tags and shuffled tags. H3c (lagged) Holm p=0.28. H1 (vs rules_only) was not supported. H2a rejected calibration (z=2.95), so the isotonic calibration on a small sample is imperfect. The leaky positive control was flagged: corr(tag, fwd) was 0.87 unmasked, 0.20 masked and 0.87 under perturbation. The honest tagger's corr under perturbation was ≈0.
- Null run (`--signal 0`): no confirmatory test significant (min Holm p=0.94); RC p=0.84, SPA p=0.12.

These are synthetic and say nothing about markets.

