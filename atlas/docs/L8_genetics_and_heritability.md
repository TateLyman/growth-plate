# L8 — Genetics and heritability

**39 nodes (0 stubs) · 133 edges touching the layer · 44 gaps · ~70 refs**
Confidence: A 18 · B 18 · C 2 · D 1. `human_evidence` direct 38 / indirect 1.
`translation_risk` **not_applicable on 38 of 39** — this layer is human by construction.

The published coverage table records L8 as "3 nodes, unswept". It has since been swept to 39
and the table is stale; the sweep's output entered the tree during a concurrent merge and is
documented in `audit/phase3_close.md`. Read the numbers below, not `query/coverage.md`, for this
layer.

---

## 1. The settled core

**Height is highly heritable, and the estimate is stable across a century of birth cohorts.**
Twin-based h² 0.69–0.84 (men) and 0.53–0.78 (women) across birth years 1886–1994, 40 cohorts,
143,390 complete twin pairs, **with no clear secular trend** (`jelenkovic2016a`); peak
adolescent h² 0.83 in boys across 45 cohorts and 180,520 paired measurements
(`jelenkovic2016`). Childhood is lower and ancestry-dependent: 0.57 (95% CI 0.52–0.61) European,
0.48 (0.39–0.57) Asian, 0.46 (0.40–0.51) multi-ancestry under 5 years, from 162,293 twin pairs
and 380,195 parent–offspring pairs (`dewau2025`). An IBD sibling design in 119,000 pairs gives
narrow-sense h² **0.76 (SE 0.05)** (`sidorenko2024`).

**The common-variant architecture is fully mapped and almost saturated.** 5.4 million
individuals; **12,111 conditionally independent genome-wide-significant SNPs** clustered into
**7,209 non-overlapping genomic segments** covering **21% of the genome**; 40% of phenotypic
variance explained out-of-sample in European ancestry, 45% using all HapMap 3 SNPs
(`yengo2022`). Per-allele effects of the largest common variants are **0.4–0.44 cm**
(HMGA2 rs1042725, GDF5-UQCC; `weedon2007`), and the first 20 loci together explained 3% of
variance (`weedon2008`).

**Missing heritability is now mostly accounted for, and rare variation is a minority
contributor.** GREML-LDMS on ~17M imputed variants: 56% (SE 2.3%), with inferred true
narrow-sense h² 60–70% (`yang2015`). Whole-genome sequencing of 347,630 UK Biobank genomes over
40M variants captures **88% of pedigree heritability**, partitioned as **68% common
(MAF ≥ 1%) and 20% rare (MAF < 1%)** as a cross-trait mean (`wainschtein2026`). Joint WGS
modelling reaches 46% prediction accuracy (`depope2026`).

**Mutation class predicts effect size, and the human data recapitulate a mouse correction this
atlas made independently.** In 128 unrelated Schmid metaphyseal chondrodysplasia cases,
**COL10A1 missense (dominant-negative) gives height Z −3.62 (SD 1.95) against truncating
(haploinsufficient) −1.99 (SD 1.28), P = 0.013** — a 1.63 SDS premium for dominant interference
(`meng2025`). That is the human counterpart of CORR-002, where `gress2000` had to separate the
`Col10a1` **null** (proliferative-zone compression, mild) from the collagen-X **transgenic**
(hypertrophic-zone compression, severe) in mouse, and reviews had collapsed the two. Two
species, two methods, same conclusion: **for collagen X, loss of protein and presence of bad
protein are different diseases.** `schmid_metaphyseal_chondrodysplasia` was one of only two
accepted confidence upgrades in Phase 3, on 1993 single-kindred linkage (lod 18.2) plus this 128-case
spectrum.

**The dominant single-gene effects are large and human.** ACAN heterozygotes: adult height
median **−2.8 SDS** (range −5.9 to −0.9, n = 103 from 20 families), childhood −2.0 SDS, with
early-onset osteoarthritis in 12 of 20 families and disc disease in 9 of 20
(`gkourogianni2017`). GHR homozygous loss: **−4 to −10 SDS** (69-patient Laron cohort,
`laron2015`).

---

## 2. The live disagreements

**The field's flagship height dataset is graded D in this atlas, and the reasons are specific.**
`height_gwas` carries **two** recorded contradictions. (i) SNP-based h² (56%, SE 2.3%) versus
twin/pedigree (~0.76–0.80) disagree in magnitude — recorded as an open contradiction rather than
collapsed into a single figure. (ii) An internal discrepancy in `yengo2022` itself: the
peer-reviewed *Nature* version states the 7,209 segments have a **mean** size of ~90 kb while
the bioRxiv preprint of the *same analysis* states a **median** of ~90 kb. For a right-skewed
size distribution both cannot be true, so one wording is loose. The published value is used and
the discrepancy is flagged, not silently resolved (c001).

