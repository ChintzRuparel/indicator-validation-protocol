# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 5244, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 3150 |    0.7113 |  0.2571 | 0.0654 | 0.4746 |      0.4822 |             0.0206 |                 0.6941 |            -0.7169 |          -1.1139 |          0.1562 |          0.781  |    0.0529 |      -0.3704 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 3150 |    0.7053 |  0.256  | 0.0761 | 0.474  |      0.4822 |             0.0117 |                 0.6936 |            -0.9136 |          -1.2744 |          0.1425 |          0.7702 |    0.0325 |      -0.357  |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 3150 |    0.7042 |  0.2555 | 0.0574 | 0.469  |      0.4822 |             0.0028 |                 0.6922 |            -0.6701 |          -0.7033 |          0.0133 |          0.8    |    0.1543 |      -0.2957 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 3150 |    0.7477 |  0.2637 | 0.0894 | 0.4684 |      0.4822 |             0.0271 |                 0.6969 |            -0.1888 |          -0.7699 |          0.2419 |          0.8692 |    0.1346 |      -0.2788 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 3150 |    0.7111 |  0.2581 | 0.0775 | 0.4759 |      0.4822 |             0.0757 |                 0.7141 |            -0.5871 |          -0.9626 |          0.1454 |          0.801  |    0.0819 |      -0.3654 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 3150 |    0.7157 |  0.2585 | 0.0695 | 0.4676 |      0.4822 |             0.0475 |                 0.7026 |            -0.6922 |          -1.2174 |          0.2006 |          0.779  |    0.0398 |      -0.3381 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 3150 |    0.7458 |  0.2619 | 0.0832 | 0.4595 |      0.4822 |             0.0425 |                 0.6987 |            -1.0089 |          -1.5314 |          0.2079 |          0.753  |    0.0133 |      -0.4351 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 3150 |    0.7151 |  0.2581 | 0.0788 | 0.4775 |      0.4822 |             0.0728 |                 0.7138 |            -0.6765 |          -1.025  |          0.1371 |          0.7648 |    0.0699 |      -0.3314 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 3150 |    0.7157 |  0.2585 | 0.0695 | 0.4676 |      0.4822 |             0.0475 |                 0.7026 |            -0.6922 |          -1.2174 |          0.2006 |          0.779  |    0.0398 |      -0.3381 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 3150 |    0.7107 |  0.2542 | 0.0674 | 0.5328 |      0.4822 |             0.0204 |                 0.6886 |             2.531  |           1.3705 |          0.4508 |          0.8146 |    0.9757 |      -0.1383 |    0.1212 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 3150 |    0.723  |  0.2574 | 0.0566 | 0.5137 |      0.4822 |             0.0538 |                 0.7028 |             1.9688 |           0.9743 |          0.3651 |          0.747  |    0.9202 |      -0.1938 |    0.0405 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 3150 |    0.7161 |  0.255  | 0.0519 | 0.5281 |      0.4822 |             0.0311 |                 0.691  |             2.1733 |           1.1416 |          0.3962 |          0.7625 |    0.9511 |      -0.0962 |    0.0655 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 3150 |    0.7392 |  0.2618 | 0.0808 | 0.4619 |      0.4822 |             0.0399 |                 0.6995 |            -0.5113 |          -1.1054 |          0.2667 |          0.9181 |    0.0557 |      -0.4546 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 3150 |    0.7111 |  0.2581 | 0.0757 | 0.4727 |      0.4822 |             0.08   |                 0.7155 |            -1.0342 |          -1.4123 |          0.1467 |          0.7946 |    0.0209 |      -0.3599 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 3150 |    0.7159 |  0.2581 | 0.0661 | 0.4696 |      0.4822 |             0.051  |                 0.7027 |            -0.6284 |          -1.1374 |          0.1898 |          0.7625 |    0.0509 |      -0.3455 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 3150 |    0.7249 |  0.2611 | 0.0759 | 0.4621 |      0.4822 |             0.0475 |                 0.7009 |            -1.1351 |          -1.5521 |          0.1695 |          0.774  |    0.0125 |      -0.4812 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 3150 |    0.714  |  0.258  | 0.0717 | 0.4796 |      0.4822 |             0.0777 |                 0.7128 |            -0.8578 |          -1.4281 |          0.2032 |          0.6705 |    0.0199 |      -0.4047 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 3150 |    0.7211 |  0.2596 | 0.0759 | 0.465  |      0.4822 |             0.0627 |                 0.7022 |            -1.0309 |          -1.4415 |          0.1676 |          0.7997 |    0.0195 |      -0.3993 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 3150 |    0.7138 |  0.255  | 0.0472 | 0.536  |      0.4822 |             0.0249 |                 0.686  |             2.6046 |           1.5015 |          0.4267 |          0.8305 |    0.9855 |      -0.1455 |    0.1608 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 3150 |    0.707  |  0.255  | 0.0626 | 0.5227 |      0.4822 |             0.0464 |                 0.6977 |             2.0704 |           1.1469 |          0.3873 |          0.9143 |    0.952  |      -0.1369 |    0.0663 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 3150 |    0.7078 |  0.2542 | 0.0635 | 0.5297 |      0.4822 |             0.0283 |                 0.6883 |             1.9344 |           1.1063 |          0.3702 |          0.9657 |    0.9447 |      -0.1794 |    0.0603 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            |  0.067  |        0.4733 |           0.0006 | False          |      nan |            nan |     0.8161 |
| H3a          | logit    | rules_tech - hitai_full                                      |  3.2678 |        0.0005 |           0.0351 | False          |      nan |            nan |     0.0032 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  3.0167 |        0.0013 |           0.0285 | False          |      nan |            nan |     0.0056 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  1.7673 |        0.0386 |           0.0141 | False          |      nan |            nan |     0.1083 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.4389 |        0.0006 |         nan      | False          |      nan |            nan |     0.0032 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0766 |        0.0394 |         nan      | False          |      nan |            nan |     0.1083 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.5213 |        0.6022 |           0.0031 | False          |      nan |            nan |     0.828  |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -2.3559 |        0.9908 |          -0.0177 | False          |      nan |            nan |     0.9908 |
| H3a          | gbt      | rules_tech - hitai_full                                      | -0.9393 |        0.8262 |          -0.0079 | False          |      nan |            nan |     0.9908 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       | -1.6048 |        0.9457 |          -0.0119 | False          |      nan |            nan |     0.9908 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         | -1.2346 |        0.8915 |          -0.009  | False          |      nan |            nan |     0.9908 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.1063 |        0      |         nan      | False          |      nan |            nan |     0.0009 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               | -0.0541 |        0.8927 |         nan      | False          |      nan |            nan |     0.9908 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -2.6821 |        0.0073 |          -0.016  | False          |      nan |            nan |     0.0268 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -1.635  |        0.949  |          -0.0118 | True           |        1 |              1 |     0.9908 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      | -0.0484 |        0.5193 |          -0.0003 | True           |        1 |              1 |     0.8161 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       | -0.0191 |        0.5076 |          -0.0001 | True           |        1 |              1 |     0.8161 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  0.5915 |        0.2771 |           0.005  | True           |        1 |              1 |     0.6096 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.8857 |        0.0001 |         nan      | False          |      nan |            nan |     0.0011 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               | -0.0108 |        0.5977 |         nan      | True           |        1 |              1 |     0.828  |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.2397 |        0.2151 |          -0.0083 | False          |      nan |            nan |     0.5258 |
| H4b          | tagger   | corr(tag,fwd) original=0.1675 vs perturbed-context (want ~0) | -0.0099 |        0.4757 |           0.1773 | False          |      nan |            nan |     0.8161 |

## Reality check / SPA vs rules_only: RC p=1.000, SPA p=1.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 1284 |    0.6938 |  0.2503 | 0.024  | 0.5    |      0.5164 |           0      |  nan      |
| rules_tech|pit|gbt_mono      | 1284 |    0.7289 |  0.255  | 0.0317 | 0.5003 |      0.5164 |          -2.0972 |    0.0257 |
| hitai_full|pit|gbt_mono      | 1284 |    0.7083 |  0.2521 | 0.044  | 0.5461 |      0.5164 |           0.7538 |    0.7535 |
| hitai_full|shuffled|gbt_mono | 1284 |    0.7284 |  0.2549 | 0.0383 | 0.4899 |      0.5164 |          -1.4331 |    0.0916 |
