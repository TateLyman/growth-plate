# L13 — Methods and data

**41 nodes (0 stubs) · 80 edges touching the layer · 28 gaps · ~70 refs**
Confidence: A 11 · B 18 · C 10 · D 2. `human_evidence` direct 19 / indirect 11 / absent 11.
`translation_risk` high on 15 of 41.

This is the layer that measures the atlas's own foundations, and its central outputs are three
counts: **259 human growth plates ever examined histologically, 102 of them postnatal and
growing, and exactly 2 at or immediately before fusion.** No synthesis anywhere in this atlas can
exceed that record, and several of them are shorter and less satisfying because of it.

---

## 1. The settled core

**The human growth plate tissue corpus is countable, and it has been counted.** 259 distinct
donors across 21 of 30 located studies with stated n (a **lower bound** — nine further studies
state no donor count). **157** of those are fetal or perinatal **autopsy** specimens
(`rodriguez1992` 125, `werther1990` 20, `strangevognsen1997` 12). **102** are postnatal and
growing, and all are **surgical-waste provenance**. The largest single postnatal biopsy series is
**24 donors** (`nilsson2003`, proximal tibia, Tanner 1–5); the largest series of any age is 125
stillborns and newborns at 20–41 weeks (`rodriguez1992`). Donor counts per study range **1–24**.
Grade A.

**The only zone-resolved human growth plate transcriptome is GSE9160, and it is two children.**
Distal femur, an 11-year-10-month girl and a 13-year-3-month boy, five zones each, laser-capture
microdissection onto GPL570 arrays, 12,193 and 18,454 probe sets called present of ~54,000, inter-array
correlation ≥0.91 ± 0.01. That is **the complete human zonal transcriptome corpus** (`gse9160`).
The rat equivalent has 35 arrays (`gse16981`).

**The reference human tissue atlases contain no cartilage at all.** GTEx: **0 of 54 tissue sites**
are cartilage or growth plate — and its donors are aged 20–79, so by construction none has an open
physis. Human Cell Atlas: **0 projects** indexed to a cartilage or growth plate organ term,
against 6 for bone tissue and 9 for bone marrow (Azul index, 2026-08-05).

**The literature is 6.5:1 mouse.** GEO DataSets matching "growth plate": **1,472 records total —
919 mouse, 141 human.** Single-cell: 60 all species, 18 human. Spatial transcriptomics: **7 all
species, 0 human** (`geo_census_20260805`, `g_l13data_001`).

**Automated and manual measurement error are both quantified.** Knemometry is more sensitive to
inhaled corticosteroid systemic effect than 24-hour urinary cortisol excretion within the same
trial (`chawes2017`), at a typical 2-week crossover duration (`wolthers2017`).
`stadiometry_measurement_error`, `growth_velocity_measurement_interval` and `knemometry` are all
human, grade A or B.

---

## 2. The live disagreements

**The one thing three human studies tried to establish about oestrogen in the growth plate, they
established in opposite directions.** c-L13-01, logged on `immunohistochemistry_cartilage_artifact`
(which carries `CONTRADICTS: [nilsson2003, egerbacher2002]`). `nilsson2003` counted
receptor-positive cells by image analysis in proximal tibial biopsies from 16 boys and 8 girls
across Tanner 1–5: ERα and ERβ are **more** frequent in resting and proliferative zones
(64 ± 2% for ERα) than in the hypertrophic zone (38 ± 3%). `egerbacher2002` (4 epiphysiodesis
donors) and `nilsson1999` (4 female pubertal donors): ERα and ERβ staining is **restricted to
hypertrophic chondrocytes**, with resting and proliferative chondrocytes negative.

The gradient reported by one is the **exact inverse** of the restriction reported by the other
two, so this is not a difference of sensitivity. All three are human immunohistochemistry with
polyclonal antibodies of the era on decalcified or cryostat sections; **none reports antibody
validation against a knockout or blocking peptide, and none has been checked by an orthogonal
method in human tissue**. What hangs on it: every human zonal claim about oestrogen action, and
therefore the cellular target of the mechanism that terminates human growth (L7's
`estrogen_driven_fusion`, L4's receptor nodes, L2's `rz_depletion_causes_fusion`).

