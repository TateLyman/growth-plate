#!/usr/bin/env python3
"""
GSE252289 - HUMAN CHONDROCYTE ATAC-seq, AND THE AXIAL SHEETS NOBODY OPENED.

Operator-supplied 2026-08-13 as part of the ten-dataset drop. The atlas registered it as
"89 ATAC-seq" and used it for nothing. The workbook has 34 sheets. Thirty-two are appendicular.
TWO ARE LABELLED **LUMBAR** AND **THORACIC** - human VERTEBRAL chondrocyte open chromatin,
60,161 and 61,220 peaks, from three specimens (E72 x2, E74).

WHY THAT MATTERS MORE THAN ANY OTHER UNOPENED FILE HERE. The single most decision-relevant
compartment fact in CLAUDE.md is that at this bone age the residual is TRUNK-dominant - knees
0.3-0.4 cm against trunk 6.5-9.0 cm - while every agent in the stack was characterised on LONG
BONES. Round 318 answered the compartment question from GWAS (common-variant lead alleles, SD
units, 546k people). This answers it from HUMAN TISSUE, in the regulatory layer, and the two
methods share no data and no assumptions.

THE BUILD WAS DETERMINED, NOT ASSUMED. GEO does not state it. Testing six landmark TSSs
against the peak sets: GRCh37 6/6, GRCh38 2/6. Everything below is GRCh37/hg19.

THE CONFOUNDS, ALL THREE, WRITTEN BEFORE THE RESULT.
  1. STAGE. Axial samples are E72/E74; appendicular are E54 and E67. Site is confounded with
     age. The E67 set is used for the primary contrast because it is closest, and the E54 set
     is carried as a second appendicular reference - a gene called axial-enriched against both
     appendicular stages is less likely to be an age effect.
  2. DEPTH. The axial sheets carry roughly twice the peaks of the E67 appendicular sheets, so
     raw overlap counts are not comparable. Every score below is peak base-pairs in the window
     divided by that sheet's TOTAL peak base-pairs. Depth cancels in the ratio.
  3. FETAL. E54-E74 is first/early-second trimester. This is a claim about which regulatory
     landscape a vertebral chondrocyte builds, not about a bone-age-16 growth plate.
     CLAUDE.md quarantines fetal skeletal-stem-cell data from postnatal inference and that
     quarantine applies here too.

THE CONTROLS DECIDE WHETHER THE READ IS WORTH ANYTHING, and they are chosen so that the
answer is known in advance from developmental biology, not from this atlas:
  MUST be APPENDICULAR - TBX5 (forelimb identity), TBX4 and PITX1 (hindlimb identity),
    HOXA13/HOXD13 (autopod), SHOX2 (proximal limb).
  MUST be AXIAL       - PAX1 and PAX9 (sclerotome), NKX3-2/BAPX1 (sclerotome-to-cartilage),
    MEOX1, UNCX, TBX6 (presomitic mesoderm), FOXD3-independent axial markers.
  MUST be NEITHER     - ACTB, GAPDH, RPL13A, B2M (housekeeping), and the pan-chondrocyte
    programme COL2A1, ACAN, SOX9, COL9A1 - which is CORR-311's rule that the negative control
    is rows you already have.
If the limb-identity genes do not separate, nothing else in the output is readable.

Usage: python3 analysis.py
"""
import gzip
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..")
PEAKS = os.path.join(ROOT, "data", "round323", "gse252289_peaks.json")
GTF = os.environ.get("GRCH37_GTF", "")

AXIAL = ["LUMBAR", "THORACIC"]
APP67 = ["DistFemur_67", "DistHumerus_67", "DistRadius_67", "DistTibia_67",
         "ProxFemur_67", "ProxHumerus_67", "ProxRadius_67", "ProxTibia_67"]
APP54 = ["DistFemur_54", "DistHumerus_54", "DistRadius_54", "DistTibia_54",
         "ProxFemur_54", "ProxHumerus_54", "ProxRadius_54", "ProxTibia_54"]

FLANK = 100000


def load_peaks():
    return json.load(open(PEAKS))


def build_index(peaks):
    """{sheet: {chrom: sorted [(start,end)]}} plus total bp per sheet."""
    idx, tot = {}, {}
    for sheet, rows in peaks.items():
        d = {}
        t = 0
        for ch, a, b in rows:
            d.setdefault(ch, []).append((a, b))
            t += b - a
        for ch in d:
            d[ch].sort()
        idx[sheet] = d
        tot[sheet] = t
    return idx, tot


def covered_bp(idx_sheet, ch, lo, hi):
    """Base pairs of peak inside [lo,hi]. Peaks within a sheet are non-overlapping."""
    arr = idx_sheet.get(ch)
    if not arr:
        return 0
    import bisect
    i = bisect.bisect_left(arr, (lo - 10 ** 7, 0))
    s = 0
    for a, b in arr[i:]:
        if a > hi:
            break
        if b < lo:
            continue
        s += min(b, hi) - max(a, lo)
    return s


def load_genes(gtf):
    """{symbol: (chrom, start, end)} for protein-coding + lincRNA genes, GRCh37."""
    genes = {}
    op = gzip.open if gtf.endswith(".gz") else open
    with op(gtf, "rt") as f:
        for line in f:
            if line[0] == "#":
                continue
            p = line.split("\t")
            if p[2] != "gene":
                continue
            attr = p[8]
            if 'gene_name "' not in attr:
                continue
            sym = attr.split('gene_name "')[1].split('"')[0]
            ch = "chr" + p[0]
            if len(p[0]) > 5:
                continue
            st, en = int(p[3]), int(p[4])
            prev = genes.get(sym)
            if prev is None or (en - st) > (prev[2] - prev[1]):
                genes[sym] = (ch, st, en)
    return genes


def score(idx, tot, ch, lo, hi, sheets):
    """mean normalised peak density over sheets, per million total peak bp."""
    vals = [covered_bp(idx[s], ch, lo, hi) / float(tot[s]) * 1e6 for s in sheets]
    return sum(vals) / len(vals)


def main():
    peaks = load_peaks()
    idx, tot = build_index(peaks)
    print("sheets %d; axial total peak bp %s; E67 appendicular mean %s"
          % (len(peaks), sum(tot[s] for s in AXIAL) // 2,
             sum(tot[s] for s in APP67) // len(APP67)))
    if not GTF or not os.path.exists(GTF):
        print("set GRCH37_GTF to an Ensembl GRCh37 gtf(.gz)", file=sys.stderr)
        return 1
    genes = load_genes(GTF)
    print("loaded %d GRCh37 gene symbols" % len(genes))
    return dict(idx=idx, tot=tot, genes=genes)


if __name__ == "__main__":
    main()
