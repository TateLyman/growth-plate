# L4 — Endocrine and systemic control

**72 nodes (0 stubs) · 614 edges touching the layer · 42 gaps · ~110 refs**
Confidence: **A 32** · B 16 · C 12 · D 10 · E 2. `human_evidence` direct 46 (64%) / indirect 14 /
absent 12. `translation_risk` low or not_applicable on 36 of 72; high on 15.

This is the atlas's strongest mechanistic layer by human-evidence fraction, and the reason is
structural: endocrinology is measured in serum, serum is measurable in children, and the
somatotropic and gonadal axes have a complete human loss-of-function allelic series. Thirty-two
grade-A nodes is more than L1, L2, L3, L5 and L6 combined.

---

## 1. The settled core

**The GH→IGF-1 axis is resolved in humans gene by gene, and the phenotypes are ordered.**
GHR loss −4 to −10 SDS; STAT5B −7.8 SDS; IGFALS, IGF1 and PAPPA2 each with defined human
kindreds. This is the largest set of monogenic stature effects in medicine and it is entirely
human. Grade A across `gh_receptor`, `stat5b_tf`, `igf1_receptor`, `als_igfals`, `igfbp3`,
`igf_ternary_complex`, `pappa2_protease`.

**GH secretion is overwhelmingly pulsatile and the pulse statistics are human-measured.**
13.7–13.8 bursts per 24 h (95% CI 12.1–15.7, n = 37, 10-min sampling); **88%** of 24-h output
is pulsatile rather than basal (151–191 vs 14.5 units); total 172–238 mU/L per 24 h
(`van2016`). Sleep-dependence is grade B and human.

**Oestrogen, not androgen, terminates human growth — and the human natural experiment
controls the confound the mouse cannot.** A 28-year-old man homozygous for a disruptive ESR1
mutation reached **204 cm** with unfused epiphyses **despite elevated estradiol** and normal
masculinisation (`smith1994`, n = 1; lumbar BMD 0.745 g/cm², −3.1 SD). `estrogen_receptor_alpha`
was upgraded B→A in Phase 3 on exactly this pairing — mouse ERα-null continued growth
(+8.3% tibial length, +18% plate height at 16–19 months, `brjesson2012`) **plus** the human
case, which is a different species *and* controls for ligand availability. One of only **two
confidence upgrades accepted out of twelve tested**.

**The oestrogen dose–response is biphasic and the human EC50s exist.** Half-maximal pubertal
growth acceleration at morning 17β-estradiol of **20 pmol/L in girls** (95% CI 13–31, n = 27,
37 24-h profiles) and **6.5 pmol/L in boys** (95% CI 3.2–13, n = 26) by ultrasensitive
extraction assay (`albin2012`, `albin2013`) — against 24-h means across male puberty of
<4 / 6 / 8 / 21 / 32 pmol/L (`ankarberglindg2008`). The upper limb is human too and it is a
randomised crossover: in five boys, 4 µg/day iv estradiol for four days raised three-week
ulnar velocity from 0.45 to 1.38 mm (P < 0.05), while 20 µg/day gave 0.49→1.0 and 90 µg/day
gave 0.46→0.84, **neither significant** (`carusonicolett1985`). Higher dose, smaller effect,
in the same five children.

**IGF bioavailability, not IGF concentration, is what the plate sees — proven in humans.**
PAPP-A2 deficiency: serum total IGF-1 **831–1060 µg/L (elevated)**, IGFBP-3 4403–5912 µg/L
(reference 2206–4200), IGFBP-5 645–997 (reference 211–707), free IGF-1 0.27–1.98 µg/L
(reference 1.58–3.15), **bioactive/total IGF ratio 0.09–0.32% against a healthy median of
1.23%**, and height −2.16 to −3.81 SDS (`dauber2016`, n = 5). Mutant PAPP-A2 has **0%**
residual IGFBP proteolytic activity. High hormone, low growth.

---

## 2. The live disagreements

**Glucocorticoid: potent locally, dispensable genetically** (c_l4endo_02, gap `g_l4endo_011`,
tract 4). Unilateral intra-growth-plate dexamethasone (80 ng/µL at 1 µL/h) cut ipsilateral
rabbit proximal tibial growth by **77%** against the vehicle-infused contralateral plate in
the same animal (P < 0.0001, method error ~5%, `baron1992`). Tamoxifen-inducible
chondrocyte-specific GR knockout mice have **0% detectable difference** in knee architecture,
cartilage, growth plates, discs, long bone length or bone microarchitecture at every age
tested — impairment appeared only in metaphyseal fracture healing (`tu2014`). The two designs
answer different questions (pharmacological excess vs loss of endogenous tone) and are cited
as if they answered the same one. `glucocorticoid_cortisol` and `glucocorticoid_receptor`
carry reciprocal `CONTRADICTS`. The decisive experiment — unilateral local dexamethasone
infusion **in** a chondrocyte-specific GR knockout — has never been done.

