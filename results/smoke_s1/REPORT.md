# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 5244, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 3150 |    0.713  |  0.2593 | 0.0784 | 0.4565 |      0.4829 |             0.0025 |                 0.693  |            -0.1716 |          -0.4502 |          0.1244 |          0.9263 |    0.2583 |      -0.2036 |    0.0016 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 3150 |    0.7195 |  0.2608 | 0.0885 | 0.4622 |      0.4829 |             0.003  |                 0.6924 |            -0.7441 |          -0.9364 |          0.0759 |          0.7851 |    0.0901 |      -0.2192 |    0.0001 |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 3150 |    0.7065 |  0.2566 | 0.0719 | 0.4514 |      0.4829 |             0.0011 |                 0.6922 |            -0.0888 |          -0.1206 |          0.0133 |          0.8    |    0.431  |      -0.2033 |    0.0066 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 3150 |    0.7176 |  0.2586 | 0.0806 | 0.4546 |      0.4829 |             0.0472 |                 0.6982 |            -0.9929 |          -1.1829 |          0.0705 |          0.6232 |    0.0466 |      -0.2448 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 3150 |    0.7409 |  0.2632 | 0.0875 | 0.4678 |      0.4829 |             0.0724 |                 0.7083 |            -0.2953 |          -1.1091 |          0.2908 |          0.6708 |    0.0575 |      -0.2742 |    0.0001 |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 3150 |    0.748  |  0.2611 | 0.1025 | 0.4664 |      0.4829 |             0.0296 |                 0.6953 |            -0.3914 |          -1.1162 |          0.2924 |          0.7952 |    0.0561 |      -0.2757 |    0.0001 |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 3150 |    0.7404 |  0.2606 | 0.0786 | 0.4526 |      0.4829 |             0.0568 |                 0.6994 |            -1.1844 |          -1.4694 |          0.1124 |          0.733  |    0.0183 |      -0.3272 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 3150 |    0.7411 |  0.2632 | 0.087  | 0.4673 |      0.4829 |             0.0737 |                 0.7085 |            -0.2667 |          -1.0673 |          0.2832 |          0.6581 |    0.0647 |      -0.2627 |    0.0001 |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 3150 |    0.748  |  0.2611 | 0.1025 | 0.4664 |      0.4829 |             0.0296 |                 0.6953 |            -0.3914 |          -1.1162 |          0.2924 |          0.7952 |    0.0561 |      -0.2757 |    0.0001 |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 3150 |    0.7203 |  0.2595 | 0.0814 | 0.5163 |      0.4829 |             0.0258 |                 0.688  |             2.2893 |           1.3    |          0.4187 |          0.9159 |    0.9709 |      -0.1179 |    0.3319 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 3150 |    0.7334 |  0.2605 | 0.065  | 0.495  |      0.4829 |             0.0488 |                 0.6955 |             0.5533 |          -0.3685 |          0.3692 |          0.7549 |    0.2987 |      -0.1989 |    0.0024 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 3150 |    0.7314 |  0.2582 | 0.0737 | 0.513  |      0.4829 |             0.0298 |                 0.6854 |             0.8474 |          -0.1019 |          0.4121 |          0.9073 |    0.4417 |      -0.1373 |    0.0072 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 3150 |    0.7305 |  0.2593 | 0.0755 | 0.4551 |      0.4829 |             0.0392 |                 0.6993 |            -1.0919 |          -1.3253 |          0.0914 |          0.7537 |    0.029  |      -0.2867 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 3150 |    0.7226 |  0.2617 | 0.0784 | 0.4685 |      0.4829 |             0.0707 |                 0.7075 |            -0.5653 |          -1.3331 |          0.2603 |          0.5917 |    0.03   |      -0.2938 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 3150 |    0.7261 |  0.2604 | 0.0675 | 0.4615 |      0.4829 |             0.0274 |                 0.6944 |            -0.5021 |          -1.1128 |          0.2333 |          0.6873 |    0.0568 |      -0.2504 |    0.0001 |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 3150 |    0.7112 |  0.2575 | 0.0723 | 0.4519 |      0.4829 |             0.0444 |                 0.7016 |            -0.6985 |          -0.7783 |          0.0286 |          0.594  |    0.1327 |      -0.2006 |    0.0003 |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 3150 |    0.7115 |  0.2582 | 0.0811 | 0.4773 |      0.4829 |             0.0716 |                 0.7091 |            -0.3605 |          -1.2115 |          0.3635 |          0.9022 |    0.0416 |      -0.321  |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 3150 |    0.7193 |  0.26   | 0.0978 | 0.4574 |      0.4829 |             0.0381 |                 0.6981 |            -0.8755 |          -1.3817 |          0.213  |          0.8444 |    0.0232 |      -0.3349 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 3150 |    0.7447 |  0.2606 | 0.0799 | 0.5224 |      0.4829 |             0.032  |                 0.6867 |             1.9223 |           0.9487 |          0.4241 |          0.9495 |    0.9156 |      -0.1339 |    0.1731 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 3150 |    0.7374 |  0.261  | 0.0801 | 0.5028 |      0.4829 |             0.0479 |                 0.6963 |             1.6811 |           0.6326 |          0.3981 |          0.686  |    0.8208 |      -0.1251 |    0.0805 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 3150 |    0.7185 |  0.2564 | 0.0729 | 0.5085 |      0.4829 |             0.021  |                 0.6853 |             1.5033 |           0.4902 |          0.3651 |          0.6479 |    0.7613 |      -0.1171 |    0.0541 |         21 |

