# Pathway matrix — five axes, never merged

**Status:** supersedes the earlier "four-way consensus ranking" spec.
**Built:** 2026-08-05. **Sources:** `digest.py L8 / L11 / L12`, `query/derived.json`
(`convergence`), node `common_vs_rare_pathway_divergence`, `atlas/audit/phase3_close.md` §3.
**New refs added this build:** `atlas/sources/shards/pathwaymatrix.yaml` (spence2026,
zeng2018, oconnor2019).

---

## 0. Why there is no ranking in this document

The superseded spec treated four axes as four estimates of one quantity and read
agreement as robustness. They are not four estimates of one quantity. They are five
measurements of five different constructs, in five different units, with five different
failure modes. Averaging them, or ranking on their consensus, destroys the only
information the comparison contains.

The atlas has already demonstrated this. **0 of 3 published height-GWAS pathway-enrichment
analyses name the somatotropic axis** (weedon2008, lango2010, wood2014; null established
by search log `g_l8gen_001`, 114 hits / 25 screened) — and the somatotropic axis is the
source of the largest monogenic stature effects in medicine (GHR **−4 to −10 SDS**, n=69,
laron2015; STAT5B **−7.8 SDS**, n=1, hwa2005).

That is not a contradiction awaiting resolution. It is the expected signature. Negative
selection couples larger per-allele effect to lower allele frequency across human complex
traits including height (zeng2018; oconnor2019). A gene under strong purifying selection
**cannot** carry a common large-effect allele. A height GWAS is therefore structurally
incapable of finding an essential constrained pathway, no matter how important that
pathway is. Absence from an enrichment list is evidence about *tolerance to common
variation*, and about nothing else.

Consequences enforced throughout this document:

- **No single ordering appears anywhere.** Pathways are listed alphabetically. That order
  carries no meaning.
- **Velocity elasticity is never carried into the final-height column.** Where final
  height is unmeasured it is written `unmeasured`, never imputed.
- Every cell carries value, unit, n, uncertainty, source — or says which of those could
  not be obtained.

---

## 1. The five axes

| axis | question | unit | primary source layer |
|---|---|---|---|
| `velocity_elasticity` | what pharmacologically moves growth **rate** now | cm/yr (or Z/yr) per unit modulation | L12 |
| `final_height_elasticity` | what moves **adult stature** | cm or SDS | L12 (mostly absent) |
| `gwas_enrichment` | where **tolerated common variation** lives | named / not named in 3 published enrichment analyses | L8 |
| `mendelian_burden` | where the system is **fragile to disruption** | disorder count; effect size in SDS | L8 / L11 |
| `graph_convergence` | where the map says causal information concentrates | inbound edges; rank of 80 ranked / 614 nodes | `query/derived.json` |

### Global caveats that apply to every elasticity cell

1. **Elasticity is dose-, age- and context-dependent.** Nearly every value below comes
   from a single trial, at a single dose level, in a single indication, over 52 weeks.
   None of them is a dose–response curve.
2. **Almost every velocity estimate is measured in a disease population**, usually
   achondroplasia or GH deficiency, and cannot be assumed to transfer to normal-range
   stature.
3. **Velocity does not convert to final height at a known rate.** The conversion factor
   is an open quantitative gap (`g_l12b_016`). Documented failures of conversion:
   - **Aromatase inhibitors:** the predicted-adult-height gain seen at year 1 **did not
     persist at years 2–3** (zegarra2024, n=79, open-label RCT; reported qualitatively by
     the authors). Open gap `g_l12b_015`.
   - **Budesonide (CAMP):** the adult-height deficit of **−1.2 cm** was already **−1.3 cm
     at 2 years** — the cost was set inside 2 years and did not grow (kelly2012, n=943).
     A short exposure bought a permanent deficit.
   - **rhGH in ACAN deficiency:** height velocity 8.3 → 7.7 → 6.8 cm/yr across years 1–3
     (muthuvel2024, n=10). Within-treatment decay, uncontrolled.
4. **No growth-modifying drug has ever had its concentration measured inside human growth
   plate cartilage** — 0 of 12 agents audited (`g_l12b_002`). Every exposure–response
   statement below uses plasma as a surrogate for a tissue the drug must diffuse into
   across avascular cartilage.
5. **Gene-level attribution from association statistics is biased** by gene specificity,
   gene length and chance (spence2026). The `gwas_enrichment` column is deliberately read
   at the level of *published pathway/gene-set enrichment results*, not by re-mapping
   SNPs to genes.

### Scoring rules for the categorical axes (stated so they can be disputed)

- `gwas_enrichment` = **PRESENT** if the pathway is named as an enriched pathway or
  gene-set in ≥1 of weedon2008 / lango2010 / wood2014, **or** carries a replicated
  genome-wide-significant common height locus with a published per-allele cm effect.
  Otherwise **ABSENT**. Marouli2017 rare-coding results are recorded but scored
  separately — they are a *rare* coding tier, not common variation.
- `mendelian_burden` = **HIGH** if ≥1 human monogenic disorder of the pathway has a
  measured stature effect ≥2 SDS, **or** a pathway gene appears on the ClinGen
  commonest-skeletal-dysplasia list (webb2026: COL1A1, COL1A2, COL2A1, FGFR3, SLC26A2,
  TRPV4, COMP, ALPL, SOX9). Otherwise **MODERATE** / **LOW**.
- `graph_convergence` = **HIGH** if ≥1 member node is in the top 25 of the derived
  convergence ranking. Pathway sums are over all member nodes.

---

## 2. The matrix

Alphabetical. **The order is not a ranking.** Read down a column, never across a row as
if the cells were commensurable.

