# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 10488, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6300 |    0.7054 |  0.2523 | 0.0225 | 0.5042 |      0.4879 |             0.0406 |                 0.6977 |            -0.3645 |          -0.6014 |          0.0473 |          0.4098 |    0.1915 |      -0.1206 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6300 |    0.7032 |  0.253  | 0.0242 | 0.4965 |      0.4879 |             0.0439 |                 0.6975 |            -0.8767 |          -1.2659 |          0.0816 |          0.4137 |    0.0328 |      -0.1641 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6300 |    0.7009 |  0.2521 | 0.0254 | 0.4934 |      0.4879 |             0.0369 |                 0.696  |            -0.3028 |          -0.7554 |          0.1075 |          0.646  |    0.138  |      -0.1272 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6300 |    0.706  |  0.2526 | 0.0248 | 0.513  |      0.4879 |             0.0344 |                 0.6957 |            -0.1158 |          -1.4753 |          0.3517 |          0.6552 |    0.0155 |      -0.2376 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6300 |    0.6963 |  0.2513 | 0.0206 | 0.4999 |      0.4879 |             0.0762 |                 0.7103 |            -0.9842 |          -1.593  |          0.1294 |          0.4635 |    0.0104 |      -0.2006 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6300 |    0.6977 |  0.2517 | 0.0216 | 0.5007 |      0.4879 |             0.0438 |                 0.7011 |            -0.4914 |          -1.0494 |          0.121  |          0.5011 |    0.0649 |      -0.1716 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6300 |    0.7041 |  0.2534 | 0.0399 | 0.5025 |      0.4879 |             0.0473 |                 0.6982 |            -0.2776 |          -1.696  |          0.3983 |          0.7376 |    0.007  |      -0.2945 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6300 |    0.6952 |  0.2511 | 0.0209 | 0.4986 |      0.4879 |             0.0756 |                 0.71   |            -0.639  |          -1.1627 |          0.1162 |          0.5117 |    0.0457 |      -0.1785 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6300 |    0.6979 |  0.2518 | 0.0207 | 0.5003 |      0.4879 |             0.0471 |                 0.7013 |            -0.5381 |          -1.2293 |          0.1481 |          0.4686 |    0.0377 |      -0.1765 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6300 |    0.6973 |  0.2489 | 0.0335 | 0.5669 |      0.4879 |             0.0362 |                 0.6848 |             4.2038 |           2.5868 |          0.4937 |          0.897  |    0.9999 |      -0.0588 |    0.041  |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6300 |    0.6999 |  0.249  | 0.0236 | 0.5577 |      0.4879 |             0.0526 |                 0.6942 |             3.2379 |           1.7477 |          0.4668 |          0.9105 |    0.9942 |      -0.1099 |    0.0015 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6300 |    0.6912 |  0.2477 | 0.0208 | 0.5681 |      0.4879 |             0.0379 |                 0.6851 |             4.9963 |           3.2471 |          0.4743 |          0.721  |    1      |      -0.0381 |    0.2167 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6300 |    0.7096 |  0.2534 | 0.0317 | 0.4987 |      0.4879 |             0.0363 |                 0.6985 |            -0.8699 |          -2.5262 |          0.4027 |          0.5837 |    0.0001 |      -0.363  |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6300 |    0.7014 |  0.2519 | 0.0209 | 0.5022 |      0.4879 |             0.078  |                 0.7101 |            -1.004  |          -1.7904 |          0.1671 |          0.4667 |    0.0046 |      -0.2281 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6300 |    0.699  |  0.252  | 0.0196 | 0.5035 |      0.4879 |             0.0444 |                 0.7004 |            -0.8195 |          -1.4823 |          0.139  |          0.437  |    0.0151 |      -0.2032 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6300 |    0.7044 |  0.2529 | 0.0309 | 0.502  |      0.4879 |             0.039  |                 0.6982 |            -0.4326 |          -1.8388 |          0.353  |          0.6022 |    0.0037 |      -0.2791 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6300 |    0.6996 |  0.2517 | 0.0193 | 0.5016 |      0.4879 |             0.0777 |                 0.7101 |            -0.7908 |          -1.7276 |          0.2073 |          0.4798 |    0.0058 |      -0.2153 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6300 |    0.6989 |  0.2523 | 0.0247 | 0.5018 |      0.4879 |             0.0474 |                 0.7008 |            -0.1098 |          -0.6194 |          0.1168 |          0.6011 |    0.1852 |      -0.1461 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6300 |    0.6951 |  0.2481 | 0.0304 | 0.5699 |      0.4879 |             0.0436 |                 0.6852 |             5.2477 |           3.3836 |          0.5113 |          0.7735 |    1      |      -0.0258 |    0.2782 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6300 |    0.701  |  0.2499 | 0.0252 | 0.5532 |      0.4879 |             0.055  |                 0.6971 |             2.8676 |           1.4269 |          0.4502 |          0.9111 |    0.9812 |      -0.0707 |    0.0003 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6300 |    0.6879 |  0.2469 | 0.0111 | 0.5721 |      0.4879 |             0.0383 |                 0.6864 |             5.2796 |           3.5657 |          0.47   |          0.709  |    1      |      -0.0428 |    0.3701 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  1.5286 |        0.0632 |           0.0082 | False          | nan      |       nan      |     0.1158 |
| H3a          | logit    | rules_tech - hitai_full                                      |  1.6396 |        0.0505 |           0.0068 | False          | nan      |       nan      |     0.1013 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.0974 |        0.018  |           0.0123 | False          | nan      |       nan      |     0.0565 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  1.6388 |        0.0506 |           0.0071 | False          | nan      |       nan      |     0.1013 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.1781 |        0.0294 |         nan      | False          | nan      |       nan      |     0.0719 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.1373 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.8427 |        0.3994 |          -0.0022 | False          | nan      |       nan      |     0.4982 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  0.4755 |        0.3172 |           0.0034 | False          | nan      |       nan      |     0.4362 |
| H3a          | gbt      | rules_tech - hitai_full                                      | -0.7698 |        0.7793 |          -0.0046 | False          | nan      |       nan      |     0.8572 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  0.2337 |        0.4076 |           0.0016 | False          | nan      |       nan      |     0.4982 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         | -0.0337 |        0.5134 |          -0.0002 | False          | nan      |       nan      |     0.5945 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.7817 |        0.0748 |         nan      | False          | nan      |       nan      |     0.1266 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0772 |        0.006  |         nan      | False          | nan      |       nan      |     0.0416 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.1801 |        0.857  |           0.0011 | False          | nan      |       nan      |     0.8696 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  2.0973 |        0.018  |           0.0097 | True           |   0.036  |         0.0899 |     0.0565 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  2.0358 |        0.0209 |           0.0067 | True           |   0.036  |         0.1044 |     0.0574 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  2.3474 |        0.0095 |           0.0078 | True           |   0.0332 |         0.0473 |     0.0416 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  2.3956 |        0.0083 |           0.0077 | True           |   0.0332 |         0.0415 |     0.0416 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.5394 |        0.1237 |         nan      | False          | nan      |       nan      |     0.1828 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.1524 |        0      |         nan      | True           |   0      |         0      |     0      |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.5356 |        0.1246 |          -0.0033 | False          | nan      |       nan      |     0.1828 |
| H4b          | tagger   | corr(tag,fwd) original=0.1894 vs perturbed-context (want ~0) |  0.0016 |        0.8696 |           0.1878 | False          | nan      |       nan      |     0.8696 |

## Reality check / SPA vs rules_only: RC p=0.123, SPA p=0.057

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2568 |    0.6932 |  0.25   | 0.0078 | 0.5014 |      0.4879 |          -1.5823 |    0.0722 |
| rules_tech|pit|gbt_mono      | 2568 |    0.6962 |  0.2508 | 0.029  | 0.4948 |      0.4879 |          -0.8286 |    0.222  |
| hitai_full|pit|gbt_mono      | 2568 |    0.6917 |  0.2479 | 0.037  | 0.5763 |      0.4879 |           5.025  |    1      |
| hitai_full|shuffled|gbt_mono | 2568 |    0.698  |  0.2516 | 0.0354 | 0.4872 |      0.4879 |          -2.1621 |    0.0226 |
