#!/usr/bin/env python3
"""
ROUND 323 POST-HOC. The question: WHICH OF THIS ATLAS'S TARGETS HAS AN AXIAL REGULATORY
LANDSCAPE? At bone age 16 the residual is trunk-dominant and every stack agent was
characterised on long bones. Round 318 answered this from GWAS; this answers it from human
chromatin, in tissue, with a completely different failure mode.

SCORE. For a gene, peak base-pairs within (gene body +/- 100 kb) divided by that sheet's total
peak base-pairs, x1e6. Axial = mean(LUMBAR, THORACIC). Appendicular = mean over the 8 E67
sheets, with the 8 E54 sheets as a second reference. Reported as log2(axial / appendicular).

BASE RATE FIRST, ALWAYS (CORR-329). The genome-wide distribution of that log2 ratio is
computed over every gene before a single target is read, because a screen with a global skew
makes the common direction uninformative and only the rare one carries signal.

CONTROLS BEFORE TARGETS (CORR-311). Limb-identity genes must come out appendicular, sclerotome
genes axial, housekeeping and the pan-chondrocyte programme neither. Those calls are made from
developmental biology, not from this atlas, so they are a real test.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis import (AXIAL, APP54, APP67, FLANK, build_index, load_genes,  # noqa: E402
                      load_peaks, score)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
OUT = os.path.join(ROOT, "data", "round323")
GTF = os.environ["GRCH37_GTF"]

CONTROLS = {
    "TBX5": "forelimb identity - MUST be appendicular",
    "TBX4": "hindlimb identity - MUST be appendicular",
    "PITX1": "hindlimb identity - MUST be appendicular",
    "HOXA13": "autopod - MUST be appendicular",
    "HOXD13": "autopod - MUST be appendicular",
    "SHOX2": "proximal limb - MUST be appendicular",
    "PAX1": "sclerotome - MUST be axial",
    "PAX9": "sclerotome - MUST be axial",
    "NKX3-2": "sclerotome to cartilage - MUST be axial",
    "MEOX1": "somite - MUST be axial",
    "UNCX": "somite posterior half - MUST be axial",
    "TBX6": "presomitic mesoderm - MUST be axial",
    "ACTB": "housekeeping - MUST be neither",
    "GAPDH": "housekeeping - MUST be neither",
    "RPL13A": "housekeeping - MUST be neither",
    "B2M": "housekeeping - MUST be neither",
    "COL2A1": "pan-chondrocyte - MUST be neither",
    "ACAN": "pan-chondrocyte - MUST be neither",
    "SOX9": "pan-chondrocyte - MUST be neither",
    "COL9A1": "pan-chondrocyte - MUST be neither",
}

TARGETS = {
    "HHIP": "R318 95% trunk by GWAS; best-validated target in the atlas",
    "TET1": "R318 96% trunk; dioxygenase, small-molecule binder",
    "CHAD": "R313 secreted, motif known to 8 residues",
    "SCUBE3": "R318 says LIMB by GWAS - a direct test",
    "NRK": "83.5x chondrocyte-enriched, no inhibitor",
    "FGFR3": "erdafitinib arm; R318 73% trunk",
    "NPPC": "vosoritide ligand; R318 78% leg",
    "NPR2": "vosoritide receptor",
    "NPR3": "R318 ~100% leg",
    "CYP19A1": "anastrozole arm",
    "ESR1": "the period arm's receptor",
    "GHR": "GH arm", "IGF1": "GH arm", "SOCS2": "GH arm brake",
    "TNKS": "R302 lead; R318 says LIMB",
    "LOXL2": "R301 last candidate standing",
    "PLOD2": "same pathway",
    "ENPP1": "R323 top lengthening KO by growth-plate abundance",
    "NCOR2": "R323 dose-dependent lengthening KO",
    "MICU1": "R323 strongest P among lengthening KOs",
    "PANK3": "R323 lengthening KO with a high-quality pocket",
    "LTA4H": "R323 lengthening KO with a clinical inhibitor",
    "PDE3B": "R310 closed - systemic",
    "AMD1": "polyamine arm", "SPIN4": "pool lever",
    "ACAN": "largest kosmicki effect", "FBN1": "R318 LIMB",
    "IHH": "hedgehog ligand", "PTCH1": "hedgehog receptor",
    "SUFU": "intracellular hedgehog brake",
    "SLC26A2": "sulfate transporter - R320", "PAPSS2": "R320",
    "PDE4B": "R308", "PDE4D": "R308", "CDKN2B": "HPO tall-only",
    "CDKN1B": "HPO tall-only", "AR": "HPO tall-only, 9 approved antagonists",
    "KDM6B": "HPO proportionate tall", "FIBP": "HPO proportionate tall",
    "NOTCH2": "the ONLY gene annotated to HP:0008421 tall lumbar vertebral bodies",
}


def main():
    peaks = load_peaks()
    idx, tot = build_index(peaks)
    genes = load_genes(GTF)

    def row(sym):
        g = genes.get(sym)
        if not g:
            return None
        ch, st, en = g
        lo, hi = max(1, st - FLANK), en + FLANK
        a = score(idx, tot, ch, lo, hi, AXIAL)
        p67 = score(idx, tot, ch, lo, hi, APP67)
        p54 = score(idx, tot, ch, lo, hi, APP54)
        import math
        eps = 1e-3
        return dict(gene=sym, axial=a, app67=p67, app54=p54, kb=(hi - lo) / 1000.0,
                    l2_67=math.log((a + eps) / (p67 + eps), 2),
                    l2_54=math.log((a + eps) / (p54 + eps), 2))

    # ---- BASE RATE FIRST ------------------------------------------------------
    allrows = []
    for sym in genes:
        r = row(sym)
        if r and (r["axial"] + r["app67"]) > 0.5:   # window has some signal in either
            allrows.append(r)
    vals = sorted(r["l2_67"] for r in allrows)
    n = len(vals)

    def pct(x):
        import bisect
        return 100.0 * bisect.bisect_left(vals, x) / n
    med = vals[n // 2]
    print("=" * 104)
    print("BASE RATE - log2(axial / E67 appendicular) over %d gene windows with signal" % n)
    print("=" * 104)
    print("  median %+0.3f   p10 %+0.3f  p25 %+0.3f  p75 %+0.3f  p90 %+0.3f  p99 %+0.3f"
          % (med, vals[n // 10], vals[n // 4], vals[3 * n // 4], vals[9 * n // 10],
             vals[99 * n // 100]))
    print("  fraction above zero: %.1f%%" % (100.0 * sum(1 for v in vals if v > 0) / n))
    print("  -> a gene is only interesting where it sits in THIS distribution, not by its sign")

    print()
    print("=" * 104)
    print("CONTROLS - the read is worthless unless these separate")
    print("=" * 104)
    print("  %-9s %8s %8s %8s  %7s %7s  %s"
          % ("gene", "axial", "app67", "app54", "l2_67", "pctile", "expectation"))
    ctrl = []
    for sym, note in CONTROLS.items():
        r = row(sym)
        if not r:
            print("  %-9s not in GRCh37 annotation" % sym)
            continue
        r["note"] = note
        r["pctile"] = pct(r["l2_67"])
        ctrl.append(r)
        print("  %-9s %8.2f %8.2f %8.2f  %+7.2f %6.1f  %s"
              % (sym, r["axial"], r["app67"], r["app54"], r["l2_67"], r["pctile"], note))

    print()
    print("=" * 104)
    print("TARGETS")
    print("=" * 104)
    print("  %-9s %8s %8s %8s  %7s %7s  %s"
          % ("gene", "axial", "app67", "app54", "l2_67", "pctile", "why it is here"))
    out = []
    for sym, note in sorted(TARGETS.items(), key=lambda kv: kv[0]):
        r = row(sym)
        if not r:
            print("  %-9s not in GRCh37 annotation" % sym)
            continue
        r["note"] = note
        r["pctile"] = pct(r["l2_67"])
        out.append(r)
    out.sort(key=lambda r: -r["l2_67"])
    for r in out:
        print("  %-9s %8.2f %8.2f %8.2f  %+7.2f %6.1f  %s"
              % (r["gene"], r["axial"], r["app67"], r["app54"], r["l2_67"], r["pctile"],
                 r["note"]))

    # ---- DISCOVERY -----------------------------------------------------------
    gp = json.load(open(os.path.join(ROOT, "data", "round308",
                                     "gse288028_pseudobulk_presence.json")))["genes"]
    top = [r for r in allrows
           if r["l2_67"] > vals[99 * n // 100] and r["l2_54"] > 0 and r["axial"] > 2.0]
    top.sort(key=lambda r: -r["l2_67"])
    print()
    print("=" * 104)
    print("DISCOVERY - top-1%% axial windows that are ALSO axial-enriched against E54,")
    print("            filtered to genes present in the POSTNATAL human growth plate")
    print("=" * 104)
    keep = []
    for r in top:
        e = gp.get(r["gene"])
        if not e or (e.get("det") or 0) < 10 or (e.get("medCPM") or 0) < 5:
            continue
        r["gp_cpm"] = e["medCPM"]
        r["gp_det"] = e["det"]
        r["gp_pct"] = e["maxPct"]
        keep.append(r)
    print("  %d of %d top-1%% windows survive the postnatal-expression filter" % (len(keep), len(top)))
    for r in keep[:60]:
        print("  %-12s l2_67 %+6.2f  l2_54 %+6.2f  axial %7.2f  GP %8.1f CPM %2d/14 %5.1f%%"
              % (r["gene"], r["l2_67"], r["l2_54"], r["axial"], r["gp_cpm"], r["gp_det"],
                 r["gp_pct"]))

    os.makedirs(OUT, exist_ok=True)
    json.dump(dict(base_rate=dict(n=n, median=med, p90=vals[9 * n // 10],
                                  p99=vals[99 * n // 100]),
                   controls=ctrl, targets=out, discovery=keep),
              open(os.path.join(OUT, "axial_vs_appendicular_atac.json"), "w"), indent=1)
    print("\nwrote axial_vs_appendicular_atac.json")


if __name__ == "__main__":
    main()
