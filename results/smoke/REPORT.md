# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 5244, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 3150 |    0.6962 |  0.2514 | 0.0334 | 0.5143 |      0.5333 |             0.0433 |                 0.696  |             0.3886 |           0.0127 |          0.1257 |          0.6248 |    0.5073 |      -0.1328 |    0.0006 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 3150 |    0.6978 |  0.2523 | 0.0371 | 0.4995 |      0.5333 |             0.0431 |                 0.6962 |            -0.3425 |          -0.5535 |          0.0708 |          0.5381 |    0.2116 |      -0.1401 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 3150 |    0.696  |  0.2514 | 0.0357 | 0.4987 |      0.5333 |             0.0408 |                 0.6956 |             0.1382 |           0.0641 |          0.0292 |          0.8    |    0.5368 |      -0.1571 |    0.0008 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 3150 |    0.716  |  0.2536 | 0.0574 | 0.5272 |      0.5333 |             0.0459 |                 0.6946 |             0.2788 |          -0.3699 |          0.2632 |          0.8108 |    0.2965 |      -0.1254 |    0.0001 |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 3150 |    0.707  |  0.253  | 0.0506 | 0.5208 |      0.5333 |             0.0886 |                 0.7147 |             0.7019 |           0.0335 |          0.2692 |          0.8114 |    0.5193 |      -0.1244 |    0.0007 |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 3150 |    0.7235 |  0.2549 | 0.0594 | 0.5152 |      0.5333 |             0.0609 |                 0.7011 |             0.5854 |          -0.1035 |          0.2768 |          0.8854 |    0.4406 |      -0.1811 |    0.0003 |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 3150 |    0.7153 |  0.2551 | 0.0485 | 0.5163 |      0.5333 |             0.0503 |                 0.6958 |            -0.0882 |          -0.785  |          0.2651 |          0.7448 |    0.1275 |      -0.1782 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 3150 |    0.707  |  0.253  | 0.0506 | 0.5208 |      0.5333 |             0.0886 |                 0.7147 |             0.7019 |           0.0335 |          0.2692 |          0.8114 |    0.5193 |      -0.1244 |    0.0007 |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 3150 |    0.7241 |  0.2551 | 0.0591 | 0.5132 |      0.5333 |             0.0625 |                 0.701  |             0.7235 |           0.0341 |          0.2768 |          0.8797 |    0.5196 |      -0.1811 |    0.0007 |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 3150 |    0.7279 |  0.2527 | 0.0618 | 0.5691 |      0.5333 |             0.0535 |                 0.6907 |             3.1972 |           2.1613 |          0.4406 |          0.9797 |    0.9991 |      -0.0648 |    0.4441 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 3150 |    0.7024 |  0.2513 | 0.0427 | 0.5516 |      0.5333 |             0.0764 |                 0.7082 |             2.7903 |           1.8191 |          0.3803 |          0.8416 |    0.9956 |      -0.1009 |    0.2632 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 3150 |    0.7004 |  0.2504 | 0.0432 | 0.5633 |      0.5333 |             0.051  |                 0.6935 |             4.0315 |           2.8394 |          0.4286 |          0.7794 |    1      |      -0.1089 |    0.7982 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 3150 |    0.7113 |  0.2532 | 0.0505 | 0.5252 |      0.5333 |             0.0484 |                 0.6962 |            -0.4648 |          -1.1443 |          0.2876 |          0.846  |    0.048  |      -0.2781 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 3150 |    0.7174 |  0.2538 | 0.0533 | 0.5263 |      0.5333 |             0.0868 |                 0.7159 |             1.0129 |           0.3686 |          0.2527 |          0.7987 |    0.7022 |      -0.1161 |    0.0032 |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 3150 |    0.7243 |  0.2553 | 0.0565 | 0.5144 |      0.5333 |             0.0628 |                 0.7005 |             0.4758 |          -0.2254 |          0.2806 |          0.8756 |    0.3724 |      -0.1793 |    0.0002 |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 3150 |    0.7089 |  0.254  | 0.0408 | 0.5102 |      0.5333 |             0.0812 |                 0.7058 |            -0.1626 |          -0.5062 |          0.14   |          0.8238 |    0.2324 |      -0.249  |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 3150 |    0.7072 |  0.2542 | 0.0565 | 0.5096 |      0.5333 |             0.1026 |                 0.7235 |             0.874  |           0.0391 |          0.3346 |          0.9057 |    0.5225 |      -0.1177 |    0.0007 |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 3150 |    0.7092 |  0.2541 | 0.0566 | 0.5085 |      0.5333 |             0.0803 |                 0.7066 |             0.8475 |           0.3734 |          0.1829 |          0.8083 |    0.7044 |      -0.1427 |    0.0033 |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 3150 |    0.7218 |  0.2513 | 0.0457 | 0.5711 |      0.5333 |             0.0497 |                 0.6923 |             3.8679 |           2.8146 |          0.4343 |          0.9098 |    1      |      -0.048  |    0.7865 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 3150 |    0.697  |  0.2508 | 0.0381 | 0.5499 |      0.5333 |             0.0807 |                 0.7106 |             2.8389 |           1.7072 |          0.4267 |          0.8568 |    0.9924 |      -0.1222 |    0.2162 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 3150 |    0.7076 |  0.251  | 0.0476 | 0.5591 |      0.5333 |             0.0563 |                 0.6957 |             2.5278 |           1.679  |          0.3381 |          0.901  |    0.992  |      -0.1073 |    0.2028 |         21 |

