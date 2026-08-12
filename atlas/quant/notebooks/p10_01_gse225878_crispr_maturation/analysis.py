#!/usr/bin/env python3
"""
GSE225878 - GENOME-WIDE CRISPR KNOCKOUT SCREEN OF CHONDROCYTE MATURATION (22,624 genes).
Operator-supplied 2026-08-13. BLOCKED until round 311 because the sign convention was
uncalibrated; unblocked by the operator supplying the source paper (baronas2023,
Cell Genomics 3:100299) on 2026-08-12.

WHY THIS DATASET IS DIFFERENT FROM EVERYTHING ELSE IN THE ATLAS.
Every other dataset here is OBSERVATIONAL - expression, association, localisation. This is
a PERTURBATION screen: 22,624 genes knocked out one at a time, 600 million cells assayed,
with a readout that is MATURATION TIMING. At bone age 16 the scarce resource is the PERIOD,
not the rate, and maturation timing IS the period. The atlas has never had a period-directed
screen in any species.

THE SIGN CONVENTION, now calibrated from baronas2023 and NOT inferred.
  - Readout is CD-200, a cell-surface chondrocyte MATURATION marker. GPLCs (growth-plate-like
    chondrocytes) are CD-200-low early and CD-200-high late.
  - At each time point the top 10% and bottom 10% CD-200 cells were collected and their guide
    barcodes counted. Column header in the deposited file is "Imm vs Mat Average Fold Change".
  - PAPER'S OWN THRESHOLDS: LFC > 0.57 = the knockout MATURED EARLY.
                            LFC < -0.63 = the knockout FAILED TO MATURE / stayed immature.
  - So: POSITIVE LFC = losing this gene ACCELERATES maturation (spends the period).
        NEGATIVE LFC = losing this gene DELAYS maturation (extends the period).

THE CONTROLS VALIDATE IT, AND THIS IS WHY THE CALL IS NOW SAFE TO MAKE. Round 310 recorded
four control genes and said they did not resolve direction. Under the calibrated convention
all four are textbook:
  - Pth1r KO -> POSITIVE (early maturation). PTHrP/PTH1R is THE canonical brake on hypertrophic
    differentiation; Pth1r-null cartilage undergoes accelerated maturation. Correct.
  - Npr2  KO -> POSITIVE (early maturation). CNP/NPR-B sustains the proliferative zone; NPR2
    loss-of-function is acromesomelic dysplasia. Correct.
  - Sox9  KO -> NEGATIVE (fails to mature). SOX9 is required for the chondrocyte programme.
  - Runx2 KO -> NEGATIVE (fails to mature). RUNX2 drives the hypertrophic transition.
  Two delayers and two drivers, both pairs on the correct side. CORR-296's prohibition is
  lifted FOR THIS DATASET ONLY - it was never lifted for chu2026.

THERAPEUTIC DIRECTION FOR THIS CASE. We want to DELAY maturation, so we want to INHIBIT genes
whose knockout is NEGATIVE. A positive-LFC gene is one whose loss spends the period, which
makes an inhibitor of it a CONTRAINDICATION - the same signed logic as round 300.

WHAT THIS SCREEN CANNOT DO, stated before reading it.
  - Monolayer murine cell line, not a growth plate. No zones, no columns, no matrix loading.
  - CD-200 is a maturation MARKER, not length. Delayed maturation is necessary for a longer
    period and NOT sufficient for a longer bone - CORR-292's jam (expanded resting zone with
    SHORT bones) would read as "delayed maturation" here and is a failure, not a success.
  - Proliferation and maturation are confounded: a knockout depleted from culture can shift
    apparent maturation. The paper handles this in secondary screening; the primary files do not.
  - Mouse. Every call carries species.

Usage: python3 analysis.py
"""
import gzip
import os
import json

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "supplied_2026_08_13")
FILES = {
    "prim_d4": "GSE225878_Prim_D4_Average_LFC_100_21-10-12-16-49.txt.gz",
    "prim_d15": "GSE225878_Prim_D15_Average_LFC_100_21-10-12-16-49.txt.gz",
    "sec_d4": "GSE225878_Sec_D4_Avg_LFC_100_21-11-09-14-52.txt.gz",
    "sec_d15": "GSE225878_Sec_D15_Avg_LFC_100_21-11-09-14-59.txt.gz",
}

# Paper's own significance thresholds (baronas2023, results text)
LFC_MATURE = 0.57
LFC_IMMATURE = -0.63
NLOGP = 3.0


def load(key):
    """Return {gene: (lfc, avg_-log10p, n_guides)}."""
    out = {}
    with gzip.open(os.path.join(BASE, FILES[key]), "rt") as f:
        header = f.readline()
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) < 4:
                continue
            try:
                out[p[0]] = (float(p[1]), float(p[2]), int(p[3]))
            except ValueError:
                continue
    return out


def controls(d4, d15):
    """Re-run round 310's four uncalibrated controls plus the paper's own named hits."""
    rows = []
    spec = [
        ("Pth1r", "canonical brake on hypertrophy; null matures early"),
        ("Npr2", "CNP receptor; LoF = acromesomelic dysplasia"),
        ("Sox9", "master chondrocyte TF; required"),
        ("Runx2", "drives hypertrophic transition"),
        ("Sufu", "intracellular Hh brake; paper reports premature maturation"),
        ("Ptch1", "Hh receptor/brake; paper reports premature maturation"),
        ("Eed", "PRC2; paper reports as top hit"),
        ("Ezh2", "PRC2; paper reports as top hit"),
        ("Suz12", "PRC2; paper reports as top hit"),
    ]
    for g, note in spec:
        rows.append((g, d4.get(g), d15.get(g), note))
    return rows


def main():
    data = {k: load(k) for k in FILES}
    d4, d15 = data["prim_d4"], data["prim_d15"]
    print("GSE225878 primary screen: D4 %d genes, D15 %d genes" % (len(d4), len(d15)))
    print("Secondary: D4 %d, D15 %d" % (len(data["sec_d4"]), len(data["sec_d15"])))
    print()
    print("== CONTROLS (calibration check) ==")
    for g, a, b, note in controls(d4, d15):
        fa = "%+.3f (p %.2f)" % (a[0], a[1]) if a else "absent"
        fb = "%+.3f (p %.2f)" % (b[0], b[1]) if b else "absent"
        print("  %-8s D4 %-20s D15 %-20s  %s" % (g, fa, fb, note))
    return data


if __name__ == "__main__":
    main()
