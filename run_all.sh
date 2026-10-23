#!/usr/bin/env bash
# One command from a fresh clone to the paper's tables/figures.  Usage: bash run_all.sh [--quick] [--skip-download]
#   full   : power grid (22,000 simulated studies, ~1-2 h on 8 cores) + leakage + real ETF dev/holdout + semi-synthetic
#   --quick: skip the power grid (uses the committed results_ivp/power_grid.csv for the tables/figure)
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p results; exec > >(tee results/run_log.txt) 2>&1   # full console log, parsed into results/RESULTS.md
export OMP_NUM_THREADS=1 PYTHONHASHSEED=0 PYTHONPATH=.
PY=${PYTHON:-python3}; QUICK=0; DL=1
for a in "$@"; do case $a in --quick) QUICK=1;; --skip-download) DL=0;; esac; done
[ -d .venv ] || $PY -m venv .venv
. .venv/bin/activate
pip install -q --upgrade pip && pip install -q -r requirements.txt
echo "== 1/6 tests + frozen-plan hashes"; python -m pytest -q tests; python tools/sha256check.py -c UNIVERSE_FROZEN.sha256
grep -v protocol.py results_ivp/ANALYSIS_PLAN.sha256 | grep '^[0-9a-f]\{64\} ' | python tools/sha256check.py -c
echo "  note: ivp/protocol.py intentionally differs from its frozen hash (the one disclosed amendment: optional score_from, see paper Sec. 3)"
if [ $QUICK = 0 ]; then echo "== 2/6 power grid (synthetic, seeded)"; python run_power.py; else echo "== 2/6 power grid skipped (--quick)"; fi
if [ $DL = 1 ]; then echo "== 3/6 download 38 ETFs from Yahoo (personal-use terms; not redistributed)"; python scripts/download_data.py --out data/prices; fi
echo "== 4/6 leakage experiments (synthetic, seeded)"; python run_leakage.py > /dev/null
echo "== 5/6 real data: dev (2000-2019), one-shot holdout (2020-2026), semi-synthetic power"
python run_real.py dev > /dev/null; python run_real.py holdout > /dev/null; python run_real_extra.py > /dev/null
echo "== 6/6 tables, figure, compare with the paper"
mkdir -p results/paper; export PAPER_OUT="$PWD/results/paper"
python paper/power_tables.py results_ivp/power_grid.csv results/paper/power_summary.csv > /dev/null
(cd paper && python make_ivp_figs.py)
cp results_ivp/*.json results/paper/
S=0
if [ $QUICK = 0 ]; then python tools/compare.py --tol 0 paper/reference/power_grid.csv results_ivp/power_grid.csv || S=1; fi
python tools/compare.py --tol 0 paper/reference/power_summary.csv results/paper/power_summary.csv paper/reference/leakage.json results_ivp/leakage.json || S=1
python tools/compare.py --tol ${REAL_TOL:-0.02} paper/reference/real_dev.json results_ivp/real_dev.json paper/reference/real_holdout.json results_ivp/real_holdout.json paper/reference/real_extra.json results_ivp/real_extra.json \
  || echo "!! real-data numbers drift (Yahoo revises adjusted closes; the paper's last bar 2026-10-20 was intraday)"
[ $S = 0 ] || echo "!! synthetic results differ from the paper (should be exact)"
echo "Done. Tables: results/paper/power_summary.csv, results/paper/*.json; figure: results/paper/fig_ivp_power.pdf"

echo "== write results/RESULTS.md"
python tools/write_results.py --mode="${*:-default}" --title "Indicator validation protocol" --copy "results_ivp:results_ivp" --data data --headline results/paper/power_summary.csv results/results_ivp/real_holdout.json results/results_ivp/real_dev.json results/results_ivp/real_extra.json results/results_ivp/leakage.json
echo "Share: git add results && git commit -m \"Add run results\" && git push"
