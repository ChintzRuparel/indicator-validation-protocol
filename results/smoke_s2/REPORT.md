# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 5244, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 3150 |    0.7343 |  0.2566 | 0.0521 | 0.4934 |       0.506 |             0.0092 |                 0.6946 |             0.0322 |          -0.3555 |          0.0737 |          0.2171 |    0.3041 |      -0.0844 |    0.0016 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 3150 |    0.7002 |  0.2533 | 0.0277 | 0.5081 |       0.506 |             0.009  |                 0.6943 |            -0.2563 |          -0.5869 |          0.0463 |          0.1079 |    0.2007 |      -0.0672 |    0.0006 |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 3150 |    0.6969 |  0.2519 | 0.0181 | 0.5007 |       0.506 |             0.008  |                 0.6934 |            -0.4229 |          -0.6162 |          0.0502 |          0.4    |    0.1842 |      -0.1378 |    0.0004 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 3150 |    0.769  |  0.2614 | 0.0432 | 0.4908 |       0.506 |             0.0378 |                 0.7042 |             0.374  |          -0.0813 |          0.0946 |          0.267  |    0.4533 |      -0.1085 |    0.0054 |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 3150 |    0.7166 |  0.2551 | 0.0451 | 0.5046 |       0.506 |             0.0993 |                 0.72   |             0.3394 |          -0.3797 |          0.1676 |          0.3054 |    0.2932 |      -0.145  |    0.0015 |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 3150 |    0.7148 |  0.2559 | 0.0466 | 0.5087 |       0.506 |             0.0792 |                 0.7103 |             0.5886 |          -0.0634 |          0.1473 |          0.3035 |    0.4635 |      -0.1579 |    0.0058 |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 3150 |    0.7554 |  0.26   | 0.0537 | 0.4702 |       0.506 |             0.0405 |                 0.7066 |            -0.9171 |          -1.2548 |          0.0971 |          0.48   |    0.0335 |      -0.2205 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 3150 |    0.7166 |  0.2551 | 0.0451 | 0.5046 |       0.506 |             0.0993 |                 0.72   |             0.3394 |          -0.3797 |          0.1676 |          0.3054 |    0.2932 |      -0.145  |    0.0015 |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 3150 |    0.7148 |  0.2559 | 0.0466 | 0.5087 |       0.506 |             0.0792 |                 0.7103 |             0.5886 |          -0.0634 |          0.1473 |          0.3035 |    0.4635 |      -0.1579 |    0.0058 |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 3150 |    0.7286 |  0.2564 | 0.0558 | 0.5288 |       0.506 |             0.0335 |                 0.6955 |             2.7025 |           1.7354 |          0.367  |          0.779  |    0.9929 |      -0.1203 |    0.5279 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 3150 |    0.7294 |  0.2569 | 0.0333 | 0.5224 |       0.506 |             0.0844 |                 0.7108 |             1.6748 |           0.627  |          0.3578 |          0.6248 |    0.8177 |      -0.1282 |    0.0629 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 3150 |    0.7313 |  0.2578 | 0.0441 | 0.5349 |       0.506 |             0.0586 |                 0.6997 |             3.0813 |           1.9618 |          0.4035 |          0.7886 |    0.9975 |      -0.072  |    0.6538 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 3150 |    0.7369 |  0.2573 | 0.0435 | 0.4812 |       0.506 |             0.0509 |                 0.7073 |            -0.1806 |          -0.7451 |          0.1451 |          0.4479 |    0.1413 |      -0.1118 |    0.0002 |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 3150 |    0.7222 |  0.2565 | 0.0414 | 0.5085 |       0.506 |             0.0978 |                 0.7202 |             0.0163 |          -0.84   |          0.1873 |          0.2857 |    0.1137 |      -0.1799 |    0.0001 |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 3150 |    0.7142 |  0.2555 | 0.051  | 0.5005 |       0.506 |             0.0727 |                 0.7098 |             0.5005 |          -0.1091 |          0.1543 |          0.3987 |    0.4375 |      -0.1071 |    0.0048 |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 3150 |    0.7117 |  0.2566 | 0.0492 | 0.4849 |       0.506 |             0.0554 |                 0.7062 |            -0.0825 |          -0.7169 |          0.1749 |          0.4556 |    0.1508 |      -0.1239 |    0.0003 |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 3150 |    0.7167 |  0.2556 | 0.0573 | 0.5047 |       0.506 |             0.0967 |                 0.7206 |            -0.1171 |          -0.8954 |          0.2105 |          0.4619 |    0.1007 |      -0.1645 |    0.0001 |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 3150 |    0.7365 |  0.2578 | 0.0654 | 0.4925 |       0.506 |             0.0741 |                 0.7093 |            -0.0405 |          -0.5961 |          0.1797 |          0.6111 |    0.1953 |      -0.1507 |    0.0005 |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 3150 |    0.7171 |  0.2576 | 0.0513 | 0.5094 |       0.506 |             0.0237 |                 0.6956 |             0.972  |           0.1231 |          0.3105 |          0.72   |    0.5703 |      -0.1696 |    0.0123 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 3150 |    0.7143 |  0.2535 | 0.0254 | 0.53   |       0.506 |             0.082  |                 0.7103 |             1.9006 |           0.9167 |          0.3356 |          0.6133 |    0.9082 |      -0.1108 |    0.1323 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 3150 |    0.7508 |  0.2587 | 0.0458 | 0.5234 |       0.506 |             0.0614 |                 0.7018 |             2.427  |           1.286  |          0.3857 |          0.6889 |    0.9675 |      -0.0637 |    0.2831 |         21 |

