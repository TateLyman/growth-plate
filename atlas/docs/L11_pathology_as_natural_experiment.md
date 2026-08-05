# L11 — Pathology as natural experiment

**56 nodes (0 stubs) · 307 edges touching the layer · 52 gaps · ~120 refs**
Confidence: A 19 · B 23 · C 14 · D 0 · E 0. `human_evidence` **direct on 56 of 56 (100%)**.
`translation_risk` **not_applicable on 56 of 56**. Every node is a `phenotype`.

No mouse in this layer. Also, as far as the atlas can establish, **no growth plate**: five
independent searches asked whether the physeal histology of any of these disorders has ever been
described in a living human, and five returned nothing.

---

## 1. The settled core

**The FGFR3 allelic series maps genotype to stature across the full survivable range, in
humans, with genotype frequencies.** Achondroplasia: G380R on **16/16** affected chromosomes in
the defining series (15× c.1138G>A, 1× c.1138G>C — the most mutable nucleotide in the genome
reached by two independent substitutions), adult height **132 cm (males) / 124 cm (females)**
from 466 children and 4,375 measurement occasions (`shiang1994`, `merker2018`).
Hypochondroplasia: N540K in **50–70%** of cases, genu varum 55%, macrocephaly 45% in the largest
single-genotype series (n = 20, `bellus1995`, `kim2023`). Thanatophoric dysplasia: birth
prevalence **1 in 20,000**, K650E in 16/16 TD2 cases and R248C in 22/39 TD1 cases
(`tavormina1995`), with 91 registry cases carrying matched genotype, radiology **and**
histopathology (`wilcox1998`).

**The GH–IGF axis is resolved by a chain of human nulls, each with a measured deficit.** STAT5B
null: height 114 cm at 16.4 y, **−7.8 SDS**, IGF-I 7.2 ng/mL against a 242–600 reference,
IGFBP-3 543 vs 2500–4800, ALS 1.22 vs 5.6–16 µg/mL — with **no rise on IGF-I generation testing**
(`hwa2005`, n = 1). IGF1 homozygous deletion (`woods1996`, n = 1) plus nine heterozygous cases
from six families (`joustra2025`). PAPP-A2 deficiency: two homozygous mutations, both abolishing
proteolysis, giving decreased **free** IGF-I despite elevated total IGF-I, IGF-II, IGFBP-3 and
IGFBP-5 (`dauber2016`). GHR deficiency: 201 adults in the Ecuadorian cohort with the
lowest lower-segment/height ratio and the highest head-circumference/height ratio of four groups,
the latter negatively correlated with serum IGF-I (`guevaraaguirre2025`).

**The CNP axis runs in both directions and the human dosage is bidirectional.** Loss:
AMDM (biallelic NPR2), NPR2 haploinsufficiency at ~3% yield among SHOX-negative disproportionate
short stature referrals (n = 268, `hisadooliva2015`), 2 pathogenic NPPC variants among 668
screened patients (`hisadooliva2018`). Gain: NPR2 p.Val883Met tall stature with constitutive
cGMP generation in the absence of CNP (`miura2012`, one three-generation pedigree); NPPC
overexpression from a t(2;7) breakpoint with **2-fold** plasma CNP (`bocciardi2007`, n = 1) and a
t(1;2) breakpoint mapped to **200,365 bp** downstream of NPPC (`ko2015`).

**Mutation class predicts severity, quantitatively, in two matrix genes.** COL10A1: missense
(dominant-negative) height Z **−3.62 (SD 1.95)** vs truncating (haploinsufficient) **−1.99
(SD 1.28)**, P = 0.013, n = 128; and age at onset 12 months for NC1-domain variants vs **72
months** for non-NC1, P = 0.0014 (`meng2025`). COMP: 830 patients, 471 probands, 224 distinct
variants across 106 articles — **80.8% missense, 87.7% in the type-3 calcium-binding repeat,
38.9% in exon 13** (`ni2026`).

**Sex-chromosome dosage gives SHOX its effect size.** Modelled across 45,X, 47,XXY, 47,XYY,
47,XXX and euploid adults in 1,225 aneuploid and 928,605 euploid individuals: **3.1 cm
(95% CI 1.9–4.3)** of extra height per unit Y-chromosome dosage over inactive-X dosage
(`berry2025`).

---

