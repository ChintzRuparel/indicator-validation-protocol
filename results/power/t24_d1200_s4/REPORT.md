# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 20976, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 12600 |    0.6943 |  0.2506 | 0.0116 | 0.4956 |      0.5105 |             0.0179 |                 0.6944 |            -0.7231 |          -1.5979 |          0.1025 |          0.2975 |    0.0095 |      -0.1126 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 12600 |    0.6949 |  0.2509 | 0.0163 | 0.4877 |      0.5105 |             0.0178 |                 0.6954 |            -0.7071 |          -1.3402 |          0.0752 |          0.3045 |    0.0246 |      -0.1036 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 12600 |    0.6933 |  0.2501 | 0.0027 | 0.4997 |      0.5105 |             0.017  |                 0.694  |             0.2042 |          -0.1332 |          0.0322 |          0.2206 |    0.4236 |      -0.0394 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 12600 |    0.7027 |  0.2521 | 0.0178 | 0.4898 |      0.5105 |             0.0351 |                 0.6956 |            -0.0883 |          -0.626  |          0.0819 |          0.4372 |    0.1798 |      -0.0606 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 12600 |    0.6943 |  0.2506 | 0.0203 | 0.4944 |      0.5105 |             0.0506 |                 0.7024 |             0.6991 |          -0.1857 |          0.1387 |          0.4905 |    0.3941 |      -0.0669 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 12600 |    0.6959 |  0.2508 | 0.0072 | 0.5022 |      0.5105 |             0.028  |                 0.6979 |             0.4169 |          -0.4617 |          0.1005 |          0.2912 |    0.252  |      -0.042  |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 12600 |    0.699  |  0.2517 | 0.0142 | 0.493  |      0.5105 |             0.0314 |                 0.6959 |             0.0793 |          -1.0466 |          0.1448 |          0.3571 |    0.0655 |      -0.0732 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 12600 |    0.6947 |  0.2507 | 0.0187 | 0.4936 |      0.5105 |             0.048  |                 0.7025 |             0.3515 |          -0.9229 |          0.1778 |          0.3573 |    0.0885 |      -0.0998 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 12600 |    0.6959 |  0.2508 | 0.0072 | 0.5022 |      0.5105 |             0.028  |                 0.6979 |             0.4169 |          -0.4617 |          0.1005 |          0.2912 |    0.252  |      -0.042  |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 12600 |    0.6926 |  0.2477 | 0.0068 | 0.5595 |      0.5105 |             0.0216 |                 0.6888 |             8.6295 |           5.6983 |          0.5825 |          0.8474 |    1      |      -0.0151 |    0.6677 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 12600 |    0.6972 |  0.2497 | 0.0147 | 0.5451 |      0.5105 |             0.0331 |                 0.6961 |             6.1136 |           3.5215 |          0.5043 |          0.7644 |    1      |      -0.0274 |    0.0032 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 12600 |    0.6934 |  0.2486 | 0.0106 | 0.5536 |      0.5105 |             0.0242 |                 0.6906 |             7.465  |           4.8679 |          0.5319 |          0.8467 |    1      |      -0.0228 |    0.2213 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 12600 |    0.6982 |  0.2512 | 0.0104 | 0.4956 |      0.5105 |             0.0286 |                 0.6962 |            -0.4829 |          -1.5342 |          0.1336 |          0.3339 |    0.0133 |      -0.1052 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 12600 |    0.6946 |  0.2505 | 0.015  | 0.4937 |      0.5105 |             0.0496 |                 0.7029 |             0.5037 |          -0.3765 |          0.1048 |          0.2979 |    0.2926 |      -0.0526 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 12600 |    0.6966 |  0.2509 | 0.0095 | 0.5021 |      0.5105 |             0.0311 |                 0.698  |             0.4323 |          -0.516  |          0.1126 |          0.3053 |    0.228  |      -0.0506 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 12600 |    0.7009 |  0.2517 | 0.0111 | 0.4954 |      0.5105 |             0.0292 |                 0.6961 |             0.1655 |          -0.7089 |          0.1021 |          0.302  |    0.1509 |      -0.0712 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 12600 |    0.6946 |  0.2507 | 0.0108 | 0.4953 |      0.5105 |             0.0532 |                 0.7031 |             0.3991 |          -0.5785 |          0.1597 |          0.4961 |    0.2006 |      -0.0902 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 12600 |    0.6971 |  0.2509 | 0.0058 | 0.5009 |      0.5105 |             0.0342 |                 0.6982 |             0.213  |          -0.4893 |          0.0773 |          0.2732 |    0.2394 |      -0.0479 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 12600 |    0.6888 |  0.247  | 0.0111 | 0.5638 |      0.5105 |             0.0222 |                 0.6873 |             9.3784 |           6.4833 |          0.5817 |          0.8984 |    1      |      -0.0144 |    0.9324 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 12600 |    0.698  |  0.249  | 0.0126 | 0.554  |      0.5105 |             0.0284 |                 0.6943 |             7.6567 |           4.8706 |          0.534  |          0.776  |    1      |      -0.0192 |    0.2256 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 12600 |    0.693  |  0.2479 | 0.0087 | 0.5604 |      0.5105 |             0.0217 |                 0.6894 |             8.2611 |           5.6478 |          0.5324 |          0.7947 |    1      |      -0.0192 |    0.6375 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  0.7341 |        0.2314 |           0.0017 | False          | nan      |       nan      |     0.3395 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.2514 |        0.0122 |           0.0065 | False          | nan      |       nan      |     0.0536 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.0716 |        0.0192 |           0.0056 | False          | nan      |       nan      |     0.0602 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  3.3696 |        0.0004 |           0.0084 | False          | nan      |       nan      |     0.0041 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.6505 |        0.008  |         nan      | False          | nan      |       nan      |     0.0442 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0241 |        0.1343 |         nan      | False          | nan      |       nan      |     0.2438 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.7793 |        0.0752 |          -0.0037 | False          | nan      |       nan      |     0.1654 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -0.8197 |        0.7938 |          -0.0022 | False          | nan      |       nan      |     0.8597 |
| H3a          | gbt      | rules_tech - hitai_full                                      | -0.954  |        0.83   |          -0.0025 | False          | nan      |       nan      |     0.8597 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       | -0.9447 |        0.8276 |          -0.0026 | False          | nan      |       nan      |     0.8597 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         | -0.9912 |        0.8392 |          -0.0026 | False          | nan      |       nan      |     0.8597 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.7924 |        0.0001 |         nan      | False          | nan      |       nan      |     0.0033 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0453 |        0.0187 |         nan      | False          | nan      |       nan      |     0.0602 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.4811 |        0.6305 |           0.0009 | False          | nan      |       nan      |     0.8159 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -0.0359 |        0.5143 |          -0.0001 | True           |   0.5143 |         1      |     0.7072 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  1.0621 |        0.1441 |           0.0025 | True           |   0.2933 |         0.7205 |     0.2438 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  1.3103 |        0.0951 |           0.0032 | True           |   0.2933 |         0.4753 |     0.1901 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  1.4515 |        0.0733 |           0.0036 | True           |   0.2933 |         0.3666 |     0.1654 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.0545 |        0.0023 |         nan      | False          | nan      |       nan      |     0.0165 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0343 |        0.0576 |         nan      | True           |   0.2878 |         0.2878 |     0.1583 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.1768 |        0.8597 |          -0.0004 | False          | nan      |       nan      |     0.8597 |
| H4b          | tagger   | corr(tag,fwd) original=0.1522 vs perturbed-context (want ~0) |  0.009  |        0.1923 |           0.1432 | False          | nan      |       nan      |     0.3021 |

## Reality check / SPA vs rules_only: RC p=0.900, SPA p=0.883

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5136 |    0.6932 |  0.25   | 0.0039 | 0.482  |      0.5018 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 5136 |    0.6962 |  0.2514 | 0.0256 | 0.4748 |      0.5018 |          -2.614  |    0.0055 |
| hitai_full|pit|gbt_mono      | 5136 |    0.6904 |  0.2482 | 0.0132 | 0.5536 |      0.5018 |           5.9493 |    1      |
| hitai_full|shuffled|gbt_mono | 5136 |    0.6961 |  0.251  | 0.0302 | 0.474  |      0.5018 |          -2.4713 |    0.0096 |
