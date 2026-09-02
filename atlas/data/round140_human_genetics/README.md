# Round 140 — human genetics of the phosphatase arm

Raw GWAS Catalog association downloads, retrieved 2026-08-09, one file per gene:

    https://www.ebi.ac.uk/gwas/api/search/downloads?q=ensemblMappedGenes:"<GENE>"&facet=association&efo=true

`MAPPED_GENE` in these files is a **proximity annotation, not a causal assignment** — see CORR-142.
Every height row was re-checked against GTEx v8 single-tissue eQTLs before use:

    https://gtexportal.org/api/v2/dataset/variant?snpId=<rsid>
    https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=<id>&datasetId=gtex_v8

and NPR2 coding variation against gnomAD v4:

    POST https://gnomad.broadinstitute.org/api   { gene(gene_symbol:"NPR2", reference_genome:GRCh38) }

Findings and their grades are in
`nodes/L8_genetics_and_heritability/human_genetics_of_the_phosphatase_arm.yaml`.
