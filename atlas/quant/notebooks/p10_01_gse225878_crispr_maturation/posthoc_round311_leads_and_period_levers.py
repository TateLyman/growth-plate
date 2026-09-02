#!/usr/bin/env python3
"""
ROUND 311 POST-HOC on GSE225878, run only after the sign convention was calibrated against
baronas2023 and verified on nine control genes (see analysis.py).

TWO QUESTIONS, both of which the atlas has never been able to ask.

Q1. WHAT DOES THIS SCREEN SAY ABOUT THE ATLAS'S OWN LEADS? Every lead in CLAUDE.md was
    promoted on expression, human burden genetics or a length endpoint. None has ever been
    tested against MATURATION TIMING, which is the term that matters at bone age 16. A lead
    whose loss ACCELERATES maturation is spending the period even if it adds a rate.

Q2. WHICH GENES DELAY MATURATION WHEN LOST? That is the period-lever list. The atlas's own
    scale section says every arm but anastrozole raises a rate; anastrozole buys ~1.3 cm over
    3 years and is the only period agent in the stack. A ranked, genome-wide, causal list of
    period levers has never existed here.

DIRECTION RULE (from analysis.py): POSITIVE LFC = knockout matures EARLY = losing the gene
SPENDS the period, so an inhibitor is a CONTRAINDICATION. NEGATIVE LFC = knockout stays
IMMATURE = losing the gene EXTENDS the period, so an inhibitor is the wanted direction.

REQUIRED CAVEAT, applied to every row below. Delayed maturation is NECESSARY for a longer
period and NOT SUFFICIENT for a longer bone. CORR-292: an expanded resting zone with SHORT
bones is a JAM, and a jam reads as "delayed maturation" in this assay exactly like a genuine
period extension does. Only a length endpoint separates them. Nothing here is a promotion.
"""
import os
import sys
import json

sys.path.insert(0, os.path.dirname(__file__))
from analysis import load, LFC_MATURE, LFC_IMMATURE  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "round311")

# Atlas leads. Mouse symbols; human symbol given where it differs in the atlas text.
LEADS = {
    "HHIP": "Hhip", "NRK": "Nrk", "TNKS": "Tnks", "TNKS2": "Tnks2",
    "LOXL2": "Loxl2", "PLOD2": "Plod2", "TET1": "Tet1", "AMD1": "Amd1",
    "SPIN4": "Spin4", "FBN1": "Fbn1", "PDE3B": "Pde3b", "PDE4B": "Pde4b",
    "PDE4D": "Pde4d", "LCORL": "Lcorl", "ZFAT": "Zfat", "CHD8": "Chd8",
    "ACAN": "Acan", "FGFR3": "Fgfr3", "NPR3": "Npr3", "NPPC": "Nppc",
    "SCUBE3": "Scube3", "EXT1": "Ext1", "TGFB3": "Tgfb3", "LTBP2": "Ltbp2",
    "CXXC5": "Cxxc5", "AXIN2": "Axin2", "CTNNB1": "Ctnnb1", "PORCN": "Porcn",
    "SIK3": "Sik3", "HDAC4": "Hdac4", "MEF2C": "Mef2c", "GNAS": "Gnas",
    "ADCY6": "Adcy6", "PIEZO1": "Piezo1", "TRPM7": "Trpm7", "PRKG2": "Prkg2",
    "IHH": "Ihh", "GLI3": "Gli3", "SMO": "Smo", "SOCS2": "Socs2",
    "ESR1": "Esr1", "CYP19A1": "Cyp19a1", "IGF1R": "Igf1r", "GHR": "Ghr",
    "DNMT3A": "Dnmt3a", "NSD1": "Nsd1", "SETD2": "Setd2", "KDM5A": "Kdm5a",
}


def fmt(v):
    return "%+7.3f p%5.2f" % (v[0], v[1]) if v else "   absent    "