| pathway | velocity_elasticity | final_height_elasticity | gwas_enrichment | mendelian_burden | graph_convergence |
|---|---|---|---|---|---|
| aggrecan / proteoglycan | +3.1 cm/yr yr-1 (5.2→8.3 median), n=10, uncontrolled | `unmeasured` (predicted only, +6.8 cm) | **PRESENT** — all 3 tiers | **HIGH** — −2.8 SDS, n=103 | MODERATE — Σ12, rank 26 |
| BMP / TGF-β | `unmeasured` | `unmeasured` | **PRESENT** — locus only (GDF5 0.44 cm/allele) | **HIGH** — Grebe/H-T; SDS unmeasured | LOW — Σ18, rank 35, **intra-L3** |
| CNP / NPR2 / PKG | +1.36 cm/yr class (95% CI 1.05–1.68), n=326 | `unmeasured` — 0 programmes | **ABSENT** — 0/3 | **HIGH** — het −1.4 SDS; biallelic ~−6 SDS | HIGH — Σ46, rank 10 |
| collagen II / X / XI | `unmeasured` (n=1 reports only) | `unmeasured` | **ABSENT** — 0/3 | **HIGH** — −3.62 vs −1.99 SDS, n=128 | MODERATE — Σ23, rank 25 |
| FGFR3 | +1.74 cm/yr (95% CI 1.31–2.17), n=114 | `unmeasured` — 0 programmes | **PRESENT** — FGF signalling (wood2014) | **HIGH** — adult 132/124 cm, n=466 | HIGH — Σ49, rank 7 |
| GH–IGF1 somatotropic | +3.0 to +5.0 cm/yr, n=21,812 (high ROB) | +0.9 SDS (SD 1.1), n=102, registry | **ABSENT** — 0/3 (explicit null) | **HIGH** — −4 to −10 SDS; −7.8 SDS | HIGH — Σ96, rank 6 |
| glucocorticoid | −0.1 cm per µg/kg/day (p=0.007), n=943 | **−1.2 cm** (95% CI −1.9 to −0.5), n=943 | **ABSENT** — 0/3 | **LOW** — no monogenic stature disorder | **LOWEST** — Σ6, **0 in top-80** |
| HIF1A / hypoxia | `unmeasured` | `unmeasured` | **ABSENT** — 0/3 | **LOW** — none identified | LOW — Σ8, **0 in top-80** |
| matrix mineralization (TNAP/PPi/ENPP1) | +0.085 Z/yr children (P<0.0001), n=641 | `unmeasured` | **ABSENT** — 0/3 | **HIGH** — ALPL on ClinGen list; SDS unmeasured | LOW — Σ19, rank 34 |
| mechanotransduction (PIEZO/TRPV4/YAP-TAZ) | 17.1 %/0.1 MPa — **animal**, not human, not cm/yr | `unmeasured` | **ABSENT** — 0/3 | **HIGH** — TRPV4 on ClinGen list; SDS unmeasured | LOW for the molecules — PIEZO1 1, TRPV4 0, YAP/TAZ 0 |
| mTORC1 | `unmeasured` | `unmeasured` | **PRESENT** — mTOR (wood2014) | **LOW** — none identified | LOW — Σ12, rank 41 |
| PTHrP / IHH | `unmeasured` — never administered | `unmeasured` | **PRESENT** — Hedgehog (weedon2008) | **HIGH** — Blomstrand lethal; Jansen n=24 | HIGH — Σ63, ranks 11/14/19 |
| RUNX2 / MEF2C / HDAC4 | `unmeasured` | `unmeasured` | **ABSENT** — 0/3 | **MODERATE** — CCD; brachydactyly 48%, n=103 | LOW — Σ17, rank 42 |
| sex steroid / aromatase | +1.3 cm PAH yr-1 (p=0.043), n=79 — **does not persist** | +3.5 to +4.5 cm, n=21,812 (high ROB) | **ABSENT** — 0/3 (AR at rare-coding tier) | **HIGH** — ESR1-null 204 cm; aromatase-def. tall | MODERATE — Σ25, rank 44 |
| SOX9 / SOX trio | `unmeasured` | `unmeasured` | **ABSENT** — 0/3 | **HIGH** — SOX9 on ClinGen list; SDS unmeasured | MODERATE — Σ16, rank 22, **intra-L3** |
| thyroid hormone | `unmeasured` as elasticity | −0.1 SDS treated vs −0.8 target, n=215 | **ABSENT** — 0/3 | **HIGH** (qualitative) — SDS unmeasured | LOW — Σ11, rank 53 |
| WNT / β-catenin | `unmeasured` | `unmeasured` | **PRESENT** — WNT/β-catenin (wood2014) | **LOW** — LRP5 phenotypes are bone mass | LOW — Σ22, rank 43, **intra-L3** |

**Cell census.** 17 pathways × 5 axes = **85 cells**. Strictly `unmeasured`: **22 / 85 =
26%** (velocity 9, final height 13). A further **8 mendelian cells** carry a disorder
count but no stature effect size in SDS — half-measured, and each is an open
`quantitative_gap`. Cells lacking their headline number: **30 / 85 = 35%**.

**Final-height elasticity is unmeasured for 13 of 17 pathways.** Only four pathways have
any attained-adult-height number at all, and one of those four (glucocorticoid) is
negative.

---

## 3. Cell detail

Each cell below gives value · unit · n · uncertainty · source. Where the n or the CI could
not be obtained, that is stated rather than omitted.

### aggrecan / proteoglycan

- **velocity_elasticity** — rhGH 50 µg/kg/day in ACAN haploinsufficiency: median height
  velocity **5.2 → 8.3 cm/yr** in year 1 (ranges 3.8–7.1 → 7.3–11.2), **P=0.004**; **n=10**
  treatment-naive prepubertal children; **open-label, single-arm, no control group**;
  velocity fell to 7.7 (yr 2) and 6.8 cm/yr (yr 3). ΔHtSDS +1.21 over 3 y (range
  +0.82–1.94). `muthuvel2024` (PMID 39502477). *This is a GH effect measured in an ACAN
  background, not a modulation of aggrecan itself — no aggrecan-directed agent exists.*
- **final_height_elasticity** — `unmeasured`. The trial reports Δ**predicted** adult
  height +6.8 cm over 3 years. Predicted adult height is not attained adult height and is
  not carried into this column.
- **gwas_enrichment** — **PRESENT at all three tiers**, the broadest of any pathway:
  ACAN and ADAMTSL3 in the extracellular-matrix set of weedon2008 (20 loci); chondroitin-
  sulfate genes, osteoglycin and hyaluronic-acid binding in wood2014 (697 variants,
  n=253,288); proteoglycan/glycosaminoglycan synthesis at the rare-coding tier in
  marouli2017 (83 low-frequency coding variants, MAF 0.1–4.8%, max effect ~2 cm/allele).
- **mendelian_burden** — heterozygous ACAN: adult height **−2.8 SDS** (median, range −5.9
  to −0.9), **n=103** from 20 families; childhood −2.0 SDS; bone age advance +1.3 y (range
  0.0–+3.7); early-onset OA in 12/20 families. `gkourogianni2017`. Independent discovery
  families −2.3 to −4.2 SDS, `nilsson2014_2`. SLC26A2 (sulfate transport) on the ClinGen
  commonest-dysplasia list, `webb2026`.
- **graph_convergence** — Σ inbound 12 across 9 member nodes; `aggrecan_acan` rank **26**
  (9 inbound, 5 layers). Note `phase3_close.md` §5: `acan_dosage_effect` (L5) and
  `acan_related_short_stature` (L11) were a surviving cross-layer duplicate, which inflated
  this pathway's apparent node count before merge.

### BMP / TGF-β

- **velocity_elasticity** — `unmeasured`. No human agent modulating BMP or TGF-β
  signalling has been given with a linear-growth endpoint.
- **final_height_elasticity** — `unmeasured`.
- **gwas_enrichment** — **PRESENT at the locus level only.** BMP/TGF-β is *not* named as
  an enriched pathway in weedon2008, lango2010 or wood2014. But the **GDF5–UQCC** region
  carries a replicated additive per-allele adult-height effect of **0.44 cm**, n=6,669
  Finnish + Sardinian plus 28,801 follow-up, overall **P < 1e-15** (`sanna2008`) — one of
  the two largest-effect common height variants known. This split (pathway absent, gene
  present) is why this pathway is a boundary case in §4.
- **mendelian_burden** — **HIGH but unquantified.** GDF5/CDMP1 loss of function causes
  Grebe- and Hunter-Thompson-type acromesomelic chondrodysplasia with severe limb
  shortening (Thomas 1996, via `gdf5_protein`); LTBP3 loss of function causes brachyolmia
  with short stature (Huckert 2015); TGFB1 gain of function causes Camurati-Engelmann
  (Kinoshita 2000); NOG and BMPR1B produce recognisable skeletal phenotypes. **No adult
  height in cm or SDS was retrieved for any of these.** Open quantitative gap.
- **graph_convergence** — Σ inbound 18 across 13 member nodes. Only
  `bmp_signaling_growth_plate` reaches the top 80, at rank **35** with **n_layers = 1** —
  all 8 of its inbound edges originate inside L3. See §5.

