"""ML fusion models + calibrated confidence. All preprocessing lives inside the
sklearn Pipeline so scalers are fit on the training fold only."""
from __future__ import annotations
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.isotonic import IsotonicRegression


def make_model(kind: str, feature_names: list[str], seed: int = 0):
    if kind == "logit":      # regularized linear
        return make_pipeline(SimpleImputer(strategy="median"), StandardScaler(),
                             LogisticRegression(C=0.1, max_iter=2000))
    if kind == "gbt":        # gradient-boosted trees
        return HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, max_iter=200,
                                              min_samples_leaf=200, l2_regularization=1.0,
                                              early_stopping=False, random_state=seed)
    if kind == "gbt_mono":   # constrained nonlinear: monotone in human rule votes
        cst = [1 if f.startswith("rule_") else 0 for f in feature_names]
        return HistGradientBoostingClassifier(max_depth=2, learning_rate=0.05, max_iter=150,
                                              min_samples_leaf=300, l2_regularization=1.0,
                                              monotonic_cst=cst, early_stopping=False,
                                              random_state=seed)
    raise ValueError(kind)


class Calibrated:
    """Fit base model on `fit` rows, isotonic calibrator on the later `cal` rows
    (both inside the training window). Never touches test rows."""
    def __init__(self, base):
        self.base = base
        self.iso = IsotonicRegression(out_of_bounds="clip", y_min=1e-3, y_max=1 - 1e-3)

    def fit(self, X_fit, y_fit, X_cal, y_cal):
        self.base.fit(X_fit, y_fit)
        self.iso.fit(self.base.predict_proba(X_cal)[:, 1], y_cal)
        self.fitted_on_ = (len(X_fit), len(X_cal))
        return self

    def predict_proba(self, X):
        return self.iso.predict(self.base.predict_proba(X)[:, 1])