## Hypothesis tests

| hypothesis   | model        | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:-------------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit        | rules_only - hitai_full (logloss)                            |  0.2864 |        0.3873 |           0.0057 | False          |      nan |            nan |     0.65   |
| H3a          | logit        | rules_tech - hitai_full                                      |  2.2237 |        0.0131 |           0.0267 | False          |      nan |            nan |     0.0467 |
| H3b          | logit        | hitai_full[shuffled] - hitai_full[pit]                       |  0.9575 |        0.1692 |           0.0083 | False          |      nan |            nan |     0.3844 |
| H3c          | logit        | hitai_full[lagged] - hitai_full[pit]                         | -1.5274 |        0.9367 |          -0.0169 | False          |      nan |            nan |     0.998  |
| H2a          | logit        | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.2983 |        0      |         nan      | False          |      nan |            nan |     0.0001 |
| H2b          | logit        | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0597 |        0.0854 |         nan      | False          |      nan |            nan |     0.2135 |
| H4a          | logit        | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.1439 |        0.2527 |          -0.0115 | False          |      nan |            nan |     0.5264 |
| H1           | gbt          | rules_only - hitai_full (logloss)                            | -2.8768 |        0.998  |          -0.0292 | False          |      nan |            nan |     0.998  |
| H3a          | gbt          | rules_tech - hitai_full                                      | -2.0021 |        0.9774 |          -0.0128 | False          |      nan |            nan |     0.998  |
| H3b          | gbt          | hitai_full[shuffled] - hitai_full[pit]                       | -1.0786 |        0.8596 |          -0.0072 | False          |      nan |            nan |     0.998  |
| H3c          | gbt          | hitai_full[lagged] - hitai_full[pit]                         | -1.5803 |        0.943  |          -0.0127 | False          |      nan |            nan |     0.998  |
| H2a          | gbt          | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  6.6608 |        0      |         nan      | False          |      nan |            nan |     0      |
| H2b          | gbt          | Spearman(|p-.5|, hit) on non-overlapping dates               | -0.0105 |        0.5955 |         nan      | False          |      nan |            nan |     0.9304 |
| H4a          | gbt          | masked - unmasked logloss (two-sided; want NOT rejected)     | -2.062  |        0.0392 |          -0.015  | False          |      nan |            nan |     0.1089 |
| H1           | gbt_mono     | rules_only - hitai_full (logloss)                            | -2.8829 |        0.998  |          -0.0344 | True           |        1 |              1 |     0.998  |
| H3a          | gbt_mono     | rules_tech - hitai_full                                      | -1.9387 |        0.9737 |          -0.0165 | True           |        1 |              1 |     0.998  |
| H3b          | gbt_mono     | hitai_full[shuffled] - hitai_full[pit]                       | -1.8441 |        0.9674 |          -0.0171 | True           |        1 |              1 |     0.998  |
| H3c          | gbt_mono     | hitai_full[lagged] - hitai_full[pit]                         |  0.4255 |        0.3352 |           0.0052 | True           |        1 |              1 |     0.6447 |
| H2a          | gbt_mono     | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  5.9513 |        0      |         nan      | False          |      nan |            nan |     0      |
| H2b          | gbt_mono     | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0122 |        0.39   |         nan      | True           |        1 |              1 |     0.65   |
| H4a          | gbt_mono     | masked - unmasked logloss (two-sided; want NOT rejected)     |  2.1534 |        0.0313 |           0.0195 | False          |      nan |            nan |     0.0978 |
| H4b          | tagger       | corr(tag,fwd) original=0.1681 vs perturbed-context (want ~0) |  0.0016 |        0.9099 |           0.1665 | False          |      nan |            nan |     0.998  |
| H4-demo      | leaky_tagger | corr(tag,fwd) unmasked                                       |  0.8659 |        0      |         nan      | False          |      nan |            nan |     0      |
| H4-demo      | leaky_tagger | corr(tag,fwd) masked                                         |  0.169  |        0      |         nan      | False          |      nan |            nan |     0      |
| H4-demo      | leaky_tagger | corr(tag,fwd) perturbed                                      |  0.8659 |        0      |         nan      | False          |      nan |            nan |     0      |

## Reality check / SPA vs rules_only: RC p=0.973, SPA p=1.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 1284 |    0.6942 |  0.2505 | 0.0232 | 0.5    |      0.4984 |           0.492  |    0.6741 |
| rules_tech|pit|gbt_mono      | 1284 |    0.6958 |  0.2513 | 0.0274 | 0.5162 |      0.4984 |           0.939  |    0.8047 |
| hitai_full|pit|gbt_mono      | 1284 |    0.7124 |  0.2505 | 0.0258 | 0.5603 |      0.4984 |           1.9158 |    0.9603 |
| hitai_full|shuffled|gbt_mono | 1284 |    0.7092 |  0.2525 | 0.0274 | 0.5269 |      0.4984 |           0.9494 |    0.8073 |
