# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 5244, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 3150 |    0.7081 |  0.2548 | 0.0291 | 0.5075 |      0.4956 |             0.0449 |                 0.6988 |            -0.4358 |          -0.5857 |          0.0505 |          0.6495 |    0.1989 |      -0.1858 |    0.0003 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 3150 |    0.6958 |  0.2512 | 0.0176 | 0.5138 |      0.4956 |             0.0348 |                 0.6965 |            -0.0827 |          -0.2134 |          0.0343 |          0.4159 |    0.379  |      -0.1341 |    0.002  |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 3150 |    0.6939 |  0.2504 | 0.0155 | 0.515  |      0.4956 |             0.0285 |                 0.6948 |            -0.0682 |          -0.1033 |          0.0114 |          0.6    |    0.4407 |      -0.1647 |    0.0033 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 3150 |    0.7133 |  0.2536 | 0.039  | 0.5227 |      0.4956 |             0.0463 |                 0.6973 |            -0.1967 |          -0.8943 |          0.2156 |          0.5524 |    0.0988 |      -0.2389 |    0.0001 |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 3150 |    0.7273 |  0.2558 | 0.041  | 0.5026 |      0.4956 |             0.0907 |                 0.716  |            -0.5557 |          -0.9769 |          0.1644 |          0.853  |    0.0803 |      -0.312  |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 3150 |    0.7073 |  0.2533 | 0.0359 | 0.508  |      0.4956 |             0.0625 |                 0.7066 |            -0.2624 |          -0.9456 |          0.247  |          0.7717 |    0.0864 |      -0.2706 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 3150 |    0.7067 |  0.2517 | 0.0268 | 0.5242 |      0.4956 |             0.0573 |                 0.7001 |            -0.1946 |          -0.8192 |          0.193  |          0.514  |    0.1196 |      -0.1881 |    0.0001 |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 3150 |    0.7254 |  0.2555 | 0.0406 | 0.5027 |      0.4956 |             0.0909 |                 0.716  |            -0.4435 |          -0.8507 |          0.1581 |          0.853  |    0.1107 |      -0.2962 |    0.0001 |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 3150 |    0.7073 |  0.2533 | 0.0359 | 0.508  |      0.4956 |             0.0625 |                 0.7066 |            -0.2624 |          -0.9456 |          0.247  |          0.7717 |    0.0864 |      -0.2706 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 3150 |    0.713  |  0.2504 | 0.0332 | 0.5641 |      0.4956 |             0.0465 |                 0.6889 |             2.2342 |           0.889  |          0.4943 |          0.801  |    0.9004 |      -0.1464 |    0.0997 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 3150 |    0.7078 |  0.2504 | 0.034  | 0.5539 |      0.4956 |             0.0687 |                 0.7016 |             1.9213 |           0.8374 |          0.4041 |          0.8197 |    0.8872 |      -0.108  |    0.0869 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 3150 |    0.7121 |  0.2506 | 0.0327 | 0.5623 |      0.4956 |             0.0384 |                 0.6907 |             2.696  |           1.4309 |          0.4657 |          0.7987 |    0.9803 |      -0.0835 |    0.309  |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 3150 |    0.7171 |  0.2532 | 0.0289 | 0.5209 |      0.4956 |             0.0576 |                 0.7013 |             0.0431 |          -0.6566 |          0.2333 |          0.6057 |    0.1714 |      -0.1715 |    0.0002 |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 3150 |    0.7377 |  0.2563 | 0.0465 | 0.501  |      0.4956 |             0.0902 |                 0.717  |            -0.3008 |          -0.7784 |          0.1975 |          0.9759 |    0.1315 |      -0.2886 |    0.0001 |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 3150 |    0.7256 |  0.2551 | 0.044  | 0.5113 |      0.4956 |             0.0589 |                 0.7063 |            -0.4741 |          -1.1901 |          0.2622 |          0.7902 |    0.0426 |      -0.3263 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 3150 |    0.7133 |  0.2528 | 0.0334 | 0.5209 |      0.4956 |             0.0626 |                 0.7034 |            -0.0574 |          -0.6391 |          0.1984 |          0.601  |    0.1782 |      -0.2772 |    0.0002 |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 3150 |    0.7138 |  0.2566 | 0.0483 | 0.5166 |      0.4956 |             0.0869 |                 0.7136 |            -0.0416 |          -0.7734 |          0.2816 |          0.8575 |    0.1321 |      -0.2608 |    0.0001 |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 3150 |    0.7301 |  0.258  | 0.0542 | 0.5076 |      0.4956 |             0.0759 |                 0.7069 |            -0.145  |          -0.8153 |          0.2708 |          0.9127 |    0.1201 |      -0.3326 |    0.0001 |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 3150 |    0.7159 |  0.2507 | 0.0311 | 0.5695 |      0.4956 |             0.0465 |                 0.6893 |             2.4682 |           1.3746 |          0.4276 |          0.8286 |    0.9766 |      -0.147  |    0.28   |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 3150 |    0.7261 |  0.2529 | 0.0361 | 0.5499 |      0.4956 |             0.075  |                 0.7037 |             1.7717 |           0.8855 |          0.353  |          0.919  |    0.9003 |      -0.1468 |    0.098  |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 3150 |    0.7316 |  0.2523 | 0.0243 | 0.5615 |      0.4956 |             0.0441 |                 0.692  |             2.643  |           1.5137 |          0.4295 |          0.841  |    0.9855 |      -0.1184 |    0.3518 |         21 |

