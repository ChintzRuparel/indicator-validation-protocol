#!/usr/bin/env python3
"""Portable sha256sum replacement (macOS/Linux).
  sha256check.py -c [LISTFILE|-]   verify "<hash>  <file>" lines (stdin if no file)
  sha256check.py FILE...           print "<hash>  <file>" lines
"""
import hashlib, sys
def h(p):
    d = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): d.update(b)
    return d.hexdigest()
a = [x for x in sys.argv[1:] if x != "--quiet"]
quiet = "--quiet" in sys.argv
if a and a[0] == "-c":
    src = open(a[1]) if len(a) > 1 and a[1] != "-" else sys.stdin
    bad = 0
    for line in src:
        line = line.rstrip("\n")
        if not line.strip(): continue
        want, name = line.split(None, 1)
        name = name.lstrip("*").strip()
        try: ok = h(name) == want.lower()
        except FileNotFoundError: ok = False
        if not ok: bad += 1; print(f"{name}: FAILED")
        elif not quiet: print(f"{name}: OK")
    sys.exit(1 if bad else 0)
for p in a: print(f"{h(p)}  {p}")
