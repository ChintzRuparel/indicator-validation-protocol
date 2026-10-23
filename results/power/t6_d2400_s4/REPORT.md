# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 11004, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6606 |    0.6982 |  0.2521 | 0.029  | 0.4967 |      0.5162 |             0.0406 |                 0.6973 |            -0.1901 |          -0.393  |          0.0556 |          0.4257 |    0.2063 |      -0.1469 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6606 |    0.6987 |  0.2524 | 0.0294 | 0.4906 |      0.5162 |             0.0523 |                 0.6998 |            -0.178  |          -0.3529 |          0.0551 |          0.523  |    0.2304 |      -0.1931 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6606 |    0.695  |  0.2509 | 0.0242 | 0.5029 |      0.5162 |             0.026  |                 0.694  |            -0.0418 |          -0.0501 |          0.0027 |          0.6004 |    0.4583 |      -0.1925 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6606 |    0.7082 |  0.2533 | 0.0385 | 0.5008 |      0.5162 |             0.0329 |                 0.6958 |             0.0396 |          -0.0997 |          0.0497 |          0.7031 |    0.4175 |      -0.2075 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6606 |    0.7121 |  0.2549 | 0.0523 | 0.4883 |      0.5162 |             0.0712 |                 0.7128 |            -0.2605 |          -0.6941 |          0.1529 |          0.6789 |    0.0734 |      -0.3247 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6606 |    0.7031 |  0.2542 | 0.0439 | 0.4887 |      0.5162 |             0.0564 |                 0.704  |            -0.7897 |          -1.2917 |          0.1583 |          0.5357 |    0.0036 |      -0.4503 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6606 |    0.7093 |  0.2541 | 0.0389 | 0.4965 |      0.5162 |             0.0492 |                 0.6987 |            -0.0182 |          -0.3961 |          0.1213 |          0.5226 |    0.205  |      -0.1887 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6606 |    0.7121 |  0.2549 | 0.0523 | 0.4883 |      0.5162 |             0.0712 |                 0.7128 |            -0.2605 |          -0.6941 |          0.1529 |          0.6789 |    0.0734 |      -0.3247 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6606 |    0.7031 |  0.2542 | 0.0439 | 0.4887 |      0.5162 |             0.0564 |                 0.704  |            -0.7897 |          -1.2917 |          0.1583 |          0.5357 |    0.0036 |      -0.4503 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6606 |    0.6978 |  0.2513 | 0.0371 | 0.5369 |      0.5162 |             0.0402 |                 0.6921 |             3.3456 |           2.0939 |          0.4673 |          0.8618 |    1      |      -0.1378 |    0.6107 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6606 |    0.7051 |  0.2534 | 0.0445 | 0.5144 |      0.5162 |             0.0666 |                 0.7041 |             1.6952 |           0.7249 |          0.3589 |          0.81   |    0.9346 |      -0.1895 |    0.005  |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6606 |    0.7028 |  0.2527 | 0.0459 | 0.5269 |      0.5162 |             0.0418 |                 0.6945 |             2.4    |           1.3005 |          0.417  |          0.8332 |    0.9967 |      -0.1096 |    0.0838 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6606 |    0.7104 |  0.2539 | 0.0416 | 0.4892 |      0.5162 |             0.0491 |                 0.6988 |            -0.3248 |          -0.7079 |          0.1182 |          0.4879 |    0.0705 |      -0.2428 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6606 |    0.7081 |  0.2543 | 0.0496 | 0.4901 |      0.5162 |             0.074  |                 0.7122 |            -0.0216 |          -0.442  |          0.1341 |          0.5993 |    0.1784 |      -0.2966 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6606 |    0.7054 |  0.2546 | 0.0462 | 0.4848 |      0.5162 |             0.0567 |                 0.7036 |            -0.6663 |          -1.1398 |          0.1508 |          0.5506 |    0.0088 |      -0.4017 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6606 |    0.7013 |  0.2532 | 0.0394 | 0.4947 |      0.5162 |             0.051  |                 0.7009 |            -0.1614 |          -0.5541 |          0.1332 |          0.6101 |    0.1246 |      -0.2068 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6606 |    0.7076 |  0.2547 | 0.0529 | 0.4853 |      0.5162 |             0.0797 |                 0.7133 |            -0.144  |          -0.4799 |          0.1256 |          0.7738 |    0.1579 |      -0.3245 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6606 |    0.7037 |  0.2544 | 0.0438 | 0.4862 |      0.5162 |             0.0606 |                 0.7046 |            -0.549  |          -1.1437 |          0.1714 |          0.4514 |    0.0089 |      -0.3643 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6606 |    0.7006 |  0.2522 | 0.0448 | 0.5354 |      0.5162 |             0.0408 |                 0.6928 |             2.9673 |           1.7982 |          0.4282 |          0.8006 |    0.9999 |      -0.1151 |    0.3663 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6606 |    0.7086 |  0.2535 | 0.0414 | 0.5112 |      0.5162 |             0.0696 |                 0.7061 |             1.6467 |           0.7149 |          0.3547 |          0.8082 |    0.9324 |      -0.1662 |    0.0046 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6606 |    0.7059 |  0.2535 | 0.0448 | 0.5196 |      0.5162 |             0.042  |                 0.6958 |             2.3811 |           1.4134 |          0.366  |          0.8388 |    0.9985 |      -0.1062 |    0.1261 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  0.1196 |        0.4524 |           0.0004 | False          | nan      |       nan      |     0.5498 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.2658 |        0.0117 |           0.0114 | False          | nan      |       nan      |     0.0645 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.3369 |        0.0097 |           0.0126 | False          | nan      |       nan      |     0.0645 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  1.1352 |        0.1281 |           0.0035 | False          | nan      |       nan      |     0.2819 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.354  |        0.0186 |         nan      | False          | nan      |       nan      |     0.0817 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.011  |        0.3581 |         nan      | False          | nan      |       nan      |     0.5252 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.6862 |        0.0918 |           0.0027 | False          | nan      |       nan      |     0.2464 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -1.5895 |        0.944  |          -0.0064 | False          | nan      |       nan      |     0.9622 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  1.4768 |        0.0699 |           0.007  | False          | nan      |       nan      |     0.2196 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  0.8022 |        0.2112 |           0.0029 | False          | nan      |       nan      |     0.4224 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  0.6467 |        0.2589 |           0.0024 | False          | nan      |       nan      |     0.4382 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.7474 |        0.0002 |         nan      | False          | nan      |       nan      |     0.0039 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0385 |        0.1008 |         nan      | False          | nan      |       nan      |     0.2464 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.8147 |        0.4153 |           0.0035 | False          | nan      |       nan      |     0.5374 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -1.7768 |        0.9622 |          -0.0079 | True           |   1      |         1      |     0.9622 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  0.0632 |        0.4748 |           0.0003 | True           |   1      |         1      |     0.5498 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  0.5563 |        0.289  |           0.0025 | True           |   1      |         1      |     0.4541 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  0.2144 |        0.4151 |           0.0009 | True           |   1      |         1      |     0.5374 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.2376 |        0.0012 |         nan      | False          | nan      |       nan      |     0.0133 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0492 |        0.0512 |         nan      | True           |   0.2559 |         0.2559 |     0.1877 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.1398 |        0.2544 |           0.0031 | False          | nan      |       nan      |     0.4382 |
| H4b          | tagger   | corr(tag,fwd) original=0.1538 vs perturbed-context (want ~0) | -0.0055 |        0.563  |           0.1593 | False          | nan      |       nan      |     0.6193 |

## Reality check / SPA vs rules_only: RC p=1.000, SPA p=1.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2724 |    0.6927 |  0.2498 | 0.0007 | 0.5016 |      0.5151 |          -1.0779 |    0.0709 |
| rules_tech|pit|gbt_mono      | 2724 |    0.6932 |  0.25   | 0.0028 | 0.52   |      0.5151 |           0.2696 |    0.6414 |
| hitai_full|pit|gbt_mono      | 2724 |    0.6841 |  0.2455 | 0.0047 | 0.5863 |      0.5151 |           2.7084 |    0.9998 |
| hitai_full|shuffled|gbt_mono | 2724 |    0.6926 |  0.2497 | 0.0039 | 0.5199 |      0.5151 |           0.2157 |    0.6139 |
