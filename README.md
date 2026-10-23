# How Much Data Do You Need to Validate a Trading Indicator? A Leakage-Safe, Power-Aware Protocol

Code for the paper *How Much Data Do You Need to Validate a Trading Indicator? A Leakage-Safe, Power-Aware Protocol* — Chintz Ruparel (2026). arXiv: **TODO**.

Repository: https://github.com/ChintzRuparel/indicator-validation-protocol

## One command
```bash
bash run_all.sh   # --quick skips the synthetic power grid
```
Runtime: ~5 min full on 4 CPUs (--quick ~1 min). Synthetic results match exactly; real-data results match within 0.3%. Results go to `results/`, and numbers are checked against `paper/reference/` automatically.


## Run and share results
```bash
bash run_all.sh                 # writes everything to results/, ending with results/RESULTS.md
git add results                 # results/ is committed on purpose (raw data, models and >10 MB files are ignored)
git commit -m "Add run results"
git push
```
`results/RESULTS.md` holds the headline numbers behind the paper's tables, the run date, git commit, Python/package versions, input-data sha256 hashes and PASS/DIFF against `paper/reference/`. The full console log is `results/run_log.txt`.

## Abstract
New trading indicators are routinely declared useful on the strength of a single in-sample $t$-statistic, a shuffled cross-validation score or the best of many parameterisations. We specify and stress-test a simple protocol for deciding whether a candidate indicator adds out-of-sample predictive value over the historical mean: a point-in-time truncation audit, purged expanding walk-forward estimation with training-only standardisation, a Clark–West nested-model test on cross-sectionally averaged losses with Newey–West errors, and Holm control over the indicator family, all frozen in a pre-registered plan. In a synthetic panel with fat tails, volatility clustering and cross-sectional correlation (22,000 simulated studies) the protocol holds its nominal size (null rejection 1.6–5.6% across 16 panel shapes, 500 replications each), whereas the common pooled OLS $t$-test on overlapping 5-day returns rejects a useless indicator 19–24% of the time. Power is the binding constraint: an indicator with a daily information coefficient (IC) of 0.01 needs about 10 years of 50 tickers, or 20 years of 25, to be detected with 80% probability; at IC 0.005 no panel in our grid reaches 60%. A truncation audit flags three typical look-ahead constructions in 100% of checks and six classic indicators in 0%; one such leak (a centred moving average) yields an apparent out-of-sample $R^2$ of 0.41 on real ETF data. Applied to RSI, MACD, 12–1 momentum, one-month reversal, realised volatility and the 200-day moving-average gap on 38 liquid ETFs (development 2000–2019, one-shot holdout 2020–2026), no indicator adds predictive value at a 5- or 21-day horizon (all Holm $p=1.0$, all out-of-sample $R^2\le 0.0001$). A semi-synthetic check on the same real returns shows the panel had 83% power for IC 0.01, so the null is informative: these indicators carry less than roughly that much linear predictive content for these assets.

## Setup
Python 3.11+ (tested on 3.13). `requirements.txt` is pinned from a working environment; `requirements-min.txt` lists minimum versions.
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Reproduce
```bash
python -m pytest -q tests                  # ivp + legacy hitai tests
python run_power.py                          # 22k simulated studies -> results_ivp/power_grid.csv (8 processes)
python run_leakage.py                        # truncation audit -> results_ivp/leakage.json
python run_real.py dev                       # needs data/etf_long.csv (see below)
python run_real.py holdout                   # ONE-SHOT; plan frozen in results_ivp/ANALYSIS_PLAN.md (+ .sha256); lock file HOLDOUT_USED.lock
python run_real_extra.py                     # semi-synthetic power check on real returns
(cd paper && python make_ivp_figs.py); (cd paper && python make_powercurve.py)
```
More detail (all flags, ablations): [docs/REPRODUCE.md](docs/REPRODUCE.md).

**Expected runtime:** Tests ~10 s; power grid ~1-2 h on 8 cores; real dev/holdout a few minutes.

## Data
Daily OHLCV for 38 liquid ETFs (2000-2026) as a long CSV `data/etf_long.csv` (columns date,ticker,open,high,low,close,volume) from any source you are licensed to use. **Not redistributed.** The `hitai/` package is the earlier HITAI design kept for reference; the paper uses `ivp/`.

## Results → paper mapping
Scripts in `paper/` are run from inside `paper/` and read the regenerated outputs in `../results*` (large per-day/per-case CSVs are not committed, so rerun the experiments first).

| Paper item | Produced by | Output |
|---|---|---|
| Size/power tables, power curve | `run_power.py`, `paper/make_powercurve.py` | `results_ivp/power_grid.csv`, `paper/fig_powercurve.pdf` |
| Leakage audit | `run_leakage.py` | `results_ivp/leakage.json` |
| Real ETF dev / holdout | `run_real.py` | `results_ivp/real_dev.json`, `real_holdout.json` |
| Semi-synthetic power on real returns | `run_real_extra.py` | `results_ivp/real_extra.json` |

The LaTeX source of the paper is in `paper/`. Small result summaries (`metrics.json`/`.md`, frozen plans and their hashes) are committed; large per-case outputs are not.

## Citation
```bibtex
@misc{ruparel2026indicatorvalidation,
  author = {Ruparel, Chintz},
  title  = {How Much Data Do You Need to Validate a Trading Indicator? A Leakage-Safe, Power-Aware Protocol},
  year   = {2026},
  eprint = {TODO},
  archivePrefix = {arXiv},
  url    = {https://arxiv.org/abs/TODO}
}
```

## License
Code: MIT (see `LICENSE`). Data are **not** covered by this licence: third-party data (prices, TCGA, model weights) remain under their providers' terms and are not included.
