# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 10488, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6300 |    0.6973 |  0.2516 | 0.0243 | 0.5019 |       0.501 |             0.0272 |                 0.6958 |            -0.0843 |          -0.7857 |          0.1441 |          0.52   |    0.1283 |      -0.1366 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6300 |    0.695  |  0.2509 | 0.0324 | 0.5035 |       0.501 |             0.0268 |                 0.6953 |             0.1741 |          -0.5933 |          0.1824 |          0.6597 |    0.195  |      -0.1445 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6300 |    0.6946 |  0.2507 | 0.0253 | 0.5006 |       0.501 |             0.0266 |                 0.6952 |             0.3399 |          -0.358  |          0.1457 |          0.5154 |    0.3026 |      -0.0933 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6300 |    0.7373 |  0.2563 | 0.0319 | 0.5069 |       0.501 |             0.0334 |                 0.6982 |            -0.2292 |          -0.9502 |          0.1486 |          0.4221 |    0.0857 |      -0.1433 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6300 |    0.7053 |  0.2525 | 0.0275 | 0.5045 |       0.501 |             0.0751 |                 0.708  |             0.364  |          -0.4704 |          0.1613 |          0.4162 |    0.2495 |      -0.1025 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6300 |    0.7019 |  0.2521 | 0.0307 | 0.512  |       0.501 |             0.0519 |                 0.7004 |             0.5177 |          -0.2177 |          0.1424 |          0.4397 |    0.377  |      -0.0924 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6300 |    0.7233 |  0.2545 | 0.0278 | 0.508  |       0.501 |             0.0362 |                 0.7002 |             0.9101 |           0.1876 |          0.1327 |          0.3516 |    0.6067 |      -0.0617 |    0.0001 |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6300 |    0.6991 |  0.252  | 0.0307 | 0.5017 |       0.501 |             0.0732 |                 0.7078 |             0.3767 |          -0.5051 |          0.1752 |          0.4284 |    0.2336 |      -0.1075 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6300 |    0.7019 |  0.2521 | 0.0307 | 0.512  |       0.501 |             0.0519 |                 0.7004 |             0.5177 |          -0.2177 |          0.1424 |          0.4397 |    0.377  |      -0.0924 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6300 |    0.6936 |  0.2484 | 0.0349 | 0.5735 |       0.501 |             0.0395 |                 0.6869 |             5.0634 |           3.15   |          0.5221 |          0.9122 |    1      |      -0.0464 |    0.6547 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6300 |    0.702  |  0.2516 | 0.0328 | 0.5509 |       0.501 |             0.0512 |                 0.6959 |             4.1085 |           2.2811 |          0.4844 |          0.7363 |    0.9995 |      -0.0427 |    0.1967 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6300 |    0.7067 |  0.2508 | 0.0323 | 0.5602 |       0.501 |             0.0356 |                 0.6887 |             4.314  |           2.6171 |          0.4268 |          0.7402 |    0.9999 |      -0.0321 |    0.3562 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6300 |    0.702  |  0.2527 | 0.0267 | 0.5094 |       0.501 |             0.0355 |                 0.7002 |             0.66   |           0.0272 |          0.1271 |          0.5179 |    0.5157 |      -0.086  |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6300 |    0.699  |  0.2521 | 0.0338 | 0.4979 |       0.501 |             0.0735 |                 0.7069 |             0.2905 |          -0.4953 |          0.1443 |          0.3781 |    0.2382 |      -0.0888 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6300 |    0.7029 |  0.2526 | 0.0364 | 0.507  |       0.501 |             0.0519 |                 0.7005 |             0.1428 |          -0.6834 |          0.1879 |          0.5632 |    0.1628 |      -0.1309 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6300 |    0.6971 |  0.2518 | 0.0232 | 0.5106 |       0.501 |             0.0398 |                 0.6998 |             0.173  |          -0.64   |          0.1641 |          0.4016 |    0.177  |      -0.1177 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6300 |    0.7028 |  0.2523 | 0.0371 | 0.499  |       0.501 |             0.0784 |                 0.7088 |             0.4036 |          -0.4999 |          0.1705 |          0.3998 |    0.2361 |      -0.0951 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6300 |    0.7029 |  0.2525 | 0.0368 | 0.506  |       0.501 |             0.0511 |                 0.7004 |             0.2005 |          -0.6388 |          0.181  |          0.5544 |    0.1791 |      -0.1326 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6300 |    0.7063 |  0.2498 | 0.034  | 0.5689 |       0.501 |             0.0351 |                 0.6866 |             4.6893 |           2.903  |          0.4768 |          0.8797 |    1      |      -0.0507 |    0.5193 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6300 |    0.6976 |  0.2508 | 0.0305 | 0.5533 |       0.501 |             0.0483 |                 0.6958 |             4.0141 |           2.2167 |          0.5306 |          0.9214 |    0.9994 |      -0.061  |    0.1697 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6300 |    0.7006 |  0.2502 | 0.035  | 0.5625 |       0.501 |             0.0351 |                 0.6889 |             4.6946 |           2.9982 |          0.4617 |          0.8413 |    1      |      -0.0429 |    0.5737 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  0.8893 |        0.1869 |           0.0037 | False          | nan      |       nan      |     0.3163 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.831  |        0.0023 |           0.0297 | False          | nan      |       nan      |     0.0082 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.7097 |        0.0034 |           0.0084 | False          | nan      |       nan      |     0.0082 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  0.9839 |        0.1626 |           0.0035 | False          | nan      |       nan      |     0.3129 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.1862 |        0.0014 |         nan      | False          | nan      |       nan      |     0.0079 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0833 |        0.0034 |         nan      | False          | nan      |       nan      |     0.0082 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  2.9789 |        0.0029 |           0.0127 | False          | nan      |       nan      |     0.0082 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -1.499  |        0.9331 |          -0.007  | False          | nan      |       nan      |     0.9708 |
| H3a          | gbt      | rules_tech - hitai_full                                      | -0.6564 |        0.7442 |          -0.0029 | False          | nan      |       nan      |     0.9051 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       | -0.6957 |        0.7567 |          -0.003  | False          | nan      |       nan      |     0.9051 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  0.1382 |        0.445  |           0.0008 | False          | nan      |       nan      |     0.6993 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.9794 |        0.0001 |         nan      | False          | nan      |       nan      |     0.0015 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.085  |        0.0028 |         nan      | False          | nan      |       nan      |     0.0082 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -2.0642 |        0.039  |          -0.0045 | False          | nan      |       nan      |     0.0858 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -1.8926 |        0.9708 |          -0.012  | True           |   1      |         1      |     0.9708 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      | -0.7778 |        0.7817 |          -0.0047 | True           |   1      |         1      |     0.9051 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       | -0.63   |        0.7356 |          -0.0038 | True           |   1      |         1      |     0.9051 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         | -0.5979 |        0.7251 |          -0.0037 | True           |   1      |         1      |     0.9051 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.2617 |        0.0011 |         nan      | False          | nan      |       nan      |     0.0079 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0999 |        0.0006 |         nan      | True           |   0.0029 |         0.0029 |     0.0063 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.3701 |        0.1707 |          -0.0061 | False          | nan      |       nan      |     0.3129 |
| H4b          | tagger   | corr(tag,fwd) original=0.1647 vs perturbed-context (want ~0) |  0.0008 |        0.9368 |           0.1639 | False          | nan      |       nan      |     0.9708 |

## Reality check / SPA vs rules_only: RC p=0.910, SPA p=0.907

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2568 |    0.6954 |  0.2511 | 0.0252 | 0.5093 |      0.5093 |          -0.389  |    0.3607 |
| rules_tech|pit|gbt_mono      | 2568 |    0.6958 |  0.2512 | 0.0282 | 0.5021 |      0.5093 |          -0.4109 |    0.3538 |
| hitai_full|pit|gbt_mono      | 2568 |    0.693  |  0.2497 | 0.0331 | 0.5559 |      0.5093 |           3.3458 |    0.999  |
| hitai_full|shuffled|gbt_mono | 2568 |    0.6964 |  0.2513 | 0.0283 | 0.5015 |      0.5093 |          -0.5273 |    0.3154 |
