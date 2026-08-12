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
