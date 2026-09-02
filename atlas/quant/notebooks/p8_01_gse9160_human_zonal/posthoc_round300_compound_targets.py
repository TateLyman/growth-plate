#!/usr/bin/env python3
"""
POST HOC, ADDED ROUND 300. Second post-hoc use of this notebook; declared, not hidden.
The gene list below was chosen because kosmicki2026 Supplementary Table 6 gave each of
these a signed effect on human height in centimetres, which happened after this notebook
was written. Every claim drawn from it is capped accordingly.

WHAT IT ASKS. Round 300 pulled signed burden effects for all 207 genome-wide-significant
height genes. Before any of them is proposed as a drug target, CORR-316 requires the free
local query first: is the gene expressed in a HUMAN growth plate at all? A target absent
from the tissue is not a growth-plate target, whatever its effect on adult height - it may
act through the liver, the gonad or the pituitary instead.

WHAT IT INHERITS. Everything methodological comes from analysis.py and from this notebook's
own findings, identically to posthoc_height_gene_localisation.py (round 292):
  - the olfactory-receptor empirical null as the per-array detection threshold;
  - donor 2's laser capture largely failed to separate zones, so ZONAL ORDER IS READ FROM
    DONOR 1 ONLY and donor 2 contributes presence/absence only.

THE SEX CAVEAT, CORR-314/317. Donor 1 is female, donor 2 is male. Any X-linked gene must be
compared only WITHIN a donor, never across. X-linked genes in this panel are flagged in the
output.

CEILING ON WHAT AN ABSENCE MEANS. This platform missed NPPC - vosoritide's own ligand - by
one to two orders of magnitude while detecting NPR2 and NPR3. It is insensitive to
low-abundance secreted and regulatory transcripts. A detection is therefore strong evidence
of presence; a non-detection is weak evidence of absence and is reported as such.

Usage:  python3 posthoc_round300_compound_targets.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analysis as A  # noqa: E402

ZONES = ["RZ", "PZ", "PHZ", "HZ", "PC"]
X_LINKED = {"FGD1", "IRS4", "SHOX", "NRK", "SHANK1"}

GENES = [
    ("TGF-beta restraint axis - three genes, one axis, all loss->taller",
     ["FBN1", "TGFB3", "LTBP2", "TGFB1", "TGFB2", "LTBP1", "LTBP3", "LTBP4",
      "AGTR1", "SMAD3"]),
    ("CNP axis - both arms human-validated in opposite directions",
     ["NPR2", "NPR3", "NPPC", "PDE5A", "PDE3B", "PRKG2"]),
    ("free IGF-1 availability - the objective with no molecule",
     ["PAPPA", "PAPPA2", "STC1", "STC2", "IGFBP4", "IGFBP5", "IRS1", "IGF1R"]),
    ("loss->taller, never in this atlas",
     ["ABCB1", "AMD1", "POR", "LOXL2", "PLOD2", "CHAD", "SCMH1", "HMG20B",
      "PTPN9", "DPP9", "CNNM3", "B4GALNT3", "KIF7", "HLTF", "ZNF518A"]),
    ("loss->shorter and large - contraindication candidates",
     ["ERF", "FGF2", "DLK1", "SERPINH1", "DDR2", "FBLN5", "HMGA2", "TRPS1"]),
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
    print("donor 1 = female 11 y 10 m (dissection CLEAN); donor 2 = male 13 y 3 m (FAILED)")
    print("Zonal ORDER from donor 1 only. Donor 2 = presence/absence only.")
    print("A detection is strong; a non-detection is WEAK (this platform missed NPPC).\n")

    verdicts = []
    for header, genes in GENES:
        print("=" * 100)
        print("## %s" % header.upper())
        for g in genes:
            probes = sym.get(g, [])
            if not probes:
                print("  %-9s NOT ON PLATFORM" % g)
                verdicts.append((g, "not on platform", "", ""))
                continue
            det = {1: 0, 2: 0}
            d1_profile = []
            for p in sorted(probes):
                for d in (1, 2):
                    for z in ZONES:
                        i = idx[(d, z)]
                        if X[p][i] > thr[i]:
                            det[d] += 1
            n = len(probes) * 5
            # zonal profile: donor 1, best-detected probe
            best = max(probes, key=lambda p: sum(X[p][idx[(1, z)]] for z in ZONES))
            for z in ZONES:
                i = idx[(1, z)]
                d1_profile.append("%s%s%.0f" % (z, "+" if X[best][i] > thr[i] else ".",
                                                X[best][i]))
            flag = "  [X-LINKED: compare within donor only]" if g in X_LINKED else ""
            print("  %-9s D1 %2d/%-2d  D2 %2d/%-2d   %s%s"
                  % (g, det[1], n, det[2], n, "  ".join(d1_profile), flag))
            verdicts.append((g, "%d/%d" % (det[1], n), "%d/%d" % (det[2], n),
                             " ".join(d1_profile)))
        print()

    print("=" * 100)
    print("## WHAT IS PRESENT AND WHAT IS NOT")
    present = [v for v in verdicts if "/" in v[1] and int(v[1].split("/")[0]) > 0]
    absent = [v for v in verdicts if "/" in v[1] and int(v[1].split("/")[0]) == 0]
    missing = [v for v in verdicts if v[1] == "not on platform"]
    print("  detected in donor 1 : %s" % ", ".join(v[0] for v in present))
    print("  ZERO in donor 1     : %s" % ", ".join(v[0] for v in absent))
    print("  not on platform     : %s" % ", ".join(v[0] for v in missing))
    return 0


if __name__ == "__main__":
    sys.exit(main())
