# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 22008, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 13212 |    0.6953 |  0.251  | 0.0271 | 0.4961 |      0.4942 |             0.0223 |                 0.6938 |            -0.0389 |          -0.6308 |          0.1423 |          0.4992 |    0.0971 |      -0.1879 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 13212 |    0.6951 |  0.2509 | 0.0301 | 0.4907 |      0.4942 |             0.0234 |                 0.694  |            -0.2588 |          -0.8282 |          0.1249 |          0.418  |    0.0454 |      -0.2256 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 13212 |    0.6943 |  0.2506 | 0.0199 | 0.4906 |      0.4942 |             0.017  |                 0.6937 |            -0.1009 |          -0.1174 |          0.0036 |          0.3996 |    0.4034 |      -0.1102 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 13212 |    0.6968 |  0.2514 | 0.0276 | 0.5027 |      0.4942 |             0.0265 |                 0.6946 |             0.2368 |          -0.5553 |          0.2143 |          0.6546 |    0.1248 |      -0.2184 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 13212 |    0.7003 |  0.2519 | 0.0294 | 0.4976 |      0.4942 |             0.0446 |                 0.6996 |             0.0787 |          -1.0012 |          0.2268 |          0.4056 |    0.0179 |      -0.2571 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 13212 |    0.7045 |  0.2522 | 0.0274 | 0.4994 |      0.4942 |             0.0304 |                 0.6957 |            -0.1001 |          -1.2355 |          0.3004 |          0.6515 |    0.005  |      -0.4111 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 13212 |    0.706  |  0.2522 | 0.0264 | 0.5038 |      0.4942 |             0.0315 |                 0.6947 |             0.2833 |          -0.3963 |          0.1593 |          0.5379 |    0.204  |      -0.1335 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 13212 |    0.6999 |  0.2519 | 0.0354 | 0.4965 |      0.4942 |             0.0464 |                 0.6997 |            -0.2514 |          -1.3823 |          0.2998 |          0.6256 |    0.0019 |      -0.4205 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 13212 |    0.7045 |  0.2522 | 0.0274 | 0.4994 |      0.4942 |             0.0304 |                 0.6957 |            -0.1001 |          -1.2355 |          0.3004 |          0.6515 |    0.005  |      -0.4111 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 13212 |    0.6923 |  0.2463 | 0.0217 | 0.5813 |      0.4942 |             0.0247 |                 0.6828 |             7.3865 |           5.5329 |          0.5386 |          0.8451 |    1      |      -0.0367 |    0.9261 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 13212 |    0.6913 |  0.248  | 0.024  | 0.5621 |      0.4942 |             0.027  |                 0.6873 |             5.0032 |           3.2019 |          0.5192 |          0.8148 |    1      |      -0.046  |    0.0002 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 13212 |    0.6898 |  0.2469 | 0.0261 | 0.5736 |      0.4942 |             0.0201 |                 0.6841 |             6.9243 |           5.051  |          0.5372 |          0.8287 |    1      |      -0.0298 |    0.6654 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 13212 |    0.6992 |  0.2518 | 0.0308 | 0.5064 |      0.4942 |             0.0284 |                 0.6945 |             0.4592 |          -0.6342 |          0.2778 |          0.5816 |    0.0944 |      -0.2377 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 13212 |    0.6987 |  0.2518 | 0.0359 | 0.4994 |      0.4942 |             0.0463 |                 0.6998 |            -0.4558 |          -1.5489 |          0.2871 |          0.5774 |    0.0006 |      -0.4697 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 13212 |    0.7033 |  0.2521 | 0.0297 | 0.4994 |      0.4942 |             0.0298 |                 0.6959 |             0.1827 |          -0.7403 |          0.2379 |          0.5528 |    0.0633 |      -0.2433 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 13212 |    0.707  |  0.2527 | 0.0327 | 0.5004 |      0.4942 |             0.0307 |                 0.6947 |             0.0528 |          -0.8267 |          0.2346 |          0.6916 |    0.0425 |      -0.2761 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 13212 |    0.7013 |  0.2522 | 0.0353 | 0.4964 |      0.4942 |             0.0442 |                 0.6993 |            -0.2423 |          -1.2034 |          0.2698 |          0.6556 |    0.0067 |      -0.3944 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 13212 |    0.7041 |  0.2522 | 0.0289 | 0.4986 |      0.4942 |             0.0297 |                 0.6959 |            -0.2049 |          -1.1961 |          0.2483 |          0.5552 |    0.0074 |      -0.3792 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 13212 |    0.6944 |  0.2466 | 0.0218 | 0.582  |      0.4942 |             0.0223 |                 0.6827 |             6.9726 |           5.0516 |          0.5378 |          0.8352 |    1      |      -0.038  |    0.6697 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 13212 |    0.6887 |  0.2475 | 0.022  | 0.5663 |      0.4942 |             0.0239 |                 0.6866 |             4.9755 |           3.0887 |          0.5012 |          0.7249 |    1      |      -0.0512 |    0.0002 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 13212 |    0.6892 |  0.2468 | 0.0264 | 0.5757 |      0.4942 |             0.0186 |                 0.6837 |             6.2417 |           4.3703 |          0.5166 |          0.7858 |    1      |      -0.0381 |    0.1513 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  0.839  |        0.2007 |           0.003  | False          | nan      |       nan      |     0.2324 |
| H3a          | logit    | rules_tech - hitai_full                                      |  3.0874 |        0.001  |           0.0137 | False          | nan      |       nan      |     0.002  |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.6967 |        0.0035 |           0.0069 | False          | nan      |       nan      |     0.0064 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  3.4023 |        0.0003 |           0.0147 | False          | nan      |       nan      |     0.0008 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.3314 |        0      |         nan      | False          | nan      |       nan      |     0.0002 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0252 |        0.1184 |         nan      | False          | nan      |       nan      |     0.1533 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.0687 |        0.2852 |           0.0021 | False          | nan      |       nan      |     0.3137 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  1.7727 |        0.0381 |           0.0038 | False          | nan      |       nan      |     0.0599 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  3.471  |        0.0003 |           0.0086 | False          | nan      |       nan      |     0.0007 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  3.3492 |        0.0004 |           0.0073 | False          | nan      |       nan      |     0.0009 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  4.1674 |        0      |           0.0099 | False          | nan      |       nan      |     0.0002 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.8319 |        0.0001 |         nan      | False          | nan      |       nan      |     0.0004 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0453 |        0.0166 |         nan      | False          | nan      |       nan      |     0.0281 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.7204 |        0.0854 |          -0.0026 | False          | nan      |       nan      |     0.1174 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  1.6271 |        0.0519 |           0.0045 | True           |   0.1037 |         0.2593 |     0.0761 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  3.6524 |        0.0001 |           0.0147 | True           |   0.0006 |         0.0006 |     0.0004 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  3.6499 |        0.0001 |           0.0135 | True           |   0.0006 |         0.0007 |     0.0004 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  3.6678 |        0.0001 |           0.0143 | True           |   0.0006 |         0.0006 |     0.0004 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.2153 |        0      |         nan      | False          | nan      |       nan      |     0.0002 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0187 |        0.1903 |         nan      | True           |   0.1903 |         0.9514 |     0.2324 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.2647 |        0.7912 |          -0.0006 | False          | nan      |       nan      |     0.7912 |
| H4b          | tagger   | corr(tag,fwd) original=0.1697 vs perturbed-context (want ~0) | -0.0027 |        0.6911 |           0.1723 | False          | nan      |       nan      |     0.724  |

## Reality check / SPA vs rules_only: RC p=0.337, SPA p=0.130

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5448 |    0.6937 |  0.2503 | 0.0214 | 0.5    |       0.513 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 5448 |    0.7206 |  0.2536 | 0.041  | 0.4901 |       0.513 |          -1.6407 |    0.0135 |
| hitai_full|pit|gbt_mono      | 5448 |    0.7062 |  0.2475 | 0.0368 | 0.5829 |       0.513 |           4.9084 |    1      |
| hitai_full|shuffled|gbt_mono | 5448 |    0.7213 |  0.2539 | 0.0365 | 0.4868 |       0.513 |          -1.644  |    0.0132 |