## Hypothesis tests

| hypothesis   | model        | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:-------------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit        | rules_only - hitai_full (logloss)                            | -1.0532 |        0.8539 |          -0.0074 | False          | nan      |       nan      |     0.999  |
| H3a          | logit        | rules_tech - hitai_full                                      |  1.5242 |        0.0637 |           0.02   | False          | nan      |       nan      |     0.1991 |
| H3b          | logit        | hitai_full[shuffled] - hitai_full[pit]                       |  0.8607 |        0.1947 |           0.0101 | False          | nan      |       nan      |     0.3744 |
| H3c          | logit        | hitai_full[lagged] - hitai_full[pit]                         | -1.2711 |        0.8982 |          -0.0091 | False          | nan      |       nan      |     0.999  |
| H2a          | logit        | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  5.5764 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H2b          | logit        | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0566 |        0.0969 |         nan      | False          | nan      |       nan      |     0.2691 |
| H4a          | logit        | masked - unmasked logloss (two-sided; want NOT rejected)     |  2.0989 |        0.0358 |           0.0243 | False          | nan      |       nan      |     0.128  |
| H1           | gbt          | rules_only - hitai_full (logloss)                            | -1.6885 |        0.9543 |          -0.0138 | False          | nan      |       nan      |     0.999  |
| H3a          | gbt          | rules_tech - hitai_full                                      |  0.7125 |        0.2381 |           0.0077 | False          | nan      |       nan      |     0.4252 |
| H3b          | gbt          | hitai_full[shuffled] - hitai_full[pit]                       | -1.4435 |        0.9256 |          -0.0107 | False          | nan      |       nan      |     0.999  |
| H3c          | gbt          | hitai_full[lagged] - hitai_full[pit]                         | -3.0761 |        0.999  |          -0.0218 | False          | nan      |       nan      |     0.999  |
| H2a          | gbt          | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  7.0026 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H2b          | gbt          | Spearman(|p-.5|, hit) on non-overlapping dates               | -0.0698 |        0.9453 |         nan      | False          | nan      |       nan      |     0.999  |
| H4a          | gbt          | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.6359 |        0.5248 |           0.0041 | False          | nan      |       nan      |     0.82   |
| H1           | gbt_mono     | rules_only - hitai_full (logloss)                            | -2.854  |        0.9978 |          -0.0249 | True           |   1      |         1      |     0.999  |
| H3a          | gbt_mono     | rules_tech - hitai_full                                      |  1.1163 |        0.1321 |           0.0166 | True           |   0.6182 |         0.6607 |     0.2767 |
| H3b          | gbt_mono     | hitai_full[shuffled] - hitai_full[pit]                       | -0.475  |        0.6826 |          -0.0053 | True           |   1      |         1      |     0.999  |
| H3c          | gbt_mono     | hitai_full[lagged] - hitai_full[pit]                         | -1.3236 |        0.9072 |          -0.0121 | True           |   1      |         1      |     0.999  |
| H2a          | gbt_mono     | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  5.6994 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H2b          | gbt_mono     | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0504 |        0.1236 |         nan      | True           |   0.6182 |         0.6182 |     0.2767 |
| H4a          | gbt_mono     | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.5032 |        0.1328 |          -0.0129 | False          | nan      |       nan      |     0.2767 |
| H4b          | tagger       | corr(tag,fwd) original=0.1496 vs perturbed-context (want ~0) | -0.011  |        0.4278 |           0.1605 | False          | nan      |       nan      |     0.7129 |
| H4-demo      | leaky_tagger | corr(tag,fwd) unmasked                                       |  0.8652 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4-demo      | leaky_tagger | corr(tag,fwd) masked                                         |  0.1538 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4-demo      | leaky_tagger | corr(tag,fwd) perturbed                                      |  0.8652 |        0      |         nan      | False          | nan      |       nan      |     0      |

## Reality check / SPA vs rules_only: RC p=1.000, SPA p=1.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 1284 |    0.6972 |  0.252  | 0.0504 | 0.5018 |      0.4798 |          -0.5767 |    0.2966 |
| rules_tech|pit|gbt_mono      | 1284 |    0.6992 |  0.253  | 0.0558 | 0.5067 |      0.4798 |          -0.3158 |    0.3853 |
| hitai_full|pit|gbt_mono      | 1284 |    0.7018 |  0.2508 | 0.0649 | 0.5666 |      0.4798 |          -0.0603 |    0.4779 |
| hitai_full|shuffled|gbt_mono | 1284 |    0.698  |  0.2524 | 0.0541 | 0.4974 |      0.4798 |          -0.5897 |    0.2922 |
