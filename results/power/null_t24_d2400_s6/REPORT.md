# HITAI run report (auto-generated)

**No profitability claim.** Synthetic-data numbers only validate the pipeline.

rules_version `feaf59592dcb`, holdout starts 2019-06-10 (unlocked: True), dev rows 44016, walk-forward folds 5, trials 21.

## Dev (walk-forward OOS) metrics

| config                       | feature_set   | tag_variant   | model    |     n |   logloss |   brier |    ece |    auc |   base_rate |   ece_uncalibrated |   logloss_uncalibrated |   sharpe_gross_ann |   sharpe_net_ann |   mean_turnover |   mean_exposure |   psr_net |   max_dd_net |   dsr_net |   n_trials |
|:-----------------------------|:--------------|:--------------|:---------|------:|----------:|--------:|-------:|-------:|------------:|-------------------:|-----------------------:|-------------------:|-----------------:|----------------:|----------------:|----------:|-------------:|----------:|-----------:|
| rules_only|pit|logit         | rules_only    | pit           | logit    | 26424 |    0.6936 |  0.2501 | 0.0067 | 0.4997 |      0.4955 |             0.0184 |                 0.6939 |            -0.1004 |          -0.6686 |          0.0198 |          0.0278 |    0.0789 |      -0.0304 |    0.0024 |         21 |
| rules_only|pit|gbt           | rules_only    | pit           | gbt      | 26424 |    0.6933 |  0.2501 | 0.007  | 0.5001 |      0.4955 |             0.0185 |                 0.694  |            -0.6506 |          -0.9733 |          0.0098 |          0.0165 |    0.0182 |      -0.0361 |    0.0002 |         21 |
| rules_only|pit|gbt_mono      | rules_only    | pit           | gbt_mono | 26424 |    0.6933 |  0.25   | 0.0017 | 0.5089 |      0.4955 |             0.0181 |                 0.6937 |            -0.4855 |          -1.1144 |          0.0211 |          0.0197 |    0.0086 |      -0.0449 |    0.0001 |         21 |
| tech_only|pit|logit          | tech_only     | pit           | logit    | 26424 |    0.6951 |  0.2502 | 0.0034 | 0.5126 |      0.4955 |             0.0219 |                 0.6943 |             0.8302 |          -0.183  |          0.1017 |          0.189  |    0.3515 |      -0.0787 |    0.0385 |         21 |
| tech_only|pit|gbt            | tech_only     | pit           | gbt      | 26424 |    0.6962 |  0.2505 | 0.005  | 0.5062 |      0.4955 |             0.0387 |                 0.6986 |             0.7286 |          -0.0042 |          0.0288 |          0.0248 |    0.4965 |      -0.03   |    0.0807 |         21 |
| tech_only|pit|gbt_mono       | tech_only     | pit           | gbt_mono | 26424 |    0.6952 |  0.2502 | 0.0038 | 0.5062 |      0.4955 |             0.0302 |                 0.6957 |             0.4644 |          -0.2001 |          0.0261 |          0.0229 |    0.3377 |      -0.0234 |    0.035  |         21 |
| rules_tech|pit|logit         | rules_tech    | pit           | logit    | 26424 |    0.6942 |  0.2501 | 0.0022 | 0.5121 |      0.4955 |             0.0217 |                 0.6944 |             0.8797 |           0.047  |          0.0604 |          0.0923 |    0.5391 |      -0.0317 |    0.0979 |         21 |
| rules_tech|pit|gbt           | rules_tech    | pit           | gbt      | 26424 |    0.6964 |  0.2505 | 0.0063 | 0.5061 |      0.4955 |             0.0385 |                 0.6986 |             0.5381 |          -0.176  |          0.0283 |          0.0247 |    0.3572 |      -0.03   |    0.04   |         21 |
| rules_tech|pit|gbt_mono      | rules_tech    | pit           | gbt_mono | 26424 |    0.6952 |  0.2502 | 0.0038 | 0.5062 |      0.4955 |             0.0302 |                 0.6957 |             0.4644 |          -0.2001 |          0.0261 |          0.0229 |    0.3377 |      -0.0234 |    0.035  |         21 |
| hitai_full|pit|logit         | hitai_full    | pit           | logit    | 26424 |    0.6958 |  0.2503 | 0.0021 | 0.511  |      0.4955 |             0.0227 |                 0.6946 |             0.9847 |          -0.0594 |          0.0997 |          0.2015 |    0.4507 |      -0.049  |    0.0649 |         21 |
| hitai_full|pit|gbt           | hitai_full    | pit           | gbt      | 26424 |    0.6964 |  0.2504 | 0.005  | 0.5079 |      0.4955 |             0.0395 |                 0.6984 |             0.4368 |          -0.6658 |          0.0588 |          0.054  |    0.0814 |      -0.0466 |    0.0026 |         21 |
| hitai_full|pit|gbt_mono      | hitai_full    | pit           | gbt_mono | 26424 |    0.6963 |  0.2505 | 0.0053 | 0.5068 |      0.4955 |             0.0309 |                 0.6958 |             0.935  |          -0.0339 |          0.0449 |          0.0388 |    0.4718 |      -0.0299 |    0.0718 |         21 |
| hitai_full|shuffled|logit    | hitai_full    | shuffled      | logit    | 26424 |    0.6948 |  0.2503 | 0.008  | 0.5063 |      0.4955 |             0.0227 |                 0.6943 |             1.0629 |          -0.4592 |          0.1388 |          0.1522 |    0.1713 |      -0.0521 |    0.01   |         21 |
| hitai_full|shuffled|gbt      | hitai_full    | shuffled      | gbt      | 26424 |    0.6967 |  0.2504 | 0.0052 | 0.5048 |      0.4955 |             0.0408 |                 0.6984 |             0.9289 |           0.0878 |          0.0375 |          0.0313 |    0.5728 |      -0.0247 |    0.1134 |         21 |
| hitai_full|shuffled|gbt_mono | hitai_full    | shuffled      | gbt_mono | 26424 |    0.6949 |  0.2502 | 0.0065 | 0.5074 |      0.4955 |             0.0304 |                 0.6955 |             0.6681 |          -0.3288 |          0.045  |          0.0395 |    0.2459 |      -0.0329 |    0.0188 |         21 |
| hitai_full|lagged|logit      | hitai_full    | lagged        | logit    | 26424 |    0.6945 |  0.2502 | 0.0069 | 0.5071 |      0.4955 |             0.0202 |                 0.6944 |             1.3514 |           0.2268 |          0.0915 |          0.1305 |    0.6821 |      -0.0338 |    0.1796 |         21 |
| hitai_full|lagged|gbt        | hitai_full    | lagged        | gbt      | 26424 |    0.6957 |  0.2504 | 0.006  | 0.5088 |      0.4955 |             0.0423 |                 0.6985 |             0.7158 |          -0.3415 |          0.0594 |          0.0598 |    0.2381 |      -0.0401 |    0.0178 |         21 |
| hitai_full|lagged|gbt_mono   | hitai_full    | lagged        | gbt_mono | 26424 |    0.6953 |  0.2503 | 0.0076 | 0.5062 |      0.4955 |             0.0327 |                 0.6959 |             0.6654 |          -0.3132 |          0.0528 |          0.0538 |    0.2569 |      -0.0337 |    0.0206 |         21 |
| hitai_full|masked|logit      | hitai_full    | masked        | logit    | 26424 |    0.6949 |  0.2502 | 0.0025 | 0.511  |      0.4955 |             0.0241 |                 0.6945 |             0.5377 |          -0.5226 |          0.0702 |          0.0839 |    0.1372 |      -0.043  |    0.0065 |         21 |
| hitai_full|masked|gbt        | hitai_full    | masked        | gbt      | 26424 |    0.6954 |  0.2504 | 0.0062 | 0.5068 |      0.4955 |             0.039  |                 0.6986 |             0.4383 |          -0.5097 |          0.0435 |          0.0378 |    0.1455 |      -0.0475 |    0.0074 |         21 |
| hitai_full|masked|gbt_mono   | hitai_full    | masked        | gbt_mono | 26424 |    0.6966 |  0.2503 | 0.0045 | 0.5057 |      0.4955 |             0.0299 |                 0.6957 |             0.6696 |          -0.0163 |          0.0271 |          0.0235 |    0.4864 |      -0.02   |    0.077  |         21 |

