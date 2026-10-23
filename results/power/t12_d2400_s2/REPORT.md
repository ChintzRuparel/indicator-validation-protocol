# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 22008, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 13212 |    0.6988 |  0.2512 | 0.0242 | 0.4938 |      0.5076 |             0.0118 |                 0.6935 |             0.5145 |          -0.1011 |          0.1111 |          0.3073 |    0.4163 |      -0.0925 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 13212 |    0.6967 |  0.251  | 0.0269 | 0.4907 |      0.5076 |             0.0138 |                 0.6939 |             0.275  |          -0.3626 |          0.1122 |          0.2969 |    0.2238 |      -0.0975 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 13212 |    0.6944 |  0.2506 | 0.0262 | 0.4951 |      0.5076 |             0.011  |                 0.6938 |             0.3292 |          -0.1791 |          0.0825 |          0.25   |    0.3539 |      -0.0925 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 13212 |    0.7004 |  0.2518 | 0.0294 | 0.4957 |      0.5076 |             0.024  |                 0.6944 |             0.1755 |          -0.7453 |          0.1757 |          0.4001 |    0.0596 |      -0.1942 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 13212 |    0.6995 |  0.2511 | 0.0204 | 0.5011 |      0.5076 |             0.0396 |                 0.6982 |             0.2235 |          -0.4124 |          0.1132 |          0.3036 |    0.1937 |      -0.1276 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 13212 |    0.6962 |  0.251  | 0.0202 | 0.4931 |      0.5076 |             0.0322 |                 0.6953 |            -0.149  |          -0.5169 |          0.0595 |          0.2464 |    0.139  |      -0.1067 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 13212 |    0.6984 |  0.2518 | 0.0314 | 0.4977 |      0.5076 |             0.0268 |                 0.6947 |            -0.2198 |          -1.0294 |          0.1491 |          0.3896 |    0.0159 |      -0.2238 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 13212 |    0.6991 |  0.251  | 0.021  | 0.5006 |      0.5076 |             0.04   |                 0.6982 |             0.1704 |          -0.3987 |          0.099  |          0.2899 |    0.2018 |      -0.1145 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 13212 |    0.6962 |  0.251  | 0.0202 | 0.4931 |      0.5076 |             0.0322 |                 0.6953 |            -0.149  |          -0.5169 |          0.0595 |          0.2464 |    0.139  |      -0.1067 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 13212 |    0.691  |  0.2469 | 0.0177 | 0.5736 |      0.5076 |             0.0143 |                 0.6844 |             7.1202 |           5.1489 |          0.5561 |          0.8557 |    1      |      -0.0687 |    0.8218 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 13212 |    0.6885 |  0.2467 | 0.0131 | 0.5709 |      0.5076 |             0.0224 |                 0.6866 |             5.8233 |           3.8789 |          0.564  |          0.9318 |    1      |      -0.0699 |    0.0485 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 13212 |    0.6864 |  0.2461 | 0.011  | 0.575  |      0.5076 |             0.016  |                 0.6839 |             6.5518 |           4.7361 |          0.5533 |          0.9802 |    1      |      -0.0596 |    0.5365 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 13212 |    0.6992 |  0.2516 | 0.026  | 0.499  |      0.5076 |             0.0291 |                 0.6948 |            -0.386  |          -1.4023 |          0.1871 |          0.3877 |    0.0017 |      -0.3003 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 13212 |    0.6987 |  0.2511 | 0.0203 | 0.4987 |      0.5076 |             0.0423 |                 0.6981 |             0.1613 |          -0.3659 |          0.0938 |          0.2929 |    0.222  |      -0.0948 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 13212 |    0.696  |  0.2509 | 0.0193 | 0.4942 |      0.5076 |             0.029  |                 0.6951 |             0.0444 |          -0.3383 |          0.0613 |          0.2499 |    0.2393 |      -0.0912 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 13212 |    0.698  |  0.2515 | 0.0324 | 0.4985 |      0.5076 |             0.0283 |                 0.6953 |             0.0633 |          -1.3506 |          0.2616 |          0.3626 |    0.0023 |      -0.3099 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 13212 |    0.6966 |  0.2511 | 0.0266 | 0.4955 |      0.5076 |             0.0441 |                 0.6986 |            -0.1419 |          -1.0707 |          0.1842 |          0.3872 |    0.0123 |      -0.267  |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 13212 |    0.6954 |  0.2509 | 0.0274 | 0.492  |      0.5076 |             0.0319 |                 0.6949 |             0.3415 |          -0.1718 |          0.0869 |          0.2789 |    0.3596 |      -0.0925 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 13212 |    0.6911 |  0.247  | 0.0146 | 0.575  |      0.5076 |             0.0139 |                 0.6843 |             7.2554 |           5.2579 |          0.5481 |          0.8694 |    1      |      -0.0478 |    0.8766 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 13212 |    0.6877 |  0.2466 | 0.0085 | 0.5733 |      0.5076 |             0.023  |                 0.6855 |             5.6513 |           3.7103 |          0.5574 |          0.8243 |    1      |      -0.0459 |    0.0208 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 13212 |    0.6847 |  0.2457 | 0.0138 | 0.581  |      0.5076 |             0.0178 |                 0.6833 |             6.5446 |           4.7006 |          0.5437 |          0.8758 |    1      |      -0.0468 |    0.5081 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  2.4525 |        0.0071 |           0.0078 | False          | nan      |       nan      |     0.0104 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.7773 |        0.0027 |           0.0075 | False          | nan      |       nan      |     0.006  |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.9584 |        0.0015 |           0.0082 | False          | nan      |       nan      |     0.0038 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.5546 |        0.0053 |           0.0071 | False          | nan      |       nan      |     0.009  |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.6955 |        0.007  |         nan      | False          | nan      |       nan      |     0.0104 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0489 |        0.0108 |         nan      | False          | nan      |       nan      |     0.0149 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.0548 |        0.9563 |           0.0001 | False          | nan      |       nan      |     0.9733 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  3.6394 |        0.0001 |           0.0082 | False          | nan      |       nan      |     0.0004 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  4.6405 |        0      |           0.0106 | False          | nan      |       nan      |     0      |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  3.8117 |        0.0001 |           0.0102 | False          | nan      |       nan      |     0.0002 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  4.1331 |        0      |           0.0081 | False          | nan      |       nan      |     0.0001 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.2571 |        0.2087 |         nan      | False          | nan      |       nan      |     0.2417 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0554 |        0.0046 |         nan      | False          | nan      |       nan      |     0.0085 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.4439 |        0.6571 |          -0.0008 | False          | nan      |       nan      |     0.7228 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  3.8919 |        0      |           0.0079 | True           |   0.0001 |         0.0002 |     0.0002 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  4.5676 |        0      |           0.0098 | True           |   0      |         0      |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  4.452  |        0      |           0.0095 | True           |   0      |         0      |     0      |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  4.6589 |        0      |           0.009  | True           |   0      |         0      |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.0682 |        0.0386 |         nan      | False          | nan      |       nan      |     0.05   |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0576 |        0.0034 |         nan      | True           |   0.0034 |         0.017  |     0.0068 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.4132 |        0.1576 |          -0.0017 | False          | nan      |       nan      |     0.1926 |
| H4b          | tagger   | corr(tag,fwd) original=0.1778 vs perturbed-context (want ~0) | -0.0002 |        0.9733 |           0.178  | False          | nan      |       nan      |     0.9733 |

## Reality check / SPA vs rules_only: RC p=0.000, SPA p=0.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5448 |    0.6974 |  0.2508 | 0.0206 | 0.4994 |      0.5029 |          -0.2702 |    0.3583 |
| rules_tech|pit|gbt_mono      | 5448 |    0.7013 |  0.2498 | 0.0177 | 0.5202 |      0.5029 |          -0.4758 |    0.2605 |
| hitai_full|pit|gbt_mono      | 5448 |    0.6875 |  0.2455 | 0.0128 | 0.5803 |      0.5029 |           5.7651 |    1      |
| hitai_full|shuffled|gbt_mono | 5448 |    0.6996 |  0.2495 | 0.017  | 0.5178 |      0.5029 |          -0.635  |    0.1957 |
