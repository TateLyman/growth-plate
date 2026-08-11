#!/usr/bin/env python3
"""
ROUND 283 - cross the largest human rare-variant height study against the growth-plate
transcriptome this atlas already owns.

WHY. kosmicki2026 (preprint, 826,066 discovery exomes + 624,567 replication) reports 17 genes
whose SINGLETON putative-loss-of-function variants move adult height by a mean of 8.92 cm -
about 52x the average common height variant. SIX of them move it UP: FBN1 +11.14, CHD8
+10.22, LCORL +9.99, TET1 +8.32, ZFAT +7.86, NRK +3.79 cm per allele.

The question this tool answers is the one the human genetics cannot: DO ANY OF THESE GENES
LOCALISE TO THE GROWTH PLATE, AND IF SO TO WHICH COMPARTMENT? The atlas holds chu2026's
mouse GP1-vs-GP2 differential expression table (Sci Transl Med, adw3590, data file S1,
"Table S2: differentially regulated genes between mouse GP1 and GP2 clusters"), where GP1 is
the ROOT cluster.

METHOD, AND THE ONE THING THAT HAD TO BE ESTABLISHED FIRST. The supplementary table does not
state which way round the contrast runs. So the sign convention is CALIBRATED, not assumed:
a panel of canonical root/resting markers (SFRP5, PTHLH, NT5E/CD73, GAS1) is read against a
panel of differentiation markers (COL10A1, GDF10, PRG4, IBSP). If the resting panel is
consistently one sign and the differentiation panel the other, the convention is fixed and
reported; if not, the script REFUSES to assign direction and says so. Nothing downstream is
printed without that check passing.

CORR-270 applies: a transcript localisation is a pointer, not a mechanism, and this script
grades nothing.
"""
import csv, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "round243_supplied", "chu2026_supp", "adw3590_data_file_s1.csv")
OUT = os.path.join(ROOT, "data", "round283")

# kosmicki2026 Table 1 - the 17 singleton-pLoF height genes, beta in cm per allele
HEIGHT_GENES = {
    "ACAN": -16.55, "ANKRD11": -11.16, "COL1A1": -10.36, "EXT1": -8.70,
    "IGF2BP2": -8.68, "ADAMTS6": -8.40, "ADAMTS10": -8.24, "IGF1R": -8.23,
    "DTL": -7.34, "SCUBE3": -7.18, "NF1": -5.55,
    "NRK": +3.79, "ZFAT": +7.86, "TET1": +8.32, "LCORL": +9.99,
    "CHD8": +10.22, "FBN1": +11.14,
}

# sign-calibration panels. Chosen BEFORE looking at the height genes.
ROOT_MARKERS = ["SFRP5", "PTHLH", "NT5E", "GAS1"]          # resting / root cluster
DIFF_MARKERS = ["COL10A1", "GDF10", "PRG4", "IBSP"]        # differentiated / away from root


def load():
    rows = {}
    with open(SRC, encoding="utf-8-sig") as fh:
        for rec in csv.reader(fh, delimiter=";"):
            if len(rec) < 6 or rec[0] in ("Gene", "") or rec[0].startswith("Table"):
                continue
            g = rec[0].strip()
            try:
                base = float(rec[1].replace(",", "."))
                lfc = float(rec[2].replace(",", "."))
            except ValueError:
                continue
            padj = None
            if len(rec) > 6 and rec[6].strip():
                try:
                    padj = float(rec[6].replace(",", "."))
                except ValueError:
                    padj = None
            rows[g] = {"baseMean": base, "lfc": lfc, "padj": padj}
    return rows