## Hypothesis tests

| hypothesis   | model    | comparison                                                    |    stat |   p_one_sided |   mean_loss_diff | confirmatory   |   p_holm |   p_bonferroni |   p_bh_all |
|:-------------|:---------|:--------------------------------------------------------------|--------:|--------------:|-----------------:|:---------------|---------:|---------------:|-----------:|
| H1           | logit    | rules_only - hitai_full (logloss)                             | -1.8322 |        0.9665 |          -0.0022 | False          |      nan |            nan |     0.9989 |
| H3a          | logit    | rules_tech - hitai_full                                       | -1.6825 |        0.9538 |          -0.0015 | False          |      nan |            nan |     0.9989 |
| H3b          | logit    | hitai_full[shuffled] - hitai_full[pit]                        | -1.2125 |        0.8873 |          -0.001  | False          |      nan |            nan |     0.9989 |
| H3c          | logit    | hitai_full[lagged] - hitai_full[pit]                          | -1.4247 |        0.9229 |          -0.0013 | False          |      nan |            nan |     0.9989 |
| H2a          | logit    | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  3.8228 |        0.0001 |         nan      | False          |      nan |            nan |     0.0029 |
| H2b          | logit    | Spearman(|p-.5|, hit) on non-overlapping dates                |  0.0085 |        0.2854 |         nan      | False          |      nan |            nan |     0.8969 |
| H4a          | logit    | masked - unmasked logloss (two-sided; want NOT rejected)      | -0.8434 |        0.399  |          -0.0008 | False          |      nan |            nan |     0.9754 |
| H1           | gbt      | rules_only - hitai_full (logloss)                             | -2.9687 |        0.9985 |          -0.0031 | False          |      nan |            nan |     0.9989 |
| H3a          | gbt      | rules_tech - hitai_full                                       | -0.05   |        0.52   |          -0      | False          |      nan |            nan |     0.9989 |
| H3b          | gbt      | hitai_full[shuffled] - hitai_full[pit]                        |  0.3749 |        0.3539 |           0.0003 | False          |      nan |            nan |     0.9732 |
| H3c          | gbt      | hitai_full[lagged] - hitai_full[pit]                          | -1.2749 |        0.8988 |          -0.0007 | False          |      nan |            nan |     0.9989 |
| H2a          | gbt      | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  3.1095 |        0.0019 |         nan      | False          |      nan |            nan |     0.0206 |
| H2b          | gbt      | Spearman(|p-.5|, hit) on non-overlapping dates                |  0.0131 |        0.1912 |         nan      | False          |      nan |            nan |     0.8267 |
| H4a          | gbt      | masked - unmasked logloss (two-sided; want NOT rejected)      | -1.4222 |        0.155  |          -0.001  | False          |      nan |            nan |     0.8267 |
| H1           | gbt_mono | rules_only - hitai_full (logloss)                             | -3.0625 |        0.9989 |          -0.003  | True           |        1 |              1 |     0.9989 |
| H3a          | gbt_mono | rules_tech - hitai_full                                       | -1.7637 |        0.9611 |          -0.0011 | True           |        1 |              1 |     0.9989 |
| H3b          | gbt_mono | hitai_full[shuffled] - hitai_full[pit]                        | -1.8144 |        0.9652 |          -0.0014 | True           |        1 |              1 |     0.9989 |
| H3c          | gbt_mono | hitai_full[lagged] - hitai_full[pit]                          | -0.9461 |        0.828  |          -0.001  | True           |        1 |              1 |     0.9989 |
| H2a          | gbt_mono | Spiegelhalter z (H0 calibrated; want NOT rejected)            |  2.7225 |        0.0065 |         nan      | False          |      nan |            nan |     0.0475 |
| H2b          | gbt_mono | Spearman(|p-.5|, hit) on non-overlapping dates                |  0.0113 |        0.2255 |         nan      | True           |        1 |              1 |     0.8267 |
| H4a          | gbt_mono | masked - unmasked logloss (two-sided; want NOT rejected)      |  0.3845 |        0.7006 |           0.0003 | False          |      nan |            nan |     0.9989 |
| H4b          | tagger   | corr(tag,fwd) original=-0.0006 vs perturbed-context (want ~0) | -0.0024 |        0.6148 |           0.0018 | False          |      nan |            nan |     0.9989 |

## Reality check / SPA vs rules_only: RC p=0.983, SPA p=1.000

## Untouched holdout (single shot)

| config                       |     n |   logloss |   brier |    ece |    auc |   base_rate |   sharpe_net_ann |   psr_net |
|:-----------------------------|------:|----------:|--------:|-------:|-------:|------------:|-----------------:|----------:|
| rules_only|pit|gbt_mono      | 10896 |    0.6938 |  0.2503 | 0.0178 | 0.4999 |       0.506 |          -1.2037 |    0.0539 |
| rules_tech|pit|gbt_mono      | 10896 |    0.697  |  0.2511 | 0.0202 | 0.4845 |       0.506 |          -2.2786 |    0.0012 |
| hitai_full|pit|gbt_mono      | 10896 |    0.697  |  0.2511 | 0.0202 | 0.4845 |       0.506 |          -2.2786 |    0.0012 |
| hitai_full|shuffled|gbt_mono | 10896 |    0.6969 |  0.2512 | 0.0222 | 0.4892 |       0.506 |          -3.1392 |    0      |
