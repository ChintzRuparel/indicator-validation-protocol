# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 20976, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 12600 |    0.6974 |  0.251  | 0.013  | 0.4962 |       0.511 |             0.002  |                 0.6931 |            -0.098  |          -0.5415 |          0.0758 |          0.6094 |    0.2174 |      -0.0875 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 12600 |    0.696  |  0.2514 | 0.0126 | 0.4903 |       0.511 |             0.0082 |                 0.6941 |            -0.3847 |          -0.8755 |          0.0693 |          0.4051 |    0.1031 |      -0.0916 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 12600 |    0.6959 |  0.2512 | 0.014  | 0.4911 |       0.511 |             0.0089 |                 0.6943 |            -0.6068 |          -1.1771 |          0.0902 |          0.5347 |    0.0443 |      -0.1144 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 12600 |    0.6987 |  0.2523 | 0.0189 | 0.4933 |       0.511 |             0.0139 |                 0.6958 |            -0.2361 |          -0.9743 |          0.1288 |          0.6052 |    0.0805 |      -0.1227 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 12600 |    0.7175 |  0.2539 | 0.0286 | 0.49   |       0.511 |             0.0467 |                 0.7022 |            -0.7282 |          -1.4603 |          0.1298 |          0.6584 |    0.0178 |      -0.154  |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 12600 |    0.7077 |  0.2535 | 0.0262 | 0.4955 |       0.511 |             0.0275 |                 0.6969 |            -0.103  |          -0.9446 |          0.1519 |          0.676  |    0.0871 |      -0.1421 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 12600 |    0.6996 |  0.2523 | 0.0199 | 0.4841 |       0.511 |             0.0271 |                 0.6979 |            -0.5905 |          -1.1343 |          0.0872 |          0.5136 |    0.0509 |      -0.1251 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 12600 |    0.7158 |  0.2537 | 0.0273 | 0.4908 |       0.511 |             0.0466 |                 0.7021 |            -0.6238 |          -1.3386 |          0.1277 |          0.6688 |    0.0268 |      -0.1438 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 12600 |    0.7072 |  0.2534 | 0.0262 | 0.4946 |       0.511 |             0.0285 |                 0.6969 |            -0.1365 |          -0.9811 |          0.1503 |          0.659  |    0.0793 |      -0.1445 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 12600 |    0.6923 |  0.2483 | 0.0279 | 0.5744 |       0.511 |             0.0126 |                 0.6842 |             9.3812 |           6.6488 |          0.5467 |          0.8847 |    1      |      -0.0169 |    0.6827 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 12600 |    0.6951 |  0.2478 | 0.0228 | 0.5673 |       0.511 |             0.0156 |                 0.6871 |             7.2696 |           4.5029 |          0.539  |          0.8879 |    1      |      -0.0228 |    0.0052 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 12600 |    0.6927 |  0.2467 | 0.0228 | 0.5806 |       0.511 |             0.007  |                 0.6826 |             8.5311 |           5.9029 |          0.5306 |          0.8907 |    1      |      -0.0197 |    0.2841 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 12600 |    0.7015 |  0.252  | 0.0161 | 0.4941 |       0.511 |             0.026  |                 0.6981 |            -0.139  |          -1.3521 |          0.1943 |          0.5228 |    0.0261 |      -0.1409 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 12600 |    0.7162 |  0.2535 | 0.0233 | 0.4919 |       0.511 |             0.0426 |                 0.7014 |            -0.954  |          -1.8793 |          0.1529 |          0.612  |    0.0034 |      -0.1854 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 12600 |    0.7113 |  0.2532 | 0.0252 | 0.4977 |       0.511 |             0.0275 |                 0.6966 |             0.0023 |          -1.1864 |          0.1908 |          0.5297 |    0.0444 |      -0.1378 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 12600 |    0.7019 |  0.2527 | 0.0179 | 0.4881 |       0.511 |             0.0269 |                 0.6982 |            -0.8053 |          -1.5283 |          0.1126 |          0.5078 |    0.0134 |      -0.1605 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 12600 |    0.7187 |  0.2538 | 0.0284 | 0.4922 |       0.511 |             0.0483 |                 0.7025 |            -0.784  |          -1.5754 |          0.1454 |          0.7316 |    0.0118 |      -0.1809 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 12600 |    0.7163 |  0.2539 | 0.022  | 0.4967 |       0.511 |             0.026  |                 0.6969 |             0.0215 |          -0.7956 |          0.1448 |          0.6624 |    0.1261 |      -0.1226 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 12600 |    0.7029 |  0.2477 | 0.0194 | 0.5755 |       0.511 |             0.0171 |                 0.6838 |             9.0905 |           6.3994 |          0.5348 |          0.9236 |    1      |      -0.0215 |    0.5474 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 12600 |    0.6947 |  0.2478 | 0.0195 | 0.5686 |       0.511 |             0.0144 |                 0.6862 |             7.7126 |           5.0515 |          0.5613 |          0.9279 |    1      |      -0.0253 |    0.0388 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 12600 |    0.6932 |  0.2468 | 0.0299 | 0.5807 |       0.511 |             0.0138 |                 0.6824 |             9.1624 |           6.4347 |          0.5245 |          0.8136 |    1      |      -0.0269 |    0.5648 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  1.6033 |        0.0544 |           0.0051 | False          | nan      |       nan      |     0.0748 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.6403 |        0.0041 |           0.0072 | False          | nan      |       nan      |     0.0083 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  3.4926 |        0.0002 |           0.0092 | False          | nan      |       nan      |     0.0007 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.8477 |        0.0022 |           0.0095 | False          | nan      |       nan      |     0.005  |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.901  |        0.0001 |         nan      | False          | nan      |       nan      |     0.0004 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0067 |        0.38   |         nan      | False          | nan      |       nan      |     0.44   |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  2.8209 |        0.0048 |           0.0106 | False          | nan      |       nan      |     0.0088 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  0.3098 |        0.3784 |           0.0009 | False          | nan      |       nan      |     0.44   |
| H3a          | gbt      | rules_tech - hitai_full                                      |  3.852  |        0.0001 |           0.0208 | False          | nan      |       nan      |     0.0003 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  3.6209 |        0.0001 |           0.0211 | False          | nan      |       nan      |     0.0005 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  3.915  |        0      |           0.0237 | False          | nan      |       nan      |     0.0003 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.2319 |        0.0256 |         nan      | False          | nan      |       nan      |     0.0403 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0617 |        0.0023 |         nan      | False          | nan      |       nan      |     0.005  |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.1563 |        0.8758 |          -0.0003 | False          | nan      |       nan      |     0.8758 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  0.9249 |        0.1775 |           0.0032 | True           |   0.1775 |         0.8875 |     0.2297 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  3.6759 |        0.0001 |           0.0145 | True           |   0.0004 |         0.0006 |     0.0004 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  4.3797 |        0      |           0.0186 | True           |   0      |         0      |     0.0001 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  4.7686 |        0      |           0.0236 | True           |   0      |         0      |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.7737 |        0.0055 |         nan      | False          | nan      |       nan      |     0.0094 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.04   |        0.0332 |         nan      | True           |   0.0663 |         0.1658 |     0.0486 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.266  |        0.7903 |           0.0006 | False          | nan      |       nan      |     0.8693 |
| H4b          | tagger   | corr(tag,fwd) original=0.1779 vs perturbed-context (want ~0) |  0.0011 |        0.8695 |           0.1768 | False          | nan      |       nan      |     0.8758 |

## Reality check / SPA vs rules_only: RC p=0.527, SPA p=0.500

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5136 |    0.6929 |  0.2499 | 0.0033 | 0.508  |      0.4977 |          -0.2658 |    0.4035 |
| rules_tech|pit|gbt_mono      | 5136 |    0.693  |  0.2499 | 0.0033 | 0.5069 |      0.4977 |          -1.1785 |    0.1384 |
| hitai_full|pit|gbt_mono      | 5136 |    0.6874 |  0.2467 | 0.0113 | 0.5752 |      0.4977 |           8.7261 |    1      |
| hitai_full|shuffled|gbt_mono | 5136 |    0.6932 |  0.25   | 0.0056 | 0.5037 |      0.4977 |          -1.4573 |    0.09   |
