import os
import numpy as np
import pandas as pd
import pytest
from hitai import data, features, rules, llm_tags, cv, models, stats, experiment

H = 5


@pytest.fixture(scope="module")
def panel():
    px, news = data.synthetic_panel(3, 500, seed=1, signal_strength=0.25)
    df = rules.add_rules(features.add_labels(features.add_technical(px), H))
    return px, news, df


def _build(px):
    return rules.add_rules(features.add_labels(features.add_technical(px), H))


# ---------------------------------------------------------------- look-ahead
def test_features_rules_invariant_to_future_prices(panel):
    px, _, df = panel
    tk, t_idx = "SYN00", 300
    g = px[px.ticker == tk].index
    cut_date = px.loc[g[t_idx], "date"]
    px2 = px.copy()
    fut = px2.ticker.eq(tk) & (px2.date > cut_date)
    px2.loc[fut, ["open", "high", "low", "close"]] *= 3.0
    px2.loc[fut, "volume"] *= 0.1
    df2 = _build(px2)
    cols = features.TECH_FEATURES + rules.RULE_FEATURES
    a = df[(df.ticker == tk) & (df.date <= cut_date)][cols]
    b = df2[(df2.ticker == tk) & (df2.date <= cut_date)][cols]
    pd.testing.assert_frame_equal(a.reset_index(drop=True), b.reset_index(drop=True))


def test_label_uses_next_open_and_window(panel):
    _, _, df = panel
    g = df[df.ticker == "SYN01"].reset_index(drop=True)
    i = 50
    exp = np.log(g.open[i + 1 + H] / g.open[i + 1])
    assert np.isclose(g.fwd_ret[i], exp)
    assert g.label_end_date[i] == g.date[i + 1 + H]
    assert np.isclose(g.ret_next[i], np.log(g.open[i + 2] / g.open[i + 1]))


# ---------------------------------------------------------------- splits
def test_holdout_untouched(panel):
    dev, hold, cut = cv.holdout_split(panel[2], 0.2)
    assert (dev.date < cut).all() and (dev.label_end_date < cut).all()
    assert (hold.date >= cut).all()
    assert set(dev.index).isdisjoint(hold.index)


def test_walk_forward_purged(panel):
    dev, _, _ = cv.holdout_split(panel[2], 0.2)
    dev = dev.reset_index(drop=True)
    for tr, te in cv.walk_forward(dev, 4, embargo_days=5):
        t0 = dev.date.iloc[te].min()
        assert (dev.date.iloc[tr] < t0).all()
        assert (dev.label_end_date.iloc[tr] < t0).all(), "train label overlaps test"


def test_purged_kfold_purge_and_embargo(panel):
    dev, _, _ = cv.holdout_split(panel[2], 0.2)
    dev = dev.reset_index(drop=True)
    for tr, te in cv.purged_kfold(dev, 5, embargo_days=5):
        t0, t1 = dev.date.iloc[te].min(), dev.date.iloc[te].max()
        trd = dev.iloc[tr]
        assert not ((trd.date <= t1) & (trd.label_end_date >= t0)).any()
        assert not ((trd.date > t1) & (trd.date <= t1 + pd.offsets.BDay(5))).any()


def test_calib_split_no_overlap(panel):
    dev, _, _ = cv.holdout_split(panel[2], 0.2)
    f, c = cv.calib_split(dev)
    assert dev.label_end_date.iloc[f].max() < dev.date.iloc[c].min()


def test_scaler_and_calibrator_fit_on_train_only(panel):
    dev, _, _ = cv.holdout_split(panel[2], 0.2)
    dev = dev.dropna(subset=["y"]).reset_index(drop=True)
    f, c = cv.calib_split(dev)
    feats = features.TECH_FEATURES
    m = models.Calibrated(models.make_model("logit", feats))
    m.fit(dev.iloc[f][feats], dev.iloc[f].y, dev.iloc[c][feats], dev.iloc[c].y)
    assert m.fitted_on_ == (len(f), len(c))
    scaler = m.base.named_steps["standardscaler"]
    imp = m.base.named_steps["simpleimputer"].transform(dev.iloc[f][feats])
    assert np.allclose(scaler.mean_, imp.mean(0))


# ---------------------------------------------------------------- LLM tags
def test_tag_cache_reproducible_and_pit(panel, tmp_path):
    _, news, df = panel
    sub = df.head(200)
    tg = llm_tags.MockPITTagger(0)
    c1 = llm_tags.TagCache(str(tmp_path / "c.jsonl"))
    a = llm_tags.add_tags(sub, tg, c1, news)
    c2 = llm_tags.TagCache(str(tmp_path / "c.jsonl"))
    b = llm_tags.add_tags(sub, tg, c2, news)
    assert c2.misses == 0 and c2.hits == len(sub)
    pd.testing.assert_frame_equal(a, b)
    for r in c2.mem.values():
        assert pd.Timestamp(r["asof"]) <= pd.Timestamp(r["key"].split("|")[4])


def test_cache_with_future_asof_is_rejected(panel, tmp_path):
    _, news, df = panel
    sub = df.head(1)
    tg = llm_tags.MockPITTagger(0)
    c = llm_tags.TagCache(str(tmp_path / "c.jsonl"))
    llm_tags.add_tags(sub, tg, c, news)
    k = next(iter(c.mem))
    c.mem[k]["asof"] = "2099-01-01"
    with pytest.raises(AssertionError):
        llm_tags.add_tags(sub, tg, c, news)


