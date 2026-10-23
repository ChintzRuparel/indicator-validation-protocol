# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 10488, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6300 |    0.6995 |  0.2523 | 0.0355 | 0.4926 |      0.4871 |             0.0163 |                 0.6939 |            -0.2152 |          -0.5144 |          0.0686 |          0.5257 |    0.2285 |      -0.1135 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6300 |    0.6971 |  0.2516 | 0.039  | 0.4834 |      0.4871 |             0.0203 |                 0.6947 |            -0.2536 |          -0.4894 |          0.0527 |          0.4994 |    0.24   |      -0.1195 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6300 |    0.6956 |  0.2512 | 0.0373 | 0.4898 |      0.4871 |             0.0104 |                 0.6934 |            -0.3522 |          -0.6025 |          0.0619 |          0.6019 |    0.1922 |      -0.1427 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6300 |    0.7396 |  0.257  | 0.051  | 0.4927 |      0.4871 |             0.0308 |                 0.6974 |            -0.1872 |          -0.9346 |          0.206  |          0.7508 |    0.0875 |      -0.2544 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6300 |    0.7014 |  0.2522 | 0.0367 | 0.4902 |      0.4871 |             0.0665 |                 0.7055 |            -0.2533 |          -0.6554 |          0.094  |          0.5276 |    0.1725 |      -0.1371 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6300 |    0.7017 |  0.2531 | 0.0433 | 0.4902 |      0.4871 |             0.0381 |                 0.6983 |            -0.411  |          -0.9945 |          0.1329 |          0.5033 |    0.0733 |      -0.1772 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6300 |    0.7276 |  0.2559 | 0.0492 | 0.4958 |      0.4871 |             0.0339 |                 0.6975 |            -0.134  |          -0.7992 |          0.1889 |          0.7711 |    0.1243 |      -0.2153 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6300 |    0.7015 |  0.2523 | 0.0376 | 0.4915 |      0.4871 |             0.0653 |                 0.7057 |            -0.2393 |          -0.6828 |          0.1029 |          0.5273 |    0.1627 |      -0.1362 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6300 |    0.7022 |  0.2534 | 0.0424 | 0.4895 |      0.4871 |             0.0388 |                 0.6983 |            -0.4175 |          -1.0014 |          0.133  |          0.5033 |    0.0719 |      -0.1772 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6300 |    0.7005 |  0.2481 | 0.035  | 0.5734 |      0.4871 |             0.0217 |                 0.6848 |             7.1699 |           5.4574 |          0.5448 |          0.9154 |    1      |      -0.0275 |    0.9172 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6300 |    0.6934 |  0.2486 | 0.0162 | 0.5571 |      0.4871 |             0.0384 |                 0.6922 |             6.0605 |           4.2557 |          0.516  |          0.8003 |    1      |      -0.0255 |    0.4076 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6300 |    0.7042 |  0.2499 | 0.0409 | 0.5645 |      0.4871 |             0.0191 |                 0.6854 |             6.324  |           4.6452 |          0.5181 |          0.9113 |    1      |      -0.0247 |    0.6168 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6300 |    0.7177 |  0.2554 | 0.0503 | 0.489  |      0.4871 |             0.0349 |                 0.6978 |            -0.1381 |          -0.9869 |          0.2276 |          0.7303 |    0.0757 |      -0.2341 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6300 |    0.7044 |  0.2528 | 0.0432 | 0.4902 |      0.4871 |             0.0658 |                 0.7062 |            -0.241  |          -0.7087 |          0.1094 |          0.5184 |    0.1536 |      -0.1376 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6300 |    0.701  |  0.2531 | 0.0422 | 0.49   |      0.4871 |             0.0393 |                 0.6983 |            -0.2004 |          -0.7738 |          0.1321 |          0.524  |    0.1298 |      -0.1586 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6300 |    0.7237 |  0.2562 | 0.0589 | 0.4968 |      0.4871 |             0.0377 |                 0.6989 |             0.0805 |          -0.7055 |          0.2143 |          0.7278 |    0.1553 |      -0.1767 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6300 |    0.7019 |  0.2528 | 0.0364 | 0.4906 |      0.4871 |             0.0654 |                 0.7061 |            -0.5051 |          -1.3636 |          0.1897 |          0.4087 |    0.0251 |      -0.1798 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6300 |    0.7003 |  0.2527 | 0.0391 | 0.5013 |      0.4871 |             0.0432 |                 0.6984 |             0.0913 |          -0.8353 |          0.211  |          0.4619 |    0.115  |      -0.146  |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6300 |    0.6938 |  0.2478 | 0.0183 | 0.5654 |      0.4871 |             0.0172 |                 0.6856 |             5.6977 |           4.0481 |          0.5156 |          0.9384 |    1      |      -0.0333 |    0.2994 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6300 |    0.6957 |  0.25   | 0.0388 | 0.5363 |      0.4871 |             0.0471 |                 0.6927 |             3.3257 |           1.7786 |          0.4246 |          0.7771 |    0.9947 |      -0.0916 |    0.0001 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6300 |    0.7033 |  0.2499 | 0.0333 | 0.5596 |      0.4871 |             0.0156 |                 0.6859 |             5.2079 |           3.6515 |          0.4635 |          0.8437 |    1      |      -0.0296 |    0.1405 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -0.1525 |        0.5606 |          -0.001  | False          |      nan |            nan |     0.7255 |
| H3a          | logit    | rules_tech - hitai_full                                      |  4.6425 |        0      |           0.0271 | False          |      nan |            nan |     0      |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  3.3567 |        0.0004 |           0.0172 | False          |      nan |            nan |     0.0029 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  3.9244 |        0      |           0.0232 | False          |      nan |            nan |     0.0005 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.193  |        0.0283 |         nan      | False          |      nan |            nan |     0.0778 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0531 |        0.0424 |         nan      | False          |      nan |            nan |     0.1037 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.0525 |        0.2926 |          -0.0067 | False          |      nan |            nan |     0.4597 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  1.0039 |        0.1577 |           0.0037 | False          |      nan |            nan |     0.2891 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  2.2539 |        0.0121 |           0.0081 | False          |      nan |            nan |     0.0444 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  2.7737 |        0.0028 |           0.0111 | False          |      nan |            nan |     0.0152 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  2.3939 |        0.0083 |           0.0086 | False          |      nan |            nan |     0.0367 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.6686 |        0.0952 |         nan      | False          |      nan |            nan |     0.2094 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0106 |        0.3658 |         nan      | False          |      nan |            nan |     0.5365 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.2072 |        0.2273 |           0.0023 | False          |      nan |            nan |     0.3847 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -1.5269 |        0.9366 |          -0.0086 | True           |        1 |              1 |     0.9366 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      | -0.3583 |        0.64   |          -0.002  | True           |        1 |              1 |     0.7822 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       | -0.5721 |        0.7164 |          -0.0032 | True           |        1 |              1 |     0.8295 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         | -0.696  |        0.7568 |          -0.0039 | True           |        1 |              1 |     0.8325 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.2215 |        0.0263 |         nan      | False          |      nan |            nan |     0.0778 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0039 |        0.4501 |         nan      | True           |        1 |              1 |     0.6189 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.2593 |        0.7954 |          -0.001  | False          |      nan |            nan |     0.8333 |
| H4b          | tagger   | corr(tag,fwd) original=0.1927 vs perturbed-context (want ~0) | -0.0144 |        0.1394 |           0.2071 | False          |      nan |            nan |     0.2787 |

## Reality check / SPA vs rules_only: RC p=0.800, SPA p=0.703

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2568 |    0.6944 |  0.2506 | 0.0253 | 0.5    |      0.4996 |          -0.716  |    0.254  |
| rules_tech|pit|gbt_mono      | 2568 |    0.7107 |  0.2524 | 0.0248 | 0.5056 |      0.4996 |          -0.2178 |    0.4206 |
| hitai_full|pit|gbt_mono      | 2568 |    0.6829 |  0.2449 | 0.0199 | 0.5893 |      0.4996 |           4.3934 |    1      |
| hitai_full|shuffled|gbt_mono | 2568 |    0.7091 |  0.2524 | 0.0238 | 0.5088 |      0.4996 |          -0.1022 |    0.4626 |
