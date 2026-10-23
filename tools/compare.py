#!/usr/bin/env python3
"""Compare regenerated outputs against the reference numbers committed with the paper.
Usage: python tools/compare.py --tol 0 REF NEW [REF NEW ...]   (JSON: numeric leaves; other files: exact text)
Exit code 0 if every pair matches within --tol (relative, with 1e-12 absolute floor)."""
import argparse, json, math, sys
def leaves(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items(): yield from leaves(v, f"{p}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from leaves(v, f"{p}[{i}]")
    else: yield p, x
SKIP = ("runtime", "elapsed", "seconds", "sec", "time", "timestamp", "date_run", "python", "version", "host", "path", "out", "data")
def cmp_json(a, b, tol):
    A, B = dict(leaves(a)), dict(leaves(b)); bad = []; n = 0; worst = 0.0
    for k, v in A.items():
        last = k.rsplit("/", 1)[-1].split("[")[0].lower()
        if last in SKIP or last.endswith("_s") or any(s in k.lower() for s in ("runtime", "elapsed", "wall", "latency")): continue
        w = B.get(k, "<missing>")
        if isinstance(v, (int, float)) and isinstance(w, (int, float)) and not isinstance(v, bool):
            n += 1
            if v != v and w != w: continue
            d = abs(v - w) / max(abs(v), 1e-12) if abs(v - w) > 1e-12 else 0.0
            worst = max(worst, d)
            if d > tol: bad.append((k, v, w))
        elif v != w: bad.append((k, v, w))
    return n, worst, bad
ap = argparse.ArgumentParser(); ap.add_argument("--tol", type=float, default=0.0); ap.add_argument("pairs", nargs="+")
a = ap.parse_args(); ok = True
for ref, new in zip(a.pairs[::2], a.pairs[1::2]):
    try:
        if ref.endswith(".json"):
            n, worst, bad = cmp_json(json.load(open(ref)), json.load(open(new)), a.tol)
            st = "MATCH" if not bad else "DIFF"
            print(f"[{st}] {new}: {n} numbers, max rel diff {worst:.3g}" + (f", {len(bad)} over tol" if bad else ""))
            for k, v, w in bad[:8]: print(f"     {k}: paper={v} rerun={w}")
        elif ref.endswith(".csv"):
            import csv
            def load(f):
                rows = list(csv.reader(open(f))); out = {}
                for i, r in enumerate(rows):
                    for j, c in enumerate(r):
                        try: out[f"r{i}c{j}"] = float(c)
                        except ValueError: out[f"r{i}c{j}"] = c
                return out
            n, worst, bad = cmp_json(load(ref), load(new), a.tol)
            print(f"[{'MATCH' if not bad else 'DIFF'}] {new}: {n} numbers, max rel diff {worst:.3g}" + (f", {len(bad)} over tol" if bad else ""))
            for k, v, w in bad[:8]: print(f"     {k}: paper={v} rerun={w}")
        else:
            same = open(ref).read() == open(new).read(); bad = not same
            print(f"[{'MATCH' if same else 'DIFF'}] {new} (exact text)")
        ok &= not bad
    except FileNotFoundError as e:
        print(f"[MISSING] {e.filename}"); ok = False
sys.exit(0 if ok else 1)