The atlas names the adjudicator and then names its limit: this is answerable at transcript level
against **GSE9160 — the only zone-resolved human transcriptome, which is two children** — or by
RNAscope (`g_l13b_005`). Both routes are open and neither has been taken.

**Nobody knows what dissociation does to a growth plate scRNA-seq experiment.** `g_l13b_003`
(quantitative_gap, tract 4): **0 published studies compare scRNA-seq zonal composition against
histological zonal composition in the same growth plate**, in any species. The concern is not
abstract — hypertrophic chondrocytes are the largest cells in the body relative to their lacunae
(human distal tibia terminal volume **5,900 µm³**, `white2008`) and are the most likely to be lost
or lysed. The first growth plate scRNA-seq study recovered **217 cells** (`gse76157`).
`chondrocyte_dissociation_bias` is graded **D** for exactly this reason, and it is a caveat on
every single-cell claim in L1, L2 and L3.

**The obvious fix has never been applied to human tissue.** `g_l13b_006` (search_established,
tract 4): single-nucleus RNA-seq is the standard solution to mineralised-matrix dissociation and
would unlock archival material, and it has **never** been used on human growth plate.
`snrna_seq_growth_plate` is grade B with `human_evidence: absent`.

**And the one human single-cell dataset that exists withholds its data.** GSE288028 — the only
human growth plate scRNA-seq deposit — has its raw human sequence data **withheld from the
repository**, stated verbatim in the GEO series record. **1 of 1.**

**The atlas's own model-species nodes disagree with the literature that uses them.**
`rat_growth_plate_model` (A, `he=absent`, `tr=high`), `mouse_model_translation_risk` (A,
`he=absent`, `tr=high`), `cre_lox_lineage_tracing` (A, `he=absent`, `tr=high`),
`lineage_tracing_limitations` (A, `he=absent`), `zebrafish_skeletal_model` (B, `he=absent`),
`metatarsal_explant_culture` (B, `he=absent`) — six grade-A/B methods nodes whose
`human_evidence` is **absent** by construction, because they *are* the animal apparatus. The
question `g_l13data_002` (tract 4) asks — what fraction of published growth plate mechanism rests
on mouse data, and **is that fraction acknowledged in the sources that transfer it to humans?** —
is the atlas's own reason for existing, and it is still open.

**Two model systems are contradicted at the level of the physical quantity they measure.**
`atomic_force_microscopy_cartilage` (C) and `finite_element_model_physis` (C) inherit L5's
four-way stiffness disagreement spanning **380 kPa to 416 MPa**. `computational_model_growth_plate`
(C) and `finite_element_model_physis` additionally inherit L6's missing input: in vivo human
physeal stress has never been measured, so every FE model of the physis takes an animal
coefficient and an unmeasured load.

---

## 3. The load-bearing assumption

**That surgical-waste human growth plate tissue is representative of a normal growing physis.**

Every human histological, immunohistochemical and transcriptomic number in this atlas rests on
it — the 24 cells per proliferative column, the 5,900 µm³ terminal hypertrophic volume, the
ER-alpha zonal fractions, GSE9160's five-zone expression profile, the AFM modulus profile, the
ToF-SIMS mineralization front, the two fusing specimens. There is no human growth plate datum
anywhere in this atlas that does not depend on it.

**All 102 postnatal donors are surgical waste.** The census records the provenance explicitly.
That means the tissue comes from children undergoing orthopaedic surgery: polydactyly digit
resection, epiphysiodesis for limb-length discrepancy, deformity correction, tumour margins. A
polydactylous digit's physis has been supernumerary since limb patterning; an epiphysiodesis
specimen is by definition from a limb whose growth was abnormal enough to warrant arresting it.
The other 157 donors are **fetal or perinatal autopsy**, i.e. tissue from pregnancies and infants
that ended.

