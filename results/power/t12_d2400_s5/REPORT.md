# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 22008, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 13212 |    0.6965 |  0.2513 | 0.0233 | 0.4958 |      0.5043 |             0.0168 |                 0.6947 |             0.0941 |          -0.374  |          0.0555 |          0.1564 |    0.2184 |      -0.0699 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 13212 |    0.6956 |  0.251  | 0.0226 | 0.4968 |      0.5043 |             0.0186 |                 0.695  |             0.2541 |          -0.3483 |          0.082  |          0.2287 |    0.234  |      -0.0898 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 13212 |    0.6937 |  0.2503 | 0.0189 | 0.496  |      0.5043 |             0.0185 |                 0.694  |            -0.4412 |          -0.6543 |          0.02   |          0.1171 |    0.0854 |      -0.0693 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 13212 |    0.7066 |  0.252  | 0.013  | 0.5148 |      0.5043 |             0.0158 |                 0.6945 |             0.6234 |          -0.1341 |          0.1191 |          0.2583 |    0.3896 |      -0.1022 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 13212 |    0.6961 |  0.251  | 0.0133 | 0.5038 |      0.5043 |             0.0544 |                 0.7017 |             0.7997 |          -0.3331 |          0.1765 |          0.2899 |    0.244  |      -0.1107 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 13212 |    0.6996 |  0.2516 | 0.0189 | 0.5026 |      0.5043 |             0.0346 |                 0.6978 |             0.1852 |          -0.8717 |          0.1669 |          0.3003 |    0.0331 |      -0.1612 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 13212 |    0.7127 |  0.2533 | 0.0139 | 0.4974 |      0.5043 |             0.0305 |                 0.6971 |            -0.1604 |          -0.8421 |          0.0913 |          0.1944 |    0.037  |      -0.1374 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 13212 |    0.6973 |  0.251  | 0.0081 | 0.5042 |      0.5043 |             0.0519 |                 0.7017 |             0.7186 |          -0.342  |          0.173  |          0.3132 |    0.2381 |      -0.0996 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 13212 |    0.6996 |  0.2516 | 0.0189 | 0.5026 |      0.5043 |             0.0346 |                 0.6978 |             0.1852 |          -0.8717 |          0.1669 |          0.3003 |    0.0331 |      -0.1612 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 13212 |    0.7011 |  0.2494 | 0.0157 | 0.5631 |      0.5043 |             0.0204 |                 0.6881 |             5.7829 |           3.813  |          0.5298 |          0.8781 |    1      |      -0.0419 |    0.344  |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 13212 |    0.6952 |  0.2489 | 0.0195 | 0.5578 |      0.5043 |             0.0312 |                 0.6916 |             5.3345 |           3.2269 |          0.5211 |          0.7641 |    1      |      -0.0438 |    0.047  |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 13212 |    0.6901 |  0.248  | 0.0118 | 0.5634 |      0.5043 |             0.014  |                 0.6874 |             6.3773 |           4.3172 |          0.5321 |          0.8458 |    1      |      -0.0458 |    0.7367 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 13212 |    0.7134 |  0.253  | 0.0115 | 0.501  |      0.5043 |             0.0309 |                 0.6974 |            -0.0604 |          -0.756  |          0.0901 |          0.1685 |    0.0541 |      -0.1305 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 13212 |    0.6992 |  0.2515 | 0.0163 | 0.496  |      0.5043 |             0.0529 |                 0.7018 |             0.2005 |          -0.8716 |          0.1226 |          0.1571 |    0.036  |      -0.1179 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 13212 |    0.6998 |  0.2514 | 0.0072 | 0.5038 |      0.5043 |             0.0342 |                 0.6979 |             0.1831 |          -0.7225 |          0.1309 |          0.2416 |    0.0634 |      -0.1236 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 13212 |    0.7151 |  0.2533 | 0.0101 | 0.5029 |      0.5043 |             0.028  |                 0.6971 |             0.1122 |          -0.5526 |          0.1045 |          0.2642 |    0.1236 |      -0.1384 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 13212 |    0.6964 |  0.2511 | 0.009  | 0.5048 |      0.5043 |             0.0543 |                 0.702  |             0.3839 |          -0.7096 |          0.1885 |          0.3417 |    0.0703 |      -0.1478 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 13212 |    0.701  |  0.2518 | 0.0283 | 0.494  |      0.5043 |             0.0341 |                 0.6978 |             0.1299 |          -0.7531 |          0.1247 |          0.2516 |    0.0561 |      -0.121  |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 13212 |    0.7053 |  0.2496 | 0.0179 | 0.5595 |      0.5043 |             0.0177 |                 0.6886 |             6.5922 |           4.5306 |          0.5342 |          0.8571 |    1      |      -0.036  |    0.8472 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 13212 |    0.6937 |  0.2492 | 0.0146 | 0.5545 |      0.5043 |             0.0317 |                 0.692  |             5.3746 |           3.2565 |          0.5102 |          0.7787 |    1      |      -0.0451 |    0.0591 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 13212 |    0.6912 |  0.2481 | 0.0244 | 0.5652 |      0.5043 |             0.0194 |                 0.6876 |             5.9364 |           3.9021 |          0.5338 |          0.9308 |    1      |      -0.0375 |    0.4151 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -1.3133 |        0.9055 |          -0.0046 | False          | nan      |       nan      |     0.9055 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.1955 |        0.0141 |           0.0116 | False          | nan      |       nan      |     0.0344 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.4799 |        0.0066 |           0.0123 | False          | nan      |       nan      |     0.0181 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.5789 |        0.005  |           0.014  | False          | nan      |       nan      |     0.0171 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.0542 |        0.0001 |         nan      | False          | nan      |       nan      |     0.0005 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0321 |        0.0661 |         nan      | False          | nan      |       nan      |     0.1212 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.7754 |        0.0758 |           0.0042 | False          | nan      |       nan      |     0.1283 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  0.1117 |        0.4555 |           0.0004 | False          | nan      |       nan      |     0.5275 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  0.6594 |        0.2548 |           0.0021 | False          | nan      |       nan      |     0.3738 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  1.2145 |        0.1123 |           0.004  | False          | nan      |       nan      |     0.1764 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  0.382  |        0.3512 |           0.0012 | False          | nan      |       nan      |     0.4545 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.7795 |        0.0054 |         nan      | False          | nan      |       nan      |     0.0171 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0351 |        0.0498 |         nan      | False          | nan      |       nan      |     0.1095 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.6591 |        0.5098 |          -0.0015 | False          | nan      |       nan      |     0.5608 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  1.5797 |        0.0571 |           0.0036 | True           |   0.1142 |         0.2855 |     0.1142 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  3.7796 |        0.0001 |           0.0095 | True           |   0.0003 |         0.0004 |     0.0005 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  3.7521 |        0.0001 |           0.0096 | True           |   0.0003 |         0.0004 |     0.0005 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  4.1064 |        0      |           0.0109 | True           |   0.0001 |         0.0001 |     0.0004 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.7809 |        0.0054 |         nan      | False          | nan      |       nan      |     0.0171 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0104 |        0.3122 |         nan      | True           |   0.3122 |         1      |     0.4292 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.8806 |        0.3785 |           0.001  | False          | nan      |       nan      |     0.4627 |
| H4b          | tagger   | corr(tag,fwd) original=0.1715 vs perturbed-context (want ~0) |  0.0025 |        0.7066 |           0.1689 | False          | nan      |       nan      |     0.7403 |

## Reality check / SPA vs rules_only: RC p=0.573, SPA p=0.133

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5448 |    0.692  |  0.2494 | 0.0027 | 0.5133 |      0.5204 |           0.916  |    0.8918 |
| rules_tech|pit|gbt_mono      | 5448 |    0.6928 |  0.2498 | 0.0018 | 0.5084 |      0.5204 |           0.6132 |    0.7949 |
| hitai_full|pit|gbt_mono      | 5448 |    0.6861 |  0.2461 | 0.0119 | 0.5709 |      0.5204 |           4.0967 |    1      |
| hitai_full|shuffled|gbt_mono | 5448 |    0.6928 |  0.2498 | 0.002  | 0.5109 |      0.5204 |           0.5271 |    0.7604 |
