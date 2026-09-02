#!/usr/bin/env python3
"""
Create stub nodes in bulk (Phase 1, the ontology coastline).

Input: a TSV on stdin or a file, one node per line:
    node_id <TAB> Name <TAB> type <TAB> layer [<TAB> alias1;alias2]

Stubs carry only id/name/type/layer/aliases and stub: true. They are exempt from
the full-schema requirements until researched, but they ARE validated for
controlled-vocabulary correctness, so a typo in a type or layer fails fast.

Usage:  python3 atlas/tools/mkstub.py stubs.tsv
        python3 atlas/tools/mkstub.py stubs.tsv --overwrite   # re-stub existing
"""
import os, sys, argparse, time
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("infile")
    ap.add_argument("--overwrite", action="store_true")
    a = ap.parse_args()

    vocab = yaml.safe_load(open(os.path.join(ROOT, "schema", "vocab.yaml")))
    types, layers = set(vocab["node_types"]), vocab["layers"]
    dirname = {L: f"{L}_{n}" for L, n in layers.items()}

    made = skipped = bad = 0
    today = time.strftime("%Y-%m-%d")
    seen = {}
    for ln, line in enumerate(open(a.infile), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = [p.strip() for p in line.split("\t")]
        if len(parts) < 4:
            print(f"  ✗ line {ln}: needs 4 fields, got {len(parts)}: {line[:60]}"); bad += 1; continue
        nid, name, ntype, layer = parts[0], parts[1], parts[2], parts[3]
        aliases = [x.strip() for x in parts[4].split(";") if x.strip()] if len(parts) > 4 else []

        if ntype not in types:
            print(f"  ✗ line {ln}: bad type '{ntype}' for {nid}"); bad += 1; continue
        if layer not in layers:
            print(f"  ✗ line {ln}: bad layer '{layer}' for {nid}"); bad += 1; continue
        if nid in seen:
            print(f"  ✗ line {ln}: duplicate id '{nid}' (also line {seen[nid]})"); bad += 1; continue
        seen[nid] = ln

        path = os.path.join(ROOT, "nodes", dirname[layer], f"{nid}.yaml")
        # a node may already exist in a DIFFERENT layer dir - that is a duplicate
        import glob as _g
        existing = _g.glob(os.path.join(ROOT, "nodes", "*", f"{nid}.yaml"))
        if existing and not a.overwrite:
            skipped += 1; continue
        if existing and a.overwrite:
            for e in existing:
                if e != path:
                    os.remove(e)

        doc = {"id": nid, "name": name, "type": ntype, "layer": layer, "stub": True,
               "human_evidence": "absent", "last_verified": today}
        if aliases:
            doc["aliases"] = aliases
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            yaml.safe_dump(doc, f, sort_keys=False, default_flow_style=False,
                           allow_unicode=True)
        made += 1

    print(f"stubs created {made}, already existed {skipped}, rejected {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
