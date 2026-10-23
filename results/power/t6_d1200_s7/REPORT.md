# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 5244, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 3150 |    0.7072 |  0.256  | 0.0769 | 0.4718 |      0.4698 |             0.0298 |                 0.6946 |            -0.229  |          -0.5005 |          0.1086 |          0.6911 |    0.2366 |      -0.2371 |    0.0006 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 3150 |    0.705  |  0.2559 | 0.0808 | 0.4703 |      0.4698 |             0.0285 |                 0.6941 |             0.2012 |           0.064  |          0.0571 |          0.8076 |    0.5368 |      -0.1935 |    0.0076 |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 3150 |    0.7033 |  0.255  | 0.0696 | 0.4632 |      0.4698 |             0.0203 |                 0.6924 |            -0.4503 |          -0.5864 |          0.0514 |          0.6    |    0.2002 |      -0.177  |    0.0004 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 3150 |    0.7727 |  0.2646 | 0.0745 | 0.4692 |      0.4698 |             0.073  |                 0.7069 |            -0.1736 |          -0.5586 |          0.179  |          0.9067 |    0.211  |      -0.312  |    0.0005 |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 3150 |    0.729  |  0.2583 | 0.0833 | 0.4837 |      0.4698 |             0.1027 |                 0.7263 |            -0.4301 |          -0.8501 |          0.1848 |          0.8568 |    0.1107 |      -0.3036 |    0.0001 |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 3150 |    0.7288 |  0.2599 | 0.0943 | 0.4836 |      0.4698 |             0.0865 |                 0.7127 |            -0.9748 |          -1.3254 |          0.1683 |          0.974  |    0.0285 |      -0.4129 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 3150 |    0.785  |  0.2673 | 0.0788 | 0.4636 |      0.4698 |             0.075  |                 0.7083 |            -0.1318 |          -0.5422 |          0.1727 |          0.7317 |    0.2182 |      -0.2337 |    0.0005 |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 3150 |    0.7293 |  0.2584 | 0.0815 | 0.4815 |      0.4698 |             0.1012 |                 0.727  |            -0.4441 |          -0.8509 |          0.18   |          0.867  |    0.1106 |      -0.301  |    0.0001 |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 3150 |    0.7288 |  0.2599 | 0.0943 | 0.4836 |      0.4698 |             0.0865 |                 0.7127 |            -0.9748 |          -1.3254 |          0.1683 |          0.974  |    0.0285 |      -0.4129 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 3150 |    0.7374 |  0.2573 | 0.0626 | 0.5347 |      0.4698 |             0.0656 |                 0.6963 |             2.4494 |           1.5781 |          0.4463 |          0.9702 |    0.9888 |      -0.1846 |    0.4041 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 3150 |    0.7113 |  0.2565 | 0.0603 | 0.5242 |      0.4698 |             0.0831 |                 0.7091 |             2.2221 |           1.3526 |          0.3727 |          0.7419 |    0.9734 |      -0.1647 |    0.2872 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 3150 |    0.7257 |  0.2554 | 0.0697 | 0.5231 |      0.4698 |             0.0627 |                 0.6994 |             1.669  |           0.8641 |          0.3549 |          0.7879 |    0.8935 |      -0.1442 |    0.1019 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 3150 |    0.7802 |  0.2648 | 0.0925 | 0.4655 |      0.4698 |             0.0777 |                 0.7102 |            -0.6936 |          -1.2698 |          0.2406 |          0.7587 |    0.0357 |      -0.3459 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 3150 |    0.7248 |  0.2578 | 0.0769 | 0.4852 |      0.4698 |             0.0948 |                 0.7273 |            -0.131  |          -0.5689 |          0.186  |          0.8181 |    0.2063 |      -0.29   |    0.0004 |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 3150 |    0.7397 |  0.2615 | 0.0911 | 0.4822 |      0.4698 |             0.0837 |                 0.7123 |            -0.7452 |          -1.1333 |          0.1816 |          0.9352 |    0.0519 |      -0.3809 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 3150 |    0.7827 |  0.2643 | 0.0669 | 0.4724 |      0.4698 |             0.0714 |                 0.7089 |            -0.2094 |          -0.634  |          0.1867 |          0.7937 |    0.1809 |      -0.2431 |    0.0003 |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 3150 |    0.7335 |  0.2584 | 0.0853 | 0.4898 |      0.4698 |             0.0946 |                 0.7248 |             0.3471 |          -0.267  |          0.2584 |          0.7975 |    0.3503 |      -0.2873 |    0.0019 |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 3150 |    0.7441 |  0.2603 | 0.091  | 0.4869 |      0.4698 |             0.0799 |                 0.7108 |            -0.5407 |          -0.9318 |          0.1797 |          0.9156 |    0.0906 |      -0.3764 |    0.0001 |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 3150 |    0.7214 |  0.2548 | 0.0635 | 0.5244 |      0.4698 |             0.0574 |                 0.6961 |             1.7554 |           0.8525 |          0.4416 |          0.934  |    0.8909 |      -0.1612 |    0.0985 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 3150 |    0.7175 |  0.2571 | 0.0668 | 0.5191 |      0.4698 |             0.0868 |                 0.7133 |             1.639  |           0.9353 |          0.3238 |          0.8838 |    0.9111 |      -0.1578 |    0.1215 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 3150 |    0.7624 |  0.2605 | 0.0792 | 0.5041 |      0.4698 |             0.0599 |                 0.6994 |             1.3053 |           0.5882 |          0.3267 |          0.8892 |    0.8025 |      -0.2016 |    0.0471 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -2.2605 |        0.9881 |          -0.0302 | False          | nan      |       nan      |     0.9881 |
| H3a          | logit    | rules_tech - hitai_full                                      |  3.2222 |        0.0006 |           0.0476 | False          | nan      |       nan      |     0.0047 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.8854 |        0.002  |           0.0429 | False          | nan      |       nan      |     0.0086 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.9051 |        0.0018 |           0.0453 | False          | nan      |       nan      |     0.0086 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.1431 |        0      |         nan      | False          | nan      |       nan      |     0.0005 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0875 |        0.0223 |         nan      | False          | nan      |       nan      |     0.0699 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.5551 |        0.1199 |          -0.016  | False          | nan      |       nan      |     0.1849 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -0.931  |        0.8241 |          -0.0063 | False          | nan      |       nan      |     0.9065 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  1.4893 |        0.0682 |           0.018  | False          | nan      |       nan      |     0.1364 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  1.1451 |        0.1261 |           0.0135 | False          | nan      |       nan      |     0.1849 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  1.5462 |        0.061  |           0.0222 | False          | nan      |       nan      |     0.1343 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.073  |        0      |         nan      | False          | nan      |       nan      |     0.0005 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0472 |        0.1397 |         nan      | False          | nan      |       nan      |     0.1921 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.0253 |        0.3052 |           0.0062 | False          | nan      |       nan      |     0.395  |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -2.1122 |        0.9827 |          -0.0224 | True           |   0.9827 |         1      |     0.9881 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  0.3288 |        0.3711 |           0.0031 | True           |   0.7423 |         1      |     0.4419 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  1.3508 |        0.0884 |           0.014  | True           |   0.3353 |         0.4419 |     0.1496 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  1.3797 |        0.0838 |           0.0184 | True           |   0.3353 |         0.4192 |     0.1496 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.8677 |        0.0041 |         nan      | False          | nan      |       nan      |     0.0152 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.076  |        0.0406 |         nan      | True           |   0.2029 |         0.2029 |     0.0992 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  2.1493 |        0.0316 |           0.0367 | False          | nan      |       nan      |     0.0869 |
| H4b          | tagger   | corr(tag,fwd) original=0.1952 vs perturbed-context (want ~0) |  0.0121 |        0.3816 |           0.1831 | False          | nan      |       nan      |     0.4419 |

## Reality check / SPA vs rules_only: RC p=0.997, SPA p=1.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 1284 |    0.6973 |  0.252  | 0.045  | 0.4975 |      0.4938 |          -0.56   |    0.3035 |
| rules_tech|pit|gbt_mono      | 1284 |    0.7801 |  0.2612 | 0.0628 | 0.5014 |      0.4938 |          -0.2824 |    0.3977 |
| hitai_full|pit|gbt_mono      | 1284 |    0.6957 |  0.2494 | 0.0524 | 0.5781 |      0.4938 |           1.4839 |    0.9094 |
| hitai_full|shuffled|gbt_mono | 1284 |    0.7785 |  0.261  | 0.0603 | 0.4971 |      0.4938 |          -0.2979 |    0.3922 |
