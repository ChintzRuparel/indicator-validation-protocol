# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6939 |  0.2503 | 0.0109 | 0.5122 |      0.5014 |             0.0023 |                 0.6927 |             1.2027 |           0.2677 |          0.1169 |          0.2719 |    0.7124 |      -0.0574 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6942 |  0.2505 | 0.0091 | 0.5077 |      0.5014 |             0.011  |                 0.6933 |             0.4877 |          -0.4097 |          0.0884 |          0.1926 |    0.1958 |      -0.0774 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6935 |  0.2501 | 0.0063 | 0.5026 |      0.5014 |             0.0063 |                 0.6932 |             0.5983 |          -0.9198 |          0.0912 |          0.0558 |    0.0279 |      -0.0722 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6952 |  0.2503 | 0.0139 | 0.5196 |      0.5014 |             0.0091 |                 0.6924 |             1.8925 |           0.2937 |          0.2659 |          0.5398 |    0.7301 |      -0.0653 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6947 |  0.2501 | 0.0154 | 0.5155 |      0.5014 |             0.0223 |                 0.694  |             0.8749 |          -1.0218 |          0.2889 |          0.4552 |    0.0161 |      -0.1991 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6964 |  0.2503 | 0.0127 | 0.5158 |      0.5014 |             0.0167 |                 0.693  |             0.8531 |          -0.7434 |          0.2232 |          0.3925 |    0.0592 |      -0.1405 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6971 |  0.2504 | 0.0125 | 0.5194 |      0.5014 |             0.0071 |                 0.6923 |             1.5188 |          -0.027  |          0.2235 |          0.38   |    0.4775 |      -0.0937 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6935 |  0.25   | 0.0114 | 0.5147 |      0.5014 |             0.0233 |                 0.6942 |             1.2069 |          -0.7524 |          0.2842 |          0.4251 |    0.0575 |      -0.1506 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6965 |  0.2503 | 0.0133 | 0.515  |      0.5014 |             0.0167 |                 0.6929 |             0.8665 |          -0.7287 |          0.2232 |          0.3907 |    0.0627 |      -0.1384 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6841 |  0.2445 | 0.0105 | 0.5904 |      0.5014 |             0.0045 |                 0.6799 |            10.2637 |           7.5704 |          0.5434 |          0.8573 |    1      |      -0.0257 |    0.9597 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6832 |  0.2447 | 0.01   | 0.586  |      0.5014 |             0.0089 |                 0.6816 |             9.0011 |           6.2888 |          0.5548 |          0.8872 |    1      |      -0.0298 |    0.237  |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6834 |  0.244  | 0.0099 | 0.5928 |      0.5014 |             0.0028 |                 0.6795 |            10.0864 |           7.3811 |          0.5333 |          0.8085 |    1      |      -0.0285 |    0.9189 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6967 |  0.2503 | 0.01   | 0.5221 |      0.5014 |             0.006  |                 0.6925 |             1.6429 |          -0.2779 |          0.2951 |          0.4666 |    0.2806 |      -0.086  |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6947 |  0.2501 | 0.0108 | 0.5141 |      0.5014 |             0.0244 |                 0.6943 |             0.8935 |          -0.9953 |          0.2628 |          0.3956 |    0.0184 |      -0.1849 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6953 |  0.2502 | 0.0121 | 0.5166 |      0.5014 |             0.0167 |                 0.693  |             0.8667 |          -0.7824 |          0.2295 |          0.3789 |    0.0507 |      -0.1459 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6966 |  0.2504 | 0.0163 | 0.5189 |      0.5014 |             0.0078 |                 0.6925 |             1.6905 |          -0.1784 |          0.3289 |          0.6126 |    0.3547 |      -0.0998 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6949 |  0.2502 | 0.0121 | 0.5158 |      0.5014 |             0.0228 |                 0.6941 |             0.8382 |          -1.0359 |          0.2789 |          0.4445 |    0.0152 |      -0.1711 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6972 |  0.2505 | 0.0179 | 0.5115 |      0.5014 |             0.0161 |                 0.6929 |             0.6212 |          -1.0958 |          0.2522 |          0.4266 |    0.0111 |      -0.1802 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6834 |  0.2441 | 0.0114 | 0.5922 |      0.5014 |             0.0057 |                 0.6794 |            10.1667 |           7.4671 |          0.553  |          0.8861 |    1      |      -0.0451 |    0.9323 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.683  |  0.2445 | 0.0135 | 0.5881 |      0.5014 |             0.0068 |                 0.6804 |             8.452  |           5.8413 |          0.5562 |          0.898  |    1      |      -0.0411 |    0.0576 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6825 |  0.2439 | 0.0127 | 0.5932 |      0.5014 |             0.0065 |                 0.679  |             9.0963 |           6.4444 |          0.5463 |          0.8585 |    1      |      -0.0378 |    0.3435 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  5.7037 |        0      |           0.0098 | False          |      nan |            nan |     0      |
| H3a          | logit    | rules_tech - hitai_full                                      |  6.941  |        0      |           0.013  | False          |      nan |            nan |     0      |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  6.9708 |        0      |           0.0127 | False          |      nan |            nan |     0      |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  7.3319 |        0      |           0.0126 | False          |      nan |            nan |     0      |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.3351 |        0.0195 |         nan      | False          |      nan |            nan |     0.0269 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0596 |        0      |         nan      | False          |      nan |            nan |     0.0001 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.6323 |        0.5272 |          -0.0007 | False          |      nan |            nan |     0.5523 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  7.0152 |        0      |           0.011  | False          |      nan |            nan |     0      |
| H3a          | gbt      | rules_tech - hitai_full                                      |  7.2427 |        0      |           0.0103 | False          |      nan |            nan |     0      |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  7.9851 |        0      |           0.0115 | False          |      nan |            nan |     0      |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  8.105  |        0      |           0.0118 | False          |      nan |            nan |     0      |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.0401 |        0.2983 |         nan      | False          |      nan |            nan |     0.3646 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.085  |        0      |         nan      | False          |      nan |            nan |     0      |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.1984 |        0.8428 |          -0.0002 | False          |      nan |            nan |     0.8428 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  5.1264 |        0      |           0.0102 | True           |        0 |              0 |     0      |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  7.912  |        0      |           0.0131 | True           |        0 |              0 |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  7.4417 |        0      |           0.0119 | True           |        0 |              0 |     0      |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  8.3598 |        0      |           0.0138 | True           |        0 |              0 |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.6236 |        0.1045 |         nan      | False          |      nan |            nan |     0.1352 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0866 |        0      |         nan      | True           |        0 |              0 |     0      |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.6934 |        0.488  |          -0.0008 | False          |      nan |            nan |     0.5523 |
| H4b          | tagger   | corr(tag,fwd) original=0.1878 vs perturbed-context (want ~0) |  0.0031 |        0.52   |           0.1847 | False          |      nan |            nan |     0.5523 |

## Reality check / SPA vs rules_only: RC p=0.000, SPA p=0.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6936 |  0.2502 | 0.0159 | 0.4988 |      0.4931 |          -2.0257 |    0.0036 |
| rules_tech|pit|gbt_mono      | 10896 |    0.694  |  0.2504 | 0.0102 | 0.5058 |      0.4931 |          -1.1863 |    0.0559 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6848 |  0.245  | 0.0084 | 0.5841 |      0.4931 |           6.8778 |    1      |
| hitai_full|shuffled|gbt_mono | 10896 |    0.694  |  0.2504 | 0.0102 | 0.5058 |      0.4931 |          -1.1863 |    0.0559 |
