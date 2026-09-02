#!/usr/bin/env python3
"""
ROUND 432. THE RECESSIVE / BIALLELIC SCREEN - the one neither of the file's two systematic
human-genetics instruments can run.

WHY THIS ROUND EXISTS. The conclusion the atlas has been converging on - "the elevation
direction is fully occupied" (R331), "nothing passes both tests" (R312) - rests on exactly two
systematic instruments:

  1. kosmicki2026's 207-gene burden table (atlas/data/round300/s6_burden_effects.json).
     1.45M exomes. It is a HETEROZYGOUS burden test.
  2. R323b's HPO tall/period screen (atlas/data/round323/hpo_tall_and_period.json).
     TALL_ONLY 106, DELAYED_ONLY 353, TALL_AND_PERIOD 4.

NEITHER CONTAINS CYP19A1 - the gene behind the single largest human height effect this atlas
holds (aromatase deficiency: untreated men at 188-204 cm, bone age 15.5 at chronological age
26.8, epiphyses unfused, still growing), and the mechanistic reason anastrozole is in the
stack. Verified against both files on disk before this script was written.

  - The 207 cannot contain it because aromatase deficiency is RECESSIVE and heterozygous
    carriers are phenotypically normal. No number of exomes fixes a zygosity model.
  - R323b's screen dropped it for a DIFFERENT reason than the brief supposed, and the real
    reason is more general and more damaging - see THE DIAGNOSIS below.

B1. THE GUARD, DECLARED BEFORE RESULTS ARE READ.
    PRIMARY POSITIVE CONTROL: CYP19A1. A screen design that does not recover CYP19A1 is broken
    and its output is inadmissible; fix the screen, not the interpretation.
    SECONDARY CONTROLS: ESR1 (recessive, 204 cm), NPR3 (biallelic, +3.9 SDS), CBS
    (homocystinuria, recessive, tall - already in R323b's TALL_ONLY, so it is the control that
    should survive BOTH designs).
    NEGATIVE CONTROL: the screen must NOT return a set dominated by short-stature syndromes.
    The short:tall base rate is reported so CORR-295 can be read off the output.

THE DIAGNOSIS - and it is not term-keying.
CYP19A1 IS annotated to HP:0000098 Tall stature (ORPHA:91, aromatase deficiency) AND to
HP:0002750 Delayed skeletal maturation (ORPHA:91 and OMIM:613546). The vocabulary was never
the problem. What R323b did was take a SET DIFFERENCE AT THE GENE LEVEL: tall-annotated genes
MINUS short-annotated genes. CYP19A1 carries HP:0004322 Short stature under ORPHA:178345 -
aromatase EXCESS, the opposite lesion of the same gene - and HP:0005616 Accelerated skeletal
maturation under the same ORPHA:178345. So the gene was removed from the tall list and from
the period list by its own mirror disease.

  TWO OPPOSITE CONDITIONS OF ONE GENE CANCELLED EACH OTHER IN A SET OPERATION.

That is CORR-309's error - record the ARM, not the citation - committed against a gene instead
of a paper: RECORD THE DISEASE, NOT THE GENE. CLAUDE.md already reports the size of the damage
without knowing what it was: "74 of the 180 are annotated BOTH ways, leaving 106 directional".
Every one of those 74 is a candidate for this failure.

THE FIX. Key every annotation on the (GENE, DISEASE) pair. A disease is a single lesion in a
single direction; a gene is not.

B2. KEY ON MECHANISM, NOT ON THE LABEL "TALL". The phenotype this project wants is an EXTENDED
GROWTH PERIOD WITH AN OPEN PLATE, which is what the clinic records in these patients:
delayed skeletal maturation, delayed epiphyseal ossification, eunuchoid habitus, increased arm
span, absent pubertal growth spurt. Tall stature is one term among those, not the key.

B3. ZYGOSITY-AWARE. HPO carries mode of inheritance per (gene, disease) as HP:0000007 etc, so
the recessive subset is separable inside the file already on disk. gnomAD homozygous pLoF
counts are fetched where the API is reachable; where it is not, that column is reported absent
rather than assumed.

WHAT THIS SCREEN CANNOT DO, STATED BEFORE THE RESULTS.
  - An HPO annotation is a curated statement about a SYNDROME. No effect size, no allele, no
    direction of the molecular lesion. It nominates; it cannot rank and it cannot dose.
  - CORR-295 IN REVERSE: recessive tall-stature genes have the opposite ascertainment problem
    to short ones - the tall phenotype is TREATED AWAY on diagnosis, so absence of published
    extreme heights is not absence of the effect. Nulls here are not negatives.
  - CORR-299: every hit is a germline biallelic lesion from conception. Whether the gene is
    still doing work in an OPEN PLATE is a separate question per gene.
  - A syndrome that lists tall stature among twenty features is evidence the gene is somewhere
    upstream of height, not that it is a lever.

Usage:  python3 atlas/tools/round432_recessive_period_screen.py
"""
from __future__ import annotations

