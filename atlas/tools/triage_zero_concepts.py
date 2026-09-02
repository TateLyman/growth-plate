#!/usr/bin/env python3
"""
triage_zero_concepts.py
=======================
A ZERO list is not actionable. CORR-295 states the rule that cost this project several
rounds: an enumeration with NO SIGN and NO MAGNITUDE is a list, not a result. The atlas's
own top-ranked gene (ZFAT) sat unused for rounds because it arrived as a name.

So this tool takes the output of concept_coverage_map.py and, for every gene symbol it can
find in a concept's aliases, attaches the three things that turn a name into a decision:

  1. SIGN AND MAGNITUDE - the signed burden effect in centimetres from kosmicki2026's 207
     (atlas/data/round300/s6_per_gene_direction.json). Positive = loss LENGTHENS, so the
     therapeutic direction is INHIBIT. Negative = load-bearing, so an inhibitor is a
     CONTRAINDICATION and the direction is to RAISE.
  2. IS IT IN THE TISSUE - CORR-327's receiver test, run against the purity-corrected
     postnatal human growth plate (R344's male-only split, R411's recalibration, where
     COL2A1 = 7.65 and ACAN = 1.96 is the cartilage benchmark). A target absent from the
     tissue is disqualifier (1) under R302 - the same test that killed losartan (AGTR1
     0.03), sacubitril (MME 0.17) and romosozumab (SOST 0.35).
  3. IS THERE CHEMICAL MATTER - left to the ChEMBL sweep, but the column is emitted so the
     ranking has a slot for it. CORR-347: n_molecules and max_phase are different questions.

WHAT IT DELIBERATELY DOES NOT DO
    It does not decide. A high score here means "worth a round", not "add it". Step 0
    (does an arm already in the stack move this term?) and CORR-325 (what does losing BOTH
    copies do?) are judgement calls that stay with the reader.

CAVEATS THAT TRAVEL WITH EVERY ROW
    * A purity ratio measures ENRICHMENT, not PRESENCE (CORR-351). ESR1 reads 0.16 while
      64% of human growth-plate chondrocytes carry the protein. A low ratio is a hypothesis
      about a transcript's cellular origin, not an absence.
    * Absence from the 207 is not absence of effect (CORR-310) - it is absence from one
      heterozygous burden test, which by construction cannot contain a recessive gene
      (CORR-358).
    * Gene symbols are extracted from concept aliases, so a concept whose aliases are prose
      gets no annotation. That is a miss, not a null.

USAGE
    python3 atlas/tools/concept_coverage_map.py --json atlas/data/round436/coverage.json
    python3 atlas/tools/triage_zero_concepts.py --coverage atlas/data/round436/coverage.json
    python3 atlas/tools/triage_zero_concepts.py --tier ZERO --tier REF_ONLY --min-cpm 20
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(HERE)
BURDEN = os.path.join(HERE, "data", "round300", "s6_per_gene_direction.json")
CPM = os.path.join(HERE, "data", "round344", "gse288028_human12_cpm.npy")
GEN = os.path.join(HERE, "data", "round344", "gse288028_gene_names.json")
PUR = os.path.join(HERE, "data", "round344", "gse288028_purity_corrected.json")

# R411's recalibrated benchmarks on the male-only split.
ACAN_BENCHMARK = 1.96
COL2A1_BENCHMARK = 7.65
GENEISH = re.compile(r"^[A-Z][A-Z0-9]{1,9}[0-9A-Z]$")


def load_expression():
    """Purity-corrected postnatal human growth plate, male-only split (R411)."""
    cpm = np.load(CPM)
    genes = json.load(open(GEN))
    if isinstance(genes, dict):
        genes = genes.get("genes", genes.get("gene_names"))
    genes = [str(g).upper() for g in genes]
    idx = {g: i for i, g in enumerate(genes)}
    meta = json.load(open(PUR))
    col = meta["col2a1_by_sample"]
    vals = np.array([col[k] for k in col] if isinstance(col, dict) else list(col), float)
    xist = cpm[:, idx["XIST"]]
    male = [i for i in range(cpm.shape[0]) if xist[i] < 10]
    ordered = sorted(male, key=lambda i: -vals[i])
    pure, contam = ordered[:4], ordered[-4:]

    def stat(sym):
        i = idx.get(sym)
        if i is None:
            return None
        p = float(np.median(cpm[pure, i]))
        c = float(np.median(cpm[contam, i]))
        det = int(sum(1 for r in male if cpm[r, i] > 0))
        ratio = p / c if c > 0 else (float("inf") if p > 0 else 0.0)
        return dict(cpm_pure=round(p, 1), cpm_contam=round(c, 1),
                    ratio=(round(ratio, 2) if ratio != float("inf") else None),
                    detected_in=det, n_male=len(male))

    return stat


def load_burden():
    rows = json.load(open(BURDEN))
    return {r["gene"].upper(): r for r in rows}


def symbols_from(row) -> list[str]:
    out = []
    for a in [row["concept"]] + list(row.get("aliases") or []):
        for tok in re.split(r"[^A-Za-z0-9]+", a):
            if GENEISH.match(tok) and len(tok) >= 3:
                out.append(tok.upper())
    seen, uniq = set(), []
    for s in out:
        if s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--coverage", required=True)
    ap.add_argument("--tier", action="append", default=None,
                    help="repeatable; default ZERO and REF_ONLY")
    ap.add_argument("--min-cpm", type=float, default=0.0)
    ap.add_argument("--json")
    args = ap.parse_args()

    tiers = set(args.tier or ["ZERO", "REF_ONLY"])
    cov = json.load(open(args.coverage))
    rows = [r for r in cov["rows"] if r["tier"] in tiers]

    stat = load_expression()
    burden = load_burden()

    out = []
    for r in rows:
        syms = symbols_from(r)
        ann = []
        for s in syms:
            e = stat(s)
            b = burden.get(s)
            if e is None and b is None:
                continue
            ann.append(dict(symbol=s, expression=e,
                            burden_cm=(b or {}).get("any_eff"),
                            burden_p=(b or {}).get("any_p"),
                            burden_cat=(b or {}).get("any_cat"),
                            constrained=(b or {}).get("constrained")))
        best_cm = max((a["burden_cm"] for a in ann if a["burden_cm"] is not None),
                      key=abs, default=None)
        best_e = None
        for a in ann:
            e = a["expression"]
            if e and (best_e is None or (e["cpm_pure"] or 0) > (best_e["cpm_pure"] or 0)):
                best_e = e
        if args.min_cpm and (not best_e or (best_e["cpm_pure"] or 0) < args.min_cpm):
            continue
        out.append(dict(
            concept=r["concept"], domain=r["domain"], tier=r["tier"],
            direction=r.get("direction"), obscure=r.get("obscure"),
            symbols=syms, annotations=ann,
            best_burden_cm=best_cm,
            best_cpm_pure=(best_e or {}).get("cpm_pure"),
            best_ratio=(best_e or {}).get("ratio"),
        ))

    def rank(x):
        cm = abs(x["best_burden_cm"]) if x["best_burden_cm"] is not None else -1
        enr = x["best_ratio"] if x["best_ratio"] is not None else -1
        return (-cm, -(enr or 0), -(x["best_cpm_pure"] or 0))

    out.sort(key=rank)

    print("TRIAGED ZERO/REF_ONLY CONCEPTS")
    print("  tiers        : %s" % ", ".join(sorted(tiers)))
    print("  concepts in  : %d" % len(rows))
    print("  with a gene  : %d" % sum(1 for x in out if x["annotations"]))
    print("  benchmarks   : COL2A1 %.2f, ACAN %.2f (male-only split, R411)\n"
          % (COL2A1_BENCHMARK, ACAN_BENCHMARK))
    print("  %-40s %-14s %8s %9s %7s  %s"
          % ("CONCEPT", "DOMAIN", "cm", "CPM_pure", "ratio", "direction"))
    for x in out[:80]:
        print("  %-40s %-14s %8s %9s %7s  %s" % (
            x["concept"][:40], (x["domain"] or "")[:14],
            "%.2f" % x["best_burden_cm"] if x["best_burden_cm"] is not None else "-",
            "%.1f" % x["best_cpm_pure"] if x["best_cpm_pure"] is not None else "-",
            "%.2f" % x["best_ratio"] if x["best_ratio"] is not None else "-",
            (x.get("direction") or "")[:34]))

    if args.json:
        os.makedirs(os.path.dirname(args.json), exist_ok=True)
        json.dump({"n": len(out), "rows": out}, open(args.json, "w"), indent=1)
        print("\nwritten: %s" % os.path.relpath(args.json, ROOT))


if __name__ == "__main__":
    main()
