#!/usr/bin/env python3
"""
height_genetics.py - the arbiter the atlas otherwise cannot reach.

WHY THIS IS THE RIGHT GROUND TRUTH
----------------------------------
`target_screen.py` predicts a direction on height by multiplying signs along a graph
path. Six of its seven surviving rows bottom out at grade C - one animal study at the
weakest link. Meanwhile the flow model cannot score adult height at all, because
`growth_velocity_longitudinal` is a sink in the graph (45 edges in, 0 out): a predicted
velocity gain and a predicted adult-height gain are indistinguishable to it.

Human genetics answers both problems at once. It is a lifetime, whole-organism,
population-scale perturbation experiment on every gene, already run, in the species of
interest - and its readout, attained stature, INTEGRATES velocity and duration by
construction. A gene whose perturbation makes people taller has already answered the
question the atlas is structurally unable to ask.

WHAT AN ASSOCIATION IS AND IS NOT
---------------------------------
An Open Targets association score is a link between a gene and a phenotype. It is NOT an
effect direction. "TGFBR1 - proportionate tall stature (0.27)" says the gene is
implicated in tall stature; it does NOT say loss of function causes it, and it does not
give an effect size in centimetres. Both must be read from the primary, and until they
are, any candidate resting on such a row is UNCONFIRMED. This script deliberately emits
the raw phenotype strings and scores rather than a derived direction, so that nothing
downstream can mistake one for the other.

Two further limits worth stating:
  - A gene can carry BOTH tall and short associations and this is usually correct rather
    than contradictory - FGFR3 gain of function causes achondroplasia while loss of
    function causes CATSHL tall stature. Direction is allele-specific, not gene-specific.
  - Absence of a stature association is weak evidence. It is dominated by what has been
    studied, and rare-disease phenotype curation is far from complete.

Usage:
  python3 atlas/tools/height_genetics.py
"""
from __future__ import annotations
import json, os, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SCREEN = os.path.join(ROOT, "query", "target_screen", "compounds.json")
OUT = os.path.join(ROOT, "query", "target_screen", "height_genetics.json")
API = "https://api.platform.opentargets.org/api/v4/graphql"

SEARCH = 'query($q:String!){search(queryString:$q,entityNames:["target"]){hits{id name}}}'
ASSOC = ('query($id:String!){target(ensemblId:$id){approvedSymbol '
         'associatedDiseases(page:{index:0,size:250}){rows{score disease{name}}}}}')

TALL = ("tall stature", "overgrowth", "gigantism", "macrosomia", "marfan")
SHORT = ("short stature", "dwarf", "growth retardation", "brachyolmia",
         "achondroplasia", "hypochondroplasia")
GRADE_ORDER = ["A", "B", "C", "D", "E", "speculative", "X"]


def gql(query, variables, tries=4):
    for k in range(tries):
        try:
            req = urllib.request.Request(
                API, data=json.dumps({"query": query, "variables": variables}).encode(),
                headers={"Content-Type": "application/json"})
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception:
            if k == tries - 1:
                raise
            time.sleep(2 * (k + 1))


def main():
    rows = json.load(open(SCREEN))
    targets = sorted({t for r in rows if r["helps"] and r["expressed_in_human_gp"]
                      and GRADE_ORDER.index(r["best_grade"]) <= 3
                      for t in r["targets"]})
    out = {}
    for i, sym in enumerate(targets):
        try:
            hits = gql(SEARCH, {"q": sym})["data"]["search"]["hits"]
            eid = next((h["id"] for h in hits if h["name"].upper() == sym.upper()), None)
            if not eid:
                out[sym] = {"resolved": False, "reason": "no exact symbol match"}
                print(f"{i+1}/{len(targets)} {sym}: UNRESOLVED", flush=True)
                continue
            d = gql(ASSOC, {"id": eid})["data"]["target"]
            h = [(x["disease"]["name"], x["score"])
                 for x in d["associatedDiseases"]["rows"]]
            out[sym] = {
                "resolved": True, "symbol": d["approvedSymbol"], "ensembl": eid,
                "tall": sorted([x for x in h if any(k in x[0].lower() for k in TALL)],
                               key=lambda z: -z[1]),
                "short": sorted([x for x in h if any(k in x[0].lower() for k in SHORT)],
                                key=lambda z: -z[1])}
            print(f"{i+1}/{len(targets)} {sym}: tall={len(out[sym]['tall'])} "
                  f"short={len(out[sym]['short'])}", flush=True)
        except Exception as ex:
            out[sym] = {"resolved": False, "reason": type(ex).__name__}
            print(f"{i+1}/{len(targets)} {sym}: ERR {type(ex).__name__}", flush=True)
        time.sleep(0.4)

    meta = {
        "source": "Open Targets Platform v4 GraphQL",
        "n_targets": len(targets),
        "n_resolved": sum(1 for v in out.values() if v.get("resolved")),
        "WARNING": "association scores are NOT effect directions. A tall- or short-stature "
                   "association says the gene is implicated in that phenotype, not that "
                   "loss of function causes it, and gives no effect size. Direction and "
                   "magnitude must be read from the primary; until then any candidate "
                   "resting on one of these rows is UNCONFIRMED.",
        "note": "a gene carrying BOTH tall and short associations is usually correct, not "
                "contradictory - FGFR3 gain of function causes achondroplasia while loss "
                "of function causes CATSHL tall stature. Direction is allele-specific.",
    }
    json.dump({"meta": meta, "targets": out}, open(OUT, "w"), indent=1)
    print(f"\nDONE {meta['n_resolved']}/{meta['n_targets']} resolved -> {OUT}")

    print("\ntargets with a stature association:")
    for s, v in sorted(out.items()):
        if not v.get("resolved") or not (v["tall"] or v["short"]):
            continue
        t = ", ".join(f"{a}({b:.2f})" for a, b in v["tall"][:2]) or "-"
        sh = ", ".join(f"{a}({b:.2f})" for a, b in v["short"][:2]) or "-"
        print(f"  {s:9s} TALL: {t[:42]:42s} SHORT: {sh[:44]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
