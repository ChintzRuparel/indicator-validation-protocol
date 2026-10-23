# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 11004, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6606 |    0.6955 |  0.2512 | 0.0195 | 0.4853 |        0.51 |             0.0139 |                 0.6939 |            -0.2278 |          -0.6881 |          0.1338 |          0.5492 |    0.075  |      -0.2554 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6606 |    0.6969 |  0.2519 | 0.0234 | 0.4803 |        0.51 |             0.0231 |                 0.695  |            -0.4002 |          -0.7354 |          0.0966 |          0.5413 |    0.0613 |      -0.2603 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6606 |    0.6969 |  0.2518 | 0.0183 | 0.4899 |        0.51 |             0.0121 |                 0.6938 |            -0.128  |          -0.6071 |          0.1253 |          0.4423 |    0.1007 |      -0.2216 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6606 |    0.7053 |  0.2529 | 0.0435 | 0.4948 |        0.51 |             0.0236 |                 0.6962 |            -0.1709 |          -0.5915 |          0.1061 |          0.3571 |    0.109  |      -0.2893 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6606 |    0.6973 |  0.2517 | 0.0337 | 0.4867 |        0.51 |             0.0616 |                 0.7054 |            -0.0711 |          -0.6515 |          0.1789 |          0.6048 |    0.0868 |      -0.2472 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6606 |    0.6965 |  0.2516 | 0.0266 | 0.4927 |        0.51 |             0.0339 |                 0.6975 |             0.1557 |          -0.2437 |          0.1272 |          0.6066 |    0.3055 |      -0.183  |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6606 |    0.7166 |  0.2538 | 0.0472 | 0.5039 |        0.51 |             0.0275 |                 0.6959 |             0.7318 |           0.1796 |          0.1821 |          0.6479 |    0.6463 |      -0.1459 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6606 |    0.6973 |  0.2517 | 0.0335 | 0.4868 |        0.51 |             0.0615 |                 0.7054 |            -0.0711 |          -0.6515 |          0.1789 |          0.6048 |    0.0868 |      -0.2472 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6606 |    0.6964 |  0.2515 | 0.0266 | 0.4917 |        0.51 |             0.0346 |                 0.6975 |             0.2129 |          -0.1865 |          0.1275 |          0.6097 |    0.3485 |      -0.1631 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6606 |    0.7038 |  0.2491 | 0.0297 | 0.5681 |        0.51 |             0.0193 |                 0.6869 |             4.0964 |           2.783  |          0.4717 |          0.8294 |    1      |      -0.0789 |    0.6659 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6606 |    0.6952 |  0.2493 | 0.0152 | 0.546  |        0.51 |             0.0418 |                 0.6968 |             3.3627 |           1.8713 |          0.5649 |          0.8627 |    0.9999 |      -0.0766 |    0.076  |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6606 |    0.6978 |  0.2492 | 0.0212 | 0.5574 |        0.51 |             0.0194 |                 0.6881 |             3.7452 |           2.3588 |          0.5198 |          0.8411 |    1      |      -0.0799 |    0.3319 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6606 |    0.7071 |  0.2531 | 0.0482 | 0.5044 |        0.51 |             0.0316 |                 0.6966 |             0.6126 |          -0.0578 |          0.2274 |          0.7092 |    0.4519 |      -0.2277 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6606 |    0.6979 |  0.2519 | 0.0369 | 0.4874 |        0.51 |             0.0613 |                 0.7059 |             0.0372 |          -0.6349 |          0.2483 |          0.7477 |    0.0925 |      -0.2938 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6606 |    0.6978 |  0.2519 | 0.0313 | 0.4866 |        0.51 |             0.0313 |                 0.6974 |             0.1396 |          -0.1805 |          0.0996 |          0.5854 |    0.3532 |      -0.2002 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6606 |    0.7031 |  0.252  | 0.0303 | 0.5025 |        0.51 |             0.0308 |                 0.6966 |             0.3796 |          -0.3457 |          0.2257 |          0.5218 |    0.2358 |      -0.2372 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6606 |    0.7019 |  0.2524 | 0.0358 | 0.4885 |        0.51 |             0.0595 |                 0.7045 |            -0.3377 |          -1.0769 |          0.2351 |          0.5875 |    0.0119 |      -0.4109 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6606 |    0.7045 |  0.2521 | 0.0321 | 0.49   |        0.51 |             0.0373 |                 0.6972 |             0.0676 |          -0.3599 |          0.1338 |          0.5727 |    0.2259 |      -0.239  |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6606 |    0.7074 |  0.2495 | 0.0226 | 0.5615 |        0.51 |             0.0348 |                 0.688  |             4.0499 |           2.704  |          0.4821 |          0.7593 |    1      |      -0.0709 |    0.607  |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6606 |    0.6938 |  0.2488 | 0.0127 | 0.552  |        0.51 |             0.0422 |                 0.695  |             3.2683 |           1.8984 |          0.4809 |          0.767  |    1      |      -0.0707 |    0.0817 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6606 |    0.6944 |  0.2482 | 0.0172 | 0.5598 |        0.51 |             0.0214 |                 0.6881 |             3.7242 |           2.4526 |          0.4843 |          0.8288 |    1      |      -0.0794 |    0.4021 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -1.4016 |        0.9195 |          -0.0083 | False          | nan      |       nan      |     0.9195 |
| H3a          | logit    | rules_tech - hitai_full                                      |  1.5383 |        0.062  |           0.0128 | False          | nan      |       nan      |     0.2273 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  0.4625 |        0.3219 |           0.0034 | False          | nan      |       nan      |     0.5937 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         | -0.0966 |        0.5385 |          -0.0007 | False          | nan      |       nan      |     0.6376 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.2032 |        0.0014 |         nan      | False          | nan      |       nan      |     0.0135 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0874 |        0.0018 |         nan      | False          | nan      |       nan      |     0.0135 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.7406 |        0.4589 |           0.0036 | False          | nan      |       nan      |     0.6376 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  0.5391 |        0.2949 |           0.0017 | False          | nan      |       nan      |     0.5937 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  0.7121 |        0.2382 |           0.0021 | False          | nan      |       nan      |     0.5822 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  0.9309 |        0.1759 |           0.0028 | False          | nan      |       nan      |     0.4839 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  2.1277 |        0.0167 |           0.0067 | False          | nan      |       nan      |     0.0734 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.6159 |        0.0089 |         nan      | False          | nan      |       nan      |     0.0489 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0033 |        0.4563 |         nan      | False          | nan      |       nan      |     0.6376 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.5548 |        0.579  |          -0.0014 | False          | nan      |       nan      |     0.6376 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -0.2009 |        0.5796 |          -0.0008 | True           |   1      |         1      |     0.6376 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      | -0.3387 |        0.6326 |          -0.0013 | True           |   1      |         1      |     0.6627 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  0.0125 |        0.495  |           0.0001 | True           |   1      |         1      |     0.6376 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  1.2792 |        0.1004 |           0.0067 | True           |   0.5021 |         0.5021 |     0.3156 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.1158 |        0.0018 |         nan      | False          | nan      |       nan      |     0.0135 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0022 |        0.4715 |         nan      | True           |   1      |         1      |     0.6376 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.9867 |        0.3238 |          -0.0033 | False          | nan      |       nan      |     0.5937 |
| H4b          | tagger   | corr(tag,fwd) original=0.1643 vs perturbed-context (want ~0) |  0.0073 |        0.4449 |           0.157  | False          | nan      |       nan      |     0.6376 |

## Reality check / SPA vs rules_only: RC p=0.890, SPA p=0.273

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2724 |    0.6928 |  0.2498 | 0.0108 | 0.5107 |      0.5022 |          -0.9961 |    0.0899 |
| rules_tech|pit|gbt_mono      | 2724 |    0.6922 |  0.2496 | 0.0192 | 0.5089 |      0.5022 |          -0.6913 |    0.1771 |
| hitai_full|pit|gbt_mono      | 2724 |    0.6902 |  0.2478 | 0.0186 | 0.553  |      0.5022 |           1.5524 |    0.9813 |
| hitai_full|shuffled|gbt_mono | 2724 |    0.6941 |  0.2496 | 0.0181 | 0.5108 |      0.5022 |          -0.5472 |    0.2316 |