**And the direction of the GC effect on SOX9 inverts across a 10,000-fold concentration
range** (C-L4-03, `g_l4l3_006`). `sekiya2001`: dexamethasone **raises** Sox9 mRNA and protein
in newborn mouse rib chondrocytes within 24 h, dose-dependent from 0.1 nM to 10 nM, with
parallel Col2a1 induction — which is why 100 nM dexamethasone is standard chondrogenic
medium. `song2012`: at **100 µM**, glucocorticoid suppresses SOX9, COL2 and aggrecan in human
knee articular chondrocytes via p38 inactivation, transcriptionally and **before** any
apoptotic effect. The atlas records `sign: biphasic` rather than resolving it. If the low-dose
limb is physiological, glucocorticoid growth arrest is **not** a SOX9 lesion and must run
through local GH/IGF-1 resistance, IHH suppression and PI3K-AKT apoptosis instead — a
completely different set of edges.

**Which thyroid receptor isoform acts on cartilage?** (C-L4-04 / c_l4endo_01, `g_l4endo_007`).
In primary neonatal mouse rib chondrocytes, T3 lowered proliferation and accelerated
differentiation normally without TRα but **every** T3 response was abrogated without TRβ
(`rabier2006`); THRβ1 binds a TRE in the distal *Ihh* promoter and the TRβ-selective agonist
GC1 raises epiphyseal *Ihh* ~100-fold (`xing2016`). Against this, human dominant-negative
*THRA* variants cause disharmonious short stature with delayed bone age, while
dominant-negative *THRB* (RTHβ) is common and typically **not** associated with short stature
(`jorge2025`). Localisation does not adjudicate: `robson2000` finds TRα1, TRα2 **and** TRβ1 in
rat reserve/proliferating zones and none in hypertrophic cells. `thra_receptor` (A) and
`thrb_receptor` (D) carry reciprocal `CONTRADICTS`. Practical stake: the paediatric skeletal
safety of TRβ-selective thyromimetics (resmetirom class).

**Circulating or local IGF-1?** (c_l4endo_04, `g_l4endo_001`). Liver-specific *Igf1* deletion
cuts serum IGF-1 by **75%** with **0% change** in body weight, body length or femoral length
in two independent mouse lines (`yakar1999`, `sjgren1999`). But LID+ALSKO (serum IGF-1 down a
further 65%) drops plate height, BMD by 10% and periosteal circumference/cortical thickness by
>35%, restored by IGF-1 (`yakar2002`). A threshold model reconciles them **in mouse**. The
human partition has never been made: **no measurement of IGF-1 concentration in human physeal
interstitium exists.**

**Seasonality peaks in opposite seasons** (c_l4endo_03, `g_l4endo_008`). `shulman2013`
(2,277 GH-treated prepubertal children): velocity rises 0.146 cm/yr per daylight hour with no
independent calendar-month effect. `narumi2020` (9,409 Japanese infants): summer peak,
winter–summer difference 0.0026 z/day (~13% of mean velocity). `dalskov2016` (760 Danish
8–11-year-olds): velocity exceeds the 6.10 cm/yr mean in **January–April**, and weight, BMI and
fat-free mass index peak coincidentally rather than in the classical antiphase.
`seasonality_growth_velocity` carries `CONTRADICTS: [dalskov2016, narumi2020]`. Latitude
(35°N vs 56°N), age, GH treatment status and method all differ; photoperiod, temperature and
seasonal nutrition have never been separated in one design. Consequence: **any growth trial
shorter than 12 months carries an uncontrolled seasonal term of ~13% of mean velocity.**

**Androgen receptor is abundant in human chondrocytes and does nothing in explant**
(`g_l4l3_009`). AR protein is present in **41–65%** of human growth plate chondrocytes, and AR
modulation has no effect on longitudinal growth in cultured metatarsals. Either the explant
lacks a required co-factor, or the androgen effect on human growth is entirely aromatase-mediated
— which the aromatase-deficiency and ESR1 human cases would predict.

---

## 3. The load-bearing assumption

**That serum hormone concentration is a valid proxy for the concentration acting at the
chondrocyte.**

Every dose–response in this layer is a serum measurement regressed on a whole-body growth
readout: the 20 pmol/L and 6.5 pmol/L estradiol EC50s, the GH burst statistics, the IGF-1
thresholds, the T3 and vitamin D reference ranges, the entire clinical practice of dosing
growth by serum IGF-1. Nothing downstream of it survives if it is wrong — including L12's dose
selection, which uses the same proxy.

