# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 22008, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 13212 |    0.6946 |  0.2507 | 0.0154 | 0.5095 |      0.5031 |             0.0123 |                 0.6936 |             0.0712 |          -0.8803 |          0.1785 |          0.4519 |    0.0335 |      -0.2357 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 13212 |    0.6947 |  0.2508 | 0.0153 | 0.5042 |      0.5031 |             0.0143 |                 0.6942 |            -0.5431 |          -1.2733 |          0.1387 |          0.4215 |    0.0041 |      -0.3076 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 13212 |    0.6938 |  0.2503 | 0.0073 | 0.5029 |      0.5031 |             0.0119 |                 0.6938 |             0.0454 |          -0.8457 |          0.1385 |          0.2855 |    0.0391 |      -0.1916 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 13212 |    0.6951 |  0.2506 | 0.016  | 0.5028 |      0.5031 |             0.0152 |                 0.6942 |             0.0507 |          -0.8037 |          0.1708 |          0.456  |    0.0468 |      -0.2322 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 13212 |    0.6958 |  0.251  | 0.0105 | 0.5031 |      0.5031 |             0.0513 |                 0.7031 |             0.2214 |          -0.753  |          0.0966 |          0.0998 |    0.0597 |      -0.1135 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 13212 |    0.6993 |  0.2515 | 0.0125 | 0.4992 |      0.5031 |             0.0346 |                 0.6989 |            -0.336  |          -1.2145 |          0.0973 |          0.125  |    0.0056 |      -0.1571 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 13212 |    0.6965 |  0.2508 | 0.0136 | 0.4995 |      0.5031 |             0.0149 |                 0.6945 |            -0.211  |          -1.0058 |          0.142  |          0.3714 |    0.0181 |      -0.2376 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 13212 |    0.6966 |  0.2513 | 0.0147 | 0.4972 |      0.5031 |             0.0512 |                 0.7035 |             0.0228 |          -0.9537 |          0.0916 |          0.0883 |    0.0235 |      -0.1096 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 13212 |    0.6994 |  0.2515 | 0.0123 | 0.4993 |      0.5031 |             0.0355 |                 0.6989 |            -0.4992 |          -1.3812 |          0.0971 |          0.1219 |    0.002  |      -0.1736 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 13212 |    0.6891 |  0.2452 | 0.0147 | 0.5853 |      0.5031 |             0.0169 |                 0.682  |             7.2304 |           5.0876 |          0.558  |          0.7796 |    1      |      -0.0356 |    0.7411 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 13212 |    0.6913 |  0.2476 | 0.0158 | 0.5656 |      0.5031 |             0.0273 |                 0.6888 |             5.1841 |           3.2816 |          0.5379 |          0.8772 |    1      |      -0.0916 |    0.0009 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 13212 |    0.6882 |  0.2465 | 0.0136 | 0.5758 |      0.5031 |             0.0174 |                 0.6844 |             6.4155 |           4.4155 |          0.5238 |          0.814  |    1      |      -0.0356 |    0.2261 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 13212 |    0.696  |  0.2507 | 0.0157 | 0.5012 |      0.5031 |             0.0179 |                 0.6947 |            -0.5434 |          -1.2402 |          0.115  |          0.309  |    0.0049 |      -0.2644 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 13212 |    0.6975 |  0.2511 | 0.0062 | 0.5027 |      0.5031 |             0.0518 |                 0.7031 |             0.037  |          -1.0699 |          0.1243 |          0.1369 |    0.0139 |      -0.1379 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 13212 |    0.7003 |  0.2516 | 0.0117 | 0.5034 |      0.5031 |             0.0335 |                 0.6989 |            -0.0443 |          -1.0585 |          0.1253 |          0.1621 |    0.0136 |      -0.1539 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 13212 |    0.695  |  0.2508 | 0.0173 | 0.5018 |      0.5031 |             0.0254 |                 0.695  |            -0.2035 |          -1.1392 |          0.1632 |          0.3627 |    0.0087 |      -0.2602 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 13212 |    0.6968 |  0.2514 | 0.0128 | 0.499  |      0.5031 |             0.0598 |                 0.7034 |            -0.5432 |          -1.5477 |          0.111  |          0.1218 |    0.0005 |      -0.1907 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 13212 |    0.6985 |  0.2513 | 0.0146 | 0.4927 |      0.5031 |             0.0392 |                 0.6989 |             0.1192 |          -0.848  |          0.1097 |          0.1262 |    0.039  |      -0.1078 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 13212 |    0.6898 |  0.2455 | 0.0165 | 0.5835 |      0.5031 |             0.0161 |                 0.682  |             7.1965 |           5.065  |          0.559  |          0.8429 |    1      |      -0.0321 |    0.7241 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 13212 |    0.6877 |  0.2464 | 0.0137 | 0.5724 |      0.5031 |             0.0267 |                 0.688  |             5.5878 |           3.4628 |          0.5311 |          0.7396 |    1      |      -0.0508 |    0.003  |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 13212 |    0.6887 |  0.2462 | 0.0124 | 0.5781 |      0.5031 |             0.0179 |                 0.6842 |             6.1421 |           4.0132 |          0.5472 |          0.8243 |    1      |      -0.0401 |    0.0535 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  1.8667 |        0.031  |           0.0056 | False          | nan      |       nan      |     0.038  |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.5019 |        0.0062 |           0.0074 | False          | nan      |       nan      |     0.0131 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.4414 |        0.0073 |           0.007  | False          | nan      |       nan      |     0.0134 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.0186 |        0.0218 |           0.006  | False          | nan      |       nan      |     0.0299 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.247  |        0      |         nan      | False          | nan      |       nan      |     0.0002 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0315 |        0.0692 |         nan      | False          | nan      |       nan      |     0.0802 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.3027 |        0.7621 |           0.0007 | False          | nan      |       nan      |     0.7765 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  1.4252 |        0.077  |           0.0034 | False          | nan      |       nan      |     0.0848 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  2.19   |        0.0143 |           0.0053 | False          | nan      |       nan      |     0.0224 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  2.7169 |        0.0033 |           0.0061 | False          | nan      |       nan      |     0.0091 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  2.4808 |        0.0066 |           0.0055 | False          | nan      |       nan      |     0.0131 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.8212 |        0.0001 |         nan      | False          | nan      |       nan      |     0.0005 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0582 |        0.0031 |         nan      | False          | nan      |       nan      |     0.0091 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -2.1558 |        0.0311 |          -0.0037 | False          | nan      |       nan      |     0.038  |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  2.3585 |        0.0092 |           0.0056 | True           |   0.0092 |         0.0459 |     0.0155 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  4.1526 |        0      |           0.0112 | True           |   0.0001 |         0.0001 |     0.0002 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  3.824  |        0.0001 |           0.0121 | True           |   0.0003 |         0.0003 |     0.0003 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  3.7856 |        0.0001 |           0.0103 | True           |   0.0003 |         0.0004 |     0.0003 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.5837 |        0      |         nan      | False          | nan      |       nan      |     0.0001 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.057  |        0.0037 |         nan      | True           |   0.0074 |         0.0185 |     0.0091 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.2839 |        0.7765 |           0.0005 | False          | nan      |       nan      |     0.7765 |
| H4b          | tagger   | corr(tag,fwd) original=0.1740 vs perturbed-context (want ~0) | -0.0161 |        0.0171 |           0.19   | False          | nan      |       nan      |     0.0251 |

## Reality check / SPA vs rules_only: RC p=0.027, SPA p=0.040

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5448 |    0.6936 |  0.2502 | 0.0198 | 0.5077 |      0.5029 |          -0.1553 |    0.4174 |
| rules_tech|pit|gbt_mono      | 5448 |    0.6943 |  0.2506 | 0.0258 | 0.5016 |      0.5029 |          -1.0313 |    0.0846 |
| hitai_full|pit|gbt_mono      | 5448 |    0.6836 |  0.2452 | 0.02   | 0.5797 |      0.5029 |           4.4455 |    1      |
| hitai_full|shuffled|gbt_mono | 5448 |    0.6946 |  0.2507 | 0.0229 | 0.5    |      0.5029 |          -1.1277 |    0.0665 |
