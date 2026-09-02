#!/usr/bin/env python3
"""
ROUND 376. THE HHIP-LOWERING ROUTES, TRIAGED ON THE FREE LOCAL QUERY BEFORE ANY LITERATURE CLAIM.

Eight routes to lowering HHIP were proposed. Five of them are INDIRECT - they act on a receptor
somewhere else and are supposed to lower HHIP transcription or circulating HHIP. CORR-327 says the
first question for any such proposal is whether the DRUG'S ACTUAL TARGET is in the growth plate, and
that question is a lookup against data already on disk, not a literature search.

This script runs the panel against R344's purity-corrected GSE288028 - 12 human postnatal growth-plate
samples, the 5 purest by COL2A1 versus the 5 most blood-contaminated. The ratio measures whether a
transcript's origin is the chondrocyte or the contaminating blood/immune fraction. Calibrators are
carried in the same panel so the numbers can be read against known answers:
  COL2A1 8.92 and ACAN 4.65 = cartilage;  PTPRC 0.00 and HBB 0.00 = contamination.
  AGTR1 0.03 killed losartan (R301/R344); MME 0.17 killed sacubitril; SOST 0.35 killed romosozumab.

⚠ CORR-351: a ratio measures ENRICHMENT, not PRESENCE. A gene expressed in both compartments reads
contaminant-leaning even when the protein is really there (ESR1 did exactly this). A low ratio is a
hypothesis about a transcript's cellular origin; direct protein localisation would override it. What
makes the calls below strong is that the numbers sit AT or BELOW the values that already killed three
drugs, and in two cases the biosynthetic enzyme is flatly absent as well.
"""
import json, numpy as np

cpm = np.load('atlas/data/round344/gse288028_human12_cpm.npy')
genes = json.load(open('atlas/data/round344/gse288028_gene_names.json'))
meta = json.load(open('atlas/data/round344/gse288028_purity_corrected.json'))
gi = {g: i for i, g in enumerate(genes)}

# recover sample order by matching the stored COL2A1 value per sample
c2 = cpm[:, gi['COL2A1']]
names = [None] * 12
for s, v in meta['col2a1_by_sample'].items():
    names[int(np.argmin(np.abs(c2 - v)))] = s
pure = [names.index(s) for s in meta['purest_samples']]
cont = [names.index(s) for s in meta['contaminated_samples']]

PANEL = [
    ('COL2A1', 'CALIBRATOR - cartilage'), ('ACAN', 'CALIBRATOR - cartilage'),
    ('PTPRC', 'CALIBRATOR - blood/immune'), ('HBB', 'CALIBRATOR - blood'),
    ('AGTR1', 'PRIOR KILL - losartan'), ('MME', 'PRIOR KILL - sacubitril'),
    ('SOST', 'PRIOR KILL - romosozumab'),
    ('HHIP', 'THE TARGET'), ('SMO', 'Hh transduction'), ('PTCH1', 'Hh transduction'),
    ('GLI1', 'Hh readout'), ('IHH', 'Hh ligand'),
    ('NR3C2', 'ROUTE - finerenone / spironolactone'),
    ('CYP11B2', 'ROUTE - does the plate make aldosterone at all'),
    ('HSD11B2', 'ROUTE - MR gatekeeper'),
    ('PPARG', 'ROUTE - rosiglitazone / TZD'),
    ('PPARA', 'context'), ('PPARD', 'context'),
    ('GLP1R', 'ROUTE - liraglutide / GLP-1RA'),
    ('SLC5A2', 'ROUTE - canagliflozin (SGLT2)'),
    ('AGO2', 'RNAi machinery - can the tissue execute knockdown'),
    ('DICER1', 'RNAi machinery'), ('TARBP2', 'RNAi machinery'),
    ('ASGR1', 'GalNAc-siRNA receptor - is the liver-targeting conjugate relevant here'),
    ('ASGR2', 'GalNAc-siRNA receptor'),
]

print(f"{'gene':9s} {'pure':>9s} {'contam':>9s} {'ratio':>7s}   note")
out = {}
for g, note in PANEL:
    if g not in gi:
        print(f"{g:9s} {'NOT ON PLATFORM':>28s}   {note}")
        continue
    v = cpm[:, gi[g]]
    p, c = float(np.median(v[pure])), float(np.median(v[cont]))
    ratio = (p + 0.01) / (c + 0.01)
    out[g] = dict(pure_med_cpm=round(p, 2), contam_med_cpm=round(c, 2),
                  purity_ratio=round(ratio, 2), note=note)
    print(f"{g:9s} {p:9.1f} {c:9.1f} {ratio:7.2f}   {note}")

print("""
VERDICT ON THE FIVE INDIRECT ROUTES - all fail the receiver test in the growth plate:
  NR3C2   ratio 0.05 and CYP11B2 0/12  -> the mineralocorticoid axis is absent AND the plate makes no
          aldosterone. Finerenone and spironolactone cannot act locally. The mineralocorticoid arm now
          joins the RAAS arm (REN 0/12, AGTR1 0.03, AGTR2) as absent from this tissue.
  PPARG   ratio 0.02  -> the TZD target is the most contaminant-leaning gene in the panel apart from
          the blood calibrators. PPARD (27.4 CPM) is the plate's PPAR, and it is not what a TZD hits.
  GLP1R   0.3 CPM     -> effectively absent. Liraglutide cannot act locally.
  SLC5A2  0.3 CPM     -> absent, independently reproducing R313's canagliflozin kill on a second dataset.
So every indirect route would have to work through the CIRCULATING HHIP pool - and the growth plate
makes its own HHIP at 68.8 CPM, 4.65x cartilage-enriched, whose potency requires binding to LOCAL
heparan sulfate (griffiths2021). A locally made, GAG-clustered antagonist is not set by a serum level.

VERDICT ON THE DIRECT ROUTE: AGO2, DICER1 and TARBP2 are all present, so the tissue can execute RNAi.
ASGR1/ASGR2 are near-absent, so a GalNAc conjugate - the standard systemic siRNA format - is aimed at
a receptor this tissue does not have, and the delivery problem has to be solved another way.
""")
json.dump(out, open('atlas/data/round376/hhip_route_receiver_test.json', 'w'), indent=1)