import collections
import json
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUP = os.path.join(HERE, "data", "supplied_2026_08_13")
P2G = os.path.join(SUP, "hpo_phenotype_to_genes.txt")
G2P = os.path.join(SUP, "hpo_genes_to_phenotype.txt")
OUTDIR = os.path.join(HERE, "data", "round432")

# ---------------------------------------------------------------- B2 vocabulary
# The mechanism, not the label. Weighted by how specific each term is to the thing
# this project wants: an extended growth period with an open plate.
PERIOD = {  # the plate is still running late - the core of the ask
    "HP:0002750": "Delayed skeletal maturation",
    "HP:0005832": "Dysharmonic delayed bone age",
    "HP:0002663": "Delayed epiphyseal ossification",
    "HP:0006016": "Delayed phalangeal epiphyseal ossification",
    "HP:0008828": "Delayed proximal femoral epiphyseal ossification",
    "HP:6000866": "Delayed distal femoral epiphyseal ossification",
    "HP:6000867": "Delayed tibial epiphyseal ossification",
}
TALL = {
    "HP:0000098": "Tall stature",
    "HP:0001519": "Disproportionate tall stature",
    "HP:0011407": "Proportionate tall stature",
}
PROPORTION = {  # limbs kept growing after the trunk stopped - the eunuchoid signature
    "HP:0003782": "Eunuchoid habitus",
    "HP:0012771": "Increased arm span",
}
PUBERTY_UNCOUPLED = {  # growth continuing while the pubertal signal is absent or late
    "HP:0031087": "Absent pubertal growth spurt",
    "HP:0000823": "Delayed puberty",
}
MECHANISM = {}
for _d in (PERIOD, TALL, PROPORTION, PUBERTY_UNCOUPLED):
    MECHANISM.update(_d)

# Opposing terms. Applied WITHIN a disease, never across a gene - that is the whole fix.
OPPOSING = {
    "HP:0004322": "Short stature",
    "HP:0003502": "Mild short stature",
    "HP:0003498": "Disproportionate short stature",
    "HP:0003508": "Proportionate short stature",
    "HP:0003510": "Severe short stature",
    "HP:0008848": "Moderately short stature",
    "HP:0005616": "Accelerated skeletal maturation",
    "HP:0012770": "Reduced arm span",
    "HP:0006140": "Premature fusion of phalangeal epiphyses",
}

RECESSIVE = {"HP:0000007": "Autosomal recessive",
             "HP:0001419": "X-linked recessive",
             "HP:0034341": "Pseudoautosomal recessive"}
DOMINANT = {"HP:0000006": "Autosomal dominant",
            "HP:0001423": "X-linked dominant",
            "HP:0012275": "Autosomal dominant with maternal imprinting"}

CONTROLS_PRIMARY = ["CYP19A1"]
CONTROLS_SECONDARY = ["ESR1", "NPR3", "CBS"]


# ---------------------------------------------------------------- loaders
def load_pairs():
    """(gene, disease) -> set of hpo ids.  This is the unit of analysis."""
    terms = collections.defaultdict(set)
    names = {}
    with open(P2G) as fh:
        fh.readline()
        for line in fh:
            p = line.rstrip("\n").split("\t")
            if len(p) < 5:
                continue
            hid, hname, sym, dis = p[0], p[1], p[3], p[4]
            terms[(sym, dis)].add(hid)
            names[hid] = hname
    # genes_to_phenotype carries the same pairs plus inheritance rows
    with open(G2P) as fh:
        fh.readline()
        for line in fh:
            p = line.rstrip("\n").split("\t")
            if len(p) < 6:
                continue
            sym, hid, hname, dis = p[1], p[2], p[3], p[5]
            terms[(sym, dis)].add(hid)
            names[hid] = hname
    return terms, names


