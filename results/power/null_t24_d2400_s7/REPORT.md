# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.694  |  0.2504 | 0.0141 | 0.5056 |      0.5004 |             0.0055 |                 0.6932 |             0.6391 |           0.0201 |          0.0765 |          0.2911 |    0.5168 |      -0.0663 |    0.0116 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6958 |  0.2507 | 0.0184 | 0.5021 |      0.5004 |             0.0107 |                 0.6937 |             0.0296 |          -0.6685 |          0.0697 |          0.2199 |    0.0811 |      -0.0969 |    0.0001 |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6933 |  0.2501 | 0.0086 | 0.5047 |      0.5004 |             0.0051 |                 0.6933 |             0.1908 |          -0.7003 |          0.0232 |          0.0137 |    0.0661 |      -0.0259 |    0.0001 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6978 |  0.2508 | 0.0132 | 0.5066 |      0.5004 |             0.0093 |                 0.6933 |             1.3326 |           0.0952 |          0.1615 |          0.3233 |    0.5788 |      -0.0683 |    0.0174 |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6951 |  0.2505 | 0.0122 | 0.5008 |      0.5004 |             0.0301 |                 0.6964 |            -0.0626 |          -1.8327 |          0.1645 |          0.1831 |    0.0001 |      -0.1953 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6933 |  0.25   | 0.0079 | 0.5121 |      0.5004 |             0.0185 |                 0.6938 |             0.6638 |          -0.6436 |          0.0954 |          0.1031 |    0.0894 |      -0.0584 |    0.0001 |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6963 |  0.2507 | 0.0128 | 0.5095 |      0.5004 |             0.0067 |                 0.6933 |             1.0355 |          -0.482  |          0.2139 |          0.3814 |    0.1561 |      -0.114  |    0.0004 |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6956 |  0.2504 | 0.0103 | 0.5054 |      0.5004 |             0.0296 |                 0.6964 |             0.2054 |          -1.5645 |          0.1792 |          0.2123 |    0.0005 |      -0.1833 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6932 |  0.25   | 0.0079 | 0.5134 |      0.5004 |             0.0182 |                 0.6937 |             0.8224 |          -0.4889 |          0.092  |          0.0973 |    0.1537 |      -0.0424 |    0.0004 |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.696  |  0.251  | 0.0104 | 0.5107 |      0.5004 |             0.0118 |                 0.6932 |             0.8024 |          -0.7055 |          0.1996 |          0.3174 |    0.0697 |      -0.1144 |    0.0001 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6946 |  0.2504 | 0.0135 | 0.5028 |      0.5004 |             0.0298 |                 0.6961 |             0.1099 |          -1.6191 |          0.1552 |          0.1741 |    0.0004 |      -0.1602 |    0      |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6932 |  0.2499 | 0.0079 | 0.5128 |      0.5004 |             0.0178 |                 0.6937 |             0.634  |          -0.7263 |          0.1061 |          0.1191 |    0.0643 |      -0.0647 |    0.0001 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6958 |  0.2509 | 0.0133 | 0.5053 |      0.5004 |             0.0102 |                 0.6934 |             0.2385 |          -1.2777 |          0.173  |          0.2404 |    0.0037 |      -0.1644 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6944 |  0.2504 | 0.014  | 0.504  |      0.5004 |             0.0295 |                 0.6962 |             0.2731 |          -1.5378 |          0.1754 |          0.1933 |    0.0005 |      -0.1675 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6931 |  0.2499 | 0.0077 | 0.5131 |      0.5004 |             0.018  |                 0.6937 |             0.6272 |          -0.62   |          0.0839 |          0.0835 |    0.0972 |      -0.0483 |    0.0002 |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6965 |  0.2508 | 0.012  | 0.5094 |      0.5004 |             0.0096 |                 0.6934 |             0.7158 |          -0.8977 |          0.2133 |          0.3239 |    0.0291 |      -0.1722 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6949 |  0.2503 | 0.0126 | 0.5033 |      0.5004 |             0.0293 |                 0.6961 |             0.413  |          -1.5077 |          0.1905 |          0.1901 |    0.0006 |      -0.1821 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6946 |  0.2502 | 0.0079 | 0.5098 |      0.5004 |             0.0204 |                 0.6937 |            -0.0846 |          -1.325  |          0.1159 |          0.1441 |    0.0017 |      -0.1376 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6967 |  0.251  | 0.0135 | 0.5097 |      0.5004 |             0.0112 |                 0.6932 |             0.877  |          -0.94   |          0.2183 |          0.2983 |    0.024  |      -0.1481 |    0      |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6942 |  0.2503 | 0.0098 | 0.5048 |      0.5004 |             0.028  |                 0.6963 |            -0.1394 |          -2.0171 |          0.1808 |          0.1919 |    0      |      -0.2142 |    0      |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6938 |  0.2501 | 0.0079 | 0.5098 |      0.5004 |             0.018  |                 0.6938 |             0.5272 |          -0.7292 |          0.0883 |          0.0933 |    0.0629 |      -0.0565 |    0.0001 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -2.1398 |        0.9838 |          -0.002  | False          | nan      |       nan      |     0.9838 |
| H3a          | logit    | rules_tech - hitai_full                                      |  0.2924 |        0.385  |           0.0003 | False          | nan      |       nan      |     0.5647 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       | -0.308  |        0.621  |          -0.0002 | False          | nan      |       nan      |     0.719  |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  0.5644 |        0.2862 |           0.0005 | False          | nan      |       nan      |     0.5481 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.5697 |        0.0004 |         nan      | False          | nan      |       nan      |     0.0079 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               | -0.0065 |        0.6678 |         nan      | False          | nan      |       nan      |     0.7346 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.3125 |        0.1893 |           0.0007 | False          | nan      |       nan      |     0.5481 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  1.1035 |        0.1349 |           0.0012 | False          | nan      |       nan      |     0.4946 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  1.5806 |        0.057  |           0.001  | False          | nan      |       nan      |     0.3396 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       | -0.6128 |        0.73   |          -0.0002 | False          | nan      |       nan      |     0.7648 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  0.5066 |        0.3062 |           0.0004 | False          | nan      |       nan      |     0.5481 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.8682 |        0.0617 |         nan      | False          | nan      |       nan      |     0.3396 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0123 |        0.2061 |         nan      | False          | nan      |       nan      |     0.5481 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.5337 |        0.5935 |          -0.0004 | False          | nan      |       nan      |     0.719  |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  0.3348 |        0.3689 |           0.0002 | True           |   1      |         1      |     0.5647 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  0.5755 |        0.2825 |           0.0001 | True           |   1      |         1      |     0.5481 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       | -0.1521 |        0.5604 |          -0      | True           |   1      |         1      |     0.719  |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  2.1984 |        0.014  |           0.0014 | True           |   0.0698 |         0.0698 |     0.1536 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.1717 |        0.2413 |         nan      | False          | nan      |       nan      |     0.5481 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0069 |        0.3239 |         nan      | True           |   1      |         1      |     0.5481 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.6908 |        0.0909 |           0.0006 | False          | nan      |       nan      |     0.3998 |
| H4b          | tagger   | corr(tag,fwd) original=0.0154 vs perturbed-context (want ~0) |  0.0024 |        0.6079 |           0.0129 | False          | nan      |       nan      |     0.719  |

## Reality check / SPA vs rules_only: RC p=0.943, SPA p=0.707

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6932 |  0.25   | 0.0049 | 0.499  |      0.4979 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 10896 |    0.6937 |  0.2503 | 0.0075 | 0.4985 |      0.4979 |          -1.3622 |    0.0358 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6936 |  0.2502 | 0.0038 | 0.4995 |      0.4979 |          -0.8098 |    0.1421 |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6936 |  0.2502 | 0.0078 | 0.4994 |      0.4979 |          -2.0604 |    0.0039 |