## Hypothesis tests

| hypothesis   | model        | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:-------------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit        | rules_only - hitai_full (logloss)                            | -0.4358 |        0.6685 |          -0.0049 | False          | nan      |       nan      |     0.799  |
| H3a          | logit        | rules_tech - hitai_full                                      | -0.5334 |        0.7031 |          -0.0063 | False          | nan      |       nan      |     0.799  |
| H3b          | logit        | hitai_full[shuffled] - hitai_full[pit]                       |  0.3141 |        0.3767 |           0.0041 | False          | nan      |       nan      |     0.554  |
| H3c          | logit        | hitai_full[lagged] - hitai_full[pit]                         |  0.0272 |        0.4892 |           0.0003 | False          | nan      |       nan      |     0.6436 |
| H2a          | logit        | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.1397 |        0.0324 |         nan      | False          | nan      |       nan      |     0.1349 |
| H2b          | logit        | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.041  |        0.1737 |         nan      | False          | nan      |       nan      |     0.2895 |
| H4a          | logit        | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.3021 |        0.7626 |           0.0029 | False          | nan      |       nan      |     0.8289 |
| H1           | gbt          | rules_only - hitai_full (logloss)                            | -1.6712 |        0.9527 |          -0.012  | False          | nan      |       nan      |     0.9619 |
| H3a          | gbt          | rules_tech - hitai_full                                      |  1.6588 |        0.0486 |           0.0176 | False          | nan      |       nan      |     0.1712 |
| H3b          | gbt          | hitai_full[shuffled] - hitai_full[pit]                       |  2.3776 |        0.0087 |           0.0299 | False          | nan      |       nan      |     0.0436 |
| H3c          | gbt          | hitai_full[lagged] - hitai_full[pit]                         |  0.816  |        0.2072 |           0.0061 | False          | nan      |       nan      |     0.3238 |
| H2a          | gbt          | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.4297 |        0.0006 |         nan      | False          | nan      |       nan      |     0.0038 |
| H2b          | gbt          | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0536 |        0.1093 |         nan      | False          | nan      |       nan      |     0.2277 |
| H4a          | gbt          | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.9206 |        0.0548 |           0.0183 | False          | nan      |       nan      |     0.1712 |
| H1           | gbt_mono     | rules_only - hitai_full (logloss)                            | -1.7737 |        0.9619 |          -0.0181 | True           |   1      |         1      |     0.9619 |
| H3a          | gbt_mono     | rules_tech - hitai_full                                      | -0.445  |        0.6718 |          -0.0047 | True           |   1      |         1      |     0.799  |
| H3b          | gbt_mono     | hitai_full[shuffled] - hitai_full[pit]                       |  1.0202 |        0.1538 |           0.0135 | True           |   0.5442 |         0.769  |     0.2747 |
| H3c          | gbt_mono     | hitai_full[lagged] - hitai_full[pit]                         |  1.2824 |        0.0998 |           0.018  | True           |   0.4992 |         0.4992 |     0.2269 |
| H2a          | gbt_mono     | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.8461 |        0.0649 |         nan      | False          | nan      |       nan      |     0.1802 |
| H2b          | gbt_mono     | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0479 |        0.1361 |         nan      | True           |   0.5442 |         0.6803 |     0.2616 |
| H4a          | gbt_mono     | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.7682 |        0.077  |           0.0196 | False          | nan      |       nan      |     0.1926 |
| H4b          | tagger       | corr(tag,fwd) original=0.1953 vs perturbed-context (want ~0) |  0.0114 |        0.4099 |           0.1839 | False          | nan      |       nan      |     0.5693 |
| H4-demo      | leaky_tagger | corr(tag,fwd) unmasked                                       |  0.8659 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4-demo      | leaky_tagger | corr(tag,fwd) masked                                         |  0.1865 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4-demo      | leaky_tagger | corr(tag,fwd) perturbed                                      |  0.8659 |        0      |         nan      | False          | nan      |       nan      |     0      |

## Reality check / SPA vs rules_only: RC p=1.000, SPA p=1.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 1284 |    0.6929 |  0.2499 | 0.0154 | 0.5031 |      0.4891 |          -1.0271 |    0.1705 |
| rules_tech|pit|gbt_mono      | 1284 |    0.6959 |  0.2515 | 0.0466 | 0.4974 |      0.4891 |          -1.7179 |    0.0574 |
| hitai_full|pit|gbt_mono      | 1284 |    0.6906 |  0.2484 | 0.0418 | 0.5626 |      0.4891 |           1.9092 |    0.9559 |
| hitai_full|shuffled|gbt_mono | 1284 |    0.7108 |  0.2535 | 0.0521 | 0.4965 |      0.4891 |          -1.8375 |    0.0444 |
