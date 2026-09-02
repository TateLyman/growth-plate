#!/usr/bin/env python3
"""
cnp_source_bulk.py - DOES THE HUMAN GROWTH PLATE TRANSCRIBE ITS OWN CNP?

THE QUESTION AND WHY IT DECIDES A DRUG CHOICE
---------------------------------------------
g_l12_does_the_human_plate_produce_its_own_cnp. Two routes out of the CNP dose ceiling
identified in thread_3_the_dose_ceiling_is_a_systemic_safety_margin are decided in
OPPOSITE directions by this one fact:

  If the plate is a CONSUMER of circulating CNP, a cartilage-TARGETED LIGAND is worth
  most - it raises plate concentration at fixed systemic Cmax, which is the quantity the
  cardiovascular safety margin is denominated in.

  If the plate is a PRODUCER, an NPR2 POSITIVE ALLOSTERIC MODULATOR is worth most -
  a PAM amplifies wherever ligand meets receptor, so it is growth-plate-selective only
  if local ligand exceeds vascular ligand. (npr2_positive_allosteric_modulation)

WHY THIS SCRIPT EXISTS RATHER THAN THE scRNA-seq ONE
----------------------------------------------------
cnp_zonal_system.py asked this of GSE288028 droplet data and THE TEST WAS VOID -
CORR-114. NPPC came back at the detection floor, but so did PTHLH (0.43-1.40% of cells)
and GDF5 (0.20-0.34%), and PTHrP is the canonical growth-plate paracrine factor. Droplet
scRNA-seq cannot resolve low-abundance secreted-ligand transcripts, so absence there is
uninformative. Round 98 had already drawn an inference from the same NPPC 0/4-donor
result; that inference inherits the same defect.

GSE9160 has no dropout. It is laser-capture microdissected, zone-resolved Affymetrix
HG-U133 Plus 2.0 (GPL570) profiling of DISTAL FEMORAL GROWTH PLATE from TWO NORMAL
CHILDREN - female 11y10m and male 13y3m - across five compartments: reserve,
proliferative, prehypertrophic, hypertrophic AND PERICHONDRIUM. The perichondrium arm
matters specifically: the atlas's own alternative hypothesis, recorded in
the_cnp_axis_mapped_end_to_end, is that CNP may reach the plate from endothelium,
perichondrium or circulation rather than from chondrocytes.

Values are MAS5 signal, global-scaled to a trimmed mean target intensity of 100, on a
LINEAR scale. Present/absent calls are not in the series matrix, so the background is
established empirically from negative controls instead - which is the point.

PRE-REGISTERED READING, FIXED BEFORE ANY VALUE WAS EXTRACTED
------------------------------------------------------------
NEGATIVE CONTROLS  NPPA, NPPB - cardiac natriuretic peptides, expected at array
                   background in cartilage. They define the floor.
LOW CALIBRATORS    PTHLH, GDF5 - essential secreted growth-plate regulators that sat at
                   the droplet floor in GSE288028. They define "genuinely present but
                   low-abundance" on this platform.
HIGH CONTROLS      COL2A1, COL10A1, ACAN - must be very high or the assay is not reading
                   growth plate.

  NPPC at or below the NPPA/NPPB background  => the plate does NOT transcribe NPPC.
                                                CONSUMER. Favours a targeted ligand.
  NPPC at or above PTHLH/GDF5                => the plate DOES transcribe NPPC and the
                                                scRNA-seq absence was dropout.
                                                PRODUCER. Favours a PAM.
  NPPC concentrated in PERICHONDRIUM rather than in the chondrocyte zones
                                             => supports the atlas's own alternative
                                                source hypothesis, and is a third answer
                                                distinct from both of the above.

LIMITS, STATED BEFORE THE NUMBERS
---------------------------------
n = 2 DONORS. This cannot establish a population value and no statistics are computed;
per-donor values are printed and any claim must survive being read as two anecdotes.
Transcript is not protein, and for a secreted rapidly-degraded peptide the gap between
them is larger than usual. Microarray probes can cross-hybridise and can miss isoforms;
where a gene has several probe sets on GPL570 all of them are printed rather than
averaged, because disagreement between probe sets for the same gene is itself a warning.
The donors came to epiphysiodesis, i.e. they are not a random sample of children.

Usage:
  python3 atlas/tools/cnp_source_bulk.py --dir <dir with GSE9160_series_matrix.txt.gz and GPL570.txt>
"""
from __future__ import annotations
import argparse, gzip, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

NEG_CONTROL = ["NPPA", "NPPB"]
LOW_CALIB   = ["PTHLH", "GDF5"]
HIGH_CTRL   = ["COL2A1", "COL10A1", "ACAN"]
TARGETS     = ["NPPC", "NPR2", "NPR3", "MME", "FURIN"]
EXTRA       = ["IHH", "FGFR3", "PECAM1"]
PANEL = TARGETS + LOW_CALIB + NEG_CONTROL + HIGH_CTRL + EXTRA

