# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 11004, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6606 |    0.6957 |  0.2512 | 0.0258 | 0.5143 |      0.4938 |             0.0085 |                 0.6927 |             0.2285 |          -0.2103 |          0.1502 |          0.6079 |    0.3306 |      -0.1762 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6606 |    0.6954 |  0.2511 | 0.0231 | 0.5156 |      0.4938 |             0.0087 |                 0.6935 |             0.7545 |           0.3619 |          0.1367 |          0.6182 |    0.7763 |      -0.1826 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6606 |    0.6944 |  0.2506 | 0.0209 | 0.5005 |      0.4938 |             0.0179 |                 0.6939 |             0.1119 |          -0.0589 |          0.0447 |          0.4031 |    0.4511 |      -0.1691 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6606 |    0.713  |  0.2528 | 0.0265 | 0.5165 |      0.4938 |             0.017  |                 0.6931 |             0.1353 |          -0.3313 |          0.1267 |          0.4108 |    0.244  |      -0.2167 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6606 |    0.6978 |  0.2507 | 0.0289 | 0.5041 |      0.4938 |             0.0611 |                 0.706  |             0.0004 |          -0.7471 |          0.1482 |          0.2251 |    0.0593 |      -0.1913 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6606 |    0.6965 |  0.2512 | 0.0224 | 0.5023 |      0.4938 |             0.0354 |                 0.6984 |             0.2726 |          -0.5501 |          0.1795 |          0.2887 |    0.1259 |      -0.2305 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6606 |    0.7122 |  0.2528 | 0.0273 | 0.5062 |      0.4938 |             0.0226 |                 0.6937 |            -0.1961 |          -0.6871 |          0.1483 |          0.4827 |    0.0741 |      -0.3457 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6606 |    0.6969 |  0.2509 | 0.0313 | 0.4975 |      0.4938 |             0.0624 |                 0.7064 |            -0.0661 |          -0.8082 |          0.1527 |          0.2393 |    0.0458 |      -0.2305 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6606 |    0.6965 |  0.2512 | 0.0224 | 0.5023 |      0.4938 |             0.0354 |                 0.6984 |             0.2726 |          -0.5501 |          0.1795 |          0.2887 |    0.1259 |      -0.2305 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6606 |    0.6973 |  0.2452 | 0.0136 | 0.5915 |      0.4938 |             0.0106 |                 0.6798 |             4.7197 |           3.3101 |          0.5574 |          0.8577 |    1      |      -0.1089 |    0.7802 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6606 |    0.6917 |  0.2478 | 0.014  | 0.559  |      0.4938 |             0.0389 |                 0.691  |             2.5068 |           1.1513 |          0.5126 |          0.7946 |    0.9912 |      -0.1607 |    0.0001 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6606 |    0.6933 |  0.2469 | 0.0188 | 0.5778 |      0.4938 |             0.0185 |                 0.6839 |             4.4394 |           3.044  |          0.4973 |          0.7342 |    1      |      -0.1162 |    0.5941 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6606 |    0.7108 |  0.2526 | 0.024  | 0.5107 |      0.4938 |             0.0177 |                 0.6937 |            -0.0401 |          -0.5599 |          0.1393 |          0.4154 |    0.1193 |      -0.2379 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6606 |    0.6999 |  0.2511 | 0.0321 | 0.4941 |      0.4938 |             0.0638 |                 0.706  |            -0.1277 |          -0.7831 |          0.1574 |          0.363  |    0.0498 |      -0.2331 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6606 |    0.6955 |  0.2508 | 0.0232 | 0.5055 |      0.4938 |             0.0334 |                 0.6983 |             0.3338 |          -0.4183 |          0.1435 |          0.256  |    0.1914 |      -0.2146 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6606 |    0.703  |  0.2518 | 0.027  | 0.5018 |      0.4938 |             0.032  |                 0.695  |            -0.1341 |          -0.6817 |          0.1605 |          0.4871 |    0.0752 |      -0.2939 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6606 |    0.6951 |  0.2503 | 0.0297 | 0.501  |      0.4938 |             0.073  |                 0.7064 |            -0.1528 |          -0.9047 |          0.2181 |          0.4186 |    0.0291 |      -0.3469 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6606 |    0.6985 |  0.2512 | 0.024  | 0.5027 |      0.4938 |             0.0421 |                 0.699  |             0.0385 |          -0.5078 |          0.1773 |          0.5801 |    0.1439 |      -0.2783 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6606 |    0.7043 |  0.2456 | 0.0255 | 0.5974 |      0.4938 |             0.014  |                 0.6784 |             4.8841 |           3.5597 |          0.5448 |          0.8968 |    1      |      -0.0892 |    0.8984 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6606 |    0.701  |  0.2481 | 0.0136 | 0.5669 |      0.4938 |             0.0365 |                 0.6887 |             2.5118 |           1.2656 |          0.5118 |          0.8769 |    0.9956 |      -0.1278 |    0.0003 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6606 |    0.6909 |  0.2459 | 0.0167 | 0.5836 |      0.4938 |             0.0138 |                 0.6822 |             4.2469 |           2.875  |          0.5421 |          0.853  |    1      |      -0.0731 |    0.4563 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -0.259  |        0.6022 |          -0.0016 | False          | nan      |       nan      |     0.6022 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.6144 |        0.0045 |           0.0149 | False          | nan      |       nan      |     0.0328 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.4593 |        0.007  |           0.0135 | False          | nan      |       nan      |     0.0383 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  1.1801 |        0.119  |           0.0057 | False          | nan      |       nan      |     0.2014 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.045  |        0.0409 |         nan      | False          | nan      |       nan      |     0.0899 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.056  |        0.0314 |         nan      | False          | nan      |       nan      |     0.0899 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.2324 |        0.2178 |           0.007  | False          | nan      |       nan      |     0.2818 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  1.0036 |        0.1578 |           0.0037 | False          | nan      |       nan      |     0.2194 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  1.4413 |        0.0747 |           0.0052 | False          | nan      |       nan      |     0.1495 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  1.7985 |        0.036  |           0.0083 | False          | nan      |       nan      |     0.0899 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  0.9963 |        0.1595 |           0.0034 | False          | nan      |       nan      |     0.2194 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.0675 |        0.0387 |         nan      | False          | nan      |       nan      |     0.0899 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0363 |        0.1138 |         nan      | False          | nan      |       nan      |     0.2014 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  2.1824 |        0.0291 |           0.0093 | False          | nan      |       nan      |     0.0899 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  0.2337 |        0.4076 |           0.0011 | True           |   0.6936 |         1      |     0.4484 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  0.7349 |        0.2312 |           0.0032 | True           |   0.6936 |         1      |     0.2826 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  0.5067 |        0.3062 |           0.0022 | True           |   0.6936 |         1      |     0.3545 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  1.0743 |        0.1413 |           0.0052 | True           |   0.5654 |         0.7067 |     0.2194 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.4386 |        0.0006 |         nan      | False          | nan      |       nan      |     0.0129 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0892 |        0.0015 |         nan      | True           |   0.0076 |         0.0076 |     0.0166 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.561  |        0.5748 |          -0.0024 | False          | nan      |       nan      |     0.6022 |
| H4b          | tagger   | corr(tag,fwd) original=0.1837 vs perturbed-context (want ~0) | -0.0204 |        0.0322 |           0.2041 | False          | nan      |       nan      |     0.0899 |

## Reality check / SPA vs rules_only: RC p=0.773, SPA p=0.737

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2724 |    0.696  |  0.2514 | 0.0407 | 0.4937 |      0.4684 |          -0.8923 |    0.1203 |
| rules_tech|pit|gbt_mono      | 2724 |    0.6946 |  0.2508 | 0.0436 | 0.5145 |      0.4684 |          -0.6416 |    0.1978 |
| hitai_full|pit|gbt_mono      | 2724 |    0.6837 |  0.2453 | 0.0396 | 0.5863 |      0.4684 |           3.2512 |    1      |
| hitai_full|shuffled|gbt_mono | 2724 |    0.6947 |  0.2508 | 0.0433 | 0.5129 |      0.4684 |          -0.8914 |    0.1184 |
