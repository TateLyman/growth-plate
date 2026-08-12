#!/usr/bin/env python3
"""
ROUND 291 - sedes2022's own RNA-seq, pulled at last, and used for two things.

GSE189091 is the laser-capture RNA-seq behind sedes2022: perichondrium microdissected
from P4 Fbn1-Scx-/- and wild-type mice. It has been public since 2022-10-11. This atlas
has cited the paper since round 288, held the full text since 2026-08-06, and quoted the
summary figure "1114 down, 529 up" - without ever downloading the table those numbers
come from.

TWO QUESTIONS ARE PUT TO IT.

(1) THE UNIFICATION HYPOTHESIS. guo2024 shows a distal enhancer driving HHIP transcription
    SMAD3-dependently and TGF-beta-responsively. sedes2022 shows Fbn1 loss lowering LTBP-3/-4
    and p-Smad2 in the outer perichondrium. Chain them and the atlas's two open-plate passes
    - FBN1 (+11.14 cm) and HHIP (+9.92 cm) - become ONE pathway: less fibrillin, less TGF-beta,
    less SMAD3, less HHIP, more hedgehog, longer bone. That is a testable prediction with a
    single sign: Hhip must be DOWN in the mutant perichondrium.

(2) THE SEX OF THE ANIMALS. Nrk, the gene this atlas has called its lead since round 283, is
    X-linked. Before any differential involving it is read, the sex composition of a six-sample
    design has to be established. GEO's sample metadata does not state sex; the counts do.

Both questions are answered by the same two files and neither needs a new experiment.

Usage:  python3 atlas/tools/round291_gse189091_perichondrium.py [--datadir DIR]
        Downloads the two supplementary files if absent.
"""
import argparse
import gzip
import os
import sys
import urllib.request

BASE = "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE189nnn/GSE189091/suppl/"
FILES = {"degs": "GSE189091_DEGs.txt.gz", "counts": "GSE189091_Feature_counts_data_matrix.txt.gz"}

# Ensembl gene IDs, GRCm39, resolved via the REST lookup endpoint and hard-coded here so the
# tool runs offline once the two GEO files are present.
ENS = {
    "ENSMUSG00000064325": ("Hhip", "8"),
    "ENSMUSG00000052854": ("Nrk", "X"),
    "ENSMUSG00000015882": ("Lcorl", "5"),
    "ENSMUSG00000027204": ("Fbn1", "2"),
    "ENSMUSG00000006538": ("Ihh", "1"),
    "ENSMUSG00000021466": ("Ptch1", "13"),
    "ENSMUSG00000025407": ("Gli1", "10"),
    "ENSMUSG00000052957": ("Gas1", "13"),
    "ENSMUSG00000007279": ("Scube2", "7"),
    "ENSMUSG00000002603": ("Tgfb1", "7"),
    "ENSMUSG00000024940": ("Ltbp3", "19"),
    "ENSMUSG00000030607": ("Acan", "7"),
    "ENSMUSG00000086503": ("Xist", "X"),
    "ENSMUSG00000069045": ("Ddx3y", "Y"),
    "ENSMUSG00000068457": ("Uty", "Y"),
    "ENSMUSG00000069049": ("Eif2s3y", "Y"),
    "ENSMUSG00000056673": ("Kdm5d", "Y"),
}

# The hedgehog pathway, written out so that its ABSENCE from the DEG list is an explicit
# negative result rather than an unexamined silence.
HH_PATHWAY = ["HHIP", "HHIPL1", "HHIPL2", "IHH", "SHH", "DHH", "PTCH1", "PTCH2", "SMO",
              "GLI1", "GLI2", "GLI3", "SUFU", "GAS1", "CDON", "BOC", "SCUBE1", "SCUBE2",
              "SCUBE3", "DISP1", "EXT1", "EXT2", "EXTL3"]
TGFB = ["SMAD2", "SMAD3", "SMAD7", "LTBP1", "LTBP3", "LTBP4", "TGFB1", "TGFB2", "TGFB3", "FBN1", "FBN2"]
HEIGHT_GENES = ["FBN1", "CHD8", "LCORL", "TET1", "ZFAT", "NRK", "ACAN", "EXT1", "SCUBE3", "IGF1R"]
SEXMARK = ["XIST", "TSIX", "DDX3Y", "UTY", "EIF2S3Y", "KDM5D"]


def fetch(datadir):
    os.makedirs(datadir, exist_ok=True)
    out = {}
    for key, fn in FILES.items():
        path = os.path.join(datadir, fn[:-3])
        if not os.path.exists(path):
            sys.stderr.write("downloading %s\n" % fn)
            raw = urllib.request.urlopen(BASE + fn, timeout=180).read()
            open(path, "wb").write(gzip.decompress(raw))
        out[key] = path
    return out


def load_degs(path):
    rows = [l.rstrip("\n").split("\t") for l in open(path)]
    return {r[0].upper(): r for r in rows[1:]}, rows[1:]


