# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6941 |  0.2505 | 0.0131 | 0.501  |      0.4888 |             0.0056 |                 0.6932 |             0.6777 |          -0.1714 |          0.0517 |          0.0765 |    0.3603 |      -0.0535 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.694  |  0.2504 | 0.0147 | 0.4994 |      0.4888 |             0.0069 |                 0.6937 |            -0.147  |          -0.9151 |          0.0647 |          0.139  |    0.0261 |      -0.107  |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6937 |  0.2503 | 0.0136 | 0.4951 |      0.4888 |             0.002  |                 0.693  |             0.1303 |          -0.93   |          0.0553 |          0.0351 |    0.0256 |      -0.0648 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6935 |  0.2502 | 0.012  | 0.5143 |      0.4888 |             0.0125 |                 0.6932 |             1.0997 |          -0.0597 |          0.178  |          0.481  |    0.4504 |      -0.0696 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6963 |  0.2508 | 0.0151 | 0.5107 |      0.4888 |             0.0226 |                 0.6949 |            -0.0676 |          -1.8674 |          0.2641 |          0.413  |    0.0001 |      -0.3275 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6975 |  0.2507 | 0.0166 | 0.5098 |      0.4888 |             0.0181 |                 0.6935 |             0.6847 |          -0.7297 |          0.2178 |          0.4875 |    0.0662 |      -0.1816 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6937 |  0.2502 | 0.0153 | 0.5073 |      0.4888 |             0.0169 |                 0.6935 |             0.9677 |          -0.282  |          0.169  |          0.3882 |    0.2775 |      -0.0745 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6959 |  0.2507 | 0.0163 | 0.5088 |      0.4888 |             0.024  |                 0.6948 |             0.0071 |          -1.6981 |          0.2505 |          0.4083 |    0.0003 |      -0.3009 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6975 |  0.2507 | 0.0166 | 0.5098 |      0.4888 |             0.0181 |                 0.6935 |             0.6847 |          -0.7297 |          0.2178 |          0.4875 |    0.0662 |      -0.1816 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6843 |  0.2444 | 0.0093 | 0.5865 |      0.4888 |             0.0102 |                 0.6812 |            10.5049 |           7.9017 |          0.5409 |          0.9411 |    1      |      -0.0161 |    0.9583 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6859 |  0.245  | 0.0123 | 0.584  |      0.4888 |             0.0095 |                 0.6817 |             9.4763 |           6.7219 |          0.5416 |          0.7719 |    1      |      -0.014  |    0.2486 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6856 |  0.2444 | 0.0103 | 0.5887 |      0.4888 |             0.0143 |                 0.6808 |            10.4162 |           7.7269 |          0.5387 |          0.847  |    1      |      -0.0128 |    0.9157 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6938 |  0.2502 | 0.0161 | 0.5073 |      0.4888 |             0.015  |                 0.6935 |             0.7215 |          -0.6729 |          0.1855 |          0.3716 |    0.0796 |      -0.123  |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6965 |  0.2508 | 0.0142 | 0.5094 |      0.4888 |             0.0233 |                 0.695  |             0.1539 |          -1.6642 |          0.2959 |          0.4899 |    0.0003 |      -0.3401 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.698  |  0.2507 | 0.0159 | 0.5114 |      0.4888 |             0.0167 |                 0.6935 |             0.6114 |          -0.7084 |          0.2037 |          0.4847 |    0.071  |      -0.1857 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6952 |  0.2504 | 0.0125 | 0.5078 |      0.4888 |             0.0142 |                 0.6936 |             0.2803 |          -1.1789 |          0.1918 |          0.3394 |    0.0069 |      -0.2005 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6961 |  0.2507 | 0.011  | 0.5101 |      0.4888 |             0.0257 |                 0.695  |             0.0559 |          -1.8193 |          0.2704 |          0.3909 |    0.0001 |      -0.3277 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.698  |  0.2507 | 0.0155 | 0.5102 |      0.4888 |             0.019  |                 0.6936 |             0.5039 |          -0.8308 |          0.2177 |          0.5293 |    0.0423 |      -0.1988 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6846 |  0.2448 | 0.0102 | 0.5844 |      0.4888 |             0.0111 |                 0.6821 |             9.4444 |           6.8643 |          0.5367 |          0.9254 |    1      |      -0.0164 |    0.3513 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6853 |  0.2454 | 0.0137 | 0.5817 |      0.4888 |             0.0096 |                 0.6824 |             8.0521 |           5.3782 |          0.5369 |          0.8162 |    1      |      -0.0223 |    0.0003 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6872 |  0.2451 | 0.0131 | 0.5839 |      0.4888 |             0.0133 |                 0.6814 |             9.0464 |           6.4319 |          0.5305 |          0.8785 |    1      |      -0.0267 |    0.0976 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  5.8518 |        0      |           0.0098 | False          |      nan |       nan      |     0      |
| H3a          | logit    | rules_tech - hitai_full                                      |  6.01   |        0      |           0.0094 | False          |      nan |       nan      |     0      |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  5.9931 |        0      |           0.0095 | False          |      nan |       nan      |     0      |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  7.0604 |        0      |           0.0109 | False          |      nan |       nan      |     0      |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.4117 |        0.158  |         nan      | False          |      nan |       nan      |     0.1932 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0665 |        0      |         nan      | False          |      nan |       nan      |     0      |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.2469 |        0.805  |           0.0003 | False          |      nan |       nan      |     0.8433 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  4.448  |        0      |           0.008  | False          |      nan |       nan      |     0      |
| H3a          | gbt      | rules_tech - hitai_full                                      |  5.432  |        0      |           0.0099 | False          |      nan |       nan      |     0      |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  5.7513 |        0      |           0.0105 | False          |      nan |       nan      |     0      |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  5.661  |        0      |           0.0102 | False          |      nan |       nan      |     0      |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.5632 |        0.118  |         nan      | False          |      nan |       nan      |     0.1527 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0701 |        0      |         nan      | False          |      nan |       nan      |     0      |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.5309 |        0.5955 |          -0.0007 | False          |      nan |       nan      |     0.655  |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  4.243  |        0      |           0.0081 | True           |        0 |         0.0001 |     0      |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  6.9027 |        0      |           0.0119 | True           |        0 |         0      |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  6.9002 |        0      |           0.0123 | True           |        0 |         0      |     0      |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  6.9244 |        0      |           0.0123 | True           |        0 |         0      |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.7556 |        0.0792 |         nan      | False          |      nan |       nan      |     0.1088 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0832 |        0      |         nan      | True           |        0 |         0      |     0      |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.1357 |        0.2561 |           0.0016 | False          |      nan |       nan      |     0.2965 |
| H4b          | tagger   | corr(tag,fwd) original=0.1722 vs perturbed-context (want ~0) |  0.0008 |        0.8587 |           0.1714 | False          |      nan |       nan      |     0.8587 |

## Reality check / SPA vs rules_only: RC p=0.000, SPA p=0.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6938 |  0.2503 | 0.0176 | 0.4994 |      0.5043 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 10896 |    0.6968 |  0.2514 | 0.0213 | 0.5105 |      0.5043 |          -2.0595 |    0.0032 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6843 |  0.2455 | 0.0272 | 0.5882 |      0.5043 |           7.0029 |    1      |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6965 |  0.2513 | 0.0217 | 0.507  |      0.5043 |          -2.044  |    0.0033 |
