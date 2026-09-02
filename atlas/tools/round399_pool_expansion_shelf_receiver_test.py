#!/usr/bin/env python3
"""
R399 - THE STEM-CELL-EXPANSION PHARMACOPOEIA HAS NEVER BEEN ASKED.

CLAUDE.md's answer to "what is missing" is: nothing in the stack refills the pool.
Every pool candidate this file has ever worked (HHIP, SPIN4, SMOC1, STC2, CHAD,
CLEC3A, ECRG4) was reached from HEIGHT GENETICS and has no molecule.

⭐ BUT THERE IS AN ENTIRE FIELD WHOSE EXPLICIT PURPOSE IS EXPANDING A STEM CELL POOL,
   WITH APPROVED AND CLINICAL-STAGE MOLECULES, AND THIS ATLAS HAS ZERO COVERAGE OF IT.
   Grep, 2026-08-14:  UM171 0 files · "aryl hydrocarbon" 0 · StemRegenin 0 ·
   omidubicel 0 · "stem cell expansion" 0 · CoREST 0 · "gamma secretase" 0 ·
   nirogacestat 0 · jagged 0 · "prostaglandin E2" 0 · sprifermin 0.

This runs CORR-327's receiver test on every target of that shelf against the
purity-corrected human postnatal growth plate BEFORE any literature search, so that
nothing gets proposed into a tissue that does not carry it.
"""
import json, sys
import numpy as np

CPM = 'atlas/data/round344/gse288028_human12_cpm.npy'
GEN = 'atlas/data/round344/gse288028_gene_names.json'
PUR = 'atlas/data/round344/gse288028_purity_corrected.json'

cpm = np.load(CPM)
genes = json.load(open(GEN))
meta = json.load(open(PUR))
if isinstance(genes, dict):
    genes = genes.get('genes', genes.get('gene_names'))
genes = [g.upper() for g in genes]
idx = {g: i for i, g in enumerate(genes)}

# purity split, exactly as R344 defined it
col = meta['col2a1_by_sample']
if isinstance(col, dict):
    order = list(col)
    vals = [col[k] for k in order]
else:
    order = list(range(len(col)))
    vals = list(col)
rank = np.argsort(vals)[::-1]
pure_i = list(rank[:5])
cont_i = list(rank[-5:])

def row(sym):
    i = idx.get(sym.upper())
    if i is None:
        return None
    p = float(np.median(cpm[pure_i, i]))
    c = float(np.median(cpm[cont_i, i]))
    r = (p + 0.01) / (c + 0.01)
    det = int((cpm[:, i] > 0).sum())
    return p, c, r, det