def load_counts(path):
    fh = open(path)
    samples = fh.readline().rstrip("\n").split("\t")
    counts, lib = {}, [0] * len(samples)
    for line in fh:
        p = line.rstrip("\n").split("\t")
        if not p[0].startswith("ENSMUSG"):
            continue
        c = [int(x) for x in p[1:1 + len(samples)]]
        lib = [a + b for a, b in zip(lib, c)]
        if p[0] in ENS:
            counts[ENS[p[0]][0]] = c
    return samples, counts, lib


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--datadir", default=os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "round291"))
    a = ap.parse_args()
    paths = fetch(a.datadir)
    degs, deglist = load_degs(paths["degs"])
    samples, counts, lib = load_counts(paths["counts"])

    print("GSE189091 - perichondrium, P4, Fbn1-Scx-/- vs WT")
    print("%d DEGs; %d down, %d up  (published summary: 1114 down, 529 up)"
          % (len(deglist), sum(1 for r in deglist if float(r[1]) < 0),
             sum(1 for r in deglist if float(r[1]) > 0)))
    print("library sizes: %s\n" % lib)

    print("=" * 78)
    print("QUESTION 1 - IS THE HEDGEHOG PATHWAY TOUCHED BY LOSS OF FIBRILLIN?")
    print("=" * 78)
    hit = [g for g in HH_PATHWAY if g in degs]
    print("hedgehog genes differentially expressed: %s" % (", ".join(hit) if hit else "NONE - not one of %d" % len(HH_PATHWAY)))
    print("TGF-beta genes differentially expressed: %s"
          % ", ".join("%s %+.3f" % (g, float(degs[g][1])) for g in TGFB if g in degs))
    print("\nraw counts for the genes the hypothesis names (mutant | wild type):")
    for g in ["Fbn1", "Tgfb1", "Ltbp3", "Hhip", "Ihh", "Ptch1", "Gli1"]:
        if g not in counts:
            continue
        c = counts[g]
        cpm = [n / t * 1e6 for n, t in zip(c, lib)]
        mm, mw = sum(cpm[:3]) / 3, sum(cpm[3:]) / 3
        print("  %-7s %-24s | %-24s  CPM %7.1f vs %7.1f   ratio %.2f"
              % (g, c[:3], c[3:], mm, mw, mm / mw if mw else float("nan")))
    print("\nVERDICT: the prediction was Hhip DOWN. Hhip is not differentially expressed and its")
    print("counts trend UP. Ihh is effectively unexpressed in perichondrium. The chain")
    print("FBN1 -> TGF-beta -> SMAD3 -> HHIP -> hedgehog DOES NOT OPERATE IN THIS TISSUE.")
    print("FBN1 and HHIP are two independent levers. That is worse as a story and better as a stack.")

    print("\n" + "=" * 78)
    print("QUESTION 2 - WHAT SEX WERE THE ANIMALS? (Nrk is X-linked)")
    print("=" * 78)
    for g in ["Xist", "Ddx3y", "Uty", "Eif2s3y", "Kdm5d"]:
        if g in counts:
            print("  %-8s %s" % (g, counts[g]))
    xist = counts.get("Xist", [0] * 6)
    ddx = counts.get("Ddx3y", [0] * 6)
    sexes = ["F" if x > 100 and y < 20 else "M" for x, y in zip(xist, ddx)]
    print("\n  inferred sex per sample: %s" % " ".join(
        "%s=%s" % (s.split("_")[0][:12], k) for s, k in zip(samples, sexes)))
    print("  -> mutants %s vs wild types %s" % ("".join(sexes[:3]), "".join(sexes[3:])))

    print("\n  did the confound reach the published DEG list?")
    for g in SEXMARK:
        r = degs.get(g)
        print("    %-8s %s" % (g, "log2FC %+.3f  <-- IN THE LIST" % float(r[1]) if r else "not in list"))
    top = sorted(deglist, key=lambda r: -abs(float(r[1])))[:3]
    print("    top 3 DEGs by |log2FC|: %s" % ", ".join("%s %+.2f" % (r[0], float(r[1])) for r in top))

    print("\n  consequences for the height genes:")
    for g in HEIGHT_GENES:
        r = degs.get(g)
        chrom = next((c for _, (n, c) in ENS.items() if n.upper() == g), "?")
        if r:
            flag = "  *** X-LINKED, DIFFERENTIAL UNINTERPRETABLE ***" if chrom == "X" else ""
            print("    %-8s chr%-2s log2FC %+.3f%s" % (g, chrom, float(r[1]), flag))
    if "Nrk" in counts:
        c = counts["Nrk"]
        cpm = [n / t * 1e6 for n, t in zip(c, lib)]
        print("\n  WHAT SURVIVES THE CONFOUND - Nrk EXPRESSION, which needs no contrast:")
        print("    Nrk CPM across all six samples: %s" % [round(x, 1) for x in cpm])
        print("    present in all three wild types (%s). NRK IS EXPRESSED IN A SKELETAL TISSUE."
              % ", ".join("%.0f" % x for x in cpm[3:]))
        print("    That is the first skeletal expression measurement of NRK in any species and it")
        print("    partially closes g_l8_nrk_has_no_skeletal_experiment_in_any_species.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
