# Results: Indicator validation protocol

Generated automatically by `run_all.sh` (tools/write_results.py). Do not edit by hand.

## Check against the paper's reference numbers

**Overall: DIFFERENCES FOUND** (5 matched, 1 differ/missing).

```
[DIFF] results_ivp/power_grid.csv: 206400 numbers, max rel diff 1.19e-12, 1 over tol
[MATCH] results/paper/power_summary.csv: 602 numbers, max rel diff 0
[MATCH] results_ivp/leakage.json: 29 numbers, max rel diff 0
[MATCH] results_ivp/real_dev.json: 115 numbers, max rel diff 2.2e-05
[MATCH] results_ivp/real_holdout.json: 115 numbers, max rel diff 0.00266
[MATCH] results_ivp/real_extra.json: 28 numbers, max rel diff 7.05e-05
!! synthetic results differ from the paper (should be exact)
```

Differences on downloaded market/public data are expected to be small (providers revise history); synthetic/seeded outputs should match exactly. See the README.

## Headline numbers (map to the paper's tables)

### `results/paper/power_summary.csv`

| ic | n | years | rho | rej_cw | reps | rej_naive |
|---|---|---|---|---|---|---|
| 0.0 | 5 | 3 | 0.3 | 0.042 | 500 | 0.192 |
| 0.0 | 5 | 5 | 0.3 | 0.05 | 500 | 0.206 |
| 0.0 | 5 | 10 | 0.3 | 0.044 | 500 | 0.22 |
| 0.0 | 5 | 20 | 0.3 | 0.022 | 500 | 0.226 |
| 0.0 | 10 | 3 | 0.3 | 0.056 | 500 | 0.208 |
| 0.0 | 10 | 5 | 0.3 | 0.044 | 500 | 0.222 |
| 0.0 | 10 | 10 | 0.3 | 0.054 | 500 | 0.22 |
| 0.0 | 10 | 20 | 0.3 | 0.036 | 500 | 0.234 |
| 0.0 | 25 | 3 | 0.3 | 0.044 | 500 | 0.24 |
| 0.0 | 25 | 5 | 0.3 | 0.042 | 500 | 0.228 |
| 0.0 | 25 | 10 | 0.0 | 0.02 | 200 | 0.215 |
| 0.0 | 25 | 10 | 0.3 | 0.044 | 500 | 0.234 |
| 0.0 | 25 | 10 | 0.6 | 0.045 | 200 | 0.24 |
| 0.0 | 25 | 20 | 0.3 | 0.016 | 500 | 0.194 |
| 0.0 | 50 | 3 | 0.3 | 0.032 | 500 | 0.198 |
| 0.0 | 50 | 5 | 0.3 | 0.048 | 500 | 0.222 |
| 0.0 | 50 | 10 | 0.3 | 0.036 | 500 | 0.216 |
| 0.0 | 50 | 20 | 0.3 | 0.016 | 500 | 0.232 |
| 0.0025 | 5 | 3 | 0.3 | 0.065 | 200 | 0.0 |
| 0.0025 | 5 | 5 | 0.3 | 0.06 | 200 | 0.0 |
| 0.0025 | 5 | 10 | 0.3 | 0.06 | 200 | 0.0 |
| 0.0025 | 5 | 20 | 0.3 | 0.07 | 200 | 0.0 |
| 0.0025 | 10 | 3 | 0.3 | 0.045 | 200 | 0.0 |
| 0.0025 | 10 | 5 | 0.3 | 0.02 | 200 | 0.0 |
| 0.0025 | 10 | 10 | 0.3 | 0.04 | 200 | 0.0 |
| 0.0025 | 10 | 20 | 0.3 | 0.04 | 200 | 0.0 |
| 0.0025 | 25 | 3 | 0.3 | 0.1 | 200 | 0.0 |
| 0.0025 | 25 | 5 | 0.3 | 0.045 | 200 | 0.0 |
| 0.0025 | 25 | 10 | 0.3 | 0.05 | 200 | 0.0 |
| 0.0025 | 25 | 20 | 0.3 | 0.1 | 200 | 0.0 |
... (86 rows; see file)

### `results/results_ivp/real_holdout.json`