## 2. The live disagreements

**FGFR3 severity is non-monotonic in kinase activity — but only within one allele class, and
the atlas records the scope limit rather than the headline.** `tavormina1999`: **K650M (SADDAN)
has ~3× the constitutive kinase activity of K650E (thanatophoric dysplasia II), yet K650M is
survivable and K650E is lethal**; 3 of the 4 defining SADDAN individuals survived past infancy.
The pharmacology mirrors the inversion: infigratinib inhibits K650E at **0.5 nM** and K650M at
**44.4 nM** (`ryu2022`).

`saddan_syndrome` carries an explicit `CONTRADICTS` entry that is a **scope limit**, not a
counter-claim: *"the non-monotonicity result is specific to the kinase-domain pair K650E/K650M.
Across the kinase-domain-to-transmembrane comparison (K650E vs G380R) activation and severity DO
track together."* So the correct statement is: **within the kinase domain, activation and severity
are decoupled; across domains, they track.** That distinction is load-bearing for the entire
FGFR3 tyrosine kinase inhibitor class (C-L12-03), because "reduce kinase output, reduce severity"
is true across the allelic series and false inside it, and no published inference states which
regime it is invoking (`g_l11path_004`, `g_mr002_allele`).

**Two disorders produce short stature with opposite bone-age direction, and nobody knows why.**
ACAN haploinsufficiency: height **−2.8 SDS** (range −5.9 to −0.9, n = 103, 20 families) with bone
age **advanced +1.3 years** (range 0.0 to +3.7), early-onset osteoarthritis in 12/20 families and
disc disease in 9/20 (`gkourogianni2017`). X-linked hypophosphatemia: short stature with bone age
**delayed**. `g_l11path_021` (tract 3) asks the question directly and it has no candidate answer.
`g_l11path_011` (tract 4) sharpens it within ACAN alone: do the short stature and the advanced
bone age share one cause, or does bone age advance independently of the height deficit? Note the
mouse says the mechanism is *not* proliferative: *Acan*⁺/⁻ chondrocyte proliferation is
"**0 detectable change**" by histomorphometry (`bendre2025`).

**Same gene, same domain, different disease, and no explanation.** `g_l11path_019`: why do some
COMP alleles spare adult stature (multiple epiphyseal dysplasia — 15 children followed to ages
11–18 with height "normal or at the lower limit", median follow-up 5.5 y, `taner2026`) while
others in **the same type-3 repeat domain** cost 4–6 SD (pseudoachondroplasia)? 87.7% of
pseudoachondroplasia probands and 47% of MED variants are in COMP, and the domain does not
separate them.

**Blomstrand chondrodysplasia may not be a biallelic disease.** The Phase 2d audit found that the
`jobert1998` patient is **heterozygous** for the splice-creating point mutation, with the paternal
allele simply **not expressed by an unexplained mechanism**. Functionally biallelic, genotypically
not, n = 1. `g_l2d_007` opens the question of what silences the paternal allele and whether
Blomstrand is generally biallelic at all. The node's "biallelic loss of functional receptor" was
carrying more genetic weight than the primary supports.

**A cross-layer duplicate survived eight sweeps in this layer.** `acan_dosage_effect` (L5) and
`acan_related_short_stature` (L11) were the same entity — same cohort (103 individuals, 20
families), same three headline numbers, two aliases verbatim in common — and
`graph.py --duplicates` is structurally blind to it because the two ids share no substring. The
lesson for reading L11: a disorder node and a molecular node can describe the same measurement
under different names, and the graph will double-count the evidence unless a human checks.

---

## 3. The load-bearing assumption

**That the histological lesion in a skeletal dysplasia can be inferred from the radiographic
phenotype plus the mutated gene's known expression zone.**

This is what makes L11 useful to the rest of the atlas. Fifty-six human disorders with 100%
direct human evidence are worth having only if each one licenses a mechanistic inference — that
*ACAN* deficiency is a matrix lesion in the proliferative/resting zone, that *COL10A1* disease is
a hypertrophic-zone lesion, that *NPR2* loss shortens the hypertrophic zone as it does in the
mouse cKO (23% of control, L3). Twenty-seven edges run from L11 into L3 on exactly that reading.