def call(d4, d15):
    """Classify a gene using the paper's own thresholds at either time point."""
    hits = []
    for tag, v in (("D4", d4), ("D15", d15)):
        if not v:
            continue
        lfc, p = v[0], v[1]
        if p < 3.0:
            continue
        if lfc > LFC_MATURE:
            hits.append(tag + ":EARLY")
        elif lfc < LFC_IMMATURE:
            hits.append(tag + ":DELAYED")
    return ",".join(hits) if hits else "-"


def main():
    d4, d15 = load("prim_d4"), load("prim_d15")
    os.makedirs(OUT, exist_ok=True)

    print("=" * 78)
    print("Q1  ATLAS LEADS vs MATURATION TIMING")
    print("    POSITIVE = KO matures early = gene's loss SPENDS the period")
    print("    NEGATIVE = KO stays immature = gene's loss EXTENDS the period")
    print("    (paper thresholds LFC>+0.57 / <-0.63 AND -log10p>3)")
    print("=" * 78)
    rows = []
    for h, m in sorted(LEADS.items()):
        a, b = d4.get(m), d15.get(m)
        c = call(a, b)
        rows.append({"human": h, "mouse": m,
                     "d4_lfc": a[0] if a else None, "d4_nlogp": a[1] if a else None,
                     "d15_lfc": b[0] if b else None, "d15_nlogp": b[1] if b else None,
                     "call": c})
        flag = "  <<<" if c != "-" else ""
        print("  %-8s %-8s D4 %s   D15 %s   %s%s" % (h, m, fmt(a), fmt(b), c, flag))

    # Q2: genome-wide period levers
    print()
    print("=" * 78)
    print("Q2  PERIOD LEVERS - knockouts that DELAY maturation at high confidence")
    print("=" * 78)
    delayed = []
    for g in d4:
        a, b = d4.get(g), d15.get(g)
        best = None
        for tag, v in (("D4", a), ("D15", b)):
            if v and v[1] >= 3.0 and v[0] < LFC_IMMATURE:
                if best is None or v[1] > best[2]:
                    best = (tag, v[0], v[1])
        if best:
            delayed.append({"gene": g, "tp": best[0], "lfc": best[1], "nlogp": best[2],
                            "d4_lfc": a[0] if a else None, "d15_lfc": b[0] if b else None})
    delayed.sort(key=lambda r: -r["nlogp"])

    early = []
    for g in d4:
        a, b = d4.get(g), d15.get(g)
        best = None
        for tag, v in (("D4", a), ("D15", b)):
            if v and v[1] >= 3.0 and v[0] > LFC_MATURE:
                if best is None or v[1] > best[2]:
                    best = (tag, v[0], v[1])
        if best:
            early.append({"gene": g, "tp": best[0], "lfc": best[1], "nlogp": best[2]})
    early.sort(key=lambda r: -r["nlogp"])

    print("  BASE RATE: %d genes DELAY, %d genes ACCELERATE, of %d screened"
          % (len(delayed), len(early), len(d4)))
    print("  (CORR-329: in a skewed screen only the rare direction is informative -")
    print("   this screen's skew is reported above and must be read before any sign claim.)")
    print()
    print("  TOP 40 DELAYERS (inhibiting these is the period-extending direction):")
    for r in delayed[:40]:
        print("    %-12s %s LFC %+7.3f  -log10p %6.2f   (D4 %+.2f / D15 %+.2f)"
              % (r["gene"], r["tp"], r["lfc"], r["nlogp"],
                 r["d4_lfc"] if r["d4_lfc"] is not None else float("nan"),
                 r["d15_lfc"] if r["d15_lfc"] is not None else float("nan")))

    json.dump({"leads": rows, "delayed": delayed, "early": early,
               "n_screened": len(d4),
               "thresholds": {"mature": LFC_MATURE, "immature": LFC_IMMATURE, "nlogp": 3.0}},
              open(os.path.join(OUT, "gse225878_calibrated_calls.json"), "w"), indent=1)
    print()
    print("  wrote %s" % os.path.join(OUT, "gse225878_calibrated_calls.json"))


if __name__ == "__main__":
    main()