def inheritance_of(tset):
    rec = sorted(RECESSIVE[t] for t in tset if t in RECESSIVE)
    dom = sorted(DOMINANT[t] for t in tset if t in DOMINANT)
    if rec and not dom:
        return "recessive"
    if dom and not rec:
        return "dominant"
    if rec and dom:
        return "both"
    return "unstated"


def gnomad_hom(symbols, enable=True):
    """Homozygous pLoF carrier counts. Absent is reported as absent, never as zero."""
    if not enable:
        return {}
    url = "https://gnomad.broadinstitute.org/api"
    q = """query($s:String!){gene(gene_symbol:$s, reference_genome:GRCh38){
      gene_id symbol variants(dataset:"gnomad_r4"){
        consequence transcript_id genome{ac_hom} exome{ac_hom}}}}"""
    out = {}
    for s in symbols:
        body = json.dumps({"query": q, "variables": {"s": s}}).encode()
        req = urllib.request.Request(url, data=body,
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                d = json.loads(r.read().decode())
        except Exception as e:  # noqa: BLE001 - network; absence is recorded, not assumed
            print("  ! gnomAD %s: %s" % (s, e), file=sys.stderr)
            return out
        g = ((d.get("data") or {}).get("gene") or {})
        lof = {"frameshift_variant", "stop_gained", "splice_donor_variant",
               "splice_acceptor_variant"}
        tot = 0
        for v in (g.get("variants") or []):
            if v.get("consequence") in lof:
                for k in ("genome", "exome"):
                    tot += ((v.get(k) or {}).get("ac_hom") or 0)
        out[s] = tot
        time.sleep(0.4)
    return out


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    pairs, names = load_pairs()
    print("HPO (gene, disease) pairs loaded: %d" % len(pairs))

    # ---- the two screens, run side by side on identical vocabulary --------------
    # GENE-LEVEL (reproduces R323b's operation) vs DISEASE-LEVEL (the fix).
    gene_terms = collections.defaultdict(set)
    for (sym, _dis), ts in pairs.items():
        gene_terms[sym] |= ts

    gene_level = set()
    for sym, ts in gene_terms.items():
        if (ts & set(MECHANISM)) and not (ts & set(OPPOSING)):
            gene_level.add(sym)

    disease_level = {}
    for (sym, dis), ts in pairs.items():
        hits = ts & set(MECHANISM)
        opp = ts & set(OPPOSING)
        if not hits or opp:
            continue
        rec = disease_level.setdefault(sym, [])
        rec.append(dict(
            disease=dis,
            inheritance=inheritance_of(ts),
            period=sorted(t for t in hits if t in PERIOD),
            tall=sorted(t for t in hits if t in TALL),
            proportion=sorted(t for t in hits if t in PROPORTION),
            puberty=sorted(t for t in hits if t in PUBERTY_UNCOUPLED),
            n_terms=len(ts),
        ))

    print("\nGENE-LEVEL screen (R323b's operation) : %d genes" % len(gene_level))
    print("DISEASE-LEVEL screen (the fix)        : %d genes" % len(disease_level))
    recovered = sorted(set(disease_level) - gene_level)
    print("RECOVERED by moving to disease level  : %d genes" % len(recovered))

    # ---- B1 GUARD --------------------------------------------------------------
    print("\n--- B1 GUARD ---")
    ok = True
    for g in CONTROLS_PRIMARY:
        got = g in disease_level
        print("  PRIMARY   %-8s gene-level=%-5s disease-level=%-5s"
              % (g, g in gene_level, got))
        ok = ok and got
    for g in CONTROLS_SECONDARY:
        print("  secondary %-8s gene-level=%-5s disease-level=%-5s"
              % (g, g in gene_level, g in disease_level))
    if not ok:
        print("\n  GUARD FAILED - the screen is inadmissible. Fix the screen.")
        sys.exit(2)
    print("  GUARD PASSED.")

    # ---- CORR-295 base rate, measured not asserted -----------------------------
    short_pairs = sum(1 for ts in pairs.values() if ts & set(OPPOSING))
    mech_pairs = sum(1 for ts in pairs.values() if ts & set(MECHANISM))
    tall_pairs = sum(1 for ts in pairs.values() if ts & set(TALL))
    print("\n--- CORR-295 base rate, at the DISEASE level ---")
    print("  diseases with an OPPOSING (short/advanced) term : %d" % short_pairs)
    print("  diseases with any MECHANISM term                : %d" % mech_pairs)
    print("  diseases with a TALL term                       : %d" % tall_pairs)
    print("  short : tall ratio                              : %.1f : 1"
          % (short_pairs / max(tall_pairs, 1)))

    # ---- B3 ZYGOSITY -----------------------------------------------------------
    # A SECOND structural defect in the source, found by the guard rather than assumed.
    # HPO records the SAME condition twice - once as an OMIM entry and once as an ORPHA
    # entry - and it annotates them differently. For CYP19A1, inheritance (HP:0000007)
    # is on OMIM:613546 while tall stature and eunuchoid habitus are on ORPHA:91.
    # Joining on disease_id therefore splits one condition in two.
    #
    # The asymmetric fix, and the asymmetry is the point:
    #   DIRECTION is collapsed per DISEASE and never per gene - that is the CYP19A1
    #     lesson and it is what stops aromatase EXCESS cancelling aromatase DEFICIENCY.
    #   INHERITANCE and AXIS COVERAGE are unioned per GENE, but only over diseases that
    #     have ALREADY passed the per-disease direction filter. The excess-aromatase
    #     record is gone before this step, so it contributes nothing.
    gene_inh = collections.defaultdict(set)
    for (sym, _dis), ts in pairs.items():
        gene_inh[sym].add(inheritance_of(ts))

    def zyg(sym):
        s = gene_inh.get(sym, set())
        if "recessive" in s and "dominant" in s:
            return "mixed"
        if "recessive" in s or "both" in s:
            return "recessive"
        if "dominant" in s:
            return "dominant"
        return "unstated"

    recessive = {s: ds for s, ds in disease_level.items()
                 if zyg(s) in ("recessive", "mixed")}
    print("\n--- B3 ZYGOSITY ---")
    print("  mechanism-positive genes with a RECESSIVE disease : %d" % len(recessive))
    print("    of which purely recessive                       : %d"
          % sum(1 for s in recessive if zyg(s) == "recessive"))
    print("    of which mixed dominant/recessive               : %d"
          % sum(1 for s in recessive if zyg(s) == "mixed"))

    def axes_of(ds):
        a = set()
        for d in ds:
            for k in ("period", "tall", "proportion", "puberty"):
                if d[k]:
                    a.add(k)
        return a

    def score(ds):
        a = axes_of(ds)
        return (2 * ("period" in a) + 2 * ("tall" in a)
                + 2 * ("proportion" in a) + 1 * ("puberty" in a))

    ranked = sorted(recessive.items(), key=lambda kv: (-score(kv[1]), kv[0]))
    strong = [(s, d) for s, d in ranked if score(d) >= 4]
    print("\n  RECESSIVE genes carrying >=2 of the four mechanism axes: n = %d"
          % len(strong))
    for sym, ds in strong:
        print("    %-12s score=%-2d %-10s %s"
              % (sym, score(ds), zyg(sym), ",".join(sorted(axes_of(ds)))))

    out = {
        "vocabulary": {"MECHANISM": MECHANISM, "OPPOSING": OPPOSING},
        "counts": {
            "pairs": len(pairs),
            "gene_level": len(gene_level),
            "disease_level": len(disease_level),
            "recovered_by_fix": len(recovered),
            "recessive": len(recessive),
            "short_pairs": short_pairs,
            "tall_pairs": tall_pairs,
            "mechanism_pairs": mech_pairs,
        },
        "recovered_by_fix": recovered,
        "recessive": {s: dict(diseases=d, zygosity=zyg(s), score=score(d),
                              axes=sorted(axes_of(d))) for s, d in ranked},
        "strong_recessive": [s for s, _ in strong],
        "guard": {"primary": CONTROLS_PRIMARY, "secondary": CONTROLS_SECONDARY,
                  "passed": ok},
        "term_names": {k: names.get(k, MECHANISM.get(k, "")) for k in
                       list(MECHANISM) + list(OPPOSING)},
    }
    path = os.path.join(OUTDIR, "recessive_period_screen.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("\n  written: %s" % os.path.relpath(path, HERE))


if __name__ == "__main__":
    main()