**And the grade is D for a third reason found by this build: the field cannot independently
replicate its own flagship estimate.** `height_gwas` was nominated for upgrade to A by an
earlier audit and **rejected on nesting** — Wood 2014 and Wainschtein 2026 sit *inside*
Yengo 2022's 5.4 million participants. Candidate replications that are subsets of the discovery
sample are not replications. This was the sharpest of ten rejections in the
propositional-replication pass, which ran **2 accepted, 10 rejected — an 83% rejection rate**.
Two failure patterns account for all ten: the node's grade was set by a *different claim* than
the one the second paper tests (6 cases), and the "replication" was a curation or aggregation
**not source-independent** of the first reference (2 cases).

**Common and rare variation rank the same trait's biology differently, and the atlas records it
as a node rather than smoothing it.** `common_vs_rare_pathway_divergence` (grade C):

| ranking | dominated by |
|---|---|
| **Common-variant enrichment** (`weedon2008`, Lango Allen 2010, `wood2014`) | paracrine signalling and matrix — Hedgehog, FGF, WNT/β-catenin, chondroitin sulfate, mTOR (6 pathway families) |
| **Rare Mendelian burden** (771 nosology entries, 552 genes, `unger2023`) | structural collagens and the GH–IGF endocrine axis |

**0 of 3 GWAS pathway-enrichment lists name the somatotropic axis** (`g_l8gen_001`, logged
search) — the source of the largest monogenic stature effects in medicine (GHR −4 to −10 SDS,
STAT5B −7.8 SDS). Convergence is limited to Hedgehog, CNP/NPR2 and proteoglycan/GAG synthesis.
The obvious reconciliation — common variation is depleted where rare variation is catastrophic,
i.e. buffering — is held at **grade E with a discriminating test**, not asserted.

**Polygenic prediction is ancestry-bound and the drop is quantified.** 40% variance explained in
European ancestry against **10–20% in non-European** (14–24% with all HapMap 3 SNPs,
`yengo2022`). Of 802 European signals tested in 52,764 African-ancestry individuals, 643 were
directionally consistent but only **205 nominally significant at P < 0.05**, and only 2 of 20
new African-ancestry secondary signals had MAF < 5% (`graff2021`).

**The epigenetic clock contradicts itself within one cohort.** `epigenetic_clock_growth` carries
an explicit `CONTRADICTS`: `simpkin2017` reports epigenetic age acceleration **positively**
associated with average height (0.23 cm per year of EAA at age 7, 95% CI 0.04–0.41, n = 1,018)
and **negatively** associated with *change* in height in the same cohort, and does not reconcile
the two directions. `kim2024_2` finds a small effect on peak height velocity (β = 0.018 cm/y per
unit EAA, P = 0.0008) and **no** significant association with age at peak height velocity
(β = −0.0022, P = 0.067). The node was drafted at grade X, the search returned these two
papers mid-write, and it was re-graded **D→B with the gap re-scoped** — one of two cases in this
build where a search falsified a draft while it was being written.

---

## 3. The load-bearing assumption

**That common-variant height loci and Mendelian short-stature genes describe the same
biology, so a GWAS hit can be read as a growth-plate gene.**

This is the only reason L8 exists in a growth-plate atlas. Its whole downstream function is as a
discovery engine feeding L3 (which pathway to believe), L5 (which matrix protein matters) and
L11 (which gene to model as a natural experiment). Every edge from L8 into L3 — twelve of them —
presupposes it.

The evidence for it is real but narrow: three pathway families converge (Hedgehog, CNP/NPR2,
proteoglycan/GAG synthesis), and several loci are simultaneously GWAS hits and Mendelian
disease genes (*ACAN*, *GDF5*, *IHH*, *NPR2*, *HMGA2*).

The evidence against it is the divergence above, and one unanswered question that makes the
divergence hard to explain away: **what fraction of the 12,111 independent height SNPs exert
their effect through the growth plate chondrocyte at all**, as opposed to through muscle,
endocrine tissue, vasculature or gut (`g_l8gwas_001`, tract 4)? Nobody knows. The associated
segments cover **21% of the genome**, which is close to the omnigenic prediction that essentially
every expressed gene contributes — and `g_l8gen_010` asks the omnigenic model's own load-bearing
question (do peripheral loci act by altering core growth-plate gene expression in chondrocytes?)
and records that it has never been tested in chondrocytes.

Two of the layer's search-established gaps sharpen the problem to embarrassment. **`g_l8gen_004`
(tract 2): is SHOX protein expressed in human growth plate chondrocytes, and in which zone?**
SHOX haploinsufficiency is the single best-characterised human short-stature locus and the
protein's zonal localisation in human physis is not established. **`g_l0l9_005`/`g_l8gen_009`:
does ZBTB38 — one of the first twenty replicated height loci — have any measurable function in
growth plate chondrocytes?** No.

