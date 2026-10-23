# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 5244, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 3150 |    0.7075 |  0.2514 | 0.018  | 0.5321 |      0.5102 |             0.0176 |                 0.6938 |             1.2279 |           1.0725 |          0.0508 |          0.606  |    0.9399 |      -0.1006 |    0.0949 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 3150 |    0.6929 |  0.2498 | 0.0218 | 0.5227 |      0.5102 |             0.0237 |                 0.6923 |             1.1562 |           0.983  |          0.0546 |          0.6    |    0.9212 |      -0.0891 |    0.0764 |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 3150 |    0.6937 |  0.2503 | 0.0241 | 0.5073 |      0.5102 |             0.0091 |                 0.6928 |             0.2055 |           0.1077 |          0.0251 |          0.4102 |    0.5616 |      -0.1545 |    0.0035 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 3150 |    0.761  |  0.2576 | 0.0451 | 0.542  |      0.5102 |             0.0193 |                 0.6944 |             1.8058 |           1.0593 |          0.2537 |          0.5625 |    0.9347 |      -0.0987 |    0.095  |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 3150 |    0.7398 |  0.26   | 0.0662 | 0.4942 |      0.5102 |             0.0751 |                 0.7131 |             0.2531 |          -0.6715 |          0.3403 |          0.6784 |    0.1657 |      -0.2557 |    0.0001 |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 3150 |    0.7336 |  0.2594 | 0.0643 | 0.5002 |      0.5102 |             0.0519 |                 0.7038 |             0.2177 |          -0.8714 |          0.4076 |          0.7273 |    0.104  |      -0.2738 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 3150 |    0.7452 |  0.2567 | 0.0422 | 0.5377 |      0.5102 |             0.0208 |                 0.6953 |             1.5573 |           0.842  |          0.2603 |          0.6349 |    0.8853 |      -0.0806 |    0.0525 |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 3150 |    0.7442 |  0.2601 | 0.0637 | 0.4958 |      0.5102 |             0.0727 |                 0.713  |             0.2766 |          -0.6532 |          0.3365 |          0.6527 |    0.1726 |      -0.2502 |    0.0001 |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 3150 |    0.7336 |  0.2594 | 0.0643 | 0.5002 |      0.5102 |             0.0519 |                 0.7038 |             0.2177 |          -0.8714 |          0.4076 |          0.7273 |    0.104  |      -0.2738 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 3150 |    0.7144 |  0.2533 | 0.0377 | 0.5524 |      0.5102 |             0.0262 |                 0.6883 |             3.4076 |           2.3259 |          0.4063 |          0.7527 |    0.9995 |      -0.0487 |    0.6901 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 3150 |    0.7317 |  0.2582 | 0.0472 | 0.5303 |      0.5102 |             0.0615 |                 0.7043 |             2.0241 |           1.0297 |          0.3673 |          0.6822 |    0.9302 |      -0.1292 |    0.087  |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 3150 |    0.7572 |  0.2579 | 0.0532 | 0.5383 |      0.5102 |             0.0426 |                 0.6947 |             2.7474 |           1.6085 |          0.447  |          0.8502 |    0.9896 |      -0.0682 |    0.298  |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 3150 |    0.7307 |  0.2552 | 0.0345 | 0.5371 |      0.5102 |             0.0299 |                 0.6961 |             0.9662 |           0.1111 |          0.3098 |          0.6162 |    0.5636 |      -0.1297 |    0.0036 |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 3150 |    0.7388 |  0.261  | 0.0668 | 0.5    |      0.5102 |             0.0776 |                 0.7124 |             0.6805 |          -0.332  |          0.3721 |          0.6714 |    0.3154 |      -0.2738 |    0.0004 |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 3150 |    0.7323 |  0.2593 | 0.0618 | 0.4983 |      0.5102 |             0.0525 |                 0.7038 |             0.6696 |          -0.3983 |          0.4667 |          0.9    |    0.283  |      -0.2601 |    0.0003 |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 3150 |    0.7482 |  0.2572 | 0.0279 | 0.5416 |      0.5102 |             0.0236 |                 0.6958 |             1.8837 |           1.0587 |          0.2851 |          0.6022 |    0.9359 |      -0.0807 |    0.0933 |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 3150 |    0.7382 |  0.2599 | 0.0585 | 0.4994 |      0.5102 |             0.0714 |                 0.7125 |             0.1372 |          -0.8322 |          0.3203 |          0.5787 |    0.1131 |      -0.3134 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 3150 |    0.7304 |  0.2592 | 0.0656 | 0.5029 |      0.5102 |             0.0514 |                 0.7033 |             0.1918 |          -0.8326 |          0.3981 |          0.7867 |    0.1146 |      -0.2606 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 3150 |    0.713  |  0.2517 | 0.0372 | 0.5551 |      0.5102 |             0.0241 |                 0.6896 |             3.2856 |           2.2329 |          0.4    |          0.7479 |    0.9993 |      -0.0588 |    0.6421 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 3150 |    0.7298 |  0.2571 | 0.0444 | 0.5363 |      0.5102 |             0.0654 |                 0.7039 |             1.4445 |           0.3832 |          0.3943 |          0.7422 |    0.7091 |      -0.1624 |    0.0109 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 3150 |    0.744  |  0.2566 | 0.0509 | 0.5445 |      0.5102 |             0.0467 |                 0.6952 |             2.2076 |           1.1196 |          0.4556 |          0.9035 |    0.9465 |      -0.1113 |    0.1084 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -0.6506 |        0.7423 |          -0.0069 | False          | nan      |       nan      |     0.9999 |
| H3a          | logit    | rules_tech - hitai_full                                      |  2.2657 |        0.0117 |           0.0308 | False          | nan      |       nan      |     0.0516 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  1.66   |        0.0485 |           0.0163 | False          | nan      |       nan      |     0.1777 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.457  |        0.007  |           0.0338 | False          | nan      |       nan      |     0.0385 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.281  |        0.001  |         nan      | False          | nan      |       nan      |     0.0076 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0649 |        0.0681 |         nan      | False          | nan      |       nan      |     0.1872 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.2334 |        0.8154 |          -0.0014 | False          | nan      |       nan      |     0.9999 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -3.3212 |        0.9996 |          -0.0388 | False          | nan      |       nan      |     0.9999 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  1.4113 |        0.0791 |           0.0125 | False          | nan      |       nan      |     0.1933 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  0.8465 |        0.1986 |           0.0071 | False          | nan      |       nan      |     0.3973 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  0.692  |        0.2445 |           0.0065 | False          | nan      |       nan      |     0.4482 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  5.2897 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0202 |        0.322  |         nan      | False          | nan      |       nan      |     0.545  |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.3328 |        0.7393 |          -0.0019 | False          | nan      |       nan      |     0.9999 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -3.6615 |        0.9999 |          -0.0635 | True           |   1      |         1      |     0.9999 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      | -1.7405 |        0.9591 |          -0.0236 | True           |   1      |         1      |     0.9999 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       | -1.8388 |        0.967  |          -0.0249 | True           |   1      |         1      |     0.9999 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         | -1.9088 |        0.9719 |          -0.0268 | True           |   1      |         1      |     0.9999 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.1153 |        0      |         nan      | False          | nan      |       nan      |     0.0004 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0547 |        0.105  |         nan      | True           |   0.5248 |         0.5248 |     0.2309 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.8258 |        0.0679 |          -0.0132 | False          | nan      |       nan      |     0.1872 |
| H4b          | tagger   | corr(tag,fwd) original=0.1485 vs perturbed-context (want ~0) |  0.0118 |        0.3937 |           0.1368 | False          | nan      |       nan      |     0.6187 |

## Reality check / SPA vs rules_only: RC p=0.980, SPA p=0.563

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 1284 |    0.6966 |  0.2515 | 0.0345 | 0.4694 |      0.5413 |           0.3555 |    0.6279 |
| rules_tech|pit|gbt_mono      | 1284 |    0.6962 |  0.2513 | 0.0393 | 0.4776 |      0.5413 |          -2.6285 |    0.0039 |
| hitai_full|pit|gbt_mono      | 1284 |    0.6972 |  0.2518 | 0.0395 | 0.5027 |      0.5413 |           2.3407 |    0.9837 |
| hitai_full|shuffled|gbt_mono | 1284 |    0.6961 |  0.2513 | 0.0422 | 0.4761 |      0.5413 |          -2.1068 |    0.0213 |