| key | value |
|---|---|
| audit.RSI14 | 0 |
| audit.MACDhist | 0 |
| audit.MOM12_1 | 0 |
| audit.REV1M | 0 |
| audit.RVOL21 | 0 |
| audit.MA200gap | 0 |
| n_tickers | 38 |
| start | 2000-01-04 |
| end | 2026-10-20 |
| RSI14_h5.t_cw | 0.0377 |
| RSI14_h5.p_cw | 0.485 |
| RSI14_h5.t_dm | -0.1112 |
| RSI14_h5.p_dm | 0.5443 |
| RSI14_h5.oos_r2 | -0.0001646 |
| RSI14_h5.n_dates | 1704 |
| RSI14_h5.n_obs | 6.475e+04 |
| RSI14_h5.lag | 8 |
| RSI14_h5.p_cw_holm | 1 |
| MACDhist_h5.t_cw | -0.8369 |
| MACDhist_h5.p_cw | 0.7987 |
| MACDhist_h5.t_dm | -0.9598 |
| MACDhist_h5.p_dm | 0.8314 |
| MACDhist_h5.oos_r2 | -0.003328 |
| MACDhist_h5.n_dates | 1704 |
| MACDhist_h5.n_obs | 6.475e+04 |
| MACDhist_h5.lag | 8 |
| MACDhist_h5.p_cw_holm | 1 |
| MOM12_1_h5.t_cw | -1.688 |
| MOM12_1_h5.p_cw | 0.9543 |
| MOM12_1_h5.t_dm | -1.72 |
| MOM12_1_h5.p_dm | 0.9573 |
| MOM12_1_h5.oos_r2 | -0.0001592 |
| MOM12_1_h5.n_dates | 1704 |
| MOM12_1_h5.n_obs | 6.475e+04 |
| MOM12_1_h5.lag | 8 |
| MOM12_1_h5.p_cw_holm | 1 |
| REV1M_h5.t_cw | -0.2362 |
| REV1M_h5.p_cw | 0.5934 |
| REV1M_h5.t_dm | -0.2976 |
| REV1M_h5.p_dm | 0.617 |
| REV1M_h5.oos_r2 | -0.00045 |
| REV1M_h5.n_dates | 1704 |
| REV1M_h5.n_obs | 6.475e+04 |
| REV1M_h5.lag | 8 |
| REV1M_h5.p_cw_holm | 1 |
| RVOL21_h5.t_cw | -0.4313 |
| RVOL21_h5.p_cw | 0.6669 |
| RVOL21_h5.t_dm | -0.487 |
| RVOL21_h5.p_dm | 0.6869 |
| RVOL21_h5.oos_r2 | -0.0006287 |
| RVOL21_h5.n_dates | 1704 |
| RVOL21_h5.n_obs | 6.475e+04 |
| RVOL21_h5.lag | 8 |
| RVOL21_h5.p_cw_holm | 1 |
| MA200gap_h5.t_cw | -0.5893 |
| MA200gap_h5.p_cw | 0.7222 |
| MA200gap_h5.t_dm | -0.6357 |
| MA200gap_h5.p_dm | 0.7375 |
| MA200gap_h5.oos_r2 | -0.0004235 |
| MA200gap_h5.n_dates | 1704 |
... (117 values; see file)

### `results/results_ivp/real_dev.json`

