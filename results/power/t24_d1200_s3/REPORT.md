# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 20976, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 12600 |    0.7022 |  0.2517 | 0.0293 | 0.4953 |      0.4952 |             0.0136 |                 0.6938 |            -0.5871 |          -1.4536 |          0.1387 |          0.4425 |    0.0159 |      -0.1269 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 12600 |    0.7014 |  0.2519 | 0.0315 | 0.4965 |      0.4952 |             0.0241 |                 0.6943 |            -0.0674 |          -1.2812 |          0.1458 |          0.2766 |    0.027  |      -0.0866 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 12600 |    0.6966 |  0.2512 | 0.0272 | 0.4958 |      0.4952 |             0.0151 |                 0.6938 |            -0.5784 |          -1.6562 |          0.0986 |          0.1871 |    0.0081 |      -0.0832 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 12600 |    0.7025 |  0.252  | 0.0289 | 0.5001 |      0.4952 |             0.0131 |                 0.694  |            -0.5986 |          -2.3079 |          0.3267 |          0.6898 |    0.0004 |      -0.25   |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 12600 |    0.7016 |  0.2516 | 0.0282 | 0.4946 |      0.4952 |             0.0457 |                 0.7001 |            -0.1773 |          -1.1021 |          0.1456 |          0.4426 |    0.0527 |      -0.113  |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 12600 |    0.6982 |  0.2519 | 0.0299 | 0.4862 |      0.4952 |             0.037  |                 0.6975 |            -0.966  |          -2.354  |          0.1625 |          0.2923 |    0.0002 |      -0.145  |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 12600 |    0.7016 |  0.2516 | 0.0274 | 0.5024 |      0.4952 |             0.0143 |                 0.6943 |             0.1278 |          -1.3628 |          0.271  |          0.5797 |    0.0249 |      -0.1428 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 12600 |    0.7009 |  0.2515 | 0.0259 | 0.4961 |      0.4952 |             0.0455 |                 0.7001 |            -0.3269 |          -1.4281 |          0.1725 |          0.4398 |    0.0174 |      -0.1381 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 12600 |    0.6982 |  0.2519 | 0.0297 | 0.4863 |      0.4952 |             0.0364 |                 0.6975 |            -0.9924 |          -2.4184 |          0.1639 |          0.2843 |    0.0001 |      -0.1462 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 12600 |    0.6904 |  0.2452 | 0.0101 | 0.5849 |      0.4952 |             0.0203 |                 0.681  |             8.3649 |           5.9574 |          0.5182 |          0.8618 |    1      |      -0.0165 |    0.1966 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 12600 |    0.6893 |  0.2471 | 0.0117 | 0.5657 |      0.4952 |             0.0198 |                 0.6854 |             6.7359 |           4.1563 |          0.5702 |          0.9278 |    1      |      -0.0304 |    0.0003 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 12600 |    0.6881 |  0.2461 | 0.0093 | 0.5787 |      0.4952 |             0.0167 |                 0.6824 |             7.8752 |           5.4519 |          0.5013 |          0.8108 |    1      |      -0.0186 |    0.0596 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 12600 |    0.6999 |  0.2517 | 0.0277 | 0.502  |      0.4952 |             0.0138 |                 0.6943 |            -0.3746 |          -2.0544 |          0.2852 |          0.4907 |    0.0017 |      -0.1855 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 12600 |    0.6987 |  0.2514 | 0.03   | 0.4943 |      0.4952 |             0.0457 |                 0.7003 |            -0.2443 |          -1.211  |          0.1743 |          0.5708 |    0.0384 |      -0.1491 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 12600 |    0.6985 |  0.2519 | 0.0285 | 0.4869 |      0.4952 |             0.0353 |                 0.6974 |            -1.0476 |          -2.4794 |          0.1653 |          0.2886 |    0.0001 |      -0.1505 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 12600 |    0.7064 |  0.2525 | 0.0281 | 0.4954 |      0.4952 |             0.0168 |                 0.6946 |            -0.3634 |          -1.8949 |          0.23   |          0.4177 |    0.003  |      -0.1546 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 12600 |    0.6989 |  0.2514 | 0.0264 | 0.4986 |      0.4952 |             0.0498 |                 0.7005 |            -0.5362 |          -1.7116 |          0.1869 |          0.4864 |    0.0055 |      -0.1521 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 12600 |    0.702  |  0.2521 | 0.0302 | 0.489  |      0.4952 |             0.0387 |                 0.6973 |            -0.8802 |          -2.0495 |          0.1482 |          0.2987 |    0.0009 |      -0.1366 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 12600 |    0.692  |  0.2451 | 0.0179 | 0.5865 |      0.4952 |             0.0198 |                 0.6814 |             9.2618 |           6.7526 |          0.5531 |          0.904  |    1      |      -0.0124 |    0.6202 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 12600 |    0.6888 |  0.2471 | 0.007  | 0.5665 |      0.4952 |             0.0211 |                 0.687  |             7.5809 |           4.9918 |          0.567  |          0.9027 |    1      |      -0.0297 |    0.0124 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 12600 |    0.6878 |  0.2461 | 0.0091 | 0.5763 |      0.4952 |             0.0155 |                 0.6833 |             7.7516 |           5.4786 |          0.4958 |          0.8123 |    1      |      -0.0203 |    0.0589 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  3.3099 |        0.0005 |           0.0118 | False          | nan      |       nan      |     0.0009 |
| H3a          | logit    | rules_tech - hitai_full                                      |  3.0763 |        0.001  |           0.0111 | False          | nan      |       nan      |     0.0018 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.8012 |        0.0025 |           0.0094 | False          | nan      |       nan      |     0.004  |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  3.5737 |        0.0002 |           0.016  | False          | nan      |       nan      |     0.0004 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  0.7167 |        0.4736 |         nan      | False          | nan      |       nan      |     0.5483 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0797 |        0.0001 |         nan      | False          | nan      |       nan      |     0.0003 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.6193 |        0.5357 |           0.0015 | False          | nan      |       nan      |     0.5893 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  3.7398 |        0.0001 |           0.0121 | False          | nan      |       nan      |     0.0003 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  4.0046 |        0      |           0.0116 | False          | nan      |       nan      |     0.0002 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  3.8407 |        0.0001 |           0.0094 | False          | nan      |       nan      |     0.0002 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  3.8532 |        0.0001 |           0.0096 | False          | nan      |       nan      |     0.0002 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.0524 |        0.2926 |         nan      | False          | nan      |       nan      |     0.4023 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0549 |        0.0058 |         nan      | False          | nan      |       nan      |     0.0086 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.2794 |        0.78   |          -0.0005 | False          | nan      |       nan      |     0.8171 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  3.5235 |        0.0002 |           0.0086 | True           |   0.0004 |         0.0011 |     0.0005 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  4.3017 |        0      |           0.0101 | True           |   0      |         0      |     0.0001 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  4.3294 |        0      |           0.0105 | True           |   0      |         0      |     0.0001 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  5.1524 |        0      |           0.0139 | True           |   0      |         0      |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  0.7673 |        0.4429 |         nan      | False          | nan      |       nan      |     0.5413 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0759 |        0.0002 |         nan      | True           |   0.0004 |         0.0012 |     0.0005 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.17   |        0.865  |          -0.0003 | False          | nan      |       nan      |     0.865  |
| H4b          | tagger   | corr(tag,fwd) original=0.1784 vs perturbed-context (want ~0) |  0.0068 |        0.3229 |           0.1716 | False          | nan      |       nan      |     0.4179 |

## Reality check / SPA vs rules_only: RC p=0.013, SPA p=0.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5136 |    0.693  |  0.2499 | 0.009  | 0.5204 |      0.5099 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 5136 |    0.6928 |  0.2499 | 0.0126 | 0.5066 |      0.5099 |          -0.1784 |    0.4346 |
| hitai_full|pit|gbt_mono      | 5136 |    0.6815 |  0.2433 | 0.0178 | 0.5988 |      0.5099 |           5.8659 |    1      |
| hitai_full|shuffled|gbt_mono | 5136 |    0.693  |  0.2499 | 0.0101 | 0.503  |      0.5099 |           0.4424 |    0.657  |