def test_schema_enforced():
    with pytest.raises(ValueError):
        llm_tags.validate_tag({"sentiment": 0.37, "event_risk": 0, "regime": "calm", "confidence": 1})


def test_tags_do_not_use_future_news(panel, tmp_path):
    _, news, df = panel
    sub = df[df.ticker == "SYN00"].head(150)
    d = sub.date.iloc[100]
    n2 = news.copy()
    n2.loc[n2.date > d, "news"] = 99.0
    tg = llm_tags.MockPITTagger(0)
    a = llm_tags.add_tags(sub, tg, llm_tags.TagCache(str(tmp_path / "a.jsonl")), news)
    b = llm_tags.add_tags(sub, tg, llm_tags.TagCache(str(tmp_path / "b.jsonl")), n2)
    cols = llm_tags.TAG_FEATURES
    pd.testing.assert_frame_equal(a[a.date <= d][cols], b[b.date <= d][cols])


def test_shuffle_respects_segments_and_lag(panel, tmp_path):
    _, news, df = panel
    t = llm_tags.add_tags(df, llm_tags.MockPITTagger(0), llm_tags.TagCache(str(tmp_path / "s.jsonl")), news)
    cut = t.date.sort_values().iloc[int(len(t) * 0.8)]
    s = llm_tags.shuffle_tags(t, 0, segment_cut=cut)
    for tk in t.ticker.unique():
        for seg in [t.date < cut, t.date >= cut]:
            m = (t.ticker == tk) & seg
            assert sorted(t.loc[m, "tag_sentiment"]) == sorted(s.loc[m, "tag_sentiment"])
    lg = llm_tags.lag_tags(t, 20)
    g, gl = t[t.ticker == "SYN00"], lg[lg.ticker == "SYN00"]
    assert np.array_equal(gl.tag_sentiment.iloc[20:].to_numpy(), g.tag_sentiment.iloc[:-20].to_numpy())


def test_memorization_detector_flags_leaky_tagger(panel, tmp_path):
    _, news, df = panel
    lt = llm_tags.MockMemorizingTagger(0)
    c = llm_tags.TagCache(str(tmp_path / "l.jsonl"))
    un = llm_tags.add_tags(df, lt, c, news, masked=False, oracle=True)
    ms = llm_tags.add_tags(df, lt, c, news, masked=True, oracle=True)
    ok = df.fwd_ret.notna()
    cu = np.corrcoef(un.tag_sentiment[ok], df.fwd_ret[ok])[0, 1]
    cm = np.corrcoef(ms.tag_sentiment[ok], df.fwd_ret[ok])[0, 1]
    assert cu > 0.5 and cm < 0.3


# ---------------------------------------------------------------- stats
def test_multiple_testing():
    p = np.array([0.01, 0.04, 0.03, 0.2])
    assert np.allclose(stats.benjamini_hochberg(p), [0.04, 0.16 / 3, 0.16 / 3, 0.2])
    assert np.allclose(stats.bonferroni(p), [0.04, 0.16, 0.12, 0.8])
    assert np.allclose(stats.holm(p), [0.04, 0.09, 0.09, 0.2])


def test_dsr_le_psr_and_rc_null():
    rng = np.random.default_rng(0)
    r = rng.normal(0.0005, 0.01, 1000)
    assert stats.deflated_sharpe(r, 0.002, 50) <= stats.psr(r)
    lb = rng.normal(1, 0.1, 400)
    lm = np.column_stack([lb + rng.normal(0, 0.05, 400) for _ in range(5)])
    out = stats.reality_check_spa(lb, lm, B=200)
    assert out["rc_p"] > 0.05 and out["spa_p"] > 0.05


def test_calibration_metrics():
    rng = np.random.default_rng(1)
    p = rng.uniform(0.2, 0.8, 20000)
    y = (rng.uniform(size=p.size) < p).astype(float)
    assert stats.ece(p, y) < 0.02
    assert stats.spiegelhalter_z(p, y)[1] > 0.01


# ---------------------------------------------------------------- end to end
def test_end_to_end_and_holdout_lock(tmp_path):
    out = str(tmp_path / "run")
    args = experiment.parse(["--n-tickers", "3", "--n-days", "700", "--n-splits", "3", "--bootstrap", "50",
                             "--out", out, "--unlock-holdout", "--signal", "0"])
    met, tests, spa, hold = experiment.run(args)
    for f in ["metrics_dev.csv", "hypothesis_tests.csv", "reality_check_spa.csv", "holdout_metrics.csv",
              "run_manifest.json", "REPORT.md", "HOLDOUT_USED.lock"]:
        assert os.path.exists(os.path.join(out, f)), f
    assert met.n.min() > 0 and tests.confirmatory.sum() == 5
    with pytest.raises(SystemExit):
        experiment.run(args)


def test_csv_path_runs(tmp_path):
    px, _ = data.synthetic_panel(2, 600, seed=3)
    f = tmp_path / "p.csv"
    px.to_csv(f, index=False)
    args = experiment.parse(["--data", str(f), "--n-splits", "3", "--bootstrap", "30", "--out", str(tmp_path / "o")])
    met, tests, _, _ = experiment.run(args)
    assert len(met) == 21 and "H4b" not in set(tests.hypothesis)
