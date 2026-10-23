# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6939 |  0.2502 | 0.0103 | 0.5049 |      0.5027 |             0.0075 |                 0.6934 |             0.4086 |          -0.2906 |          0.0481 |          0.1213 |    0.272  |      -0.047  |    0.0063 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6939 |  0.2503 | 0.0128 | 0.5012 |      0.5027 |             0.0074 |                 0.6934 |             0.3379 |          -0.7788 |          0.0917 |          0.1477 |    0.0511 |      -0.0898 |    0.0002 |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6934 |  0.2501 | 0.0127 | 0.5051 |      0.5027 |             0.0052 |                 0.6931 |             0.4479 |          -0.6382 |          0.0844 |          0.1498 |    0.0921 |      -0.0726 |    0.0007 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.695  |  0.2504 | 0.0136 | 0.4963 |      0.5027 |             0.018  |                 0.6941 |            -0.2082 |          -0.7772 |          0.0496 |          0.1838 |    0.0506 |      -0.084  |    0.0002 |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6955 |  0.2506 | 0.0197 | 0.4969 |      0.5027 |             0.0364 |                 0.6969 |             0.1386 |          -1.7395 |          0.17   |          0.202  |    0.0001 |      -0.1851 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6965 |  0.2507 | 0.0112 | 0.5026 |      0.5027 |             0.0203 |                 0.6947 |            -0.283  |          -1.7436 |          0.1503 |          0.2367 |    0.0001 |      -0.2052 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6941 |  0.2502 | 0.0116 | 0.4999 |      0.5027 |             0.0198 |                 0.6941 |            -0.2049 |          -1.0131 |          0.0532 |          0.0739 |    0.0165 |      -0.0809 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6968 |  0.2507 | 0.017  | 0.4982 |      0.5027 |             0.0356 |                 0.6969 |             0.3537 |          -1.468  |          0.1753 |          0.219  |    0.001  |      -0.1644 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6967 |  0.2507 | 0.0112 | 0.5027 |      0.5027 |             0.0201 |                 0.6947 |            -0.347  |          -1.7583 |          0.1441 |          0.2298 |    0.0001 |      -0.2005 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.697  |  0.2506 | 0.0119 | 0.4974 |      0.5027 |             0.0229 |                 0.6941 |            -0.1076 |          -1.2167 |          0.0797 |          0.0975 |    0.0049 |      -0.1095 |    0      |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.696  |  0.2506 | 0.0194 | 0.4977 |      0.5027 |             0.0337 |                 0.6966 |             0.3437 |          -1.5259 |          0.1663 |          0.181  |    0.0007 |      -0.1532 |    0      |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6976 |  0.2508 | 0.011  | 0.5028 |      0.5027 |             0.0186 |                 0.6947 |            -0.3958 |          -1.708  |          0.1251 |          0.2194 |    0.0002 |      -0.1825 |    0      |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6973 |  0.2506 | 0.0113 | 0.501  |      0.5027 |             0.0189 |                 0.6944 |             0.0582 |          -1.2695 |          0.0845 |          0.078  |    0.0039 |      -0.0948 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6955 |  0.2506 | 0.0189 | 0.4972 |      0.5027 |             0.0339 |                 0.6968 |             0.0221 |          -1.835  |          0.1645 |          0.1788 |    0.0001 |      -0.1802 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6966 |  0.2507 | 0.0156 | 0.4994 |      0.5027 |             0.0239 |                 0.6948 |            -0.0654 |          -1.5696 |          0.1294 |          0.1666 |    0.0006 |      -0.1562 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6955 |  0.2507 | 0.0158 | 0.4972 |      0.5027 |             0.0188 |                 0.6945 |            -0.3467 |          -1.7833 |          0.1428 |          0.2262 |    0.0001 |      -0.1954 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6966 |  0.2507 | 0.0168 | 0.4984 |      0.5027 |             0.0353 |                 0.697  |             0.3357 |          -1.4475 |          0.1873 |          0.261  |    0.0014 |      -0.1708 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6953 |  0.2506 | 0.0156 | 0.4989 |      0.5027 |             0.0226 |                 0.695  |            -0.107  |          -1.2604 |          0.1064 |          0.2117 |    0.0046 |      -0.1335 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6983 |  0.2506 | 0.0123 | 0.5005 |      0.5027 |             0.0199 |                 0.694  |            -0.0568 |          -0.8281 |          0.0403 |          0.0468 |    0.0426 |      -0.0604 |    0.0002 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6955 |  0.2505 | 0.016  | 0.4969 |      0.5027 |             0.0343 |                 0.6966 |            -0.158  |          -1.9737 |          0.1601 |          0.1822 |    0      |      -0.1996 |    0      |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6972 |  0.2508 | 0.0102 | 0.5029 |      0.5027 |             0.0214 |                 0.6948 |            -0.2343 |          -1.8171 |          0.1641 |          0.2472 |    0.0001 |      -0.2133 |    0      |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                    |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:--------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                             | -2.3845 |        0.9914 |          -0.0031 | False          |      nan |            nan |     0.9993 |
| H3a          | logit    | rules_tech - hitai_full                                       | -2.757  |        0.9971 |          -0.003  | False          |      nan |            nan |     0.9993 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                        |  0.2097 |        0.417  |           0.0003 | False          |      nan |            nan |     0.8024 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                          | -1.2136 |        0.8875 |          -0.0015 | False          |      nan |            nan |     0.9993 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  3.0585 |        0.0022 |         nan      | False          |      nan |            nan |     0.0163 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates                |  0.0114 |        0.2246 |         nan      | False          |      nan |            nan |     0.7115 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)      |  1.2782 |        0.2012 |           0.0013 | False          |      nan |            nan |     0.7115 |
| H1           | gbt      | rules_only - hitai_full (logloss)                             | -2.3794 |        0.9913 |          -0.0021 | False          |      nan |            nan |     0.9993 |
| H3a          | gbt      | rules_tech - hitai_full                                       |  0.9593 |        0.1687 |           0.0008 | False          |      nan |            nan |     0.7115 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                        | -0.8205 |        0.794  |          -0.0005 | False          |      nan |            nan |     0.9993 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                          |  0.5232 |        0.3004 |           0.0006 | False          |      nan |            nan |     0.8024 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  6.1407 |        0      |         nan      | False          |      nan |            nan |     0      |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates                |  0.0027 |        0.4286 |         nan      | False          |      nan |            nan |     0.8024 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)      | -0.8533 |        0.3935 |          -0.0005 | False          |      nan |            nan |     0.8024 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                             | -3.1887 |        0.9993 |          -0.0042 | True           |        1 |              1 |     0.9993 |
| H3a          | gbt_mono | rules_tech - hitai_full                                       | -2.2778 |        0.9886 |          -0.0009 | True           |        1 |              1 |     0.9993 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                        | -1.3367 |        0.9093 |          -0.001  | True           |        1 |              1 |     0.9993 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                          | -1.8458 |        0.9675 |          -0.0022 | True           |        1 |              1 |     0.9993 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  5.0226 |        0      |         nan      | False          |      nan |            nan |     0      |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates                | -0.0056 |        0.6439 |         nan      | True           |        1 |              1 |     0.9993 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)      | -0.7761 |        0.4377 |          -0.0003 | False          |      nan |            nan |     0.8024 |
| H4b          | tagger   | corr(tag,fwd) original=-0.0070 vs perturbed-context (want ~0) | -0.0058 |        0.2264 |          -0.0012 | False          |      nan |            nan |     0.7115 |

## Reality check / SPA vs rules_only: RC p=1.000, SPA p=1.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6936 |  0.2502 | 0.0056 | 0.5033 |      0.5058 |          -0.2646 |    0.3605 |
| rules_tech|pit|gbt_mono      | 10896 |    0.6934 |  0.2501 | 0.0033 | 0.4988 |      0.5058 |           0.1659 |    0.5876 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6934 |  0.2501 | 0.0034 | 0.4993 |      0.5058 |          -1.1889 |    0.0242 |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6954 |  0.2503 | 0.0032 | 0.4984 |      0.5058 |          -1.4028 |    0.0025 |
