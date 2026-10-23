# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 10488, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6300 |    0.6985 |  0.2523 | 0.0389 | 0.4877 |       0.513 |             0.0061 |                 0.6932 |            -0.6126 |          -0.924  |          0.0406 |          0.2302 |    0.0916 |      -0.0637 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6300 |    0.6972 |  0.252  | 0.029  | 0.4908 |       0.513 |             0.0133 |                 0.6938 |            -0.6571 |          -1.3288 |          0.1163 |          0.3348 |    0.0279 |      -0.1436 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6300 |    0.6962 |  0.2515 | 0.038  | 0.4845 |       0.513 |             0.0099 |                 0.6937 |            -0.7118 |          -0.7416 |          0.0038 |          0.2    |    0.1419 |      -0.0488 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6300 |    0.7277 |  0.2551 | 0.0498 | 0.4907 |       0.513 |             0.022  |                 0.6957 |            -0.7776 |          -1.5719 |          0.1524 |          0.4322 |    0.0113 |      -0.1862 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6300 |    0.7043 |  0.2529 | 0.0363 | 0.4926 |       0.513 |             0.0632 |                 0.7043 |            -0.358  |          -1.4041 |          0.269  |          0.6976 |    0.0227 |      -0.2084 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6300 |    0.71   |  0.2534 | 0.0339 | 0.4926 |       0.513 |             0.0399 |                 0.6991 |            -0.9973 |          -1.8608 |          0.2083 |          0.6462 |    0.004  |      -0.2487 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6300 |    0.7268 |  0.2552 | 0.0441 | 0.488  |       0.513 |             0.0257 |                 0.6959 |            -1.1039 |          -1.9122 |          0.1532 |          0.4257 |    0.0028 |      -0.2058 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6300 |    0.7044 |  0.2529 | 0.0369 | 0.4923 |       0.513 |             0.0639 |                 0.7044 |            -0.2774 |          -1.3639 |          0.2806 |          0.7048 |    0.026  |      -0.2002 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6300 |    0.71   |  0.2534 | 0.0339 | 0.4926 |       0.513 |             0.0399 |                 0.6991 |            -0.9973 |          -1.8608 |          0.2083 |          0.6462 |    0.004  |      -0.2487 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6300 |    0.7073 |  0.2515 | 0.0374 | 0.5481 |       0.513 |             0.0166 |                 0.688  |             3.7895 |           2.1535 |          0.5035 |          0.8687 |    0.999  |      -0.0525 |    0.0403 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6300 |    0.6932 |  0.2499 | 0.0298 | 0.54   |       0.513 |             0.0462 |                 0.6954 |             3.4673 |           1.8315 |          0.4741 |          0.8648 |    0.996  |      -0.04   |    0.0127 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6300 |    0.6928 |  0.249  | 0.0259 | 0.5502 |       0.513 |             0.0211 |                 0.6894 |             4.2278 |           2.5143 |          0.4714 |          0.7957 |    0.9999 |      -0.0418 |    0.1061 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6300 |    0.7269 |  0.2553 | 0.0405 | 0.4918 |       0.513 |             0.0327 |                 0.6963 |            -0.4449 |          -1.5782 |          0.2527 |          0.5854 |    0.0113 |      -0.217  |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6300 |    0.7031 |  0.2525 | 0.0387 | 0.4972 |       0.513 |             0.0579 |                 0.7033 |            -0.2485 |          -1.4639 |          0.2767 |          0.5697 |    0.0174 |      -0.1984 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6300 |    0.706  |  0.2531 | 0.0367 | 0.4892 |       0.513 |             0.0411 |                 0.6983 |            -1.0322 |          -1.713  |          0.1778 |          0.6852 |    0.0066 |      -0.2485 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6300 |    0.7229 |  0.2555 | 0.0493 | 0.4828 |       0.513 |             0.0502 |                 0.6996 |            -0.7028 |          -1.7666 |          0.2594 |          0.6413 |    0.0053 |      -0.2466 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6300 |    0.7043 |  0.2531 | 0.0506 | 0.4868 |       0.513 |             0.0638 |                 0.7052 |            -0.4772 |          -1.5553 |          0.2581 |          0.5214 |    0.014  |      -0.2138 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6300 |    0.7106 |  0.2544 | 0.0399 | 0.4802 |       0.513 |             0.0487 |                 0.7007 |            -1.163  |          -2.0254 |          0.1962 |          0.5027 |    0.002  |      -0.253  |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6300 |    0.7006 |  0.2496 | 0.0386 | 0.5581 |       0.513 |             0.0236 |                 0.6875 |             4.3975 |           2.6577 |          0.4844 |          0.724  |    0.9999 |      -0.0362 |    0.1523 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6300 |    0.6941 |  0.2499 | 0.026  | 0.5486 |       0.513 |             0.0413 |                 0.6944 |             3.2936 |           1.652  |          0.4981 |          0.9579 |    0.9912 |      -0.0629 |    0.0066 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6300 |    0.6952 |  0.2488 | 0.0243 | 0.555  |       0.513 |             0.0271 |                 0.6888 |             3.9971 |           2.2534 |          0.4984 |          0.8973 |    0.9994 |      -0.0471 |    0.0532 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -1.8583 |        0.9684 |          -0.0088 | False          | nan      |       nan      |     0.9684 |
| H3a          | logit    | rules_tech - hitai_full                                      |  1.6616 |        0.0483 |           0.0195 | False          | nan      |       nan      |     0.0855 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  1.8554 |        0.0318 |           0.0196 | False          | nan      |       nan      |     0.0699 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  1.5187 |        0.0644 |           0.0156 | False          | nan      |       nan      |     0.0945 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  3.7476 |        0.0002 |         nan      | False          | nan      |       nan      |     0.0008 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0003 |        0.4963 |         nan      | False          | nan      |       nan      |     0.5459 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.9234 |        0.0544 |          -0.0067 | False          | nan      |       nan      |     0.0855 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            |  2.0436 |        0.0205 |           0.004  | False          | nan      |       nan      |     0.0564 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  3.5096 |        0.0002 |           0.0113 | False          | nan      |       nan      |     0.0008 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  3.4314 |        0.0003 |           0.0099 | False          | nan      |       nan      |     0.0009 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  3.6929 |        0.0001 |           0.0111 | False          | nan      |       nan      |     0.0008 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.9267 |        0.054  |         nan      | False          | nan      |       nan      |     0.0855 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.027  |        0.1908 |         nan      | False          | nan      |       nan      |     0.2469 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.574  |        0.566  |           0.0009 | False          | nan      |       nan      |     0.5929 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            |  1.2697 |        0.1021 |           0.0034 | True           |   0.1021 |         0.5104 |     0.1404 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  3.9772 |        0      |           0.0172 | True           |   0.0002 |         0.0002 |     0.0008 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  3.6094 |        0.0002 |           0.0132 | True           |   0.0006 |         0.0008 |     0.0008 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  3.5806 |        0.0002 |           0.0178 | True           |   0.0006 |         0.0009 |     0.0008 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.1203 |        0.2626 |         nan      | False          | nan      |       nan      |     0.3209 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.052  |        0.0457 |         nan      | True           |   0.0913 |         0.2283 |     0.0855 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.9482 |        0.343  |           0.0024 | False          | nan      |       nan      |     0.3972 |
| H4b          | tagger   | corr(tag,fwd) original=0.1586 vs perturbed-context (want ~0) | -0.021  |        0.0313 |           0.1796 | False          | nan      |       nan      |     0.0699 |

## Reality check / SPA vs rules_only: RC p=0.730, SPA p=0.113

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2568 |    0.6934 |  0.2501 | 0.0266 | 0.5278 |      0.4875 |           0.1127 |    0.5413 |
| rules_tech|pit|gbt_mono      | 2568 |    0.694  |  0.2505 | 0.0259 | 0.4986 |      0.4875 |          -2.0148 |    0.028  |
| hitai_full|pit|gbt_mono      | 2568 |    0.6916 |  0.2476 | 0.0205 | 0.5537 |      0.4875 |           4.8474 |    1      |
| hitai_full|shuffled|gbt_mono | 2568 |    0.6944 |  0.2506 | 0.0254 | 0.4976 |      0.4875 |          -1.2253 |    0.129  |