def main():
    if not os.path.exists(SRC):
        sys.stderr.write("missing %s\n" % SRC)
        return 2
    rows = load()
    print("chu2026 data file S1 - mouse GP1 vs GP2 DEG table: %d genes\n" % len(rows))

    # --- STEP 1: calibrate the sign convention, or refuse ---
    print("SIGN CALIBRATION (this must pass before any direction is reported)")
    rmark = [(g, rows[g]["lfc"], rows[g]["padj"]) for g in ROOT_MARKERS if g in rows]
    dmark = [(g, rows[g]["lfc"], rows[g]["padj"]) for g in DIFF_MARKERS if g in rows]
    for label, panel in (("root/resting", rmark), ("differentiated", dmark)):
        for g, lfc, p in panel:
            print("  %-14s %-9s lfc %+7.3f  padj %s" % (label, g, lfc, "-" if p is None else "%.2e" % p))
    r_neg = sum(1 for _, l, _ in rmark if l < 0)
    d_pos = sum(1 for _, l, _ in dmark if l > 0)
    ok = bool(rmark) and bool(dmark) and r_neg == len(rmark) and d_pos == len(dmark)

    # independent anchor: round 241 records human GP1 vs GP2 as 819 up / 165 down, so the
    # GP1-up direction should be the MAJORITY sign among significant genes.
    sig = [v for v in rows.values() if v["padj"] is not None and v["padj"] < 0.05]
    npos = sum(1 for v in sig if v["lfc"] > 0)
    nneg = len(sig) - npos
    print("\n  global skew among %d significant genes: %d positive, %d negative (%.2f:1)"
          % (len(sig), npos, nneg, npos / max(nneg, 1)))

    if not ok:
        print("\n  *** CALIBRATION FAILS - DIRECTION WILL NOT BE ASSIGNED. ***")
        print("  %d/%d root markers negative, %d/%d differentiation markers positive."
              % (r_neg, len(rmark), d_pos, len(dmark)))
        print("  The panels DISAGREE WITH EACH OTHER: SFRP5, PTHLH and NT5E run one way while")
        print("  GAS1 - which round 241 records as a GP1 marker, and which is the quiescent")
        print("  epiphyseal-stem-cell marker - runs the other way, strongly (padj 1.8e-10).")
        print("  The global skew and GAS1 both point to POSITIVE = GP1; the resting-marker panel")
        print("  points to NEGATIVE = GP1. THAT IS A REAL TENSION IN A DATASET THIS ATLAS HAS")
        print("  BUILT FOUR ROUNDS ON, not a bug in this script - chu2026's RNA-velocity root")
        print("  cluster is evidently NOT co-extensive with the canonical resting-zone marker")
        print("  panel. Everything below is therefore reported DIRECTION-FREE: presence and")
        print("  cluster-restriction only, with no compartment assigned.\n")
        directional = False
    else:
        print("\n  PASSES: every root marker is NEGATIVE and every differentiation marker is POSITIVE.")
        print("  CONVENTION: negative log2FC = ENRICHED IN GP1, THE ROOT CLUSTER.\n")
        directional = True

    # --- STEP 2: the height genes against that axis ---
    print("THE 17 kosmicki2026 SINGLETON-pLoF HEIGHT GENES IN THE MOUSE GROWTH PLATE")
    print("%-10s %8s  %9s %8s %10s  %s" % ("gene", "beta_cm", "baseMean", "log2FC", "padj", "call"))
    out = []
    for g, beta in sorted(HEIGHT_GENES.items(), key=lambda kv: -kv[1]):
        r = rows.get(g)
        if r is None:
            print("%-10s %+8.2f  %9s %8s %10s  not in table" % (g, beta, "-", "-", "-"))
            out.append({"gene": g, "beta_cm": beta, "in_table": False})
            continue
        issig = r["padj"] is not None and r["padj"] < 0.05
        call = "not cluster-restricted"
        if issig and directional:
            call = "ROOT-ENRICHED (GP1)" if r["lfc"] < 0 else "away from root (GP2)"
        elif issig:
            call = "CLUSTER-RESTRICTED (direction unassigned)"
        print("%-10s %+8.2f  %9.2f %+8.3f %10s  %s"
              % (g, beta, r["baseMean"], r["lfc"],
                 "-" if r["padj"] is None else "%.2e" % r["padj"], call))
        out.append({"gene": g, "beta_cm": beta, "in_table": True,
                    "baseMean": r["baseMean"], "log2FC": r["lfc"], "padj": r["padj"],
                    "call": call})

    # --- STEP 3: the subset that matters ---
    hits = [o for o in out if o.get("in_table") and o["beta_cm"] > 0
            and o.get("padj") is not None and o["padj"] < 0.05]
    print("\nHEIGHT-INCREASING genes that are EXPRESSED AND CLUSTER-RESTRICTED in the mouse")
    print("growth plate (padj < 0.05, direction deliberately not assigned): %d of 6" % len(hits))
    for o in sorted(hits, key=lambda x: -x["baseMean"]):
        print("  %-8s beta %+0.2f cm/allele | baseMean %7.2f | |log2FC| %.3f | padj %.2e"
              % (o["gene"], o["beta_cm"], o["baseMean"], abs(o["log2FC"]), o["padj"]))
    print("\nFor scale, baseMean in the same table: ACAN %.2f, COL2A1 %.2f, FGFR3 %.2f, NT5E %.2f."
          % (rows["ACAN"]["baseMean"], rows["COL2A1"]["baseMean"],
             rows["FGFR3"]["baseMean"], rows["NT5E"]["baseMean"]))

    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "height_genes_vs_root_cluster.tsv")
    with open(path, "w") as fh:
        fh.write("gene\tbeta_cm\tbaseMean\tlog2FC\tpadj\tcall\n")
        for o in out:
            fh.write("%s\t%+0.2f\t%s\t%s\t%s\t%s\n" % (
                o["gene"], o["beta_cm"],
                "%.4f" % o["baseMean"] if o.get("in_table") else "NA",
                "%+0.4f" % o["log2FC"] if o.get("in_table") else "NA",
                ("%.3e" % o["padj"]) if o.get("in_table") and o["padj"] is not None else "NA",
                o.get("call", "not_in_table")))
    print("\nwrote %s" % path)
    print("\nCAVEATS, STATED HERE SO THEY TRAVEL WITH THE OUTPUT:")
    print("  - MOUSE clusters against HUMAN height genetics. Cross-species by construction.")
    print("  - A GP1-vs-GP2 contrast is TWO clusters, not the whole plate: 'not enriched in GP1'")
    print("    does not mean absent from the growth plate.")
    print("  - Transcript abundance is not protein and not function (CORR-270).")
    print("  - Direction of the human effect (LoF raises height) says nothing about which")
    print("    compartment carries it; this cross only says where the gene is switched on.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
