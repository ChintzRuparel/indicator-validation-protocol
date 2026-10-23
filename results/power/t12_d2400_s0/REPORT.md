# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 22008, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 13212 |    0.6939 |  0.2502 | 0.0175 | 0.503  |      0.5121 |             0.014  |                 0.6936 |             0.9557 |           0.2572 |          0.1053 |          0.2759 |    0.7049 |      -0.0997 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 13212 |    0.6937 |  0.2502 | 0.0188 | 0.4979 |      0.5121 |             0.0184 |                 0.6939 |             0.4338 |          -0.1434 |          0.0855 |          0.2581 |    0.3825 |      -0.1362 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 13212 |    0.6933 |  0.2501 | 0.0151 | 0.5025 |      0.5121 |             0.0145 |                 0.6935 |             0.6993 |           0.2681 |          0.0594 |          0.2389 |    0.7132 |      -0.0505 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 13212 |    0.6965 |  0.2511 | 0.0227 | 0.5005 |      0.5121 |             0.0152 |                 0.6943 |             0.4434 |          -0.4799 |          0.2224 |          0.5806 |    0.1582 |      -0.1372 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 13212 |    0.6971 |  0.2513 | 0.0197 | 0.4978 |      0.5121 |             0.0469 |                 0.7017 |             0.5217 |          -0.3078 |          0.1519 |          0.3816 |    0.2608 |      -0.1167 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 13212 |    0.6951 |  0.2509 | 0.0148 | 0.4975 |      0.5121 |             0.0388 |                 0.698  |             0.5944 |          -0.1812 |          0.1203 |          0.2736 |    0.3526 |      -0.1086 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 13212 |    0.6986 |  0.2514 | 0.0196 | 0.4945 |      0.5121 |             0.0317 |                 0.6955 |             0.8174 |           0.2397 |          0.0711 |          0.2087 |    0.6927 |      -0.0397 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 13212 |    0.6972 |  0.2513 | 0.0193 | 0.5004 |      0.5121 |             0.0476 |                 0.7016 |             0.7909 |           0.015  |          0.1309 |          0.3334 |    0.5125 |      -0.1114 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 13212 |    0.6961 |  0.2511 | 0.0147 | 0.4972 |      0.5121 |             0.0393 |                 0.698  |             0.5969 |          -0.0899 |          0.0969 |          0.2429 |    0.4255 |      -0.1094 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 13212 |    0.6888 |  0.2476 | 0.011  | 0.5631 |      0.5121 |             0.0309 |                 0.6881 |             5.7306 |           3.7745 |          0.5405 |          0.8476 |    1      |      -0.0378 |    0.723  |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 13212 |    0.692  |  0.2481 | 0.0076 | 0.5551 |      0.5121 |             0.0328 |                 0.6913 |             4.8941 |           3.0139 |          0.5182 |          0.7953 |    1      |      -0.0596 |    0.1657 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 13212 |    0.6935 |  0.2482 | 0.0127 | 0.5597 |      0.5121 |             0.0275 |                 0.6877 |             5.4981 |           3.6246 |          0.5269 |          0.8215 |    1      |      -0.0409 |    0.6119 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 13212 |    0.6975 |  0.2514 | 0.0238 | 0.4953 |      0.5121 |             0.029  |                 0.6957 |             0.6435 |           0.1162 |          0.0985 |          0.3823 |    0.596  |      -0.0596 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 13212 |    0.6972 |  0.2514 | 0.0185 | 0.4953 |      0.5121 |             0.0514 |                 0.7022 |             0.5836 |          -0.4696 |          0.2365 |          0.526  |    0.1635 |      -0.1524 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 13212 |    0.6957 |  0.251  | 0.0156 | 0.4973 |      0.5121 |             0.0385 |                 0.698  |             0.4292 |          -0.2144 |          0.0928 |          0.2399 |    0.3273 |      -0.1128 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 13212 |    0.6966 |  0.2512 | 0.0182 | 0.497  |      0.5121 |             0.0311 |                 0.6958 |             0.604  |           0.0049 |          0.0822 |          0.2415 |    0.5041 |      -0.0796 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 13212 |    0.7015 |  0.2517 | 0.0202 | 0.4953 |      0.5121 |             0.0527 |                 0.7022 |             0.3881 |          -0.3389 |          0.134  |          0.3642 |    0.2397 |      -0.1716 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 13212 |    0.6962 |  0.2511 | 0.016  | 0.5    |      0.5121 |             0.0389 |                 0.6979 |             0.4165 |          -0.2707 |          0.1006 |          0.2492 |    0.2858 |      -0.1458 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 13212 |    0.6894 |  0.2474 | 0.0089 | 0.5645 |      0.5121 |             0.0316 |                 0.6886 |             6.5821 |           4.5356 |          0.5417 |          0.8052 |    1      |      -0.0541 |    0.9835 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 13212 |    0.6906 |  0.248  | 0.0084 | 0.5531 |      0.5121 |             0.0348 |                 0.6922 |             5.283  |           3.3562 |          0.5054 |          0.7521 |    1      |      -0.0406 |    0.3936 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 13212 |    0.6935 |  0.2481 | 0.009  | 0.56   |      0.5121 |             0.0275 |                 0.6883 |             6.1766 |           4.1404 |          0.5416 |          0.8031 |    1      |      -0.0509 |    0.9102 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  2.8295 |        0.0023 |           0.0051 | False          | nan      |       nan      |     0.0103 |
| H3a          | logit    | rules_tech - hitai_full                                      |  4.408  |        0      |           0.0098 | False          | nan      |       nan      |     0.0001 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  4.5818 |        0      |           0.0087 | False          | nan      |       nan      |     0.0001 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  4.2025 |        0      |           0.0078 | False          | nan      |       nan      |     0.0001 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.0488 |        0.0405 |         nan      | False          | nan      |       nan      |     0.0817 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0331 |        0.0601 |         nan      | False          | nan      |       nan      |     0.1101 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.3843 |        0.7007 |           0.0005 | False          | nan      |       nan      |     0.7341 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  0.8302 |        0.2032 |           0.0017 | False          | nan      |       nan      |     0.2794 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  2.7033 |        0.0034 |           0.0052 | False          | nan      |       nan      |     0.0108 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  2.7589 |        0.0029 |           0.0053 | False          | nan      |       nan      |     0.0106 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  3.8259 |        0.0001 |           0.0095 | False          | nan      |       nan      |     0.0004 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.19   |        0.234  |         nan      | False          | nan      |       nan      |     0.3029 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0371 |        0.0408 |         nan      | False          | nan      |       nan      |     0.0817 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.8541 |        0.393  |          -0.0014 | False          | nan      |       nan      |     0.4656 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -0.0736 |        0.5293 |          -0.0002 | True           |   0.5293 |         1      |     0.5823 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  1.0784 |        0.1404 |           0.0025 | True           |   0.4624 |         0.7021 |     0.2207 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  0.9886 |        0.1614 |           0.0022 | True           |   0.4624 |         0.8071 |     0.2368 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  1.1973 |        0.1156 |           0.0027 | True           |   0.4624 |         0.578  |     0.1956 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.0484 |        0.0405 |         nan      | False          | nan      |       nan      |     0.0817 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0563 |        0.0041 |         nan      | True           |   0.0205 |         0.0205 |     0.0112 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -0.0258 |        0.9794 |          -0.0001 | False          | nan      |       nan      |     0.9794 |
| H4b          | tagger   | corr(tag,fwd) original=0.1658 vs perturbed-context (want ~0) | -0.0056 |        0.4021 |           0.1715 | False          | nan      |       nan      |     0.4656 |

## Reality check / SPA vs rules_only: RC p=0.023, SPA p=0.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 5448 |    0.6936 |  0.2502 | 0.0093 | 0.4966 |      0.5051 |          -0.675  |    0.1862 |
| rules_tech|pit|gbt_mono      | 5448 |    0.6937 |  0.2503 | 0.0091 | 0.4965 |      0.5051 |           0.3936 |    0.7018 |
| hitai_full|pit|gbt_mono      | 5448 |    0.6825 |  0.2442 | 0.0139 | 0.5889 |      0.5051 |           5.2912 |    1      |
| hitai_full|shuffled|gbt_mono | 5448 |    0.6943 |  0.2506 | 0.0123 | 0.4961 |      0.5051 |          -0.4445 |    0.2742 |
