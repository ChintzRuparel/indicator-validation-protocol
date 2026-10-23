# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 20976, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 12600 |    0.6946 |  0.2503 | 0.0198 | 0.5004 |       0.499 |             0.0074 |                 0.6932 |             0.0648 |          -0.5433 |          0.0721 |          0.2513 |    0.2156 |      -0.0653 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 12600 |    0.6942 |  0.2505 | 0.0194 | 0.4957 |       0.499 |             0.0117 |                 0.6934 |            -0.8697 |          -1.7263 |          0.039  |          0.031  |    0.0046 |      -0.0457 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 12600 |    0.6942 |  0.2506 | 0.0237 | 0.4914 |       0.499 |             0.0094 |                 0.6933 |             0.0296 |          -0.724  |          0.1036 |          0.3047 |    0.1478 |      -0.0879 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 12600 |    0.6991 |  0.2518 | 0.0306 | 0.4935 |       0.499 |             0.0283 |                 0.6957 |             0.0008 |          -1.8962 |          0.2755 |          0.4327 |    0.0032 |      -0.165  |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 12600 |    0.7023 |  0.2521 | 0.0287 | 0.5013 |       0.499 |             0.0443 |                 0.7006 |            -0.1208 |          -1.9583 |          0.2778 |          0.4456 |    0.0024 |      -0.1879 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 12600 |    0.7008 |  0.2524 | 0.03   | 0.4992 |       0.499 |             0.0278 |                 0.6963 |            -0.4391 |          -2.1045 |          0.2652 |          0.514  |    0.001  |      -0.2162 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 12600 |    0.6978 |  0.2519 | 0.0258 | 0.4989 |       0.499 |             0.0277 |                 0.6955 |             0.2048 |          -1.4822 |          0.2474 |          0.3799 |    0.0171 |      -0.1331 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 12600 |    0.7023 |  0.2521 | 0.0287 | 0.5013 |       0.499 |             0.0443 |                 0.7006 |            -0.1208 |          -1.9583 |          0.2778 |          0.4456 |    0.0024 |      -0.1879 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 12600 |    0.7008 |  0.2524 | 0.03   | 0.4992 |       0.499 |             0.0278 |                 0.6963 |            -0.4391 |          -2.1045 |          0.2652 |          0.514  |    0.001  |      -0.2162 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 12600 |    0.6873 |  0.2459 | 0.016  | 0.5783 |       0.499 |             0.0116 |                 0.6832 |             8.1295 |           5.4815 |          0.5271 |          0.823  |    1      |      -0.018  |    0.0597 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 12600 |    0.6937 |  0.2479 | 0.0234 | 0.5678 |       0.499 |             0.0186 |                 0.6891 |             7.0011 |           4.3979 |          0.5161 |          0.7973 |    1      |      -0.0226 |    0.0012 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 12600 |    0.6888 |  0.2463 | 0.0262 | 0.5773 |       0.499 |             0.0185 |                 0.6836 |             8.3305 |           5.7316 |          0.4943 |          0.7432 |    1      |      -0.0279 |    0.1083 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 12600 |    0.6969 |  0.2517 | 0.0275 | 0.4953 |       0.499 |             0.0294 |                 0.6959 |            -0.041  |          -1.6999 |          0.3041 |          0.6374 |    0.0077 |      -0.195  |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 12600 |    0.6986 |  0.2519 | 0.0264 | 0.5034 |       0.499 |             0.0443 |                 0.7008 |            -0.1303 |          -2.1524 |          0.3004 |          0.4513 |    0.0009 |      -0.1817 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 12600 |    0.6999 |  0.2521 | 0.028  | 0.4999 |       0.499 |             0.0249 |                 0.696  |            -0.475  |          -2.2498 |          0.253  |          0.426  |    0.0006 |      -0.1996 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 12600 |    0.6972 |  0.2518 | 0.0314 | 0.4971 |       0.499 |             0.0344 |                 0.6966 |            -0.1319 |          -1.3019 |          0.2031 |          0.4901 |    0.031  |      -0.142  |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 12600 |    0.7005 |  0.2528 | 0.0214 | 0.5033 |       0.499 |             0.0414 |                 0.7022 |            -0.1931 |          -1.8206 |          0.236  |          0.3874 |    0.0041 |      -0.1646 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 12600 |    0.7018 |  0.2527 | 0.0313 | 0.5005 |       0.499 |             0.0282 |                 0.6968 |            -0.7345 |          -2.4312 |          0.2617 |          0.4936 |    0.0002 |      -0.2313 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 12600 |    0.6874 |  0.2463 | 0.0162 | 0.5765 |       0.499 |             0.0145 |                 0.683  |             9.4066 |           6.4626 |          0.5504 |          0.811  |    1      |      -0.0204 |    0.4162 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 12600 |    0.6903 |  0.2476 | 0.0166 | 0.5664 |       0.499 |             0.0209 |                 0.6888 |             7.5112 |           4.7594 |          0.5459 |          0.8448 |    1      |      -0.0273 |    0.0046 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 12600 |    0.6901 |  0.2467 | 0.0163 | 0.5737 |       0.499 |             0.0215 |                 0.6835 |             9.5112 |           6.5788 |          0.5494 |          0.82   |    1      |      -0.0298 |    0.4783 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  3.1259 |        0.0009 |           0.0072 | False          | nan      |       nan      |     0.0028 |
| H3a          | logit    | rules_tech - hitai_full                                      |  4.8272 |        0      |           0.0105 | False          | nan      |       nan      |     0      |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  4.3254 |        0      |           0.0095 | False          | nan      |       nan      |     0      |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  4.6954 |        0      |           0.0099 | False          | nan      |       nan      |     0      |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.5108 |        0.1308 |         nan      | False          | nan      |       nan      |     0.1609 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0606 |        0.0027 |         nan      | False          | nan      |       nan      |     0.0074 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.0547 |        0.9563 |           0.0001 | False          | nan      |       nan      |     0.9563 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  0.1588 |        0.4369 |           0.0005 | False          | nan      |       nan      |     0.4806 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  2.7407 |        0.0031 |           0.0086 | False          | nan      |       nan      |     0.0075 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  1.7983 |        0.0361 |           0.0049 | False          | nan      |       nan      |     0.0567 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  2.5644 |        0.0052 |           0.0068 | False          | nan      |       nan      |     0.0114 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.2335 |        0.0255 |         nan      | False          | nan      |       nan      |     0.0432 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0331 |        0.0643 |         nan      | False          | nan      |       nan      |     0.0884 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.5078 |        0.1316 |          -0.0034 | False          | nan      |       nan      |     0.1609 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  1.9593 |        0.025  |           0.0054 | True           |   0.0277 |         0.1252 |     0.0432 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  4.2903 |        0      |           0.012  | True           |   0      |         0      |     0      |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  4.155  |        0      |           0.0111 | True           |   0      |         0.0001 |     0.0001 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  4.9167 |        0      |           0.013  | True           |   0      |         0      |     0      |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.8997 |        0.0575 |         nan      | False          | nan      |       nan      |     0.0843 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0479 |        0.0138 |         nan      | True           |   0.0277 |         0.0692 |     0.0277 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.7889 |        0.4302 |           0.0013 | False          | nan      |       nan      |     0.4806 |
| H4b          | tagger   | corr(tag,fwd) original=0.1746 vs perturbed-context (want ~0) | -0.0043 |        0.5338 |           0.1789 | False          | nan      |       nan      |     0.5592 |

## Reality check / SPA vs rules_only: RC p=0.003, SPA p=0.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5136 |    0.6932 |  0.25   | 0.0003 | 0.5    |       0.506 |          -0.9423 |    0.1937 |
| rules_tech|pit|gbt_mono      | 5136 |    0.6939 |  0.2504 | 0.0204 | 0.4941 |       0.506 |          -2.0495 |    0.0257 |
| hitai_full|pit|gbt_mono      | 5136 |    0.6927 |  0.2479 | 0.0239 | 0.562  |       0.506 |           6.8707 |    1      |
| hitai_full|shuffled|gbt_mono | 5136 |    0.6941 |  0.2505 | 0.0245 | 0.4916 |       0.506 |          -1.9144 |    0.041  |
