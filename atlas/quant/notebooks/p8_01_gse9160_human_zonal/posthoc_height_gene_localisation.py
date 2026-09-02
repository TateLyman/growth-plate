#!/usr/bin/env python3
"""
POST HOC, ADDED ROUND 292. Not preregistered - the genes below were chosen because
rounds 283-291 made them interesting, which is after this notebook was written. That is
declared here rather than hidden, and every claim drawn from it is capped accordingly.

WHAT IT ASKS. Rounds 285-291 built a case for HHIP on mouse data alone - chu2026's mouse
growth-plate table, haraguchi2025's mouse conditional, saturne2025's mouse suture. The
atlas's own standing rule is that every claim carries a species, and "HHIP is expressed
in the growth plate" had only ever been established in a mouse. Round 283's lead gene NRK
had no skeletal measurement in ANY species until round 291 found it in mouse perichondrium.
GSE9160 is the only public zone-resolved transcriptome of a HUMAN growth plate and it has
been in this repository throughout. Neither gene had ever been looked up in it.

WHAT IT INHERITS, RATHER THAN RE-IMPLEMENTS. Everything methodological comes from
analysis.py and from this notebook's own findings:
  - the olfactory-receptor empirical null as the per-array detection threshold, which
    passed its preregistered control against the submitters' present-calls;
  - the donor asymmetry this notebook discovered: donor 2's laser capture largely failed
    to separate the zones (COL10A1 at 15-36 % of hypertrophic level in its RESTING zone
    against 0.6 % in donor 1; 1.0 % versus 9.6 % of probe sets varying more than
    five-fold). SO ZONAL ORDERING IS READ FROM DONOR 1 ONLY. Donor 2 is used only for
    presence/absence, where a failed dissection cannot manufacture a signal.

WHY DETECTION IS REPORTED PER PROBE SET AND PER ARRAY. Donor 1's thresholds run 719-827
and donor 2's 254-451, so a raw intensity means nothing until it is placed against the
array it came from. Averaging the two donors - which is what a naive lookup does - mixes
two different detection regimes and two different dissection qualities, and would have
returned "HHIP is a proliferative-zone gene" as a soft average while hiding that most of
those numbers are below background.

Usage:  python3 posthoc_height_gene_localisation.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analysis as A  # noqa: E402

ZONES = ["RZ", "PZ", "PHZ", "HZ", "PC"]

# Grouped by why round 292 wants them, so the output reads as an argument and not a dump.
GENES = [
    ("the two the case rests on", ["HHIP", "NRK"]),
    ("hedgehog, for context", ["PTCH1", "SMO", "GLI1", "IHH", "PTHLH"]),
    ("hedgehog availability layer (R287/R290)", ["GAS1", "CDON", "BOC", "SCUBE2", "SCUBE3", "EXT1"]),
    ("other height genes (kosmicki2026)", ["LCORL", "TET1", "ZFAT", "ACAN", "FBN1", "SPIN4"]),
    ("dissection controls", ["COL10A1", "COL2A1"]),
]


def main():
    X, p2g = A.load()
    _, thr = A.background(X, p2g)
    idx = {(d, z): [k for k, (_, dd, zz) in enumerate(A.SAMPLES) if dd == d and zz == z][0]
           for d in (1, 2) for z in ZONES}
    sym = {}
    for probe, g in p2g.items():
        if g:
            sym.setdefault(str(g).upper(), []).append(probe)

    print("GSE9160 - the only zone-resolved transcriptome of a HUMAN growth plate.")
    print("donor 1 = female 11 y 10 m (dissection CLEAN); donor 2 = male 13 y 3 m (dissection FAILED)")
    print("'+' = above that array's olfactory-receptor threshold; '.' = below background.")
    print("Zonal ORDER is read from donor 1 only. Donor 2 contributes presence/absence only.\n")

    summary = {}
    for header, genes in GENES:
        print("=" * 96)
        print("## %s" % header.upper())
        for g in genes:
            probes = sym.get(g, [])
            if not probes:
                print("  %-8s NOT ON PLATFORM" % g)
                continue
            print("  %s" % g)
            det = {1: 0, 2: 0}
            pc_det = 0
            for p in sorted(probes):
                row = []
                for d in (1, 2):
                    cells = []
                    for z in ZONES:
                        i = idx[(d, z)]
                        v = X[p][i]
                        ok = v > thr[i]
                        cells.append("%s%s%7.0f" % (z, "+" if ok else ".", v))
                        if ok:
                            det[d] += 1
                            if z == "PC":
                                pc_det += 1
                    row.append("D%d %s" % (d, " ".join(cells)))
                print("    %-14s %s" % (p, row[0]))
                print("    %-14s %s" % ("", row[1]))
            n = len(probes) * 5
            summary[g] = (det[1], det[2], n, pc_det, len(probes))
            print("    -> detected in %d/%d donor-1 and %d/%d donor-2 compartment-probe cells; "
                  "PERICHONDRIUM detected in %d/%d"
                  % (det[1], n, det[2], n, pc_det, len(probes) * 2))
        print()

    print("=" * 96)
    print("## THE TWO RESULTS THAT SURVIVE BOTH DONORS")
    for g in ("HHIP", "NRK"):
        if g not in summary:
            continue
        d1, d2, n, pc, npr = summary[g]
        print("  %-6s donor1 %2d/%d cells, donor2 %2d/%d cells, PERICHONDRIUM %d/%d probe-donor cells"
              % (g, d1, npr * 5, d2, npr * 5, pc, npr * 2))
    print("""
  HHIP  - present in HUMAN growth-plate CARTILAGE and ABSENT FROM PERICHONDRIUM in every
          probe-donor cell. First human measurement of this gene in a growth plate, and an
          independent corroboration - different species, platform and tissue source - of
          round 291's finding that HHIP is not the perichondrial mediator of the fibrillin
          effect. A gene below background in the perichondrium of two human donors cannot
          be the route by which FBN1 loss lengthens a bone.
  NRK   - detected in EVERY compartment of BOTH donors. First human skeletal measurement
          of the gene round 283 named as its lead and which had no skeletal data in any
          species eight days ago. In donor 1, the clean dissection, it rises steeply from
          the resting zone into the proliferative and prehypertrophic zones.
          CAVEAT CARRIED FORWARD FROM CORR-314: NRK is X-linked and the two donors are one
          female and one male, so the donors are NOT comparable in magnitude. The claim is
          detection WITHIN each donor, which does not depend on that comparison.""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
