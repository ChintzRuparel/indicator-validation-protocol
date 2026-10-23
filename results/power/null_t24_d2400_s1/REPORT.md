# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6939 |  0.2504 | 0.0125 | 0.5006 |      0.4969 |             0.0102 |                 0.6934 |            -0.1024 |          -1.1573 |          0.1212 |          0.2776 |    0.0081 |      -0.158  |       nan |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6938 |  0.2503 | 0.0111 | 0.4993 |      0.4969 |             0.0118 |                 0.6937 |            -0.0065 |          -1.0498 |          0.1049 |          0.1883 |    0.015  |      -0.1282 |       nan |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6934 |  0.2501 | 0.0116 | 0.4954 |      0.4969 |             0.0059 |                 0.6932 |             0      |           0      |          0      |          0      |  nan      |       0      |       nan |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6949 |  0.2505 | 0.0175 | 0.4961 |      0.4969 |             0.0159 |                 0.6942 |             0.1242 |          -1.0227 |          0.1149 |          0.1886 |    0.0168 |      -0.1502 |       nan |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6946 |  0.2506 | 0.0123 | 0.4952 |      0.4969 |             0.0272 |                 0.6973 |            -1.1117 |          -2.4622 |          0.1235 |          0.135  |    0      |      -0.2535 |       nan |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6961 |  0.2508 | 0.0201 | 0.4929 |      0.4969 |             0.0193 |                 0.6952 |            -0.6321 |          -1.8909 |          0.1075 |          0.1138 |    0      |      -0.1815 |       nan |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.695  |  0.2509 | 0.0202 | 0.4929 |      0.4969 |             0.0153 |                 0.6941 |            -0.3396 |          -1.4302 |          0.1588 |          0.4072 |    0.0015 |      -0.2375 |       nan |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6949 |  0.2508 | 0.0156 | 0.4916 |      0.4969 |             0.0282 |                 0.6972 |            -1.2814 |          -2.5973 |          0.0932 |          0.0881 |    0      |      -0.203  |       nan |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6961 |  0.2508 | 0.0201 | 0.4929 |      0.4969 |             0.0193 |                 0.6952 |            -0.6321 |          -1.8909 |          0.1075 |          0.1138 |    0      |      -0.1815 |       nan |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6956 |  0.2508 | 0.0174 | 0.493  |      0.4969 |             0.02   |                 0.6945 |            -0.132  |          -1.3091 |          0.1274 |          0.246  |    0.0035 |      -0.1635 |       nan |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6949 |  0.2508 | 0.0158 | 0.4933 |      0.4969 |             0.0287 |                 0.6973 |            -1.3659 |          -2.6343 |          0.1162 |          0.127  |    0      |      -0.2638 |       nan |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6955 |  0.2507 | 0.0181 | 0.4952 |      0.4969 |             0.0191 |                 0.6951 |            -0.3924 |          -1.7802 |          0.1299 |          0.1559 |    0      |      -0.1996 |       nan |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6954 |  0.2508 | 0.0206 | 0.4913 |      0.4969 |             0.0154 |                 0.6942 |            -0.6255 |          -1.9176 |          0.1778 |          0.3572 |    0      |      -0.3041 |       nan |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6945 |  0.2507 | 0.0145 | 0.4931 |      0.4969 |             0.0305 |                 0.6972 |            -1.1235 |          -2.5437 |          0.1238 |          0.1348 |    0      |      -0.2451 |       nan |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6954 |  0.2507 | 0.0191 | 0.4928 |      0.4969 |             0.0208 |                 0.6952 |            -0.702  |          -1.8689 |          0.094  |          0.0958 |    0      |      -0.1669 |       nan |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6974 |  0.251  | 0.0192 | 0.4911 |      0.4969 |             0.0167 |                 0.6943 |             0.1657 |          -0.8498 |          0.1078 |          0.2145 |    0.0375 |      -0.1141 |       nan |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6947 |  0.2507 | 0.0126 | 0.4958 |      0.4969 |             0.0289 |                 0.697  |            -0.9838 |          -2.597  |          0.1522 |          0.1547 |    0      |      -0.274  |       nan |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6947 |  0.2507 | 0.0168 | 0.4926 |      0.4969 |             0.0214 |                 0.6951 |            -0.7484 |          -2.1951 |          0.1519 |          0.1922 |    0      |      -0.2689 |       nan |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6945 |  0.2505 | 0.0122 | 0.4946 |      0.4969 |             0.021  |                 0.6945 |            -0.6881 |          -2.3456 |          0.1884 |          0.2398 |    0      |      -0.3103 |       nan |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6949 |  0.2509 | 0.0171 | 0.4901 |      0.4969 |             0.0285 |                 0.6975 |            -1.3145 |          -2.4965 |          0.0841 |          0.095  |    0      |      -0.1958 |       nan |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6952 |  0.2507 | 0.019  | 0.4929 |      0.4969 |             0.0194 |                 0.6951 |            -0.2225 |          -1.7097 |          0.1474 |          0.1763 |    0.0001 |      -0.1931 |       nan |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                    |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:--------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                             | -2.3878 |        0.9915 |          -0.0017 | False          |      nan |            nan |     0.9986 |
| H3a          | logit    | rules_tech - hitai_full                                       | -0.9669 |        0.8332 |          -0.0007 | False          |      nan |            nan |     0.9986 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                        | -0.2254 |        0.5892 |          -0.0002 | False          |      nan |            nan |     0.9986 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                          |  1.01   |        0.1563 |           0.0017 | False          |      nan |            nan |     0.6875 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  4.2341 |        0      |         nan      | False          |      nan |            nan |     0.0005 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates                | -0.0048 |        0.624  |         nan      | False          |      nan |            nan |     0.9986 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)      | -1.7584 |        0.0787 |          -0.0011 | False          |      nan |            nan |     0.4327 |
| H1           | gbt      | rules_only - hitai_full (logloss)                             | -2.2905 |        0.989  |          -0.0011 | False          |      nan |            nan |     0.9986 |
| H3a          | gbt      | rules_tech - hitai_full                                       | -0.0599 |        0.5239 |          -0      | False          |      nan |            nan |     0.9986 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                        | -1.4619 |        0.9281 |          -0.0004 | False          |      nan |            nan |     0.9986 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                          | -1.1952 |        0.884  |          -0.0002 | False          |      nan |            nan |     0.9986 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  3.9342 |        0.0001 |         nan      | False          |      nan |            nan |     0.0009 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates                | -0.0319 |        0.9829 |         nan      | False          |      nan |            nan |     0.9986 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)      |  0.0017 |        0.9986 |           0      | False          |      nan |            nan |     0.9986 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                             | -2.2773 |        0.9886 |          -0.0021 | True           |        1 |              1 |     0.9986 |
| H3a          | gbt_mono | rules_tech - hitai_full                                       |  0.6138 |        0.2697 |           0.0006 | True           |        1 |              1 |     0.9888 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                        | -0.2532 |        0.6    |          -0.0002 | True           |        1 |              1 |     0.9986 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                          | -0.9687 |        0.8337 |          -0.0008 | True           |        1 |              1 |     0.9986 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  3.817  |        0.0001 |         nan      | False          |      nan |            nan |     0.001  |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates                | -0.0093 |        0.7323 |         nan      | True           |        1 |              1 |     0.9986 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)      | -0.537  |        0.5913 |          -0.0003 | False          |      nan |            nan |     0.9986 |
| H4b          | tagger   | corr(tag,fwd) original=-0.0051 vs perturbed-context (want ~0) |  0.0033 |        0.4944 |          -0.0084 | False          |      nan |            nan |     0.9986 |

## Reality check / SPA vs rules_only: RC p=1.000, SPA p=1.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6932 |  0.25   | 0.0033 | 0.5    |      0.5027 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 10896 |    0.6937 |  0.2502 | 0.0098 | 0.4929 |      0.5027 |          -1.6829 |    0.0098 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6938 |  0.2503 | 0.0057 | 0.4935 |      0.5027 |          -2.4717 |    0.0004 |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6939 |  0.2504 | 0.0076 | 0.4913 |      0.5027 |          -2.5332 |    0.0003 |
