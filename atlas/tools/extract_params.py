#!/usr/bin/env python3
"""
Harvest every `quantitative:` row from every node into quant/parameters.csv,
and run consistency checks over the result.

The CSV is a derived artifact - nodes are the source of truth, so this is safe
to re-run at any time. Checks performed:
  - unit sanity: values that parse as numbers get a magnitude check per unit
    family, flagging implausible entries (e.g. a growth velocity in um/day that
    would imply metres per year)
  - unit inconsistency: the same parameter name expressed in different units
    across nodes
  - spread: where >1 source gives a value for the same parameter, report the
    range so disagreement is visible rather than averaged away
  - unverified: count of value_unverified rows, which must stay auditable
  - missing species / source, which the validator also enforces

Usage:
  python3 atlas/tools/extract_params.py            # write CSV + report
  python3 atlas/tools/extract_params.py --check    # report only, no write
"""
import os, sys, csv, glob, re, argparse
from collections import defaultdict
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "quant", "parameters.csv")

FIELDS = ["param_id", "layer", "node_id", "parameter", "value", "value_min",
          "value_max", "unit", "conditions", "species", "site", "age", "sex",
          "source_ref", "uncertainty", "value_unverified", "notes"]

# plausibility envelopes: unit -> (low, high) for a single scalar value.
# Deliberately wide - this catches order-of-magnitude blunders, not fine detail.
ENVELOPE = {
    "um/day": (0.1, 1000), "µm/day": (0.1, 1000),
    "um": (0.01, 10000), "µm": (0.01, 10000),
    "mm": (0.001, 1000), "cm": (0.01, 300),
    "cm/yr": (0.01, 40), "cm/year": (0.01, 40),
    "%": (0, 100), "h": (0.1, 1000), "hours": (0.1, 1000),
    "days": (0.01, 20000), "years": (0, 120),
    "sds": (-10, 10), "sd": (-10, 10), "z-score": (-10, 10),
    "nm": (0.0001, 1e6), "um_conc": (1e-6, 1e6),
    "fold": (0.001, 1000), "kb": (0.001, 1e6),
}


def num(v):
    """Return (point, lo, hi) parsed from a value string, or (None, None, None)."""
    if v is None:
        return None, None, None
    s = str(v).strip().replace(",", "")
    m = re.fullmatch(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", s)
    if m:
        f = float(s)
        return f, f, f
    m = re.fullmatch(r"([-+]?\d*\.?\d+)\s*[-–—to]+\s*([-+]?\d*\.?\d+)", s)
    if m:
        lo, hi = float(m.group(1)), float(m.group(2))
        return (lo + hi) / 2, lo, hi
    m = re.match(r"[~<>≈]\s*([-+]?\d*\.?\d+)", s)
    if m:
        f = float(m.group(1))
        return f, f, f
    return None, None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    rows, problems = [], []
    by_param = defaultdict(list)
    n = 0

    for p in sorted(glob.glob(os.path.join(ROOT, "nodes", "**", "*.yaml"),
                              recursive=True)):
        with open(p) as f:
            node = yaml.safe_load(f) or {}
        if not isinstance(node, dict):
            continue
        for q in (node.get("quantitative") or []):
            if not isinstance(q, dict):
                continue
            n += 1
            pid = f"p{n:05d}"
            point, lo, hi = num(q.get("value"))
            unit = str(q.get("unit") or "").strip()
            row = {
                "param_id": pid, "layer": node.get("layer"),
                "node_id": node.get("id"), "parameter": q.get("parameter"),
                "value": q.get("value"), "value_min": lo, "value_max": hi,
                "unit": unit, "conditions": q.get("conditions"),
                "species": q.get("species"), "site": q.get("site"),
                "age": q.get("age"), "sex": q.get("sex"),
                "source_ref": q.get("source_ref"),
                "uncertainty": q.get("uncertainty"),
                "value_unverified": bool(q.get("value_unverified")),
                "notes": q.get("notes"),
            }
            rows.append(row)
            key = re.sub(r"\s+", " ", str(q.get("parameter") or "").lower()).strip()
            by_param[key].append(row)

            env = ENVELOPE.get(unit.lower())
            if env and point is not None and not (env[0] <= abs(point) <= env[1]):
                problems.append(f"IMPLAUSIBLE {pid} {node.get('id')}: "
                                f"{q.get('parameter')} = {q.get('value')} {unit} "
                                f"(envelope {env[0]}-{env[1]})")
            if point is None and str(q.get("value") or "").strip():
                problems.append(f"UNPARSED  {pid} {node.get('id')}: "
                                f"value '{q.get('value')}' is not numeric - fine if "
                                f"categorical, check if not")

    # unit inconsistency + spread across sources
    for key, rs in sorted(by_param.items()):
        units = {r["unit"] for r in rs if r["unit"]}
        if len(units) > 1:
            problems.append(f"UNIT-CLASH '{key}': {sorted(units)} "
                            f"(nodes: {sorted({r['node_id'] for r in rs})})")
        srcs = {r["source_ref"] for r in rs if r["source_ref"]}
        pts = [r["value_min"] for r in rs if r["value_min"] is not None]
        if len(srcs) > 1 and len(pts) > 1 and len(units) <= 1:
            lo, hi = min(pts), max(pts)
            if lo and hi and hi > lo * 1.5:
                problems.append(f"SPREAD    '{key}': {lo}-{hi} across "
                                f"{len(srcs)} sources {sorted(srcs)} - disagreement, "
                                f"do not average; report the range")

    if not a.check:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            w.writeheader()
            for r in rows:
                w.writerow(r)

    unver = sum(1 for r in rows if r["value_unverified"])
    nosrc = sum(1 for r in rows if not r["source_ref"])
    print(f"parameters extracted : {len(rows)}")
    print(f"distinct parameters  : {len(by_param)}")
    print(f"value_unverified     : {unver}")
    print(f"missing source_ref   : {nosrc}")
    print(f"nodes contributing   : {len({r['node_id'] for r in rows})}")
    if not a.check:
        print(f"written              : {os.path.relpath(OUT, ROOT)}")
    if problems:
        print(f"\n--- {len(problems)} consistency flags ---")
        for x in problems[:40]:
            print("  " + x)
        if len(problems) > 40:
            print(f"  ... and {len(problems)-40} more")
    else:
        print("\nno consistency flags")
    return 0


if __name__ == "__main__":
    sys.exit(main())
