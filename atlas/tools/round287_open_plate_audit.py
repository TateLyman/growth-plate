#!/usr/bin/env python3
"""
ROUND 287 - the open-plate audit, run against THIS GRAPH FIRST.

CORR-302 made this step mandatory: before asserting that a gene is untested, grep
the atlas. The graph is now 811 nodes and 1,573 references and is no longer small
enough to hold in working memory - round 285 declared FBN1 untested while
perichondrial_tgfb_restraint held the decisive datum, from a full text the operator
had supplied five days earlier.

So this tool reports, for every one of kosmicki2026's 17 singleton-pLoF height genes:
  - the signed human effect size in cm per allele
  - which atlas NODES mention the gene, and how many times
  - which BIBLIOGRAPHY entries mention it in their one_line_finding
  - which GAPS mention it
It asserts nothing about the literature. Its only job is to tell the next search
where this file has already been, so that a literature claim is made against a
known baseline rather than against memory.

Direction convention: beta > 0 means LOSS of function makes a human TALLER, so the
therapeutic direction is INHIBITION. beta < 0 means loss makes a human SHORTER, so
the therapeutic direction - if any - is AGONISM, RESTORATION or OVEREXPRESSION, and
those genes are NOT dismissible: the largest single number in the table is ACAN at
-16.55 cm, and a gene that costs 16.55 cm when halved is a gene the plate cares
about.
"""
import os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NODES = os.path.join(ROOT, "nodes")
BIB = os.path.join(ROOT, "sources", "bibliography.yaml")
GAPS = os.path.join(ROOT, "gaps", "gaps.yaml")
OUT = os.path.join(ROOT, "data", "round287")

# kosmicki2026 Table 1. beta in cm of adult height per allele, with SE and carriers.
GENES = [
    ("FBN1",     +11.14, 40, "ECM, TGF-beta",              "Marfan syndrome"),
    ("CHD8",     +10.22, 21, "transcription, Wnt",         "ASD, ID, macrocephaly"),
    ("LCORL",     +9.99, 71, "transcription",              "-"),
    ("TET1",      +8.32, 42, "epigenetic mark maintenance", "-"),
    ("ZFAT",      +7.86, 41, "transcription",              "autoimmune thyroid disease"),
    ("NRK",       +3.79, 56, "transcription",              "-"),
    ("NF1",       -5.55, 140, "ECM",                       "NF1"),
    ("SCUBE3",    -7.18, 49, "ECM, TGF-beta",              "short stature/skeletal anomalies"),
    ("DTL",       -7.34, 42, "TGF-beta, DNA damage repair", "-"),
    ("IGF1R",     -8.23, 53, "IGF",                        "IGF1 resistance"),
    ("ADAMTS10",  -8.24, 27, "ECM",                        "Weill-Marchesani"),
    ("ADAMTS6",   -8.40, 27, "ECM",                        "-"),
    ("IGF2BP2",   -8.68, 27, "IGF",                        "-"),
    ("EXT1",      -8.70, 30, "ECM, GAG biosynthesis",      "multiple osteochondromas"),
    ("COL1A1",   -10.36, 19, "ECM",                        "EDS, OI"),
    ("ANKRD11",  -11.16, 17, "transcription",              "KBG syndrome"),
    ("ACAN",     -16.55, 42, "ECM, proteoglycan",          "spondyloepiphyseal dysplasia"),
]
# HHIP is not in Table 1 - reported incidentally at +9.92 cm, P = 3.72e-7 - but it is
# the gene that passed round 285, so it is carried here explicitly and flagged.
EXTRA = [("HHIP", +9.92, None, "hedgehog antagonist (secreted)", "sub-threshold, incidental")]


def word(g):
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(g) + r"(?![A-Za-z0-9])")


def scan_nodes(pat):
    hits = {}
    for dp, _, fs in os.walk(NODES):
        for fn in fs:
            if not fn.endswith(".yaml"):
                continue
            path = os.path.join(dp, fn)
            try:
                txt = open(path, errors="ignore").read()
            except OSError:
                continue
            n = len(pat.findall(txt))
            if n:
                hits[os.path.relpath(path, NODES)] = n
    return hits


def scan_flat(path, pat):
    if not os.path.exists(path):
        return 0
    return len(pat.findall(open(path, errors="ignore").read()))


def main():
    rows = []
    print("%-10s %8s %7s  %-6s %s" % ("gene", "beta_cm", "carriers", "nodes", "where this atlas has already been"))
    print("-" * 108)
    for g, beta, carr, func, omim in GENES + EXTRA:
        pat = word(g)
        nh = scan_nodes(pat)
        bib = scan_flat(BIB, pat)
        gap = scan_flat(GAPS, pat)
        top = sorted(nh.items(), key=lambda kv: -kv[1])[:3]
        where = "; ".join("%s x%d" % (os.path.basename(k)[:-5][:46], v) for k, v in top) or "NOTHING IN GRAPH"
        print("%-10s %+8.2f %7s  %-6d %s" % (g, beta, carr if carr else "-", len(nh), where))
        if bib or gap:
            print("%-10s %8s %7s  %-6s   bibliography x%d, gaps x%d" % ("", "", "", "", bib, gap))
        rows.append({"gene": g, "beta_cm": beta, "carriers": carr, "function": func,
                     "omim": omim, "n_nodes": len(nh), "nodes": nh,
                     "bib_mentions": bib, "gap_mentions": gap})

    print()
    silent = [r["gene"] for r in rows if r["n_nodes"] == 0]
    thin = [r["gene"] for r in rows if 0 < r["n_nodes"] <= 2]
    print("GENES WITH NO NODE IN THIS GRAPH AT ALL (%d): %s" % (len(silent), ", ".join(silent) or "none"))
    print("GENES MENTIONED IN ONLY 1-2 NODES (%d): %s" % (len(thin), ", ".join(thin) or "none"))
    print()
    print("Sorted by |beta| among genes the graph barely holds - these are where the")
    print("largest human effect sizes meet the least atlas coverage:")
    gapset = [r for r in rows if r["n_nodes"] <= 2]
    for r in sorted(gapset, key=lambda r: -abs(r["beta_cm"])):
        print("  %-10s %+7.2f cm  nodes=%d bib=%d  %s | OMIM: %s"
              % (r["gene"], r["beta_cm"], r["n_nodes"], r["bib_mentions"], r["function"], r["omim"]))

    os.makedirs(OUT, exist_ok=True)
    json.dump(rows, open(os.path.join(OUT, "atlas_coverage_of_height_genes.json"), "w"), indent=1)
    print("\nwrote %s" % os.path.join(OUT, "atlas_coverage_of_height_genes.json"))
    print("\nNOTE ON DIRECTION - negative beta genes are NOT dismissible. A gene that costs")
    print("16.55 cm when halved is a gene the plate cares about; the question for those is")
    print("whether the OPPOSITE manipulation - agonism, restoration, overexpression - has")
    print("ever been given a length endpoint. That is a separate search from the pLoF one.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
