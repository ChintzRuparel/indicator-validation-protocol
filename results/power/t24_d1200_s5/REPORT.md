# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 20976, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 12600 |    0.6947 |  0.2508 | 0.0251 | 0.5009 |        0.51 |             0.0053 |                 0.6928 |             0.4578 |          -0.1407 |          0.1083 |          0.7131 |    0.4196 |      -0.075  |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 12600 |    0.6946 |  0.2507 | 0.0268 | 0.5005 |        0.51 |             0.0045 |                 0.6933 |             0.7528 |           0.1035 |          0.1344 |          0.9137 |    0.5593 |      -0.0889 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 12600 |    0.6944 |  0.2506 | 0.023  | 0.498  |        0.51 |             0.0043 |                 0.6931 |             0.7777 |          -0.1963 |          0.1349 |          0.4275 |    0.3885 |      -0.0454 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 12600 |    0.7045 |  0.2526 | 0.0321 | 0.4994 |        0.51 |             0.0227 |                 0.6948 |            -0.3762 |          -1.1466 |          0.1442 |          0.7482 |    0.0502 |      -0.1484 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 12600 |    0.6987 |  0.2515 | 0.0235 | 0.4906 |        0.51 |             0.0528 |                 0.7035 |            -0.449  |          -1.3789 |          0.1722 |          0.7613 |    0.0236 |      -0.1602 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 12600 |    0.7104 |  0.253  | 0.0381 | 0.4926 |        0.51 |             0.0397 |                 0.6984 |            -0.0309 |          -0.8677 |          0.1517 |          0.6781 |    0.1057 |      -0.1181 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 12600 |    0.7035 |  0.2526 | 0.0363 | 0.5009 |        0.51 |             0.0263 |                 0.6958 |             0.0197 |          -0.989  |          0.1856 |          0.6722 |    0.0767 |      -0.1343 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 12600 |    0.6994 |  0.2515 | 0.024  | 0.4903 |        0.51 |             0.0533 |                 0.7037 |            -0.4795 |          -1.598  |          0.1991 |          0.7066 |    0.0108 |      -0.1658 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 12600 |    0.7105 |  0.2531 | 0.0381 | 0.4913 |        0.51 |             0.0397 |                 0.6984 |            -0.1237 |          -0.9728 |          0.1537 |          0.6771 |    0.0806 |      -0.1251 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 12600 |    0.6936 |  0.2472 | 0.0243 | 0.5742 |        0.51 |             0.0201 |                 0.6841 |             8.1019 |           5.6754 |          0.4867 |          0.8936 |    1      |      -0.0203 |    0.6048 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 12600 |    0.6948 |  0.2485 | 0.012  | 0.5574 |        0.51 |             0.028  |                 0.6901 |             5.5972 |           3.2616 |          0.4486 |          0.7926 |    1      |      -0.0236 |    0.0009 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 12600 |    0.7011 |  0.2491 | 0.0189 | 0.566  |        0.51 |             0.0131 |                 0.6856 |             7.9467 |           5.4046 |          0.4921 |          0.8473 |    1      |      -0.0199 |    0.4564 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 12600 |    0.707  |  0.2526 | 0.0372 | 0.4994 |        0.51 |             0.0286 |                 0.6959 |            -0.3069 |          -1.2911 |          0.1826 |          0.6807 |    0.0321 |      -0.165  |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 12600 |    0.6966 |  0.2514 | 0.0247 | 0.4907 |        0.51 |             0.0541 |                 0.7036 |            -0.6376 |          -1.6507 |          0.184  |          0.7258 |    0.0088 |      -0.1793 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 12600 |    0.71   |  0.253  | 0.0381 | 0.4913 |        0.51 |             0.0393 |                 0.6983 |            -0.1108 |          -1.1521 |          0.183  |          0.6002 |    0.0484 |      -0.139  |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 12600 |    0.7034 |  0.2523 | 0.0365 | 0.5074 |        0.51 |             0.0292 |                 0.6959 |             0.5784 |          -0.4735 |          0.1879 |          0.6603 |    0.2473 |      -0.0847 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 12600 |    0.7016 |  0.2518 | 0.0253 | 0.4953 |        0.51 |             0.0533 |                 0.7038 |            -0.2035 |          -1.4977 |          0.2187 |          0.6245 |    0.0148 |      -0.1525 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 12600 |    0.7121 |  0.2531 | 0.0311 | 0.4946 |        0.51 |             0.0371 |                 0.698  |            -0.0008 |          -0.826  |          0.1471 |          0.6737 |    0.1171 |      -0.121  |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 12600 |    0.6914 |  0.2467 | 0.018  | 0.5756 |        0.51 |             0.019  |                 0.6844 |             8.0238 |           5.6065 |          0.4902 |          0.8456 |    1      |      -0.0269 |    0.5685 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 12600 |    0.6938 |  0.2483 | 0.0114 | 0.5658 |        0.51 |             0.0213 |                 0.6893 |             6.685  |           4.2614 |          0.4649 |          0.7883 |    1      |      -0.0292 |    0.0412 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 12600 |    0.696  |  0.2478 | 0.0265 | 0.5739 |        0.51 |             0.0154 |                 0.6849 |             8.6567 |           6.0098 |          0.4946 |          0.8321 |    1      |      -0.0155 |    0.7705 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  0.3616 |        0.3588 |           0.0012 | False          | nan      |       nan      |     0.4643 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.5774 |        0.005  |           0.0099 | False          | nan      |       nan      |     0.0173 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.9071 |        0.0018 |           0.0134 | False          | nan      |       nan      |     0.01   |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.4214 |        0.0077 |           0.0099 | False          | nan      |       nan      |     0.0213 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.7266 |        0.0002 |         nan      | False          | nan      |       nan      |     0.0015 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0352 |        0.0528 |         nan      | False          | nan      |       nan      |     0.0917 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.6913 |        0.4894 |          -0.0022 | False          | nan      |       nan      |     0.5938 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -0.0702 |        0.528  |          -0.0002 | False          | nan      |       nan      |     0.5938 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  1.4233 |        0.0773 |           0.0046 | False          | nan      |       nan      |     0.1215 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  0.7135 |        0.2378 |           0.0018 | False          | nan      |       nan      |     0.3269 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  1.9279 |        0.0269 |           0.0068 | False          | nan      |       nan      |     0.0539 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.7109 |        0.0002 |         nan      | False          | nan      |       nan      |     0.0015 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0421 |        0.0265 |         nan      | False          | nan      |       nan      |     0.0539 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.6131 |        0.5398 |          -0.001  | False          | nan      |       nan      |     0.5938 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -1.8112 |        0.9649 |          -0.0067 | True           |   0.9649 |         1      |     0.9649 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  2.5431 |        0.0055 |           0.0094 | True           |   0.0229 |         0.0275 |     0.0173 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  2.3236 |        0.0101 |           0.0089 | True           |   0.0302 |         0.0504 |     0.0246 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  2.6067 |        0.0046 |           0.011  | True           |   0.0229 |         0.0229 |     0.0173 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.3998 |        0      |         nan      | False          | nan      |       nan      |     0.0002 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0237 |        0.1383 |         nan      | True           |   0.2765 |         0.6913 |     0.2028 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.9251 |        0.0542 |          -0.0051 | False          | nan      |       nan      |     0.0917 |
| H4b          | tagger   | corr(tag,fwd) original=0.1742 vs perturbed-context (want ~0) | -0.0013 |        0.8555 |           0.1754 | False          | nan      |       nan      |     0.8962 |

## Reality check / SPA vs rules_only: RC p=0.880, SPA p=0.883

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5136 |    0.6933 |  0.2501 | 0.0037 | 0.5024 |      0.5107 |          -1.0345 |    0.1744 |
| rules_tech|pit|gbt_mono      | 5136 |    0.693  |  0.2499 | 0.0051 | 0.5068 |      0.5107 |          -0.3716 |    0.3677 |
| hitai_full|pit|gbt_mono      | 5136 |    0.6918 |  0.2467 | 0.0158 | 0.5741 |      0.5107 |           6.4662 |    1      |
| hitai_full|shuffled|gbt_mono | 5136 |    0.693  |  0.2499 | 0.0051 | 0.5068 |      0.5107 |          -0.3716 |    0.3677 |
