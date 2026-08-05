# Claim vs counter-claim ledger

Two sections:
1. **Contradictions** - two credible primary sources disagree, unresolved.
2. **X-grade claims** - repeated in reviews but not traceable to primary data.
   Per the confidence scale these are high-value findings, not filler.

## 1. Contradictions

| id | Claim | Counter-claim | Refs | Load-bearing for | Status |
|----|-------|---------------|------|------------------|--------|
| c001 | Yengo 2022 (Nature, peer-reviewed): the 7,209 height-associated genomic segments have a **mean** size of ~90 kb | The bioRxiv preprint of the *same analysis* states a **median** of ~90 kb | `yengo2022` (10.1038/s41586-022-05275-y) vs preprint 10.1101/2022.01.07.475305 | `height_gwas` segment-size quantitative row; any downstream estimate of per-segment gene density | **Unresolved.** For a right-skewed segment-size distribution mean and median cannot both be ~90 kb, so one wording is loose. Published value used, discrepancy flagged on the node. Needs Supplementary Table retrieval to settle — queued P2 in access_queue.md. Neither number is load-bearing for a mechanistic claim, so impact is low. |

## 2. X-grade claims (untraceable to primary data)

| id | The claim as usually stated | Where it is repeated | What I could not find | Nodes |
|----|-----------------------------|----------------------|-----------------------|-------|
| x001 | "Growth plate chondrocytes exhaust a finite proliferative capacity through telomere attrition" — telomere shortening as the molecular clock that terminates longitudinal growth | Routinely asserted in growth-plate and skeletal-ageing review literature as the mechanistic basis of the finite-proliferative-capacity model | Any primary measurement of telomere length or telomerase activity in **human** growth plate or resting-zone chondrocytes as a function of age or proximity to fusion. Targeted Europe PMC search returned only osteoarthritis articular cartilage, general skeletal-ageing reviews, and rodent work. Nearest positive datum is murine and indirect (mTert-GFP marking a transitional skeletal progenitor peaking during adolescent growth rather than persisting). Search logged under g_l2stem_007. | `telomere_attrition_chondrocyte`, and indirectly `finite_proliferative_capacity_model`, `clonal_exhaustion`, `replicative_senescence_chondrocyte` |
