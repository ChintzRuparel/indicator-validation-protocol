# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 22008, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 13212 |    0.6954 |  0.2511 | 0.0106 | 0.4917 |      0.5093 |             0.0132 |                 0.6939 |            -0.3258 |          -0.6113 |          0.0559 |          0.3155 |    0.1001 |      -0.167  |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 13212 |    0.6951 |  0.251  | 0.0196 | 0.4963 |      0.5093 |             0.0092 |                 0.6937 |            -0.1775 |          -0.5009 |          0.054  |          0.2329 |    0.146  |      -0.1264 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 13212 |    0.6941 |  0.2505 | 0.0092 | 0.4952 |      0.5093 |             0.0085 |                 0.6935 |            -0.3957 |          -0.5519 |          0.025  |          0.2137 |    0.1229 |      -0.1334 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 13212 |    0.7047 |  0.2527 | 0.0343 | 0.5061 |      0.5093 |             0.0162 |                 0.6935 |             0.9516 |          -0.106  |          0.2235 |          0.4513 |    0.4123 |      -0.096  |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 13212 |    0.7011 |  0.2529 | 0.0292 | 0.4976 |      0.5093 |             0.0518 |                 0.7013 |            -0.5598 |          -1.7892 |          0.3081 |          0.5703 |    0.0001 |      -0.5231 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 13212 |    0.7088 |  0.2529 | 0.0271 | 0.501  |      0.5093 |             0.0285 |                 0.6971 |            -0.0834 |          -1.0504 |          0.2044 |          0.4363 |    0.0137 |      -0.2907 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 13212 |    0.7036 |  0.2521 | 0.0305 | 0.5057 |      0.5093 |             0.0187 |                 0.6939 |             0.8068 |          -0.1589 |          0.2256 |          0.5013 |    0.3699 |      -0.1441 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 13212 |    0.7036 |  0.2533 | 0.03   | 0.4957 |      0.5093 |             0.05   |                 0.7012 |            -0.554  |          -1.6182 |          0.2635 |          0.5437 |    0.0003 |      -0.472  |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 13212 |    0.7113 |  0.2533 | 0.0275 | 0.4999 |      0.5093 |             0.0281 |                 0.6972 |            -0.1748 |          -1.1491 |          0.2173 |          0.4775 |    0.0079 |      -0.3121 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 13212 |    0.6968 |  0.2483 | 0.0279 | 0.5751 |      0.5093 |             0.0157 |                 0.6831 |             6.4725 |           4.7521 |          0.5085 |          0.886  |    1      |      -0.0502 |    0.5194 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 13212 |    0.6927 |  0.2482 | 0.0213 | 0.5661 |      0.5093 |             0.0233 |                 0.6875 |             5.3007 |           3.6245 |          0.4959 |          0.7996 |    1      |      -0.0445 |    0.0107 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 13212 |    0.6892 |  0.2467 | 0.0198 | 0.5739 |      0.5093 |             0.0101 |                 0.6843 |             6.0249 |           4.3036 |          0.5029 |          0.8389 |    1      |      -0.0363 |    0.1914 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 13212 |    0.7009 |  0.2522 | 0.0378 | 0.4979 |      0.5093 |             0.0287 |                 0.695  |             0.4616 |          -0.7961 |          0.3315 |          0.632  |    0.0489 |      -0.2766 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 13212 |    0.7006 |  0.2529 | 0.0281 | 0.4931 |      0.5093 |             0.0507 |                 0.7018 |            -0.466  |          -1.6047 |          0.248  |          0.4437 |    0.0004 |      -0.4298 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 13212 |    0.7127 |  0.2534 | 0.0228 | 0.4988 |      0.5093 |             0.0287 |                 0.6975 |             0.2761 |          -0.9573 |          0.2682 |          0.4741 |    0.0224 |      -0.2753 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 13212 |    0.702  |  0.2521 | 0.0292 | 0.5079 |      0.5093 |             0.0211 |                 0.6938 |             0.7123 |          -0.2219 |          0.2265 |          0.5558 |    0.3214 |      -0.1264 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 13212 |    0.7016 |  0.2529 | 0.027  | 0.4976 |      0.5093 |             0.0477 |                 0.7002 |            -0.7149 |          -1.8551 |          0.2646 |          0.4797 |    0      |      -0.5161 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 13212 |    0.7058 |  0.2525 | 0.0278 | 0.5011 |      0.5093 |             0.0294 |                 0.697  |            -0.2304 |          -1.2576 |          0.226  |          0.4545 |    0.004  |      -0.3368 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 13212 |    0.6983 |  0.2476 | 0.0198 | 0.5781 |      0.5093 |             0.0128 |                 0.6829 |             6.6941 |           4.9977 |          0.4946 |          0.8699 |    1      |      -0.0369 |    0.7091 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 13212 |    0.6914 |  0.2481 | 0.0275 | 0.5681 |      0.5093 |             0.0264 |                 0.6873 |             4.834  |           3.23   |          0.479  |          0.8424 |    1      |      -0.0574 |    0.001  |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 13212 |    0.6886 |  0.2467 | 0.023  | 0.576  |      0.5093 |             0.0091 |                 0.6838 |             6.0316 |           4.3302 |          0.4772 |          0.8014 |    1      |      -0.045  |    0.2057 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -0.4967 |        0.6903 |          -0.0015 | False          | nan      |       nan      |     0.7593 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.053  |        0.02   |           0.0067 | False          | nan      |       nan      |     0.0315 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  1.2463 |        0.1063 |           0.004  | False          | nan      |       nan      |     0.1462 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  1.6587 |        0.0486 |           0.0052 | False          | nan      |       nan      |     0.0713 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.6559 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0684 |        0.0007 |         nan      | False          | nan      |       nan      |     0.0016 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.4361 |        0.6627 |           0.0014 | False          | nan      |       nan      |     0.7593 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  0.9856 |        0.1622 |           0.0024 | False          | nan      |       nan      |     0.2099 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  3.754  |        0.0001 |           0.0109 | False          | nan      |       nan      |     0.0003 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  2.9124 |        0.0018 |           0.0079 | False          | nan      |       nan      |     0.0039 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  3.4325 |        0.0003 |           0.0089 | False          | nan      |       nan      |     0.0008 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.6321 |        0.0085 |         nan      | False          | nan      |       nan      |     0.0156 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0877 |        0      |         nan      | False          | nan      |       nan      |     0.0001 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.8031 |        0.4219 |          -0.0013 | False          | nan      |       nan      |     0.5157 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  2.1744 |        0.0148 |           0.0049 | True           |   0.0148 |         0.0742 |     0.0251 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  5.147  |        0      |           0.0222 | True           |   0      |         0      |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  5.4214 |        0      |           0.0235 | True           |   0      |         0      |     0      |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  4.7994 |        0      |           0.0166 | True           |   0      |         0      |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.0191 |        0.0025 |         nan      | False          | nan      |       nan      |     0.0051 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0836 |        0      |         nan      | True           |   0.0001 |         0.0002 |     0.0002 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.3077 |        0.7583 |          -0.0006 | False          | nan      |       nan      |     0.7944 |
| H4b          | tagger   | corr(tag,fwd) original=0.1724 vs perturbed-context (want ~0) |  0.0012 |        0.8588 |           0.1712 | False          | nan      |       nan      |     0.8588 |

## Reality check / SPA vs rules_only: RC p=0.257, SPA p=0.030

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5448 |    0.6941 |  0.2505 | 0.0225 | 0.5039 |      0.5057 |          -1.0334 |    0.0833 |
| rules_tech|pit|gbt_mono      | 5448 |    0.6948 |  0.2508 | 0.0223 | 0.4987 |      0.5057 |          -0.6252 |    0.2014 |
| hitai_full|pit|gbt_mono      | 5448 |    0.6808 |  0.2435 | 0.019  | 0.5929 |      0.5057 |           5.2621 |    1      |
| hitai_full|shuffled|gbt_mono | 5448 |    0.6945 |  0.2506 | 0.0204 | 0.4989 |      0.5057 |          -0.5788 |    0.2196 |
