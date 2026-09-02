#!/usr/bin/env python3
"""
R486 -- CROSS THE JERBOA PROPORTION SIGNAL AGAINST THE HUMAN PLATE'S OWN
PURITY SPLIT.  Two orthogonal datasets, and the cross is what removes the
composition confound in a principled way rather than by assertion.

THE PROBLEM THIS SOLVES.  round486_saxena_interaction_analysis.py measured the
composition confound in saxena2022's own deposited DESeq2 output (CORR-339):

    median species x element interaction, by module
        CARTILAGE      -0.86   (Col2a1 -1.78, Comp -1.14, Col11a1 -0.86)
        MUSCLE         +1.93   (Myh3 +3.42, Acta1 +2.27)
        BONE           +1.74   (Alpl +2.07, Col1a1 +1.74, Ibsp +1.36)
        HOUSEKEEPING   +0.22

The jerboa metatarsal sample is relatively cartilage-poor and muscle/bone-rich.
So on its own the interaction column cannot distinguish:
    a POSITIVE value  =  real up-regulation   OR  muscle/bone contamination
    a NEGATIVE value  =  real down-regulation OR  cartilage dilution

THE ASYMMETRY THAT MAKES THE SCREEN WORK.  The cartilage confound is NEGATIVE.
So a gene that is CARTILAGE-RESTRICTED in an independent human dataset and
comes out POSITIVE in the interaction is moving AGAINST its own dilution, and
cannot be muscle or bone contamination because it is not a muscle or bone gene.
That conjunction is the robust class.  The mirror class -- cartilage gene,
negative interaction -- is confounded WITH the dilution and is therefore the
weak class, and is printed separately rather than mixed in.

THE SECOND DATASET.  R411's sex-corrected purity split on GSE288028: 12 human
postnatal growth-plate samples, sex called from XIST vs a Y panel, split WITHIN
the 9 males by COL2A1, ratio = median CPM purest half / median contaminated
half.  Benchmarks COL2A1 7.65, ACAN 1.96; blood calibrators PTPRC 0.00,
HBB 0.03.  Cartilage-enriched is defined here at the ACAN benchmark, 1.96.

CORR-363 GOVERNS AND IS THE REASON THIS IS A CONJUNCTION AND NOT A RANKING.
A purity ratio measures INVESTMENT, not rate-limitation, and is structurally
blind to universal machinery.  It is used here ONLY to answer "is this gene
cartilage-restricted or is it a plausible muscle/bone contaminant", which is
exactly what it can answer.  It is not used to rank.

Output: atlas/data/round486/interaction_x_human_purity.tsv
"""
import csv
import json
import os

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
R486 = os.path.join(DATA, "round486")

ACAN_BENCHMARK = 1.96   # R411's cartilage-enrichment benchmark
MIN_PURE_CPM = 20.0     # must actually be expressed in the human plate
MIN_BASEMEAN = 50.0     # saxena's own abundance floor
MAX_PADJ = 0.01         # significant in the elongating element's own contrast


def human_purity():
    """R411 sex-corrected split, recomputed from source (not carried)."""
    genes = json.load(open(os.path.join(DATA, "round344", "gse288028_gene_names.json")))
    cpm = np.load(os.path.join(DATA, "round344", "gse288028_human12_cpm.npy"))
    idx = {g: i for i, g in enumerate(genes)}

    ypanel = [g for g in ("RPS4Y1", "UTY", "USP9Y", "DDX3Y", "EIF2S3Y", "KDM5D") if g in idx]
    xist = cpm[:, idx["XIST"]] if "XIST" in idx else np.zeros(cpm.shape[0])
    yexp = cpm[:, [idx[g] for g in ypanel]].sum(axis=1)
    males = [i for i in range(cpm.shape[0]) if xist[i] <= yexp[i]]

    col2 = cpm[:, idx["COL2A1"]]
    ms = sorted(males, key=lambda i: -col2[i])
    n = len(ms) // 2
    pure_i, cont_i = ms[:n], ms[-n:]

    out = {}
    for g, i in idx.items():
        v = cpm[:, i]
        p, c = float(np.median(v[pure_i])), float(np.median(v[cont_i]))
        out[g] = (p, c, (p / c) if c > 0 else (float("inf") if p > 0 else None))
    return out


def load_interaction(path):
    rows = {}
    with open(path) as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            s = r["symbol"]
            if not s or s == "NA":
                continue
            try:
                rows[s] = dict(
                    baseMean=float(r["MT_baseMean"]),
                    mt=float(r["MT_log2FoldChange"]),
                    ru=float(r["RU_log2FoldChange"]),
                    padj=float(r["MT_padj"]) if r["MT_padj"] not in ("", "NA") else 1.0,
                    inter=float(r["interaction_MT_minus_RU"]),
                )
            except ValueError:
                continue
    return rows


