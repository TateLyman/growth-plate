#!/usr/bin/env python3
"""
POST HOC, ADDED ROUND 302. Third post-hoc use of this notebook; declared, not hidden.

WHAT IT ASKS, AND WHY IT IS DIFFERENT FROM ROUNDS 292 AND 300. Both of those typed a
HAND-PICKED gene list into this notebook - the genes that happened to be interesting that
round. That is the same failure the atlas keeps repeating in another form: the answer is
bounded by what I thought to ask. This run types in ALL 207 genome-wide-significant human
height genes from kosmicki2026 Table S4, plus every druggable-pathway gene the atlas has
named but never localised. It costs nothing, it is the only human zone-resolved growth
plate that exists, and after this run no future round needs to ask "is it in the tissue?"
as a separate question - the answer is a lookup.

WHAT IT INHERITS. Identical methodology to the round 292 and 300 scripts:
  - the olfactory-receptor empirical null as each array's detection threshold;
  - donor 2's laser capture largely failed to separate zones, so ZONAL ORDER IS READ FROM
    DONOR 1 ONLY and donor 2 contributes presence/absence only.

CEILING ON WHAT AN ABSENCE MEANS - THIS MATTERS MORE HERE THAN ANYWHERE. This platform
missed NPPC, vosoritide's own ligand, by one to two orders of magnitude while detecting
NPR2 and NPR3. It is insensitive to low-abundance secreted and regulatory transcripts, and
to low-abundance GPCRs. A DETECTION IS STRONG EVIDENCE OF PRESENCE. A NON-DETECTION IS WEAK
EVIDENCE OF ABSENCE and must never on its own kill a candidate - it may only lower a prior.
Sex caveat CORR-314/317: donor 1 is female, donor 2 male, so X-linked genes are comparable
only WITHIN a donor.

Usage:  python3 posthoc_round302_all207_localisation.py
Writes: TSV to stdout; redirect to atlas/data/round302/gse9160_all207_localisation.tsv
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analysis as A  # noqa: E402

ZONES = ["RZ", "PZ", "PHZ", "HZ", "PC"]

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))

# Druggable-pathway genes the atlas has named but never run against human tissue.
# Grouped by why round 302 wants them; every one is a target for an obtainable or
# clinical-stage agent that a previous round parked on "no length endpoint".
EXTRA = [
    # canonical-Wnt band (R281's top frontier item) - tankyrase and CBP/beta-catenin
    "TNKS", "TNKS2", "AXIN1", "AXIN2", "CTNNB1", "CREBBP", "EP300", "PORCN", "CSNK1A1",
    # TGF-beta receptor handle identified in R301
    "TGFB1", "TGFB2", "SMAD2", "SMAD4", "SMAD7",
    # lysyl oxidase / hydroxylase family, the R301 survivor
    "LOX", "LOXL1", "LOXL3", "LOXL4", "PLOD3", "P4HA1", "P4HB",
    # polyamine pathway completion
    "SAT1", "OAZ1", "AZIN1", "SMS", "AMD1", "ODC1", "SRM", "SMOX",
    # hedgehog, for the R293/R294 arm
    "HHIP", "PTCH1", "SMO", "GLI1", "GLI2", "GLI3", "SUFU", "KIF7",
    # epigenetic erasers/writers with agents
    "TET1", "TET2", "TET3", "DNMT1", "DNMT3A", "KDM5A", "KDM5B", "EZH2", "HDAC4", "HDAC6",
    # misc obtainable-agent targets parked on "no length endpoint"
    "AKR1B1", "NFAT5", "SLC12A2", "STK39", "OXSR1", "PIEZO1", "MTOR", "IGF1R", "ESR1",
    "CYP19A1", "SOCS2", "STAT5B", "GHR", "NPR2", "NPR3", "FGFR3", "PDE3A", "PDE4B",
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

    genes = []
    path = os.path.join(ROOT, "atlas", "data", "round300", "kosmicki207_genes.txt")
    with open(path) as fh:
        for line in fh:
            g = line.strip().upper()
            if g:
                genes.append(g)
    n207 = set(genes)
    for g in EXTRA:
        if g not in n207:
            genes.append(g)

    print("gene\tin_kosmicki207\tn_probes\td1_detected\td1_cells\td2_detected\td2_cells"
          "\td1_RZ\td1_PZ\td1_PHZ\td1_HZ\td1_PC\td1_max_zone\tverdict")
    for g in genes:
        probes = sym.get(g, [])
        if not probes:
            print("%s\t%s\t0\t0\t0\t0\t0\t\t\t\t\t\t\tNOT_ON_PLATFORM"
                  % (g, int(g in n207)))
            continue
        n = len(probes) * 5
        d1 = sum(1 for p in probes for z in ZONES if X[p][idx[(1, z)]] > thr[idx[(1, z)]])
        d2 = sum(1 for p in probes for z in ZONES if X[p][idx[(2, z)]] > thr[idx[(2, z)]])
        best = max(probes, key=lambda p: sum(X[p][idx[(1, z)]] for z in ZONES))
        vals = {z: X[best][idx[(1, z)]] for z in ZONES}
        det = {z: vals[z] > thr[idx[(1, z)]] for z in ZONES}
        maxz = max(ZONES, key=lambda z: vals[z]) if any(det.values()) else ""
        if d1 > 0 and d2 > 0:
            verdict = "PRESENT_BOTH"
        elif d1 > 0:
            verdict = "PRESENT_D1"
        elif d2 > 0:
            verdict = "PRESENT_D2_ONLY"
        else:
            verdict = "not_detected"
        print("%s\t%d\t%d\t%d\t%d\t%d\t%d\t%.0f\t%.0f\t%.0f\t%.0f\t%.0f\t%s\t%s"
              % (g, int(g in n207), len(probes), int(d1 > 0), d1, int(d2 > 0), d2,
                 vals["RZ"], vals["PZ"], vals["PHZ"], vals["HZ"], vals["PC"],
                 maxz, verdict))
    return 0


if __name__ == "__main__":
    sys.exit(main())