### CNP / NPR2 / PKG

- **velocity_elasticity** — pooled class effect on annualised growth velocity **+1.36
  cm/yr, 95% CI 1.05–1.68**, meta-analysis of **4 RCTs, n=326**, children <18 y with
  genetically confirmed achondroplasia (`kamrulhasan2026`). Component trials: vosoritide
  15 µg/kg/day **+1.57 cm/yr, 95% CI 1.22–1.93**, n=121 randomised (60/61), 52 weeks
  (`savarirayan2020`); navepegritide 100 µg/kg/week **+1.49 cm/yr, 95% CI 1.05–1.93**,
  n=84 (57/27), 52 weeks (`nct05598320`). **No head-to-head trial exists**; the two agents
  differ ~300-fold in exposure duration (released-CNP t½ 5.3 d vs vosoritide 21.0–27.9
  min) yet produce indistinguishable velocity effects — an unexplained result bearing on
  gaps `g_mr002_h1`–`h3`.
- **final_height_elasticity** — `unmeasured`. **0 CNP-analogue or FGFR3-inhibitor
  programmes have reported attained final or near-adult height** as of 2026-08-05; both
  achondroplasia approvals are **accelerated**, on a surrogate endpoint. Gaps
  `g_l12pharm_001`, `g_l12b_001`.
- **gwas_enrichment** — **ABSENT.** Not named in weedon2008, lango2010 or wood2014.
  ⚠ **Internal discrepancy flagged:** the summary of node
  `common_vs_rare_pathway_divergence` lists CNP/NPR2 as one of three families where the
  common and rare rankings converge, but that node's own claim-grade B basis documents
  only IHH and ACAN. A targeted Europe PMC search this build (NPR3/NPPC/NPR2 × height ×
  GWAS, 247 and 187 hits) returned no published height pathway-enrichment analysis naming
  the CNP axis. The assertion should be downgraded or a citation supplied.
- **mendelian_burden** — **HIGH, and bidirectional (the strongest two-sided human dose
  evidence in the matrix).** Loss: biallelic NPR2 → acromesomelic dysplasia Maroteaux, 21
  mutations in 21 families (`bartels2004`); two siblings after 8.5 y of high-dose GH
  reached −6.57 and −4.58 SDS (`arya2020`, n=2). Heterozygous NPR2 carriers **−1.8 SDS
  (SD 1.1)** vs non-carrier relatives −0.4 SDS (SD 0.8), **P<0.0005**, n=16 vs 23, same
  family and environment → **~1.4 SDS attributable to one lost allele** (`olney2006`).
  ISS yield 3/47 = 6% (`vasques2013`); 0–3.8% (`wang2015`, n=192+192). NPPC LoF 2 of 668
  screened (`hisadooliva2018`). Gain: NPR2 p.Met482_Leu483del family **+2.77 / +1.96 /
  +1.30 SDS**, n=3 (`lauffer2020`); NPPC-overexpressing translocation, plasma CNP 2-fold,
  overgrowth, n=1 vs 5 controls (`bocciardi2007`).
- **graph_convergence** — Σ inbound 46; `npr2_receptor` rank **10** (18 inbound, 4 layers),
  `cgmp_second_messenger` rank 16, `pkg2_kinase` rank 50, `cnp_protein` rank 73.
  ⚠ Carries correction **CORR-003**: PKG-II loss expands the plate 2.6× (rat, 665 vs 255
  µm) while NPR2 loss shrinks it to 23% of control (mouse) — the effector step of the
  pathway vosoritide targets is sign-inconsistent, and cGKI is *more* zone-enriched
  (5.9×) than cGKII (4.4×) yet has never been removed genetically here.

### collagen II / X / XI

- **velocity_elasticity** — `unmeasured` as an elasticity. Nearest evidence: rhGH in
  COL2A1 spondyloepiphyseal dysplasia congenita, **+0.76 SDS over 3.5 y (n=1)** and
  **+0.27 SDS over 3 y (n=1)**, no control arm (`zhan2025`). Two single patients is not an
  elasticity.
- **final_height_elasticity** — `unmeasured`.
- **gwas_enrichment** — **ABSENT.** No fibrillar collagen is named in any of the three
  enrichment analyses. weedon2008's "extracellular matrix" set is EFEMP1, ADAMTSL3 and
  ACAN — fibulin, ADAMTS-like and proteoglycan, not collagen.
- **mendelian_burden** — **HIGH; the largest disorder count in the matrix, and the only
  pathway with a *measured allelic-mechanism gradient*.** COL10A1 dominant-negative
  missense **−3.62 SDS (SD 1.95)** vs truncating/haploinsufficient **−1.99 SDS (SD 1.28)**,
  **P=0.013**, **n=128** metaphyseal chondrodysplasia Schmid cases — a **1.63 SDS premium
  for dominant-negative over haploinsufficient alleles at the same locus** (no CI is
  published on the difference; `meng2025`). Age at onset 12 vs 72 months by domain
  (P=0.0014). COL2A1 glycine substitutions in 6 of 7 consecutive SEDC families
  (`zhan2025`); 1 of 102 ISS (`andrade2022`). COL1A1, COL1A2 and COL2A1 head the ClinGen
  commonest-dysplasia list (`webb2026`).
- **graph_convergence** — Σ inbound 23; `collagen_type_x` rank **25** (9 inbound, **6
  layers** — the broadest layer span of any matrix node), `collagen_type_ii` rank 47,
  `collagen_crosslinking` rank 77. COL11 has 0 inbound.

### FGFR3

- **velocity_elasticity** — oral infigratinib 0.25 mg/kg/day: LS mean difference vs
  placebo **+1.74 cm/yr, 95% CI 1.31–2.17, p<0.001**, week 52; **n=114** (75 infigratinib
  / 39 placebo), achondroplasia aged 3–17 y, phase 3 NCT06164951 (`savarirayan2026infig`).
  Height z-score difference +0.32 (96% CI 0.23–0.41).
  **Counter-evidence in the same pathway:** the soluble FGFR3 decoy recifercept gave an
  observed/expected height-change ratio of **1.0 (95% CI 0.8–1.1)** at month 12 in all
  three arms — a null — and the programme was terminated with n=95 enrolled
  (`nct04638153`, `nct05116046`). Because no tissue concentration was measured, the
  failure **cannot be attributed between mechanism and delivery** (`g_l12b_006`).
  Allele-dependence is documented and unresolved: infigratinib IC50 0.66 nM (WT), 0.5 nM
  (K650E), 44.4 nM (K650M), 505.9 nM (V555M) (`ryu2022`, no CIs); it is a **weak inhibitor
  of N540K** (hypochondroplasia) (`ursachi2026_2`), and its IC50 against **G380R — the
  allele it is licensed-track to treat — has never been measured** (`g_l12b_005`,
  `g_mr002_allele`).
- **final_height_elasticity** — `unmeasured`. 0 programmes reporting final or near-adult
  height (`g_l12b_001`).
- **gwas_enrichment** — **PRESENT.** "FGF signalling" is one of six pathway families named
  in wood2014 (697 variants, n=253,288).
