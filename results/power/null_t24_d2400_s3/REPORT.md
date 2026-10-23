# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6941 |  0.2505 | 0.0196 | 0.4987 |      0.5033 |             0.0033 |                 0.6933 |             0.3586 |          -0.7414 |          0.1406 |          0.3477 |    0.0611 |      -0.1139 |    0.0002 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6941 |  0.2505 | 0.019  | 0.4983 |      0.5033 |             0.0076 |                 0.6935 |             0.208  |          -0.7335 |          0.1269 |          0.4058 |    0.0626 |      -0.114  |    0.0002 |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6941 |  0.2505 | 0.0164 | 0.5011 |      0.5033 |             0.0112 |                 0.6933 |             0.4188 |          -0.704  |          0.1524 |          0.4117 |    0.0709 |      -0.1183 |    0.0002 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6972 |  0.2508 | 0.019  | 0.5005 |      0.5033 |             0.0095 |                 0.6933 |             0.0751 |          -0.4223 |          0.0628 |          0.2996 |    0.189  |      -0.0987 |    0.0016 |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6962 |  0.2507 | 0.0141 | 0.5019 |      0.5033 |             0.0261 |                 0.6954 |             0.1531 |          -1.0162 |          0.1302 |          0.2576 |    0.0177 |      -0.137  |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6968 |  0.251  | 0.0204 | 0.5004 |      0.5033 |             0.0149 |                 0.694  |            -0.0574 |          -1.4248 |          0.1825 |          0.3729 |    0.0015 |      -0.2363 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6974 |  0.2512 | 0.0234 | 0.4983 |      0.5033 |             0.014  |                 0.6935 |             0.3952 |          -0.4266 |          0.1124 |          0.351  |    0.1863 |      -0.1134 |    0.0016 |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6973 |  0.2509 | 0.013  | 0.5043 |      0.5033 |             0.0264 |                 0.6954 |             0.0856 |          -0.8792 |          0.1083 |          0.2619 |    0.0339 |      -0.1209 |    0.0001 |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6966 |  0.2509 | 0.0214 | 0.499  |      0.5033 |             0.0139 |                 0.694  |            -0.1904 |          -1.6201 |          0.191  |          0.3665 |    0.0004 |      -0.2651 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.697  |  0.251  | 0.0239 | 0.5028 |      0.5033 |             0.012  |                 0.6934 |             0.4203 |          -0.8127 |          0.1697 |          0.3717 |    0.0446 |      -0.1545 |    0.0001 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6962 |  0.2508 | 0.0174 | 0.5053 |      0.5033 |             0.0269 |                 0.6956 |            -0.2832 |          -1.649  |          0.1933 |          0.4109 |    0.0003 |      -0.2674 |    0      |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6971 |  0.251  | 0.0216 | 0.4975 |      0.5033 |             0.0142 |                 0.694  |            -0.1904 |          -1.6338 |          0.1967 |          0.4027 |    0.0003 |      -0.2569 |    0      |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6976 |  0.2511 | 0.0254 | 0.4961 |      0.5033 |             0.0147 |                 0.6939 |             0.2284 |          -0.877  |          0.1509 |          0.3488 |    0.0335 |      -0.162  |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6958 |  0.2508 | 0.0154 | 0.5028 |      0.5033 |             0.0254 |                 0.6954 |            -0.185  |          -1.5716 |          0.1773 |          0.3262 |    0.0005 |      -0.2305 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6975 |  0.251  | 0.0207 | 0.5028 |      0.5033 |             0.0143 |                 0.6941 |             0.1899 |          -1.317  |          0.1982 |          0.3474 |    0.0031 |      -0.2204 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6968 |  0.2508 | 0.0182 | 0.4965 |      0.5033 |             0.0161 |                 0.6938 |             0.1521 |          -0.3993 |          0.0615 |          0.2452 |    0.2019 |      -0.0774 |    0.0019 |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6965 |  0.2506 | 0.0141 | 0.505  |      0.5033 |             0.025  |                 0.6955 |            -0.3148 |          -1.7462 |          0.2002 |          0.397  |    0.0001 |      -0.2916 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6962 |  0.251  | 0.0231 | 0.5006 |      0.5033 |             0.0141 |                 0.694  |            -0.3302 |          -1.9149 |          0.226  |          0.4201 |    0      |      -0.3176 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6967 |  0.2508 | 0.0216 | 0.5062 |      0.5033 |             0.0102 |                 0.6934 |             0.7768 |          -0.4558 |          0.1988 |          0.5069 |    0.1698 |      -0.1147 |    0.0012 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6972 |  0.2508 | 0.0143 | 0.5057 |      0.5033 |             0.0258 |                 0.6953 |            -0.1047 |          -1.8274 |          0.1653 |          0.1919 |    0.0001 |      -0.2069 |    0      |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6974 |  0.251  | 0.0234 | 0.5006 |      0.5033 |             0.0129 |                 0.6939 |             0.049  |          -1.241  |          0.1809 |          0.3915 |    0.0049 |      -0.2134 |    0      |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -2.5952 |        0.9953 |          -0.0029 | False          | nan      |       nan      |     0.9957 |
| H3a          | logit    | rules_tech - hitai_full                                      |  0.3344 |        0.369  |           0.0004 | False          | nan      |       nan      |     0.6706 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  0.438  |        0.3307 |           0.0005 | False          | nan      |       nan      |     0.6706 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         | -0.1698 |        0.5674 |          -0.0002 | False          | nan      |       nan      |     0.8916 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  5.4791 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0294 |        0.0253 |         nan      | False          | nan      |       nan      |     0.1394 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.3057 |        0.7598 |          -0.0003 | False          | nan      |       nan      |     0.9733 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -2.6259 |        0.9957 |          -0.0021 | False          | nan      |       nan      |     0.9957 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  1.3865 |        0.0828 |           0.0011 | False          | nan      |       nan      |     0.3583 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       | -0.8287 |        0.7964 |          -0.0005 | False          | nan      |       nan      |     0.9733 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  0.2631 |        0.3962 |           0.0002 | False          | nan      |       nan      |     0.6706 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.5023 |        0.0005 |         nan      | False          | nan      |       nan      |     0.0034 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0051 |        0.3681 |         nan      | False          | nan      |       nan      |     0.6706 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.1407 |        0.254  |           0.0009 | False          | nan      |       nan      |     0.6706 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -2.3227 |        0.9899 |          -0.003  | True           |   1      |         1      |     0.9957 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      | -1.0074 |        0.8431 |          -0.0005 | True           |   1      |         1      |     0.9763 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  0.4585 |        0.3233 |           0.0004 | True           |   1      |         1      |     0.6706 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         | -0.8008 |        0.7884 |          -0.0009 | True           |   1      |         1      |     0.9733 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.6589 |        0.0003 |         nan      | False          | nan      |       nan      |     0.0028 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0195 |        0.0977 |         nan      | True           |   0.4886 |         0.4886 |     0.3583 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.3611 |        0.718  |           0.0003 | False          | nan      |       nan      |     0.9733 |
| H4b          | tagger   | corr(tag,fwd) original=0.0022 vs perturbed-context (want ~0) |  0.0053 |        0.2703 |          -0.0031 | False          | nan      |       nan      |     0.6706 |

## Reality check / SPA vs rules_only: RC p=0.957, SPA p=1.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6928 |  0.2499 | 0.0136 | 0.5022 |      0.5132 |           1.4579 |    0.9926 |
| rules_tech|pit|gbt_mono      | 10896 |    0.6971 |  0.2512 | 0.0339 | 0.4908 |      0.5132 |          -2.4287 |    0.0006 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6979 |  0.251  | 0.0207 | 0.4968 |      0.5132 |          -1.768  |    0.0068 |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6965 |  0.251  | 0.0287 | 0.4917 |      0.5132 |          -1.9434 |    0.0047 |
