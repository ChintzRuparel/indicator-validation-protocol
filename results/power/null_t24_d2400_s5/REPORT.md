# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6941 |  0.2505 | 0.0134 | 0.4957 |      0.5022 |             0.0088 |                 0.6935 |            -0.4666 |          -0.5789 |          0.0096 |          0.2092 |    0.1119 |      -0.0542 |    0.0058 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6945 |  0.2506 | 0.0177 | 0.4983 |      0.5022 |             0.0086 |                 0.6935 |            -0.6727 |          -1.3318 |          0.0707 |          0.3081 |    0.0024 |      -0.1597 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6941 |  0.2505 | 0.011  | 0.4974 |      0.5022 |             0.0087 |                 0.6934 |            -0.5463 |          -0.8529 |          0.0325 |          0.2992 |    0.0363 |      -0.1103 |    0.0009 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.696  |  0.2511 | 0.0211 | 0.4954 |      0.5022 |             0.0152 |                 0.6941 |            -0.921  |          -1.2881 |          0.033  |          0.2116 |    0.0031 |      -0.1273 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6974 |  0.251  | 0.0203 | 0.495  |      0.5022 |             0.0354 |                 0.6975 |            -0.1866 |          -1.5232 |          0.1285 |          0.2443 |    0.0009 |      -0.1674 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6969 |  0.251  | 0.0209 | 0.4985 |      0.5022 |             0.0224 |                 0.6949 |            -0.1068 |          -1.1629 |          0.119  |          0.2909 |    0.0072 |      -0.1442 |    0.0001 |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6952 |  0.2508 | 0.0179 | 0.4957 |      0.5022 |             0.0167 |                 0.6942 |            -0.6609 |          -1.0297 |          0.035  |          0.2319 |    0.0148 |      -0.1075 |    0.0002 |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6969 |  0.2509 | 0.02   | 0.4949 |      0.5022 |             0.0351 |                 0.6975 |            -0.2248 |          -1.1016 |          0.0909 |          0.2853 |    0.0107 |      -0.1319 |    0.0002 |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6971 |  0.251  | 0.0205 | 0.4991 |      0.5022 |             0.022  |                 0.6949 |            -0.1958 |          -1.2486 |          0.1194 |          0.2948 |    0.0043 |      -0.1558 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.695  |  0.2509 | 0.0173 | 0.4958 |      0.5022 |             0.0188 |                 0.6946 |            -0.7451 |          -1.3427 |          0.0537 |          0.2213 |    0.0023 |      -0.1346 |    0      |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6969 |  0.251  | 0.0182 | 0.4945 |      0.5022 |             0.0373 |                 0.6978 |            -0.6256 |          -1.7085 |          0.0921 |          0.1837 |    0.0002 |      -0.1598 |    0      |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6969 |  0.251  | 0.0171 | 0.4962 |      0.5022 |             0.0236 |                 0.6951 |            -0.5204 |          -1.5524 |          0.1232 |          0.3337 |    0.0005 |      -0.2034 |    0      |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6951 |  0.2509 | 0.0168 | 0.4942 |      0.5022 |             0.0158 |                 0.6943 |            -0.6604 |          -1.0884 |          0.0397 |          0.2298 |    0.0112 |      -0.1111 |    0.0002 |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6975 |  0.251  | 0.0218 | 0.4937 |      0.5022 |             0.0355 |                 0.6977 |            -0.1256 |          -1.2101 |          0.1045 |          0.2407 |    0.0062 |      -0.1336 |    0.0001 |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6968 |  0.251  | 0.0214 | 0.495  |      0.5022 |             0.022  |                 0.6949 |            -0.4205 |          -1.4079 |          0.1178 |          0.3238 |    0.0014 |      -0.1956 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6958 |  0.251  | 0.0226 | 0.4928 |      0.5022 |             0.0215 |                 0.6944 |            -0.3751 |          -0.9947 |          0.063  |          0.2539 |    0.0183 |      -0.1118 |    0.0003 |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6955 |  0.2508 | 0.0208 | 0.493  |      0.5022 |             0.0385 |                 0.6975 |            -0.9382 |          -2.0384 |          0.1298 |          0.3445 |    0      |      -0.2641 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6968 |  0.2511 | 0.0131 | 0.4981 |      0.5022 |             0.0248 |                 0.6949 |            -0.1509 |          -0.838  |          0.059  |          0.2031 |    0.039  |      -0.0816 |    0.0011 |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.695  |  0.2508 | 0.016  | 0.4972 |      0.5022 |             0.0171 |                 0.6944 |            -0.5088 |          -0.9866 |          0.0417 |          0.2044 |    0.0191 |      -0.0953 |    0.0004 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6983 |  0.251  | 0.022  | 0.494  |      0.5022 |             0.0356 |                 0.6976 |            -0.3485 |          -1.3945 |          0.0937 |          0.2068 |    0.0019 |      -0.1421 |    0      |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6971 |  0.2512 | 0.0196 | 0.4966 |      0.5022 |             0.0236 |                 0.6949 |            -0.4197 |          -1.3961 |          0.1002 |          0.2601 |    0.0015 |      -0.1626 |    0      |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                    |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:--------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                             | -2.4165 |        0.9922 |          -0.0009 | False          |      nan |            nan |     0.9945 |
| H3a          | logit    | rules_tech - hitai_full                                       |  0.6115 |        0.2704 |           0.0002 | False          |      nan |            nan |     0.6829 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                        |  0.4769 |        0.3167 |           0.0002 | False          |      nan |            nan |     0.6829 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                          |  1.1781 |        0.1194 |           0.0008 | False          |      nan |            nan |     0.4131 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  5.1382 |        0      |         nan      | False          |      nan |            nan |     0      |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates                | -0.0156 |        0.8506 |         nan      | False          |      nan |            nan |     0.9945 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)      |  0.0491 |        0.9609 |           0      | False          |      nan |            nan |     0.9945 |
| H1           | gbt      | rules_only - hitai_full (logloss)                             | -2.5229 |        0.9942 |          -0.0025 | False          |      nan |            nan |     0.9945 |
| H3a          | gbt      | rules_tech - hitai_full                                       | -0.0168 |        0.5067 |          -0      | False          |      nan |            nan |     0.8265 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                        |  1.1196 |        0.1314 |           0.0006 | False          |      nan |            nan |     0.4131 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                          | -1.7531 |        0.9602 |          -0.0014 | False          |      nan |            nan |     0.9945 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  5.2586 |        0      |         nan      | False          |      nan |            nan |     0      |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates                |  0.0061 |        0.3414 |         nan      | False          |      nan |            nan |     0.6829 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)      |  1.7529 |        0.0796 |           0.0014 | False          |      nan |            nan |     0.3503 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                             | -2.5416 |        0.9945 |          -0.0028 | True           |        1 |              1 |     0.9945 |
| H3a          | gbt_mono | rules_tech - hitai_full                                       |  0.4799 |        0.3156 |           0.0001 | True           |        1 |              1 |     0.6829 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                        | -0.4772 |        0.6834 |          -0.0001 | True           |        1 |              1 |     0.9396 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                          | -0.1247 |        0.5496 |          -0.0001 | True           |        1 |              1 |     0.8265 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  4.5844 |        0      |         nan      | False          |      nan |            nan |     0      |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates                | -0.0024 |        0.5635 |         nan      | True           |        1 |              1 |     0.8265 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)      |  0.7531 |        0.4514 |           0.0002 | False          |      nan |            nan |     0.8265 |
| H4b          | tagger   | corr(tag,fwd) original=-0.0076 vs perturbed-context (want ~0) | -0.0093 |        0.0518 |           0.0017 | False          |      nan |            nan |     0.2848 |

## Reality check / SPA vs rules_only: RC p=0.943, SPA p=0.427

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6936 |  0.2502 | 0.0156 | 0.5    |      0.5015 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 10896 |    0.6934 |  0.2501 | 0.0167 | 0.5028 |      0.5015 |           0.0752 |    0.5402 |
| hitai_full|pit|gbt_mono      | 10896 |    0.693  |  0.2499 | 0.0161 | 0.5177 |      0.5015 |          -0.3448 |    0.3225 |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6932 |  0.25   | 0.0172 | 0.5153 |      0.5015 |          -1.1176 |    0.0671 |
