"""End-to-end HITAI experiment: build features -> point-in-time tags -> walk-forward
fusion models with calibrated confidence -> decision layer with costs -> H1-H4 tests
with multiple-testing control -> (optionally, once) untouched holdout.

Usage: python -m hitai.experiment --help
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import platform
import sys
import numpy as np
import pandas as pd
import sklearn
from scipy import stats as sst

from . import data, features, rules, llm_tags, cv, models, stats

TECH, RULE, TAG = features.TECH_FEATURES, rules.RULE_FEATURES, llm_tags.TAG_FEATURES

# Pre-registered feature sets (do not edit after first real-data run; see scope.md)
FEATURE_SETS = {
    "rules_only": RULE,
    "tech_only": TECH,
    "rules_tech": RULE + TECH,
    "hitai_full": RULE + TECH + TAG,
}
# Tag-variant ablations evaluated with the full feature set
TAG_VARIANTS = ["pit", "shuffled", "lagged", "masked"]
MODELS = ["logit", "gbt", "gbt_mono"]
PRIMARY_MODEL = "gbt_mono"   # pre-registered primary model for H1-H4


# ----------------------------------------------------------------------------- data
def build_panel(args):
    if args.data == "synthetic":
        px, news = data.synthetic_panel(args.n_tickers, args.n_days, args.seed, args.signal)
    else:
        px, news = data.load_csv(args.data), None
    df = features.add_technical(px)
    df = features.add_labels(df, args.horizon)
    df = rules.add_rules(df)
    warm = df.groupby("ticker").cumcount() >= 100          # drop indicator warm-up
    df = df[warm].reset_index(drop=True)
    return df, news


def attach_tags(df, news, args, segment_cut=None):
    cache_dir = os.path.join(args.out, "tag_cache")
    honest = llm_tags.MockPITTagger(seed=args.seed)
    c = llm_tags.TagCache(os.path.join(cache_dir, f"{honest.model_version}.jsonl"))
    variants = {}
    pit = llm_tags.add_tags(df, honest, c, news, masked=False)
    variants["pit"] = pit
    variants["masked"] = llm_tags.add_tags(df, honest, c, news, masked=True)
    variants["shuffled"] = llm_tags.shuffle_tags(pit, seed=args.seed, segment_cut=segment_cut)
    variants["lagged"] = llm_tags.lag_tags(pit, lag=args.tag_lag)
    cache_stats = {"honest": {"hits": c.hits, "misses": c.misses}}
    leaky = None
    if args.leaky_demo:
        lt = llm_tags.MockMemorizingTagger(seed=args.seed)
        lc = llm_tags.TagCache(os.path.join(cache_dir, f"{lt.model_version}.jsonl"))
        leaky = {"unmasked": llm_tags.add_tags(df, lt, lc, news, masked=False, oracle=True),
                 "masked": llm_tags.add_tags(df, lt, lc, news, masked=True, oracle=True)}
    # Path/context perturbation for H4b: replace the context with an independent draw.
    pert_news = None
    if news is not None:
        rng = np.random.default_rng(args.seed + 999)
        pert_news = news.copy()
        pert_news["news"] = rng.permutation(pert_news["news"].to_numpy())
        pc = llm_tags.TagCache(os.path.join(cache_dir, f"{honest.model_version}-perturbed.jsonl"))
        variants["_perturbed"] = llm_tags.add_tags(df, honest, pc, pert_news, masked=False)
        if args.leaky_demo:
            leaky["perturbed"] = llm_tags.add_tags(df, lt, lc, pert_news, masked=False, oracle=True)
    return variants, leaky, cache_stats


# ----------------------------------------------------------------------------- modelling
def oos_predictions(df, feats, kind, splits, seed):
    """Walk-forward OOS calibrated & raw probabilities. Each fold: fit on purged train
    (fit part), isotonic on later calib part of train, predict test."""
    p_cal = np.full(len(df), np.nan); p_raw = np.full(len(df), np.nan)
    for tr, te in splits:
        trd = df.iloc[tr]
        f_idx, c_idx = cv.calib_split(trd)
        fit, cal = trd.iloc[f_idx], trd.iloc[c_idx]
        m = models.Calibrated(models.make_model(kind, feats, seed))
        m.fit(fit[feats], fit["y"], cal[feats], cal["y"])
        X = df.iloc[te][feats]
        p_cal[te] = m.predict_proba(X)
        p_raw[te] = m.base.predict_proba(X)[:, 1]
    return p_cal, p_raw


def decision(df, p, tau, cost_bps):
    """Long/short/flat by calibrated probability with dead-band tau; per-ticker turnover cost.
    Returns per-date equal-weight portfolio net & gross returns."""
    d = df[["date", "ticker", "ret_next"]].copy()
    d["p"] = p
    d = d[d["p"].notna() & d["ret_next"].notna()]
    d["pos"] = np.where(d["p"] > 0.5 + tau, 1.0, np.where(d["p"] < 0.5 - tau, -1.0, 0.0))
    d = d.sort_values(["ticker", "date"])
    d["turn"] = d.groupby("ticker")["pos"].diff().abs().fillna(d["pos"].abs())
    d["gross"] = d["pos"] * d["ret_next"]
    d["net"] = d["gross"] - d["turn"] * cost_bps / 1e4
    port = d.groupby("date")[["gross", "net", "turn"]].mean()
    port["exposure"] = d.groupby("date")["pos"].apply(lambda s: s.abs().mean())
    return port


def per_date_loss(df, p):
    y = df["y"].to_numpy()
    pc = np.clip(p, 1e-6, 1 - 1e-6)
    ll = -(y * np.log(pc) + (1 - y) * np.log(1 - pc))
    s = pd.Series(ll, index=df["date"].to_numpy())
    return s[~np.isnan(p)].groupby(level=0).mean()


def forecast_metrics(df, p):
    m = ~np.isnan(p)
    y = df["y"].to_numpy()[m]; q = p[m]
    return {"n": int(m.sum()), "logloss": stats.log_loss(q, y), "brier": stats.brier(q, y),
            "ece": stats.ece(q, y), "auc": stats.auc(q, y), "base_rate": float(y.mean())}


# ----------------------------------------------------------------------------- main
def run(args):
    os.makedirs(args.out, exist_ok=True)
    df, news = build_panel(args)
    _, _, cut0 = cv.holdout_split(df, args.holdout_frac)
    variants, leaky, cache_stats = attach_tags(df, news, args, segment_cut=cut0)
    base = variants["pit"]
    dev, hold, cut = cv.holdout_split(base, args.holdout_frac)
    assert cut == cut0
    dev_idx = dev.index
    splits = list(cv.walk_forward(dev.reset_index(drop=True), args.n_splits, embargo_days=args.embargo))

    def dev_of(v):
        return variants[v].loc[dev_idx].reset_index(drop=True)

    rows, preds, ports = [], {}, {}
    configs = [(fs, "pit") for fs in FEATURE_SETS] + [("hitai_full", v) for v in TAG_VARIANTS if v != "pit"]
    for fs, var in configs:
        d = dev_of(var)
        for kind in MODELS:
            name = f"{fs}|{var}|{kind}"
            pc, pr = oos_predictions(d, FEATURE_SETS[fs], kind, splits, args.seed)
            preds[name] = (pc, pr)
            port = decision(d, pc, args.tau, args.cost_bps)
            ports[name] = port
            fm = forecast_metrics(d, pc)
            fm_raw = forecast_metrics(d, pr)
            r = port["net"].to_numpy()
            rows.append({"config": name, "feature_set": fs, "tag_variant": var, "model": kind, **fm,
                         "ece_uncalibrated": fm_raw["ece"], "logloss_uncalibrated": fm_raw["logloss"],
                         "sharpe_gross_ann": stats.sharpe(port["gross"]), "sharpe_net_ann": stats.sharpe(r),
                         "mean_turnover": float(port["turn"].mean()), "mean_exposure": float(port["exposure"].mean()),
                         "psr_net": stats.psr(r), "max_dd_net": stats.max_drawdown(r)})
            print(f"  {name:38s} logloss={fm['logloss']:.4f} auc={fm['auc']:.3f} ece={fm['ece']:.4f}", flush=True)
    met = pd.DataFrame(rows)
    # Deflated Sharpe across ALL trials run
    srs = np.array([ports[c]["net"].mean() / ports[c]["net"].std(ddof=1) for c in met["config"]])
    met["dsr_net"] = [stats.deflated_sharpe(ports[c]["net"].to_numpy(), srs.var(ddof=1), len(srs))
                      for c in met["config"]]
    met["n_trials"] = len(srs)
    met.to_csv(os.path.join(args.out, "metrics_dev.csv"), index=False)

    d0 = dev_of("pit")
    tests = hypothesis_tests(d0, preds, variants, dev_idx, leaky, args)
    tests.to_csv(os.path.join(args.out, "hypothesis_tests.csv"), index=False)

    # Reality check / SPA: benchmark = rules_only (primary model) on per-date log loss
    bench = f"rules_only|pit|{PRIMARY_MODEL}"
    L = {c: per_date_loss(d0 if c.split("|")[1] == "pit" else dev_of(c.split("|")[1]), preds[c][0]) for c in preds}
    common = sorted(set.intersection(*[set(v.index) for v in L.values()]))
    others = [c for c in preds if c != bench and c.split("|")[1] == "pit"]
    spa = stats.reality_check_spa(L[bench].loc[common].to_numpy(),
                                  np.column_stack([L[c].loc[common].to_numpy() for c in others]),
                                  B=args.bootstrap, mean_block=max(args.horizon * 2, 5), seed=args.seed)
    pd.Series({"benchmark": bench, "n_models": len(others), **spa}).to_csv(os.path.join(args.out, "reality_check_spa.csv"))

    hold_res = None
    if args.unlock_holdout:
        hold_res = run_holdout(variants, dev_idx, hold.index, args)

    manifest = {
        "rules_version": rules.RULES_VERSION, "tagger": "mock-pit-1/p1", "cache": cache_stats,
        "holdout_start": str(cut.date()), "holdout_unlocked": bool(args.unlock_holdout),
        "n_rows_dev": int(len(dev)), "n_rows_holdout": int(len(hold)), "splits": len(splits),
        "args": vars(args), "python": sys.version.split()[0], "sklearn": sklearn.__version__,
        "numpy": np.__version__, "pandas": pd.__version__, "platform": platform.platform(),
        "data_sha256": hashlib.sha256(pd.util.hash_pandas_object(base[["date", "ticker", "close"]]).values.tobytes()).hexdigest()[:16],
    }
    with open(os.path.join(args.out, "run_manifest.json"), "w") as fh:
        json.dump(manifest, fh, indent=2, default=str)
    write_report(args.out, met, tests, spa, hold_res, manifest)
    return met, tests, spa, hold_res


def hypothesis_tests(d0, preds, variants, dev_idx, leaky, args):
    H = args.horizon
    out = []
    for kind in MODELS:
        L = lambda c: per_date_loss(d0, preds[c][0])
        full = L(f"hitai_full|pit|{kind}")

        def dm(a, b, hyp, desc):
            la, lb = a.align(b, join="inner")
            s, p2 = stats.diebold_mariano(la.to_numpy(), lb.to_numpy(), h=H + 1)
            out.append({"hypothesis": hyp, "model": kind, "comparison": desc,
                        "stat": s, "p_one_sided": float(1 - sst.norm.cdf(s)), "mean_loss_diff": float((la - lb).mean())})
        # H1: fusion beats frozen rules alone (positive stat => full has lower loss)
        dm(L(f"rules_only|pit|{kind}"), full, "H1", "rules_only - hitai_full (logloss)")
        # H3: LLM tags add timing-specific info beyond rules+tech; must beat shuffled & lagged
        dm(L(f"rules_tech|pit|{kind}"), full, "H3a", "rules_tech - hitai_full")
        for v in ["shuffled", "lagged"]:
            dv = variants[v].loc[dev_idx].reset_index(drop=True)
            dm(per_date_loss(dv, preds[f"hitai_full|{v}|{kind}"][0]), full, "H3b" if v == "shuffled" else "H3c",
               f"hitai_full[{v}] - hitai_full[pit]")
        # H2: calibrated confidence is reliable (Spiegelhalter on non-overlapping subsample)
        pc = preds[f"hitai_full|pit|{kind}"][0]
        m = ~np.isnan(pc)
        dates = np.sort(d0.loc[m, "date"].unique())[::H + 1]
        sub = m & d0["date"].isin(dates).to_numpy()
        z, p = stats.spiegelhalter_z(pc[sub], d0["y"].to_numpy()[sub])
        y = d0["y"].to_numpy()
        conf = np.abs(pc - 0.5)
        hit = ((pc > 0.5) == (y == 1)).astype(float)
        rho, prho = sst.spearmanr(conf[sub], hit[sub])
        out.append({"hypothesis": "H2a", "model": kind, "comparison": "Spiegelhalter z (H0 calibrated; want NOT rejected)",
                    "stat": z, "p_one_sided": p, "mean_loss_diff": np.nan})
        out.append({"hypothesis": "H2b", "model": kind, "comparison": "Spearman(|p-.5|, hit) on non-overlapping dates",
                    "stat": rho, "p_one_sided": float(prho / 2 if rho > 0 else 1 - prho / 2), "mean_loss_diff": np.nan})
        # H4a: masking does not reduce performance (two-sided, want NOT rejected)
        dmk = variants["masked"].loc[dev_idx].reset_index(drop=True)
        la, lb = per_date_loss(dmk, preds[f"hitai_full|masked|{kind}"][0]).align(full, join="inner")
        s, p2 = stats.diebold_mariano(la.to_numpy(), lb.to_numpy(), h=H + 1)
        out.append({"hypothesis": "H4a", "model": kind, "comparison": "masked - unmasked logloss (two-sided; want NOT rejected)",
                    "stat": s, "p_one_sided": p2, "mean_loss_diff": float((la - lb).mean())})
    # H4b: tag-outcome association collapses under context perturbation (model-free)
    def tag_corr(v):
        dv = v.loc[dev_idx]
        ok = dv["fwd_ret"].notna() & dv["tag_sentiment"].notna()
        return sst.spearmanr(dv.loc[ok, "tag_sentiment"], dv.loc[ok, "fwd_ret"])
    if "_perturbed" in variants:
        r_o, _ = tag_corr(variants["pit"]); r_p, p_p = tag_corr(variants["_perturbed"])
        out.append({"hypothesis": "H4b", "model": "tagger", "comparison": f"corr(tag,fwd) original={r_o:.4f} vs perturbed-context (want ~0)",
                    "stat": r_p, "p_one_sided": p_p, "mean_loss_diff": r_o - r_p})
    if leaky is not None:
        for k in ["unmasked", "masked", "perturbed"]:
            if k in leaky:
                r, p = tag_corr(leaky[k])
                out.append({"hypothesis": "H4-demo", "model": "leaky_tagger", "comparison": f"corr(tag,fwd) {k}",
                            "stat": r, "p_one_sided": p, "mean_loss_diff": np.nan})
    t = pd.DataFrame(out)
    # Multiple-testing control over the confirmatory family (H1, H3a-c with PRIMARY model)
    fam = (t["model"] == PRIMARY_MODEL) & t["hypothesis"].isin(["H1", "H3a", "H3b", "H3c", "H2b"])
    t["confirmatory"] = fam
    t.loc[fam, "p_holm"] = stats.holm(t.loc[fam, "p_one_sided"])
    t.loc[fam, "p_bonferroni"] = stats.bonferroni(t.loc[fam, "p_one_sided"])
    t["p_bh_all"] = stats.benjamini_hochberg(t["p_one_sided"].fillna(1).to_numpy())
    return t


def run_holdout(variants, dev_idx, hold_idx, args):
    """Single-shot evaluation. Writes a lock file; refuses to rerun unless --force-holdout."""
    lock = os.path.join(args.out, "HOLDOUT_USED.lock")
    if os.path.exists(lock) and not args.force_holdout:
        raise SystemExit(f"Holdout already used ({lock}). Re-use invalidates it; pass --force-holdout to override and REPORT it.")
    res = []
    for fs, var in [("rules_only", "pit"), ("rules_tech", "pit"), ("hitai_full", "pit"), ("hitai_full", "shuffled")]:
        v = variants[var]
        full = pd.concat([v.loc[dev_idx], v.loc[hold_idx]]).reset_index(drop=True)
        n_dev = len(dev_idx)
        tr = np.arange(n_dev); te = np.arange(n_dev, len(full))
        trd = full.iloc[tr]
        trd = trd[trd["y"].notna()]
        f_idx, c_idx = cv.calib_split(trd)
        m = models.Calibrated(models.make_model(PRIMARY_MODEL, FEATURE_SETS[fs], args.seed))
        m.fit(trd.iloc[f_idx][FEATURE_SETS[fs]], trd.iloc[f_idx]["y"], trd.iloc[c_idx][FEATURE_SETS[fs]], trd.iloc[c_idx]["y"])
        h = full.iloc[te].reset_index(drop=True)
        h = h[h["y"].notna()].reset_index(drop=True)
        p = m.predict_proba(h[FEATURE_SETS[fs]])
        port = decision(h, p, args.tau, args.cost_bps)
        res.append({"config": f"{fs}|{var}|{PRIMARY_MODEL}", **forecast_metrics(h, p),
                    "sharpe_net_ann": stats.sharpe(port["net"]), "psr_net": stats.psr(port["net"].to_numpy())})
    with open(lock, "w") as fh:
        fh.write(pd.Timestamp.now().isoformat())
    r = pd.DataFrame(res)
    r.to_csv(os.path.join(args.out, "holdout_metrics.csv"), index=False)
    return r


def write_report(out, met, tests, spa, hold, man):
    L = ["# HITAI run report (auto-generated)", "",
         "**No profitability claim.** Synthetic-data numbers only validate the pipeline." if man["args"]["data"] == "synthetic" else
         "**No profitability claim.** Results are statistical evidence under stated assumptions only.", "",
         f"rules_version `{man['rules_version']}`, holdout starts {man['holdout_start']} (unlocked: {man['holdout_unlocked']}), "
         f"dev rows {man['n_rows_dev']}, walk-forward folds {man['splits']}, trials {met['n_trials'].iloc[0]}.", "",
         "## Dev (walk-forward OOS) metrics", "", met.round(4).to_markdown(index=False), "",
         "## Hypothesis tests", "", tests.round(4).to_markdown(index=False), "",
         f"## Reality check / SPA vs rules_only: RC p={spa['rc_p']:.3f}, SPA p={spa['spa_p']:.3f}", ""]
    if hold is not None:
        L += ["## Untouched holdout (single shot)", "", hold.round(4).to_markdown(index=False), ""]
    open(os.path.join(out, "REPORT.md"), "w").write("\n".join(L))


def parse(argv=None):
    a = argparse.ArgumentParser(description="HITAI experiment")
    a.add_argument("--data", default="synthetic", help="'synthetic' or path to long OHLCV csv")
    a.add_argument("--out", default="results/smoke")
    a.add_argument("--n-tickers", type=int, default=8)
    a.add_argument("--n-days", type=int, default=1500)
    a.add_argument("--horizon", type=int, default=5)
    a.add_argument("--n-splits", type=int, default=5)
    a.add_argument("--embargo", type=int, default=5)
    a.add_argument("--holdout-frac", type=float, default=0.2)
    a.add_argument("--tau", type=float, default=0.02, help="decision dead-band around 0.5")
    a.add_argument("--cost-bps", type=float, default=10.0, help="one-way cost per unit turnover")
    a.add_argument("--tag-lag", type=int, default=20)
    a.add_argument("--bootstrap", type=int, default=300)
    a.add_argument("--seed", type=int, default=0)
    a.add_argument("--signal", type=float, default=0.25, help="synthetic only: strength of PIT news->drift link (0 = pure null)")
    a.add_argument("--leaky-demo", action="store_true", help="also run deliberately-leaky tagger to validate H4 test")
    a.add_argument("--unlock-holdout", action="store_true")
    a.add_argument("--force-holdout", action="store_true")
    return a.parse_args(argv)


if __name__ == "__main__":
    run(parse())
