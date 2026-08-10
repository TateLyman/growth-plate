#!/usr/bin/env python3
"""GSE9160 - the zone-resolved human growth plate array, read for any gene panel.

WHY THIS EXISTS
---------------
This atlas has twice settled a question about the human growth plate on DROPLET
scRNA-seq detection percentages (GSE288028) and been wrong to, because CORR-114
established on this atlas's own data that droplet absence is UNINTERPRETABLE for
low-abundance secreted and regulatory transcripts: PTHLH sits at 0.43-1.40 % of
cells and GDF5 at 0.20-0.34 %, and both are canonical growth plate factors.

GSE9160 has no dropout. Laser-capture microdissected, zone-resolved Affymetrix
HG-U133 Plus 2.0, FIVE compartments (reserve, proliferative, prehypertrophic,
hypertrophic, perichondrium) from TWO normal children - female 11y10m and male
13y3m - distal femoral growth plate. MAS5, linear, trimmed mean target 100.

CORR-218 exists because KLB was declared absent from human growth plate on the
droplet platform. On this one it is detected in ten of ten samples.

HOW TO READ A NUMBER HERE
-------------------------
The calibrators are fixed and are printed with every run, so a value can be
placed rather than asserted:
    NPPC     4 - 20      the floor. A gene the plate demonstrably does not make.
    PTHLH    7 - 309     a canonical low-abundance paracrine regulator.
    GDF5    31 - 604     a known essential secreted regulator.
    COL2A1  43k - 104k   the tissue identity control.
A gene in the PTHLH/GDF5 band is DETECTED. A gene at the NPPC band is not.
NEITHER TELLS YOU ABOUT PROTEIN, and n = 2 donors is n = 2 donors.

EVERY PROBE SET IS PRINTED SEPARATELY. A gene carried by one probe set out of
three is a cross-hybridisation question, not a finding, and summarising by the
maximum hides exactly that.

Usage:
  python3 gse9160_panel.py --dir <dir with GSE9160_series_matrix.txt.gz and GPL570.txt>
                           [--genes GENE1,GENE2,...]
  GPL570.txt is the GEO platform annotation table (~79 MB) and is NOT committed;
  the series matrix (2 MB) is archived under atlas/data/gse9160/.
"""
import argparse, gzip, os, sys

CALIBRATORS = ["NPPC", "PTHLH", "GDF5", "COL2A1"]
DEFAULT_PANEL = [
    # the CNP axis and its two destruction routes
    "NPPC", "NPR1", "NPR2", "NPR3", "MME", "ECE1", "IDE", "FURIN", "PRKG2", "PDE3A", "OSTN",
    # the endocrine FGF question CORR-218 reopened
    "KLB", "KL", "FGF19", "FGF21", "FGFR1", "FGFR2", "FGFR3", "FGFR4", "FGF18",
    # calibrators and tissue identity
    "PTHLH", "GDF5", "COL2A1", "COL10A1", "ACAN", "IHH", "PECAM1",
]
ZONE_ORDER = ["Reserve", "Proliferative", "Prehypertrophic", "Hypertrophic", "Perichondrium"]


def load(dirpath, panel):
    mat = os.path.join(dirpath, "GSE9160_series_matrix.txt.gz")
    gpl = os.path.join(dirpath, "GPL570.txt")
    for p in (mat, gpl):
        if not os.path.exists(p):
            print(f"MISSING {p}", file=sys.stderr)
            print("  series matrix: atlas/data/gse9160/GSE9160_series_matrix.txt.gz", file=sys.stderr)
            print("  platform:      https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPL570nnn/GPL570/annot/",
                  file=sys.stderr)
            sys.exit(1)

    want, probe2sym = set(panel), {}
    with open(gpl, errors="replace") as f:
        si = None
        for line in f:
            if line.startswith("ID\t"):
                si = line.rstrip("\n").split("\t").index("Gene Symbol"); continue
            if si is None or line[:1] in "!^#":
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) > si and p[si].strip() in want:
                probe2sym[p[0]] = p[si].strip()

    with gzip.open(mat, "rt") as f:
        titles = None
        for line in f:
            if line.startswith("!Sample_title"):
                titles = [x.strip('"') for x in line.rstrip("\n").split("\t")[1:]]
                break
    # GEO titles are "<Zone>, replicate N"; replicate 1 is the female donor
    cols = [(t.split(",")[0].strip(),
             "d1_F_11y10m" if "replicate 1" in t else "d2_M_13y3m") for t in titles]

    vals = {}
    with gzip.open(mat, "rt") as f:
        started = False
        for line in f:
            if line.startswith("!series_matrix_table_begin"):
                started = True; next(f); continue
            if line.startswith("!series_matrix_table_end"):
                break
            if not started:
                continue
            p = line.rstrip("\n").split("\t")
            pid = p[0].strip('"')
            if pid in probe2sym:
                try:
                    vals.setdefault(probe2sym[pid], {})[pid] = [float(x) for x in p[1:]]
                except ValueError:
                    pass
    return cols, vals


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--genes", default=None, help="comma-separated; default is the standing panel")
    a = ap.parse_args()
    panel = [g.strip().upper() for g in a.genes.split(",")] if a.genes else DEFAULT_PANEL
    panel = list(dict.fromkeys(panel + CALIBRATORS))
    cols, vals = load(a.dir, panel)

    donors = ["d1_F_11y10m", "d2_M_13y3m"]
    idx = {d: [i for i, (_, dd) in enumerate(cols) if dd == d] for d in donors}

    print("=" * 108)
    print("GSE9160 - laser-microdissected human distal femoral growth plate, MAS5 linear, "
          "trimmed mean 100")
    print("n = 2 normal children (F 11y10m, M 13y3m) x 5 compartments. EVERY PROBE SET SHOWN "
          "SEPARATELY.")
    print("=" * 108)
    hdr = "  ".join(f"{z[:6]:>7s}" for z in ZONE_ORDER)
    print(f"\n{'gene':<9}{'probe set':<14}  donor            {hdr}")
    print("-" * 108)
    for g in panel:
        if g not in vals:
            print(f"{g:<9}{'-- NO PROBE SET ON GPL570 --':<14}")
            continue
        for pid in sorted(vals[g]):
            for d in donors:
                z = {cols[i][0]: vals[g][pid][i] for i in idx[d]}
                row = "  ".join(f"{z.get(zn, float('nan')):7.0f}" for zn in ZONE_ORDER)
                print(f"{g:<9}{pid:<14}  {d:<15}  {row}")
        print()
    print("-" * 108)
    print("CALIBRATOR BAND, printed every run so any value above can be placed rather than asserted:")
    for c in CALIBRATORS:
        if c in vals:
            flat = [x for pid in vals[c] for x in vals[c][pid]]
            print(f"    {c:<9} {min(flat):9.0f} - {max(flat):9.0f}")
    print("\nA gene inside the PTHLH/GDF5 band is DETECTED on a platform that has no dropout.")
    print("It is NOT thereby present as functional protein, and n = 2 donors is n = 2 donors.")
    print("=" * 108)


if __name__ == "__main__":
    main()