The evidence for it is indirect and consists of the axis working: serum IGF-1 tracks GH dose,
GH dose tracks growth. The evidence **against** it is in this layer and is human. PAPP-A2
deficiency has **elevated** total serum IGF-1 (831–1060 µg/L) with **0.09–0.32%** bioactive
fraction and height −2.16 to −3.81 SDS. A serum assay reading high in a child who is failing to
grow is the cleanest available demonstration that the circulating measurement and the
tissue-level signal can dissociate completely. Five separate searches asked whether the
tissue-level quantity has ever been measured — physeal interstitial IGF-1 (`g_l4endo_001`),
intracellular T3 with zonal DIO2/DIO3 activity (`g_l4l3_008`), zonal IGFBP gradients setting
free IGF-1 (`g_l4endo_009`), zonal GR expression and ligand occupancy (`g_l4endo_003`), and
11β-HSD1/2 pre-receptor cortisol interconversion inside the plate (`g_l4endo_005`). **All five
returned nothing.** The plate's own hormone microenvironment has never been sampled in any
species.

---

## 4. What would change everything

A direct measurement of free hormone concentration inside human growth plate tissue —
microdialysis at epiphysiodesis, or mass-spectrometry imaging of estradiol, T3 and IGF-1 on
physeal blocks with zonal annotation.

If interstitial free IGF-1 tracks serum, the layer's serum-proxy licence is finally earned and
the somatomedin/dual-effector dispute (c_l4endo_04) becomes answerable in humans for the first
time. If it does not — if local IGFBP or PAPP-A/PAPP-A2 activity sets a physeal free-IGF
concentration decoupled from serum — then serum IGF-1 monitoring is measuring the wrong
compartment, the 11β-HSD question becomes urgent because pre-receptor cortisol amplification
would explain the `baron1992`/`tu2014` split, and every L12 exposure–response analysis built on
plasma PK inherits a systematic error whose sign is unknown.

Second, cheaper, and it would settle a separate quadrant: the orthogonal glucocorticoid
experiment — unilateral local dexamethasone infusion in a chondrocyte-specific GR knockout.
Suppression persisting means glucocorticoid growth arrest is non-GR or non-chondrocyte;
suppression abolished means `tu2014`'s null is a statement about endogenous tone only, and the
two literatures stop being read as contradictory.

---

## 5. Numbers

