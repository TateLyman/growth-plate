#!/usr/bin/env python3
"""
ROUND 299 - the INDIRECT sweep. Round 298 asked which drugs BIND our targets and found
202 of 298 undruggable. This asks the different question: which chemicals MOVE a target
by ANY route - transcription, upstream signalling, cofactor supply, off-target - without
binding it at all.

WHY A NEW SOURCE. Open Targets indexes direct target engagement, so it is structurally
blind to indirect action and will keep returning "no molecule" for exactly the genes this
atlas leads with. The database that curates indirect chemical-gene action is CTD (the
Comparative Toxicogenomics Database), whose statements are of the form "chemical X results
in increased/decreased expression of gene Y". CTD's own batch API is behind a human
verification captcha and cannot be queried computationally from here.
ROUTE AROUND IT: Harmonizome (maayanlab) re-serves CTD Gene-Chemical Interactions as a
gene-centric REST endpoint with no key and no captcha, alongside PerturbAtlas, which gives
GENETIC perturbations (knockdown/knockout/overexpression of OTHER genes) that move the
target - the upstream-node route to an undruggable protein.

    https://maayanlab.cloud/Harmonizome/api/1.0/gene/<SYMBOL>?showAssociations=true

WHAT COMES BACK, per target: every curated chemical that changes its expression, plus every
genetic perturbation that does. A hit is a candidate INDIRECT handle. It is not evidence of
a height effect and the endpoint does not carry direction, which has to be recovered from
the primary record before any hit is used.

STATUS: method established and validated on HHIP (3 chemicals, 1071 perturbation signatures
of all kinds). The full sweep over atlas/data/round298/undrugged_targets.txt is the next run.

Usage:  python3 atlas/tools/round299_indirect_perturbagen_sweep.py --targets FILE [--limit N]
"""
import argparse
import collections
import json
import os
import re
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "round299")
API = "https://maayanlab.cloud/Harmonizome/api/1.0/gene/%s?showAssociations=true"


def fetch(sym, tries=3):
    for i in range(tries):
        try:
            r = urllib.request.Request(API % sym, headers={"User-Agent": "growth-atlas/1.0"})
            return json.loads(urllib.request.urlopen(r, timeout=90).read())
        except Exception:
            if i == tries - 1:
                return None
            time.sleep(2 ** i)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--targets", required=True)
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    syms = [l.strip() for l in open(a.targets) if l.strip()]
    if a.limit:
        syms = syms[:a.limit]

    os.makedirs(OUT, exist_ok=True)
    res, chem_count = {}, collections.Counter()
    for i, s in enumerate(syms, 1):
        d = fetch(s)
        if not d:
            continue
        assoc = d.get("associations") or []
        chems = sorted({re.sub(r"/CTD Gene-Chemical Interactions$", "", x["geneSet"]["name"])
                        for x in assoc
                        if x["geneSet"]["name"].endswith("CTD Gene-Chemical Interactions")})
        perts = sorted({x["geneSet"]["name"].split("/")[0] for x in assoc
                        if "PerturbAtlas" in x["geneSet"]["name"]})
        res[s] = {"chemicals": chems, "n_genetic_perturbations": len(perts)}
        for c in chems:
            chem_count[c] += 1
        sys.stderr.write("[%d/%d] %-10s chem=%-3d pert=%d\n" % (i, len(syms), s, len(chems), len(perts)))

    json.dump(res, open(os.path.join(OUT, "indirect_perturbagens.json"), "w"), indent=1)

    print("=" * 84)
    print("INDIRECT CHEMICAL HANDLES ON UNDRUGGABLE ATLAS TARGETS")
    print("=" * 84)
    withchem = {k: v for k, v in res.items() if v["chemicals"]}
    print("targets queried: %d | with >=1 curated chemical: %d" % (len(res), len(withchem)))
    print("\nCHEMICALS RECURRING ACROSS THE MOST TARGETS (a chemical that moves many of our")
    print("undruggable genes is either a broad tool or a genuine upstream node):")
    for c, n in chem_count.most_common(40):
        print("  %-40s %d targets" % (c[:40], n))
    print("\nPER-TARGET:")
    for k in sorted(withchem, key=lambda z: -len(withchem[z]["chemicals"])):
        print("  %-10s %s" % (k, ", ".join(withchem[k]["chemicals"])[:110]))
    print("\nwrote %s" % os.path.join(OUT, "indirect_perturbagens.json"))
    print("\nDIRECTION IS NOT CARRIED BY THIS ENDPOINT. Every hit must be resolved against the")
    print("primary CTD record before use - a chemical that DECREASES an inhibitor and one that")
    print("DECREASES a driver point opposite ways for height.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