- **mendelian_burden** — **HIGH.** Achondroplasia adult height **132 cm (M) / 124 cm (F)**,
  European GAMLSS reference from **n=466** children, 4,375 measurement occasions
  (`merker2018`; SDs not separately reported). G380R on **16/16** achondroplasia
  chromosomes (`shiang1994`). Thanatophoric dysplasia birth prevalence 1 in 20,000,
  perinatal lethal; K650E in 16/16 TD2, R248C in 22/39 TD1 (`tavormina1995`).
  Hypochondroplasia N540K in 50–70% of cases. FGFR3 on the ClinGen commonest-dysplasia
  list. 2 of 102 ISS (`andrade2022`). *Note the direction: FGFR3 disorders are
  gain-of-function; this is a pathway that is fragile to being turned up, not down.*
- **graph_convergence** — Σ inbound 49; `fgfr3_receptor` rank **7** (22 inbound, 5 layers),
  `fgfr3_mapk_branch` rank 33, `mek1_erk_chondrocyte` rank 39, `achondroplasia` rank 75.

### GH–IGF1 somatotropic axis

- **velocity_elasticity** — **the largest of any pathway in the matrix.** rhGH across
  paediatric growth disorders **+3.0 to +5.0 cm/yr** (range across 20 studies, n=21,812;
  authors note **moderate-to-serious risk of bias**; `martn2026`). Weekly vs daily GH:
  lonapegsomatropin **+0.91 cm/yr, 95% CI 0.37–1.45, p=0.0010**, n=153 (`ying2026`).
  rhGH ± rhIGF-1, year 1: **9.3** (GH alone) vs **10.1 / 9.7 / 11.2 cm/yr** (+50 / +100 /
  +150 µg/kg rhIGF-1) — **non-monotonic in dose**, n=106 randomised, trial terminated;
  by year 4 the arms converge to 7.7 / 8.1 / 8.4 / 8.3 cm/yr (`nct00572156`).
- **final_height_elasticity** — rhIGF-1 in severe primary IGF-1 deficiency: **+0.9 height
  SDS (SD 1.1)** from initiation to near-adult height, **n=102** registry patients;
  **+1.4 SDS (SD 1.0)** in the treatment-naive prepubertal subgroup (`ramonkrauel2026`).
  **Registry, no control arm.** Only **10.5%** of Laron patients reached near-adult height
  in the normal range. rhGH height SDS gain **+0.3 to +0.9 SDS** (range across studies,
  same high-ROB review, `martn2026`).
- **gwas_enrichment** — **ABSENT: 0 of 3 analyses**, the anchor result of this document.
  Null established by search log `g_l8gen_001` (Europe PMC, 114 hits, 25 screened; hits
  dominated by livestock GWAS and unrelated human traits). ⚠ **Precision required:** the
  axis is not invisible to common variation — two-sample Mendelian randomisation gives
  **0.09 SD adult height per 1 SD genetically predicted serum IGF-1**, GIANT outcome
  sample n=1,176,465, persisting after adjustment for childhood BMI (`de2026`). What is
  absent is the axis *as an enriched pathway*, which is exactly what negative selection
  predicts: many small tolerated effects, no large ones.
- **mendelian_burden** — **the largest effect sizes in medicine.** GHR homozygous loss
  (Laron) **−4 to −10 SDS**, n=69 followed >50 y (`laron2015`). STAT5B null **−7.8 SDS**
  (114 cm at 16.4 y), IGF-1 7.2 ng/mL against a normal range of 242–600, n=1 (`hwa2005`).
  IGFALS deficiency **−2 to −3 SDS**, n=17 carrying 14 distinct mutations (`domen2009`).
  IGF1 homozygous partial deletion, n=1 (`woods1996`); IGF1R n=1 compound heterozygote of
  42 screened (`abuzzahab2003`); PAPPA2 2 homozygous mutations, both abolishing proteolytic
  activity, free IGF-1 decreased despite elevated total IGF-1 (`dauber2016`).
- **graph_convergence** — **the highest sum in the matrix, Σ inbound 96** across 16 member
  nodes; `igf1_systemic` rank **6** (25 inbound, 6 layers), `igf1_receptor` rank 12,
  `gh_receptor` rank 21, `stat5b_tf` rank 45. The graph and the Mendelian axis agree; the
  GWAS axis dissents, structurally.

### glucocorticoid

- **velocity_elasticity** — inhaled budesonide, dose–response on adult height regressed on
  daily dose in the **first 2 years**: **−0.1 cm per µg/kg/day, p=0.007**, n=943 (CAMP,
  `kelly2012`). A cm/yr elasticity is not reported by the trial and is not derived here.
  **Animal, not human, and must not be read as human fact:** local dexamethasone infusion
  (80 ng/µL at 1 µL/h) into one rabbit proximal tibia reduced growth rate by **77%,
  P<0.0001**, contralateral vehicle control, single dose level (`baron1992`, rabbit).
- **final_height_elasticity** — **the best-characterised final-height elasticity in the
  entire matrix, and it is negative.** Inhaled budesonide 400 µg/day for 4–6 years from
  age 5–13: adult height **−1.2 cm, 95% CI −1.9 to −0.5, p=0.001**, **n=943** measured at
  adult height in a randomised trial (`kelly2012`). Internal negative control in the same
  trial: nedocromil **−0.2 cm, 95% CI −0.9 to 0.5, p=0.61**. The deficit at 2 years was
  already **−1.3 cm (95% CI −1.7 to −0.9)** — **the cost was set within 2 years and did
  not grow thereafter.** No glucocorticoid-sparing agent has ever been carried to an
  attained-adult-height endpoint (0 agents, `g_l12b_023`); the deflazacort label makes no
  growth-advantage claim.
- **gwas_enrichment** — **ABSENT.** Not named in any of the three analyses.
- **mendelian_burden** — **LOW.** No monogenic disorder of the glucocorticoid pathway with
  a defined stature phenotype was identified. Cushing syndrome is acquired, not monogenic,
  and iatrogenic exposure vastly outnumbers endogenous disease. The genetic test in mouse
  is null: chondrocyte-specific inducible GR deletion produced **no detectable difference**
  in long bone length or growth plate structure at any age (`tu2014`, mouse) — endogenous
  glucocorticoid signalling in chondrocytes is dispensable for normal growth in mouse.
  The node `glucocorticoid_receptor` carries `human_evidence: absent`.
- **graph_convergence** — **Σ inbound 6, and not one member node reaches the top 80.**
  The lowest convergence of any pathway here. See §5 — this is a graph defect, not a
  biology result.

### HIF1A / hypoxia

- **velocity_elasticity** — `unmeasured`. No agent.
- **final_height_elasticity** — `unmeasured`.
- **gwas_enrichment** — **ABSENT.** Not named in any of the three analyses.
- **mendelian_burden** — **LOW.** No human monogenic disorder of HIF1A/VHL with a stature
  effect size was identified in this build.
- **graph_convergence** — Σ inbound 8; **0 members in the top 80**.
- **Human evidence on this pathway is absent in every sense.** The node
  `hif1a_chondrocyte` records that there is no HIF1A staining series and no oxygen
  measurement from any human growth plate. The mouse result is strong and specific
  (Schipani 2001: the plate interior is hypoxic; chondrocyte Hif1a deletion kills interior
  cells, lowers p57 and raises BrdU) and it has never been tested in a human. This
  pathway is in the matrix as a **documented five-axis absence**, which is a finding.

### matrix mineralization (TNAP / PPi / ENPP1)

