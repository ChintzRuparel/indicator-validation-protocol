# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 20976, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 12600 |    0.6956 |  0.2508 | 0.0125 | 0.5044 |      0.4926 |             0.0182 |                 0.6942 |            -0.4424 |          -1.3062 |          0.0984 |          0.2543 |    0.0277 |      -0.098  |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 12600 |    0.6952 |  0.251  | 0.0134 | 0.5006 |      0.4926 |             0.0188 |                 0.6946 |            -0.1851 |          -1.3033 |          0.141  |          0.3448 |    0.0291 |      -0.1012 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 12600 |    0.6942 |  0.2505 | 0.0145 | 0.4999 |      0.4926 |             0.0233 |                 0.6941 |            -0.0185 |          -1.1683 |          0.1637 |          0.4256 |    0.0436 |      -0.1128 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 12600 |    0.697  |  0.2515 | 0.0165 | 0.497  |      0.4926 |             0.0308 |                 0.6955 |            -0.1266 |          -1.4748 |          0.1903 |          0.4065 |    0.0153 |      -0.1458 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 12600 |    0.6961 |  0.2509 | 0.0231 | 0.4964 |      0.4926 |             0.056  |                 0.7033 |            -0.0104 |          -1.3632 |          0.2204 |          0.5775 |    0.0217 |      -0.1923 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 12600 |    0.6978 |  0.2512 | 0.0203 | 0.5024 |      0.4926 |             0.0337 |                 0.6976 |             0.6532 |          -0.38   |          0.179  |          0.5967 |    0.2911 |      -0.1019 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 12600 |    0.6969 |  0.2513 | 0.0174 | 0.4927 |      0.4926 |             0.0311 |                 0.6958 |            -0.1149 |          -1.36   |          0.1606 |          0.2926 |    0.0222 |      -0.1234 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 12600 |    0.6952 |  0.2506 | 0.0193 | 0.5031 |      0.4926 |             0.0544 |                 0.7031 |             0.6499 |          -0.6928 |          0.1993 |          0.4747 |    0.1573 |      -0.1298 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 12600 |    0.6976 |  0.2511 | 0.0198 | 0.504  |      0.4926 |             0.0341 |                 0.6975 |             0.8777 |          -0.2187 |          0.1936 |          0.624  |    0.376  |      -0.1032 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 12600 |    0.6923 |  0.2463 | 0.0185 | 0.5768 |      0.4926 |             0.0213 |                 0.6835 |            10.4136 |           7.745  |          0.552  |          0.9162 |    1      |      -0.0162 |    0.9556 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 12600 |    0.6875 |  0.2469 | 0.013  | 0.5697 |      0.4926 |             0.0298 |                 0.6885 |             7.4184 |           4.8608 |          0.5379 |          0.8605 |    1      |      -0.0394 |    0.0149 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 12600 |    0.6897 |  0.2461 | 0.0222 | 0.5802 |      0.4926 |             0.0194 |                 0.6839 |             8.7864 |           6.1814 |          0.5329 |          0.8595 |    1      |      -0.0198 |    0.3605 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 12600 |    0.6964 |  0.2509 | 0.0176 | 0.4931 |      0.4926 |             0.0397 |                 0.6964 |            -1.0049 |          -2.4731 |          0.2333 |          0.4729 |    0.0001 |      -0.2171 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 12600 |    0.6953 |  0.2508 | 0.0195 | 0.4983 |      0.4926 |             0.0579 |                 0.7032 |             0.1454 |          -1.0646 |          0.1554 |          0.3555 |    0.0617 |      -0.0993 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 12600 |    0.698  |  0.2515 | 0.025  | 0.5001 |      0.4926 |             0.0339 |                 0.6976 |             0.474  |          -0.6506 |          0.1807 |          0.4917 |    0.1716 |      -0.0971 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 12600 |    0.6977 |  0.2511 | 0.0139 | 0.5026 |      0.4926 |             0.0337 |                 0.6964 |             0.419  |          -1.104  |          0.2163 |          0.3617 |    0.0534 |      -0.1085 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 12600 |    0.6954 |  0.2507 | 0.0203 | 0.5023 |      0.4926 |             0.0587 |                 0.704  |             0.5231 |          -1.0156 |          0.2154 |          0.4133 |    0.0701 |      -0.1056 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 12600 |    0.6984 |  0.2513 | 0.0222 | 0.5029 |      0.4926 |             0.0338 |                 0.6977 |             0.6459 |          -0.6016 |          0.205  |          0.5444 |    0.1916 |      -0.098  |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 12600 |    0.6859 |  0.2459 | 0.0102 | 0.576  |      0.4926 |             0.0205 |                 0.6832 |             9.0897 |           6.4175 |          0.5456 |          0.861  |    1      |      -0.0222 |    0.4796 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 12600 |    0.6908 |  0.2475 | 0.0222 | 0.5629 |      0.4926 |             0.0315 |                 0.6895 |             6.9829 |           4.1978 |          0.541  |          0.8435 |    1      |      -0.0233 |    0.0007 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 12600 |    0.692  |  0.2471 | 0.0184 | 0.5744 |      0.4926 |             0.0197 |                 0.6847 |             9.2112 |           6.4631 |          0.5156 |          0.8491 |    1      |      -0.0164 |    0.5045 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  0.9935 |        0.1602 |           0.0034 | False          | nan      |       nan      |     0.1958 |
| H3a          | logit    | rules_tech - hitai_full                                      |  1.3754 |        0.0845 |           0.0046 | False          | nan      |       nan      |     0.1239 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  1.2125 |        0.1127 |           0.0042 | False          | nan      |       nan      |     0.1458 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  1.5671 |        0.0586 |           0.0054 | False          | nan      |       nan      |     0.0991 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.6349 |        0.1021 |         nan      | False          | nan      |       nan      |     0.1404 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0472 |        0.0151 |         nan      | False          | nan      |       nan      |     0.0332 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -2.2071 |        0.0273 |          -0.0064 | False          | nan      |       nan      |     0.0546 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  4.054  |        0      |           0.0078 | False          | nan      |       nan      |     0.0001 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  4.4534 |        0      |           0.0077 | False          | nan      |       nan      |     0      |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  4.3192 |        0      |           0.0078 | False          | nan      |       nan      |     0      |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  4.4845 |        0      |           0.0079 | False          | nan      |       nan      |     0      |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  0.638  |        0.5235 |         nan      | False          | nan      |       nan      |     0.5235 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.1192 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  2.0129 |        0.0441 |           0.0034 | False          | nan      |       nan      |     0.0809 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  1.4263 |        0.0769 |           0.0044 | True           |   0.0769 |         0.3844 |     0.1208 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  2.6235 |        0.0044 |           0.0079 | True           |   0.009  |         0.0218 |     0.0106 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  2.8422 |        0.0022 |           0.0083 | True           |   0.009  |         0.0112 |     0.0069 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  2.8075 |        0.0025 |           0.0087 | True           |   0.009  |         0.0125 |     0.0069 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.0627 |        0.2879 |         nan      | False          | nan      |       nan      |     0.3016 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.1267 |        0      |         nan      | True           |   0      |         0      |     0      |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.272  |        0.2034 |           0.0022 | False          | nan      |       nan      |     0.2355 |
| H4b          | tagger   | corr(tag,fwd) original=0.1835 vs perturbed-context (want ~0) |  0.0081 |        0.2414 |           0.1754 | False          | nan      |       nan      |     0.2656 |

## Reality check / SPA vs rules_only: RC p=0.043, SPA p=0.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5136 |    0.6957 |  0.2513 | 0.0371 | 0.5001 |      0.5105 |          -2.5751 |    0.009  |
| rules_tech|pit|gbt_mono      | 5136 |    0.7009 |  0.2513 | 0.0341 | 0.5117 |      0.5105 |          -1.5195 |    0.0793 |
| hitai_full|pit|gbt_mono      | 5136 |    0.6922 |  0.2472 | 0.0365 | 0.5867 |      0.5105 |           7.0473 |    1      |
| hitai_full|shuffled|gbt_mono | 5136 |    0.7021 |  0.2514 | 0.0335 | 0.5107 |      0.5105 |          -1.6843 |    0.0581 |
