# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6937 |  0.2503 | 0.0109 | 0.4982 |      0.5035 |             0.0033 |                 0.6934 |             0.8247 |          -0.333  |          0.045  |          0.0269 |    0.2446 |      -0.0248 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6941 |  0.2505 | 0.0227 | 0.4934 |      0.5035 |             0.0073 |                 0.6938 |             0.1939 |          -1.4682 |          0.0992 |          0.0678 |    0.0011 |      -0.1047 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6935 |  0.2502 | 0.0116 | 0.5001 |      0.5035 |             0.0047 |                 0.6934 |             1.1189 |           0.006  |          0.0429 |          0.0266 |    0.505  |      -0.019  |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6956 |  0.2504 | 0.0179 | 0.5117 |      0.5035 |             0.0066 |                 0.693  |             0.9    |          -1.3206 |          0.3244 |          0.5104 |    0.0028 |      -0.2328 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6951 |  0.2504 | 0.0139 | 0.5064 |      0.5035 |             0.0303 |                 0.6956 |             0.6289 |          -1.4747 |          0.2554 |          0.3056 |    0.001  |      -0.2115 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6952 |  0.2507 | 0.0158 | 0.5024 |      0.5035 |             0.0175 |                 0.6939 |             0.3128 |          -1.7404 |          0.2488 |          0.3319 |    0.0001 |      -0.237  |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6973 |  0.2508 | 0.0187 | 0.5107 |      0.5035 |             0.008  |                 0.6931 |             1.3983 |          -1.1019 |          0.3308 |          0.3907 |    0.0114 |      -0.1739 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6951 |  0.2505 | 0.0145 | 0.5064 |      0.5035 |             0.0308 |                 0.6959 |             0.8799 |          -1.427  |          0.2874 |          0.3388 |    0.0015 |      -0.204  |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6948 |  0.2507 | 0.0135 | 0.5069 |      0.5035 |             0.0152 |                 0.6938 |             0.5673 |          -1.5888 |          0.2842 |          0.365  |    0.0004 |      -0.2461 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6857 |  0.2455 | 0.0101 | 0.5795 |      0.5035 |             0.0055 |                 0.6827 |            10.2676 |           7.4068 |          0.5554 |          0.8223 |    1      |      -0.0163 |    0.3292 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6867 |  0.2461 | 0.009  | 0.5743 |      0.5035 |             0.0148 |                 0.6843 |             9.2122 |           6.3936 |          0.5643 |          0.8465 |    1      |      -0.0197 |    0.0066 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6867 |  0.2458 | 0.0101 | 0.5802 |      0.5035 |             0.0044 |                 0.6825 |            10.245  |           7.3641 |          0.5489 |          0.7887 |    1      |      -0.0162 |    0.299  |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6973 |  0.2508 | 0.0159 | 0.5069 |      0.5035 |             0.0144 |                 0.6936 |             1.0835 |          -1.5616 |          0.3483 |          0.3837 |    0.0006 |      -0.2343 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6957 |  0.2505 | 0.0124 | 0.5065 |      0.5035 |             0.0315 |                 0.6961 |             0.5139 |          -1.8    |          0.2776 |          0.3196 |    0.0001 |      -0.2464 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6949 |  0.2507 | 0.0134 | 0.5049 |      0.5035 |             0.0167 |                 0.694  |             0.4054 |          -1.8305 |          0.2691 |          0.3044 |    0.0001 |      -0.2545 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6963 |  0.2505 | 0.0153 | 0.5108 |      0.5035 |             0.0106 |                 0.6932 |             1.067  |          -1.2478 |          0.3068 |          0.3888 |    0.0048 |      -0.1935 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6946 |  0.2504 | 0.014  | 0.5058 |      0.5035 |             0.033  |                 0.6959 |             0.4397 |          -1.4546 |          0.2419 |          0.3148 |    0.0011 |      -0.222  |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6955 |  0.2506 | 0.0148 | 0.507  |      0.5035 |             0.0157 |                 0.694  |             0.6363 |          -1.4621 |          0.2754 |          0.3719 |    0.0011 |      -0.2239 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6863 |  0.2453 | 0.0087 | 0.5814 |      0.5035 |             0.0028 |                 0.6821 |            10.7723 |           7.9036 |          0.5451 |          0.7885 |    1      |      -0.0193 |    0.6997 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6859 |  0.2458 | 0.011  | 0.5789 |      0.5035 |             0.0114 |                 0.6837 |             9.6155 |           6.7665 |          0.5382 |          0.7394 |    1      |      -0.0201 |    0.0435 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6844 |  0.2453 | 0.0107 | 0.5829 |      0.5035 |             0.0032 |                 0.6817 |            10.1534 |           7.2946 |          0.542  |          0.7643 |    1      |      -0.0169 |    0.2525 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  5.2751 |        0      |           0.008  | False          |      nan |       nan      |     0      |
| H3a          | logit    | rules_tech - hitai_full                                      |  6.9903 |        0      |           0.0116 | False          |      nan |       nan      |     0      |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  6.7446 |        0      |           0.0116 | False          |      nan |       nan      |     0      |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  6.5291 |        0      |           0.0106 | False          |      nan |       nan      |     0      |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.9958 |        0.046  |         nan      | False          |      nan |       nan      |     0.0562 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0603 |        0      |         nan      | False          |      nan |       nan      |     0      |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.4487 |        0.6537 |           0.0005 | False          |      nan |       nan      |     0.6647 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  5.2654 |        0      |           0.0074 | False          |      nan |       nan      |     0      |
| H3a          | gbt      | rules_tech - hitai_full                                      |  6.1321 |        0      |           0.0084 | False          |      nan |       nan      |     0      |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  5.4848 |        0      |           0.0089 | False          |      nan |       nan      |     0      |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  5.8596 |        0      |           0.0078 | False          |      nan |       nan      |     0      |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.8342 |        0.0666 |         nan      | False          |      nan |       nan      |     0.0771 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0608 |        0      |         nan      | False          |      nan |       nan      |     0      |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.8021 |        0.4225 |          -0.0008 | False          |      nan |       nan      |     0.4647 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  4.3849 |        0      |           0.0068 | True           |        0 |         0      |     0      |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  5.5013 |        0      |           0.0081 | True           |        0 |         0      |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  5.564  |        0      |           0.0082 | True           |        0 |         0      |     0      |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  5.9902 |        0      |           0.0088 | True           |        0 |         0      |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.3495 |        0.0188 |         nan      | False          |      nan |       nan      |     0.0243 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0622 |        0      |         nan      | True           |        0 |         0.0001 |     0      |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -2.446  |        0.0144 |          -0.0023 | False          |      nan |       nan      |     0.0199 |
| H4b          | tagger   | corr(tag,fwd) original=0.1743 vs perturbed-context (want ~0) |  0.0021 |        0.6647 |           0.1722 | False          |      nan |       nan      |     0.6647 |

## Reality check / SPA vs rules_only: RC p=0.000, SPA p=0.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6929 |  0.2499 | 0.004  | 0.5056 |      0.5132 |          -0.051  |    0.4728 |
| rules_tech|pit|gbt_mono      | 10896 |    0.6924 |  0.2496 | 0.0033 | 0.5199 |      0.5132 |          -0.9725 |    0.0957 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6804 |  0.2437 | 0.0122 | 0.5916 |      0.5132 |           7.8588 |    1      |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6924 |  0.2496 | 0.0034 | 0.5204 |      0.5132 |          -1.4782 |    0.0262 |
