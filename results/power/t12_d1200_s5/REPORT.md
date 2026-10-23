# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2015-10-05 (unlocked: True), dev rows 10488, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |    n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|-----:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 6300 |    0.6959 |  0.2512 | 0.0256 | 0.514  |      0.5116 |             0.0113 |                 0.6929 |             0.8282 |           0.1811 |          0.1441 |          0.6251 |    0.6028 |      -0.0522 |    0      |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 6300 |    0.6952 |  0.251  | 0.0295 | 0.507  |      0.5116 |             0.0131 |                 0.6929 |             1.1997 |           0.6498 |          0.1448 |          0.8551 |    0.8245 |      -0.0658 |    0      |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 6300 |    0.6946 |  0.2507 | 0.0261 | 0.5016 |      0.5116 |             0.0085 |                 0.6929 |             1.2542 |           0.6164 |          0.1538 |          0.6935 |    0.8117 |      -0.0504 |    0      |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 6300 |    0.7201 |  0.2522 | 0.0234 | 0.5271 |      0.5116 |             0.014  |                 0.6923 |             1.3739 |           0.5909 |          0.2254 |          0.9148 |    0.8023 |      -0.1031 |    0      |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 6300 |    0.7037 |  0.2522 | 0.0429 | 0.495  |      0.5116 |             0.0741 |                 0.7106 |            -0.1413 |          -1.2316 |          0.2802 |          0.8267 |    0.0378 |      -0.2057 |    0      |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 6300 |    0.7112 |  0.2538 | 0.0392 | 0.5002 |      0.5116 |             0.0509 |                 0.702  |            -0.0556 |          -1.0447 |          0.2375 |          0.6981 |    0.0649 |      -0.1638 |    0      |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 6300 |    0.7335 |  0.2539 | 0.0266 | 0.5178 |      0.5116 |             0.0179 |                 0.6928 |             0.571  |          -0.2223 |          0.2305 |          0.9443 |    0.3741 |      -0.1229 |    0      |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 6300 |    0.7041 |  0.2524 | 0.0393 | 0.4966 |      0.5116 |             0.0752 |                 0.7112 |             0.2493 |          -0.8437 |          0.2752 |          0.7908 |    0.1119 |      -0.1729 |    0      |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 6300 |    0.7115 |  0.2539 | 0.0411 | 0.4965 |      0.5116 |             0.052  |                 0.7018 |             0.0258 |          -0.956  |          0.2349 |          0.6886 |    0.0827 |      -0.1523 |    0      |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 6300 |    0.7007 |  0.2462 | 0.0174 | 0.5831 |      0.5116 |             0.0173 |                 0.6798 |             7.1935 |           5.2055 |          0.527  |          0.9121 |    1      |      -0.0221 |    0.9655 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 6300 |    0.6954 |  0.2484 | 0.0206 | 0.5558 |      0.5116 |             0.0484 |                 0.6969 |             3.7535 |           1.9847 |          0.4197 |          0.7162 |    0.9981 |      -0.0456 |    0.0021 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 6300 |    0.6991 |  0.2483 | 0.0181 | 0.5617 |      0.5116 |             0.0211 |                 0.6877 |             4.8986 |           3.1369 |          0.4098 |          0.6395 |    1      |      -0.0363 |    0.1225 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 6300 |    0.7066 |  0.252  | 0.0251 | 0.5131 |      0.5116 |             0.0192 |                 0.6933 |             0.5137 |          -0.3892 |          0.2356 |          0.7735 |    0.2873 |      -0.1462 |    0      |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 6300 |    0.7034 |  0.2522 | 0.0361 | 0.4932 |      0.5116 |             0.0762 |                 0.7103 |             0.2745 |          -0.6688 |          0.2481 |          0.8035 |    0.1666 |      -0.1538 |    0      |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 6300 |    0.7099 |  0.2533 | 0.0391 | 0.505  |      0.5116 |             0.0475 |                 0.7013 |             0.2949 |          -0.7509 |          0.2587 |          0.7417 |    0.1384 |      -0.1287 |    0      |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 6300 |    0.7248 |  0.2537 | 0.0375 | 0.5078 |      0.5116 |             0.019  |                 0.6931 |             0.558  |          -0.1878 |          0.1905 |          0.7908 |    0.3932 |      -0.1208 |    0      |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 6300 |    0.7041 |  0.2527 | 0.0341 | 0.4911 |      0.5116 |             0.0719 |                 0.7116 |             0.5632 |          -0.4782 |          0.257  |          0.7398 |    0.2452 |      -0.1276 |    0      |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 6300 |    0.7119 |  0.2535 | 0.0364 | 0.5024 |      0.5116 |             0.0524 |                 0.7018 |             0.1182 |          -0.9051 |          0.2527 |          0.7206 |    0.0948 |      -0.1485 |    0      |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 6300 |    0.6944 |  0.2456 | 0.0297 | 0.5857 |      0.5116 |             0.0121 |                 0.6811 |             7.9069 |           5.827  |          0.5156 |          0.8421 |    1      |      -0.0253 |    0.996  |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 6300 |    0.6979 |  0.2495 | 0.0194 | 0.5506 |      0.5116 |             0.0496 |                 0.6982 |             3.0892 |           1.6338 |          0.3559 |          0.6887 |    0.9902 |      -0.0439 |    0.0005 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 6300 |    0.6941 |  0.248  | 0.0168 | 0.5669 |      0.5116 |             0.022  |                 0.6873 |             4.9093 |           3.2368 |          0.4213 |          0.7863 |    1      |      -0.0399 |    0.1604 |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                   |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:-------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                            | -0.7884 |        0.7848 |          -0.0048 | False          | nan      |       nan      |     0.8221 |
| H3a          | logit    | rules_tech - hitai_full                                      |  3.1059 |        0.0009 |           0.0329 | False          | nan      |       nan      |     0.0209 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                       |  1.1658 |        0.1218 |           0.0059 | False          | nan      |       nan      |     0.2062 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                         |  2.6831 |        0.0036 |           0.0241 | False          | nan      |       nan      |     0.0315 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.1838 |        0.029  |         nan      | False          | nan      |       nan      |     0.0894 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0252 |        0.2071 |         nan      | False          | nan      |       nan      |     0.2832 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.4606 |        0.1441 |          -0.0063 | False          | nan      |       nan      |     0.2265 |
| H1           | gbt      | rules_only - hitai_full (logloss)                            | -0.0457 |        0.5182 |          -0.0002 | False          | nan      |       nan      |     0.5701 |
| H3a          | gbt      | rules_tech - hitai_full                                      |  2.0608 |        0.0197 |           0.0087 | False          | nan      |       nan      |     0.0894 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                       |  1.7284 |        0.042  |           0.0081 | False          | nan      |       nan      |     0.0923 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                         |  1.9128 |        0.0279 |           0.0087 | False          | nan      |       nan      |     0.0894 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  2.2907 |        0.022  |         nan      | False          | nan      |       nan      |     0.0894 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0808 |        0.0043 |         nan      | False          | nan      |       nan      |     0.0315 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)     |  0.6496 |        0.5159 |           0.0025 | False          | nan      |       nan      |     0.5701 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                            | -0.9634 |        0.8323 |          -0.0045 | True           |   0.8323 |         1      |     0.8323 |
| H3a          | gbt_mono | rules_tech - hitai_full                                      |  1.792  |        0.0366 |           0.0124 | True           |   0.1682 |         0.1828 |     0.0894 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                       |  1.583  |        0.0567 |           0.0108 | True           |   0.1701 |         0.2836 |     0.104  |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                         |  1.8299 |        0.0336 |           0.0127 | True           |   0.1682 |         0.1682 |     0.0894 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)           |  1.9537 |        0.0507 |         nan      | False          | nan      |       nan      |     0.1015 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates               |  0.0293 |        0.1705 |         nan      | True           |   0.3409 |         0.8523 |     0.25   |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)     | -1.2297 |        0.2188 |          -0.005  | False          | nan      |       nan      |     0.2832 |
| H4b          | tagger   | corr(tag,fwd) original=0.1798 vs perturbed-context (want ~0) | -0.0068 |        0.4876 |           0.1866 | False          | nan      |       nan      |     0.5701 |

## Reality check / SPA vs rules_only: RC p=0.990, SPA p=1.000

## Untouched holdout (single shot)

| config                       |    n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|-----:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 2568 |    0.6946 |  0.2507 | 0.0112 | 0.4937 |      0.5234 |          -1.9119 |    0.0359 |
| rules_tech|pit|gbt_mono      | 2568 |    0.6969 |  0.2514 | 0.0103 | 0.4979 |      0.5234 |           0.5402 |    0.6901 |
| hitai_full|pit|gbt_mono      | 2568 |    0.6859 |  0.2464 | 0.0104 | 0.5689 |      0.5234 |           4.4875 |    1      |
| hitai_full|shuffled|gbt_mono | 2568 |    0.7055 |  0.2516 | 0.0105 | 0.4981 |      0.5234 |           0.694  |    0.7377 |