**The atlas has one case where both the expression zone and the loss-of-function histology are
known, and the inference rule fails.** Collagen X is expressed **exclusively** in hypertrophic
chondrocytes. In the `Col10a1` null the **proliferative** zone is more compressed than the
hypertrophic — the primary says so explicitly, and the hypertrophic-dominant phenotype belongs to
the *dominant-interference transgenic*, a different mechanism (CORR-002, `gress2000`). The gene's
expression zone predicted the wrong compartment. `g_l11path_018` (tract 3) generalises the
question — *is the zone in which a cartilage matrix gene is expressed a general predictor of which
radiographic compartment fails when that gene is mutated?* — and the one available test says no.

The scale of the exposure is the five nulls. **No human growth plate has ever been described
for:**

| Gap | Disorder class | Status |
|---|---|---|
| `g_l11path_002` (tract 3) | achondroplasia, hypochondroplasia, SADDAN — in a **living** person | none found |
| `g_l11path_005` (tract 3) | any NPR2/NPPC dosage disorder (AMDM, haploinsufficiency, gain of function, NPPC overexpression) | none found |
| `g_l11path_007` (tract 2) | Laron syndrome or any severe GH insensitivity | none found |
| `g_l11path_010` (tract 3) | ACAN haploinsufficiency | none found |
| `g_l11path_025` (tract 4) | irradiated vs non-irradiated plate **within the same patient**, with dosimetry | none found |

The one exception proves the rule's cost: thanatophoric dysplasia has 91 registry cases with
matched genotype, radiology and histopathology (`wilcox1998`) — because it is lethal, so the
tissue is obtainable at autopsy. **Every disorder compatible with life is histologically
undescribed**, which means every mechanistic claim about a survivable human dysplasia is an
inference from a mouse or from a radiograph.

---

## 4. What would change everything

**A physeal tissue bank from dysplasia surgery.** Limb-lengthening osteotomy in achondroplasia
and hypochondroplasia, guided-growth and epiphysiodesis in ACAN deficiency and Turner syndrome,
and corrective osteotomy in pseudoachondroplasia and MED all remove or expose physeal tissue that
is currently discarded. Twenty specimens across five genotypes, with zone-annotated histology,
Ki-67, TUNEL, collagen II/X and phospho-ERK/phospho-STAT1, would close four of the five nulls at
once.

The specific rewrites available:
- If achondroplastic human plates show **normal proliferation with hypertrophic-zone apoptosis**,
  `legeaimallet1998`'s human fetal TD result generalises, C-L3-01 resolves against the murine
  proliferation-arrest model, and every FGFR3 programme's preclinical endpoint (proliferation
  index in mouse) is measuring the wrong thing (`g_l12l7_005`).
- If *ACAN*⁺/⁻ plates show impaired **hypertrophy** with intact proliferation, the mouse
  (`bendre2025`: 0 detectable proliferative change) is validated and the advanced bone age becomes
  a hypertrophy-acceleration phenotype rather than a maturation phenotype (`g_l11path_010/011`).
- If *NPR2* haploinsufficient plates show a **short hypertrophic zone**, the mouse cKO's 23%
  figure transfers and vosoritide's mechanism is confirmed at the tissue level in humans for the
  first time (`g_l11path_005`).
- If any of the three shows a lesion in a zone the gene is not expressed in, `g_l11path_018`
  resolves as CORR-002 predicts, **and 27 L11→L3 edges need re-grading**.

---

## 5. Numbers

