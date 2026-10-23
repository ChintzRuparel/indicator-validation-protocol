# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 11004, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6606 |    0.6982 |  0.2521 | 0.02   | 0.5001 |       0.497 |             0.0272 |                 0.6944 |             0.0345 |          -0.4525 |          0.1375 |          0.418  |    0.1711 |      -0.2358 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6606 |    0.6952 |  0.251  | 0.0126 | 0.5086 |       0.497 |             0.027  |                 0.6944 |            -0.1332 |          -0.6217 |          0.115  |          0.3117 |    0.0966 |      -0.2125 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6606 |    0.6941 |  0.2501 | 0.0041 | 0.504  |       0.497 |             0.0257 |                 0.6951 |            -0.2568 |          -0.8648 |          0.0593 |          0.0447 |    0.0275 |      -0.1268 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6606 |    0.7035 |  0.2517 | 0.0201 | 0.4985 |       0.497 |             0.0316 |                 0.6972 |             0.0104 |          -0.7093 |          0.1877 |          0.3733 |    0.0687 |      -0.2543 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6606 |    0.6991 |  0.2511 | 0.013  | 0.4995 |       0.497 |             0.0715 |                 0.7095 |            -0.0336 |          -0.9914 |          0.1396 |          0.1217 |    0.0182 |      -0.1755 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6606 |    0.6952 |  0.251  | 0.0241 | 0.489  |       0.497 |             0.0519 |                 0.7012 |            -0.1122 |          -0.9686 |          0.1364 |          0.1527 |    0.0197 |      -0.1917 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6606 |    0.704  |  0.251  | 0.0111 | 0.5127 |       0.497 |             0.0358 |                 0.6971 |             0.2204 |          -0.5544 |          0.2066 |          0.3798 |    0.1227 |      -0.2255 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6606 |    0.6969 |  0.2508 | 0.0171 | 0.4966 |       0.497 |             0.0702 |                 0.7093 |             0.0912 |          -0.9016 |          0.1447 |          0.1282 |    0.0286 |      -0.1581 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6606 |    0.6952 |  0.251  | 0.0241 | 0.489  |       0.497 |             0.0519 |                 0.7012 |            -0.1122 |          -0.9686 |          0.1364 |          0.1527 |    0.0197 |      -0.1917 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6606 |    0.6874 |  0.2464 | 0.0161 | 0.5741 |       0.497 |             0.0284 |                 0.6857 |             4.0292 |           2.5546 |          0.5622 |          0.8418 |    1      |      -0.0531 |    0.5122 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6606 |    0.7102 |  0.2516 | 0.0204 | 0.5388 |       0.497 |             0.0526 |                 0.6981 |             2.3023 |           0.84   |          0.521  |          0.8023 |    0.9595 |      -0.1252 |    0.0002 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6606 |    0.6938 |  0.2485 | 0.0119 | 0.5583 |       0.497 |             0.0327 |                 0.6889 |             3.6901 |           2.2191 |          0.5389 |          0.7849 |    1      |      -0.0728 |    0.2531 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6606 |    0.7038 |  0.2515 | 0.0115 | 0.5088 |       0.497 |             0.0319 |                 0.6974 |             0.1329 |          -0.6784 |          0.1812 |          0.2589 |    0.079  |      -0.2275 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6606 |    0.6989 |  0.2511 | 0.0096 | 0.5    |       0.497 |             0.0715 |                 0.7092 |            -0.1116 |          -0.8774 |          0.0969 |          0.0736 |    0.0287 |      -0.129  |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6606 |    0.6963 |  0.2512 | 0.0164 | 0.4914 |       0.497 |             0.0553 |                 0.7017 |             0.2378 |          -0.6798 |          0.1346 |          0.132  |    0.0778 |      -0.1139 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6606 |    0.6969 |  0.2511 | 0.0118 | 0.5112 |       0.497 |             0.0364 |                 0.6976 |             0.9145 |          -0.0539 |          0.2687 |          0.4705 |    0.4551 |      -0.2082 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6606 |    0.7014 |  0.2517 | 0.0139 | 0.4949 |       0.497 |             0.076  |                 0.7096 |            -0.3644 |          -0.8906 |          0.0527 |          0.0345 |    0.0193 |      -0.1039 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6606 |    0.6982 |  0.2516 | 0.0173 | 0.4955 |       0.497 |             0.0544 |                 0.7011 |             0.1465 |          -0.9362 |          0.1916 |          0.173  |    0.0257 |      -0.2083 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6606 |    0.688  |  0.2471 | 0.0172 | 0.5698 |       0.497 |             0.0313 |                 0.685  |             4.2943 |           2.8261 |          0.5559 |          0.8411 |    1      |      -0.0556 |    0.7242 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6606 |    0.6961 |  0.2493 | 0.0156 | 0.5501 |       0.497 |             0.0411 |                 0.6961 |             2.4678 |           0.9669 |          0.5294 |          0.7265 |    0.9788 |      -0.092  |    0.0005 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6606 |    0.6915 |  0.2479 | 0.0145 | 0.5626 |       0.497 |             0.0306 |                 0.6884 |             3.6939 |           2.1603 |          0.5728 |          0.8258 |    1      |      -0.0754 |    0.2148 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  3.0413 |        0.0012 |           0.0108 | False          | nan      |       nan      |     0.0052 |
| H3a          | logit    | rules_tech - hitai_full                                      |  3.6025 |        0.0002 |           0.0166 | False          | nan      |       nan      |     0.0012 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  3.9216 |        0      |           0.0165 | False          | nan      |       nan      |     0.0005 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.9782 |        0.0014 |           0.0096 | False          | nan      |       nan      |     0.0053 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.875  |        0.0608 |         nan      | False          | nan      |       nan      |     0.1486 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0288 |        0.1696 |         nan      | False          | nan      |       nan      |     0.3239 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.3414 |        0.7328 |           0.0007 | False          | nan      |       nan      |     0.9483 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -2.6868 |        0.9964 |          -0.015  | False          | nan      |       nan      |     0.997  |
| H3a          | gbt      | rules_tech - hitai_full                                      | -2.7492 |        0.997  |          -0.0133 | False          | nan      |       nan      |     0.997  |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       | -2.3188 |        0.9898 |          -0.0113 | False          | nan      |       nan      |     0.997  |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         | -1.7315 |        0.9583 |          -0.0088 | False          | nan      |       nan      |     0.997  |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.7835 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0467 |        0.0605 |         nan      | False          | nan      |       nan      |     0.1486 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -3.5207 |        0.0004 |          -0.0141 | False          | nan      |       nan      |     0.0024 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  0.0874 |        0.4652 |           0.0003 | True           |   0.707  |         1      |     0.6396 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  0.4455 |        0.328  |           0.0015 | True           |   0.707  |         1      |     0.5154 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  0.7203 |        0.2357 |           0.0025 | True           |   0.707  |         1      |     0.3988 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  1.3356 |        0.0908 |           0.0044 | True           |   0.4542 |         0.4542 |     0.1999 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.7289 |        0.0064 |         nan      | False          | nan      |       nan      |     0.02   |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.028  |        0.1767 |         nan      | True           |   0.7067 |         0.8834 |     0.3239 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.7602 |        0.4471 |          -0.0023 | False          | nan      |       nan      |     0.6396 |
| H4b          | tagger   | corr(tag,fwd) original=0.1577 vs perturbed-context (want ~0) |  0.0003 |        0.9775 |           0.1574 | False          | nan      |       nan      |     0.997  |

## Reality check / SPA vs rules_only: RC p=0.227, SPA p=0.120

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2724 |    0.6935 |  0.2502 | 0.0311 | 0.5123 |      0.4776 |           0.5044 |    0.75   |
| rules_tech|pit|gbt_mono      | 2724 |    0.7015 |  0.2538 | 0.0583 | 0.4943 |      0.4776 |          -1.2217 |    0.0507 |
| hitai_full|pit|gbt_mono      | 2724 |    0.6944 |  0.2463 | 0.0458 | 0.586  |      0.4776 |           2.8974 |    1      |
| hitai_full|shuffled|gbt_mono | 2724 |    0.701  |  0.2536 | 0.0541 | 0.4929 |      0.4776 |          -1.3198 |    0.0381 |
