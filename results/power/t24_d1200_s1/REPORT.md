# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 20976, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 12600 |    0.696  |  0.2511 | 0.0196 | 0.503  |      0.4897 |             0.0066 |                 0.693  |            -0.6175 |          -1.4336 |          0.1075 |          0.3106 |    0.0179 |      -0.1121 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 12600 |    0.6952 |  0.251  | 0.0305 | 0.4934 |      0.4897 |             0.0066 |                 0.6931 |             0.0777 |          -0.5602 |          0.0821 |          0.3342 |    0.2078 |      -0.0687 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 12600 |    0.6943 |  0.2506 | 0.016  | 0.4865 |      0.4897 |             0.006  |                 0.6932 |            -0.0357 |          -0.0619 |          0.0038 |          0.4    |    0.4645 |      -0.0661 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 12600 |    0.7023 |  0.252  | 0.0206 | 0.4973 |      0.4897 |             0.019  |                 0.6939 |             0.1233 |          -0.405  |          0.0793 |          0.4186 |    0.2799 |      -0.0929 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 12600 |    0.6976 |  0.2513 | 0.0318 | 0.4892 |      0.4897 |             0.0441 |                 0.6996 |             0.1693 |          -0.704  |          0.1291 |          0.4137 |    0.1568 |      -0.1182 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 12600 |    0.6973 |  0.2513 | 0.0286 | 0.4971 |      0.4897 |             0.0345 |                 0.6951 |            -0.4774 |          -1.2027 |          0.0761 |          0.2154 |    0.0421 |      -0.0834 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 12600 |    0.7038 |  0.2525 | 0.0189 | 0.4939 |      0.4897 |             0.0187 |                 0.6941 |            -0.0482 |          -0.7094 |          0.107  |          0.5009 |    0.1541 |      -0.1197 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 12600 |    0.6954 |  0.2509 | 0.0286 | 0.4905 |      0.4897 |             0.0437 |                 0.7    |            -0.2463 |          -1.2254 |          0.1569 |          0.4633 |    0.0401 |      -0.1727 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 12600 |    0.6973 |  0.2513 | 0.0286 | 0.4971 |      0.4897 |             0.0345 |                 0.6951 |            -0.4774 |          -1.2027 |          0.0761 |          0.2154 |    0.0421 |      -0.0834 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 12600 |    0.6884 |  0.247  | 0.0106 | 0.5699 |      0.4897 |             0.0125 |                 0.6849 |             9.4126 |           6.6806 |          0.544  |          0.8867 |    1      |      -0.0133 |    0.573  |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 12600 |    0.6957 |  0.2484 | 0.0133 | 0.5548 |      0.4897 |             0.0279 |                 0.6898 |             7.9274 |           5.1296 |          0.5182 |          0.7627 |    1      |      -0.0158 |    0.0225 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 12600 |    0.6919 |  0.2475 | 0.0149 | 0.5664 |      0.4897 |             0.013  |                 0.6854 |             9.4837 |           6.7927 |          0.5465 |          0.8212 |    1      |      -0.0116 |    0.6377 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 12600 |    0.7034 |  0.2522 | 0.0173 | 0.4938 |      0.4897 |             0.0223 |                 0.6947 |             0.2913 |          -0.6035 |          0.139  |          0.486  |    0.1931 |      -0.114  |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 12600 |    0.6978 |  0.2513 | 0.0289 | 0.4865 |      0.4897 |             0.0464 |                 0.6999 |            -0.4352 |          -1.802  |          0.2002 |          0.4017 |    0.0045 |      -0.1699 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 12600 |    0.6967 |  0.2514 | 0.0303 | 0.4898 |      0.4897 |             0.0347 |                 0.6954 |            -0.3558 |          -1.3864 |          0.163  |          0.4763 |    0.0244 |      -0.1325 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 12600 |    0.697  |  0.2515 | 0.019  | 0.4945 |      0.4897 |             0.0309 |                 0.6953 |             0.1134 |          -0.7517 |          0.1566 |          0.6219 |    0.1382 |      -0.1342 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 12600 |    0.6968 |  0.2512 | 0.0339 | 0.4843 |      0.4897 |             0.047  |                 0.7012 |            -0.259  |          -1.2109 |          0.163  |          0.5143 |    0.0413 |      -0.1658 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 12600 |    0.6964 |  0.2512 | 0.0287 | 0.4913 |      0.4897 |             0.0335 |                 0.6957 |            -0.3292 |          -1.3181 |          0.1214 |          0.2544 |    0.0285 |      -0.1036 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 12600 |    0.6903 |  0.2469 | 0.0143 | 0.5715 |      0.4897 |             0.0103 |                 0.6842 |             8.9307 |           6.3243 |          0.549  |          0.8799 |    1      |      -0.0194 |    0.3784 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 12600 |    0.6964 |  0.2486 | 0.0174 | 0.5569 |      0.4897 |             0.0257 |                 0.6893 |             8.4719 |           5.7709 |          0.5321 |          0.7716 |    1      |      -0.0161 |    0.1297 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 12600 |    0.6981 |  0.2479 | 0.0168 | 0.5697 |      0.4897 |             0.0103 |                 0.685  |             9.7758 |           7.0676 |          0.5505 |          0.8444 |    1      |      -0.0124 |    0.7781 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  3.2966 |        0.0005 |           0.0076 | False          | nan      |       nan      |     0.0027 |
| H3a          | logit    | rules_tech - hitai_full                                      |  4.9428 |        0      |           0.0154 | False          | nan      |       nan      |     0      |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  5.2483 |        0      |           0.015  | False          | nan      |       nan      |     0      |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  4.1528 |        0      |           0.0086 | False          | nan      |       nan      |     0.0001 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.7497 |        0.0802 |         nan      | False          | nan      |       nan      |     0.147  |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0164 |        0.2262 |         nan      | False          | nan      |       nan      |     0.3317 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.861  |        0.3892 |           0.0018 | False          | nan      |       nan      |     0.4757 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -0.1869 |        0.5741 |          -0.0005 | False          | nan      |       nan      |     0.6015 |
| H3a          | gbt      | rules_tech - hitai_full                                      | -0.1191 |        0.5474 |          -0.0003 | False          | nan      |       nan      |     0.6015 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  0.6614 |        0.2542 |           0.0021 | False          | nan      |       nan      |     0.3495 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  0.3367 |        0.3682 |           0.001  | False          | nan      |       nan      |     0.4757 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.1667 |        0.0015 |         nan      | False          | nan      |       nan      |     0.0068 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0578 |        0.0039 |         nan      | False          | nan      |       nan      |     0.0124 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.3628 |        0.7167 |           0.0007 | False          | nan      |       nan      |     0.7167 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  0.9135 |        0.1805 |           0.0024 | True           |   0.1805 |         0.9024 |     0.2836 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  1.8978 |        0.0289 |           0.0053 | True           |   0.1154 |         0.1443 |     0.0705 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  1.7166 |        0.043  |           0.0047 | True           |   0.1291 |         0.2151 |     0.0933 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  1.678  |        0.0467 |           0.0044 | True           |   0.1291 |         0.2334 |     0.0933 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.9072 |        0.0036 |         nan      | False          | nan      |       nan      |     0.0124 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0492 |        0.0119 |         nan      | True           |   0.0595 |         0.0595 |     0.0327 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.7082 |        0.0876 |           0.0061 | False          | nan      |       nan      |     0.1482 |
| H4b          | tagger   | corr(tag,fwd) original=0.1636 vs perturbed-context (want ~0) |  0.0048 |        0.4832 |           0.1587 | False          | nan      |       nan      |     0.5595 |

## Reality check / SPA vs rules_only: RC p=0.037, SPA p=0.007

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5136 |    0.6932 |  0.25   | 0.0065 | 0.5    |      0.5006 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 5136 |    0.6946 |  0.2507 | 0.0056 | 0.5043 |      0.5006 |          -2.2202 |    0.0079 |
| hitai_full|pit|gbt_mono      | 5136 |    0.681  |  0.2436 | 0.0327 | 0.5982 |      0.5006 |          10.0787 |    1      |
| hitai_full|shuffled|gbt_mono | 5136 |    0.6953 |  0.2509 | 0.0062 | 0.5098 |      0.5006 |          -1.6615 |    0.0353 |