| Parameter | Value | Unit | Species | Spread / n | Source | Flag |
|---|---|---|---|---|---|---|
| Achondroplasia adult height | 132 (M) / 124 (F) | cm | **human** | n = 466 children, 4,375 occasions | `merker2018` | SD not separately reported |
| G380R among achondroplasia chromosomes | 16/16 (15× G>A, 1× G>C) | chromosomes | **human** | defining series | `shiang1994` | — |
| Hypochondroplasia N540K share | 50–70 | % of cases | **human** | 8/14 discovery; n = 20 largest series | `bellus1995`, `kim2023` | — |
| Thanatophoric dysplasia birth prevalence | 1 in 20,000 | live births | **human** | no CI reported | `tavormina1995` | — |
| K650E in TD2 / R248C in TD1 | 16/16 / 22/39 | cases | **human** | — | `tavormina1995` | — |
| **K650M vs K650E constitutive kinase activity** | **~3** | fold (K650M higher) | in vitro human cell | no CI; **K650M survivable, K650E lethal** | `tavormina1999` | **non-monotonic — kinase domain only** |
| Infigratinib IC50, K650E vs K650M | 0.5 vs 44.4 | nM | in vitro | radiometric panel | `ryu2022` | mirrors the inversion |
| ACAN heterozygote adult / childhood height | −2.8 / −2.0 | SDS median | **human** | ranges −5.9 to −0.9 / −4.2 to −0.6; n = 103 | `gkourogianni2017` | — |
| ACAN bone age advance | **+1.3** | years | **human** | median; range 0.0 to +3.7 | `gkourogianni2017` | opposite sign to XLH |
| *Acan*⁺/⁻ chondrocyte proliferation | **0** detectable change | — | mouse | histomorphometry | `bendre2025` | negative |
| COL10A1 missense vs truncating height Z | −3.62 vs −1.99 | SDS | **human** | SD 1.95 / 1.28; P = 0.013; n = 128 | `meng2025` | — |
| COL10A1 onset, NC1 vs non-NC1 | 12 vs 72 | months (median) | **human** | P = 0.0014 | `meng2025` | — |
| COL10A1 discovery linkage lod | 18.2 | lod (θ = 0) | **human** | single large kindred | `warman1993` | — |
| COMP variant distribution | 80.8 missense / 87.7 type-3 repeat / 38.9 exon 13 | % of probands | **human** | 830 patients, 471 probands, 224 variants | `ni2026` | — |
| MED variants in COMP / near-normal height | 47 / 15 children ages 11–18 | % / count | **human** | n = 22, median follow-up 5.5 y | `taner2026` | contrast with PSACH 4–6 SD |
| STAT5B-null height | 114 cm (**−7.8 SDS**) at 16.4 y | cm / SDS | **human** | **n = 1**; IGF-I 7.2 vs 242–600 ng/mL | `hwa2005` | n = 1 |
| PAPP-A2 proteolytic activity | **0** | % of wild type | in vitro human cell | 2 mutations, 2 families | `dauber2016` | — |
| Height per unit Y over inactive-X dosage | 3.1 | cm | **human** | 95% CI 1.9–4.3; 1,225 aneuploid vs 928,605 | `berry2025` | — |
| Plasma CNP, NPPC-translocation tall stature | 2 | fold | **human** | n = 1 vs 5 controls | `bocciardi2007` | n = 1 |
| t(1;2) breakpoint distance downstream of NPPC | 200,365 | bp | **human** | exact mapped | `ko2015` | n = 1 |
| NPPC pathogenic variants among screened patients | 2 / 668 | count | **human** | plus 29 families | `hisadooliva2018` | — |
| NPR2 yield, SHOX-negative disproportionate SS | ~3 | % | **human** | n = 268 | `hisadooliva2015` | — |
| NPR2 haploinsufficiency prevalence in ISS | 0 to 1/26 | proportion | **human** | — | `wang2015` | disputed (6% in `vasques2013`) |
| Pituitary gigantism: onset / diagnosis age F vs M | 13 median / 15.8 vs 21.5 | years | **human** | n = 208; 78.4% male; 84% macroadenoma | `rostomyan2015` | — |
| GPR101 p.E308D in acromegaly | 11/248 (4.4%) | patients | **human** | predominantly somatic | `trivellin2014` | — |
| Jansen: H223R share / paediatric bone histomorphometry | 18/24 / **2** | patients | **human** | five activating alleles in the series | `saito2018`, `pereira2025` | n = 2 |
| Human physeal histology in **living** dysplasia patients | **0** | descriptions | human | five independent searches | — | five nulls (§3) |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l11path_002`** (search_established, tract 3) — has any living person's achondroplastic,
   hypochondroplastic or SADDAN growth plate ever been described? The tissue bank in §4 is the
   answer. This gap alone gates C-L3-01, `g_l12l7_005` and the preclinical-endpoint question for
   the whole FGFR3 drug class.
2. **`g_l11path_004`** (contradiction, tract 3) — why is K650M survivable when K650E is lethal at
   one third the kinase activity? Discriminator: compare downstream branch engagement (pERK vs
   pSTAT1 vs receptor trafficking) for K650E, K650M and G380R **in one cell background at one ATP
   concentration**. Non-monotonicity that tracks branch identity rather than total activity
   explains it; equal branch profiles leave it unexplained and make the class premise unsafe.
3. **`g_l11path_021` + `g_l11path_011`** (known_unknown, tract 3–4) — why is bone age advanced in
   ACAN deficiency and delayed in XLH? Discriminator: measure hypertrophic zone height and
   mineralization-front advance rate in both, in human tissue or in the matched mouse models run
   side by side. Advanced bone age with a *taller* hypertrophic zone means accelerated maturation;
   with a normal one it means a separate maturation clock.
4. **`g_l11path_019`** (known_unknown, tract 3) — MED vs pseudoachondroplasia within the COMP
   type-3 repeat. Discriminator: assay ER retention and unfolded-protein-response activation for
   matched MED and PSACH variants in the same chondrocyte background. Retention burden predicting
   stature loss would make the severity axis proteostatic rather than structural.
5. **`g_l11path_009`** (quantitative_gap, tract 3) — what is the **upper bound** of human growth
   plate elongation? Lifelong GH excess from infancy (`pituitary_gigantism`, `xlag_gpr101`,
   n = 208) is the natural experiment; nobody has asked what terminates growth in those patients
   or what maximum the plate can deliver. This is the only route to an empirical ceiling on any
   growth-promoting therapy.
6. **`g_l11path_014`** (quantitative_gap, tract 4) — how many centimetres are attributable to SHOX
   dosage alone? Discriminator: compare the aneuploidy-derived estimate (3.1 cm per dosage unit,
   `berry2025`) against isolated SHOX deletion cohorts. Agreement validates dosage models;
   disagreement means the aneuploidy estimate is contaminated by the rest of the chromosome.
7. **`g_l11path_022`** (scale_gap, tract 4) — in systemic paediatric disease, what are the relative
   weights of inflammation, glucocorticoid exposure, undernutrition and acquired GH resistance?
   Four candidate causes, one endpoint, and no published partition — the L11 counterpart of L10's
   `g_l10env_008`.

---

## 7. Human-translation status

**100% of nodes carry direct human evidence and 100% carry `translation_risk: not_applicable`.**
On the coverage table this is the atlas's strongest layer, and the reason is definitional: every
node is a human disease phenotype, so there is no species to translate from.

That statistic conceals the layer's actual limitation, which is **level of observation, not
species**. What is human here is the *genotype* and the *stature*. What is not human — for any
survivable disorder — is everything in between.

- **17 of 56 nodes are replicated-human (30%)**, the lowest replication fraction of any
  high-human layer, because most of these disorders are rare and their defining evidence is one
  cohort, one family or one patient. `stat5b_deficiency`, `igf1_deficiency_human`,
  `nppc_duplication_tall_stature` and `estrogen_resistance_esr1` each rest on n = 1 for their
  central measurement; `npr2_gain_of_function_tall` on one pedigree; `saddan_syndrome` on four
  individuals; Jansen bone histomorphometry on two.
- **Fourteen nodes are grade C** — `allan_herndon_dudley`, `cancer_survivor_growth`,
  `celiac_disease_growth`, `cushing_syndrome_growth`, `irradiation_growth_plate_damage`,
  `juvenile_idiopathic_arthritis_growth`, `mucopolysaccharidosis_growth`,
  `osteogenesis_imperfecta_growth`, `spondyloepiphyseal_dysplasia` and others — because the
  height deficit is real and human but its attribution to the growth plate is not established.
  `g_l11path_020` (method_blocked) states the problem for OI and the MPS directly: how much of
  the adult height deficit is lost plate output and how much is mechanical loss from deformity
  and vertebral collapse? Unpartitioned.
- **The mechanistic reading of every node runs through a mouse.** Several nodes carry
  `sp=human,mouse` or `sp=human,in_vitro_human_cell` — `achondroplasia`, `hypochondroplasia`,
  `acan_related_short_stature`, `nppc_duplication_tall_stature`, `blomstrand_chondrodysplasia`,
  `jansen_metaphyseal_chondrodysplasia` — and in each case the human component is the phenotype
  and the animal or cell component is the mechanism.

The correct reading of any L11 answer: **the genotype–stature chain is human and solid; the
genotype–tissue chain is borrowed.** And the one time the atlas could check whether a gene's
expression zone predicts its lesion's zone, it did not (CORR-002).
