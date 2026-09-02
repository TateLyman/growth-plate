# L7 — Fusion and cessation

**34 nodes (0 stubs) · 230 edges touching the layer · 36 gaps · ~80 refs**
Confidence: **A 15** · B 6 · C 6 · D 6 · E 1. `human_evidence` direct 26 (76%) / indirect 5 /
absent 3. `translation_risk` not_applicable on 23 of 34.

The most human layer in the atlas — and the one with the thinnest tissue. **Exactly two human
growth plates have ever been examined histologically at or immediately before fusion.** Eleven
of the thirty-four nodes are *methods* for estimating fusion state from radiographs, which is
what a field does when it cannot obtain the tissue.

---

## 1. The settled core

**Oestrogen terminates human growth, and two independent human lesions prove it in the same
direction.** A man with a homozygous *ESR1* nonsense mutation: adult height **204 cm**,
incomplete epiphyseal closure, lumbar BMD 0.745 g/cm² (−3.1 SD) falling to 0.684 (Z −3.85) at
follow-up, and bone age advancing only **15 → 17.5 years over 3.5 chronological years**
(`smith1994`, `smith2008`). A man with congenital *CYP19A1* aromatase deficiency: **204 cm**
at 24 years 3 months (+3.7 SD), bone age **14 years**, distal radius BMD −4.7 SD
(`morishima1995`); his 46,XX sister with the same mutation reached 177.6 cm (+2.5 SD). A second
aromatase-deficient man reached 188 cm with open wrist and knee epiphyses at 24
(`singhania2022`; 15 published male cases in total). Receptor loss and ligand loss, same
phenotype. This pairing is why `estrogen_receptor_alpha` was one of only **two accepted
confidence upgrades out of twelve tested** in Phase 3 — the human ESR1 case controls a confound
(elevated estradiol) that the mouse cannot.

**Fusion order and sex difference are grade A and population-measured.** MRI in 958 healthy
Swedish subjects aged 14.0–21.5: complete fusion at age 17 in females for
radius/femur/proximal tibia/distal tibia/calcaneus = **75 / 85 / 97 / 98 / 98%**; at age 19 in
males = **90 / 97 / 95 / 97 / 98%** (`kvist2021`). Dry-bone sequencing of 21 epiphyses in 258
Bosniak males (`schaefer2007`) and Portuguese sacral union at 15–21 years (`cardoso2014`)
supply the ordering.

**Bone age reading has a measured error, and automation reduces it.** Human interobserver
spread GP vs TW2 = **0.96 vs 0.74 years** (`king1994`); intra-observer 95% limits of agreement
−2.46 to +2.18 (GP) vs −1.41 to +1.43 (TW2) years over 362 consecutive clinical radiographs
(`bull1999`); GP vs chronological age 95% limits ≈2 years, bias 2.9 months (SD 12.8, n = 472,
`guevel2026`). BoneXpert: 0.42 y SD vs the GP atlas (95% CI 0.37–0.47), **0.17 y SD on repeat
radiograph** (95% CI 0.13–0.21) (`thodberg2009`); best deep-learning MAD 4.2 months on the RSNA
challenge (`halabi2019`); ICC 0.994–0.995 against manual GP (`zmen2025`).

**The "5–7 cm after menarche" rule is wrong, and the atlas holds the real distribution.** In 793
healthy term-born Swedish girls, postmenarcheal height gain is **8.0 cm, SD 4.9, observed range
0.2 to 31.1 cm** — an SD that is 60% of the mean and an upper tail nearly four times it
(`grdstedtbergho2024`). Menarche at 13.0 y (SD 1.3, range 8.2–17.2). At menarche, **71.6%
(SD 18.8)** of the pubertal growth function is already complete. Logged as x-L7-01: no primary
source for the 5–7 cm figure with an n and a dispersion measure exists anywhere; a search of 471
records found only this one reporting the full distribution.

---

