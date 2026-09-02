#!/usr/bin/env python3
"""
R486 step 1 - extract saxena2022's own deposited DESeq2 output.

SOURCE: Zenodo 10.5281/zenodo.5123384, "Analysis code and additional data
associated with the manuscript entitled 'Interspecies transcriptome analyses
identify genes that control the development and evolution of limb skeletal
proportion'", deposited 2021-07-22, downloaded and unzipped 2026-09-02.
23.72 MB.  This is saxena2022's (PMID 34793695) own data, never opened by
this atlas.

DESIGN, from the deposited README verbatim: STAR GeneCounts for metatarsal
(MT) and radius/ulna (RU) in mouse and jerboa at POSTNATAL DAY 5, with a
PRIMARY analysis at n=3 and an INDEPENDENT VALIDATION analysis at n=2.
Two DESeq2 contrasts per cohort:
    Jerboa:Mouse in the METATARSAL   - the element whose proportion differs
    Jerboa:Mouse in the RADIUS/ULNA  - the internal control element
Positive log2FoldChange = HIGHER IN JERBOA.

WHY THE INTERACTION IS THE SIGNAL.  A gene that differs between the species
in BOTH elements is a species difference, not a proportion difference.  The
quantity that carries proportion is the DIFFERENCE OF THE TWO LOG FOLD
CHANGES, MT minus RU - the species x element interaction.  That is
saxena2022's own logic and it is what this extraction preserves.

Writes a flat TSV so every later query is a lookup rather than a re-parse.
"""
import openpyxl, os, csv

SRC = '/tmp/saxdata/Zenodo_Saxena_etal_2021_AdditionalData_AnalysisCode/Additional Data Tables_1to3.xlsx'
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'round486')

SHEETS = {'n3': '1. ALL_DESEQ2_RESULTS_n=3', 'n2': '2. ALL_DESEQ2_RESULTS_n=2'}
# Row 4 is the header; MT block starts col2, RU block starts col9 (0-based)
COLS = ['baseMean', 'log2FoldChange', 'lfcSE', 'stat', 'pvalue', 'padj']


def num(v):
    if v is None: return None
    s = str(v).strip()
    if s in ('', 'NA', 'NaN', 'nan'): return None
    try: return float(s)
    except ValueError: return None


def main():
    os.makedirs(OUT, exist_ok=True)
    wb = openpyxl.load_workbook(SRC, read_only=True, data_only=True)
    for tag, sheet in SHEETS.items():
        ws = wb[sheet]
        rows = []
        for i, r in enumerate(ws.iter_rows(min_row=5, values_only=True)):
            tid, sym = r[0], r[1]
            if tid is None: continue
            rec = {'transcript': str(tid).strip(), 'symbol': (str(sym).strip() if sym else '')}
            for j, c in enumerate(COLS):
                rec['MT_' + c] = num(r[2 + j])
                rec['RU_' + c] = num(r[9 + j])
            # the interaction: species x element
            if rec['MT_log2FoldChange'] is not None and rec['RU_log2FoldChange'] is not None:
                rec['interaction_MT_minus_RU'] = rec['MT_log2FoldChange'] - rec['RU_log2FoldChange']
            else:
                rec['interaction_MT_minus_RU'] = None
            rows.append(rec)
        path = os.path.join(OUT, f'saxena_deseq2_{tag}.tsv')
        with open(path, 'w', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter='\t')
            w.writeheader()
            w.writerows(rows)
        named = sum(1 for r in rows if r['symbol'])
        print(f'{tag}: {len(rows)} orthologues, {named} with a gene symbol -> {path}')


if __name__ == '__main__':
    main()
