# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 10488, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6300 |    0.6948 |  0.2508 | 0.0097 | 0.4936 |       0.484 |             0.0156 |                 0.694  |             0.2053 |          -0.088  |          0.0565 |          0.4232 |    0.4495 |      -0.1017 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6300 |    0.6956 |  0.2512 | 0.0233 | 0.4999 |       0.484 |             0.0128 |                 0.6939 |            -0.1626 |          -0.8183 |          0.1206 |          0.2995 |    0.1058 |      -0.0865 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6300 |    0.6934 |  0.2501 | 0.0042 | 0.505  |       0.484 |             0.0099 |                 0.6931 |             1.0167 |           0.6939 |          0.0824 |          0.6233 |    0.8437 |      -0.0907 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6300 |    0.6957 |  0.2509 | 0.0046 | 0.5016 |       0.484 |             0.0353 |                 0.6959 |             0.8608 |           0.2803 |          0.1454 |          0.653  |    0.6575 |      -0.1363 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6300 |    0.7074 |  0.2522 | 0.0138 | 0.4976 |       0.484 |             0.0669 |                 0.7089 |             0.4081 |          -0.0211 |          0.1079 |          0.5846 |    0.4879 |      -0.1723 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6300 |    0.7041 |  0.2525 | 0.0171 | 0.4921 |       0.484 |             0.0397 |                 0.6977 |             0.0204 |          -1.0281 |          0.2841 |          0.6714 |    0.071  |      -0.251  |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6300 |    0.7028 |  0.2511 | 0.0051 | 0.4961 |       0.484 |             0.0336 |                 0.6976 |             0.7695 |           0.4513 |          0.0829 |          0.6906 |    0.7432 |      -0.1224 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6300 |    0.7028 |  0.252  | 0.0149 | 0.4917 |       0.484 |             0.0702 |                 0.7087 |             0.3407 |          -0.2561 |          0.1586 |          0.6525 |    0.3565 |      -0.2016 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6300 |    0.7041 |  0.2525 | 0.0171 | 0.4921 |       0.484 |             0.0397 |                 0.6977 |             0.0204 |          -1.0281 |          0.2841 |          0.6714 |    0.071  |      -0.251  |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6300 |    0.6925 |  0.2466 | 0.0187 | 0.5712 |       0.484 |             0.0188 |                 0.6857 |             6.479  |           4.6652 |          0.5797 |          0.9717 |    1      |      -0.045  |    0.9005 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6300 |    0.6951 |  0.2486 | 0.0236 | 0.5608 |       0.484 |             0.0385 |                 0.6956 |             4.2716 |           2.3614 |          0.5471 |          0.7741 |    0.9994 |      -0.0737 |    0.0264 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6300 |    0.6935 |  0.2471 | 0.0228 | 0.5726 |       0.484 |             0.0189 |                 0.6856 |             6.1077 |           4.1164 |          0.5684 |          0.8537 |    1      |      -0.0358 |    0.6848 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6300 |    0.7022 |  0.2509 | 0.005  | 0.4954 |       0.484 |             0.0389 |                 0.6983 |             0.6176 |           0.4775 |          0.0349 |          0.6011 |    0.7555 |      -0.1309 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6300 |    0.7102 |  0.2519 | 0.0102 | 0.5001 |       0.484 |             0.0664 |                 0.7085 |             0.4312 |          -0.1279 |          0.1402 |          0.6041 |    0.427  |      -0.1704 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6300 |    0.7056 |  0.2533 | 0.0185 | 0.4924 |       0.484 |             0.0408 |                 0.6976 |            -0.1759 |          -1.1974 |          0.2746 |          0.7043 |    0.0446 |      -0.2615 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6300 |    0.6948 |  0.2503 | 0.0045 | 0.496  |       0.484 |             0.0423 |                 0.7002 |             0.571  |           0.2809 |          0.0759 |          0.6211 |    0.6578 |      -0.1344 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6300 |    0.7071 |  0.2529 | 0.02   | 0.4951 |       0.484 |             0.0653 |                 0.7087 |             0.1367 |          -0.5634 |          0.177  |          0.6302 |    0.2095 |      -0.2219 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6300 |    0.7055 |  0.2525 | 0.032  | 0.4941 |       0.484 |             0.0443 |                 0.6985 |            -0.0854 |          -1.1333 |          0.3048 |          0.7352 |    0.0488 |      -0.3191 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6300 |    0.6885 |  0.2459 | 0.0172 | 0.5793 |       0.484 |             0.0244 |                 0.6846 |             6.3901 |           4.5922 |          0.5213 |          0.8249 |    1      |      -0.0412 |    0.8831 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6300 |    0.6981 |  0.2491 | 0.0135 | 0.5566 |       0.484 |             0.0416 |                 0.6958 |             3.8866 |           2.2424 |          0.4968 |          0.7325 |    0.999  |      -0.0786 |    0.0169 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6300 |    0.6909 |  0.2468 | 0.0182 | 0.5728 |       0.484 |             0.0206 |                 0.6851 |             5.7908 |           3.849  |          0.5584 |          0.8594 |    1      |      -0.0267 |    0.5421 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  0.5439 |        0.2932 |           0.0024 | False          | nan      |       nan      |     0.3659 |
| H3a          | logit    | rules_tech - hitai_full                                      |  1.951  |        0.0255 |           0.0103 | False          | nan      |       nan      |     0.0624 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  1.6892 |        0.0456 |           0.0097 | False          | nan      |       nan      |     0.0848 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  0.5261 |        0.2994 |           0.0023 | False          | nan      |       nan      |     0.3659 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.9125 |        0.0036 |         nan      | False          | nan      |       nan      |     0.0491 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0568 |        0.0324 |         nan      | False          | nan      |       nan      |     0.0714 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.3025 |        0.1928 |          -0.004  | False          | nan      |       nan      |     0.2827 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  0.1533 |        0.4391 |           0.0006 | False          | nan      |       nan      |     0.483  |
| H3a          | gbt      | rules_tech - hitai_full                                      |  1.6068 |        0.054  |           0.0078 | False          | nan      |       nan      |     0.0915 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  2.4063 |        0.0081 |           0.0152 | False          | nan      |       nan      |     0.0491 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  2.009  |        0.0223 |           0.0121 | False          | nan      |       nan      |     0.0624 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.5378 |        0.0112 |         nan      | False          | nan      |       nan      |     0.0491 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.017  |        0.2905 |         nan      | False          | nan      |       nan      |     0.3659 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.9369 |        0.3488 |           0.0031 | False          | nan      |       nan      |     0.4039 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -0.015  |        0.506  |          -0.0001 | True           |   0.506  |         1      |     0.506  |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  2.0045 |        0.0225 |           0.0107 | True           |   0.0675 |         0.1126 |     0.0624 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  2.4389 |        0.0074 |           0.0121 | True           |   0.0368 |         0.0368 |     0.0491 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  2.2885 |        0.0111 |           0.012  | True           |   0.0442 |         0.0553 |     0.0491 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.251  |        0.0244 |         nan      | False          | nan      |       nan      |     0.0624 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0431 |        0.081  |         nan      | True           |   0.162  |         0.405  |     0.1273 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.6811 |        0.4958 |          -0.0025 | False          | nan      |       nan      |     0.506  |
| H4b          | tagger   | corr(tag,fwd) original=0.1797 vs perturbed-context (want ~0) |  0.0195 |        0.0463 |           0.1602 | False          | nan      |       nan      |     0.0848 |

## Reality check / SPA vs rules_only: RC p=0.933, SPA p=0.927

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2568 |    0.6936 |  0.2502 | 0.0188 | 0.5009 |      0.4961 |          -1.7151 |    0.0551 |
| rules_tech|pit|gbt_mono      | 2568 |    0.6934 |  0.2502 | 0.0202 | 0.5043 |      0.4961 |          -0.7855 |    0.2339 |
| hitai_full|pit|gbt_mono      | 2568 |    0.6865 |  0.2455 | 0.0254 | 0.5914 |      0.4961 |           5.7678 |    1      |
| hitai_full|shuffled|gbt_mono | 2568 |    0.6936 |  0.2503 | 0.0203 | 0.5033 |      0.4961 |          -0.6366 |    0.2782 |