| key | value |
|---|---|
| audit.RSI14 | 0 |
| audit.MACDhist | 0 |
| audit.MOM12_1 | 0 |
| audit.REV1M | 0 |
| audit.RVOL21 | 0 |
| audit.MA200gap | 0 |
| n_tickers | 38 |
| start | 2000-01-04 |
| end | 2019-12-31 |
| RSI14_h5.t_cw | -0.005291 |
| RSI14_h5.p_cw | 0.5021 |
| RSI14_h5.t_dm | -0.7384 |
| RSI14_h5.p_dm | 0.7699 |
| RSI14_h5.oos_r2 | -0.00107 |
| RSI14_h5.n_dates | 4774 |
| RSI14_h5.n_obs | 1.691e+05 |
| RSI14_h5.lag | 10 |
| RSI14_h5.p_cw_holm | 1 |
| MACDhist_h5.t_cw | 0.3611 |
| MACDhist_h5.p_cw | 0.359 |
| MACDhist_h5.t_dm | -0.7532 |
| MACDhist_h5.p_dm | 0.7743 |
| MACDhist_h5.oos_r2 | -0.0007163 |
| MACDhist_h5.n_dates | 4774 |
| MACDhist_h5.n_obs | 1.688e+05 |
| MACDhist_h5.lag | 10 |
| MACDhist_h5.p_cw_holm | 1 |
| MOM12_1_h5.t_cw | -0.71 |
| MOM12_1_h5.p_cw | 0.7611 |
| MOM12_1_h5.t_dm | -1.098 |
| MOM12_1_h5.p_dm | 0.864 |
| MOM12_1_h5.oos_r2 | -0.001906 |
| MOM12_1_h5.n_dates | 4648 |
| MOM12_1_h5.n_obs | 1.626e+05 |
| MOM12_1_h5.lag | 10 |
| MOM12_1_h5.p_cw_holm | 1 |
| REV1M_h5.t_cw | -0.1133 |
| REV1M_h5.p_cw | 0.5451 |
| REV1M_h5.t_dm | -0.8372 |
| REV1M_h5.p_dm | 0.7988 |
| REV1M_h5.oos_r2 | -0.001603 |
| REV1M_h5.n_dates | 4774 |
| REV1M_h5.n_obs | 1.69e+05 |
| REV1M_h5.lag | 10 |
| REV1M_h5.p_cw_holm | 1 |
| RVOL21_h5.t_cw | -1.399 |
| RVOL21_h5.p_cw | 0.9191 |
| RVOL21_h5.t_dm | -2.145 |
| RVOL21_h5.p_dm | 0.984 |
| RVOL21_h5.oos_r2 | -0.00454 |
| RVOL21_h5.n_dates | 4774 |
| RVOL21_h5.n_obs | 1.69e+05 |
| RVOL21_h5.lag | 10 |
| RVOL21_h5.p_cw_holm | 1 |
| MA200gap_h5.t_cw | -0.726 |
| MA200gap_h5.p_cw | 0.7661 |
| MA200gap_h5.t_dm | -1.29 |
| MA200gap_h5.p_dm | 0.9015 |
| MA200gap_h5.oos_r2 | -0.002456 |
| MA200gap_h5.n_dates | 4774 |
... (117 values; see file)

### `results/results_ivp/real_extra.json`

| key | value |
|---|---|
| leaky_on_real_dev.centeredMA.t_cw | 19.19 |
| leaky_on_real_dev.centeredMA.p_cw | 0 |
| leaky_on_real_dev.centeredMA.t_dm | 14.98 |
| leaky_on_real_dev.centeredMA.p_dm | 0 |
| leaky_on_real_dev.centeredMA.oos_r2 | 0.4105 |
| leaky_on_real_dev.centeredMA.n_dates | 4769 |
| leaky_on_real_dev.centeredMA.n_obs | 1.69e+05 |
| leaky_on_real_dev.centeredMA.lag | 10 |
| leaky_on_real_dev.fullsampleZ.t_cw | 1.675 |
| leaky_on_real_dev.fullsampleZ.p_cw | 0.04699 |
| leaky_on_real_dev.fullsampleZ.t_dm | 0.1745 |
| leaky_on_real_dev.fullsampleZ.p_dm | 0.4307 |
| leaky_on_real_dev.fullsampleZ.oos_r2 | 0.0011 |
| leaky_on_real_dev.fullsampleZ.n_dates | 4774 |
| leaky_on_real_dev.fullsampleZ.n_obs | 1.692e+05 |
| leaky_on_real_dev.fullsampleZ.lag | 10 |
| leaky_on_real_dev.nextDay.t_cw | 6.907 |
| leaky_on_real_dev.nextDay.p_cw | 2.483e-12 |
| leaky_on_real_dev.nextDay.t_dm | 3.9 |
| leaky_on_real_dev.nextDay.p_dm | 4.811e-05 |
| leaky_on_real_dev.nextDay.oos_r2 | 0.02534 |
| leaky_on_real_dev.nextDay.n_dates | 4774 |
| leaky_on_real_dev.nextDay.n_obs | 1.693e+05 |
| leaky_on_real_dev.nextDay.lag | 10 |
| semi_synthetic_ic0 | 0.01 |
| semi_synthetic_ic0.005 | 0.33 |
| semi_synthetic_ic0.01 | 0.83 |
| semi_synthetic_ic0.02 | 1 |

