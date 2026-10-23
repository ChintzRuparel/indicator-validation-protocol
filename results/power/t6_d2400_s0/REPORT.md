# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 11004, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6606 |    0.6954 |  0.2511 | 0.0309 | 0.4984 |       0.521 |             0.0181 |                 0.6935 |             0.1326 |          -0.0861 |          0.0775 |          0.6971 |    0.4286 |      -0.2878 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6606 |    0.6951 |  0.251  | 0.0258 | 0.4913 |       0.521 |             0.0184 |                 0.6935 |             0.1097 |          -0.2883 |          0.1483 |          0.7074 |    0.2736 |      -0.2946 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6606 |    0.6946 |  0.2507 | 0.0202 | 0.5025 |       0.521 |             0.0182 |                 0.6933 |             0.1144 |          -0.0558 |          0.0633 |          0.7449 |    0.4536 |      -0.2171 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6606 |    0.6999 |  0.2531 | 0.0319 | 0.4982 |       0.521 |             0.0192 |                 0.696  |            -0.0175 |          -0.421  |          0.158  |          0.8011 |    0.189  |      -0.4348 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6606 |    0.7034 |  0.2533 | 0.0293 | 0.4844 |       0.521 |             0.0747 |                 0.7127 |             0.0566 |          -0.4068 |          0.1798 |          0.8103 |    0.1975 |      -0.3866 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6606 |    0.7103 |  0.2557 | 0.05   | 0.4824 |       0.521 |             0.0615 |                 0.7064 |            -0.1813 |          -0.6274 |          0.185  |          0.8981 |    0.0948 |      -0.4667 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6606 |    0.7055 |  0.2534 | 0.0387 | 0.494  |       0.521 |             0.0299 |                 0.6974 |             0.0733 |          -0.358  |          0.1732 |          0.8137 |    0.2271 |      -0.4254 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6606 |    0.7031 |  0.2531 | 0.0288 | 0.4854 |       0.521 |             0.0727 |                 0.7126 |             0.0865 |          -0.3766 |          0.1798 |          0.8123 |    0.2156 |      -0.3739 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6606 |    0.7103 |  0.2557 | 0.05   | 0.4824 |       0.521 |             0.0615 |                 0.7064 |            -0.1813 |          -0.6274 |          0.185  |          0.8981 |    0.0948 |      -0.4667 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6606 |    0.6954 |  0.2495 | 0.027  | 0.5496 |       0.521 |             0.0412 |                 0.6905 |             3.3235 |           2.0395 |          0.5005 |          0.8939 |    1      |      -0.0936 |    0.407  |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6606 |    0.6944 |  0.2498 | 0.0315 | 0.5434 |       0.521 |             0.0555 |                 0.7006 |             2.7132 |           1.4446 |          0.4649 |          0.7563 |    0.9987 |      -0.0848 |    0.0694 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6606 |    0.7021 |  0.2504 | 0.0302 | 0.5488 |       0.521 |             0.045  |                 0.695  |             3.0919 |           1.8886 |          0.4585 |          0.817  |    1      |      -0.0824 |    0.2917 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6606 |    0.7057 |  0.2531 | 0.037  | 0.4957 |       0.521 |             0.0315 |                 0.6974 |            -0.1626 |          -0.6705 |          0.1959 |          0.789  |    0.0805 |      -0.4411 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6606 |    0.7038 |  0.2538 | 0.0305 | 0.4854 |       0.521 |             0.077  |                 0.7124 |            -0.1564 |          -0.6492 |          0.1892 |          0.7879 |    0.0871 |      -0.4728 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6606 |    0.7122 |  0.2564 | 0.0512 | 0.4835 |       0.521 |             0.0615 |                 0.7061 |            -0.217  |          -0.6761 |          0.188  |          0.8842 |    0.0787 |      -0.4904 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6606 |    0.699  |  0.2529 | 0.0393 | 0.4912 |       0.521 |             0.0356 |                 0.6982 |            -0.2544 |          -0.644  |          0.157  |          0.8235 |    0.0888 |      -0.5238 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6606 |    0.7047 |  0.2539 | 0.037  | 0.484  |       0.521 |             0.0746 |                 0.7126 |            -0.2957 |          -0.7394 |          0.1744 |          0.7985 |    0.0608 |      -0.5388 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6606 |    0.7166 |  0.2563 | 0.045  | 0.4795 |       0.521 |             0.0623 |                 0.7062 |            -0.2217 |          -0.6096 |          0.1583 |          0.8674 |    0.101  |      -0.4815 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6606 |    0.6929 |  0.2485 | 0.022  | 0.559  |       0.521 |             0.0395 |                 0.6904 |             3.5981 |           2.4137 |          0.4528 |          0.8191 |    1      |      -0.1181 |    0.7059 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6606 |    0.6932 |  0.2496 | 0.0186 | 0.5451 |       0.521 |             0.0606 |                 0.7003 |             2.9049 |           1.6164 |          0.483  |          0.7576 |    0.9996 |      -0.1016 |    0.1325 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6606 |    0.7045 |  0.2509 | 0.0283 | 0.549  |       0.521 |             0.0453 |                 0.6946 |             3.1177 |           1.8575 |          0.4782 |          0.7919 |    0.9999 |      -0.1223 |    0.2717 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -0.0049 |        0.502  |          -0      | False          | nan      |       nan      |     0.5554 |
| H3a          | logit    | rules_tech - hitai_full                                      |  1.8412 |        0.0328 |           0.0101 | False          | nan      |       nan      |     0.0725 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  1.8016 |        0.0358 |           0.0103 | False          | nan      |       nan      |     0.0725 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  1.1221 |        0.1309 |           0.0036 | False          | nan      |       nan      |     0.2057 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.0708 |        0.0021 |         nan      | False          | nan      |       nan      |     0.0078 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0248 |        0.2049 |         nan      | False          | nan      |       nan      |     0.3005 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.8405 |        0.4007 |          -0.0025 | False          | nan      |       nan      |     0.4988 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  0.2324 |        0.4081 |           0.0007 | False          | nan      |       nan      |     0.4988 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  2.895  |        0.0019 |           0.0087 | False          | nan      |       nan      |     0.0078 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  3.2566 |        0.0006 |           0.0094 | False          | nan      |       nan      |     0.0046 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  3.2291 |        0.0006 |           0.0103 | False          | nan      |       nan      |     0.0046 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.1288 |        0.0018 |         nan      | False          | nan      |       nan      |     0.0078 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.039  |        0.0977 |         nan      | False          | nan      |       nan      |     0.1653 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.6304 |        0.5284 |          -0.0012 | False          | nan      |       nan      |     0.5554 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -1.2413 |        0.8928 |          -0.0075 | True           |   0.8928 |         1      |     0.8928 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  1.7959 |        0.0363 |           0.0081 | True           |   0.1088 |         0.1813 |     0.0725 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  2.1977 |        0.014  |           0.0101 | True           |   0.0559 |         0.0699 |     0.0385 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  2.5072 |        0.0061 |           0.0144 | True           |   0.0304 |         0.0304 |     0.0191 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.3961 |        0      |         nan      | False          | nan      |       nan      |     0.0002 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0452 |        0.0668 |         nan      | True           |   0.1336 |         0.334  |     0.1225 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.9343 |        0.3502 |           0.0024 | False          | nan      |       nan      |     0.4815 |
| H4b          | tagger   | corr(tag,fwd) original=0.1660 vs perturbed-context (want ~0) | -0.006  |        0.5301 |           0.172  | False          | nan      |       nan      |     0.5554 |

## Reality check / SPA vs rules_only: RC p=0.947, SPA p=0.907

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2724 |    0.6943 |  0.2506 | 0.0243 | 0.4982 |      0.5018 |           0.5601 |    0.7741 |
| rules_tech|pit|gbt_mono      | 2724 |    0.695  |  0.2509 | 0.0268 | 0.4989 |      0.5018 |           0.4367 |    0.7212 |
| hitai_full|pit|gbt_mono      | 2724 |    0.6885 |  0.2477 | 0.0243 | 0.5675 |      0.5018 |           1.8039 |    0.9921 |
| hitai_full|shuffled|gbt_mono | 2724 |    0.695  |  0.2509 | 0.0268 | 0.4989 |      0.5018 |           0.4367 |    0.7212 |
