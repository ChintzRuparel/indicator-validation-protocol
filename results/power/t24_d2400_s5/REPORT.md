# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6944 |  0.2506 | 0.0091 | 0.4982 |      0.5021 |             0.0106 |                 0.6941 |            -0.0028 |          -0.9543 |          0.0671 |          0.1368 |    0.0213 |      -0.0782 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.694  |  0.2504 | 0.0183 | 0.4936 |      0.5021 |             0.0169 |                 0.6946 |            -0.4037 |          -1.0463 |          0.0433 |          0.1282 |    0.0128 |      -0.0775 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6938 |  0.2503 | 0.0151 | 0.4973 |      0.5021 |             0.0196 |                 0.6938 |            -0.2315 |          -0.9265 |          0.0453 |          0.1215 |    0.0245 |      -0.0665 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6961 |  0.2509 | 0.0104 | 0.5019 |      0.5021 |             0.0145 |                 0.6942 |             0.129  |          -0.5885 |          0.0683 |          0.2242 |    0.1083 |      -0.0617 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6973 |  0.2514 | 0.0209 | 0.4952 |      0.5021 |             0.0401 |                 0.6989 |             0.1465 |          -1.0353 |          0.1006 |          0.2079 |    0.0137 |      -0.1077 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6961 |  0.2513 | 0.0184 | 0.4946 |      0.5021 |             0.0284 |                 0.696  |             0.243  |          -0.9355 |          0.1004 |          0.1979 |    0.0246 |      -0.1044 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6961 |  0.2511 | 0.0145 | 0.4978 |      0.5021 |             0.022  |                 0.6956 |             0.1594 |          -0.6989 |          0.0806 |          0.2097 |    0.07   |      -0.0778 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6989 |  0.2515 | 0.0206 | 0.4933 |      0.5021 |             0.0405 |                 0.699  |             0.158  |          -0.8946 |          0.0863 |          0.2024 |    0.0294 |      -0.0939 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6959 |  0.2512 | 0.018  | 0.4965 |      0.5021 |             0.0281 |                 0.696  |             0.5706 |          -0.926  |          0.1514 |          0.2574 |    0.0274 |      -0.1129 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6924 |  0.2476 | 0.0125 | 0.565  |      0.5021 |             0.0148 |                 0.6864 |             9.0547 |           6.1907 |          0.5238 |          0.8116 |    1      |      -0.0128 |    0.4099 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6916 |  0.2481 | 0.016  | 0.5622 |      0.5021 |             0.0205 |                 0.6886 |             8.25   |           5.2042 |          0.5523 |          0.8285 |    1      |      -0.0235 |    0.0108 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6888 |  0.2471 | 0.0131 | 0.5692 |      0.5021 |             0.0124 |                 0.6855 |             9.0851 |           6.1147 |          0.5267 |          0.7599 |    1      |      -0.0176 |    0.3493 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6966 |  0.2512 | 0.012  | 0.5003 |      0.5021 |             0.0201 |                 0.6956 |             0.2728 |          -0.823  |          0.1083 |          0.2305 |    0.0418 |      -0.099  |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6987 |  0.2514 | 0.0154 | 0.4956 |      0.5021 |             0.0412 |                 0.699  |            -0.0191 |          -1.2186 |          0.108  |          0.2105 |    0.0052 |      -0.1302 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6962 |  0.2513 | 0.0181 | 0.4958 |      0.5021 |             0.026  |                 0.696  |             0.3275 |          -1.1705 |          0.1469 |          0.2464 |    0.0072 |      -0.1356 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6975 |  0.2512 | 0.0203 | 0.4943 |      0.5021 |             0.0202 |                 0.6955 |             0.1052 |          -0.9277 |          0.1176 |          0.2937 |    0.0252 |      -0.1196 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6969 |  0.2511 | 0.0153 | 0.4974 |      0.5021 |             0.0398 |                 0.6987 |             0.0666 |          -0.9799 |          0.0815 |          0.1757 |    0.0177 |      -0.0905 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6965 |  0.2512 | 0.0187 | 0.4961 |      0.5021 |             0.0264 |                 0.6959 |             0.2367 |          -1.1347 |          0.125  |          0.2072 |    0.0085 |      -0.1269 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6898 |  0.2471 | 0.0111 | 0.5674 |      0.5021 |             0.0108 |                 0.6866 |             9.5861 |           6.6978 |          0.5304 |          0.8586 |    1      |      -0.0175 |    0.7767 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.691  |  0.2478 | 0.0151 | 0.5631 |      0.5021 |             0.0214 |                 0.6886 |             9.2132 |           6.1227 |          0.5553 |          0.8381 |    1      |      -0.0213 |    0.3541 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6897 |  0.2472 | 0.0164 | 0.5702 |      0.5021 |             0.011  |                 0.6856 |             9.3551 |           6.3227 |          0.5492 |          0.8507 |    1      |      -0.0215 |    0.5141 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  1.0949 |        0.1368 |           0.002  | False          | nan      |       nan      |     0.1505 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.2224 |        0.0131 |           0.0037 | False          | nan      |       nan      |     0.0181 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.5425 |        0.0055 |           0.0042 | False          | nan      |       nan      |     0.0086 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.7855 |        0.0027 |           0.0051 | False          | nan      |       nan      |     0.0049 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.9491 |        0.0001 |         nan      | False          | nan      |       nan      |     0.0002 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0352 |        0.0096 |         nan      | False          | nan      |       nan      |     0.0141 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -2.4029 |        0.0163 |          -0.0026 | False          | nan      |       nan      |     0.021  |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  1.6222 |        0.0524 |           0.0025 | False          | nan      |       nan      |     0.064  |
| H3a          | gbt      | rules_tech - hitai_full                                      |  4.0971 |        0      |           0.0073 | False          | nan      |       nan      |     0.0001 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  4.0071 |        0      |           0.0072 | False          | nan      |       nan      |     0.0001 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  3.3136 |        0.0005 |           0.0053 | False          | nan      |       nan      |     0.0011 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.4108 |        0      |         nan      | False          | nan      |       nan      |     0.0001 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0414 |        0.0029 |         nan      | False          | nan      |       nan      |     0.005  |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.5247 |        0.5998 |          -0.0005 | False          | nan      |       nan      |     0.5998 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  3.2254 |        0.0006 |           0.0051 | True           |   0.0013 |         0.0031 |     0.0014 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  4.8458 |        0      |           0.0072 | True           |   0      |         0      |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  5.1044 |        0      |           0.0075 | True           |   0      |         0      |     0      |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  5.298  |        0      |           0.0078 | True           |   0      |         0      |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.0867 |        0      |         nan      | False          | nan      |       nan      |     0.0001 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0474 |        0.0008 |         nan      | True           |   0.0013 |         0.0041 |     0.0016 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.9296 |        0.3526 |           0.001  | False          | nan      |       nan      |     0.3694 |
| H4b          | tagger   | corr(tag,fwd) original=0.1681 vs perturbed-context (want ~0) | -0.0079 |        0.0962 |           0.1761 | False          | nan      |       nan      |     0.1114 |

## Reality check / SPA vs rules_only: RC p=0.000, SPA p=0.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6935 |  0.2502 | 0.0137 | 0.4995 |      0.5017 |          -1.9611 |    0.0044 |
| rules_tech|pit|gbt_mono      | 10896 |    0.6936 |  0.2502 | 0.0131 | 0.5052 |      0.5017 |          -1.3609 |    0.0323 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6837 |  0.2449 | 0.0119 | 0.5847 |      0.5017 |           8.9601 |    1      |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6935 |  0.2502 | 0.0132 | 0.508  |      0.5017 |          -0.2024 |    0.3932 |
