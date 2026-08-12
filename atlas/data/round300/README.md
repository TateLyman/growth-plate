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

## S13 READ — FGFR3's human height signal is MISSENSE-ONLY, and pLoF is NULL
The six missense-only-burden genes are ESR1, FGFR3, HSD11B2, MTMR11, PTPN11, RPL5.
FGFR3, across every AAF bin and both replicate blocks:
- missense burden `<0.01%`: **P = 1.1e-25, 2.8e-26, 2.0e-41, 3.2e-25, 9.1e-26, 7.1e-39**
- **singleton pLoF: P = 0.667, 0.921, 0.847, 0.233, 0.861, 0.873, 0.731 — NULL in every block**
- best test ACATV, gene P = 1.68e-61

**WHAT THIS MEANS AND DOES NOT MEAN.** FGFR3's association with human height is carried entirely by
MISSENSE variants (in FGFR3 typically gain-of-function, i.e. the achondroplasia direction, shortening).
Simply *losing* FGFR3 does not measurably move height in this cohort.
⚠ POWER CAVEAT, and it is serious: pLoF AAF is 5.99e-05 to 1.7e-4 — these are singletons, so the null
may be underpowered rather than real. This is NOT a refutation of the FGFR3 arm.
⚠ AND IT DOES NOT TOUCH the pharmacological evidence, which is what the stack rests on: infigratinib
+1.74 cm/yr in randomised placebo-controlled phase 3, and dabogratinib +8.2% femur in WILD-TYPE mice.
A germline-haploinsufficiency null and a kinase-inhibition gain are different manipulations - CORR-299
is the standing rule against conflating them, and it applies here in the atlas's own favour.
**TO CHECK NEXT: CATSHL syndrome (FGFR3 LoF, camptodactyly-tall-stature) is human evidence that reduced
FGFR3 function DOES lengthen. Reconcile with this null before either is used.**
