# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.694  |  0.2504 | 0.0156 | 0.4992 |      0.5024 |             0.0142 |                 0.6935 |            -0.5378 |          -1.7813 |          0.1349 |          0.252  |    0.0001 |      -0.2175 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6937 |  0.2503 | 0.0156 | 0.4971 |      0.5024 |             0.0141 |                 0.6935 |            -1.0452 |          -2.2636 |          0.1124 |          0.1619 |    0      |      -0.2367 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6932 |  0.2501 | 0.0072 | 0.5019 |      0.5024 |             0.0137 |                 0.6935 |             0.5802 |          -1.1577 |          0.1054 |          0.0658 |    0.007  |      -0.0892 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6965 |  0.2502 | 0.0063 | 0.5181 |      0.5024 |             0.015  |                 0.6931 |             1.1337 |           0.4051 |          0.1046 |          0.385  |    0.8018 |      -0.0501 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6943 |  0.2501 | 0.0067 | 0.5088 |      0.5024 |             0.031  |                 0.6957 |             0.5092 |          -0.9979 |          0.133  |          0.1501 |    0.0179 |      -0.113  |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6949 |  0.2504 | 0.0045 | 0.5105 |      0.5024 |             0.0171 |                 0.694  |             0.551  |          -0.9521 |          0.142  |          0.1846 |    0.0234 |      -0.1302 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6929 |  0.2498 | 0.0082 | 0.5189 |      0.5024 |             0.0149 |                 0.693  |             1.3257 |           0.3963 |          0.1455 |          0.4647 |    0.7966 |      -0.0681 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6946 |  0.2502 | 0.0046 | 0.5081 |      0.5024 |             0.0319 |                 0.6957 |             0.435  |          -1.3412 |          0.1711 |          0.1881 |    0.0024 |      -0.146  |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6951 |  0.2505 | 0.0045 | 0.5093 |      0.5024 |             0.0166 |                 0.694  |             0.5165 |          -1.0315 |          0.1321 |          0.1446 |    0.0152 |      -0.1281 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6818 |  0.2443 | 0.0073 | 0.5869 |      0.5024 |             0.0164 |                 0.6817 |            10.6928 |           7.7303 |          0.5582 |          0.819  |    1      |      -0.0141 |    0.9298 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.686  |  0.2454 | 0.0045 | 0.581  |      0.5024 |             0.0204 |                 0.6838 |             9.1894 |           6.1824 |          0.5799 |          0.8516 |    1      |      -0.0179 |    0.0475 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6848 |  0.2447 | 0.0074 | 0.5863 |      0.5024 |             0.0162 |                 0.6821 |            10.1493 |           7.2343 |          0.5512 |          0.8037 |    1      |      -0.0257 |    0.6917 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.694  |  0.2501 | 0.0049 | 0.521  |      0.5024 |             0.0149 |                 0.6929 |             1.0368 |          -0.4498 |          0.2162 |          0.3981 |    0.1747 |      -0.1253 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6943 |  0.25   | 0.0044 | 0.5122 |      0.5024 |             0.0297 |                 0.6959 |             0.4212 |          -1.0164 |          0.1155 |          0.1319 |    0.0161 |      -0.1032 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6956 |  0.2505 | 0.0073 | 0.5088 |      0.5024 |             0.0162 |                 0.694  |             0.3674 |          -1.1799 |          0.1502 |          0.1971 |    0.0069 |      -0.1505 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6994 |  0.2505 | 0.0054 | 0.5204 |      0.5024 |             0.015  |                 0.6929 |             1.6409 |           0.0974 |          0.2411 |          0.474  |    0.5807 |      -0.0572 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6951 |  0.2503 | 0.0044 | 0.5111 |      0.5024 |             0.0331 |                 0.6958 |             0.4354 |          -1.5302 |          0.2027 |          0.2159 |    0.0006 |      -0.1939 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.695  |  0.2504 | 0.0068 | 0.5118 |      0.5024 |             0.017  |                 0.6939 |             0.815  |          -0.9943 |          0.2011 |          0.252  |    0.0186 |      -0.1563 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6849 |  0.2448 | 0.0103 | 0.5846 |      0.5024 |             0.0154 |                 0.682  |             9.9763 |           7.0406 |          0.5646 |          0.8249 |    1      |      -0.0231 |    0.5402 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6844 |  0.2454 | 0.0085 | 0.5815 |      0.5024 |             0.0173 |                 0.6835 |             9.1534 |           6.1399 |          0.5751 |          0.8278 |    1      |      -0.0246 |    0.0446 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6846 |  0.245  | 0.0125 | 0.5855 |      0.5024 |             0.0154 |                 0.6819 |             9.2795 |           6.3783 |          0.5689 |          0.8502 |    1      |      -0.0275 |    0.1116 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  8.5939 |        0      |           0.0122 | False          |      nan |            nan |     0      |
| H3a          | logit    | rules_tech - hitai_full                                      |  7.9421 |        0      |           0.0111 | False          |      nan |            nan |     0      |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  8.2439 |        0      |           0.0121 | False          |      nan |            nan |     0      |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  6.9118 |        0      |           0.0175 | False          |      nan |            nan |     0      |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.4835 |        0.1379 |         nan      | False          |      nan |            nan |     0.1517 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0743 |        0      |         nan      | False          |      nan |            nan |     0      |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  2.4711 |        0.0135 |           0.003  | False          |      nan |            nan |     0.0174 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  4.9661 |        0      |           0.0076 | False          |      nan |            nan |     0      |
| H3a          | gbt      | rules_tech - hitai_full                                      |  5.4647 |        0      |           0.0085 | False          |      nan |            nan |     0      |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  5.2992 |        0      |           0.0083 | False          |      nan |            nan |     0      |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  5.9144 |        0      |           0.0091 | False          |      nan |            nan |     0      |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.4782 |        0.0132 |         nan      | False          |      nan |            nan |     0.0174 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0619 |        0      |         nan      | False          |      nan |            nan |     0      |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.6448 |        0.1    |          -0.0016 | False          |      nan |            nan |     0.1158 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  5.0397 |        0      |           0.0084 | True           |        0 |              0 |     0      |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  6.2603 |        0      |           0.0103 | True           |        0 |              0 |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  6.0556 |        0      |           0.0107 | True           |        0 |              0 |     0      |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  6.2274 |        0      |           0.0101 | True           |        0 |              0 |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.6885 |        0.0913 |         nan      | False          |      nan |            nan |     0.1116 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0879 |        0      |         nan      | True           |        0 |              0 |     0      |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.2243 |        0.8225 |          -0.0002 | False          |      nan |            nan |     0.8225 |
| H4b          | tagger   | corr(tag,fwd) original=0.1729 vs perturbed-context (want ~0) | -0.0043 |        0.3707 |           0.1771 | False          |      nan |            nan |     0.3883 |

## Reality check / SPA vs rules_only: RC p=0.000, SPA p=0.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6933 |  0.2501 | 0.0037 | 0.5021 |      0.5029 |          -2.2715 |    0.001  |
| rules_tech|pit|gbt_mono      | 10896 |    0.6967 |  0.2513 | 0.0312 | 0.4902 |      0.5029 |          -2.5498 |    0.0003 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6901 |  0.247  | 0.0181 | 0.5732 |      0.5029 |           5.2172 |    1      |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6969 |  0.2512 | 0.027  | 0.4928 |      0.5029 |          -2.6349 |    0.0001 |
