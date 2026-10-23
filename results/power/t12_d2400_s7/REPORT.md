# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 22008, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 13212 |    0.6944 |  0.2504 | 0.0235 | 0.5124 |      0.5027 |             0.0056 |                 0.6926 |             0.6021 |          -0.0042 |          0.1355 |          0.4977 |    0.4965 |      -0.1659 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 13212 |    0.6943 |  0.2503 | 0.0227 | 0.5151 |      0.5027 |             0.0063 |                 0.693  |             0.957  |          -0.1696 |          0.2706 |          0.5959 |    0.3616 |      -0.1302 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 13212 |    0.6934 |  0.2501 | 0.0118 | 0.5045 |      0.5027 |             0.0103 |                 0.6932 |             0.3791 |          -0.2293 |          0.0855 |          0.2152 |    0.3166 |      -0.1058 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 13212 |    0.6991 |  0.2513 | 0.0194 | 0.5123 |      0.5027 |             0.0149 |                 0.6929 |             0.8746 |          -0.2379 |          0.2325 |          0.4507 |    0.3096 |      -0.1619 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 13212 |    0.6962 |  0.2506 | 0.024  | 0.5097 |      0.5027 |             0.0432 |                 0.6975 |            -0.1055 |          -1.3455 |          0.305  |          0.606  |    0.0024 |      -0.4377 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 13212 |    0.6967 |  0.2506 | 0.0264 | 0.5092 |      0.5027 |             0.0301 |                 0.6947 |            -0.2272 |          -1.1538 |          0.243  |          0.7196 |    0.0079 |      -0.353  |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 13212 |    0.6956 |  0.2506 | 0.0165 | 0.5109 |      0.5027 |             0.0164 |                 0.693  |             0.6543 |          -0.5063 |          0.221  |          0.3615 |    0.1449 |      -0.2065 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 13212 |    0.696  |  0.2506 | 0.023  | 0.5101 |      0.5027 |             0.0445 |                 0.6975 |            -0.1682 |          -1.3962 |          0.3013 |          0.5931 |    0.0018 |      -0.4216 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 13212 |    0.6966 |  0.2506 | 0.0263 | 0.5078 |      0.5027 |             0.0289 |                 0.6948 |            -0.223  |          -1.2573 |          0.2657 |          0.681  |    0.0043 |      -0.3756 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 13212 |    0.6859 |  0.2445 | 0.0079 | 0.5899 |      0.5027 |             0.0108 |                 0.6802 |             7.6641 |           5.6932 |          0.5554 |          0.9264 |    1      |      -0.0355 |    0.8661 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 13212 |    0.6857 |  0.2462 | 0.0134 | 0.5763 |      0.5027 |             0.0196 |                 0.6838 |             5.6607 |           3.6833 |          0.5333 |          0.8342 |    1      |      -0.0463 |    0.0011 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 13212 |    0.6827 |  0.2445 | 0.0209 | 0.5865 |      0.5027 |             0.0092 |                 0.681  |             6.8917 |           4.9177 |          0.5198 |          0.7851 |    1      |      -0.0355 |    0.3193 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 13212 |    0.7002 |  0.2511 | 0.0191 | 0.5062 |      0.5027 |             0.0184 |                 0.6931 |             1.0677 |          -0.2472 |          0.2468 |          0.378  |    0.3027 |      -0.1548 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 13212 |    0.6964 |  0.2506 | 0.0248 | 0.5077 |      0.5027 |             0.0419 |                 0.6974 |            -0.5397 |          -1.6912 |          0.2851 |          0.6583 |    0.0002 |      -0.4646 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 13212 |    0.6965 |  0.2507 | 0.0315 | 0.5054 |      0.5027 |             0.0284 |                 0.6947 |            -0.3273 |          -1.3742 |          0.2674 |          0.6563 |    0.0021 |      -0.4202 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 13212 |    0.6945 |  0.2505 | 0.0161 | 0.512  |      0.5027 |             0.0157 |                 0.6933 |             0.5915 |          -0.43   |          0.191  |          0.4086 |    0.1847 |      -0.2274 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 13212 |    0.6974 |  0.2506 | 0.0214 | 0.5073 |      0.5027 |             0.0422 |                 0.6973 |             0.1287 |          -1.0748 |          0.28   |          0.5705 |    0.0126 |      -0.3096 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 13212 |    0.6968 |  0.2506 | 0.0247 | 0.5101 |      0.5027 |             0.0312 |                 0.6947 |            -0.5731 |          -1.7209 |          0.2749 |          0.5964 |    0.0002 |      -0.4816 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 13212 |    0.6849 |  0.244  | 0.0184 | 0.5916 |      0.5027 |             0.0154 |                 0.6795 |             7.7377 |           5.7658 |          0.5418 |          0.8221 |    1      |      -0.0425 |    0.8896 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 13212 |    0.6848 |  0.2455 | 0.0148 | 0.5815 |      0.5027 |             0.0153 |                 0.6829 |             5.3376 |           3.518  |          0.5136 |          0.8262 |    1      |      -0.0611 |    0.0003 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 13212 |    0.6823 |  0.2444 | 0.0191 | 0.5872 |      0.5027 |             0.0072 |                 0.6798 |             6.6249 |           4.7951 |          0.5176 |          0.8419 |    1      |      -0.0455 |    0.2371 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  2.8936 |        0.0019 |           0.0085 | False          |      nan |            nan |     0.0028 |
| H3a          | logit    | rules_tech - hitai_full                                      |  3.5268 |        0.0002 |           0.0098 | False          |      nan |            nan |     0.0004 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  4.1911 |        0      |           0.0144 | False          |      nan |            nan |     0      |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  3.2352 |        0.0006 |           0.0087 | False          |      nan |            nan |     0.001  |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  0.2515 |        0.8014 |         nan      | False          |      nan |            nan |     0.8014 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0911 |        0      |         nan      | False          |      nan |            nan |     0      |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.426  |        0.6701 |          -0.0009 | False          |      nan |            nan |     0.7371 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  3.9484 |        0      |           0.0087 | False          |      nan |            nan |     0.0001 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  4.817  |        0      |           0.0104 | False          |      nan |            nan |     0      |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  4.8698 |        0      |           0.0107 | False          |      nan |            nan |     0      |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  5.4923 |        0      |           0.0117 | False          |      nan |            nan |     0      |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  0.9651 |        0.3345 |         nan      | False          |      nan |            nan |     0.4599 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0809 |        0.0001 |         nan      | False          |      nan |            nan |     0.0001 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.7218 |        0.4704 |          -0.0008 | False          |      nan |            nan |     0.6088 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  4.7372 |        0      |           0.0107 | True           |        0 |              0 |     0      |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  6.0895 |        0      |           0.0139 | True           |        0 |              0 |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  5.9164 |        0      |           0.0137 | True           |        0 |              0 |     0      |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  5.845  |        0      |           0.0141 | True           |        0 |              0 |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  0.4969 |        0.6193 |         nan      | False          |      nan |            nan |     0.717  |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0993 |        0      |         nan      | True           |        0 |              0 |     0      |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.2748 |        0.7835 |          -0.0004 | False          |      nan |            nan |     0.8014 |
| H4b          | tagger   | corr(tag,fwd) original=0.1882 vs perturbed-context (want ~0) |  0.0045 |        0.5041 |           0.1837 | False          |      nan |            nan |     0.6161 |

## Reality check / SPA vs rules_only: RC p=0.000, SPA p=0.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5448 |    0.6959 |  0.2514 | 0.0414 | 0.489  |      0.4824 |          -0.9642 |    0.0986 |
| rules_tech|pit|gbt_mono      | 5448 |    0.6974 |  0.2516 | 0.0341 | 0.4948 |      0.4824 |           0.0672 |    0.5361 |
| hitai_full|pit|gbt_mono      | 5448 |    0.6985 |  0.2472 | 0.0294 | 0.5804 |      0.4824 |           5.1212 |    1      |
| hitai_full|shuffled|gbt_mono | 5448 |    0.697  |  0.2514 | 0.0338 | 0.4953 |      0.4824 |           0.0679 |    0.5364 |
