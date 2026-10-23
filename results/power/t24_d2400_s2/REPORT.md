# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6935 |  0.2502 | 0.0098 | 0.5087 |      0.4986 |             0.0162 |                 0.6935 |             0.7554 |           0.1538 |          0.0838 |          0.3997 |    0.6261 |      -0.0433 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6934 |  0.2501 | 0.0137 | 0.5104 |      0.4986 |             0.0154 |                 0.6936 |             0.4539 |          -0.2953 |          0.0777 |          0.2326 |    0.2681 |      -0.0528 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6936 |  0.2502 | 0.0143 | 0.5055 |      0.4986 |             0.0143 |                 0.6935 |             0.4935 |          -0.3725 |          0.1004 |          0.2607 |    0.2189 |      -0.0938 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6943 |  0.2502 | 0.0101 | 0.5106 |      0.4986 |             0.0154 |                 0.6937 |             1.4135 |           0.4808 |          0.1388 |          0.4233 |    0.8431 |      -0.0641 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6972 |  0.2507 | 0.0202 | 0.5066 |      0.4986 |             0.0359 |                 0.6973 |             0.5222 |          -0.5029 |          0.1402 |          0.3953 |    0.1472 |      -0.1301 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6949 |  0.2505 | 0.0116 | 0.5064 |      0.4986 |             0.023  |                 0.6947 |             0.5548 |          -0.4677 |          0.1272 |          0.3196 |    0.1643 |      -0.1146 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6944 |  0.2503 | 0.0157 | 0.5069 |      0.4986 |             0.0167 |                 0.6938 |             1.3768 |           0.4647 |          0.1288 |          0.3773 |    0.8346 |      -0.0618 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6972 |  0.2507 | 0.0202 | 0.5069 |      0.4986 |             0.0355 |                 0.6973 |             0.4244 |          -0.77   |          0.1757 |          0.4523 |    0.0543 |      -0.18   |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6949 |  0.2505 | 0.0116 | 0.5064 |      0.4986 |             0.023  |                 0.6947 |             0.5548 |          -0.4677 |          0.1272 |          0.3196 |    0.1643 |      -0.1146 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6834 |  0.2447 | 0.0104 | 0.5832 |      0.4986 |             0.0124 |                 0.6825 |            10.5103 |           7.7904 |          0.5416 |          0.8629 |    1      |      -0.0197 |    0.9274 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6857 |  0.2456 | 0.0078 | 0.5797 |      0.4986 |             0.0193 |                 0.6844 |             8.9739 |           6.3484 |          0.547  |          0.9035 |    1      |      -0.0225 |    0.0785 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6841 |  0.2447 | 0.0101 | 0.5847 |      0.4986 |             0.014  |                 0.6822 |            10.2259 |           7.5372 |          0.5296 |          0.854  |    1      |      -0.0196 |    0.8245 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.694  |  0.2503 | 0.013  | 0.5091 |      0.4986 |             0.0167 |                 0.6938 |             1.0877 |          -0.0968 |          0.172  |          0.3987 |    0.4199 |      -0.0871 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6959 |  0.2505 | 0.0178 | 0.5047 |      0.4986 |             0.033  |                 0.697  |             0.4795 |          -0.5631 |          0.1395 |          0.333  |    0.1203 |      -0.1474 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6941 |  0.2504 | 0.0112 | 0.5085 |      0.4986 |             0.0222 |                 0.6948 |             0.4969 |          -0.5494 |          0.1381 |          0.343  |    0.1255 |      -0.1268 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6951 |  0.2504 | 0.0159 | 0.5054 |      0.4986 |             0.0163 |                 0.694  |             0.5697 |          -0.6492 |          0.1753 |          0.4508 |    0.0887 |      -0.153  |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6947 |  0.2504 | 0.017  | 0.5073 |      0.4986 |             0.0309 |                 0.6971 |             0.4181 |          -0.9906 |          0.2186 |          0.4971 |    0.0195 |      -0.2362 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6944 |  0.2502 | 0.0109 | 0.5099 |      0.4986 |             0.021  |                 0.6947 |             0.7455 |          -0.3483 |          0.141  |          0.3397 |    0.2336 |      -0.1142 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6857 |  0.2452 | 0.0084 | 0.58   |      0.4986 |             0.0122 |                 0.6831 |            11.1244 |           8.3494 |          0.5421 |          0.837  |    1      |      -0.0182 |    0.9948 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.688  |  0.2459 | 0.0085 | 0.5779 |      0.4986 |             0.0184 |                 0.6844 |             9.7691 |           6.9632 |          0.5518 |          0.8409 |    1      |      -0.0175 |    0.4252 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6846 |  0.245  | 0.009  | 0.5847 |      0.4986 |             0.0159 |                 0.6824 |            10.9241 |           8.1496 |          0.5276 |          0.8121 |    1      |      -0.0152 |    0.9844 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  6.9448 |        0      |           0.0101 | False          |      nan |            nan |     0      |
| H3a          | logit    | rules_tech - hitai_full                                      |  7.2358 |        0      |           0.011  | False          |      nan |            nan |     0      |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  7.2274 |        0      |           0.0107 | False          |      nan |            nan |     0      |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  6.9568 |        0      |           0.0117 | False          |      nan |            nan |     0      |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.6172 |        0.1058 |         nan      | False          |      nan |            nan |     0.1109 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0601 |        0      |         nan      | False          |      nan |            nan |     0      |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.7957 |        0.0725 |           0.0023 | False          |      nan |            nan |     0.0798 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  5.0871 |        0      |           0.0077 | False          |      nan |            nan |     0      |
| H3a          | gbt      | rules_tech - hitai_full                                      |  6.5207 |        0      |           0.0115 | False          |      nan |            nan |     0      |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  6.4186 |        0      |           0.0102 | False          |      nan |            nan |     0      |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  6.0518 |        0      |           0.0089 | False          |      nan |            nan |     0      |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.7553 |        0.0059 |         nan      | False          |      nan |            nan |     0.0081 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0668 |        0      |         nan      | False          |      nan |            nan |     0      |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  2.1616 |        0.0306 |           0.0023 | False          |      nan |            nan |     0.0375 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  5.9535 |        0      |           0.0095 | True           |        0 |              0 |     0      |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  6.8084 |        0      |           0.0108 | True           |        0 |              0 |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  6.5323 |        0      |           0.01   | True           |        0 |              0 |     0      |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  6.4166 |        0      |           0.0103 | True           |        0 |              0 |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.2206 |        0.0264 |         nan      | False          |      nan |            nan |     0.0341 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0803 |        0      |         nan      | True           |        0 |              0 |     0      |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.5685 |        0.5697 |           0.0005 | False          |      nan |            nan |     0.5697 |
| H4b          | tagger   | corr(tag,fwd) original=0.1758 vs perturbed-context (want ~0) | -0.009  |        0.0581 |           0.1848 | False          |      nan |            nan |     0.0672 |

## Reality check / SPA vs rules_only: RC p=0.000, SPA p=0.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6931 |  0.25   | 0.0066 | 0.504  |      0.4961 |          -0.5864 |    0.2093 |
| rules_tech|pit|gbt_mono      | 10896 |    0.6953 |  0.2503 | 0.0084 | 0.5205 |      0.4961 |           0.2009 |    0.6064 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6828 |  0.2448 | 0.0129 | 0.5855 |      0.4961 |           9.3679 |    1      |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6963 |  0.2503 | 0.0078 | 0.5144 |      0.4961 |          -0.8205 |    0.1354 |