### `results/results_ivp/leakage.json`

| key | value |
|---|---|
| L1.naive[0] | 0.22 |
| L1.naive[1] | 0.1682 |
| L1.naive[2] | 0.2824 |
| L1.protocol[0] | 0.04 |
| L1.protocol[1] | 0.02041 |
| L1.protocol[2] | 0.07693 |
| L3.shuffled_kfold_r2_median | -0.01204 |
| L3.shuffled_frac_pos | 0.06 |
| L3.wf_r2_median | -0.02266 |
| L3.wf_frac_pos | 0.01 |
| L3.shuffled_r2_q[0] | -0.01733 |
| L3.shuffled_r2_q[1] | 0.001473 |
| L3.wf_r2_q[0] | -0.03454 |
| L3.wf_r2_q[1] | -0.01323 |
| L4.best_unadjusted[0] | 0.415 |
| L4.best_unadjusted[1] | 0.3489 |
| L4.best_unadjusted[2] | 0.4843 |
| L4.holm[0] | 0.08 |
| L4.holm[1] | 0.04984 |
| L4.holm[2] | 0.126 |
| L2_audit.RSI14 | 0 |
| L2_audit.MACDhist | 0 |
| L2_audit.MOM12_1 | 0 |
| L2_audit.REV1M | 0 |
| L2_audit.RVOL21 | 0 |
| L2_audit.MA200gap | 0 |
| L2_audit.centeredMA | 1 |
| L2_audit.fullsampleZ | 1 |
| L2_audit.nextDay | 1 |

## Run information

- Run date: 2026-10-23 16:00 EDT
- Mode: `default`
- Git commit: `4abb3811084be2ea261ed095359b3dbb35b196c8` (uncommitted changes)
- Python: 3.14.6 (macOS-26.4.1-arm64-arm-64bit-Mach-O)
- CPUs: 18

Package versions (pinned in requirements.txt):

```
beautifulsoup4==4.15.0
certifi==2026.10.19
cffi==2.1.1
charset-normalizer==3.5.2
cloudpickle==3.1.2
contourpy==1.4.0
curl_cffi==0.16.3
cycler==0.12.1
fonttools==4.67.0
idna==3.20
iniconfig==2.3.1
joblib==1.6.0
kiwisolver==1.5.1
lxml==6.1.3
matplotlib==3.11.2
multitasking==0.0.13
narwhals==2.27.1
numpy==2.5.4
packaging==26.3
pandas==3.0.6
peewee==4.5.3
pillow==13.0.0
platformdirs==4.13.5
pluggy==1.7.0
protobuf==7.36.2
pycparser==3.11
Pygments==2.21.0
pyparsing==3.3.3
pytest==9.1.1
python-dateutil==2.9.0.post0
pytz==2026.5
requests==2.34.2
scikit-learn==1.9.1
scipy==1.18.1
six==1.17.0
soupsieve==3.0.3
tabulate==0.10.0
threadpoolctl==3.7.0
typing_extensions==4.16.0
urllib3==2.8.0
websockets==17.3
yfinance==1.7.0
```

## Data hashes (sha256)

38 input files hashed; full list in `results/data_sha256.txt`.

