# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 11004, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6606 |    0.696  |  0.2514 | 0.0288 | 0.5007 |      0.4938 |             0.0062 |                 0.6931 |             0.3996 |           0.0445 |          0.097  |          0.3597 |    0.537  |      -0.1285 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6606 |    0.6971 |  0.2519 | 0.034  | 0.4847 |      0.4938 |             0.0124 |                 0.6947 |            -0.4388 |          -0.8174 |          0.1082 |          0.2604 |    0.037  |      -0.3201 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6606 |    0.6955 |  0.2512 | 0.0314 | 0.4806 |      0.4938 |             0.0116 |                 0.6933 |            -0.4443 |          -0.4768 |          0.0118 |          0.5995 |    0.1653 |      -0.2664 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6606 |    0.6979 |  0.2518 | 0.0232 | 0.501  |      0.4938 |             0.0166 |                 0.694  |             0.1528 |          -0.2264 |          0.1421 |          0.6953 |    0.3197 |      -0.2303 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6606 |    0.6982 |  0.2525 | 0.0447 | 0.4998 |      0.4938 |             0.0423 |                 0.7012 |             0.2223 |          -0.5771 |          0.3315 |          0.8044 |    0.1181 |      -0.467  |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6606 |    0.7112 |  0.2529 | 0.0353 | 0.5048 |      0.4938 |             0.0216 |                 0.6948 |             0.5685 |           0.0197 |          0.2277 |          0.7675 |    0.5164 |      -0.3024 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6606 |    0.7053 |  0.2534 | 0.0538 | 0.4902 |      0.4938 |             0.0291 |                 0.6943 |            -0.1484 |          -0.6799 |          0.2157 |          0.7691 |    0.0834 |      -0.396  |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6606 |    0.7005 |  0.2532 | 0.0417 | 0.4964 |      0.4938 |             0.0414 |                 0.7015 |             0.1553 |          -0.6618 |          0.3376 |          0.7993 |    0.0881 |      -0.4495 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6606 |    0.7112 |  0.2529 | 0.0353 | 0.5048 |      0.4938 |             0.0216 |                 0.6948 |             0.5685 |           0.0197 |          0.2277 |          0.7675 |    0.5164 |      -0.3024 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6606 |    0.7133 |  0.2495 | 0.0427 | 0.5765 |      0.4938 |             0.0179 |                 0.6841 |             4.6067 |           3.2321 |          0.561  |          0.8697 |    1      |      -0.0665 |    0.7039 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6606 |    0.6999 |  0.2493 | 0.0287 | 0.5621 |      0.4938 |             0.033  |                 0.6896 |             3.2626 |           2.0735 |          0.5209 |          0.8569 |    1      |      -0.1084 |    0.0238 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6606 |    0.7027 |  0.248  | 0.0235 | 0.5749 |      0.4938 |             0.0122 |                 0.6829 |             4.8405 |           3.5562 |          0.5468 |          0.9204 |    1      |      -0.0436 |    0.8931 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6606 |    0.7026 |  0.2519 | 0.0276 | 0.5082 |      0.4938 |             0.0207 |                 0.6937 |            -0.2699 |          -1.1722 |          0.3591 |          0.6907 |    0.0105 |      -0.5771 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6606 |    0.7016 |  0.253  | 0.0411 | 0.5052 |      0.4938 |             0.0475 |                 0.7011 |             0.2148 |          -0.5823 |          0.3488 |          0.9335 |    0.1161 |      -0.4704 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6606 |    0.704  |  0.2516 | 0.0246 | 0.5144 |      0.4938 |             0.0209 |                 0.6947 |             0.6712 |           0.0445 |          0.2313 |          0.5881 |    0.5372 |      -0.2082 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6606 |    0.7068 |  0.2522 | 0.029  | 0.5004 |      0.4938 |             0.0323 |                 0.6959 |            -0.4209 |          -0.9192 |          0.1627 |          0.4967 |    0.0287 |      -0.3665 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6606 |    0.703  |  0.2526 | 0.0344 | 0.4966 |      0.4938 |             0.0451 |                 0.7019 |             0.2107 |          -0.5597 |          0.3194 |          0.8389 |    0.1256 |      -0.4257 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6606 |    0.711  |  0.2529 | 0.0342 | 0.5063 |      0.4938 |             0.0232 |                 0.6952 |             0.2781 |          -0.2855 |          0.2038 |          0.5798 |    0.2778 |      -0.2667 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6606 |    0.7021 |  0.249  | 0.0336 | 0.5768 |      0.4938 |             0.0175 |                 0.6841 |             4.5507 |           3.2234 |          0.5436 |          0.8548 |    1      |      -0.0495 |    0.6953 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6606 |    0.7054 |  0.2504 | 0.0413 | 0.549  |      0.4938 |             0.0318 |                 0.6892 |             2.4068 |           1.2406 |          0.5256 |          0.9394 |    0.9959 |      -0.1671 |    0.0001 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6606 |    0.697  |  0.2477 | 0.0243 | 0.5714 |      0.4938 |             0.0128 |                 0.6826 |             4.0558 |           2.8292 |          0.5165 |          0.889  |    1      |      -0.1269 |    0.3655 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -2.0275 |        0.9787 |          -0.0173 | False          | nan      |       nan      |     0.9787 |
| H3a          | logit    | rules_tech - hitai_full                                      | -0.9455 |        0.8278 |          -0.008  | False          | nan      |       nan      |     0.9328 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       | -1.2288 |        0.8904 |          -0.0107 | False          | nan      |       nan      |     0.9328 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         | -0.7951 |        0.7867 |          -0.0065 | False          | nan      |       nan      |     0.9328 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.8324 |        0.0001 |         nan      | False          | nan      |       nan      |     0.0028 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0405 |        0.0892 |         nan      | False          | nan      |       nan      |     0.3243 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.5645 |        0.1177 |          -0.0112 | False          | nan      |       nan      |     0.3243 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -0.5389 |        0.705  |          -0.0028 | False          | nan      |       nan      |     0.9124 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  0.1244 |        0.4505 |           0.0006 | False          | nan      |       nan      |     0.6194 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  0.3293 |        0.371  |           0.0017 | False          | nan      |       nan      |     0.6194 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  0.6953 |        0.2434 |           0.0032 | False          | nan      |       nan      |     0.4869 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.1062 |        0.0019 |         nan      | False          | nan      |       nan      |     0.0208 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0076 |        0.4009 |         nan      | False          | nan      |       nan      |     0.6194 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  1.6612 |        0.0967 |           0.0055 | False          | nan      |       nan      |     0.3243 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -1.0303 |        0.8486 |          -0.0072 | True           |   0.8723 |         1      |     0.9328 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  1.1022 |        0.1352 |           0.0085 | True           |   0.5897 |         0.676  |     0.3305 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  0.1607 |        0.4362 |           0.0013 | True           |   0.8723 |         1      |     0.6194 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  1.1854 |        0.1179 |           0.0083 | True           |   0.5897 |         0.5897 |     0.3243 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.8978 |        0.0038 |         nan      | False          | nan      |       nan      |     0.0276 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.031  |        0.1514 |         nan      | True           |   0.5897 |         0.757  |     0.3331 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.5942 |        0.1109 |          -0.0057 | False          | nan      |       nan      |     0.3243 |
| H4b          | tagger   | corr(tag,fwd) original=0.1904 vs perturbed-context (want ~0) |  0.008  |        0.4018 |           0.1824 | False          | nan      |       nan      |     0.6194 |

## Reality check / SPA vs rules_only: RC p=0.997, SPA p=1.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2724 |    0.6948 |  0.2508 | 0.0147 | 0.4892 |      0.4978 |          -0.2143 |    0.3869 |
| rules_tech|pit|gbt_mono      | 2724 |    0.7139 |  0.2569 | 0.0596 | 0.4919 |      0.4978 |          -1.2028 |    0.0541 |
| hitai_full|pit|gbt_mono      | 2724 |    0.6876 |  0.2468 | 0.0347 | 0.5824 |      0.4978 |           3.1229 |    1      |
| hitai_full|shuffled|gbt_mono | 2724 |    0.7067 |  0.2566 | 0.0647 | 0.4892 |      0.4978 |          -0.9047 |    0.112  |
