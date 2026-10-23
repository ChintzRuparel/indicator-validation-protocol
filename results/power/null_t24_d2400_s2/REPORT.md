# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6949 |  0.2508 | 0.0184 | 0.5048 |      0.4981 |             0.0102 |                 0.6935 |             0.393  |          -0.0233 |          0.0558 |          0.3971 |    0.4806 |      -0.0678 |    0.1619 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6942 |  0.2505 | 0.015  | 0.5057 |      0.4981 |             0.0115 |                 0.6937 |             0.2501 |          -0.6214 |          0.1332 |          0.4934 |    0.097  |      -0.1277 |    0.0126 |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6944 |  0.2506 | 0.018  | 0.5025 |      0.4981 |             0.0101 |                 0.6935 |             0.2849 |          -0.2473 |          0.0509 |          0.2049 |    0.3025 |      -0.0451 |    0.0726 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6945 |  0.2504 | 0.0137 | 0.502  |      0.4981 |             0.0132 |                 0.6937 |             0.6951 |          -0.1063 |          0.0949 |          0.2867 |    0.4122 |      -0.0584 |    0.123  |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6979 |  0.251  | 0.0209 | 0.501  |      0.4981 |             0.0351 |                 0.6974 |             0.1669 |          -0.6153 |          0.0909 |          0.2756 |    0.1006 |      -0.1093 |    0.0135 |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6958 |  0.2508 | 0.0166 | 0.5017 |      0.4981 |             0.0239 |                 0.6955 |             0.0551 |          -0.4571 |          0.0548 |          0.2391 |    0.1712 |      -0.0772 |    0.0299 |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6953 |  0.2505 | 0.0186 | 0.5046 |      0.4981 |             0.0164 |                 0.6937 |             0.0854 |          -0.4894 |          0.0629 |          0.2379 |    0.1537 |      -0.0888 |    0.0252 |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6957 |  0.2508 | 0.0197 | 0.5021 |      0.4981 |             0.0383 |                 0.6976 |             0.2448 |          -0.299  |          0.0593 |          0.2453 |    0.2667 |      -0.0709 |    0.0596 |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6957 |  0.2508 | 0.0175 | 0.5007 |      0.4981 |             0.0231 |                 0.6955 |             0.001  |          -0.726  |          0.0833 |          0.2765 |    0.0663 |      -0.1214 |    0.0075 |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6952 |  0.2505 | 0.0109 | 0.5059 |      0.4981 |             0.0175 |                 0.6938 |             0.3964 |          -0.524  |          0.1128 |          0.2987 |    0.1371 |      -0.1112 |    0.0212 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6952 |  0.2508 | 0.0182 | 0.5    |      0.4981 |             0.0386 |                 0.6978 |             0.0373 |          -0.5753 |          0.0693 |          0.2628 |    0.1159 |      -0.109  |    0.0166 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6952 |  0.2508 | 0.0198 | 0.4988 |      0.4981 |             0.025  |                 0.6955 |             0.2076 |          -0.5679 |          0.089  |          0.2759 |    0.1192 |      -0.1086 |    0.0174 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6946 |  0.2504 | 0.0187 | 0.5051 |      0.4981 |             0.0135 |                 0.6937 |             0.2032 |          -0.4218 |          0.0685 |          0.2417 |    0.1894 |      -0.0726 |    0.0346 |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6988 |  0.2511 | 0.0182 | 0.5007 |      0.4981 |             0.0351 |                 0.6975 |             0.0397 |          -0.7562 |          0.0942 |          0.2846 |    0.0581 |      -0.1267 |    0.0062 |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6962 |  0.2508 | 0.0173 | 0.5002 |      0.4981 |             0.0226 |                 0.6954 |             0.3471 |           0.0854 |          0.0265 |          0.2152 |    0.5709 |      -0.0411 |    0.2235 |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6953 |  0.2505 | 0.018  | 0.5024 |      0.4981 |             0.0219 |                 0.6941 |             0.4571 |          -0.5256 |          0.12   |          0.2945 |    0.1365 |      -0.1198 |    0.021  |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6975 |  0.251  | 0.0195 | 0.4989 |      0.4981 |             0.0358 |                 0.6977 |             0.0682 |          -0.551  |          0.068  |          0.254  |    0.1264 |      -0.095  |    0.019  |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6961 |  0.251  | 0.0173 | 0.5009 |      0.4981 |             0.0276 |                 0.6956 |             0.2303 |          -0.2128 |          0.0461 |          0.2349 |    0.3288 |      -0.0531 |    0.084  |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6944 |  0.2505 | 0.0114 | 0.5054 |      0.4981 |             0.0159 |                 0.6938 |             0.329  |          -0.4453 |          0.0864 |          0.2612 |    0.1762 |      -0.0826 |    0.0309 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6969 |  0.2508 | 0.0184 | 0.5006 |      0.4981 |             0.0368 |                 0.6977 |             0.0824 |          -0.6903 |          0.089  |          0.2787 |    0.076  |      -0.1177 |    0.009  |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6957 |  0.2509 | 0.0178 | 0.5007 |      0.4981 |             0.0237 |                 0.6955 |             0.0346 |          -0.6659 |          0.08   |          0.2759 |    0.0837 |      -0.0987 |    0.0104 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                    |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:--------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                             | -0.379  |        0.6477 |          -0.0003 | False          | nan      |       nan      |     0.7499 |
| H3a          | logit    | rules_tech - hitai_full                                       |  0.1043 |        0.4585 |           0.0001 | False          | nan      |       nan      |     0.5933 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                        | -0.8762 |        0.8095 |          -0.0006 | False          | nan      |       nan      |     0.8898 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                          |  0.1719 |        0.4318 |           0.0002 | False          | nan      |       nan      |     0.5933 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  3.3769 |        0.0007 |         nan      | False          | nan      |       nan      |     0.0047 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates                | -0.0047 |        0.622  |         nan      | False          | nan      |       nan      |     0.7499 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)      | -1.4506 |        0.1469 |          -0.0008 | False          | nan      |       nan      |     0.2938 |
| H1           | gbt      | rules_only - hitai_full (logloss)                             | -1.7087 |        0.9562 |          -0.001  | False          | nan      |       nan      |     0.9562 |
| H3a          | gbt      | rules_tech - hitai_full                                       |  0.9491 |        0.1713 |           0.0005 | False          | nan      |       nan      |     0.314  |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                        |  3.1397 |        0.0008 |           0.0036 | False          | nan      |       nan      |     0.0047 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                          |  1.9494 |        0.0256 |           0.0023 | False          | nan      |       nan      |     0.1127 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  3.8499 |        0.0001 |         nan      | False          | nan      |       nan      |     0.0013 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates                |  0.0035 |        0.4077 |         nan      | False          | nan      |       nan      |     0.5933 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)      |  1.8031 |        0.0714 |           0.0017 | False          | nan      |       nan      |     0.2063 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                             | -1.0335 |        0.8493 |          -0.0008 | True           |   0.8493 |         1      |     0.8898 |
| H3a          | gbt_mono | rules_tech - hitai_full                                       |  1.182  |        0.1186 |           0.0005 | True           |   0.4744 |         0.593  |     0.2853 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                        |  1.4746 |        0.0702 |           0.001  | True           |   0.3508 |         0.3508 |     0.2063 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                          |  1.1278 |        0.1297 |           0.0009 | True           |   0.4744 |         0.6485 |     0.2853 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  4.4254 |        0      |         nan      | False          | nan      |       nan      |     0.0002 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates                |  0.0056 |        0.3541 |         nan      | True           |   0.7082 |         1      |     0.5565 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)      |  1.0504 |        0.2935 |           0.0005 | False          | nan      |       nan      |     0.4967 |
| H4b          | tagger   | corr(tag,fwd) original=-0.0015 vs perturbed-context (want ~0) | -0.0085 |        0.075  |           0.007  | False          | nan      |       nan      |     0.2063 |

## Reality check / SPA vs rules_only: RC p=0.897, SPA p=0.803

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6931 |  0.25   | 0.0037 | 0.4998 |      0.5036 |          -0.8661 |    0.0051 |
| rules_tech|pit|gbt_mono      | 10896 |    0.6941 |  0.2502 | 0.0071 | 0.5087 |      0.5036 |          -2.487  |    0.0004 |
| hitai_full|pit|gbt_mono      | 10896 |    0.6941 |  0.2503 | 0.0083 | 0.5094 |      0.5036 |          -1.6374 |    0.0144 |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6952 |  0.2502 | 0.0072 | 0.5077 |      0.5036 |          -2.3527 |    0.0008 |
