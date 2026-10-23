# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 10488, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6300 |    0.6985 |  0.2526 | 0.0507 | 0.4827 |      0.5041 |             0.0142 |                 0.6938 |            -0.5219 |          -1.0819 |          0.126  |          0.4441 |    0.0573 |      -0.1966 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6300 |    0.6973 |  0.252  | 0.0458 | 0.486  |      0.5041 |             0.0224 |                 0.695  |            -0.6368 |          -1.2003 |          0.1292 |          0.4605 |    0.0408 |      -0.2127 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6300 |    0.6967 |  0.2518 | 0.0441 | 0.4868 |      0.5041 |             0.0043 |                 0.6929 |            -0.724  |          -0.8562 |          0.0292 |          0.4178 |    0.1061 |      -0.1527 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6300 |    0.7252 |  0.2563 | 0.0554 | 0.4751 |      0.5041 |             0.0281 |                 0.6966 |            -0.6782 |          -1.1318 |          0.1248 |          0.7327 |    0.0496 |      -0.2108 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6300 |    0.7011 |  0.2526 | 0.0442 | 0.4899 |      0.5041 |             0.0502 |                 0.7034 |            -0.6096 |          -1.2942 |          0.1813 |          0.6324 |    0.029  |      -0.2571 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6300 |    0.7055 |  0.2528 | 0.0384 | 0.4861 |      0.5041 |             0.0393 |                 0.6975 |            -0.3837 |          -0.8504 |          0.1305 |          0.7322 |    0.109  |      -0.183  |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6300 |    0.7144 |  0.2549 | 0.0513 | 0.4762 |      0.5041 |             0.0239 |                 0.6971 |            -1.0811 |          -1.7097 |          0.1678 |          0.6941 |    0.0067 |      -0.2917 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6300 |    0.7025 |  0.2527 | 0.0462 | 0.4894 |      0.5041 |             0.0489 |                 0.7037 |            -0.6288 |          -1.2889 |          0.1743 |          0.6443 |    0.0302 |      -0.2494 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6300 |    0.7055 |  0.2528 | 0.0384 | 0.4861 |      0.5041 |             0.0393 |                 0.6975 |            -0.3837 |          -0.8504 |          0.1305 |          0.7322 |    0.109  |      -0.183  |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6300 |    0.6947 |  0.2499 | 0.0264 | 0.5488 |      0.5041 |             0.0115 |                 0.689  |             4.6895 |           2.9452 |          0.5073 |          0.8663 |    1      |      -0.0538 |    0.2515 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6300 |    0.6995 |  0.2502 | 0.0324 | 0.5407 |      0.5041 |             0.0358 |                 0.694  |             3.2264 |           1.7767 |          0.4189 |          0.8351 |    0.9948 |      -0.0568 |    0.009  |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6300 |    0.6917 |  0.2488 | 0.0272 | 0.5487 |      0.5041 |             0.0164 |                 0.6902 |             3.8239 |           2.4477 |          0.4105 |          0.8805 |    0.9998 |      -0.0594 |    0.0808 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6300 |    0.7081 |  0.2541 | 0.0512 | 0.478  |      0.5041 |             0.0301 |                 0.6976 |            -0.8685 |          -1.6447 |          0.1983 |          0.6727 |    0.0092 |      -0.2654 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6300 |    0.6986 |  0.2519 | 0.0403 | 0.4949 |      0.5041 |             0.0529 |                 0.7023 |            -0.5768 |          -1.2595 |          0.1694 |          0.5414 |    0.0336 |      -0.2306 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6300 |    0.7036 |  0.2525 | 0.0401 | 0.4843 |      0.5041 |             0.0362 |                 0.6974 |            -0.5918 |          -1.052  |          0.1321 |          0.8014 |    0.064  |      -0.2251 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6300 |    0.7153 |  0.2549 | 0.0543 | 0.4786 |      0.5041 |             0.0323 |                 0.6981 |            -0.656  |          -1.3147 |          0.1751 |          0.693  |    0.0285 |      -0.2244 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6300 |    0.7026 |  0.2524 | 0.0318 | 0.4912 |      0.5041 |             0.0562 |                 0.7039 |            -0.8872 |          -1.4519 |          0.1368 |          0.5235 |    0.0168 |      -0.2444 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6300 |    0.7018 |  0.2525 | 0.0343 | 0.4849 |      0.5041 |             0.0385 |                 0.6981 |            -0.3987 |          -0.727  |          0.0883 |          0.6781 |    0.1464 |      -0.1743 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6300 |    0.7048 |  0.2505 | 0.0279 | 0.5444 |      0.5041 |             0.0151 |                 0.6875 |             5.013  |           3.128  |          0.5819 |          0.9854 |    1      |      -0.0396 |    0.3373 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6300 |    0.7028 |  0.2516 | 0.0316 | 0.5378 |      0.5041 |             0.0336 |                 0.6935 |             2.9969 |           1.6697 |          0.4165 |          0.9573 |    0.9917 |      -0.089  |    0.006  |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6300 |    0.6976 |  0.2493 | 0.0153 | 0.5506 |      0.5041 |             0.013  |                 0.6881 |             4.7662 |           3.3259 |          0.4606 |          0.9613 |    1      |      -0.067  |    0.4476 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  1.3398 |        0.0902 |           0.0038 | False          | nan      |       nan      |     0.1322 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.583  |        0.0049 |           0.0196 | False          | nan      |       nan      |     0.016  |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.5696 |        0.0051 |           0.0134 | False          | nan      |       nan      |     0.016  |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.8043 |        0.0025 |           0.0205 | False          | nan      |       nan      |     0.0111 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.0223 |        0.0431 |         nan      | False          | nan      |       nan      |     0.073  |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0581 |        0.0296 |         nan      | False          | nan      |       nan      |     0.0592 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  2.2396 |        0.0251 |           0.01   | False          | nan      |       nan      |     0.0553 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -0.5296 |        0.7018 |          -0.0022 | False          | nan      |       nan      |     0.7018 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  1.2166 |        0.1119 |           0.003  | False          | nan      |       nan      |     0.1538 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       | -0.2383 |        0.5942 |          -0.0008 | False          | nan      |       nan      |     0.6225 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  0.7374 |        0.2305 |           0.0032 | False          | nan      |       nan      |     0.2982 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.3695 |        0.0178 |         nan      | False          | nan      |       nan      |     0.0435 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0899 |        0.0017 |         nan      | False          | nan      |       nan      |     0.0095 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.7681 |        0.4424 |           0.0033 | False          | nan      |       nan      |     0.5123 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  2.2118 |        0.0135 |           0.005  | True           |   0.027  |         0.0674 |     0.0371 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  4.0339 |        0      |           0.0138 | True           |   0.0001 |         0.0001 |     0.0006 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  3.6481 |        0.0001 |           0.0119 | True           |   0.0005 |         0.0007 |     0.0015 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  3.3054 |        0.0005 |           0.0101 | True           |   0.0014 |         0.0024 |     0.0035 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.0891 |        0.2761 |         nan      | False          | nan      |       nan      |     0.3375 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0549 |        0.0373 |         nan      | True           |   0.0373 |         0.1867 |     0.0684 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.7819 |        0.0748 |           0.0059 | False          | nan      |       nan      |     0.1175 |
| H4b          | tagger   | corr(tag,fwd) original=0.1586 vs perturbed-context (want ~0) |  0.0063 |        0.5168 |           0.1523 | False          | nan      |       nan      |     0.5684 |

## Reality check / SPA vs rules_only: RC p=0.627, SPA p=0.047

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2568 |    0.6976 |  0.2522 | 0.0391 | 0.4823 |      0.5039 |          -1.701  |    0.0545 |
| rules_tech|pit|gbt_mono      | 2568 |    0.713  |  0.2571 | 0.0554 | 0.4854 |      0.5039 |          -1.9053 |    0.0432 |
| hitai_full|pit|gbt_mono      | 2568 |    0.6926 |  0.2486 | 0.0276 | 0.5615 |      0.5039 |           3.5277 |    0.9991 |
| hitai_full|shuffled|gbt_mono | 2568 |    0.713  |  0.2571 | 0.0554 | 0.4854 |      0.5039 |          -1.9053 |    0.0432 |