**There is no normal control.** A healthy child's growth plate is not obtainable and never will
be, so the representativeness of the surgical-waste corpus cannot be tested against the thing it
is meant to represent. `g_l13b_010` (method_blocked, tract 3) states the adjacent structural
consequence: **no human growth plate can be sampled twice, so every human dataset is
cross-sectional** — which forecloses every within-subject inference, including every longitudinal
claim about how a plate changes as it approaches fusion.

The assumption's status is therefore permanent rather than merely unresolved, and the honest
response is not to abandon it but to bound it: `g_l13b_001` (search_established, tract 5) records
that **0 publicly catalogued human growth plate biobanks exist** and asks how much tissue is being
discarded annually in paediatric orthopaedic practice. A biobank with recorded provenance — site,
indication, age, sex, contralateral status — would not create normal tissue, but it would for the
first time allow the *variation across indications* to be measured, which is the only available
proxy for how much the surgical-waste channel distorts what the field sees.

---

## 4. What would change everything

**A catalogued human growth plate biobank with provenance metadata, coupled to single-nucleus
RNA-seq.** The two halves solve each other's problems: snRNA-seq works on mineralised and archival
material, which is what a biobank of surgical waste actually is, and it sidesteps the
dissociation bias that makes `chondrocyte_dissociation_bias` a grade-D caveat on every existing
single-cell dataset (`g_l13b_001`, `g_l13b_006`, `g_l13b_011`).

What it would change, concretely and immediately:
- **GSE9160 stops being the human transcriptome.** Two children from 2007 on a 2003-era array
  platform is currently the adjudicator the atlas proposes for at least three contradictions
  (c-L13-01, `g_l13b_005`, and several L3 zonal questions). Twenty donors across ages, sexes and
  sites would replace it.
- **The zonal questions L3 cannot answer become answerable.** Eight separate L3 searches for a
  human zonal measurement — BMP activity, mTORC1, oxygen, Notch, PDE isoforms, PCP asymmetry,
  cilium frequency, HDAC4 localisation — all returned nothing. Every one is a snRNA-seq or
  spatial-transcriptomics question.
- **The mouse-transfer question acquires a number.** `g_l13b_009` (quantitative_gap, tract 5) asks
  for the gene-by-gene concordance coefficient between the rat zone-resolved transcriptome (35
  arrays) and the human one (2 donors). That coefficient is the single most useful number the
  atlas could possess: it would put a measured value on the transfer that 919 mouse GEO records
  are silently performing.

And there is a cheaper first move that the layer has already scoped. The dataset inventory holds
**61 rows across GEO, SRA, ArrayExpress/BioStudies, HCA, GTEx and HPA; 45 map to at least one
existing atlas gap; 36 distinct gap_ids are addressable by reanalysis of already-public data.**
Thirty-six gaps in this atlas can be moved without generating a single new sample.

---

## 5. Numbers