## 2. The live disagreements

**The one human plate examined at fusion had no apoptosis.** `emons2009`: **0** TUNEL-positive
cells, no detectable cleaved caspase-3 or Bax (only Bad among pro-apoptotic proteins), no
ultrastructural apoptosis or autophagy — instead **hypoxia and necrosis**. Independently,
estrogen-accelerated resting-zone cell loss in rabbit "did not appear to be due to apoptosis"
(`nilsson2014`). Against this stands the entire murine hypertrophic-chondrocyte apoptosis
literature, carried into fusion by default. `apoptosis_at_fusion` (grade **D**) carries
`CONTRADICTS` against both `estrogen_accelerated_senescence` and `hypoxia_necrosis_at_fusion`.

This is unresolvable at present sample size and the atlas says so: **n = 1 fusing specimen, with
no published positive control demonstrating the TUNEL assay would have detected apoptosis in
that tissue block**, and **no second human fusing plate reported in the seventeen years since**
(`g_l7fuse_006`; the tissue-supply obstacle is `g_l7fuse_002`).

**"Rodents do not fuse" is terminologically true and quantitatively false.** `samvelyan2022`
counted **495 transphyseal bony bridges (SD 45) per wild-type mouse tibial growth plate** by
micro-CT, with *Socs2*⁻/⁻ animals showing 187 bridges (SD 56) at a **density of 14.4 vs 1.2**
per unit area (SD 0.7 / 0.5) — a ~12-fold density increase the authors describe as *accelerated
growth plate fusion*. And yet `yu2025` finds the same mouse plate is still calcified cartilage
at **55 weeks**, having **lost** rather than gained type X collagen and MMP-13 between W10 and
W55. Both are true at their own level: **mice bridge but never complete cartilage-to-bone
replacement.** The risk the atlas guards against is that "accelerated fusion" in a mouse paper
is read as the human endpoint; `bony_bridge_formation` and `epiphyseal_fusion` are held as
separate nodes and murine bridge counts are treated as a surrogate **whose relation to the human
endpoint has never been validated** (C-L7-02). Note also that L0 holds the counter-datum: the
mouse *phalanx* does fuse, at 3 weeks, while tibia and femur remain open past 12 weeks
(`lui2018`).

**Fusion order is assumed conserved across populations and has never been tested** (x-L7-02,
`g_l7fuse_010`). Every published sequence is single-population and uses a non-comparable element
set. Timing demonstrably differs by **at least two years** between populations
(`schaefer2005`), which is precisely what makes the untested conservation of *order* the
load-bearing assumption of forensic age estimation and of every site-specific mechanistic model.
A search of 166 records found **no formal statistical comparison of sequence between any two
populations**.

**Nobody knows why plates in one individual, under one circulating estradiol, fuse years apart**
(`g_l7fuse_012`, tract 2). This is the single most obvious question in the layer and there is no
candidate mechanism with evidence — the plates differ in HOX identity (L0, unmeasured in
chondrocytes), in mechanical environment (L6, unmeasured in humans) and in growth rate (L1), and
none has been tested against fusion order.

**The estradiol fusion threshold rests on n = 1.** >73 pmol/L inferred from a within-subject
time course in one aromatase-deficient man on transdermal replacement over five years, no CI
(`lanfranco2008`). The supporting cross-sectional contrast — 34.8 pg/mL median in obese boys
with fused epiphyses vs 15.7 in lean boys with unfused, at Tanner G5 — is flagged
`value_unverified` (secondary summary, `rochira2015`). `estradiol_threshold_fusion` is grade D.

---

## 3. The load-bearing assumption

**That bone age indexes remaining growth potential well enough to predict adult height, and
that reducing bone-age measurement error therefore improves prediction.**

