# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 22008, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 13212 |    0.695  |  0.2508 | 0.0169 | 0.5159 |      0.5103 |             0.0125 |                 0.6932 |             0.5973 |          -0.2552 |          0.1266 |          0.2221 |    0.297  |      -0.0799 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 13212 |    0.6948 |  0.2508 | 0.0186 | 0.5006 |      0.5103 |             0.0134 |                 0.6946 |            -0.3799 |          -0.9143 |          0.1064 |          0.441  |    0.0271 |      -0.234  |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 13212 |    0.695  |  0.2506 | 0.0108 | 0.5007 |      0.5103 |             0.0137 |                 0.6936 |            -0.3935 |          -1.0376 |          0.0961 |          0.2581 |    0.015  |      -0.1845 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 13212 |    0.7044 |  0.2521 | 0.0335 | 0.5007 |      0.5103 |             0.0153 |                 0.6935 |            -0.1289 |          -0.8736 |          0.1525 |          0.4484 |    0.0333 |      -0.2336 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 13212 |    0.7013 |  0.2523 | 0.0309 | 0.4887 |      0.5103 |             0.0489 |                 0.7017 |            -0.5744 |          -1.3039 |          0.1462 |          0.4202 |    0.0031 |      -0.3105 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 13212 |    0.704  |  0.2522 | 0.0254 | 0.5002 |      0.5103 |             0.0367 |                 0.6971 |            -0.066  |          -0.562  |          0.0985 |          0.4128 |    0.1185 |      -0.133  |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 13212 |    0.7024 |  0.2522 | 0.0328 | 0.5033 |      0.5103 |             0.0134 |                 0.6934 |             0.0658 |          -0.7707 |          0.1655 |          0.4276 |    0.0546 |      -0.1814 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 13212 |    0.7011 |  0.2523 | 0.0306 | 0.4878 |      0.5103 |             0.0514 |                 0.7017 |            -0.6596 |          -1.3988 |          0.1424 |          0.4003 |    0.0017 |      -0.3166 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 13212 |    0.704  |  0.2522 | 0.0254 | 0.5002 |      0.5103 |             0.0367 |                 0.6971 |            -0.066  |          -0.562  |          0.0985 |          0.4128 |    0.1185 |      -0.133  |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 13212 |    0.6965 |  0.2487 | 0.0199 | 0.5618 |      0.5103 |             0.0172 |                 0.6859 |             5.9296 |           4.0378 |          0.5224 |          0.8292 |    1      |      -0.0465 |    0.473  |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 13212 |    0.6953 |  0.2506 | 0.0213 | 0.5397 |      0.5103 |             0.0341 |                 0.6934 |             4.3438 |           2.646  |          0.4304 |          0.7224 |    1      |      -0.0543 |    0.0015 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 13212 |    0.6954 |  0.2491 | 0.0192 | 0.5554 |      0.5103 |             0.0176 |                 0.6888 |             5.1726 |           3.5237 |          0.4506 |          0.8517 |    1      |      -0.0448 |    0.1294 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 13212 |    0.7017 |  0.2523 | 0.037  | 0.5013 |      0.5103 |             0.0143 |                 0.6936 |            -0.2024 |          -1.0015 |          0.1699 |          0.4643 |    0.0185 |      -0.2547 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 13212 |    0.7028 |  0.2525 | 0.0309 | 0.491  |      0.5103 |             0.0505 |                 0.7015 |            -0.5696 |          -1.3219 |          0.1518 |          0.4025 |    0.0028 |      -0.3169 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 13212 |    0.7035 |  0.2523 | 0.0255 | 0.4989 |      0.5103 |             0.04   |                 0.6971 |            -0.2204 |          -0.6794 |          0.0915 |          0.4096 |    0.076  |      -0.159  |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 13212 |    0.7057 |  0.2527 | 0.0319 | 0.4981 |      0.5103 |             0.0184 |                 0.6943 |             0.4572 |          -0.5591 |          0.1802 |          0.3211 |    0.1219 |      -0.1394 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 13212 |    0.7023 |  0.252  | 0.0317 | 0.4918 |      0.5103 |             0.0485 |                 0.7016 |             0.0591 |          -0.5911 |          0.1404 |          0.5073 |    0.1078 |      -0.1814 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 13212 |    0.6965 |  0.2515 | 0.0247 | 0.4942 |      0.5103 |             0.0384 |                 0.6971 |            -0.3225 |          -1.0246 |          0.1375 |          0.3825 |    0.0156 |      -0.2435 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 13212 |    0.6924 |  0.2484 | 0.0239 | 0.5615 |      0.5103 |             0.0177 |                 0.6854 |             6.2844 |           4.4353 |          0.5176 |          0.8776 |    1      |      -0.0298 |    0.7813 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 13212 |    0.6955 |  0.25   | 0.0244 | 0.5411 |      0.5103 |             0.0302 |                 0.6928 |             4.5384 |           2.8233 |          0.4326 |          0.7383 |    1      |      -0.0545 |    0.0046 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 13212 |    0.6943 |  0.2489 | 0.0187 | 0.5592 |      0.5103 |             0.0163 |                 0.6883 |             6.0403 |           4.1747 |          0.5073 |          0.872  |    1      |      -0.0278 |    0.5867 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -0.4471 |        0.6726 |          -0.0015 | False          | nan      |       nan      |     0.7399 |
| H3a          | logit    | rules_tech - hitai_full                                      |  1.6074 |        0.054  |           0.0058 | False          | nan      |       nan      |     0.099  |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  1.5159 |        0.0648 |           0.0052 | False          | nan      |       nan      |     0.1096 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.4456 |        0.0072 |           0.0092 | False          | nan      |       nan      |     0.0199 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.2833 |        0      |         nan      | False          | nan      |       nan      |     0.0004 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0346 |        0.052  |         nan      | False          | nan      |       nan      |     0.099  |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.7913 |        0.0732 |          -0.0041 | False          | nan      |       nan      |     0.1151 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -0.2592 |        0.6023 |          -0.0005 | False          | nan      |       nan      |     0.7361 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  2.3398 |        0.0096 |           0.0058 | False          | nan      |       nan      |     0.0236 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  2.476  |        0.0066 |           0.0074 | False          | nan      |       nan      |     0.0199 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  2.5586 |        0.0053 |           0.007  | False          | nan      |       nan      |     0.0193 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.0879 |        0      |         nan      | False          | nan      |       nan      |     0.0005 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               | -0.0074 |        0.6361 |         nan      | False          | nan      |       nan      |     0.7365 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.1094 |        0.9129 |           0.0002 | False          | nan      |       nan      |     0.9129 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -0.1433 |        0.557  |          -0.0004 | True           |   0.6173 |         1      |     0.7361 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  2.9757 |        0.0015 |           0.0086 | True           |   0.0073 |         0.0073 |     0.008  |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  2.636  |        0.0042 |           0.0081 | True           |   0.0168 |         0.021  |     0.0185 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  0.4997 |        0.3087 |           0.0011 | True           |   0.6173 |         1      |     0.4527 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.9826 |        0.0001 |         nan      | False          | nan      |       nan      |     0.0005 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0356 |        0.0473 |         nan      | True           |   0.142  |         0.2367 |     0.099  |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.5613 |        0.5746 |          -0.0011 | False          | nan      |       nan      |     0.7361 |
| H4b          | tagger   | corr(tag,fwd) original=0.1583 vs perturbed-context (want ~0) |  0.0022 |        0.7477 |           0.1561 | False          | nan      |       nan      |     0.7833 |

## Reality check / SPA vs rules_only: RC p=0.957, SPA p=0.793

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5448 |    0.6927 |  0.2498 | 0.0079 | 0.5    |      0.5163 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 5448 |    0.697  |  0.2506 | 0.0092 | 0.5067 |      0.5163 |          -0.1738 |    0.4079 |
| hitai_full|pit|gbt_mono      | 5448 |    0.6879 |  0.2473 | 0.0068 | 0.5653 |      0.5163 |           4.9359 |    1      |
| hitai_full|shuffled|gbt_mono | 5448 |    0.6965 |  0.2504 | 0.0102 | 0.5063 |      0.5163 |           0.2681 |    0.6405 |
