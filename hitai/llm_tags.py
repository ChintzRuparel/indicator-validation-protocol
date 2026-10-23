"""Constrained, point-in-time LLM context tags with caching and versioning.

Contract for any tagger (real LLM or mock):
  * tag(ticker, date, context) -> dict of a FIXED small schema (TAG_SCHEMA), values in
    closed sets/ranges, so the LLM cannot inject free-form or numeric forecasts.
  * `context` must be assembled ONLY from documents with publish_ts <= date's cutoff
    (enforced by `build_context`), never including prices after `date`.
  * Every call is cached in an append-only JSONL keyed by
    (provider, model_version, prompt_version, ticker_or_alias, date, masked); cached rows store
    `asof` and a SHA of the context. Re-runs read from cache => reproducible.
  * Model knowledge cutoff is recorded; samples with date <= cutoff are flagged
    `in_pretrain_window` for the memorization analysis (H4).

Real LLM providers are NOT called in the smoke run. See RealLLMTagger stub.
"""
from __future__ import annotations
import hashlib
import json
import os
import numpy as np
import pandas as pd

TAG_SCHEMA = {
    "sentiment": [-1, 0, 1],            # negative / neutral / positive
    "event_risk": [0, 1],               # scheduled/unscheduled event flagged
    "regime": ["calm", "stressed"],
    "confidence": [0, 1, 2],            # tagger self-reported low/med/high
}
TAG_FEATURES = ["tag_sentiment", "tag_event_risk", "tag_regime_stressed", "tag_confidence"]


def validate_tag(t: dict) -> dict:
    for k, allowed in TAG_SCHEMA.items():
        if t.get(k) not in allowed:
            raise ValueError(f"tag {k}={t.get(k)!r} not in schema {allowed}")
    return t


def alias(ticker: str, salt: str = "hitai") -> str:
    """Deterministic ticker mask for the memorization test (no real name in prompt)."""
    return "ASSET_" + hashlib.sha256((salt + ticker).encode()).hexdigest()[:8]


class TagCache:
    def __init__(self, path: str):
        self.path = path
        self.mem: dict[str, dict] = {}
        if os.path.exists(path):
            with open(path) as fh:
                for line in fh:
                    r = json.loads(line)
                    self.mem[r["key"]] = r
        self.hits = self.misses = 0

    @staticmethod
    def key(provider, model_version, prompt_version, tk, date, masked):
        return f"{provider}|{model_version}|{prompt_version}|{tk}|{pd.Timestamp(date).date()}|{int(masked)}"

    def get(self, k):
        r = self.mem.get(k)
        self.hits += r is not None
        self.misses += r is None
        return r

    def put(self, k, rec):
        rec = dict(rec, key=k)
        self.mem[k] = rec
        os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)
        with open(self.path, "a") as fh:
            fh.write(json.dumps(rec, default=str) + "\n")


