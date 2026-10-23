# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6936 |  0.2502 | 0.007  | 0.4916 |      0.5121 |             0.0082 |                 0.6933 |             0.5627 |          -0.4101 |          0.1037 |          0.2618 |    0.1964 |      -0.0736 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6935 |  0.2502 | 0.0079 | 0.4992 |      0.5121 |             0.0166 |                 0.6934 |             0.748  |          -0.1292 |          0.1081 |          0.3445 |    0.3937 |      -0.091  |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6932 |  0.25   | 0.0075 | 0.5    |      0.5121 |             0.0082 |                 0.6932 |             0.7341 |           0.0964 |          0.0732 |          0.3266 |    0.5799 |      -0.0569 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6949 |  0.2504 | 0.0111 | 0.501  |      0.5121 |             0.0082 |                 0.6931 |             0.8937 |          -0.6416 |          0.1979 |          0.4082 |    0.0907 |      -0.1271 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6957 |  0.2504 | 0.0193 | 0.5096 |      0.5121 |             0.0305 |                 0.6954 |             1.1499 |          -0.321  |          0.2386 |          0.5678 |    0.2515 |      -0.1317 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6956 |  0.2505 | 0.0163 | 0.513  |      0.5121 |             0.0123 |                 0.6936 |             0.9093 |          -0.7831 |          0.2717 |          0.5648 |    0.0507 |      -0.1463 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6949 |  0.2506 | 0.0119 | 0.4963 |      0.5121 |             0.0134 |                 0.6935 |             0.6126 |          -0.7641 |          0.153  |          0.3194 |    0.0564 |      -0.1072 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6954 |  0.2504 | 0.0197 | 0.5089 |      0.5121 |             0.0306 |                 0.6954 |             1.1766 |          -0.4623 |          0.2597 |          0.5447 |    0.1676 |      -0.1325 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6956 |  0.2505 | 0.0163 | 0.513  |      0.5121 |             0.0123 |                 0.6936 |             0.9093 |          -0.7831 |          0.2717 |          0.5648 |    0.0507 |      -0.1463 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6893 |  0.2468 | 0.0133 | 0.5707 |      0.5121 |             0.0175 |                 0.6856 |             9.7564 |           6.8939 |          0.5453 |          0.841  |    1      |      -0.0174 |    0.7417 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6862 |  0.2464 | 0.0124 | 0.5723 |      0.5121 |             0.0205 |                 0.6861 |             8.8933 |           6.0579 |          0.5184 |          0.7625 |    1      |      -0.0162 |    0.1518 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6872 |  0.2461 | 0.0142 | 0.5752 |      0.5121 |             0.019  |                 0.6846 |             9.3685 |           6.7132 |          0.5268 |          0.8585 |    1      |      -0.0163 |    0.6104 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6949 |  0.2505 | 0.0116 | 0.4973 |      0.5121 |             0.0121 |                 0.6935 |             0.7104 |          -0.9354 |          0.186  |          0.3506 |    0.0261 |      -0.1201 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.695  |  0.2503 | 0.0173 | 0.5106 |      0.5121 |             0.0294 |                 0.6954 |             0.9018 |          -0.8306 |          0.2783 |          0.5739 |    0.0421 |      -0.1778 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6961 |  0.2505 | 0.0163 | 0.5122 |      0.5121 |             0.0129 |                 0.6936 |             0.9947 |          -0.7109 |          0.2768 |          0.5895 |    0.0689 |      -0.1436 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6952 |  0.2506 | 0.0105 | 0.4982 |      0.5121 |             0.0141 |                 0.6937 |             0.5878 |          -0.6922 |          0.1457 |          0.3327 |    0.0754 |      -0.1205 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.695  |  0.2503 | 0.0134 | 0.5105 |      0.5121 |             0.0307 |                 0.6955 |             0.8855 |          -0.6556 |          0.2392 |          0.5356 |    0.0859 |      -0.1476 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6977 |  0.2508 | 0.0163 | 0.5127 |      0.5121 |             0.0113 |                 0.6937 |             0.8025 |          -0.8859 |          0.2709 |          0.5942 |    0.0322 |      -0.1717 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6875 |  0.2465 | 0.0127 | 0.5705 |      0.5121 |             0.0165 |                 0.6855 |            10.0713 |           7.1625 |          0.536  |          0.8317 |    1      |      -0.0206 |    0.8801 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6869 |  0.2465 | 0.0141 | 0.5709 |      0.5121 |             0.0177 |                 0.6865 |             9.0678 |           6.2854 |          0.5255 |          0.8408 |    1      |      -0.0222 |    0.279  |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6867 |  0.2461 | 0.0126 | 0.5747 |      0.5121 |             0.0135 |                 0.6846 |            10.279  |           7.4255 |          0.5455 |          0.8582 |    1      |      -0.0158 |    0.9551 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  2.6634 |        0.0039 |           0.0043 | False          | nan      |       nan      |     0.005  |
| H3a          | logit    | rules_tech - hitai_full                                      |  3.4833 |        0.0002 |           0.0056 | False          | nan      |       nan      |     0.0004 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  3.5208 |        0.0002 |           0.0055 | False          | nan      |       nan      |     0.0004 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  3.718  |        0.0001 |           0.0059 | False          | nan      |       nan      |     0.0002 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.6291 |        0.0003 |         nan      | False          | nan      |       nan      |     0.0004 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0661 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.8251 |        0.068  |          -0.0018 | False          | nan      |       nan      |     0.0787 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  5.0857 |        0      |           0.0073 | False          | nan      |       nan      |     0      |
| H3a          | gbt      | rules_tech - hitai_full                                      |  6.8752 |        0      |           0.0092 | False          | nan      |       nan      |     0      |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  6.2245 |        0      |           0.0089 | False          | nan      |       nan      |     0      |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  6.4371 |        0      |           0.0088 | False          | nan      |       nan      |     0      |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.5514 |        0.0107 |         nan      | False          | nan      |       nan      |     0.0131 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0645 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.8991 |        0.3686 |           0.0008 | False          | nan      |       nan      |     0.4055 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  3.7695 |        0.0001 |           0.006  | True           |   0.0001 |         0.0004 |     0.0002 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  5.3797 |        0      |           0.0084 | True           |   0      |         0      |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  5.6091 |        0      |           0.009  | True           |   0      |         0      |     0      |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  6.4035 |        0      |           0.0105 | True           |   0      |         0      |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.9708 |        0.003  |         nan      | False          | nan      |       nan      |     0.0041 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.074  |        0      |         nan      | True           |   0      |         0      |     0      |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.5554 |        0.5787 |          -0.0005 | False          | nan      |       nan      |     0.5787 |
| H4b          | tagger   | corr(tag,fwd) original=0.1660 vs perturbed-context (want ~0) | -0.003  |        0.5273 |           0.1691 | False          | nan      |       nan      |     0.5524 |

## Reality check / SPA vs rules_only: RC p=0.000, SPA p=0.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6939 |  0.2504 | 0.0194 | 0.4962 |       0.508 |          -0.578  |    0.2207 |
| rules_tech|pit|gbt_mono      | 10896 |    0.6969 |  0.2513 | 0.0129 | 0.4998 |       0.508 |          -1.1542 |    0.0614 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6887 |  0.245  | 0.0163 | 0.5859 |       0.508 |           8.669  |    1      |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6969 |  0.2513 | 0.0129 | 0.4998 |       0.508 |          -1.1542 |    0.0614 |
