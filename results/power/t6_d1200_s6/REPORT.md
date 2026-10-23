# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 5244, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 3150 |    0.6999 |  0.2532 | 0.0361 | 0.4717 |      0.5206 |             0.0029 |                 0.6931 |             0.3291 |           0.1234 |          0.0743 |          0.7435 |    0.5706 |      -0.1699 |    0.0075 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 3150 |    0.6989 |  0.2528 | 0.0387 | 0.4811 |      0.5206 |             0.0012 |                 0.6927 |             0.1103 |          -0.0824 |          0.0724 |          0.8238 |    0.4527 |      -0.2241 |    0.0032 |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 3150 |    0.7003 |  0.2536 | 0.0449 | 0.4779 |      0.5206 |             0.0169 |                 0.6927 |             0.1689 |           0.054  |          0.0419 |          0.8    |    0.531  |      -0.1983 |    0.0057 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 3150 |    0.7317 |  0.2567 | 0.0371 | 0.4873 |      0.5206 |             0.0202 |                 0.6941 |             0.7111 |           0.3616 |          0.1324 |          0.7978 |    0.6994 |      -0.133  |    0.0183 |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 3150 |    0.7193 |  0.2554 | 0.0466 | 0.485  |      0.5206 |             0.0732 |                 0.715  |             0.8717 |           0.2225 |          0.2654 |          0.9552 |    0.6261 |      -0.1768 |    0.011  |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 3150 |    0.7178 |  0.2563 | 0.0486 | 0.4793 |      0.5206 |             0.045  |                 0.7016 |             0.8191 |          -0.0014 |          0.3403 |          0.9829 |    0.4992 |      -0.1997 |    0.0045 |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 3150 |    0.7116 |  0.2548 | 0.0394 | 0.4722 |      0.5206 |             0.0265 |                 0.6953 |             1.1215 |           0.8457 |          0.1108 |          0.8692 |    0.89   |      -0.0907 |    0.0814 |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 3150 |    0.7191 |  0.2553 | 0.0466 | 0.4859 |      0.5206 |             0.0723 |                 0.7149 |             0.934  |           0.2931 |          0.2629 |          0.9565 |    0.6641 |      -0.1614 |    0.0143 |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 3150 |    0.7178 |  0.2563 | 0.0486 | 0.4793 |      0.5206 |             0.045  |                 0.7016 |             0.8191 |          -0.0014 |          0.3403 |          0.9829 |    0.4992 |      -0.1997 |    0.0045 |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 3150 |    0.6918 |  0.2479 | 0.0212 | 0.5623 |      0.5206 |             0.0177 |                 0.6829 |             3.6093 |           2.4437 |          0.4432 |          0.86   |    0.9998 |      -0.0643 |    0.8195 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 3150 |    0.7188 |  0.2547 | 0.0415 | 0.5201 |      0.5206 |             0.0604 |                 0.7018 |             2.6461 |           1.7253 |          0.359  |          0.9206 |    0.9938 |      -0.0683 |    0.4524 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 3150 |    0.7167 |  0.2522 | 0.0283 | 0.5341 |      0.5206 |             0.0381 |                 0.6917 |             3.2565 |           2.1378 |          0.4387 |          0.9029 |    0.999  |      -0.0554 |    0.6828 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 3150 |    0.7011 |  0.2532 | 0.0574 | 0.487  |      0.5206 |             0.0365 |                 0.696  |             0.2618 |          -0.5396 |          0.3238 |          0.8149 |    0.219  |      -0.2321 |    0.0004 |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 3150 |    0.7135 |  0.2546 | 0.0407 | 0.4829 |      0.5206 |             0.0717 |                 0.715  |             0.5581 |          -0.1448 |          0.2892 |          0.9441 |    0.4174 |      -0.2245 |    0.0025 |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 3150 |    0.7177 |  0.2556 | 0.041  | 0.4844 |      0.5206 |             0.0382 |                 0.701  |             0.7371 |          -0.1224 |          0.3568 |          0.9841 |    0.43   |      -0.231  |    0.0027 |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 3150 |    0.7144 |  0.254  | 0.0442 | 0.5064 |      0.5206 |             0.024  |                 0.6953 |             0.7225 |           0.0024 |          0.2705 |          0.7746 |    0.5014 |      -0.1475 |    0.0046 |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 3150 |    0.7082 |  0.2543 | 0.0474 | 0.4845 |      0.5206 |             0.0807 |                 0.715  |             1.1254 |           0.5389 |          0.2457 |          0.9803 |    0.7824 |      -0.1454 |    0.0331 |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 3150 |    0.7136 |  0.2542 | 0.0384 | 0.4934 |      0.5206 |             0.042  |                 0.7006 |             1.1386 |           0.4958 |          0.2648 |          0.9432 |    0.7635 |      -0.1465 |    0.0288 |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 3150 |    0.6972 |  0.249  | 0.0234 | 0.5527 |      0.5206 |             0.0203 |                 0.6858 |             3.7313 |           2.6208 |          0.454  |          0.9698 |    0.9999 |      -0.0709 |    0.8704 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 3150 |    0.7317 |  0.257  | 0.043  | 0.5107 |      0.5206 |             0.062  |                 0.7045 |             1.5237 |           0.4765 |          0.3692 |          0.7089 |    0.7536 |      -0.1425 |    0.0277 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 3150 |    0.704  |  0.252  | 0.0366 | 0.5273 |      0.5206 |             0.0435 |                 0.6927 |             3.1424 |           1.9326 |          0.4863 |          0.9279 |    0.997  |      -0.0667 |    0.5704 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  1.7277 |        0.042  |           0.008  | False          |      nan |            nan |     0.1321 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.5307 |        0.0057 |           0.0198 | False          |      nan |            nan |     0.025  |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  1.9755 |        0.0241 |           0.0092 | False          |      nan |            nan |     0.0884 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.8528 |        0.0022 |           0.0225 | False          |      nan |            nan |     0.0159 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.9406 |        0.0033 |         nan      | False          |      nan |            nan |     0.018  |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0252 |        0.2816 |         nan      | False          |      nan |            nan |     0.5163 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.1457 |        0.2519 |           0.0054 | False          |      nan |            nan |     0.5038 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -1.8302 |        0.9664 |          -0.0199 | False          |      nan |            nan |     0.9664 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  0.0279 |        0.4889 |           0.0003 | False          |      nan |            nan |     0.717  |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       | -0.5867 |        0.7213 |          -0.0054 | False          |      nan |            nan |     0.88   |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         | -1.0131 |        0.8445 |          -0.0106 | False          |      nan |            nan |     0.929  |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.7329 |        0      |         nan      | False          |      nan |            nan |     0      |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               | -0.014  |        0.6256 |         nan      | False          |      nan |            nan |     0.8096 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.1975 |        0.2311 |           0.0128 | False          |      nan |            nan |     0.5038 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -1.3052 |        0.9041 |          -0.0164 | True           |        1 |              1 |     0.9471 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  0.0885 |        0.4647 |           0.0011 | True           |        1 |              1 |     0.717  |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  0.0822 |        0.4672 |           0.001  | True           |        1 |              1 |     0.717  |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         | -0.2992 |        0.6176 |          -0.0031 | True           |        1 |              1 |     0.8096 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.6089 |        0      |         nan      | False          |      nan |            nan |     0      |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               | -0.0308 |        0.76   |         nan      | True           |        1 |              1 |     0.88   |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.1892 |        0.2344 |          -0.0127 | False          |      nan |            nan |     0.5038 |
| H4b          | tagger   | corr(tag,fwd) original=0.1788 vs perturbed-context (want ~0) |  0.0205 |        0.1373 |           0.1583 | False          |      nan |            nan |     0.3777 |

## Reality check / SPA vs rules_only: RC p=0.740, SPA p=0.227

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 1284 |    0.6992 |  0.2529 | 0.0555 | 0.4964 |      0.4556 |          -3.6278 |    0      |
| rules_tech|pit|gbt_mono      | 1284 |    0.7358 |  0.2555 | 0.0753 | 0.5039 |      0.4556 |          -2.2995 |    0.0188 |
| hitai_full|pit|gbt_mono      | 1284 |    0.7215 |  0.2542 | 0.0715 | 0.5593 |      0.4556 |           1.0977 |    0.844  |
| hitai_full|shuffled|gbt_mono | 1284 |    0.7213 |  0.2553 | 0.0702 | 0.4922 |      0.4556 |          -3.0565 |    0.0021 |