class MockPITTagger:
    """Honest mock: reads only the synthetic `news` value published at the close of `date`.
    Discretizes it into the schema with noise. No access to future data by construction."""
    provider, model_version, prompt_version = "mock", "mock-pit-1", "p1"
    knowledge_cutoff = pd.Timestamp("1900-01-01")   # mock has no pretraining

    def __init__(self, seed: int = 0):
        self.seed = seed

    def tag(self, ticker, date, context):
        h = int(hashlib.sha256(f"{self.seed}{ticker}{date}".encode()).hexdigest()[:8], 16)
        r = np.random.default_rng(h)
        s = context.get("news", 0.0) + r.normal(0, 0.5)   # no text supplied -> pure noise tags
        return validate_tag({
            "sentiment": int(np.sign(s) if abs(s) > 0.5 else 0),
            "event_risk": int(abs(s) > 1.5),
            "regime": "stressed" if context.get("vol_20", 0) and context["vol_20"] > 0.015 else "calm",
            "confidence": int(min(2, abs(s) // 0.75)),
        })


class MockMemorizingTagger(MockPITTagger):
    """Deliberately LEAKY mock used to validate the memorization test (H4 / tests).
    When it 'recognizes' the ticker (unmasked) and date is inside its knowledge window,
    it peeks at the realized forward return, like an LLM that memorized history."""
    model_version = "mock-leaky-1"
    knowledge_cutoff = pd.Timestamp("2099-01-01")

    def tag(self, ticker, date, context):
        base = super().tag(ticker, date, context)
        if not context.get("masked") and context.get("_oracle_fwd_ret") is not None \
                and pd.Timestamp(date) <= self.knowledge_cutoff:
            base["sentiment"] = int(np.sign(context["_oracle_fwd_ret"]))
        return validate_tag(base)


class RealLLMTagger:  # pragma: no cover - requires API key and data licence
    """Stub. Implement with the chosen provider (see open_questions.md). Must:
    temperature=0, fixed seed if supported, pinned model snapshot id, JSON-schema output,
    prompt containing ONLY build_context() output, and the model's documented knowledge cutoff."""
    def tag(self, ticker, date, context):
        raise NotImplementedError("Configure provider; see open_questions.md")


def build_context(row: pd.Series, news_lookup: dict | None, masked: bool,
                  oracle: bool = False) -> dict:
    """Assemble point-in-time context for (ticker, date). `oracle=True` is used ONLY to
    feed the deliberately-leaky test tagger; honest pipelines never set it."""
    ctx = {"masked": masked, "date": str(pd.Timestamp(row["date"]).date()),
           "vol_20": None if pd.isna(row.get("vol_20")) else float(row["vol_20"])}
    if news_lookup is not None:
        ctx["news"] = float(news_lookup.get((row["ticker"], row["date"]), 0.0))
    if oracle:
        ctx["_oracle_fwd_ret"] = None if pd.isna(row.get("fwd_ret")) else float(row["fwd_ret"])
    return ctx


def add_tags(df: pd.DataFrame, tagger, cache: TagCache, news: pd.DataFrame | None = None,
             masked: bool = False, oracle: bool = False) -> pd.DataFrame:
    lookup = None if news is None else {(t, d): v for t, d, v in news[["ticker", "date", "news"]].itertuples(index=False)}
    recs = []
    for _, row in df.iterrows():
        tk = alias(row["ticker"]) if masked else row["ticker"]
        ctx = build_context(row, lookup, masked, oracle)
        ctx_sha = hashlib.sha256(json.dumps({k: v for k, v in ctx.items() if not k.startswith("_")},
                                            sort_keys=True).encode()).hexdigest()[:16]
        k = TagCache.key(tagger.provider, tagger.model_version, tagger.prompt_version, tk, row["date"], masked)
        hit = cache.get(k)
        if hit is None or hit.get("ctx_sha") != ctx_sha:
            t = tagger.tag(tk, row["date"], ctx)
            hit = {"tags": t, "asof": str(pd.Timestamp(row["date"]).date()), "ctx_sha": ctx_sha,
                   "in_pretrain_window": bool(pd.Timestamp(row["date"]) <= tagger.knowledge_cutoff)}
            cache.put(k, hit)
        if pd.Timestamp(hit["asof"]) > pd.Timestamp(row["date"]):
            raise AssertionError(f"tag asof {hit['asof']} after decision date {row['date']}")
        t = hit["tags"]
        recs.append((t["sentiment"], t["event_risk"], int(t["regime"] == "stressed"), t["confidence"],
                     hit["in_pretrain_window"]))
    out = df.copy()
    out[TAG_FEATURES + ["in_pretrain_window"]] = pd.DataFrame(recs, index=df.index)
    return out


def shuffle_tags(df: pd.DataFrame, seed: int = 0, segment_cut=None) -> pd.DataFrame:
    """Ablation: permute tag rows across dates WITHIN ticker and WITHIN segment
    (dev vs holdout, split at `segment_cut`) so no holdout-period tag value is moved into dev.
    Destroys timing, keeps the marginal distribution."""
    out = df.copy()
    rng = np.random.default_rng(seed)
    seg = np.zeros(len(out), int) if segment_cut is None else (out["date"] >= segment_cut).astype(int).to_numpy()
    for _, idx in out.groupby([out["ticker"], seg]).groups.items():
        idx = np.asarray(idx)
        out.loc[idx, TAG_FEATURES] = out.loc[rng.permutation(idx), TAG_FEATURES].to_numpy()
    return out


def lag_tags(df: pd.DataFrame, lag: int = 20) -> pd.DataFrame:
    """Ablation: use tags from `lag` days earlier (stale info). Still point-in-time safe."""
    out = df.copy()
    out[TAG_FEATURES] = out.groupby("ticker")[TAG_FEATURES].shift(lag)
    return out