---

## 4. What would change everything

**A growth-plate eQTL catalogue from primary human chondrocytes** (`g_l8gwas_002`, tract 2).
Genotype and RNA-sequence primary chondrocytes from enough human physeal specimens to call
cis-eQTLs, then colocalise against the 12,111 height signals.

This single resource partitions the assumption in §3 into a measured number. If a large fraction
of height signals colocalise with chondrocyte eQTLs, the discovery-engine use of L8 is validated
and the somatotropic-axis absence becomes a genuine biological statement (the GH–IGF axis is
under stabilising selection and depleted of common variation). If only a small fraction
colocalise, then most of height's common-variant architecture acts outside the plate, L8's twelve
edges into L3 are over-interpreted, and the atlas's premise that stature is primarily a
growth-plate phenomenon needs the same scrutiny that `x002` in L0 already invites.

The precedent for its feasibility is in the layer: `mcdonnell2024` assayed ~700,000 CpGs in 72
developing human chondrocyte samples (7–21 post-conception weeks), found 3% of CpGs changing
developmentally, >8,200 DMRs, and colocalised **24 loci** where osteoarthritis risk variants meet
methylation QTLs. The same design has simply never been run on postnatal physis with height as
the trait.

---

## 5. Numbers

| Parameter | Value | Unit | Species | Spread / n | Source | Flag |
|---|---|---|---|---|---|---|
| GWAS discovery sample | 5,400,000 | individuals | **human** | diverse ancestries | `yengo2022` | — |
| Independent genome-wide-significant SNPs | **12,111** | SNPs | **human** | P < 5×10⁻⁸, conditionally independent | `yengo2022` | — |
| Associated genomic segments / genome covered | 7,209 / **21** | segments / % | **human** | mean segment ~90 kb (**preprint says median**) | `yengo2022` | **c001 internal discrepancy** |
| Variance explained, European / non-European | 40 / **10–20** | % | **human** | 45% / 14–24% with all HapMap 3 | `yengo2022` | ancestry-bound |
| European signals replicating in African ancestry | 643/802 directional, **205** nominally significant | signals | **human** | n = 52,764 | `graff2021` | — |
| Twin h², men / women (1886–1994) | 0.69–0.84 / 0.53–0.78 | h² | **human** | 40 cohorts, 143,390 pairs; **no secular trend** | `jelenkovic2016a` | — |
| Twin h², age <5 y, Euro / Asian / multi | 0.57 / 0.48 / 0.46 | h² | **human** | 95% CI 0.52–0.61 / 0.39–0.57 / 0.40–0.51 | `dewau2025` | — |
| Sibling-IBD narrow-sense h² | 0.76 | h² | **human** | SE 0.05; 119,000 pairs | `sidorenko2024` | — |
| SNP h² (GREML-LDMS, ~17M variants) | **56** | % | **human** | SE 2.3; true inferred 60–70% | `yang2015` | **contradicts twin estimate** |
| Pedigree h² captured by WGS | 88 (68 common / 20 rare) | % | **human** | 347,630 genomes, 40M variants | `wainschtein2026` | **nested inside `yengo2022`** |
| Largest common per-allele effect | 0.4–0.44 | cm | **human** | HMGA2, GDF5-UQCC | `weedon2007` | two loci |
| Largest monogenic effect (GHR) | −4 to −10 | SDS | **human** | 69-patient cohort | `laron2015` | — |
| ACAN heterozygote adult height | **−2.8** (range −5.9 to −0.9) | SDS median | **human** | n = 103, 20 families | `gkourogianni2017` | — |
| COL10A1 dominant-negative vs truncating | **−3.62 vs −1.99** (Δ 1.63) | SDS | **human** | SD 1.95/1.28; P = 0.013; n = 128 | `meng2025` | no CI on the difference |
| COMP variants in the type-3 Ca-binding repeat | 87.7 (80.8% missense) | % of probands | **human** | 413/471 across 106 publications | `ni2026` | — |
| Monogenic skeletal disorder entries / genes | 771 / 552 | entries / genes | **human** | 2023 nosology, 11th revision | `unger2023` | — |
| GWAS enrichment lists naming the somatotropic axis | **0 of 3** | analyses | **human** | search logged | `wood2014` et al. | **null result** |
| Sperm germline mutation accumulation | 1.67 | mutations/year/haploid genome | **human** | 95% CI 1.41–1.92; n = 81 | `neville2025` | — |
| Sperm carrying a pathogenic exome mutation | 3–5 | % | **human** | middle-aged to older men | `neville2025` | — |
| FGFR3 missense raising ligand-independent signalling | 9 of 10 | tested substitutions | **human** | dissected postmortem testis | `moura2024` | — |
| CpGs changing across chondrocyte development | 3 (>8,200 DMRs) | % of ~700,000 | **human** | n = 72, 7–21 pcw | `mcdonnell2024` | — |
| EAA effect on height at age 7 | 0.23 | cm per year EAA | **human** | 95% CI 0.04–0.41; n = 1,018 | `simpkin2017` | **self-contradictory within cohort** |
| MR: height per 1 SD genetically predicted IGF-1 | 0.09 | SD | **human** | n = 1,176,465 outcome sample | `de2026` | replicated in ALSPAC |
| Confidence upgrades accepted / tested | **2 / 12** | — | — | 83% rejection | `phase3_close` | structural |
| Fraction of the 12,111 SNPs acting via chondrocyte | **unknown** | % | human | — | — | `g_l8gwas_001` |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l8gwas_002`** (search_established, tract 2) — the human growth-plate eQTL catalogue. See
   §4. Nothing else in this layer changes as much per unit of effort.
2. **`g_l8gwas_001`** (quantitative_gap, tract 4) — partition the 12,111 SNPs by tissue of
   action. Discriminator: colocalisation against chondrocyte, myocyte, hepatocyte and pituitary
   eQTLs in parallel. A chondrocyte-dominant answer validates L8→L3 edges; a distributed answer
   reframes stature as a multi-tissue trait the growth plate merely executes.
3. **`g_l8gen_001`** (search_established, tract 4) — why is the GH–IGF axis absent from
   common-variant enrichment? Discriminator: measure selection coefficients and common-variant
   density at somatotropic-axis loci against matched control genes. Buffering predicts depletion
   of common functional variation specifically at genes with catastrophic rare alleles.
4. **`g_l8gen_004`** (search_established, tract 2) — SHOX protein in human physis, by zone.
   Immunostaining or RNAscope on the existing human physeal blocks. The best-characterised human
   short-stature gene has no established zonal localisation.
5. **`g_l8gen_011`** (quantitative_gap, tract 3) — how much does assortative mating inflate
   twin/pedigree h², and does correcting for it reconcile 0.76–0.80 with 0.56? `sunde2024` gives
   the input (47,135 co-parent pairs, genetic assortment in 9 of 16 traits, 6 of 9 showing
   offspring variance inconsistent with equilibrium assortment). Applying that correction to the
   twin estimate is arithmetic nobody has published.
6. **`g_l8gen_005` / `g_l8gen_006` / `g_l8gen_007` / `g_l8gen_008`** (quantitative_gap, tract
   3–4) — a family of missing effect sizes: mean adult height by *COL2A1* mutation class, by
   genotype-confirmed pseudoachondroplasia *COMP* domain, of heterozygous *IGF1R* carriers
   (prenatal vs postnatal partition), and of intragenic *HDAC4* variants as distinct from whole
   2q37 deletions. Each is retrievable from existing clinical registries and none has been
   published. These are the numbers L11 needs to grade its own nodes.
7. **`g_l8gen_014`** (search_established, tract 4) — does epigenetic age acceleration track
   radiographic bone age or predict fusion timing? If it does, L7's method problem
   (`g_l7fuse_007`) acquires an orthogonal instrument; if it does not, the epigenetic clock is
   about a different ageing process than the one that closes growth plates.

---

## 7. Human-translation status

**39 of 39 nodes are human. 38 carry `translation_risk: not_applicable`; the one exception
(`dna_methylation_growth_plate`, low) is human tissue with a rabbit comparator.** This layer has
no species problem at all, which makes it unique in the atlas and is why its failure modes are
*epistemic* rather than *translational*.

Those failure modes are three, and they are specific to this layer:

**(i) Sample nesting.** The largest human datasets in medicine overlap each other. Yengo 2022's
5.4 million contains Wood 2014 and Wainschtein 2026; UK Biobank appears in most of them. The
appearance of replication is manufactured by shared participants, which is why `height_gwas`
sits at grade D in a layer that is otherwise 36 of 39 at A or B, and why the propositional-replication
rule rejected 83% of what it tested.

**(ii) Ancestry.** Prediction accuracy falls from 40% to 10–20% outside European ancestry and
only a quarter of European signals reach nominal significance in African-ancestry samples. Every
polygenic statement in this layer is a statement about the populations that were sequenced.

**(iii) The tissue is missing even though the species is right.** Being human is not the same as
being *growth plate*. `shox_gene`, `zbtb38_gene`, `hmga2_gene`, `gdf5_height_locus`,
`igf2_h19_imprinting` and `genomic_imprinting_growth` are established in human blood, human
registries and human pedigrees — and four separate searches (`g_l8gen_004`, `g_l8gen_009`,
`g_l0l9_003`, `g_l0l9_004`) asked whether the corresponding gene or mark has ever been observed
in a human growth plate chondrocyte, and returned nothing. **L8 is the layer where the atlas
knows the genotype and has never seen the cell.**
