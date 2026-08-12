# Round 300 setup — the 207-gene target list, extracted

From `kosmicki2026_supp_tables_S1_S29.xlsx`, Table S4 (207 genes, P<1.75e-9, discovery + replication).

- `kosmicki207_genes.txt` — all 207 symbols
- `kosmicki207_NEVER_IN_ATLAS.txt` — **122 of them appear in NO node of this atlas**

85 are already covered. The atlas has been reasoning from the 17 singleton-pLoF genes of Table 1/S5.

## Why this changes rounds 297-298
Both druggability sweeps used a gene set built from the atlas's own ontology plus those 17. The
denominator was wrong. "202 of 298 targets are undrugged" needs recomputing against a set that
includes these 122.

## Read these before trusting any of the 207
- **S12** — genes significant BEFORE but not AFTER conditioning on 3,034 common variants. A built-in
  false-positive filter. Any of the 207 appearing in S12 must be down-graded before use.
- **S7** — ratio of singleton pLoF beta to GWAS beta. The "~52x larger than common variants" figure
  CLAUDE.md carries has only ever been quoted from prose; this is the table behind it.
- **S13** — the six genes where MISSENSE-ONLY burden was the strongest test, and **FGFR3 is one of them**,
  with pLoF and missense reportedly running in OPPOSITE directions. The stack's lead target. Read before
  any further FGFR3 argument.

## First-pass observations on the 122, not yet checked
ABCB1 (P-glycoprotein — drug efflux at the plate would modify EVERY agent in the stack), ADCY6
(adenylate cyclase, directly upstream of the CREB arm round 265 settled discharge on), CPT1A, APOB,
DPP9, ASH1L, ANTXR1, CLEC11A. None verified; listed only as where to look first.

## Order for the next session
1. S12 filter, then S13/FGFR3, then S7.
2. Re-run `round298_druggability_sweep.py` with the 207 added to the gene set.
3. Re-run the CTD signed join over the expanded undrugged list.
4. IMPC length screen (propagate through MPheno_OBO, do not grep the phrase).
5. GSE288028's 14 .h5 matrices against CORR-296.
