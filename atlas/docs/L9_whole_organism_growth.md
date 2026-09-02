# L9 — Whole-organism growth

**34 nodes (0 stubs) · 114 edges touching the layer · 34 gaps · ~60 refs**
Confidence: A 14 · B 11 · C 5 · D 4. `human_evidence` direct 30 (88%) / indirect 3 / absent 1.
`translation_risk` not_applicable on 27 of 34.

The highest direct-human fraction of any layer except L11 — and the layer with the fewest edges
per node in the atlas (114 edges touching 34 nodes, against 683 for L3's 88). That is the
finding: **L9 measures the output of the growth plate and is barely connected to it.**

---

## 1. The settled core

**Human growth has three additive components and the transitions are dated.** Karlberg's ICP
model: infancy, childhood, puberty. The childhood (GH-dependent) component switches on at
**6–12 months**, the infancy component has virtually ceased by **3 years**, and the
infancy–childhood spurt is **absent in 100% of untreated GH deficiency** while 30–50% of children
with other growth disorders show it delayed (`karlberg1987`, `karlberg1990`). Grade B.

**Peak height velocity is measured and sex-dimorphic.** SITAR fits: boys 9.61 cm/yr at 12.46 y,
girls 8.32 cm/yr, from 1,519 and 1,820 serial heights (`chun2024`). `preece_baines_model`,
`sitar_model`, `growth_velocity_curve` and `height_sds_z_score` are all grade A.

**Catch-up growth is quantitatively describable as a first-order approach to a target.**
Monomolecular functions fit **83–90%** of catch-up episodes; the rate constant *k* is
significantly higher in coeliac disease than in juvenile hypothyroidism (p = 0.02) or GH
deficiency (p = 0.004), while the asymptotic end value is similar across conditions, and GH dose
(conventional vs high) does **not** significantly change *k* (`wit2021`, n = 18 GHD). The dose
independence is the interesting part: the target and the approach rate look like properties of
the child, not of the treatment.

**Catch-down is real, bidirectional and complete by two years.** Infants born long relative to
parental height shift down; short ones shift up; the move onto the genetic channel is largely
complete by **age 2** (`smith1976`).

**Craniofacial and appendicular growth dissociate, and the cranial base has its own clock.**
Spheno-occipital synchondrosis fusion stages 3–4 at **12.7–13.9 y (males) and 11.0–12.5 y
(females)** in 630 subjects by 3D CT, with fusion stage correlating with cervical vertebral
maturation at **ρ = 0.955/0.964** and with chronological age at only 0.887/0.885
(`kim2024`) — it indexes maturation better than it indexes age.

**Brain and skeleton are not synchronised.** From 123,984 MRI scans in 101,457 participants:
peak grey matter volume 5.9 y (95% CI 5.8–6.1), cortical surface area 10.97 y, total cerebrum
12.5 y, subcortical grey 14.4 y, white matter **28.7 y** (`bethlehem2022`). Against female
age at peak height velocity of ~11.8 y, grey matter peaks **six years earlier**, and — the sharp
result — **0 of the charted brain tissue classes shows a velocity peak coincident with the
pubertal height spurt**. Whatever drives the growth spurt does not drive brain growth.

---

## 2. The live disagreements

**The dental clock runs independently of the skeletal clock under perturbation, and this is
the layer's cleanest dissociation.** In 48 children with untreated isolated GH deficiency, bone
age is delayed **1.99 years** while dental age is delayed **0.31 years** (against +0.41 y advance
in 48 healthy controls, p = 0.024) — a **1.68-year dissociation** — and, decisively, **the extent
of dental delay does not correlate with the extent of bone age delay within the same children**
(`torliskawalkow2026`). `van1998` finds the same shape in 48 short SGA subjects: skeletal
maturation delayed, dental age **not** delayed. `demirjian1985` found age at 90% dental maturity
uncorrelated with age at PHV, with menarche and with age at 75% skeletal maturity in the same 50
girls, **while PHV, menarche and skeletal maturity were significantly intercorrelated in those
same girls**.

The counterweight: in 280 unselected Peruvian schoolchildren, dental and skeletal maturity
correlate at **r = 0.85** (0.855 stunted, 0.863 control), and stunting affects neither dental
(p = 0.497) nor skeletal (p = 0.134) stage — though the correlation falls to 0.751 in delayed
maturers against 0.903 in advanced (`floresmir2005`). Reconciliation: the two clocks are
**correlated across a population and dissociated within an individual under endocrine or
nutritional stress**. `g_l9organism_010` asks why dental mineralization is insensitive to
perturbations that delay skeletal maturation by up to two years, and the answer is unknown —
which matters, because it means dental age is the only available maturational index that is
*not* contaminated by the growth disorder being assessed.

**Canalization contradicts the neuroendocrine catch-up hypothesis.** `canalization_growth`
carries an explicit `CONTRADICTS` against `neuroendocrine_catchup_hypothesis`: if catch-up were
locally generated in the plate (L2's `catch_up_growth`, which the Phase 2d audit **SCOPED** for
resting on an unread rabbit primary), there is no need for a central size sensor; if it is
neuroendocrine, there is. `marino2008` observed catch-up in **heart, liver and kidney mass** as
well, and explicitly allowed a systemic mechanism. L9 records both and resolves neither.

**The ICP model contradicts `holmgren2017`.** The three-component decomposition is the standard
framework and one primary disputes it; `icp_growth_model` carries the contradiction rather than
adopting the standard silently. And `g_l9organism_002` (tract 5) records that **the four
competing models — ICP, Preece-Baines, JPA-2, SITAR — have never been fitted to the same
individual curves with residual SDs reported**. Four grade-A/B methods, no head-to-head.

**Muscle–bone coupling: cause or coincidence?** `g_l9organism_013` (tract 4). Muscle mass and
bone mineral accrue together through puberty; whether muscle growth *causes* mineral accrual or
the two are independently timed and merely correlated has never been dissociated.
`muscle_bone_mechanical_coupling` is grade A as an observation and the causal claim is not
graded at all. `myostatin_mstn` (D) frames the natural experiment: does human loss of myostatin
signalling change **long bone length**, or only muscle mass (`g_l9organism_012`)? The answer
would settle the direction, and it is unknown.

---

## 3. The load-bearing assumption

**That mid-parental height with a fixed 6.5 cm sex correction predicts adult height within
±8.5 cm — and that this band is a measurement.**

It is not. `mid_parental_target_height` is grade A and used in every paediatric clinic on earth
to decide whether a short child is short *for their family*, which determines referral,
investigation and treatment. Both of its constants are conventions.

**The sex correction.** The additive 6.5 cm (`tanner1970`) assumes a constant male–female
difference. Under the CDC charts the difference is **12.2 cm at the 3rd percentile and 14.7 cm
at the 97th** — not constant. A **multiplicative** factor of 1.08 (male = 1.08 × female at
matched percentile) fits with **R² = 1** with the intercept forced to zero (`zeevi2024`).

**The band.** The ±8.5 cm range was asserted to correspond to the 3rd and 97th centiles and was
**theoretically derived, never measured**; Tanner himself later revised it to ±9 (girls) / ±10
(boys). Current guidelines (GH Research Society, LWPES, ESPE) recommend ±1.64 SDS, which under
CDC standards is **±10.6 cm (girls) and ±11.7 cm (boys)** — implying a predictive SD of
**6.5–7.1 cm**.

The measured residual SD is **4.7 cm (sons) and 4.4 cm (daughters)** pooled, and 4.5 (SD across
families 0.9) and 4.2 (SD 0.8) within families, in 303 adult children of 23 large nuclear
families (`zeevi2024`). The population-based Swedish estimate is compatible: a ±10 cm 95%
prediction interval implies SD ≈ 5.1 cm (`luo1998`, n = 2,402). **The guideline band is therefore
38–62% wider than the measured residual dispersion supports** (6.5–7.1 vs 4.4–4.7 cm), and the
consequence is directional and clinical: at SD 4.7, the probability a boy is ≥10 cm shorter than
his corrected target is **1.5%**, and 1.0% for girls. The guideline treats a 1-in-70 event as
within normal family variation.

Two further corrections matter and are routinely omitted. Uncorrected mid-parental height is
biased by **2.7 cm** (children taller than predicted, parents aged 62 ± 5), falling to **0.06 cm**
after a nonlinear parental-age correction. And target height explains only **36%** of the
variance in adult child height uncorrected, rising to 40% with all three corrections — the
regression slope of child on mid-parental height being 0.79 (`zeevi2024`), 0.78/0.75 for
boys/girls in the Swedish sample (`luo1998`).

The assumption's weakness is not that it is wrong in sign but that its uncertainty band is a
convention that has never been checked against its own residuals, and the one modern check
(n = 303, **23 families, a single Israeli/US Jewish cohort**) says the convention is half again
too wide.

---

## 4. What would change everything

**Replication of the residual-SD measurement in a population-representative, multi-ancestry
cohort** (`g_l9organism_004`, tract 4). Serial adult heights of children and both biological
parents, ≥5,000 families, ancestry-stratified, with parental age recorded.

If the residual SD is confirmed near 4.4–4.7 cm, the ±1.64 SDS guideline band is retired and
short-stature referral thresholds tighten measurably — more children with a genuine deviation
from familial target are identified, and fewer normal-variant children are investigated. If the
SD is larger in a representative population — plausible, since `zeevi2024`'s families are large,
Jewish, and unusually homogeneous, and residual dispersion was *not* found to depend on parental
height (r = 0.38, p = 0.08, n = 23 families, an underpowered null) — then the guideline band is
correct and the 2024 result is a founder-population artefact.

Either outcome is a rewrite, because the quantity is used millions of times a year and its two
plausible values differ by 50%.

Second, structural rather than clinical: **`g_l9organism_001`** (scale_gap, tract 2) —
**no published model has ever derived human height velocity in cm/yr from measured growth plate
cell kinetics** (chondrocyte production rate, hypertrophic cell height, column density). L1 has
the kinetics in rat and L9 has the velocity in humans, and nothing joins them. A model that
closed that gap would make the atlas's whole L1↔L9 axis quantitative and would immediately expose
whether Kember's derived ~20-day human cycle time (L1) is compatible with a measured 9.61 cm/yr
peak velocity.

---

## 5. Numbers

| Parameter | Value | Unit | Species | Spread / n | Source | Flag |
|---|---|---|---|---|---|---|
| Target height residual SD, sons / daughters | **4.7 / 4.4** (within-family 4.5 / 4.2) | cm | **human** | SD across families 0.9 / 0.8; n = 303, 23 families | `zeevi2024` | **single cohort** |
| Clinically quoted target band (Tanner) | **±8.5** | cm | human | **theoretically derived, never measured** | `zeevi2024` | convention |
| Guideline band at ±1.64 SDS | ±10.6 (girls) / ±11.7 (boys) | cm | **human** | implies predictive SD 6.5–7.1 cm | `zeevi2024` | **38–62% wider than measured** |
| Sex correction, additive vs multiplicative | 6.5 cm vs ×1.08 | — | **human** | ×1.08 fits with R² = 1 | `tanner1970` / `zeevi2024` | M–F gap 12.2→14.7 cm across centiles |
| Bias of uncorrected mid-parental height | 2.7 → 0.06 | cm | **human** | after nonlinear parental-age correction | `zeevi2024` | — |
| Variance in child height explained by target | 36 → 40 | % | **human** | uncorrected → all corrections | `zeevi2024` | — |
| Regression slope, child on mid-parental | 0.79 (0.78 boys / 0.75 girls) | cm/cm | **human** | n = 303 / n = 2,402 | `zeevi2024`, `luo1998` | replicated |
| Tanner method underestimation at MPH < −2 SDS | 6 (vs 2 for regression method) | cm | **human** | n = 2,402 | `luo1998` | — |
| P(child ≥10 cm below corrected target) | 1.5 (boys) / 1.0 (girls) | % | **human** | normal approximation on measured SD | `zeevi2024` | derived |
| Bone age vs dental age delay, untreated GHD | 1.99 vs 0.31 (**Δ 1.68**) | years | **human** | n = 48 vs 48 controls; p = 0.024 | `torliskawalkow2026` | **uncorrelated within individuals** |
| Dental–skeletal maturity correlation, unselected | 0.85 (0.751 in delayed maturers) | Pearson r | **human** | n = 280 | `floresmir2005` | contrasts with the above |
| Dental maturity vs PHV / menarche / skeletal | **not significant** (all three) | Pearson r | **human** | n = 50 girls; PHV–menarche–skeletal *were* correlated | `demirjian1985` | — |
| Peak height velocity, boys / girls | 9.61 / 8.32 | cm/yr | **human** | ±1.26 / ±1.09; APHV 12.46 y | `chun2024` | — |
| Catch-up episodes fitted monomolecularly | 83–90 | % | **human** | n = 20 + 18 | `wit2021` | — |
| Catch-up rate constant *k* vs GH dose | **not significant** | — | **human** | n = 18 GHD | `wit2021` | negative |
| Absent IC spurt in untreated GHD | 100 | % | **human** | n not given in abstract | `karlberg1990` | — |
| Childhood component onset / infancy cessation | 6–12 months / 3 years | age | **human** | per-individual estimate | `karlberg1990` | — |
| Peak grey / white matter volume | 5.9 / **28.7** | years | **human** | 95% CI 5.8–6.1 / 28.1–29.2; n = 101,457 | `bethlehem2022` | — |
| Brain metrics with a pubertal velocity peak | **0** | of 6 tissue classes | **human** | same resource | `bethlehem2022` | **null** |
| Spheno-occipital fusion stages 3–4 | 12.7–13.9 (M) / 11.0–12.5 (F) | years | **human** | n = 630; ρ 0.955/0.964 vs CVM | `kim2024` | — |
| Cranial base / mandible SDS in short SGA | −1.8 / ≤−1.7, lower face height **+1.7** | SDS | **human** | n = 48, 77 cephalograms | `van1998` | — |
| Arm span/height ratio, Japanese vs Dutch/Turkish | lower at every age, earlier plateau | ratio | **human** | n = 11,059 | `hirano2025` | direction only |
| Human organ-specific postnatal allometric exponents | **not located** | exponent | human | search returned none | — | `g_l9organism_017` |
| Models derived from plate cell kinetics → cm/yr | **0** | published models | human | — | — | `g_l9organism_001` |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l9organism_004`** (quantitative_gap, tract 4) — the target-height residual SD in a
   representative population. See §4. Highest clinical yield per unit effort in the atlas.
2. **`g_l9organism_005`** (contradiction, tract 4) — ±8.5 cm or ±1.64 SDS? Directly adjudicable
   from the same data as gap 1: compute the empirical 90% interval of adult height about corrected
   target and compare to both bands. There is no reason this has not been done except that nobody
   has treated the band as an estimable quantity.
3. **`g_l9organism_001`** (scale_gap, tract 2) — build the plate-kinetics → stature model. Inputs
   exist: chondrocyte production rate, hypertrophic cell height, column density (L1), plate count
   and share-of-growth (L1), velocity curves (L9). Discriminator: does the model reproduce the
   measured 9.61 cm/yr peak using human column counts (24 cells/column, `kember1976`) and any
   plausible cycle time? If not, one of the two literatures is wrong.
4. **`g_l9organism_010`** (known_unknown, tract 2) — why is dental mineralization insensitive to
   GH deficiency and undernutrition? Discriminator: measure GHR, IGF1R and THRA expression in
   human ameloblasts/odontoblasts against physeal chondrocytes. Absence of the receptor explains
   it; presence forces a downstream explanation and makes dental age a validated GH-independent
   maturational reference.
5. **`g_l9organism_002`** (quantitative_gap, tract 5) — fit ICP, Preece-Baines, JPA-2 and SITAR
   to the same individual curves and report residual SDs, overall and by growth-disorder subtype.
   Four grade-A/B methods have coexisted for 35 years without a head-to-head.
6. **`g_l9organism_012`** (known_unknown, tract 4) — does human myostatin loss change **long bone
   length** or only muscle mass? The human loss-of-function cases exist; nobody has published
   their segment lengths. This is the discriminator for `g_l9organism_013` (muscle→bone causation).
7. **`g_l9organism_006`** (quantitative_gap, tract 3) — the absolute rate constant *k* of human
   catch-up, in reciprocal years, and whether it scales with the duration of preceding
   suppression. `wit2021` reports *k* comparatively (coeliac > hypothyroidism > GHD) but not
   absolutely; the absolute value is what any model of growth-plate proliferative reserve (L2, L7)
   would have to reproduce.

---

## 7. Human-translation status

**30 of 34 nodes (88%) carry direct human evidence, 21 replicated, and 27 of 34 carry
`translation_risk: not_applicable`.** This layer is almost entirely built from human
anthropometry, human radiography, human MRI and human clinical cohorts, and the four exceptions
are precisely locatable: `mandibular_condylar_cartilage` (D, rat/mouse, `he=absent`),
`satellite_cell` (C, mouse-dominant), `skeletal_muscle_growth` (C) and
`muscle_hypertrophy_vs_hyperplasia` (C) — the muscle and craniofacial-cartilage nodes, which are
the parts of L9 that reach into tissue rather than staying at the level of the whole organism.
`g_l9organism_011` records the corresponding species question: does human skeletal muscle fix its
myofibre number early postnatally, as mouse EDL does by P21? Unknown.

The layer's real limitation is not species but **coupling**. Two structural gaps say it directly:
`g_l9organism_001` (no model links plate kinetics to stature velocity) and `g_l9organism_015`
(is there any evidenced mechanistic link between visceral organ growth and growth plate function,
or must the viscera be treated as an uncoupled parallel system?). The edge count agrees — 114
edges touch L9 against 683 touching L3 — and `g_l9organism_014` extends the same complaint to the
brain, where the timing data are now excellent (n = 101,457) and the mechanistic link to the
physis is nil.

So: **L9 is the layer where the atlas's human evidence is strongest and its explanatory reach is
weakest.** It can tell you, with confidence intervals, what a human child's growth does. It
cannot yet tell you which growth plate did it.
