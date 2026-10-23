# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 11004, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6606 |    0.696  |  0.2507 | 0.0173 | 0.5024 |      0.5204 |             0.0148 |                 0.6951 |             1.0371 |           0.7499 |          0.0775 |          0.426  |    0.9413 |      -0.1182 |    0.0002 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6606 |    0.6963 |  0.2508 | 0.0176 | 0.5032 |      0.5204 |             0.015  |                 0.6949 |             0.7224 |           0.4565 |          0.0687 |          0.3739 |    0.8297 |      -0.1048 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6606 |    0.6934 |  0.2501 | 0.0161 | 0.5004 |      0.5204 |             0.0203 |                 0.6944 |             0.5204 |           0.1795 |          0.0745 |          0.2714 |    0.6461 |      -0.1339 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6606 |    0.7001 |  0.252  | 0.0177 | 0.5091 |      0.5204 |             0.0147 |                 0.6942 |             1.0624 |           0.5315 |          0.1496 |          0.454  |    0.8661 |      -0.0924 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6606 |    0.7018 |  0.2519 | 0.0271 | 0.5076 |      0.5204 |             0.0566 |                 0.706  |            -0.0149 |          -1.1061 |          0.347  |          0.6517 |    0.0102 |      -0.4289 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6606 |    0.7204 |  0.2532 | 0.0262 | 0.5135 |      0.5204 |             0.036  |                 0.6982 |             0.6335 |          -0.3551 |          0.2832 |          0.5259 |    0.2287 |      -0.2134 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6606 |    0.7265 |  0.2553 | 0.0196 | 0.5014 |      0.5204 |             0.0239 |                 0.6964 |             0.3338 |          -0.1827 |          0.1247 |          0.3556 |    0.3515 |      -0.1239 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6606 |    0.7033 |  0.2517 | 0.0193 | 0.5102 |      0.5204 |             0.0598 |                 0.7057 |             0.1784 |          -0.9937 |          0.3411 |          0.5811 |    0.0186 |      -0.3754 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6606 |    0.7204 |  0.2532 | 0.0262 | 0.5135 |      0.5204 |             0.036  |                 0.6982 |             0.6335 |          -0.3551 |          0.2832 |          0.5259 |    0.2287 |      -0.2134 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6606 |    0.6962 |  0.2501 | 0.0268 | 0.558  |      0.5204 |             0.0284 |                 0.6894 |             4.1928 |           2.6975 |          0.5286 |          0.782  |    1      |      -0.0737 |    0.7022 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6606 |    0.7124 |  0.2507 | 0.0328 | 0.5459 |      0.5204 |             0.0542 |                 0.6994 |             2.7726 |           1.36   |          0.4316 |          0.6367 |    0.9977 |      -0.1181 |    0.012  |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6606 |    0.7159 |  0.2509 | 0.0276 | 0.5558 |      0.5204 |             0.03   |                 0.6902 |             3.1195 |           1.7128 |          0.4497 |          0.6614 |    0.9998 |      -0.0835 |    0.0653 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6606 |    0.7049 |  0.2528 | 0.0219 | 0.5037 |      0.5204 |             0.0281 |                 0.6972 |             0.6345 |          -0.0508 |          0.1714 |          0.3798 |    0.4578 |      -0.1363 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6606 |    0.7003 |  0.2517 | 0.0245 | 0.511  |      0.5204 |             0.0592 |                 0.7057 |             0.0427 |          -1.0443 |          0.3445 |          0.6322 |    0.0142 |      -0.4197 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6606 |    0.719  |  0.253  | 0.0266 | 0.5135 |      0.5204 |             0.0378 |                 0.6984 |             0.7919 |          -0.1964 |          0.2823 |          0.5198 |    0.3407 |      -0.2067 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6606 |    0.6986 |  0.2522 | 0.0161 | 0.509  |      0.5204 |             0.0269 |                 0.6965 |             0.6832 |           0.166  |          0.1435 |          0.4242 |    0.6355 |      -0.1386 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6606 |    0.7035 |  0.252  | 0.0255 | 0.509  |      0.5204 |             0.06   |                 0.7062 |            -0.1354 |          -1.3553 |          0.3559 |          0.5746 |    0.0022 |      -0.4734 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6606 |    0.7131 |  0.2526 | 0.0247 | 0.5196 |      0.5204 |             0.0374 |                 0.6982 |             0.4168 |          -0.5763 |          0.2863 |          0.5324 |    0.1131 |      -0.2592 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6606 |    0.7077 |  0.2509 | 0.0316 | 0.5551 |      0.5204 |             0.0283 |                 0.6901 |             4.6879 |           3.212  |          0.5322 |          0.8094 |    1      |      -0.0718 |    0.9447 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6606 |    0.7025 |  0.2501 | 0.0285 | 0.5455 |      0.5204 |             0.0522 |                 0.7    |             2.9201 |           1.5843 |          0.4812 |          0.8191 |    0.9996 |      -0.0765 |    0.0354 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6606 |    0.7058 |  0.2507 | 0.0295 | 0.5533 |      0.5204 |             0.0308 |                 0.6906 |             3.3822 |           1.9667 |          0.5112 |          0.8456 |    1      |      -0.0995 |    0.1607 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -0.0593 |        0.5237 |          -0.0002 | False          | nan      |       nan      |     0.768  |
| H3a          | logit    | rules_tech - hitai_full                                      |  3.3088 |        0.0005 |           0.0303 | False          | nan      |       nan      |     0.0034 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  1.8929 |        0.0292 |           0.0086 | False          | nan      |       nan      |     0.1258 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  0.6685 |        0.2519 |           0.0024 | False          | nan      |       nan      |     0.4573 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.6206 |        0.0003 |         nan      | False          | nan      |       nan      |     0.0032 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0518 |        0.0427 |         nan      | False          | nan      |       nan      |     0.1343 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     |  2.1163 |        0.0343 |           0.0114 | False          | nan      |       nan      |     0.1258 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -2.42   |        0.9922 |          -0.0162 | False          | nan      |       nan      |     0.9983 |
| H3a          | gbt      | rules_tech - hitai_full                                      | -1.3473 |        0.9111 |          -0.0091 | False          | nan      |       nan      |     0.9983 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       | -1.9895 |        0.9767 |          -0.0121 | False          | nan      |       nan      |     0.9983 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         | -1.352  |        0.9118 |          -0.0089 | False          | nan      |       nan      |     0.9983 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.325  |        0.0009 |         nan      | False          | nan      |       nan      |     0.0049 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0379 |        0.1041 |         nan      | False          | nan      |       nan      |     0.2544 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.628  |        0.1035 |          -0.0099 | False          | nan      |       nan      |     0.2544 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -2.9359 |        0.9983 |          -0.0226 | True           |   1      |         1      |     0.9983 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  0.6121 |        0.2702 |           0.0045 | True           |   1      |         1      |     0.4573 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  0.407  |        0.342  |           0.0031 | True           |   1      |         1      |     0.5374 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         | -0.3392 |        0.6328 |          -0.0028 | True           |   1      |         1      |     0.8189 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  4.7786 |        0      |         nan      | False          | nan      |       nan      |     0      |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0297 |        0.162  |         nan      | True           |   0.8101 |         0.8101 |     0.324  |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.4204 |        0.1555 |          -0.0101 | False          | nan      |       nan      |     0.324  |
| H4b          | tagger   | corr(tag,fwd) original=0.1675 vs perturbed-context (want ~0) | -0.0054 |        0.5725 |           0.1729 | False          | nan      |       nan      |     0.7872 |

## Reality check / SPA vs rules_only: RC p=1.000, SPA p=1.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2724 |    0.6923 |  0.2496 | 0.0338 | 0.5063 |      0.5308 |           1.4498 |    0.9744 |
| rules_tech|pit|gbt_mono      | 2724 |    0.7066 |  0.2547 | 0.0153 | 0.4572 |      0.5308 |           0.3854 |    0.6986 |
| hitai_full|pit|gbt_mono      | 2724 |    0.6855 |  0.2462 | 0.0059 | 0.5613 |      0.5308 |           2.9204 |    1      |
| hitai_full|shuffled|gbt_mono | 2724 |    0.7061 |  0.2542 | 0.015  | 0.4584 |      0.5308 |           0.367  |    0.6896 |
