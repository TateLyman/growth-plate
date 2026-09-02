#!/usr/bin/env python3
"""
ROUND 297 - which ACCESSIBLE drugs has this atlas never looked at even once?

CLAUDE.md's conventions say a generic length-endpoint sweep no longer finds anything,
because the vocabulary is large enough that almost every real drug name already appears
somewhere. That is an argument against BLIND sweeps. It is not an argument against
asking the inverse question, which nobody had asked: across 821 nodes and 1,597
references, WHICH ACCESSIBLE AGENTS RETURN ZERO HITS?

Zero coverage is not evidence a drug works. It is evidence the atlas has never formed an
opinion - and for an approved, cheap, orally available agent that is a different and more
actionable kind of gap than "no molecule exists", which is where HHIP and the volume axis
both ended up.

Inclusion rule for the list: the agent must be OBTAINABLE - approved somewhere, or
over-the-counter, or a nutritional supplement. Investigational compounds are deliberately
excluded; the atlas already tracks those and they are not what this audit is for.

Usage:  python3 atlas/tools/round297_accessible_drug_coverage_audit.py [--verbose]
"""
import argparse
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NODES = os.path.join(ROOT, "nodes")
BIB = os.path.join(ROOT, "sources", "bibliography.yaml")

DRUGS = {
    "FGFR3 / ERK repurposing": [
        "meclizine", "meclozine", "lovastatin", "rosuvastatin", "simvastatin", "atorvastatin",
        "carbamazepine", "celecoxib"],
    "cGMP - the CNP effector, reachable by other routes": [
        "sildenafil", "tadalafil", "vardenafil", "riociguat", "vericiguat", "cinaciguat",
        "nitrate", "L-arginine", "citrulline"],
    "endocrine, accessible": [
        "oxandrolone", "testosterone", "mecasermin", "raloxifene", "leuprolide", "triptorelin"],
    "metabolic and common": [
        "metformin", "everolimus", "lithium", "acetazolamide", "thiazide", "hydrochlorothiazide",
        "amiloride", "furosemide", "spironolactone", "allopurinol", "colchicine"],
    "immune / cytokine - inflammation suppresses growth": [
        "tocilizumab", "anakinra", "etanercept", "adalimumab", "canakinumab"],
    "nutrient / over-the-counter": [
        "vitamin K", "creatine", "strontium", "glucosamine", "chondroitin", "collagen peptide",
        "boron", "alpha-ketoglutarate"],
    "cardiovascular / other": [
        "propranolol", "nifedipine", "verapamil", "pentoxifylline", "losartan", "irbesartan",
        "semaglutide", "liraglutide", "dapagliflozin", "empagliflozin", "melatonin",
        "dehydroepiandrosterone"],
}

# Written down BEFORE the audit was run, so the ranking is not post-hoc rationalisation of
# whatever happened to come back empty. Which term of HEIGHT = integral of lambda*N*A*h_term
# could the agent plausibly move, and is that term already served by the stack?
RATIONALE = {
    "metformin": "PERIOD. Slows bone-age advance in insulin-resistant girls - the one term an "
                 "aromatase inhibitor also serves, so it is a possible ADDITION only if insulin "
                 "resistance is present. Never checked.",
    "celecoxib": "COST, not lever. NSAIDs suppress longitudinal growth; if taken, may be "
                 "subtracting. Never checked.",
    "L-arginine": "cGMP by a SECOND route (NO/sGC) rather than NPR-B. The CNP arm's effector "
                  "reached without competing for the receptor. Never checked.",
    "citrulline": "as L-arginine, better oral bioavailability. Never checked.",
    "anakinra": "IL-1 blockade. Inflammatory tone suppresses chondrocyte proliferation. Never checked.",
    "tocilizumab": "IL-6 blockade produces catch-up growth in inflammatory arthritis. Thin coverage.",
    "thiazide": "mild hyponatremia lowers plasma osmolality - the only systemic route to the "
                "volume axis. Never checked.",
    "glucosamine": "sulfated amino sugar - substrate for the fixed charge density that generates "
                   "cartilage osmotic pressure, and a sulfate donor. Never checked.",
}


def hits(term):
    n = subprocess.run(["grep", "-ril", "--include=*.yaml", term, NODES],
                       capture_output=True, text=True).stdout.strip()
    n = len([x for x in n.split("\n") if x])
    b = subprocess.run(["grep", "-ic", term, BIB], capture_output=True, text=True).stdout.strip()
    return n, int(b or 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()
    never, thin = [], []
    for cat, ds in DRUGS.items():
        print("=" * 78)
        print("## %s" % cat)
        for d in ds:
            n, b = hits(d)
            tag = ""
            if n == 0 and b == 0:
                tag = "   <-- NEVER"; never.append(d)
            elif n <= 1 and b <= 1:
                tag = "   (thin)"; thin.append(d)
            if a.verbose or tag:
                print("  %-24s nodes=%-3d bib=%-3d%s" % (d, n, b, tag))
    print()
    print("ZERO COVERAGE ANYWHERE (%d): %s" % (len(never), ", ".join(sorted(set(never)))))
    print("THIN (%d): %s" % (len(thin), ", ".join(sorted(set(thin)))))
    print()
    print("PRE-REGISTERED RATIONALE for the ones worth a round - written before the audit ran:")
    for k, v in RATIONALE.items():
        print("  %-14s %s" % (k, v))
    print()
    print("A zero here is a statement about THIS FILE, not about the literature. The point of the")
    print("audit is to distinguish 'no molecule exists' - where HHIP and the volume axis ended up -")
    print("from 'an obtainable molecule exists and nobody here ever formed an opinion about it'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