```
2488bee2dd2dbb6725fe1ee26eb1a959fcb24ccdd845e401eb1ea28fe07a387b  data/prices/AGG.csv
25df8e7a591b51f0501092259059f5a59ec45b7091976e76ca28b866f2cb7cc9  data/prices/DBC.csv
f9a53a26399abc3607e1a326351db1ca056829823180739bc7edfb7df68b8ecf  data/prices/DIA.csv
2aedc1cb7775f67c4dfb6aaac814055b18fa4d1b9101206b7a3c0ee3b094c832  data/prices/EEM.csv
c42647a26400a34fdd4b37a23de62b49cf532eea5daff2025ffc43ff5a40ebca  data/prices/EFA.csv
d2360ad831a8b3b191bf06b078b60b3356a7b37598ab70857c704383b4b90a94  data/prices/EWA.csv
ef75c86962511fd8fee8f8b482094876e30ca9be9732b5121f0ac0fe1cc2dac9  data/prices/EWC.csv
e8fbf05d4156e94728713f183cf867cf1ea9b032aef82c5fd6ae79764f1b22b8  data/prices/EWG.csv
86e9800c3688cdc3e53b44ecab3a6a366a562ee57b92487432a1340bf0a7985c  data/prices/EWH.csv
46168ad21e5bb772d60c92590a28e8ed8a9b4e4035030951ae23d180dcdf77e4  data/prices/EWJ.csv
774069eb412647cb30e79a300c5f1f1f8f066291b6d1b478cc0b6b357f97cb4e  data/prices/EWU.csv
4f98e3c60caee1cf0ecfad68cf221918d6325ec5c95fc8a18b0260a3f42bf0ae  data/prices/EWZ.csv
f3ba768f12fb11145b9ffa3fab0a19d5849bc823cc696b03130e971e12e805ca  data/prices/FXI.csv
6817e2b8bbf8b4796aae720ebd32176ab56c69501a96316d93a9ed96761fc1ab  data/prices/GLD.csv
30dc3111425bc8851ea1249b9afc68f5d47bb21fac8797121d872af4c25733b5  data/prices/HYG.csv
4f0a1143a7d333b9227071d987268958d556dd3e4fb68aba06dacb78dfff3c5d  data/prices/IEF.csv
71e454945181d6214089e4a75d5395582aeecd29536638b57dc32524a819a18f  data/prices/IJR.csv
29209f9c4efd9acc47acc996bf14b59588a2807fc04c223d001351cac0c769c2  data/prices/IWM.csv
48fcc43f90fb1ce36a0121b113158d937df74636800bf8a7a4aa761ee448f412  data/prices/IYR.csv
8adcf6c248483930b040dff915ef28edbbcbff32570c27b5103c5ad9c4f00ad3  data/prices/LQD.csv
30b0950f8d23978290c55e79b43ef1ef0aa254f1e51fd84789d8c15e7362cc15  data/prices/MDY.csv
9ba0cda02bf8c7d21bf634a13b05ef0bbd251dc4b8d0b4e1ebc7825227451a00  data/prices/QQQ.csv
7fc074adccfaa5efeb30ca498f21f6ade2f9f23f52c5eccb1e072e960035959b  data/prices/SHY.csv
3f3b2907baa93e7e6de0376e4a1cb06084cb97688b9e179cbcf8a6fc551c0fd3  data/prices/SLV.csv
76b65853226b70f92ab86fba8e3f10823c265d6552acfc771e249bdc3e27368f  data/prices/SPY.csv
a8633e6f77daaacc27df55145493b5d9458909ca92c01265385444756b02818e  data/prices/TIP.csv
32f4bcdafc09dcf7d971cb4ecf57a4040a45c6aad31cd4bf6dd7cc29642577e1  data/prices/TLT.csv
8cd69849fdcfc108884559eff70ba02cf1652fc9acf918adeda97ed55137ff84  data/prices/USO.csv
14af186413effea2ddc4f5f35eb027386e66ef3db6243e78549c666526dda1b7  data/prices/VNQ.csv
53876e666c6f7da2df25e6168e6bf3b285b1d7a9ec0129799889e3c3e75ccb20  data/prices/XLB.csv
7172320e3378f6d5968c59cf98567f37f1dd13f53e731a9d42cdabf879292b4d  data/prices/XLE.csv
5d70869df04bf3944ae8e72ac8a6923d041d3cca0137ef671693beaa775201df  data/prices/XLF.csv
2c72dfd4eeaee150ed31c64dd760b4e00784b57e4dadff526a32a3094fde370b  data/prices/XLI.csv
cd971f4a83da1ec744c7b6f1a954be001765e51a8ef267d808c7722df5c1fe66  data/prices/XLK.csv
fcd9731cc561d098e41ca8a06ec01c122f74890baae491c3f528c3c94bc74e46  data/prices/XLP.csv
80f59587c4d8de70c524f847246f44e9c67a86d48f43d14577d40768eb70ae71  data/prices/XLU.csv
7d55b96e3ee8eafed213405561d42bc09644c0e780ef0388dc10e126b6203a31  data/prices/XLV.csv
bd29e542fa186cfb59a2638e5ca0e566c4347d8e131fb502f0a7a4f1cdc79bf0  data/prices/XLY.csv
```

## Output files

Total committed size of `results/`: 3.4 MB.