Eleven of thirty-four nodes in this layer exist to serve it: `bone_age`, `greulich_pyle_method`,
`tanner_whitehouse_tw3`, `rus_score`, `fels_method`, `risser_sign`, `sanders_staging`,
`mri_physeal_closure_staging`, `automated_bone_age_ai`, `bone_age_measurement_error`,
`remaining_growth_prediction`. Downstream of it sit the timing of precocious-puberty treatment,
the timing of scoliosis surgery, epiphysiodesis planning, and **the power calculation of every
growth trial powered on predicted adult height** — which is to say, most of L12.

The evidence against it is C-L7-03 and it is two-part. First, **a model that omits skeletal age
entirely (Khamis-Roche) has errors only slightly larger than the RWT model that uses it**
(`khamis1994`). Second, automation has already delivered the precision gain the field spent five
decades pursuing — repeat-measurement SD **0.17 years** against a human interobserver spread of
0.74–0.96 years, a fourfold-plus improvement — and **no study has demonstrated a corresponding
narrowing of the adult height prediction interval** (`thodberg2009`, `king1994`). Precision went
up; predictive interval did not visibly follow.

The variance decomposition that would settle it — what fraction of adult-height prediction error
is reading error, what fraction is reference-standard displacement (GP's 1930s Cleveland cohort
applied to contemporary multi-ethnic children), and what fraction is irreducible biological
variance — **has never been published** (`g_l7fuse_007`, tract 4).

The layer's own data suggest where the answer lies. Menarcheal status, the sharpest single
maturational landmark available, narrows the 95% adult-height prediction interval from ±5 to
±4 cm at age 12 and ±4 to ±3 cm at age 13 (`tanner1975`). And **only 44% of the variance in
menarcheal age is explained by everything known 3.2 years earlier** (`grdstedtbergho2024`) —
rising to just 45% at midpuberty, from 8% at age 7 and 1% at birth. Most of the timing is not
knowable in advance from anything currently measured.

---

## 4. What would change everything

**The variance decomposition, run on an existing longitudinal cohort.** Take a cohort with
serial radiographs and attained adult height; read each film by GP, TW3 and BoneXpert; fit
adult-height prediction with each reader as a random effect and decompose the residual. It
requires no new data collection.

If reading error dominates, then AI bone age is the fix and the field's five-decade programme
was correct; trials should adopt automated reading and expect narrower intervals. If
reference-standard displacement dominates, contemporary population-specific standards fix it and
the GP atlas should be retired outright. **If irreducible biological variance dominates — which
the Khamis-Roche result and the 0.17 y/no-narrowing pairing both suggest — then bone age
precision is not the rate-limiting step in growth medicine, every trial powered on predicted
adult height needs larger n rather than better imaging, and eleven nodes in this layer are
measuring something whose ceiling was reached decades ago.**

Second, and it would rewrite the mechanism half of the layer rather than the method half: **a
prospectively banked series of human growth plates at fusion.** The current n is 2. Ten
specimens with matched controls, scored for TUNEL with a validated positive control, HIF1A
stabilisation, vascular fronts from both sides, and RNA quality sufficient for sequencing, would
simultaneously address `g_l7fuse_006` (is the apoptosis null real?), `g_l12l7_003` (is terminal
fate hypoxic non-apoptotic death?), `g_l12l7_004` (bidirectional vascular invasion?),
`g_l7fuse_003` (is there any human fusion transcriptome? — currently none) and `g_l7fuse_005`
(has any epigenetic mark ever been measured in human physeal chondrocytes by age? — currently
none).

---

## 5. Numbers

