# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 10488, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6300 |    0.695  |  0.2509 | 0.0288 | 0.4959 |      0.5086 |             0.01   |                 0.6935 |             0.0896 |          -0.9239 |          0.1803 |          0.4124 |    0.0907 |      -0.1237 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6300 |    0.6971 |  0.2519 | 0.0325 | 0.4986 |      0.5086 |             0.0103 |                 0.6936 |             0.0752 |          -1.1482 |          0.2648 |          0.543  |    0.0472 |      -0.1332 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6300 |    0.6942 |  0.2505 | 0.0186 | 0.4969 |      0.5086 |             0.0094 |                 0.6936 |             0.4212 |          -0.6099 |          0.1581 |          0.3098 |    0.1918 |      -0.0792 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6300 |    0.7012 |  0.2524 | 0.0247 | 0.5023 |      0.5086 |             0.0189 |                 0.6949 |             0.154  |          -0.7941 |          0.2124 |          0.6863 |    0.1281 |      -0.1142 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6300 |    0.6978 |  0.2516 | 0.0245 | 0.4963 |      0.5086 |             0.0607 |                 0.7071 |            -0.2116 |          -1.1669 |          0.2295 |          0.6948 |    0.0459 |      -0.1714 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6300 |    0.7005 |  0.2518 | 0.0201 | 0.4981 |      0.5086 |             0.0484 |                 0.7009 |            -0.1576 |          -1.139  |          0.2051 |          0.5606 |    0.0514 |      -0.1489 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6300 |    0.6992 |  0.2521 | 0.0201 | 0.4984 |      0.5086 |             0.0191 |                 0.6952 |            -0.0144 |          -0.9778 |          0.1737 |          0.421  |    0.0794 |      -0.1159 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6300 |    0.6971 |  0.2512 | 0.0235 | 0.4994 |      0.5086 |             0.0604 |                 0.707  |            -0.1277 |          -1.0583 |          0.2283 |          0.6938 |    0.0623 |      -0.172  |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6300 |    0.7005 |  0.2518 | 0.0201 | 0.4981 |      0.5086 |             0.0484 |                 0.7009 |            -0.1576 |          -1.139  |          0.2051 |          0.5606 |    0.0514 |      -0.1489 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6300 |    0.6954 |  0.2467 | 0.0177 | 0.5759 |      0.5086 |             0.0199 |                 0.684  |             5.3864 |           3.3413 |          0.5144 |          0.8024 |    1      |      -0.0286 |    0.8024 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6300 |    0.7004 |  0.2492 | 0.0147 | 0.5562 |      0.5086 |             0.0398 |                 0.6936 |             3.2771 |           1.3967 |          0.4884 |          0.83   |    0.977  |      -0.044  |    0.0266 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6300 |    0.7044 |  0.2493 | 0.0243 | 0.5618 |      0.5086 |             0.022  |                 0.6879 |             3.9658 |           2.1473 |          0.4449 |          0.764  |    0.9989 |      -0.0522 |    0.1944 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6300 |    0.6976 |  0.2518 | 0.0152 | 0.5025 |      0.5086 |             0.0221 |                 0.6955 |             0.6453 |          -0.4917 |          0.2238 |          0.4775 |    0.2387 |      -0.0818 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6300 |    0.6977 |  0.2515 | 0.0219 | 0.5013 |      0.5086 |             0.0615 |                 0.7068 |            -0.0851 |          -1.0184 |          0.2425 |          0.7467 |    0.0702 |      -0.1983 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6300 |    0.6988 |  0.2519 | 0.0208 | 0.4907 |      0.5086 |             0.0502 |                 0.7013 |            -0.0954 |          -1.1151 |          0.1994 |          0.5333 |    0.0567 |      -0.1494 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6300 |    0.7032 |  0.2521 | 0.0218 | 0.5085 |      0.5086 |             0.0201 |                 0.695  |             0.282  |          -1.0415 |          0.2975 |          0.619  |    0.0666 |      -0.1792 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6300 |    0.7016 |  0.2516 | 0.0159 | 0.5009 |      0.5086 |             0.0674 |                 0.7071 |             0.185  |          -0.9879 |          0.2673 |          0.6683 |    0.078  |      -0.1798 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6300 |    0.6985 |  0.2522 | 0.0251 | 0.4905 |      0.5086 |             0.0414 |                 0.6994 |            -0.5759 |          -1.7919 |          0.2543 |          0.571  |    0.0049 |      -0.2109 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6300 |    0.7009 |  0.2477 | 0.0192 | 0.574  |      0.5086 |             0.0164 |                 0.6831 |             3.9435 |           2.2707 |          0.426  |          0.8184 |    0.9994 |      -0.042  |    0.248  |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6300 |    0.6955 |  0.2492 | 0.0168 | 0.5535 |      0.5086 |             0.0344 |                 0.6932 |             2.3022 |           0.5692 |          0.4141 |          0.7565 |    0.7942 |      -0.0939 |    0.0008 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6300 |    0.7003 |  0.2489 | 0.0181 | 0.5668 |      0.5086 |             0.0223 |                 0.6877 |             3.1196 |           1.2863 |          0.4511 |          0.81   |    0.9676 |      -0.0658 |    0.0178 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -0.0661 |        0.5263 |          -0.0003 | False          |  nan     |        nan     |     0.772  |
| H3a          | logit    | rules_tech - hitai_full                                      |  0.7877 |        0.2154 |           0.0038 | False          |  nan     |        nan     |     0.456  |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  0.4422 |        0.3292 |           0.0023 | False          |  nan     |        nan     |     0.5995 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  1.3257 |        0.0925 |           0.0078 | False          |  nan     |        nan     |     0.2906 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.4166 |        0.0157 |         nan      | False          |  nan     |        nan     |     0.1149 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0553 |        0.0363 |         nan      | False          |  nan     |        nan     |     0.1599 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.2063 |        0.2277 |           0.0055 | False          |  nan     |        nan     |     0.456  |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -0.6786 |        0.7513 |          -0.0033 | False          |  nan     |        nan     |     0.885  |
| H3a          | gbt      | rules_tech - hitai_full                                      | -0.6891 |        0.7546 |          -0.0033 | False          |  nan     |        nan     |     0.885  |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       | -0.5758 |        0.7176 |          -0.0028 | False          |  nan     |        nan     |     0.885  |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  0.2688 |        0.394  |           0.0012 | False          |  nan     |        nan     |     0.6192 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.7439 |        0.0061 |         nan      | False          |  nan     |        nan     |     0.0668 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0565 |        0.0333 |         nan      | False          |  nan     |        nan     |     0.1599 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.6049 |        0.1085 |          -0.0049 | False          |  nan     |        nan     |     0.2984 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -1.9262 |        0.973  |          -0.0102 | True           |    1     |          1     |     0.973  |
| H3a          | gbt_mono | rules_tech - hitai_full                                      | -0.7204 |        0.7644 |          -0.0039 | True           |    1     |          1     |     0.885  |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       | -1.0332 |        0.8493 |          -0.0056 | True           |    1     |          1     |     0.9169 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         | -1.1515 |        0.8752 |          -0.0059 | True           |    1     |          1     |     0.9169 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.8494 |        0.0044 |         nan      | False          |  nan     |        nan     |     0.0668 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0428 |        0.0822 |         nan      | True           |    0.411 |          0.411 |     0.2906 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.9264 |        0.3542 |          -0.0041 | False          |  nan     |        nan     |     0.5995 |
| H4b          | tagger   | corr(tag,fwd) original=0.1727 vs perturbed-context (want ~0) |  0.0118 |        0.228  |           0.161  | False          |  nan     |        nan     |     0.456  |

## Reality check / SPA vs rules_only: RC p=1.000, SPA p=1.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2568 |    0.6966 |  0.2517 | 0.0596 | 0.4983 |      0.4544 |          -2.3558 |    0.0118 |
| rules_tech|pit|gbt_mono      | 2568 |    0.696  |  0.2515 | 0.0625 | 0.4827 |      0.4544 |          -0.0632 |    0.4769 |
| hitai_full|pit|gbt_mono      | 2568 |    0.6874 |  0.2463 | 0.0435 | 0.5668 |      0.4544 |           2.409  |    0.9848 |
| hitai_full|shuffled|gbt_mono | 2568 |    0.6955 |  0.2512 | 0.061  | 0.5035 |      0.4544 |           0.8858 |    0.7945 |