| Parameter | Value | Unit | Species | Spread / n | Source | Flag |
|---|---|---|---|---|---|---|
| Estradiol EC50, half-maximal growth acceleration (girls) | **20** | pmol/L | **human** | 95% CI 13–31; n = 27, 37 profiles | `albin2012` | single source |
| Estradiol EC50 (boys) | **6.5** | pmol/L | **human** | 95% CI 3.2–13; n = 26 | `albin2013` | single source |
| 24-h mean estradiol across male puberty | <4 / 6 / 8 / 21 / 32 | pmol/L | **human** | 5th–95th pct given; 62 profiles | `ankarberglindg2008` | — |
| Ulnar velocity, 4 vs 20 vs 90 µg/day E2 | 0.45→1.38 / 0.49→1.0 / 0.46→0.84 | mm per 3 wk | **human** | n = 5 boys; only the lowest dose P<0.05 | `carusonicolett1985` | n = 5, **biphasic** |
| ESR1-null adult height | **204** | cm | **human** | n = 1; estradiol elevated | `smith1994` | n = 1 |
| ERα-null tibial length / plate height | +8.3 / +18 | % | mouse, 16–19 mo | P < 0.01 / P < 0.05 | `brjesson2012` | single source |
| GH burst frequency | 13.7–13.8 | bursts/24 h | **human** | 95% CI 12.1–15.7, n = 37 | `van2016` | — |
| Pulsatile share of 24-h GH | 88 | % | **human** | derived from group means | `van2016` | derived |
| Bioactive/total IGF ratio, PAPP-A2 deficiency | **0.09–0.32** (ref 1.23) | % | **human** | n = 5 vs 95 controls | `dauber2016` | single family series |
| Total serum IGF-1, PAPP-A2 deficiency | 831–1060 (**elevated**) | µg/L | **human** | n = 5 | `dauber2016` | single family series |
| Height, PAPP-A2 deficiency | −2.16 to −3.81 | SDS | **human** | n = 5 | `dauber2016` | single family series |
| Local dexamethasone growth suppression | **77** | % | rabbit | P < 0.0001; contralateral control | `baron1992` | single dose level |
| Chondrocyte-specific GR deletion effect | **0** | % | mouse | null at every age tested | `tu2014` | **negative** |
| Serum IGF-1 fall, liver-specific *Igf1* KO | 75 | % | mouse | — | `sjgren1999` | — |
| Body length change, same mice | **0** | % | mouse | two independent lines | `yakar1999` | **negative** |
| BMD / cortical loss, LID+ALSKO | 10 / >35 | % | mouse | — | `yakar2002` | single source |
| Estradiol addback effect on GH secretion | 60–70 | % increase | **human** | n = 74; P = 0.046/0.020/0.018 | `roelfsema2018` | — |
| Turner: ultra-low-dose E2 added to GH | +0.32 (2.1 cm) | SDS | **human** | SE 0.17, **P = 0.059**; n = 35/35 | `ross2011` | borderline |
| Turner: early depot E2 + GH vs GH | +3.5 | cm | **human** | n = 7/arm, P < 0.01 | `rosenfield2005` | n = 7 |
| AR-positive human chondrocytes | 41–65 | % | **human** | no growth effect in explant | (`g_l4l3_009`) | contradiction |
| Untreated congenital leptin / LEPR deficiency mortality | 26 / 9 | % | **human** | within a 145-child cohort | `saeed2023` | retrospective |
| Physeal interstitial hormone concentration | **never measured** | any unit | any species | 5 searches, 5 nulls | — | — |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l4endo_011`** (contradiction, tract 4) — the glucocorticoid paradox. Unilateral local
   dexamethasone in Col2-CreERT2;GR-flox mice with contralateral vehicle. Suppression retained
   → non-GR or non-chondrocyte mechanism; abolished → `tu2014` bounds only endogenous tone.
2. **`g_l4endo_007`** (contradiction, tract 3) — TRα vs TRβ. Chondrocyte-specific conditional
   deletion of each isoform (not germline) with zonal histomorphometry, plus T3 response in
   primary **human** physeal chondrocytes. Germline knockouts permit compensation a conditional
   would not; rib and long-bone chondrocytes are different elements.
3. **`g_l4endo_001`** (quantitative_gap, tract 3) — what fraction of chondrocyte IGF1R
   activation is locally produced? Microdialysis or MS imaging of physeal interstitium against
   paired serum, in the same subject. Threshold model predicts local ≈ serum above the
   threshold; dual-effector predicts a persistent local excess.
4. **`g_l4endo_004`** (quantitative_gap, tract 3) — the complete estradiol dose–response, from
   the stimulatory low-dose limb through the fusion-accelerating high-dose limb. `albin2012/13`
   give the lower half; `carusonicolett1985` (n = 5) and `weise2001` (rabbit, one dose level,
   70 µg/kg/week) gesture at the upper. Nobody has drawn the whole curve in one species.
5. **`g_l4endo_008`** (contradiction, tract 3) — seasonality phase. Same protocol, same
   measurement method, matched ages, run simultaneously at 35°N and 56°N with photoperiod,
   temperature and dietary intake all recorded. Photoperiod predicts a phase shift with
   latitude; nutrition predicts a shift with local harvest/school calendar.
6. **`g_l4endo_002`** (search_established, tract 2) — does GH *pattern* matter at matched 24-h
   integrated exposure in humans? `gevers1996` already reports **0 fold** hepatic GHR/GHBP
   response to the pulsatile component in dwarf rats, which undercuts the pattern hypothesis at
   its own mechanistic step. `gh_pulse_pattern_hypothesis` is held at C, rat-only, deliberately.
7. **`g_l4endo_010`** (species_gap, tract 5) — does human SOCS2 loss produce overgrowth as the
   mouse predicts? `socs2_protein` is grade D, mouse-only, and is the single node most likely
   to be a mouse-specific result masquerading as a general mechanism.

---

## 7. Human-translation status

**46 of 72 nodes (64%) carry direct human evidence and 32 of 72 are grade A** — the highest of
any layer except L11 and L7. 36 nodes carry low or not-applicable translation risk. This layer
can be quoted about humans in a way that L2 and L3 cannot.

Three caveats, and they are specific rather than generic. **(i) The human evidence is
overwhelmingly circulating.** Every A-grade number is a serum concentration, a serum ratio, or
a whole-body height response to a systemic dose. Not one is a measurement inside the plate;
see §3. **(ii) Where the layer descends to the chondrocyte, it becomes mouse instantly.**
`glucocorticoid_receptor`, `gper1_receptor`, `socs2_protein`, `estrogen_receptor_beta`,
`dio2_deiodinase`, `igf1_local_growth_plate` are `he=absent` and high-risk — the receptor-level
nodes of an otherwise human layer. **(iii) Several A grades rest on n = 1 to n = 7.** The ESR1
case is one man; the PAPP-A2 series is five individuals in two families; the Turner
depot-estradiol arm is seven girls per group. These are grade A because human interventional or
direct evidence is the grading criterion, not because they are large.

The clean summary: **L4 knows what hormone concentrations in blood do to human height, and
knows nothing about what concentration reaches the cartilage.** The one human experiment that
tested those two things against each other — PAPP-A2 deficiency — found them dissociated.
