#!/usr/bin/env python3
"""Write results/RESULTS.md: headline numbers, environment, data hashes, pass/fail vs paper/reference.
Called at the end of run_all.sh. Usage:
  python tools/write_results.py --title T --log results/run_log.txt [--copy SRC:DST ...] [--data DIR ...] [--headline FILE ...]"""
import argparse, csv, datetime, glob, hashlib, json, os, platform, re, shutil, subprocess, sys
ap = argparse.ArgumentParser()
ap.add_argument("--title", required=True); ap.add_argument("--log", default="results/run_log.txt")
ap.add_argument("--mode", default="default"); ap.add_argument("--copy", nargs="*", default=[])
ap.add_argument("--data", nargs="*", default=[]); ap.add_argument("--headline", nargs="*", default=[])
ap.add_argument("--note", default=""); ap.add_argument("--data-ref", default="")
a = ap.parse_args(); R = "results"; os.makedirs(R, exist_ok=True)
for c in a.copy:  # bring outputs that live outside results/ into results/
    src, dst = c.split(":", 1)
    for s in glob.glob(src):
        d = os.path.join(R, dst)
        if os.path.isdir(s): shutil.copytree(s, d, dirs_exist_ok=True)
        else: os.makedirs(os.path.dirname(d) or R, exist_ok=True); shutil.copy2(s, d)
def sh(cmd):
    try: return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60).stdout.strip()
    except Exception: return ""
def sha(f):
    h = hashlib.sha256()
    with open(f, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
L = [f"# Results: {a.title}", "", "Generated automatically by `run_all.sh` (tools/write_results.py). Do not edit by hand.", ""]
if a.note: L += [a.note, ""]
# ---- pass/fail
log = open(a.log, errors="replace").read() if os.path.exists(a.log) else ""
chk = list(dict.fromkeys(l.strip() for l in log.splitlines() if re.match(r"\s*\[(MATCH|DIFF|MISSING)\]", l) or l.strip().startswith(("!!", "WARNING", "FAILED"))))
nm = sum("[MATCH]" in l for l in chk); nd = sum(("[DIFF]" in l) or ("[MISSING]" in l) for l in chk)
L += ["## Check against the paper's reference numbers", ""]
if not chk: L += ["No reference comparison was run in this mode.", ""]
else:
    L += [f"**Overall: {'PASS' if nd == 0 else 'DIFFERENCES FOUND'}** ({nm} matched, {nd} differ/missing).", "", "```"] + chk + ["```", ""]
    if nd: L += ["Differences on downloaded market/public data are expected to be small (providers revise history); synthetic/seeded outputs should match exactly. See the README.", ""]
# ---- headline numbers
def show(f):
    out = [f"### `{f}`", ""]
    if f.endswith((".md", ".txt")):
        t = open(f, errors="replace").read().splitlines()
        out += (t[:80] + (["... (truncated)"] if len(t) > 80 else [])) if f.endswith(".md") else ["```"] + t[:80] + ["```"]
    elif f.endswith(".csv"):
        rows = list(csv.reader(open(f)))
        if rows:
            fmt = lambda c: (f"{float(c):.4g}" if re.fullmatch(r"-?\d+\.\d{5,}(e-?\d+)?", c) else c)
            out += ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * len(rows[0])]
            out += ["| " + " | ".join(fmt(c) for c in r) + " |" for r in rows[1:31]]
            if len(rows) > 31: out += [f"... ({len(rows)-1} rows; see file)"]
    elif f.endswith(".json"):
        def lv(x, p=""):
            if isinstance(x, dict):
                for k, v in x.items(): yield from lv(v, f"{p}.{k}" if p else k)
            elif isinstance(x, list) and len(x) <= 6:
                for i, v in enumerate(x): yield from lv(v, f"{p}[{i}]")
            elif not isinstance(x, list): yield p, x
        items = [(k, v) for k, v in lv(json.load(open(f))) if isinstance(v, (int, float, bool, str)) and len(str(v)) < 80]
        out += ["| key | value |", "|---|---|"] + [f"| {k} | {(f'{v:.4g}' if isinstance(v, float) else v)} |" for k, v in items[:60]]
        if len(items) > 60: out += [f"... ({len(items)} values; see file)"]
    return out + [""]
