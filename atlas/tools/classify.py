"""Hand classification of the 45 genes that cleared the overgrowth screen.

Written by reading each gene's disease terms and drug mechanisms, not by keyword rule. The
classes are about WHY the person is tall, because that decides whether the gene is a lead.
"""
import csv, json, os

CLASS = {
    # PI3K/AKT/mTOR: segmental/mosaic overgrowth. Tall or asymmetrically large, with cancer
    # predisposition. The drugs are oncology inhibitors and the overgrowth allele is GAIN of
    # function, so the drugs run the WRONG WAY for height.
    **{g: "pi3k_mtor_segmental" for g in
       ("PIK3CA", "MTOR", "AKT1", "AKT2", "AKT3", "PIK3R1", "PIK3R2", "FKBP1A", "KRAS",
        "IDH1", "IDH2", "ABL1", "PDGFRB")},
    # Chromatin/epigenetic overgrowth: tall WITH intellectual disability and tumour risk.
    **{g: "chromatin_syndromic" for g in ("DNMT3A", "EZH2", "DNMT1", "NSD1", "CHD8", "NFIX")},
    # Marfanoid connective tissue: tall by dolichostenomelia - a structural fibrillin/collagen
    # defect making limbs long - not by a growth plate that runs faster or longer. The drugs
    # here (losartan, beta blockers) are aortic-root protection, nothing to do with height.
    **{g: "connective_tissue" for g in
       ("TGFBR1", "TGFBR2", "TGFB2", "TGFB3", "FBN1", "SKI", "COL1A2", "COL2A1", "COL3A1",
        "COL5A1", "COL5A2", "COL11A1", "FLNA", "AGTR1", "ADRB2", "NOTCH1", "EFEMP1", "MYLK",
        "SLC2A10", "PROS1")},
    # GH/IGF endocrine drive. Real height effect, well known, and every drug listed is an
    # ACROMEGALY drug - i.e. built to reduce growth, the opposite direction.
    **{g: "gh_igf_endocrine" for g in ("GHR", "SSTR2", "IGF2", "GH1", "GPR101", "AIP")},
    # Imprinted-locus overgrowth (Beckwith-Wiedemann): not a druggable mechanism.
    **{g: "imprinted_locus" for g in ("KCNQ1", "CDKN1C", "H19")},
    # Insulin-secretion overgrowth: ABCC8 loss of function causes congenital hyperinsulinism
    # and FETAL macrosomia. The growth is insulin acting as a fetal growth factor, not
    # postnatal linear growth, and the direction that would mimic it is hypoglycaemia.
    "ABCC8": "insulin_secretion",
    "SCN4A": "unclear_probably_noise",
    # The genuine growth plate axis - and all three are already the target of an existing or
    # trialled programme, which is the finding.
    "NPR2": "growth_plate_kinetic",
    "FGFR3": "growth_plate_kinetic",
    "ESR1": "fusion_timing",
    "LEPR": "growth_plate_kinetic",
}

p = '/home/user/growth-plate/query/overgrowth_screen/targets.csv'
rows = list(csv.DictReader(open(p)))
n = 0
for r in rows:
    c = CLASS.get(r["gene"])
    if c and r["n_known_drugs"] not in ("",):
        r["mechanism_class"] = c
        n += 1
with open(p, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

triple = [r for r in rows if r["n_known_drugs"] not in ("",) and int(r["n_known_drugs"]) > 0]
from collections import Counter
c = Counter(r["mechanism_class"] or "UNCLASSIFIED" for r in triple)
print(f"classified {n} rows; {len(triple)} genes clear all three conditions\n")
for k, v in c.most_common():
    print(f"  {v:3d}  {k}")
print("\ngrowth-plate / fusion-timing genes:")
for r in triple:
    if r["mechanism_class"] in ("growth_plate_kinetic", "fusion_timing"):
        print(f"  {r['gene']:8s} assoc={r['best_assoc_score']:>6s} atlas={r['in_atlas'] or '-'}")