| Parameter | Value | Unit | Species | Spread / n | Source | Flag |
|---|---|---|---|---|---|---|
| Postmenarcheal height gain | **8.0** | cm | **human** | **SD 4.9; range 0.2–31.1**; n = 793 | `grdstedtbergho2024` | retires x-L7-01 "5–7 cm" |
| Age at menarche | 13.0 | years | **human** | SD 1.3; range 8.2–17.2 | `grdstedtbergho2024` | — |
| Pubertal growth function complete at menarche | 71.6 | % | **human** | SD 18.8 | `grdstedtbergho2024` | — |
| Menarcheal-age variance explained 3.2 y ahead | **44** | % | **human** | 45% at midpuberty; 8% at age 7 | `grdstedtbergho2024` | — |
| Complete fusion at 17 (F), radius→calcaneus | 75 / 85 / 97 / 98 / 98 | % | **human** | n = 958 total, MRI | `kvist2021` | — |
| Complete fusion at 19 (M) | 90 / 97 / 95 / 97 / 98 | % | **human** | n = 958 total | `kvist2021` | — |
| Interobserver bone age spread, GP vs TW2 | 0.96 vs 0.74 | years | **human** | 3 readers, 50 films; diff n.s. | `king1994` | — |
| Intra-observer 95% LoA, GP vs TW2 | −2.46/+2.18 vs −1.41/+1.43 | years | **human** | n = 362 | `bull1999` | — |
| Automated precision, repeat radiograph | **0.17** | years SD | **human** | 95% CI 0.13–0.21 | `thodberg2009` | **no matching interval narrowing** |
| Automated accuracy vs GP atlas | 0.42 | years SD | **human** | 95% CI 0.37–0.47 | `thodberg2009` | — |
| Adult height 95% prediction interval, pre/post menarche (age 12) | ±5 → ±4 | cm | **human** | ±4 → ±3 at age 13 | `tanner1975` | — |
| TUNEL⁺ cells, human fusing plate | **0** | cells | **human** | **n = 1**, no positive control | `emons2009` | **n = 1** |
| Pro-apoptotic proteins detected | Bad only (no Bax, no cleaved caspase-3) | — | **human** | n = 1 | `emons2009` | n = 1 |
| Bony bridges, wild-type mouse tibia | **495** | bridges/plate | mouse | SD 45 | `samvelyan2022` | single source |
| Bony bridges, *Socs2*⁻/⁻ | 187 (density 14.4 vs 1.2) | bridges/plate; per unit area | mouse | SD 56; SD 0.7 / 0.5 | `samvelyan2022` | single source |
| Mouse plate still unfused | 55 | weeks | mouse | only W10 and W55 examined; Col X and MMP-13 **lost** | `yu2025` | single source |
| ESR1-null / aromatase-deficient adult height | 204 / 204 / 188 | cm | **human** | n = 1 each; 15 male CYP19A1 cases published | `smith1994`, `morishima1995`, `singhania2022` | n = 1 each |
| Bone age at CA 24.25 y, aromatase deficiency | 14 | years | **human** | n = 1 | `morishima1995` | n = 1 |
| Bone age advance without ERα over 3.5 y | 15 → 17.5 | years | **human** | n = 1 | `smith2008` | n = 1 |
| Estradiol threshold for epiphyseal closure | >73 | pmol/L | **human** | **n = 1**, no CI | `lanfranco2008` | grade D |
| Estradiol at G5, fused vs unfused | 34.8 vs 15.7 | pg/mL median | human | ranges 25.6–41.1 / 13.2–21.0 | `rochira2015` | `value_unverified` |
| Estradiol dose accelerating rabbit senescence | 70 | µg/kg/week | rabbit | **single dose level** | `weise2001` | no dose–response |
| Cynomolgus lumbar endplates unclosed | 100 | % (11 animals, 9–15 y) | monkey | no older animals examined | `iwata2018` | single source |
| Human plates examined at fusion, ever | **2** | plates | human | — | `phase3_close`/`coverage.md` | **ceiling on the layer** |
| Population comparisons of fusion **order** | **0** | studies | human | 166 records screened | — | **grade X (x-L7-02)** |
| Human fusion transcriptomes | **0** | datasets | human | search logged | — | `g_l7fuse_003` |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l7fuse_007`** (quantitative_gap, tract 4) — the variance decomposition. See §4. It is the
   cheapest high-value experiment in the atlas: no new subjects, no new tissue.
2. **`g_l7fuse_002`** (method_blocked, tract 2) — assemble a prospective bank of human fusing
   plates. The obstacle is tissue supply, not technique; epiphysiodesis and limb-reconstruction
   surgery already remove physeal tissue at the relevant ages.
3. **`g_l7fuse_006`** (contradiction, tract 3) — is the apoptosis null real or an n = 1 artefact?
   Ten fusing specimens, TUNEL plus cleaved caspase-3, **with a positive control block from the
   same fixation and decalcification protocol**. The missing positive control is the whole
   objection to `emons2009` and it is trivially fixable.
4. **`g_l7fuse_001` / `g_l12l7_001`** (species_gap, tract 3–4) — does resting-zone depletion
   *cause* fusion, or is it the state of a plate that has already fused? Requires a species that
   completes fusion (rabbit, monkey) with progenitor ablation before radiographic closure.
   Depletion-causes-fusion predicts accelerated closure; depletion-as-consequence predicts none.
5. **`g_l7fuse_010`** (search_established, tract 3) — is fusion **order** conserved across
   populations? Apply one element set to two documented skeletal collections of different
   ancestry and test the sequence formally. Timing already differs by ≥2 years; nobody has asked
   whether the ordering does.
6. **`g_l7fuse_012`** (known_unknown, tract 2) — why do plates in one individual fuse years
   apart? Discriminator: correlate fusion order within individuals against (a) each plate's
   growth rate, (b) its mechanical environment, (c) its positional identity. Any one of the three
   showing rank correlation is the first mechanistic handle on the sequence.
7. **`g_l7fuse_004`** (species_gap, tract 3) — does the human fusing plate follow the aged mouse
   matrix trajectory (accumulating mineral while **losing** collagen X and MMP-13, `yu2025`) or
   the opposite? This is directly answerable on the two existing human specimens by IHC.

---

## 7. Human-translation status

**26 of 34 nodes (76%) carry direct human evidence, all 26 replicated, and 23 of 34 carry
`translation_risk: not_applicable`** because they are inherently human phenotypes or human
methods. On the coverage table this is the atlas's second-strongest layer. That statistic is
correct and it hides the layer's real constraint.

**The human evidence divides into two kinds and neither is tissue.** (a) **Population
radiography and anthropometry** — `kvist2021` (n = 958), `grdstedtbergho2024` (n = 793),
`schaefer2007` (n = 258), `bull1999` (n = 362), `guevel2026` (n = 472). Large, replicated,
grade A, and entirely external: it observes when plates close, never why. (b) **Single human
experiments of nature** — `smith1994`/`smith2008` (n = 1), `morishima1995` (n = 1),
`singhania2022` (n = 1), `lanfranco2008` (n = 1). These carry the entire mechanistic weight of
"oestrogen terminates growth" and each is one person. The grade is A because human interventional
or direct evidence is the criterion, not because the samples are large.

**The tissue evidence is n = 2 in the whole world.** 259 human growth plates have ever been
examined histologically, 102 of them postnatal and growing, and **exactly 2 at or immediately
before fusion**. Every mechanistic hypothesis node in this layer — `apoptosis_at_fusion` (D),
`hypoxia_necrosis_at_fusion` (D), `bidirectional_vascular_invasion` (D),
`ecm_remodeling_at_fusion` (D), `epigenetic_drift_fusion` (E), `stem_cell_exhaustion_fusion` (C)
— is either derived from those two specimens or transferred from a rabbit or a mouse that does
not complete the process being modelled.

The clean statement: **L7 knows exactly when human growth plates close and has almost no
material from which to learn how.** The mouse cannot supply it — mice bridge (495 per plate) and
never finish — and the atlas records that limitation as a node (`mouse_does_not_fuse`,
`species_transfer_risk_fusion`) rather than working around it.
