# Operator-supplied bulk data, 2026-08-12

Fetched here rather than re-requested. All direct-download, no captcha.

| file | size | what it unlocks |
|---|---|---|
| `statistical-results-ALL.csv.gz` | ~538 MB | **IMPC**, release 2026-03-16. Genome-wide KO phenotyping with effect sizes and p-values. The systematic answer to "which single-gene losses lengthen a mammal" — never run in this atlas. |
| `genotype-phenotype-assertions-ALL.csv.gz` | 4.8 MB | IMPC phenotype calls; cross-check on the above. |
| `MGI_PhenoGenoMP.rpt` | 52 MB | Every MGI allele→Mammalian Phenotype annotation, incl. non-consortium published alleles. |
| `MGI_GenePheno.rpt` | 36 MB | Gene-level MP annotations. |
| `VOC_MammalianPhenotype.rpt` | 2.9 MB | MP term vocabulary. |
| `MPheno_OBO.ontology` | 7.4 MB | MP ontology graph — lets a length screen propagate through descendants rather than grepping the literal phrase "increased body length". Operator's addition, and the right call. |
| `CTD_chem_gene_ixn_types.csv` | 8 KB | Decoder for the CTD interaction vocabulary (b, exp, pho, deg…) used by round 299's signed join. |

## Not fetched here — still needed

- **kosmicki2026 supplementary tables** (medRxiv 10.64898/2026.06.22.26355163). medRxiv's attachment
  endpoint 403s to automated clients. **Supplementary Table 4 = all 207 gene-based-test genes** and
  **Table 3 = 105 single variants in 87 genes**; the atlas currently holds only the 17 from Table 1 plus
  HHIP read out of the article text. Tables 15/16 carry the ancestry-specific rows incl. HHIP p.V496E.
- **GSE288028 raw** — the postnatal human growth-plate scRNA-seq. NOTE: this is the SAME STUDY as the
  atlas's existing `chu2026` (Sci Transl Med 10.1126/scitranslmed.adw3590); the atlas already holds its
  supplementary tables at `atlas/data/round243_supplied/chu2026_supp/`. What is missing is the RAW
  single-cell matrices, which is what would let the GP1/GP2 sign-convention problem (CORR-296, blocking
  four rounds) finally be settled.
- **`github.com/anarl/spatial_bone_growth`** — Visium + Visium HD of human growth plates from healthy
  adolescents aged 12-14 (epiphysiodesis). Zonally resolved, postnatal, human. Strongest available
  replacement for GSE9160, which is two donors with one failed dissection.
- GSE246390 (adolescent human GP bulk, mechanical loading); GSE233188 / GSE234040 / GSE233970 and
  PRJNA478935 (all FETAL — keep separate from postnatal per the operator's warning).

## Correction to my own record
I described GSE9160 as "1997-era". It was submitted 2007, public 2013. Corrected here; the substantive
caveats (n=2, one dissection failed, donors one F one M) are unchanged.

---
## Second pass, same day — full-list audit

Every remaining URL from the operator's list was tested rather than assumed.

**Additionally fetched (gitignored, on disk only):**
- `GSE288028_RAW.tar` — raw postnatal human growth-plate scRNA-seq. Same STUDY as the atlas's
  `chu2026` (whose supplementary tables are already held), but the RAW MATRICES are new here, and they
  are what can settle **CORR-296** — the GP1/GP2 sign convention that has blocked rounds 241, 244, 245,
  246 and forced "direction cannot be assigned" in every round since.
- `spatial_bone_growth/` (609 MB, cloned) — Visium + Visium HD of growth plates from healthy adolescents
  aged 12-14 via epiphysiodesis. Postnatal, human, zonally resolved. The strongest available replacement
  for GSE9160 (n=2, one dissection failed, one donor of each sex).
- `IMPC_README.md` — field documentation for the statistical-results schema.

**Confirmed reachable, not pulled (low priority):** GSE233188 (fetal), GSE9160 raw CELs (processed
matrix already vendored and analysed).

**CANNOT REACH — operator action required:**
1. **kosmicki2026 supplementary Tables 3, 4, 15, 16.** Landing page 200 but returns an HTML shell; the
   .xlsx attachments sit behind medRxiv's attachment endpoint and `.full.pdf` returns 429.
   **Table 4 = all 207 gene-based-test genes**, against the 17 the atlas currently holds. Highest-value
   outstanding item.
2. **GSE246390 — 404** on the GEO supplementary endpoint (adolescent human GP, mechanical loading).
   Likely SRA-only; check whether PMC11629350 carries counts as supplementary.
3. **GSE233970 — 404**, same pattern (human SSC Smart-seq2).
4. **science.org/doi/10.1126/scitranslmed.adw3590 — 403.** Not urgent; supplementary tables already held
   as `chu2026`.
5. **bioRxiv PDFs — 429** (rate-limited, may succeed later), incl. 2025.03.14.642964 and 2025.03.12.642613.
6. **PRJNA478935 / SRA** — raw SRA, terabyte-scale, fetal. Deliberately skipped.

## kosmicki2026 supplement — RECEIVED 2026-08-12
`kosmicki2026_supp_tables_S1_S29.xlsx` (the two uploads were byte-identical duplicates; one kept).
Contains **Tables S1-S29 — the COMPLETE supplement. Nothing outstanding.** Verified by row count:
- **Table S4 = 209 rows = THE 207 GENE-BASED-TEST GENES.** The atlas has been working from the 17 in
  main-text Table 1 plus HHIP read out of the article prose. This is the full set.
- **Table S3 = 128 rows = the 105 significant rare nonsynonymous single variants in 87 genes.**
- Columns include ENSG, symbol, test type (burden), chr, pos, beta, SE.
**S15 and S16 ARE in this file.** I reported them missing after a hand-rolled XML parser read only the
first twelve <sheet> entries; openpyxl shows 29. CORR-323. Beyond the tables already named:
- S5  gene-based stats for the 17 singleton-pLoF genes - the ONLY table the atlas had been using
- S6  burden tests for all 207 genes
- S7  ratio of singleton pLoF beta to GWAS beta - rare vs common effect magnitude, directly
- S12 genes significant BEFORE but not AFTER conditioning on 3,034 common variants = a built-in
      false-positive filter, and any atlas target appearing here needs re-grading
- S13 the 6 missense-only-burden genes, which include FGFR3
- S15 ancestry/sex-subset single variants = the HHIP p.V496E row
- S16 population-specific stats for FBN1 15:48481729:T:C
- S17 burden heritability regression; S18/S19 carrier enrichment at phenotypic extremes
NEXT: cross Table S4 against `atlas/data/round298/undrugged_targets.txt` and against the CTD signed
handles - a 207-gene target list changes the denominator of every druggability claim in rounds 297-298.