L += ["## Headline numbers (map to the paper's tables)", ""]
for pat in a.headline:
    fs = sorted(glob.glob(pat))
    if not fs: L += [f"### `{pat}`", "", "_not produced in this mode_", ""]
    for f in fs: L += show(f)
# ---- environment
L += ["## Run information", "", f"- Run date: {datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')}",
      f"- Mode: `{a.mode}`", f"- Git commit: `{sh('git rev-parse HEAD 2>/dev/null') or 'n/a (not a git checkout yet)'}`" + (" (uncommitted changes)" if sh("git status --porcelain 2>/dev/null") else ""),
      f"- Python: {platform.python_version()} ({platform.platform()})", f"- CPUs: {os.cpu_count()}", "", "Package versions (pinned in requirements.txt):", "", "```"]
L += [l for l in sh(f"{sys.executable} -m pip freeze").splitlines() if l and not l.startswith("-e")] + ["```", ""]
# ---- data hashes
L += ["## Data hashes (sha256)", ""]
hs = []
for d in a.data:
    for f in sorted(glob.glob(os.path.join(d, "**", "*"), recursive=True)):
        if os.path.isfile(f): hs.append(f"{sha(f)}  {f}")
if hs:
    open(os.path.join(R, "data_sha256.txt"), "w").write("\n".join(hs) + "\n")
    if a.data_ref and os.path.exists(a.data_ref):
        ref = open(a.data_ref).read(); ref = dict((v, k) for k, v in json.loads(ref).items()) if a.data_ref.endswith(".json") else {l.split()[1]: l.split()[0] for l in ref.splitlines() if l.strip()}
        got = {h.split()[1]: h.split()[0] for h in hs}; same = sum(1 for k, v in ref.items() if got.get(k) == v or v in got.values())
        L += [f"Compared with the paper's data (`{a.data_ref}`): {same}/{len(ref)} files identical" + ("." if same == len(ref) else " -> the provider revised history since the paper run, so real-data numbers can drift slightly."), ""]
    L += [f"{len(hs)} input files hashed; full list in `results/data_sha256.txt`.", "", "```"] + hs[:40] + (["..."] if len(hs) > 40 else []) + ["```", ""]
else: L += ["All inputs are generated from fixed seeds inside the run (no external data files)." if not a.data else "No data files found.", ""]
# ---- inventory + size guard (files > 10 MB are git-ignored to keep results/ small)
big, tot, inv = [], 0, []
for f in sorted(glob.glob(os.path.join(R, "**", "*"), recursive=True)):
    if os.path.isfile(f) and not re.search(r"(/daily/|/ledgers/|\.jsonl$)", f) or (os.path.isfile(f) and re.search(r"/metrics[^/]*\.jsonl$", f)):
        s = os.path.getsize(f)  # daily/, ledgers/ and *.jsonl are git-ignored (see .gitignore), so not counted
        if s > 10e6: big.append(os.path.relpath(f, R))
        else: tot += s
gi = os.path.join(R, ".gitignore")
if big: open(gi, "w").write("# auto: files >10 MB, not committed\n" + "\n".join(big) + "\n")
elif os.path.exists(gi): os.remove(gi)
L += ["## Output files", "", f"Total committed size of `results/`: {tot/1e6:.1f} MB" + (" (WARNING: above 50 MB)" if tot > 50e6 else "") + ".",
      *( [f"Large files left out of git (results/.gitignore): {', '.join(big)}"] if big else []), ""]
open(os.path.join(R, "RESULTS.md"), "w").write("\n".join(L) + "\n")
print(f"wrote results/RESULTS.md ({'PASS' if nd == 0 else 'DIFF'}; {nm} match, {nd} diff)")