- **velocity_elasticity** — measured on the **phosphate arm**, unmeasured on the PPi arm.
  Burosumab (anti-FGF23) in X-linked hypophosphataemia: **+0.085 height Z-score per year**
  in children (ages 2–17; 498 treated vs 143 naive; **P<0.0001**) and **+0.121 Z/yr** in
  adolescents, across **n=641** participants, median 3.3 y follow-up
  (`fukumoto2026`). **Observational real-world design, not randomised.**
  Asfotase alfa in perinatal/infantile hypophosphatasia has survival, not growth,
  endpoints: 1-year survival **95% vs 42%** historical (n=37 vs 48, p<0.0001), 5-year
  **84% vs 27%** (`whyte2016`).
- **final_height_elasticity** — `unmeasured`. No attained-adult-height endpoint for
  burosumab or asfotase alfa was retrieved.
- **gwas_enrichment** — **ABSENT.** Not named in any of the three analyses.
- **mendelian_burden** — **HIGH; stature effect size unmeasured.** ALPL loss of function →
  hypophosphatasia, perinatal-lethal through adult odontohypophosphatasia, with
  dominant-negative alleles severe in the heterozygous state; **ALPL is on the ClinGen
  commonest-dysplasia list** (`webb2026`). ENPP1 biallelic loss produces **generalised
  arterial calcification of infancy AND autosomal recessive hypophosphataemic rickets
  type 2 from the same alleles** — PPi deficiency and PPi excess both damage the plate.
  **No adult height in cm or SDS was retrieved for hypophosphatasia** — open quantitative
  gap.
- **graph_convergence** — Σ inbound 19, but concentrated in phenomenological nodes:
  `mineralization_front` rank 34 (8 inbound, 2 layers), `hydroxyapatite_nucleation` rank
  62. **The named enzymes carry almost nothing: TNAP 0 inbound, ANKH 0, ENPP1 1.**
  ⚠ Carries correction **CORR-001**: ANKH exports ATP, not PPi — the textbook mechanism
  was inferred in cells where ENPP1 was present and never excluded.

### mechanotransduction (PIEZO1 / TRPV4 / YAP-TAZ)

- **velocity_elasticity** — **measured, but not in humans and not in cm/yr per unit
  pathway modulation.** The only true elasticity is phenomenological and animal:
  growth-rate sensitivity to sustained stress **17.1% growth change per 0.1 MPa** (range
  across plates 9.2–23.9%/0.1 MPa; rat, rabbit, calf; 8 days; linear fit, **CI not
  reported**; `stokes2006`). Human data are surgical and angular, not molecular:
  tension-band guided growth corrects **0.67°/month** at the distal femur (SD 0.55) and
  **0.43°/month** at the proximal tibia (SD 0.38), **n=654 modulations in 313 children**
  (`tolk2026`). Human observational: gymnasts' peak height velocity **5.48 vs 8.0 cm/yr**
  in swimmers (SEM 0.32 / 0.50, p<0.05 at bone ages 11–13) — heavily selection-confounded,
  node graded D (`theintz1993`). **No pharmacological modulation of PIEZO1, TRPV4 or
  YAP/TAZ with a growth-rate readout exists in any postnatal physis, in any species.**
- **final_height_elasticity** — `unmeasured` for pathway modulation. Epiphysiodesis and
  guided growth change attained segment length, but by surgical ablation or tethering of
  the plate, not by modulating this pathway.
- **gwas_enrichment** — **ABSENT.** Not named in any of the three analyses.
- **mendelian_burden** — **HIGH, entirely via TRPV4.** TRPV4 is on the ClinGen
  commonest-dysplasia list (`webb2026`). Gain-of-function variants cause a graded series —
  metatropic dysplasia, spondylometaphyseal dysplasia Kozlowski, brachyolmia — all with
  severe short stature and metaphyseal disorganisation; **loss-of-function variants also
  produce SMD Kozlowski, so the dose–response is non-monotonic.** Small-molecule TRPV4
  inhibition rescues the mouse phenotype, so it is activity level and not presence that
  sets output. **No stature effect size in cm or SDS was retrieved.** PIEZO1 and YAP/TAZ
  have no human physeal evidence at all.
- **graph_convergence** — Σ inbound 19, but **13 of those 19 sit on one phenomenological
  node**, `mechanical_modulation_growth` (rank 17, **n_layers = 2** — L6 and L9 only).
  The named molecules carry: **PIEZO1 1 inbound, TRPV4 0, YAP/TAZ 0**. See §5.

### mTORC1

- **velocity_elasticity** — `unmeasured` in humans.
- **final_height_elasticity** — `unmeasured`.
- **gwas_enrichment** — **PRESENT.** "mTOR" is one of six pathway families named in
  wood2014 (697 variants, n=253,288).
- **mendelian_burden** — **LOW.** No human monogenic disorder of chondrocyte mTORC1 with a
  stature effect size was identified.
- **graph_convergence** — Σ inbound 12; `mtorc1_chondrocyte` rank 41 (7 inbound, 3 layers).
  The node carries `human_evidence: absent`, `species_basis: mouse`, confidence C: no
  study has measured phospho-S6 or phospho-4E-BP1 zonally in human growth plate tissue.
  ⚠ `phase3_close.md` §4 records that **IGF1R → mTORC1 in cartilage is unsubstantiated** —
  the single cartilage experiment coupling this receptor family to mTORC1 used **insulin,
  not IGF-1**. See §5.

### PTHrP / IHH

- **velocity_elasticity** — `unmeasured`, and the reason is unusually clean: **no PTH1R
  agonist has ever been administered to a human with open epiphyses with a prospectively
  reported linear-growth endpoint** (`g_l12l7_006`, `g_l12b_019`). Teriparatide: **0**
  paediatric trials with a linear-growth endpoint; the FDA label instructs avoidance in
  patients with open epiphyses. Abaloparatide: **0** paediatric trials with any growth
  endpoint; not recommended with open epiphyses. This is a searched, established zero, not
  a missing search.
- **final_height_elasticity** — `unmeasured`.
- **gwas_enrichment** — **PRESENT, and the strongest of any pathway.** Hedgehog (IHH,
  HHIP, PTCH1) is a named enriched set in weedon2008. IHH also appears at the rare-coding
  tier in marouli2017 among variants with effects up to ~2 cm/allele.
- **mendelian_burden** — **HIGH.** Blomstrand chondrodysplasia: PTH1R loss with **no
  detectable PTH- or PTHrP-stimulated cAMP and no detectable inositol-phosphate response**
  (`jobert1998`, `karaplis1998`) — perinatal lethal, so no stature figure exists or can
  exist. Jansen metaphyseal chondrodysplasia: PTH1R constitutive activation, **n=24**
  natural-history series, 18/24 carrying H223R (`saito2018`). Heterozygous IHH: **4 of 102
  ISS patients — the commonest single gene in that panel** (`andrade2022`); of 16 IHH
  probands, **0** had classical brachydactyly A-1 and **5 were of normal height** with
  brachydactyly alone (`sentchordimont2020`), i.e. the allele is incompletely penetrant
  for stature.
- **graph_convergence** — Σ inbound 63; `ihh_protein` rank **11**,
  `pthrp_ihh_feedback_loop` rank **14**, `pth1r_receptor` rank **19**, `pthrp_protein`
  rank 58.

### RUNX2 / MEF2C / HDAC4

- **velocity_elasticity** — `unmeasured`.
- **final_height_elasticity** — `unmeasured`.
- **gwas_enrichment** — **ABSENT.** Not named in any of the three analyses. (weedon2008's
  cell-cycle/chromatin set is CDK6, HMGA2 and DLEU7 — a different set of genes.)
