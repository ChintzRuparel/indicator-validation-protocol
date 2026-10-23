# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6939 |  0.2504 | 0.0112 | 0.5047 |      0.5035 |             0.0059 |                 0.6935 |             0.5505 |          -0.2391 |          0.0467 |          0.0631 |    0.3085 |      -0.0582 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6937 |  0.2503 | 0.0135 | 0.506  |      0.5035 |             0.0071 |                 0.6936 |             0.5137 |          -0.081  |          0.0719 |          0.3362 |    0.4328 |      -0.0583 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6934 |  0.2501 | 0.0111 | 0.5047 |      0.5035 |             0.0141 |                 0.6934 |             0.1185 |           0.0982 |          0.0018 |          0.1998 |    0.5813 |      -0.0481 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6945 |  0.2504 | 0.0188 | 0.5072 |      0.5035 |             0.018  |                 0.6938 |             0.8642 |          -0.3441 |          0.1695 |          0.4089 |    0.2364 |      -0.1354 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.695  |  0.2505 | 0.0085 | 0.5034 |      0.5035 |             0.0328 |                 0.6972 |             0.5326 |          -0.6774 |          0.1181 |          0.2152 |    0.0799 |      -0.1028 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6945 |  0.2506 | 0.0153 | 0.5032 |      0.5035 |             0.0216 |                 0.6951 |             0.458  |          -0.6091 |          0.1385 |          0.3713 |    0.1033 |      -0.132  |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6946 |  0.2504 | 0.0185 | 0.5069 |      0.5035 |             0.0174 |                 0.6938 |             0.9003 |          -0.5207 |          0.2    |          0.41   |    0.1385 |      -0.0882 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.695  |  0.2505 | 0.0078 | 0.5038 |      0.5035 |             0.0319 |                 0.6973 |             0.6711 |          -0.5026 |          0.1138 |          0.2173 |    0.1482 |      -0.078  |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.695  |  0.2507 | 0.0159 | 0.5025 |      0.5035 |             0.0198 |                 0.6951 |             0.4363 |          -0.679  |          0.1445 |          0.3753 |    0.0797 |      -0.1418 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6868 |  0.2461 | 0.0066 | 0.5737 |      0.5035 |             0.0087 |                 0.6844 |            10.5494 |           7.6288 |          0.5546 |          0.8084 |    1      |      -0.0196 |    0.9029 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6891 |  0.2471 | 0.0084 | 0.5657 |      0.5035 |             0.0163 |                 0.6874 |             9.5121 |           6.6252 |          0.5416 |          0.8078 |    1      |      -0.0199 |    0.2151 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6882 |  0.2465 | 0.013  | 0.5735 |      0.5035 |             0.0092 |                 0.6848 |            10.5034 |           7.6165 |          0.548  |          0.8205 |    1      |      -0.0208 |    0.8959 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6943 |  0.2503 | 0.017  | 0.5075 |      0.5035 |             0.0195 |                 0.6939 |             0.7812 |          -0.8708 |          0.224  |          0.3813 |    0.0347 |      -0.1442 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6956 |  0.2506 | 0.0121 | 0.5025 |      0.5035 |             0.0329 |                 0.6974 |             0.2799 |          -1.0132 |          0.1297 |          0.2372 |    0.0175 |      -0.1332 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.695  |  0.2508 | 0.0157 | 0.5046 |      0.5035 |             0.0229 |                 0.6952 |             0.478  |          -0.8884 |          0.1208 |          0.1457 |    0.0324 |      -0.1071 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6949 |  0.2505 | 0.0168 | 0.5031 |      0.5035 |             0.0219 |                 0.6945 |             0.3831 |          -1.0243 |          0.1442 |          0.2421 |    0.0167 |      -0.1458 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6959 |  0.2506 | 0.0205 | 0.5035 |      0.5035 |             0.0327 |                 0.6979 |             0.4358 |          -0.4664 |          0.0916 |          0.2552 |    0.1658 |      -0.0781 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6944 |  0.2505 | 0.0169 | 0.503  |      0.5035 |             0.0249 |                 0.6954 |             0.2444 |          -0.8275 |          0.1148 |          0.2603 |    0.0424 |      -0.1075 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6846 |  0.2457 | 0.007  | 0.5764 |      0.5035 |             0.009  |                 0.6839 |            10.7141 |           7.7296 |          0.5605 |          0.8211 |    1      |      -0.0145 |    0.9328 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.69   |  0.2472 | 0.0084 | 0.5669 |      0.5035 |             0.0152 |                 0.6872 |             9.172  |           6.298  |          0.5734 |          0.8951 |    1      |      -0.0319 |    0.0711 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6895 |  0.2465 | 0.0108 | 0.5751 |      0.5035 |             0.0078 |                 0.684  |            10.5692 |           7.5846 |          0.5447 |          0.7831 |    1      |      -0.0123 |    0.8855 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  4.364  |        0      |           0.007  | False          | nan      |       nan      |     0      |
| H3a          | logit    | rules_tech - hitai_full                                      |  5.2445 |        0      |           0.0077 | False          | nan      |       nan      |     0      |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  5.1559 |        0      |           0.0075 | False          | nan      |       nan      |     0      |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  5.3963 |        0      |           0.0081 | False          | nan      |       nan      |     0      |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.6812 |        0.0073 |         nan      | False          | nan      |       nan      |     0.0095 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0448 |        0.0015 |         nan      | False          | nan      |       nan      |     0.0023 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -2.3407 |        0.0192 |          -0.0022 | False          | nan      |       nan      |     0.0235 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  3.164  |        0.0008 |           0.0046 | False          | nan      |       nan      |     0.0014 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  3.9739 |        0      |           0.0059 | False          | nan      |       nan      |     0.0001 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  4.2648 |        0      |           0.0066 | False          | nan      |       nan      |     0      |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  4.4965 |        0      |           0.0069 | False          | nan      |       nan      |     0      |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.1842 |        0.0289 |         nan      | False          | nan      |       nan      |     0.0335 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.067  |        0      |         nan      | False          | nan      |       nan      |     0      |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.7509 |        0.4527 |           0.001  | False          | nan      |       nan      |     0.4527 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  3.0971 |        0.001  |           0.0052 | True           |   0.002  |         0.0049 |     0.0017 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  4.1448 |        0      |           0.0068 | True           |   0.0001 |         0.0001 |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  4.2195 |        0      |           0.0068 | True           |   0.0001 |         0.0001 |     0      |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  3.8126 |        0.0001 |           0.0062 | True           |   0.0002 |         0.0003 |     0.0001 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.8258 |        0.0047 |         nan      | False          | nan      |       nan      |     0.0069 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0372 |        0.0067 |         nan      | True           |   0.0067 |         0.0334 |     0.0092 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.9961 |        0.3192 |           0.0013 | False          | nan      |       nan      |     0.3344 |
| H4b          | tagger   | corr(tag,fwd) original=0.1684 vs perturbed-context (want ~0) | -0.0071 |        0.1354 |           0.1755 | False          | nan      |       nan      |     0.1489 |

## Reality check / SPA vs rules_only: RC p=0.000, SPA p=0.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6932 |  0.25   | 0.0057 | 0.5    |       0.505 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 10896 |    0.6938 |  0.2503 | 0.006  | 0.5039 |       0.505 |          -1.5343 |    0.0177 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6855 |  0.2461 | 0.0054 | 0.5738 |       0.505 |           6.6059 |    1      |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6935 |  0.2502 | 0.0062 | 0.5022 |       0.505 |          -2.299  |    0.0002 |
