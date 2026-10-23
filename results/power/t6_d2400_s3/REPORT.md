# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 11004, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6606 |    0.6944 |  0.2506 | 0.0136 | 0.5119 |      0.5101 |             0.0191 |                 0.6944 |             0.4886 |           0.3155 |          0.0736 |          0.7148 |    0.7446 |      -0.1695 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6606 |    0.6951 |  0.2509 | 0.0153 | 0.5092 |      0.5101 |             0.0197 |                 0.6943 |             0.3866 |           0.1602 |          0.0722 |          0.4124 |    0.6308 |      -0.1609 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6606 |    0.6921 |  0.2495 | 0.0127 | 0.5199 |      0.5101 |             0.017  |                 0.6932 |             0.4257 |           0.227  |          0.0521 |          0.2452 |    0.6815 |      -0.1711 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6606 |    0.6995 |  0.2514 | 0.0183 | 0.5123 |      0.5101 |             0.0278 |                 0.6953 |             0.8341 |           0.2028 |          0.2563 |          0.7402 |    0.6639 |      -0.1647 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6606 |    0.698  |  0.2506 | 0.0272 | 0.5084 |      0.5101 |             0.0501 |                 0.7028 |             0.7628 |          -0.0557 |          0.2206 |          0.31   |    0.4537 |      -0.1566 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6606 |    0.6981 |  0.2519 | 0.0327 | 0.5029 |      0.5101 |             0.0405 |                 0.6978 |             0.3888 |          -0.4713 |          0.2846 |          0.457  |    0.162  |      -0.3094 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6606 |    0.6987 |  0.2515 | 0.0197 | 0.5069 |      0.5101 |             0.0281 |                 0.6962 |             0.6483 |           0.0671 |          0.2262 |          0.6785 |    0.5557 |      -0.209  |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6606 |    0.701  |  0.2511 | 0.0291 | 0.5064 |      0.5101 |             0.0499 |                 0.7029 |             0.3953 |          -0.3085 |          0.2063 |          0.3436 |    0.2587 |      -0.2115 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6606 |    0.6981 |  0.2519 | 0.0327 | 0.5029 |      0.5101 |             0.0405 |                 0.6978 |             0.3888 |          -0.4713 |          0.2846 |          0.457  |    0.162  |      -0.3094 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6606 |    0.692  |  0.2476 | 0.0246 | 0.5769 |      0.5101 |             0.019  |                 0.6834 |             4.2421 |           3.0515 |          0.5115 |          0.8342 |    1      |      -0.0684 |    0.8652 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6606 |    0.6879 |  0.247  | 0.023  | 0.5681 |      0.5101 |             0.031  |                 0.6881 |             3.1557 |           1.9781 |          0.4946 |          0.7614 |    1      |      -0.1198 |    0.1417 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6606 |    0.6876 |  0.2459 | 0.0171 | 0.5817 |      0.5101 |             0.0135 |                 0.6823 |             4.123  |           2.9029 |          0.5153 |          0.802  |    1      |      -0.0849 |    0.7893 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6606 |    0.7012 |  0.2518 | 0.0161 | 0.5062 |      0.5101 |             0.0424 |                 0.6974 |             0.5157 |          -0.4043 |          0.3238 |          0.5348 |    0.1987 |      -0.2629 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6606 |    0.7005 |  0.2515 | 0.0283 | 0.5044 |      0.5101 |             0.0524 |                 0.7033 |            -0.3322 |          -0.9876 |          0.1602 |          0.2334 |    0.017  |      -0.3063 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6606 |    0.7024 |  0.2518 | 0.0297 | 0.506  |      0.5101 |             0.044  |                 0.6976 |             0.223  |          -0.583  |          0.2576 |          0.4213 |    0.111  |      -0.3397 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6606 |    0.6996 |  0.2517 | 0.0219 | 0.5073 |      0.5101 |             0.0321 |                 0.696  |             0.7349 |           0.0547 |          0.2358 |          0.5292 |    0.5455 |      -0.1564 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6606 |    0.6993 |  0.2514 | 0.0213 | 0.5054 |      0.5101 |             0.0505 |                 0.7019 |             0.5027 |          -0.2191 |          0.2221 |          0.3636 |    0.3229 |      -0.2579 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6606 |    0.6998 |  0.2523 | 0.031  | 0.5028 |      0.5101 |             0.0399 |                 0.6975 |             0.4958 |          -0.3724 |          0.2758 |          0.4423 |    0.2184 |      -0.2476 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6606 |    0.6872 |  0.2462 | 0.0215 | 0.5772 |      0.5101 |             0.0221 |                 0.6837 |             4.2114 |           3.0302 |          0.5381 |          0.9394 |    1      |      -0.0694 |    0.8566 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6606 |    0.6896 |  0.2466 | 0.0189 | 0.5695 |      0.5101 |             0.0289 |                 0.6862 |             2.4305 |           1.229  |          0.4891 |          0.7184 |    0.9944 |      -0.1645 |    0.0043 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6606 |    0.6859 |  0.245  | 0.0162 | 0.585  |      0.5101 |             0.0123 |                 0.6807 |             3.514  |           2.3846 |          0.5041 |          0.8781 |    1      |      -0.1093 |    0.4063 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  0.6924 |        0.2443 |           0.0024 | False          | nan      |       nan      |     0.2829 |
| H3a          | logit    | rules_tech - hitai_full                                      |  1.9003 |        0.0287 |           0.0067 | False          | nan      |       nan      |     0.0451 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  2.2093 |        0.0136 |           0.0092 | False          | nan      |       nan      |     0.0332 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  1.995  |        0.023  |           0.0076 | False          | nan      |       nan      |     0.0395 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.2972 |        0.0216 |         nan      | False          | nan      |       nan      |     0.0395 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0683 |        0.0116 |         nan      | False          | nan      |       nan      |     0.0319 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.9594 |        0.0501 |          -0.0048 | False          | nan      |       nan      |     0.0734 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  2.1648 |        0.0152 |           0.0072 | False          | nan      |       nan      |     0.0334 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  3.4895 |        0.0002 |           0.0131 | False          | nan      |       nan      |     0.0018 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  3.5022 |        0.0002 |           0.0126 | False          | nan      |       nan      |     0.0018 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  3.2207 |        0.0006 |           0.0114 | False          | nan      |       nan      |     0.0028 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.1067 |        0.0019 |         nan      | False          | nan      |       nan      |     0.0059 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               | -0.0022 |        0.5297 |         nan      | False          | nan      |       nan      |     0.555  |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.5362 |        0.5918 |           0.0017 | False          | nan      |       nan      |     0.5918 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  1.2404 |        0.1074 |           0.0045 | True           |   0.1074 |         0.5371 |     0.139  |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  2.9393 |        0.0016 |           0.0105 | True           |   0.0049 |         0.0082 |     0.0059 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  3.5952 |        0.0002 |           0.0148 | True           |   0.0008 |         0.0008 |     0.0018 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  3.2739 |        0.0005 |           0.0122 | True           |   0.0021 |         0.0027 |     0.0028 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.7015 |        0.0889 |         nan      | False          | nan      |       nan      |     0.1222 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0599 |        0.0233 |         nan      | True           |   0.0466 |         0.1166 |     0.0395 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.7702 |        0.4412 |          -0.0017 | False          | nan      |       nan      |     0.4853 |
| H4b          | tagger   | corr(tag,fwd) original=0.1821 vs perturbed-context (want ~0) | -0.0117 |        0.2196 |           0.1938 | False          | nan      |       nan      |     0.2683 |

## Reality check / SPA vs rules_only: RC p=0.237, SPA p=0.203

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2724 |    0.7064 |  0.2562 | 0.0542 | 0.492  |      0.4901 |          -0.5618 |    0.2244 |
| rules_tech|pit|gbt_mono      | 2724 |    0.738  |  0.2574 | 0.0634 | 0.4956 |      0.4901 |          -1.0933 |    0.0706 |
| hitai_full|pit|gbt_mono      | 2724 |    0.6888 |  0.2477 | 0.0444 | 0.5765 |      0.4901 |           2.3233 |    0.999  |
| hitai_full|shuffled|gbt_mono | 2724 |    0.7203 |  0.2558 | 0.0606 | 0.4925 |      0.4901 |          -0.9529 |    0.099  |