- **mendelian_burden** — **MODERATE, and poorly quantified in stature.** RUNX2
  heterozygous loss → cleidocranial dysplasia with short stature (Mundlos 1997); a 4.2 kb
  non-coding 3'UTR deletion causes it in one case (`mijovic2025`, n=1). HDAC4
  haploinsufficiency within 2q37 deletion: brachydactyly type E in **48% of n=103**,
  craniofacial features 86%, overweight/obesity 34% (`le2019`) — **but the height SDS of
  carriers of an *intragenic* HDAC4 loss-of-function variant, as distinct from a whole
  2q37 deletion, has never been reported** (open gap `g_l8gen_008`). MEF2C
  haploinsufficiency (5q14.3) is a neurodevelopmental syndrome **without a defined physeal
  phenotype**. RUNX2 is not on the ClinGen commonest-dysplasia list.
- **graph_convergence** — Σ inbound 17; `runx2_tf` rank 42 (7 inbound, 3 layers),
  `hdac4_protein` rank 59, `mef2c_tf` 2 inbound, `runx3_tf` 0.

### sex steroid / aromatase

- **velocity_elasticity** — **the clearest documented case in the matrix of a velocity
  gain that does not become height.** Anastrozole 1.0 mg/day or letrozole 2.5 mg/day in
  pubertal boys ≥10 y with ISS: combined gain in **predicted** adult height over 3 years
  **+1.3 cm, p=0.043**, **n=79**, open-label randomised, no between-arm difference; and
  **the gain observed at year 1 in both arms did not persist at years 2 and 3**
  (`zegarra2024`, reported qualitatively by the authors; mechanism unknown, open gap
  `g_l12b_015`). GnRH agonists act in the opposite direction on bone age: **−0.6 to −1.3
  years** of bone-age advancement (`martn2026`).
- **final_height_elasticity** — GnRH agonist in central precocious puberty **+3.5 to +4.5
  cm** (range across 20 studies, **n=21,812**; authors note **moderate-to-serious risk of
  bias**; `martn2026`). In boys with CPP specifically, final height minus target height
  **+1.2 cm, SD 5.9, p=0.047**, n=92 — **the SD is nearly five times the mean effect**
  (`cho2026`). Androgen therapy in constitutional delay **+1.78 cm, 95% CI 0.47–3.08,
  p=0.0076**, meta-analysis of 13 retrospective cohorts, **n=803** (`wang2026`);
  testosterone superior to oxandrolone by +2.64 cm (95% CI 1.44–3.80). Aromatase inhibitor
  + GH, propensity-matched: adult height SDS adjusted for target height **0.81 (SD 0.34)**
  anastrozole vs **0.60 (SD 0.28)** letrozole, n=32 per group (`cui2025`).
- **gwas_enrichment** — **ABSENT** at the pathway level: no sex-steroid or aromatase gene
  set is named in weedon2008, lango2010 or wood2014. Recorded separately: **AR** is one of
  the example genes carrying rare coding height alleles of up to ~2 cm in marouli2017 —
  a *rare* coding signal, not common variation.
- **mendelian_burden** — **HIGH, and the human evidence is uniquely decisive.** Homozygous
  disruptive ESR1 mutation: **204 cm** at age 28 with **incomplete epiphyseal closure
  despite elevated estradiol and estrone**, lumbar BMD 0.745 g/cm² (3.1 SD below the young
  adult mean), n=1 (`smith1994`). This case controls the confound the mouse cannot, and it
  is one of only two propositional-replication upgrades accepted in this build
  (`phase3_close.md` §2). Aromatase deficiency: tall untreated stature, n=2 index siblings
  plus 4 further (`morishima1995`); aromatase-deficient men show **severely impaired GH
  response to GHRH + arginine, P<0.001**, n=4 vs 12 (`rochira2010`). Dose–response is
  quantified in the normal range: EC50 for half-maximal pubertal growth acceleration
  **20 pmol/L morning 17β-estradiol (95% CI 13–31)** in 27 girls, and **6.5 pmol/L (95% CI
  3.2–13)** for a 50% velocity increase in 26 boys (`albin2012`, `albin2013`).
- **graph_convergence** — Σ inbound 25; `estrogen_receptor_alpha` rank 44 (6 inbound, **6
  layers**), `aromatase_cyp19a1` rank 46 (6 inbound, 5 layers), `gnrh_hormone` rank 57,
  `estradiol_hormone` rank 78. Low inbound counts but unusually **broad layer span** — the
  graph places this pathway thinly but everywhere.

### SOX9 / SOX trio

- **velocity_elasticity** — `unmeasured`.
- **final_height_elasticity** — `unmeasured`.
- **gwas_enrichment** — **ABSENT.** Not named in any of the three analyses.
- **mendelian_burden** — **HIGH; stature effect size unmeasured.** Heterozygous SOX9
  mutations and translocations cause campomelic dysplasia with bowed long bones,
  hypoplastic scapulae and XY sex reversal (Foster 1994; Wagner 1994) — **human
  haploinsufficiency alone is sufficient to derail skeletogenesis**, and SOX9 is on the
  ClinGen commonest-dysplasia list (`webb2026`). The disorder is largely lethal in the
  neonatal period, so an adult-height distribution does not exist. **No human data exist
  for SOX5 or SOX6** — the trio's human evidence is SOX9 only.
- **graph_convergence** — Σ inbound 16; `sox9_tf` rank **22** (11 inbound) but
  **n_layers = 2**. The atlas's own node text calls SOX9 "the single most convergent node
  in L3" — and the graph agrees **only within L3**. See §5.

### thyroid hormone

- **velocity_elasticity** — `unmeasured` as an elasticity. Catch-up growth on
  levothyroxine is universal clinically, but no dose-ranging study giving cm/yr per unit of
  T3 exposure was retrieved. Nearest quantitative handle is a rat kinetic result — T3
  induces alkaline phosphatase, collagen X mRNA and matrix in **7 days** in rat tibial
  growth plate chondrocytes (`robson2000`, rat) — which is not a human elasticity.
- **final_height_elasticity** — **measured, and it is the "prevention works" cell.** Final
  height in screened and treated congenital hypothyroidism **−0.1 SDS (SD 1.0)** against a
  target height of −0.8 SDS, difference from target **P<0.001**, **n=215**, 20-year Italian
  cohort (`delvecchio2015`). **Uncontrolled by necessity** — an untreated arm cannot exist.
  Congenital hypothyroidism has become an experiment in *timing*, not in presence/absence.
- **gwas_enrichment** — **ABSENT.** Not named in any of the three analyses.
- **mendelian_burden** — **HIGH on qualitative severity; stature effect size unmeasured.**
  Untreated congenital hypothyroidism arrests the plate at the resting/proliferative stage
  — chondrocytes fail to undergo terminal hypertrophy, secondary ossification centres fail
  to appear (epiphyseal dysgenesis), with severe disproportionate short stature. **No
  modern SDS figure exists**, because screening prevents the phenotype. THRA
  dominant-negative variants (resistance to thyroid hormone α) cause growth retardation
  and delayed bone age, with **up to +2.5 SDS height gain on rhGH in one patient**
  (`jorge2025`) — implying a large deficit, but by inference. MCT8 deficiency:
  Triac lowered serum T3 from 4.58 to 1.66 nmol/L (mean decrease 2.92, 95% CI 2.61–3.23)
  in **n=67**, with **no stature endpoint** (`van2022`).
  ⚠ Species conflict on record: human THRA loss gives the skeletal phenotype, while mouse
  chondrocyte data assign the differentiation response to TRβ.
