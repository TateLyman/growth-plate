#!/usr/bin/env python3
"""
ROUND 298 - the exhaustive druggability sweep. For EVERY gene this atlas has ever
nominated, does a real drug exist, and has this file ever mentioned it?

Round 297 audited 39 accessible drugs chosen from memory and found 30 with zero coverage.
That was a hand-curated list, so its ceiling was my own recall. This tool removes that
ceiling by inverting the direction of the question:

    atlas genes  ->  Open Targets  ->  every drug/clinical candidate against them
                 ->  subtract every drug name the atlas already mentions
                 ->  what is left is a real agent against a target THIS FILE NOMINATED
                     and has never once written down.

That is a different object from round 297's list. Round 297 asked "which accessible drugs
are missing?" and answered from a list I wrote. This asks "which of OUR OWN TARGETS are
already drugged?" and answers from a database.

INPUTS
  Gene set is built from the atlas itself, not from memory: every node typed gene,
  protein or hormone contributes its symbol, plus the explicitly nominated sets the file
  carries in CLAUDE.md (kosmicki2026's height genes, the hedgehog availability layer, the
  volume machinery, the CNP and FGFR3 and GH axes, Wnt, the epigenetic arm, matrix,
  steroid and cytokine nodes).

OUTPUT  atlas/data/round298/druggability_sweep.json  and a ranked console report.

WHAT A HIT MEANS, AND WHAT IT DOES NOT. A drug appearing here is a molecule that exists
and engages a protein the atlas cares about. It is NOT evidence of a height effect, and
almost none of these will have a bone-length endpoint. The point is to separate three
very different situations that the atlas has been collapsing into one:
  (a) no molecule exists          - HHIP, the volume axis. No searching repairs this.
  (b) a molecule exists, wrong direction - the PIEZO1/Yoda1 and KDM5 cases.
  (c) a molecule exists, never considered - what this tool is for.

Usage:  python3 atlas/tools/round298_druggability_sweep.py [--genes FILE] [--max-genes N]
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.platform.opentargets.org/api/v4/graphql"
OUT = os.path.join(ROOT, "data", "round298")
NODES = os.path.join(ROOT, "nodes")
BIB = os.path.join(ROOT, "sources", "bibliography.yaml")


def gql(query, variables=None, tries=4):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    for i in range(tries):
        try:
            r = urllib.request.Request(API, data=body,
                                       headers={"Content-Type": "application/json",
                                                "User-Agent": "growth-atlas/1.0"})
            return json.loads(urllib.request.urlopen(r, timeout=90).read())
        except Exception as e:
            if i == tries - 1:
                return {"errors": [str(e)]}
            time.sleep(2 ** i)


MAP = 'query($t:[String!]!){mapIds(queryTerms:$t,entityNames:["target"]){mappings{term hits{id name}}}}'
TARGETS = """query($ids:[String!]!){targets(ensemblIds:$ids){
  id approvedSymbol
  tractability{label modality value}
  drugAndClinicalCandidates{count rows{drug{id name drugType maximumClinicalStage
    mechanismsOfAction{rows{actionType mechanismOfAction}}}}}
}}"""


def resolve(symbols, chunk=100):
    out = {}
    for i in range(0, len(symbols), chunk):
        part = symbols[i:i + chunk]
        d = gql(MAP, {"t": part})
        for m in ((d.get("data") or {}).get("mapIds") or {}).get("mappings", []) or []:
            hits = m.get("hits") or []
            if hits:
                out[m["term"]] = hits[0]["id"]
        sys.stderr.write("resolved %d/%d\n" % (min(i + chunk, len(symbols)), len(symbols)))
    return out


def fetch(ids, chunk=25):
    rows = []
    for i in range(0, len(ids), chunk):
        d = gql(TARGETS, {"ids": ids[i:i + chunk]})
        for t in ((d.get("data") or {}).get("targets") or []):
            if t:
                rows.append(t)
        sys.stderr.write("fetched %d/%d\n" % (min(i + chunk, len(ids)), len(ids)))
    return rows


def atlas_mentions(name):
    """Case-insensitive whole-token search of nodes + bibliography for a drug name."""
    pat = re.escape(name)
    n = subprocess.run(["grep", "-rilw", "--include=*.yaml", pat, NODES],
                       capture_output=True, text=True).stdout.strip()
    n = len([x for x in n.split("\n") if x])
    b = subprocess.run(["grep", "-icw", pat, BIB], capture_output=True, text=True).stdout.strip()
    return n + int(b or 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--genes", default=None)
    ap.add_argument("--max-genes", type=int, default=0)
    a = ap.parse_args()

    if a.genes:
        symbols = [l.strip() for l in open(a.genes) if l.strip()]
    else:
        sys.stderr.write("no --genes file given; pass the harvested symbol list\n")
        return 2
    if a.max_genes:
        symbols = symbols[:a.max_genes]

    ids = resolve(symbols)
    sys.stderr.write("resolved %d of %d symbols to Ensembl IDs\n" % (len(ids), len(symbols)))
    rows = fetch(sorted(set(ids.values())))

    drugged, undrugged, records = [], [], []
    for t in rows:
        sym = t["approvedSymbol"]
        cand = (t.get("drugAndClinicalCandidates") or {})
        n = cand.get("count") or 0
        tract = {("%s:%s" % (x["modality"], x["label"])): x["value"] for x in (t.get("tractability") or [])}
        approved_sm = tract.get("SM:Approved Drug") or tract.get("AB:Approved Drug") or tract.get("PR:Approved Drug")
        drugs = []
        for r in (cand.get("rows") or []):
            d = r.get("drug") or {}
            acts = {m.get("actionType") or "" for m in
                    ((d.get("mechanismsOfAction") or {}).get("rows") or [])}
            moa = "; ".join(sorted(acts - {""}))
            drugs.append({"name": d.get("name"), "type": d.get("drugType"),
                          "phase": d.get("maximumClinicalStage"), "action": moa})
        rec = {"symbol": sym, "ensembl": t["id"], "n_drugs": n,
               "approved_drug_tractable": bool(approved_sm), "drugs": drugs}
        records.append(rec)
        (drugged if n else undrugged).append(sym)

    # which drug names has the atlas never written down?
    seen, novel = {}, []
    for rec in records:
        for d in rec["drugs"]:
            nm = d["name"]
            if not nm or len(nm) < 4:
                continue
            if nm not in seen:
                seen[nm] = atlas_mentions(nm)
            if seen[nm] == 0:
                novel.append({"drug": nm, "target": rec["symbol"], "type": d["type"],
                              "phase": d["phase"], "action": d["action"]})

    os.makedirs(OUT, exist_ok=True)
    json.dump({"records": records, "novel_drugs": novel},
              open(os.path.join(OUT, "druggability_sweep.json"), "w"), indent=1)

    print("=" * 96)
    print("ATLAS TARGETS RESOLVED: %d   WITH >=1 DRUG OR CLINICAL CANDIDATE: %d   WITHOUT: %d"
          % (len(records), len(drugged), len(undrugged)))
    print("=" * 96)
    print("\nTARGETS WITH NO MOLECULE AT ALL (the 'no molecule exists' class - searching does not fix these):")
    print("  " + ", ".join(sorted(undrugged)))
    def ph(x):
        v = x.get("phase")
        try:
            return float(str(v).strip() or 0)
        except ValueError:
            return {"APPROVAL": 4.0, "APPROVED": 4.0, "PHASE_4": 4.0, "PHASE_3": 3.0,
                    "PHASE_2": 2.0, "PHASE_1": 1.0, "PRECLINICAL": 0.5,
                    "EARLY_PHASE_1": 0.5}.get(str(v).strip().upper(), 0.0)

    byt = {}
    for x in novel:
        byt.setdefault(x["target"], []).append(x)
    print("\n" + "=" * 96)
    print("DRUGS AGAINST ATLAS TARGETS THAT THIS FILE HAS NEVER MENTIONED (%d drug-target pairs, %d targets)"
          % (len(novel), len(byt)))
    print("=" * 96)
    for sym in sorted(byt, key=lambda s: (-max([ph(x) for x in byt[s]] or [0]), -len(byt[s]))):
        ds = byt[sym]
        appr = [d for d in ds if ph(d) >= 4]
        print("\n%-10s  %d never-mentioned agents   (approved: %d)" % (sym, len(ds), len(appr)))
        for d in sorted(ds, key=lambda z: -ph(z))[:12]:
            print("     %-9s %-34s %-16s %s" % (str(d["phase"])[:9], (d["drug"] or "")[:34],
                                                 (d["type"] or "")[:16], d["action"][:34]))
    print("\nwrote %s" % os.path.join(OUT, "druggability_sweep.json"))
    print("\nA hit is a molecule that engages a protein this atlas nominated. It is NOT evidence of a")
    print("height effect. Its value is separating 'no molecule exists' from 'never considered'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