| Parameter | Value | Unit | Species | Spread / n | Source | Flag |
|---|---|---|---|---|---|---|
| **Human growth plate donors ever examined** | **259** | donors | **human** | 21 of 30 located studies; **lower bound** | `human_gp_donor_census_20260805` | 9 studies state no n |
| — postnatal and growing | **102** | donors | **human** | **surgical-waste provenance only** | same | probable cohort overlap |
| — fetal / perinatal autopsy | 157 | donors | **human** | 125 + 20 + 12, exact sum | same | — |
| — **at or immediately before fusion** | **2** | plates | **human** | `white2008` n=1; `emons2009` n=1 | same | exhaustive |
| Largest postnatal biopsy series | 24 | donors | **human** | 16 boys, 8 girls, Tanner 1–5 | `nilsson2003` | — |
| Largest series of any age | 125 | donors | **human** | 46 stillborn + 79 newborn, 20–41 wk | `rodriguez1992` | — |
| Donors per human study | 1–24 | donors | **human** | full observed range, 21 studies | census | — |
| **Zone-resolved human transcriptome donors** | **2** | donors | **human** | 11y10m F, 13y3m M; distal femur; 5 zones | `gse9160` | **the complete corpus** |
| — probe sets present | 12,193 and 18,454 | of ~54,000 (GPL570) | **human** | inter-array r ≥ 0.91 ± 0.01 | `gse9160` | 2007 platform |
| Rat zonal microdissection arrays | 35 | arrays | rat | — | `gse16981` | — |
| GEO "growth plate" records | 1,472 (919 mouse / **141 human**) | records | multiple | ratio **6.5:1** | `geo_census_20260805` | point-in-time |
| GEO single-cell records | 60 (18 human) | records | multiple | — | same | — |
| GEO spatial transcriptomics | 7 (**0 human**) | records | multiple | exact zero at census | same | `g_l13data_001` |
| GTEx cartilage/growth plate tissues | **0 of 54** | tissue sites | **human** | donors aged 20–79 | `geo_census_l13b_20260805` | no open physes by design |
| HCA cartilage/growth plate projects | **0** (bone 6, marrow 9) | projects | **human** | Azul organ facet | same | `g_l13b_002` |
| Publicly catalogued human GP biobanks | **0** | repositories | **human** | full sweep | `human_gp_donor_census_20260805` | `g_l13b_001` |
| Human GP scRNA-seq deposits withholding raw data | **1 of 1** | datasets | **human** | GSE288028, stated verbatim | `gse288028` | — |
| scRNA-seq vs histology zonal composition comparisons | **0** | studies | any | Europe PMC + GEO sweep | `geo_census_l13b_20260805` | `g_l13b_003` |
| Cells in the first GP scRNA-seq study | 217 | cells | mouse | plate-based protocol | `gse76157` | — |
| Human zonal ISH transcript maps | **0** | systematic surveys | **human** | Europe PMC sweep | same | `g_l13b_005` |
| Terminal hypertrophic chondrocyte volume | 5,900 | µm³ | **human** distal tibia | no significant regional difference | `white2008` | **n = 1 specimen** |
| Cells per human proliferative column | 24 | cells | **human** | point estimate, no CI | `kember1976` | single source |
| Human PZ cycle time | **20** | days | **human** | derived from 24 cells + 1.4 cm/yr | `kember1976` | **derived; rodent = 2 days** |
| Human explant loading experiment donors | 3 | donors | **human** | 18 biopsies, 0.4 N at 0.77 Hz | `gse246390` | — |
| iPSC endochondral trajectory samples | 42 | samples | iPSC-derived | GSE219215 | `geo_census_l13b_20260805` | — |
| Dataset inventory rows / mapping to a gap / distinct gaps | 61 / 45 / **36** | datasets / datasets / gap_ids | multiple | judgement-based assignment | `geo_census_l13b_20260805` | reanalysable now |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l13b_001`** (search_established, tract 5) — does any catalogued human growth plate biobank
   exist, and how much tissue is discarded annually? The answer to the first half is **0**. The
   second half is answerable by auditing paediatric orthopaedic operative logs at a handful of
   centres, and it converts a permanent-sounding scarcity into a logistics problem.
2. **`g_l13b_006`** (search_established, tract 4) — apply snRNA-seq to human growth plate. It is
   the standard method for mineralised tissue, it unlocks archival blocks, and it has never been
   done. Discriminator against the existing scRNA-seq: if nuclear composition shows a far higher
   hypertrophic fraction than dissociated-cell composition from the same block, `g_l13b_003` is
   answered and every existing single-cell zonal proportion is biased in a known direction.
3. **`g_l13b_009`** (quantitative_gap, tract 5) — the rat–human zonal transcriptome concordance
   coefficient. Compute it now from `gse16981` (35 rat arrays) against `gse9160` (2 human donors),
   gene by gene, with orthologue mapping. A high coefficient licenses the transfer 919 mouse
   datasets are performing; a low one quantifies the atlas's central warning.
4. **`g_l13b_005`** (search_established, tract 4) — a modern branched-probe (RNAscope) zonal
   survey of human growth plate. This is the orthogonal method that adjudicates c-L13-01's
   inverted ER-alpha localisation, and it works on the archival blocks that already exist.
5. **`g_l13b_003`** (quantitative_gap, tract 4) — quantify dissociation loss. Split one growth
   plate: histology on one half, scRNA-seq on the other, compare zonal proportions. Until this is
   done, `chondrocyte_dissociation_bias` stays at grade D and every single-cell proportion in the
   atlas carries an unbounded error.
6. **`g_l13b_011`** (quantitative_gap, tract 5) — how fast does RNA integrity fall in human physeal
   cartilage as a function of post-resection interval and decalcification protocol, and what is
   the maximum usable delay? This is the operational parameter that determines whether a biobank
   is possible at all, and nobody has measured it.
7. **`g_l13b_012`** (method_blocked, tract 3) — is there any imaging modality, present or
   foreseeable, that resolves an individual chondrocyte inside a **living** human growth plate?
   If the answer is permanently no, then `g_l13b_007` (has proliferative kinetics ever been
   measured in a living human plate?) is permanently no too, and the field should invest in the
   best achievable substitute — which the atlas nominates as somatic-mutation clonal phylogeny,
   because it requires no labelling and no living observation.

---

## 7. Human-translation status

**19 of 41 nodes (46%) carry direct human evidence, 13 replicated; 11 have none; 15 of 41 carry
high translation risk.** For a methods layer those numbers mean something specific: **roughly a
quarter of the atlas's methodological apparatus is animal apparatus with no human counterpart, and
the atlas grades it A because it is well characterised, not because it transfers.**

The eleven `human_evidence: absent` nodes are the honest list of what cannot be done in a person:
`cre_lox_lineage_tracing`, `tamoxifen_inducible_creert2`, `lineage_tracing_limitations`,
`metatarsal_explant_culture`, `rat_growth_plate_model`, `mouse_model_translation_risk`,
`zebrafish_skeletal_model`, `in_situ_hybridization_cartilage` (mouse-dominant),
`snrna_seq_growth_plate`, `spatial_transcriptomics_growth_plate`, `tetracycline_labeling`. The
first three are why L2 has **zero** replicated-human nodes: clonal lineage tracing is the defining
technique of stem cell biology and it is impossible in humans, full stop.

Two of that list — `snrna_seq_growth_plate` and `spatial_transcriptomics_growth_plate` — are
different in kind and worth separating, because they are `he=absent` not by biological
impossibility but because **nobody has done it yet**. Spatial transcriptomics is grade A as a
method with 7 GEO records and **0 human growth plate applications**. That is the single most
closable gap in the layer.

The remaining human methods divide into the strong and the exposed. Strong: `knemometry`,
`mri_physis_imaging`, `synchrotron_imaging_cartilage`, `dxa_body_composition`,
`histomorphometry_physis`, `human_growth_plate_tissue_scarcity` — human, grade A or B,
not_applicable translation risk. Exposed: `stereology_growth_plate` (**grade D**, and it is the
method that produced L1's elongation budget in rat), `chondrocyte_dissociation_bias` (D),
`atomic_force_microscopy_cartilage` (C, inheriting a three-order-of-magnitude disagreement), and
`immunohistochemistry_cartilage_artifact` (B, and it exists to record that three human antibody
studies of the same protein reached opposite conclusions with no validation controls).

**The layer's summary of itself is the atlas's summary of itself:** the mechanisms are largely
available elsewhere; the honest accounting of which of them are human is not. Two numbers set the
ceiling on everything, and this layer is where they are computed — **259 human growth plates ever
examined, 102 postnatal, exactly 2 at fusion.**
