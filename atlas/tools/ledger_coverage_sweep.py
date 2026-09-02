#!/usr/bin/env python3
"""
ledger_coverage_sweep.py
========================
STOP FINDING LEDGER MISSES ONE AT A TIME AND CALLING EACH ONE "THE NTH INSTANCE".

Every miss in the last twelve rounds was found the same way: a node carrying a real
endpoint that CLAUDE.md never names. The androgen arm (R419), the androgen_receptor
closure (R420), amplification (R423), osteocrin (R424), noonan2004 (R427), the
seventeen-node loading layer (R426), resveratrol, and the entire RARgamma arm
(R255-R261, found by the R431 audit). CORR-352 says the ledger is lossy in BOTH
directions - it loses positives and closures alike - and the fix written down three
times is "grep the graph before drafting". That fix has failed repeatedly because it
is a manual step.

This runs it mechanically. For every node:
  - does its text contain a LENGTH/STATURE term AND a DIRECTION term?
  - is the node id named in CLAUDE.md?
  - how many of its key_refs are named in CLAUDE.md?
Rank by (endpoint present) x (fewest refs in the ledger). The top of that list is
where the next miss is.

Run it before committing a round. If a node you are about to build on is near the
top, read it first.

Usage:
    python3 atlas/tools/ledger_coverage_sweep.py            # top 40
    python3 atlas/tools/ledger_coverage_sweep.py --all      # everything uncovered
    python3 atlas/tools/ledger_coverage_sweep.py --json OUT
"""
from __future__ import annotations
import os
import re
import sys
import json
import yaml

NODES = "atlas/nodes"
LEDGER = "CLAUDE.md"

# An endpoint this file treats as decisive: bone or body LENGTH, not a proxy.
LENGTH = re.compile(
    r"\b(bone length|body length|femur length|femoral length|tibia length|tibial length|"
    r"limb length|ulna length|naso-?anal|nasoanal|crown-?rump|stature|adult height|"
    r"final height|attained height|height velocity|longitudinal growth|elongation|"
    r"vertebral length|standing height|sitting height)\b", re.I)

# A signed direction. Without one an endpoint is an observation, not a result.
DIRECTION = re.compile(
    r"\b(longer|shorter|lengthen\w*|shorten\w*|increase[sd]?|decrease[sd]?|"
    r"greater|reduced|taller|\+\d|\bgain\w*|per cent longer|% longer)\b", re.I)

# Terms that mark a node as already-closed housekeeping rather than a live endpoint.
NEGATIVE_HINT = re.compile(r"\b(stub|placeholder|scaffold only)\b", re.I)


def load_ledger() -> str:
    with open(LEDGER, encoding="utf-8", errors="ignore") as fh:
        return fh.read()


def iter_nodes():
    for root, _dirs, files in os.walk(NODES):
        for fn in sorted(files):
            if not fn.endswith(".yaml"):
                continue
            path = os.path.join(root, fn)
            try:
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    raw = fh.read()
                doc = yaml.safe_load(raw)
            except Exception:
                continue
            if not isinstance(doc, dict):
                continue
            yield path, raw, doc


def refs_of(doc: dict) -> list:
    out = []
    for r in doc.get("key_refs") or []:
        if isinstance(r, dict):
            rid = r.get("ref_id")
        else:
            rid = r
        if rid:
            out.append(str(rid))
    return out


def main() -> None:
    ledger = load_ledger()
    ledger_l = ledger.lower()
    show_all = "--all" in sys.argv
    outpath = None
    if "--json" in sys.argv:
        outpath = sys.argv[sys.argv.index("--json") + 1]

    recs = []
    for path, raw, doc in iter_nodes():
        if doc.get("stub"):
            continue
        nid = str(doc.get("id") or "")
        text = raw
        has_len = bool(LENGTH.search(text))
        has_dir = bool(DIRECTION.search(text))
        if not (has_len and has_dir):
            continue
        if NEGATIVE_HINT.search(str(doc.get("name") or "")):
            continue
        refs = refs_of(doc)
        in_ledger = nid.lower() in ledger_l if nid else False
        present = [r for r in refs if r.lower() in ledger_l]
        missing = [r for r in refs if r.lower() not in ledger_l]
        frac = (len(present) / len(refs)) if refs else (1.0 if in_ledger else 0.0)
        recs.append({
            "id": nid or os.path.basename(path),
            "path": os.path.relpath(path),
            "name": str(doc.get("name") or "")[:110],
            "node_in_ledger": in_ledger,
            "n_refs": len(refs),
            "refs_in_ledger": len(present),
            "refs_missing": missing[:8],
            "coverage": round(frac, 3),
            "confidence": doc.get("confidence"),
        })

    # Uncovered = the node itself is not named AND most of its refs are not named.
    uncovered = [r for r in recs if not r["node_in_ledger"]]
    uncovered.sort(key=lambda r: (r["coverage"], -r["n_refs"]))

    print(f"nodes with a LENGTH endpoint AND a signed direction : {len(recs)}")
    print(f"  of those, NOT named in CLAUDE.md                  : {len(uncovered)}")
    fully = [r for r in uncovered if r["n_refs"] and r["refs_in_ledger"] == 0]
    print(f"  of those, with ZERO of their refs in CLAUDE.md    : {len(fully)}")
    print()
    print("RANKED BY LEDGER COVERAGE (lowest first). The top of this list is where the")
    print("next miss is. Read before building on anything near it.\n")
    lim = len(uncovered) if show_all else 40
    for r in uncovered[:lim]:
        print(f"  [{r['coverage']:.2f}] {r['refs_in_ledger']}/{r['n_refs']} refs  "
              f"{r['confidence'] or '-'}  {r['id'][:72]}")
        if r["refs_missing"]:
            print(f"        missing refs: {', '.join(r['refs_missing'])}")

    if outpath:
        with open(outpath, "w") as fh:
            json.dump({"n_with_endpoint": len(recs), "uncovered": uncovered}, fh, indent=1)
        print(f"\n  written: {outpath}")


if __name__ == "__main__":
    main()
