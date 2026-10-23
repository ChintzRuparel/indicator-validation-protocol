# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 20976, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 12600 |    0.6936 |  0.2502 | 0.0167 | 0.4981 |      0.5176 |             0.0061 |                 0.6927 |             0.551  |          -0.4001 |          0.1406 |          0.3907 |    0.2823 |      -0.0896 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 12600 |    0.6937 |  0.2503 | 0.0149 | 0.4967 |      0.5176 |             0.0063 |                 0.693  |             0.3016 |          -0.5003 |          0.1134 |          0.369  |    0.2367 |      -0.0907 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 12600 |    0.6932 |  0.25   | 0.014  | 0.4979 |      0.5176 |             0.0062 |                 0.6929 |             1.2749 |           0.2903 |          0.1463 |          0.4416 |    0.6626 |      -0.0424 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 12600 |    0.6985 |  0.2512 | 0.0178 | 0.499  |      0.5176 |             0.0106 |                 0.6931 |             0.8244 |           0.1002 |          0.1025 |          0.4778 |    0.5575 |      -0.0795 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 12600 |    0.6959 |  0.251  | 0.0199 | 0.5004 |      0.5176 |             0.0441 |                 0.6986 |             0.5965 |          -0.9987 |          0.3047 |          0.8344 |    0.0757 |      -0.162  |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 12600 |    0.696  |  0.2507 | 0.02   | 0.5126 |      0.5176 |             0.0207 |                 0.6937 |             0.7801 |          -0.6576 |          0.2528 |          0.6971 |    0.1721 |      -0.1245 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 12600 |    0.7016 |  0.2515 | 0.0124 | 0.4982 |      0.5176 |             0.0129 |                 0.6933 |             0.7965 |          -0.1357 |          0.1506 |          0.5829 |    0.4225 |      -0.085  |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 12600 |    0.6964 |  0.2509 | 0.0189 | 0.5017 |      0.5176 |             0.0424 |                 0.6987 |             0.696  |          -1.0981 |          0.3116 |          0.6667 |    0.0578 |      -0.1461 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 12600 |    0.6961 |  0.2508 | 0.0199 | 0.5109 |      0.5176 |             0.0205 |                 0.6938 |             0.7661 |          -0.6647 |          0.2496 |          0.6838 |    0.1694 |      -0.1224 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 12600 |    0.6847 |  0.2451 | 0.0189 | 0.5806 |      0.5176 |             0.0081 |                 0.6819 |            10.5828 |           7.8026 |          0.5515 |          0.8155 |    1      |      -0.0125 |    0.9833 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 12600 |    0.6879 |  0.2464 | 0.0112 | 0.5732 |      0.5176 |             0.015  |                 0.685  |             8.6885 |           5.9318 |          0.5226 |          0.7537 |    1      |      -0.0252 |    0.3304 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 12600 |    0.6857 |  0.2453 | 0.0122 | 0.5827 |      0.5176 |             0.008  |                 0.6819 |            10.1075 |           7.3194 |          0.5191 |          0.7538 |    1      |      -0.0187 |    0.9313 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 12600 |    0.6997 |  0.251  | 0.0149 | 0.5053 |      0.5176 |             0.0116 |                 0.6933 |             0.7337 |          -0.0326 |          0.1286 |          0.6071 |    0.4812 |      -0.0668 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 12600 |    0.6965 |  0.2508 | 0.0156 | 0.501  |      0.5176 |             0.0433 |                 0.6986 |             0.755  |          -0.6915 |          0.2633 |          0.7075 |    0.1602 |      -0.1301 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 12600 |    0.6961 |  0.2509 | 0.0201 | 0.5102 |      0.5176 |             0.019  |                 0.6938 |             0.7159 |          -0.7008 |          0.244  |          0.6676 |    0.1568 |      -0.1424 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 12600 |    0.701  |  0.2513 | 0.0145 | 0.5063 |      0.5176 |             0.0098 |                 0.693  |             0.3964 |          -0.6912 |          0.1734 |          0.5615 |    0.1604 |      -0.1366 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 12600 |    0.6977 |  0.2512 | 0.0188 | 0.4994 |      0.5176 |             0.0459 |                 0.6989 |             0.4549 |          -0.836  |          0.2367 |          0.7112 |    0.1156 |      -0.1604 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 12600 |    0.6964 |  0.2508 | 0.018  | 0.513  |      0.5176 |             0.019  |                 0.6935 |             0.719  |          -0.8612 |          0.2708 |          0.7025 |    0.1087 |      -0.1361 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 12600 |    0.688  |  0.245  | 0.0076 | 0.5844 |      0.5176 |             0.0123 |                 0.6814 |             9.3788 |           6.7341 |          0.5489 |          0.9479 |    1      |      -0.0176 |    0.7545 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 12600 |    0.6915 |  0.2464 | 0.0093 | 0.5747 |      0.5176 |             0.0195 |                 0.6849 |             7.0249 |           4.3231 |          0.5069 |          0.841  |    1      |      -0.0217 |    0.0032 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 12600 |    0.6847 |  0.2452 | 0.0151 | 0.5825 |      0.5176 |             0.0103 |                 0.6808 |             8.3961 |           5.7438 |          0.5097 |          0.8378 |    1      |      -0.0185 |    0.255  |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  3.7941 |        0.0001 |           0.0089 | False          | nan      |       nan      |     0.0001 |
| H3a          | logit    | rules_tech - hitai_full                                      |  5.0809 |        0      |           0.017  | False          | nan      |       nan      |     0      |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  4.761  |        0      |           0.0151 | False          | nan      |       nan      |     0      |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  5.068  |        0      |           0.0164 | False          | nan      |       nan      |     0      |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.9041 |        0.0569 |         nan      | False          | nan      |       nan      |     0.0695 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0853 |        0      |         nan      | False          | nan      |       nan      |     0.0001 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.3479 |        0.1777 |           0.0034 | False          | nan      |       nan      |     0.1955 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  2.5366 |        0.0056 |           0.0058 | False          | nan      |       nan      |     0.0082 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  3.8237 |        0.0001 |           0.0085 | False          | nan      |       nan      |     0.0001 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  3.5416 |        0.0002 |           0.0086 | False          | nan      |       nan      |     0.0003 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  3.7976 |        0.0001 |           0.0098 | False          | nan      |       nan      |     0.0001 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.2483 |        0.2119 |         nan      | False          | nan      |       nan      |     0.222  |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0933 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.4444 |        0.1486 |           0.0036 | False          | nan      |       nan      |     0.1721 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  3.0498 |        0.0011 |           0.0076 | True           |   0.0011 |         0.0057 |     0.0018 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  4.0816 |        0      |           0.0104 | True           |   0.0001 |         0.0001 |     0.0001 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  4.0607 |        0      |           0.0105 | True           |   0.0001 |         0.0001 |     0.0001 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  4.0876 |        0      |           0.0107 | True           |   0.0001 |         0.0001 |     0.0001 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.1003 |        0.0357 |         nan      | False          | nan      |       nan      |     0.0465 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0948 |        0      |         nan      | True           |   0      |         0      |     0      |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.6751 |        0.4996 |          -0.001  | False          | nan      |       nan      |     0.4996 |
| H4b          | tagger   | corr(tag,fwd) original=0.1751 vs perturbed-context (want ~0) | -0.0145 |        0.036  |           0.1896 | False          | nan      |       nan      |     0.0465 |

## Reality check / SPA vs rules_only: RC p=0.000, SPA p=0.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5136 |    0.6965 |  0.2517 | 0.0476 | 0.5047 |      0.4776 |          -1.8137 |    0.0462 |
| rules_tech|pit|gbt_mono      | 5136 |    0.6974 |  0.2521 | 0.0484 | 0.4992 |      0.4776 |          -2.0513 |    0.0297 |
| hitai_full|pit|gbt_mono      | 5136 |    0.6893 |  0.2475 | 0.0425 | 0.577  |      0.4776 |           4.1799 |    0.9999 |
| hitai_full|shuffled|gbt_mono | 5136 |    0.6974 |  0.2521 | 0.0484 | 0.4992 |      0.4776 |          -2.0513 |    0.0297 |
