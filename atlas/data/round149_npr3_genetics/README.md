# Round 149 - NPR3 human genetics (the query round 140 never ran)

Round 140 queried NPR2, PPP1CB, PPP2CA, PPP2R5D, PPP5C, SHOC2, CUL7 and PEX6. It did not query
**NPR3**, which is the gene the compound route now targets. Closed here.

## GWAS Catalog
`gwas_NPR3.tsv` - downloaded 2026-08-09 from
`https://www.ebi.ac.uk/gwas/api/search/downloads?q=ensemblMappedGenes%3A%22NPR3%22&facet=association&efo=true`
405 associations, 95 height/stature. Leads at p=1E-300 (Yengo 2022, n=5,314,291).

## GTEx v8 eQTL assignment (CORR-142 rule)
Variant IDs resolved via `/api/v2/dataset/variant`, eQTLs via `/api/v2/association/singleTissueEqtl`.

| lead | GTEx variantId | eQTL genes | tissues | NES (alt) | height allele | effect of height allele on NPR3 |
|---|---|---|---|---|---|---|
| rs3792752  | chr5_32768528_A_G_b38 | NPR3 only | 1 | +0.189 | G (alt) | **MORE** NPR3 |
| rs1173771  | chr5_32814922_A_G_b38 | NPR3 only | 5 | +0.400 | A (ref) | **LESS** NPR3 |
| rs11740580 | chr5_32765351_C_A_b38 | NPR3 only | 1 | +0.233 | A (alt) | **MORE** NPR3 |
| rs10057069 | chr5_32716483_T_C_b38 | NPR3 only | 3 | −0.190 | C (alt) | **LESS** NPR3 |

**Assignment is clean** - every lead is an eQTL for NPR3 and no other gene, unlike PPP2R5D which
dissolved into seven genes (CORR-142). **Direction is not** - two each way, 8 tissue-observations
favouring less-NPR3-is-taller against 2.

**GTEx contains no cartilage, bone or growth plate.** All detections are nerve, testis, adrenal, lung,
cultured fibroblast. NPR3 is CNP-inducible in growth plate (agoston2007), so these directions may not
transfer to the tissue in question.