ZONES = ["Reserve", "Proliferative", "Prehypertrophic", "Hypertrophic", "Perichondrium"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    a = ap.parse_args()

    mat = os.path.join(a.dir, "GSE9160_series_matrix.txt.gz")
    gpl = os.path.join(a.dir, "GPL570.txt")
    for p in (mat, gpl):
        if not os.path.exists(p):
            print(f"MISSING {p}", file=sys.stderr)
            return 1

    # probe -> gene symbol, keeping every probe set for a wanted gene
    want = set(PANEL)
    probe2sym = {}
    with open(gpl, "r", errors="replace") as f:
        hdr = None
        for line in f:
            if line.startswith("ID\t"):
                hdr = line.rstrip("\n").split("\t")
                si = hdr.index("Gene Symbol")
                continue
            if hdr is None or line.startswith("!") or line.startswith("^") or line.startswith("#"):
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) <= si:
                continue
            sym = p[si].strip()
            if sym in want:
                probe2sym[p[0]] = sym

    # sample order and titles
    titles, accs = None, None
    with gzip.open(mat, "rt") as f:
        for line in f:
            if line.startswith("!Sample_title"):
                titles = [x.strip('"') for x in line.rstrip("\n").split("\t")[1:]]
            elif line.startswith("!Sample_geo_accession"):
                accs = [x.strip('"') for x in line.rstrip("\n").split("\t")[1:]]
            if titles and accs:
                break
    # column index -> (zone, donor)
    cols = []
    for t in titles:
        zone = t.split(",")[0].strip()
        rep = "donor1_F_11y10m" if "replicate 1" in t else "donor2_M_13y3m"
        cols.append((zone, rep))

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

    donors = ["donor1_F_11y10m", "donor2_M_13y3m"]
    out = {}
    print("\nGSE9160 - MAS5 signal, linear scale, trimmed mean target 100")
    print("Laser-microdissected human distal femoral growth plate, n=2 donors\n")

    def block(title, genes):
        print(f"\n=== {title} ===")
        for g in genes:
            if g not in vals:
                print(f"  {g:8} NO PROBE SET FOUND ON GPL570")
                continue
            for pid, v in sorted(vals[g].items()):
                for dn in donors:
                    row = f"  {g:8} {pid:14} {dn:16}"
                    for z in ZONES:
                        try:
                            i = cols.index((z, dn))
                            row += f"{v[i]:10.1f}"
                        except ValueError:
                            row += f"{'--':>10}"
                    print(row)
                    out.setdefault(g, {}).setdefault(pid, {})[dn] = {
                        z: (v[cols.index((z, dn))] if (z, dn) in cols else None) for z in ZONES}

    print(f"  {'gene':8} {'probe':14} {'donor':16}" + "".join(f"{z[:9]:>10}" for z in ZONES))
    block("NEGATIVE CONTROLS - these define the array background", NEG_CONTROL)
    block("LOW-ABUNDANCE CALIBRATORS - genuinely present, at the droplet floor", LOW_CALIB)
    block("THE QUESTION", ["NPPC"])
    block("THE REST OF THE LOCAL CNP SYSTEM", ["NPR2", "NPR3", "MME", "FURIN"])
    block("CONTEXT", EXTRA)
    block("HIGH CONTROLS - assay sanity", HIGH_CTRL)

    op = os.path.join(ROOT, "query", "cnp_source_bulk.json")
    json.dump(out, open(op, "w"), indent=1)
    print("\nwrote", op)

    # summary against the pre-registered thresholds
    def gmax(g):
        if g not in vals:
            return None
        return max(max(v) for v in vals[g].values())
    print("\n\nAGAINST THE PRE-REGISTERED THRESHOLDS (max signal across all zones/donors)")
    for g in NEG_CONTROL + LOW_CALIB + ["NPPC"] + ["NPR2", "NPR3", "MME"] + HIGH_CTRL:
        m = gmax(g)
        print(f"  {g:8} {'no probe' if m is None else f'{m:10.1f}'}")
    neg = [gmax(g) for g in NEG_CONTROL if gmax(g) is not None]
    low = [gmax(g) for g in LOW_CALIB if gmax(g) is not None]
    npc = gmax("NPPC")
    if neg and low and npc is not None:
        print(f"\n  negative-control ceiling  = {max(neg):.1f}")
        print(f"  low-calibrator floor      = {min(low):.1f}")
        print(f"  NPPC max                  = {npc:.1f}")
        if npc <= max(neg):
            print("  => NPPC AT OR BELOW BACKGROUND. Pre-registered reading: CONSUMER.")
        elif npc >= min(low):
            print("  => NPPC AT OR ABOVE THE LOW CALIBRATORS. Pre-registered reading: PRODUCER,")
            print("     and the scRNA-seq absence was dropout.")
        else:
            print("  => NPPC BETWEEN BACKGROUND AND CALIBRATORS. THE PRE-REGISTERED READING DOES")
            print("     NOT RESOLVE IT; report as indeterminate rather than picking a side.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
