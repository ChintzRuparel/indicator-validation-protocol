# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6936 |  0.2502 | 0.0099 | 0.5004 |      0.5121 |             0.0079 |                 0.6933 |             0.5832 |           0.0316 |          0.0873 |          0.5743 |    0.5263 |      -0.0803 |    0.0229 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6933 |  0.2501 | 0.0109 | 0.5    |      0.5121 |             0.0125 |                 0.6936 |             0.3705 |          -0.1423 |          0.0813 |          0.5595 |    0.3832 |      -0.0823 |    0.0092 |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6933 |  0.2501 | 0.0088 | 0.5007 |      0.5121 |             0.011  |                 0.6932 |             0.7618 |           0.6489 |          0.0172 |          0.5346 |    0.9129 |      -0.0646 |    0.2391 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6961 |  0.2505 | 0.0135 | 0.5015 |      0.5121 |             0.0101 |                 0.6935 |             0.1164 |          -0.7195 |          0.1384 |          0.6615 |    0.066  |      -0.179  |    0.0002 |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6943 |  0.2504 | 0.0165 | 0.5075 |      0.5121 |             0.0303 |                 0.696  |             0.5073 |          -0.994  |          0.2487 |          0.5977 |    0.0199 |      -0.2448 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6956 |  0.2507 | 0.015  | 0.5082 |      0.5121 |             0.0141 |                 0.694  |             0.2076 |          -1.0005 |          0.1854 |          0.527  |    0.0186 |      -0.2136 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6942 |  0.2504 | 0.013  | 0.5006 |      0.5121 |             0.0105 |                 0.6936 |             0.0144 |          -0.8529 |          0.1318 |          0.5795 |    0.0376 |      -0.2008 |    0.0001 |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6948 |  0.2503 | 0.0156 | 0.5072 |      0.5121 |             0.0318 |                 0.6961 |             0.3529 |          -0.8624 |          0.2207 |          0.706  |    0.0367 |      -0.2677 |    0.0001 |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6956 |  0.2507 | 0.015  | 0.5082 |      0.5121 |             0.0141 |                 0.694  |             0.2076 |          -1.0005 |          0.1854 |          0.527  |    0.0186 |      -0.2136 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6946 |  0.2505 | 0.0125 | 0.4984 |      0.5121 |             0.014  |                 0.6938 |             0.5954 |          -0.4517 |          0.1675 |          0.6378 |    0.173  |      -0.1351 |    0.0013 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6954 |  0.2505 | 0.0171 | 0.5085 |      0.5121 |             0.0328 |                 0.6962 |             0.2563 |          -1.4083 |          0.2561 |          0.5526 |    0.0018 |      -0.2621 |    0      |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6949 |  0.2506 | 0.0141 | 0.5096 |      0.5121 |             0.0137 |                 0.694  |             0.6083 |          -0.7313 |          0.2103 |          0.5616 |    0.0638 |      -0.1705 |    0.0002 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6941 |  0.2503 | 0.0193 | 0.4997 |      0.5121 |             0.0104 |                 0.6937 |             0.2667 |          -0.6821 |          0.1488 |          0.6054 |    0.0772 |      -0.1682 |    0.0002 |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6947 |  0.2502 | 0.0174 | 0.5092 |      0.5121 |             0.0284 |                 0.6959 |             0.2651 |          -1.5626 |          0.3011 |          0.6019 |    0.0006 |      -0.3118 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6953 |  0.2507 | 0.0152 | 0.5084 |      0.5121 |             0.0153 |                 0.694  |             0.5608 |          -0.7469 |          0.2035 |          0.5445 |    0.0596 |      -0.1726 |    0.0001 |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6948 |  0.2506 | 0.013  | 0.4956 |      0.5121 |             0.0124 |                 0.6937 |             0.2602 |          -0.6118 |          0.1321 |          0.5704 |    0.1011 |      -0.1643 |    0.0004 |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6947 |  0.2503 | 0.018  | 0.5086 |      0.5121 |             0.031  |                 0.6958 |             0.0769 |          -1.478  |          0.2445 |          0.5773 |    0.0011 |      -0.296  |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6963 |  0.2508 | 0.0173 | 0.5083 |      0.5121 |             0.0141 |                 0.6939 |             0.4956 |          -0.8275 |          0.1985 |          0.5117 |    0.0425 |      -0.1725 |    0.0001 |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6942 |  0.2504 | 0.013  | 0.4997 |      0.5121 |             0.0155 |                 0.6938 |             0.2097 |          -0.8116 |          0.1734 |          0.6787 |    0.0448 |      -0.211  |    0.0001 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6933 |  0.2501 | 0.0157 | 0.5098 |      0.5121 |             0.0314 |                 0.696  |             0.499  |          -1.381  |          0.2896 |          0.5341 |    0.0021 |      -0.2567 |    0      |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6958 |  0.2507 | 0.0157 | 0.5086 |      0.5121 |             0.0144 |                 0.694  |             0.4894 |          -0.8555 |          0.2198 |          0.609  |    0.0373 |      -0.1973 |    0.0001 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                    |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:--------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                             | -1.6048 |        0.9457 |          -0.001  | False          | nan      |       nan      |     0.9851 |
| H3a          | logit    | rules_tech - hitai_full                                       | -0.6856 |        0.7535 |          -0.0004 | False          | nan      |       nan      |     0.9851 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                        | -0.77   |        0.7794 |          -0.0004 | False          | nan      |       nan      |     0.9851 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                          |  0.3024 |        0.3812 |           0.0002 | False          | nan      |       nan      |     0.7474 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  3.0308 |        0.0024 |         nan      | False          | nan      |       nan      |     0.0179 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates                | -0.0034 |        0.5901 |         nan      | False          | nan      |       nan      |     0.9274 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)      | -0.7649 |        0.4444 |          -0.0004 | False          | nan      |       nan      |     0.752  |
| H1           | gbt      | rules_only - hitai_full (logloss)                             | -1.9793 |        0.9761 |          -0.0021 | False          | nan      |       nan      |     0.9851 |
| H3a          | gbt      | rules_tech - hitai_full                                       | -1.5603 |        0.9407 |          -0.0006 | False          | nan      |       nan      |     0.9851 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                        | -1.2028 |        0.8855 |          -0.0007 | False          | nan      |       nan      |     0.9851 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                          | -1.3404 |        0.9099 |          -0.0007 | False          | nan      |       nan      |     0.9851 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  3.5361 |        0.0004 |         nan      | False          | nan      |       nan      |     0.0045 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates                |  0.0197 |        0.0958 |         nan      | False          | nan      |       nan      |     0.2636 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)      | -2.5754 |        0.01   |          -0.0021 | False          | nan      |       nan      |     0.0551 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                             | -2.172  |        0.9851 |          -0.0016 | True           |   0.9851 |         1      |     0.9851 |
| H3a          | gbt_mono | rules_tech - hitai_full                                       |  1.5349 |        0.0624 |           0.0008 | True           |   0.2927 |         0.312  |     0.2288 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                        |  0.8522 |        0.1971 |           0.0005 | True           |   0.3941 |         0.9853 |     0.4335 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                          |  1.5672 |        0.0585 |           0.0015 | True           |   0.2927 |         0.2927 |     0.2288 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  3.6654 |        0.0002 |         nan      | False          | nan      |       nan      |     0.0045 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates                |  0.0203 |        0.0892 |         nan      | True           |   0.2927 |         0.446  |     0.2636 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)      |  1.5563 |        0.1196 |           0.001  | False          | nan      |       nan      |     0.2925 |
| H4b          | tagger   | corr(tag,fwd) original=-0.0094 vs perturbed-context (want ~0) | -0.0039 |        0.4077 |          -0.0055 | False          | nan      |       nan      |     0.7474 |

## Reality check / SPA vs rules_only: RC p=0.997, SPA p=1.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6941 |  0.2505 | 0.0181 | 0.4979 |      0.5125 |          -0.7113 |    0.1619 |
| rules_tech|pit|gbt_mono      | 10896 |    0.6951 |  0.2509 | 0.0199 | 0.4953 |      0.5125 |          -0.7079 |    0.1686 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6947 |  0.2508 | 0.021  | 0.4968 |      0.5125 |          -1.9459 |    0.0029 |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6949 |  0.2509 | 0.0201 | 0.4961 |      0.5125 |          -1.7082 |    0.0078 |