## Hypothesis tests

| hypothesis   | model        | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:-------------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit        | rules_only - hitai_full (logloss)                            | -2.4572 |        0.993  |          -0.0317 | False          | nan      |       nan      |     0.993  |
| H3a          | logit        | rules_tech - hitai_full                                      | -1.0492 |        0.853  |          -0.0126 | False          | nan      |       nan      |     0.9693 |
| H3b          | logit        | hitai_full[shuffled] - hitai_full[pit]                       | -1.368  |        0.9143 |          -0.0166 | False          | nan      |       nan      |     0.9833 |
| H3c          | logit        | hitai_full[lagged] - hitai_full[pit]                         | -1.5891 |        0.944  |          -0.019  | False          | nan      |       nan      |     0.9833 |
| H2a          | logit        | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.8638 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H2b          | logit        | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0576 |        0.0932 |         nan      | False          | nan      |       nan      |     0.2149 |
| H4a          | logit        | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.8167 |        0.4141 |          -0.0061 | False          | nan      |       nan      |     0.5752 |
| H1           | gbt          | rules_only - hitai_full (logloss)                            | -0.7052 |        0.7597 |          -0.0046 | False          | nan      |       nan      |     0.9165 |
| H3a          | gbt          | rules_tech - hitai_full                                      |  0.6018 |        0.2737 |           0.0046 | False          | nan      |       nan      |     0.4025 |
| H3b          | gbt          | hitai_full[shuffled] - hitai_full[pit]                       |  1.5271 |        0.0634 |           0.015  | False          | nan      |       nan      |     0.176  |
| H3c          | gbt          | hitai_full[lagged] - hitai_full[pit]                         |  0.696  |        0.2432 |           0.0048 | False          | nan      |       nan      |     0.3816 |
| H2a          | gbt          | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.8145 |        0.0001 |         nan      | False          | nan      |       nan      |     0.0007 |
| H2b          | gbt          | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0513 |        0.1195 |         nan      | False          | nan      |       nan      |     0.2306 |
| H4a          | gbt          | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.1645 |        0.2442 |          -0.0054 | False          | nan      |       nan      |     0.3816 |
| H1           | gbt_mono     | rules_only - hitai_full (logloss)                            | -0.6662 |        0.7473 |          -0.0044 | True           |   0.7473 |         1      |     0.9165 |
| H3a          | gbt_mono     | rules_tech - hitai_full                                      |  2.4131 |        0.0079 |           0.0238 | True           |   0.0376 |         0.0395 |     0.0247 |
| H3b          | gbt_mono     | hitai_full[shuffled] - hitai_full[pit]                       |  2.4314 |        0.0075 |           0.0239 | True           |   0.0376 |         0.0376 |     0.0247 |
| H3c          | gbt_mono     | hitai_full[lagged] - hitai_full[pit]                         |  1.1754 |        0.1199 |           0.0088 | True           |   0.2837 |         0.5996 |     0.2306 |
| H2a          | gbt_mono     | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.9542 |        0.0031 |         nan      | False          | nan      |       nan      |     0.0131 |
| H2b          | gbt_mono     | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0572 |        0.0946 |         nan      | True           |   0.2837 |         0.4729 |     0.2149 |
| H4a          | gbt_mono     | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.2081 |        0.227  |           0.0072 | False          | nan      |       nan      |     0.3816 |
| H4b          | tagger       | corr(tag,fwd) original=0.1920 vs perturbed-context (want ~0) | -0.004  |        0.7699 |           0.1961 | False          | nan      |       nan      |     0.9165 |
| H4-demo      | leaky_tagger | corr(tag,fwd) unmasked                                       |  0.8658 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4-demo      | leaky_tagger | corr(tag,fwd) masked                                         |  0.1973 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4-demo      | leaky_tagger | corr(tag,fwd) perturbed                                      |  0.8658 |        0      |         nan      | False          | nan      |       nan      |     0      |

## Reality check / SPA vs rules_only: RC p=0.990, SPA p=1.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 1284 |    0.6942 |  0.2505 | 0.0232 | 0.4944 |      0.4899 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 1284 |    0.723  |  0.2541 | 0.0338 | 0.4931 |      0.4899 |          -2.8792 |    0.002  |
| hitai_full|pit|gbt_mono      | 1284 |    0.7105 |  0.2517 | 0.0241 | 0.5181 |      0.4899 |           1.557  |    0.9241 |
| hitai_full|shuffled|gbt_mono | 1284 |    0.7128 |  0.254  | 0.0342 | 0.489  |      0.4899 |          -1.4252 |    0.1021 |