- **graph_convergence** — Σ inbound 11; `thyroid_hormone_t3` rank 53 (6 inbound, 2 layers);
  THRA 2, THRB 2, T4 0, MCT8 0, DIO3 0.

### WNT / β-catenin

- **velocity_elasticity** — `unmeasured`. No human agent modulating WNT with a
  linear-growth endpoint.
- **final_height_elasticity** — `unmeasured`.
- **gwas_enrichment** — **PRESENT.** "WNT/β-catenin" is one of six pathway families named
  in wood2014 (697 variants, n=253,288).
- **mendelian_burden** — **LOW, and the negative is the point.** LRP5 supplies a rare
  two-sided human dose experiment: biallelic loss → osteoporosis-pseudoglioma syndrome
  (Gong 2001); heterozygous G171V, impairing DKK1 binding → autosomal dominant high bone
  mass (Boyden 2002). **Both phenotypes are dominated by bone mass, not stature** — the
  human LRP5 readout is osteoblastic, not clearly physeal. Whether WNT signalling in the
  growth plate chondrocyte contributes to human height has not been tested.
- **graph_convergence** — Σ inbound 22; `wnt_canonical_chondrocyte` rank 43 (7 inbound,
  **n_layers = 2**), `beta_catenin_ctnnb1` rank 51 (6 inbound, **n_layers = 2**).
  `beta_catenin_ctnnb1` carries `human_evidence: absent`, `species_basis: mouse`,
  confidence C — while its node text calls SOX9/β-catenin reciprocal inhibition "the single
  most important convergence in the layer". See §5.

---

## 4. Quadrant assignment

Every pathway is assigned. The thresholds are those stated in §1; they are arbitrary at
the margin and are written down so the assignment can be re-run against different ones.

### Quadrant A — high mendelian / absent GWAS enrichment (n = 8)

**Essential and constrained. Poor targets for explaining why people differ in height.
Potentially high-leverage for intervention, precisely because the system is not buffered
against changing them.**

CNP/NPR2/PKG · collagen II/X/XI · GH–IGF1 somatotropic · matrix mineralization ·
mechanotransduction (via TRPV4) · sex steroid/aromatase · SOX9/SOX trio · thyroid hormone

The interpretation is not that these pathways are unimportant to height. It is that
**common variation cannot live there**, so an association study cannot see them. Two of
the four pathways in the whole matrix with any measured final-height elasticity sit in
this quadrant (GH–IGF1, sex steroid), and a third (thyroid) sits here too. **The quadrant
with the least common-variant signal contains three of the four pathways where a human
intervention has been shown to move adult stature.** That is the practical content of the
divergence.

Note the internal heterogeneity, which a single ordering would erase:
- **GH–IGF1** has the largest velocity elasticity *and* the largest Mendelian effects *and*
  the highest graph convergence — and zero GWAS enrichment.
- **CNP/NPR2** has a strong velocity elasticity and no final-height data at all.
- **SOX9**, **thyroid** and **mineralization** have high Mendelian fragility with **no
  stature effect size measured** — three open quantitative gaps.
- **mechanotransduction** qualifies only through TRPV4; PIEZO1 and YAP/TAZ contribute
  nothing to any axis.

### Quadrant B — high GWAS / low mendelian (n = 2)

**Tolerant and tunable; plausible substrate of normal-range height variation.**

mTORC1 · WNT/β-catenin

Both are named enriched pathways in wood2014 (n=253,288) and neither has a human monogenic
disorder with a defined stature deficit. This is what a pathway that generates normal
variation is supposed to look like: many small tolerated effects, no catastrophic ones.
**Neither has any human interventional data whatsoever** — both elasticity cells are
`unmeasured`. They are candidate explanations for variation and non-candidates for
intervention, which is the exact inverse of Quadrant A.

### Quadrant C — high on BOTH (n = 4)

**Rare and important: the pathways where common variation and fragility coincide.
Enumerated in full.**

| pathway | common-variant evidence | fragility evidence |
|---|---|---|
| **aggrecan / proteoglycan** | ACAN + ADAMTSL3 (weedon2008); chondroitin sulfate, osteoglycin, HA binding (wood2014); PG/GAG synthesis at rare-coding tier (marouli2017) — **the only pathway present at all three tiers** | heterozygous ACAN adult height **−2.8 SDS**, n=103, 20 families |
| **BMP / TGF-β** ⚠ boundary | **locus, not pathway**: GDF5–UQCC **0.44 cm/allele**, P<1e-15, n=6,669+28,801 | GDF5 LoF → Grebe / Hunter-Thompson acromesomelic chondrodysplasia; LTBP3 → brachyolmia. **SDS unmeasured** |
| **FGFR3** | FGF signalling (wood2014, n=253,288) | achondroplasia adult height 132/124 cm, n=466; TD lethal; ClinGen list |
| **PTHrP / IHH** | Hedgehog: IHH, HHIP, PTCH1 (weedon2008); IHH at rare-coding tier (marouli2017) | Blomstrand lethal (PTH1R null); Jansen n=24; IHH in **4/102 ISS**, the commonest single gene in that panel |

**BMP/TGF-β is flagged as a boundary case.** It qualifies on a single gene, not on a
pathway-level enrichment result, and its Mendelian side has no effect size in cm or SDS.
Under a stricter rule (pathway-level enrichment only) it would move to Quadrant A. It is
reported here with the rule that placed it, so the call can be reversed.

These four are the pathways where the two evidence bases actually agree — and note that
**three of the four are the same three the divergence node identified as convergent**
(Hedgehog, proteoglycan/GAG, and — asserted but *not* corroborated — CNP/NPR2). This build
finds Hedgehog and proteoglycan confirmed, CNP/NPR2 **not** confirmed (see the flagged
discrepancy under CNP/NPR2 in §3), and FGFR3 and BMP/GDF5 added.

### Quadrant D — high convergence / low on both genetic axes (n = 0 at pathway level)

**Empty under the strict rule — and an empty self-audit is not a passed self-audit.**

No pathway has a top-25 convergence node while scoring low on both `gwas_enrichment` and
`mendelian_burden`. Every top-25 node in the matrix belongs to a pathway that is corroborated
by at least one genetic axis.

Taken at face value this says the atlas has not over-connected any pathway. That
conclusion should be distrusted, because the test is too coarse: it operates on pathway
aggregates, and over-connection lives at the **node** level. §5 re-runs it there and finds
four flags.

### Residual — low on mendelian, absent from GWAS, low convergence (n = 3)

**The four-quadrant scheme has a hole, and three pathways fall through it.**

glucocorticoid · HIF1A/hypoxia · RUNX2/MEF2C/HDAC4

The scheme is built from two genetic axes and one graph axis. It has **nothing to say
about a pathway whose evidence is purely pharmacological**. That is not a rounding error:

- **Glucocorticoid holds the best-measured final-height elasticity in the entire matrix**
  — **−1.2 cm, 95% CI −1.9 to −0.5, p=0.001, n=943, randomised, with an internal negative
  control** — and it is low on the Mendelian axis, absent from GWAS, and has **the lowest
  graph convergence of any pathway here (0 nodes in the top 80)**. A ranking built from
  the genetic and graph axes would place near the bottom the one pathway whose effect on
  adult human stature is best established by randomised evidence.
- **HIF1A** is the opposite: nothing on four axes and low on the fifth, with no human data
  of any kind.