PANEL = [
    # --- calibrators, so the reader can place every number ---
    ('COL2A1',  'CALIBRATOR - cartilage'),
    ('ACAN',    'CALIBRATOR - cartilage'),
    ('PTPRC',   'CALIBRATOR - immune contaminant'),
    ('HBB',     'CALIBRATOR - blood contaminant'),
    ('AGTR1',   'CALIBRATOR - the ratio that killed losartan'),
    ('MME',     'CALIBRATOR - the ratio that killed sacubitril'),
    ('SOST',    'CALIBRATOR - the absence that killed romosozumab'),

    # --- 1. THE HSC-EXPANSION SHELF (zero atlas coverage) ---
    ('AHR',     'SR1 / StemRegenin-1 target - THE canonical HSC expander'),
    ('ARNT',    'AhR dimerisation partner'),
    ('CYP1B1',  'AhR output - reports whether the pathway is ON'),
    ('CYP1A1',  'AhR output'),
    ('AHRR',    'AhR repressor - second output gene'),
    ('RCOR1',   'CoREST - the UM171 target complex'),
    ('KDM1A',   'LSD1, in the CoREST complex; UM171 degrades it'),
    ('RNF220',  'UM171 acts through a CRL3-KBTBD4 mechanism on CoREST'),
    ('KBTBD4',  'the E3 substrate receptor UM171 hijacks'),
    ('NAMPT',   'nicotinamide route - omidubicel is APPROVED on this mechanism'),
    ('NNMT',    'the plate methyl sink - R347 says nicotinamide loads it'),

    # --- 2. NOTCH, and its approved drug class (gamma-secretase, 0 coverage) ---
    ('NOTCH1',  'Notch receptor'),
    ('NOTCH2',  'Notch receptor - Hajdu-Cheney GoF is short stature'),
    ('NOTCH3',  'Notch receptor'),
    ('RBPJ',    'the obligate Notch TF - Rbpj deletion RAISES proliferation (mead2009)'),
    ('HES1',    'Notch output'),
    ('HEY1',    'Notch output'),
    ('JAG1',    'ligand - Alagille gene'),
    ('DLL1',    'ligand'),
    ('PSEN1',   'gamma-secretase catalytic - NIROGACESTAT target, APPROVED 2023'),
    ('PSEN2',   'gamma-secretase catalytic'),
    ('NCSTN',   'nicastrin - gamma-secretase'),
    ('APH1A',   'gamma-secretase'),
    ('PSENEN',  'gamma-secretase'),

    # --- 3. PROSTAGLANDIN E2 / EP4 - dmPGE2 expands HSCs; EP4 agonists exist for bone ---
    ('PTGER4',  'EP4 - Gs-coupled; EVATANEPAG was built for FRACTURE HEALING'),
    ('PTGER2',  'EP2'),
    ('PTGES',   'PGE synthase - can the plate MAKE PGE2?'),
    ('PTGS1',   'COX-1 - R306 says this is the plate COX'),
    ('PTGS2',   'COX-2'),
    ('PTGER1',  'EP1'),
    ('PTGER3',  'EP3 - Gi'),

    # --- 4. other stem-cell-maintenance handles never asked here ---
    ('MTOR',    'the second niche regulator (newton2019) - no activator exists'),
    ('EZH2',    'contraindicated, included as an internal control'),
    ('SIRT1',   'never asked'),
    ('FOXO1',   'quiescence TF, never asked'),
    ('FOXO3',   'quiescence TF, never asked'),
    ('CDKN1A',  'p21 - quiescence enforcement'),
    ('CDKN1B',  'p27'),
    ('CDKN2A',  'p16 - R266 says plate senescence is NOT this'),
    ('MTNR1A',  'melatonin receptor 1 - OTC agonist exists'),
    ('MTNR1B',  'melatonin receptor 2'),
    ('ASMT',    'does the plate make melatonin?'),
    ('FGFR3',   'reference - erdafitinib target'),
    ('NT5E',    'CD73 - the resting-zone stem cell marker'),
    ('PTHLH',   'PTHrP - the other resting-zone marker'),
]

print("=" * 98)
print("R399  CORR-327 RECEIVER TEST ON THE POOL-EXPANSION SHELF")
print("      purity-corrected human postnatal growth plate (GSE288028, 5 purest vs 5 most contaminated)")
print("=" * 98)
print(f"{'gene':<10}{'pure':>10}{'contam':>10}{'ratio':>9}{'det/12':>8}  note")
print("-" * 98)
missing = []
for sym, note in PANEL:
    r = row(sym)
    if r is None:
        missing.append(sym)
        print(f"{sym:<10}{'--':>10}{'--':>10}{'--':>9}{'--':>8}  NOT ON PLATFORM")
        continue
    p, c, ratio, det = r
    flag = ''
    if ratio >= 2.0 and p >= 5:
        flag = ' <-- CARTILAGE-ENRICHED'
    elif ratio < 0.5:
        flag = ' <-- contaminant-leaning'
    print(f"{sym:<10}{p:>10.1f}{c:>10.1f}{ratio:>9.2f}{det:>8}  {note}{flag}")

print("-" * 98)
print("""
READING RULE (CORR-351): the ratio measures where a transcript ORIGINATES, not whether
the protein is present. A low ratio is a hypothesis about cellular origin. It correctly
killed AGTR1 (0.03) and MME (0.17); it was WRONG about ESR1, whose protein is in 64% of
resting and proliferative chondrocytes by immunohistochemistry in 16 boys.
""")
if missing:
    print("not on platform:", ", ".join(missing))