def main():
    hp = human_purity()
    n3 = load_interaction(os.path.join(R486, "saxena_deseq2_n3.tsv"))
    n2 = load_interaction(os.path.join(R486, "saxena_deseq2_n2.tsv"))

    print("=" * 100)
    print("CONTROL 0 -- the human split reproduces its own benchmarks")
    print("=" * 100)
    for g in ("COL2A1", "ACAN", "COL10A1", "IHH", "PTPRC", "HBB", "AGTR1", "MME"):
        if g in hp:
            p, c, r = hp[g]
            print(f"  {g:8s} pure {p:10.2f}  contam {c:10.2f}  ratio "
                  f"{('inf' if r == float('inf') else f'{r:.2f}') if r is not None else 'na'}")

    recs = []
    for sym, a in n3.items():
        H = sym.upper()
        if H not in hp:
            continue
        p, c, ratio = hp[H]
        if ratio is None or p < MIN_PURE_CPM:
            continue
        if a["baseMean"] < MIN_BASEMEAN or a["padj"] >= MAX_PADJ:
            continue
        b = n2.get(sym)
        if not b or (a["inter"] > 0) != (b["inter"] > 0):
            continue          # sign must replicate in the independent cohort
        recs.append(dict(sym=sym, human=H, pure=p, ratio=ratio,
                         inter=a["inter"], inter_n2=b["inter"],
                         mt=a["mt"], ru=a["ru"], baseMean=a["baseMean"]))

    enriched = [r for r in recs if r["ratio"] >= ACAN_BENCHMARK]
    up = sorted([r for r in enriched if r["inter"] > 0], key=lambda r: -r["inter"])
    dn = sorted([r for r in enriched if r["inter"] < 0], key=lambda r: r["inter"])

    print()
    print("=" * 100)
    print("THE ROBUST CLASS -- cartilage-restricted in HUMAN, UP in the elongating")
    print("element in BOTH jerboa cohorts, i.e. moving AGAINST its own dilution")
    print("=" * 100)
    print(f"  {len(recs)} genes pass abundance+significance+sign-replication and are")
    print(f"  measurable in the human plate;  {len(enriched)} of those are cartilage-")
    print(f"  enriched at the ACAN benchmark;  {len(up)} of those are UP.")
    print()
    print(f"  {'gene':<12}{'humanCPM':>10}{'ratio':>8}{'baseMn':>9}{'MTlfc':>8}"
          f"{'RUlfc':>8}{'n3':>7}{'n2':>7}")
    for r in up[:35]:
        print(f"  {r['sym']:<12}{r['pure']:>10.1f}{r['ratio']:>8.2f}"
              f"{r['baseMean']:>9.0f}{r['mt']:>8.2f}{r['ru']:>8.2f}"
              f"{r['inter']:>7.2f}{r['inter_n2']:>7.2f}")

    print()
    print("=" * 100)
    print("THE WEAK CLASS -- cartilage-restricted and DOWN, i.e. CONFOUNDED WITH")
    print("the dilution.  Printed so it is not mistaken for the class above.")
    print("=" * 100)
    print(f"  {'gene':<12}{'humanCPM':>10}{'ratio':>8}{'baseMn':>9}{'n3':>7}{'n2':>7}")
    for r in dn[:20]:
        print(f"  {r['sym']:<12}{r['pure']:>10.1f}{r['ratio']:>8.2f}"
              f"{r['baseMean']:>9.0f}{r['inter']:>7.2f}{r['inter_n2']:>7.2f}")

    print()
    print("=" * 100)
    print("NAMED MODULES, scored the same way")
    print("=" * 100)
    MODULES = {
        "secreted Wnt antagonists (R281/R356)": [
            "Sfrp1", "Sfrp2", "Sfrp4", "Sfrp5", "Frzb", "Wif1", "Dkk1", "Dkk2",
            "Dkk3", "Notum", "Sost", "Sostdc1", "Smoc1", "Smoc2"],
        "canonical Wnt readout": ["Axin2", "Lef1", "Tcf7", "Ctnnb1", "Ccn4", "Wisp1", "Cxxc5"],
        "hedgehog availability layer (R287/R290)": [
            "Hhip", "Gas1", "Cdon", "Boc", "Scube1", "Scube2", "Scube3", "Ptch1",
            "Disp1", "Gli1", "Gli3", "Smo"],
        "atlas leads without a prior cross-species read": [
            "Chad", "Clec3a", "Ecrg4", "C2orf40", "Spin4", "Tet1", "Loxl2",
            "Plod1", "Plod2", "Aebp1", "Nrk", "Adam12", "Pappa2", "Stc2"],
    }
    for name, gl in MODULES.items():
        print(f"\n  --- {name}")
        for g in gl:
            a = n3.get(g)
            b = n2.get(g)
            H = g.upper()
            hpp = hp.get(H)
            if a is None:
                print(f"     {g:<10} not in the 1:1 orthologue set")
                continue
            hs = ("na" if hpp is None or hpp[2] is None
                  else ("inf" if hpp[2] == float("inf") else f"{hpp[2]:.2f}"))
            hc = "na" if hpp is None else f"{hpp[0]:.1f}"
            n2s = f"{b['inter']:+.2f}" if b else "  na"
            flag = ""
            if b and (a["inter"] > 0) == (b["inter"] > 0) and abs(a["inter"]) > 1.0:
                flag = "  <= replicated, |inter|>1"
            print(f"     {g:<10} humanCPM {hc:>9} ratio {hs:>6}  baseMn "
                  f"{a['baseMean']:>8.0f}  n3 {a['inter']:+.2f}  n2 {n2s}{flag}")

    with open(os.path.join(R486, "interaction_x_human_purity.tsv"), "w") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["symbol", "human_pure_cpm", "human_purity_ratio", "mt_baseMean",
                    "mt_lfc", "ru_lfc", "interaction_n3", "interaction_n2",
                    "cartilage_enriched"])
        for r in sorted(recs, key=lambda r: -r["inter"]):
            w.writerow([r["sym"], round(r["pure"], 2), round(r["ratio"], 3),
                        round(r["baseMean"], 1), round(r["mt"], 3), round(r["ru"], 3),
                        round(r["inter"], 3), round(r["inter_n2"], 3),
                        int(r["ratio"] >= ACAN_BENCHMARK)])
    print()
    print(f"wrote {len(recs)} rows to atlas/data/round486/interaction_x_human_purity.tsv")


if __name__ == "__main__":
    main()