- **RUNX2/MEF2C/HDAC4** sits here because its Mendelian burden, though real, is
  unquantified in stature — a measurement gap, not a biological finding.

This residual is the sharpest single argument in the document against collapsing the axes.
Any consensus score would have had to place glucocorticoid and HIF1A near each other. They
could not be further apart.

---

## 5. Self-audit: is the graph over-connecting fashionable pathways?

Literature-derived graphs over-connect what is well studied, because edges are drawn from
papers and papers are written about fashionable things. Quadrant D was the check for this,
and at pathway level it came back empty. Run at node level, using two signals the
pathway aggregate hides — **`n_layers` (an edge count concentrated inside one layer is
intra-domain chatter, not cross-domain convergence)** and **`human_evidence` on the node
itself** — it does not come back empty.

### Flagged as graph-over-connected (4)

| pathway | graph prominence | what corroborates it | the flag |
|---|---|---|---|
| **WNT / β-catenin** | rank 43 + rank 51, Σ22 | GWAS pathway named (wood2014); **no human stature gene** | Both top nodes have **n_layers = 2 — entirely intra-L3**. `beta_catenin_ctnnb1` is `human_evidence: absent`, mouse-only, confidence C, yet its node text calls this "the single most important convergence in the layer". A heavily-studied mouse pathway generating intra-layer edges. |
| **mTORC1** | rank 41, Σ12 | GWAS pathway named (wood2014); **no human monogenic stature disorder** | `human_evidence: absent`, mouse-only, confidence C. **`phase3_close.md` §4 already found the IGF1R → mTORC1 cartilage link unsubstantiated** — the one experiment used **insulin, not IGF-1**. An edge into a hub, resting on the wrong ligand. |
| **BMP / TGF-β** | rank 35, Σ18 | GDF5 locus + human dysplasias | `bmp_signaling_growth_plate` has **n_layers = 1** — **all 8 inbound edges originate inside L3**. Zero cross-layer corroboration for the layer's third-ranked signalling hub. |
| **mechanotransduction** | rank 17, Σ19 | TRPV4 dysplasias (real) | **13 of 19 inbound edges sit on `mechanical_modulation_growth`**, a phenomenological node with **n_layers = 2** (L6+L9 only). The molecules the pathway is named for carry **PIEZO1 1, TRPV4 0, YAP/TAZ 0**. `yap_taz_chondrocyte` is confidence **E**, `human_evidence: absent`, and its own text states the pathway "is highly plausible and widely asserted for the growth plate, and the specific experiment has not been done." The graph has connected the *phenomenon* densely and the *mechanism* not at all — and then the pathway inherits the phenomenon's rank. |

**These are flags on the graph, not on the biology.** None of the four is a claim that WNT,
mTORC1, BMP or mechanotransduction is unimportant. Three of the four have real human
support on some axis. The claim is narrower and checkable: **their position in the
convergence ranking is not earned by cross-layer, human-corroborated edges**, and a
perturbation traversal weighting nodes by inbound degree would over-weight them.

Suggested remediation, in the order it should be attempted:
1. Report convergence as **(inbound, n_layers)** everywhere, never as inbound alone. A
   node with 8 inbound edges from one layer is not comparable to a node with 8 from six.
2. Re-audit the L3-internal edges into `bmp_signaling_growth_plate`,
   `wnt_canonical_chondrocyte` and `beta_catenin_ctnnb1` for source independence — the
   propositional-replication rule rejected 10 of 12 candidate replications in this build
   (83%), and there is no reason to expect edges to be cleaner than upgrades.
3. Split `mechanical_modulation_growth` from the molecular mechanotransduction nodes in
   any ranking, so a phenomenological hub cannot lend its degree to unevidenced molecules.

### Flagged for the opposite defect — graph *under*-connection (2)

An over-connection audit that only looks for over-connection will miss the mirror failure,
which is equally damaging to a perturbation traversal.

- **glucocorticoid — Σ inbound 6, zero nodes in the top 80.** This pathway holds the
  matrix's only randomised, internally-controlled, attained-adult-height result
  (−1.2 cm, 95% CI −1.9 to −0.5, n=943) plus a dose–response (−0.1 cm per µg/kg/day,
  p=0.007). It is the **best-evidenced human intervention in the entire matrix and the
  worst-connected pathway in the graph.** The likely cause is structural: glucocorticoid
  effects enter through L12 and L11 as *exposures*, not as L3 signalling edges, so they
  never accumulate inbound degree. Fixing this is an L4→L3 seam problem.
- **HIF1A/hypoxia — Σ inbound 8, zero nodes in the top 80, `human_evidence: absent`.**
  Here low connectivity is **correct and honest**: there is no HIF1A staining series and
  no oxygen measurement from any human growth plate. The graph is right to be thin. This
  entry is included to show the audit distinguishes "thin because unevidenced" (correct)
  from "thin because mis-seamed" (a defect) — glucocorticoid is the second, HIF1A the
  first.

---

## 6. What this matrix does not license

- **It does not rank pathways.** There is no ordering in this document and none should be
  extracted from it. Column-wise comparison is legitimate; row-wise aggregation is not.
- **It does not convert velocity into height.** The conversion factor is unknown
  (`g_l12b_016`), and is demonstrably **not** 1 in at least three places: aromatase
  inhibitors (year-1 gain lost by years 2–3), inhaled glucocorticoids (cost fixed inside 2
  years), rhGH in ACAN deficiency (velocity decays within treatment). **13 of 17 pathways
  have no attained-adult-height number at all.**
- **It does not treat absence from a GWAS enrichment list as evidence of unimportance.**
  That inference is the error this document exists to prevent. It is evidence about
  tolerance to common variation, and negative selection predicts exactly the observed
  pattern (zeng2018, oconnor2019).
- **It does not treat graph convergence as evidence of biological importance.** §5 flags
  four pathways whose rank is not earned, and two whose thinness is a seam artefact rather
  than a biological statement.
- **It does not state any mouse result as a human fact.** Where the only elasticity is
  animal — glucocorticoid (rabbit −77%), mechanotransduction (17.1%/0.1 MPa, multi-species)
  — that is marked in the cell.

## 7. Open gaps this matrix opens or sharpens

| gap | pathway | what is missing |
|---|---|---|
| `g_l12b_016` | all | the velocity→final-height conversion factor, and whether it differs by mechanism |
| `g_l12pharm_001`, `g_l12b_001` | CNP/NPR2, FGFR3 | attained final height under CNP-analogue or FGFR3-directed therapy — **both approvals are accelerated on a surrogate** |
| `g_l12b_002` | all | drug concentration inside human growth plate cartilage — **0 of 12 agents** |
| `g_l8gen_008` | RUNX2/HDAC4 | height SDS of intragenic HDAC4 LoF carriers, distinct from whole 2q37 deletion |
| new | SOX9, thyroid, mineralization, BMP, mechanotransduction | **stature effect size in SDS** for pathways scored HIGH on Mendelian burden by disorder severity alone — 8 half-measured cells |
| new | CNP/NPR2 | citation for, or retraction of, the claim that CNP/NPR2 is a convergent common/rare family (node `common_vs_rare_pathway_divergence`) |
| new | graph | re-audit of intra-layer inbound edges on `bmp_signaling_growth_plate`, `wnt_canonical_chondrocyte`, `beta_catenin_ctnnb1` for source independence |
| new | graph | L4→L3 seam for glucocorticoid: the best-evidenced human intervention has the worst-connected pathway |
