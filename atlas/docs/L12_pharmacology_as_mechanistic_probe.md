# L12 — Pharmacology as mechanistic probe

**36 nodes (0 stubs) · 164 edges touching the layer · 60 gaps · ~90 refs**
Confidence: **A 16** · B 10 · C 4 · D 5 · **X 1**. `human_evidence` direct 30 (83%), **replicated
human 26 (72%)** — the highest in the atlas. `translation_risk` low or not_applicable on 26 of 36.

Sixty gaps against thirty-six nodes, the highest ratio in the atlas. Randomised human
perturbation is the strongest causal evidence available for growth, and this layer holds it —
and it also holds the atlas's single most exposed grade-X claim, which is that any of these drugs
reaches the tissue it is designed to act on.

---

## 1. The settled core

**CNP-analogue therapy raises growth velocity in achondroplasia, replicated across four
randomised trials.** Pooled class effect **+1.36 cm/yr (95% CI 1.05–1.68)**, n = 326
(`kamrulhasan2026`). Vosoritide **+1.57 cm/yr (95% CI 1.22–1.93)**, n = 121 (`savarirayan2020`);
navepegritide **+1.49 cm/yr (95% CI 1.05–1.93)** with arm velocities 5.89 (95% CI 5.66–6.13) vs
4.41 (4.04–4.77) cm/yr, n = 57/27 (`nct05598320`). Class injection-site reaction RR 1.65
(urticaria 4.04, swelling 3.57).

**FGFR3 kinase inhibition also works.** Infigratinib 0.25 mg/kg/day oral, phase 3 double-blind:
**+1.74 cm/yr (95% CI 1.31–2.17, p < 0.001)** and height z **+0.32 (96% CI 0.23–0.41)** at week
52 (`savarirayan2026infig`).

**rhGH is the most-replicated growth intervention in medicine.** +3.0 to +5.0 cm/yr velocity gain
and +0.3 to +0.9 SDS across 20 studies and 21,812 participants, discontinuation <2%
(`martn2026`) — with the authors' own note of moderate-to-serious risk of bias.

**Growth suppression by common paediatric drugs is quantified and grade A.** Inhaled budesonide
400 µg/day from ages 5–13 for 4–6 years: adult height **−1.2 cm (95% CI −1.9 to −0.5, P = 0.001)**,
dose-dependent at **−0.1 cm per µg/kg/day** (`kelly2012`). `methylphenidate_growth` and
`inhaled_corticosteroid_growth` are both grade A with `translation_risk: not_applicable`.

**Aromatase inhibition buys about a centimetre and does not hold.** Anastrozole 1.0 mg/day or
letrozole 2.5 mg/day for 3 years in 79 pubertal boys with ISS: **+1.3 cm** predicted adult height
combined (p = 0.043), with **the year-1 gain not sustained at years 2–3** and no between-drug
difference (`zegarra2024`). A propensity-matched cohort gives target-height-adjusted adult height
SDS 0.81 (SD 0.34) for anastrozole + rhGH vs 0.60 (SD 0.28) for letrozole + rhGH, anastrozole
superior to letrozole and GnRHa at p < 0.01 (`cui2025`, 32 boys/group).

---

## 2. The live disagreements

**A ~300-fold difference in exposure duration produces indistinguishable efficacy — and the
same molecule class shows a within-trial dose–response.** This is C-L12-02 and it is the
sharpest unresolved question in growth pharmacology.

Vosoritide: mean apparent plasma half-life **21.0–27.9 minutes** (SD 4.7–9.9 across visits,
n = 58). Navepegritide-released CNP: **5.3 days** (prodrug 6.7 days), steady-state Cmax 36.0
pmol/L, Tmax 24.4 h. Ratio ≈ **300-fold**. Placebo-controlled velocity gains: **1.57 vs 1.49
cm/yr**, confidence intervals almost completely overlapping. Continuous exposure is the *explicit
engineering premise* of the TransCon prodrug, and buying 300× more of it bought nothing
measurable.

But the atlas records an **internal tension** on `cnp_analog_pk_challenge` rather than declaring
exposure irrelevant: *navepegritide shows a clear within-trial dose–response (ACcomplisH) while
vosoritide exposure does not predict growth within its own cohort (`galetaki2026`). Both cannot be
simple exposure–response relationships over the same effective range.* Three hypotheses compete
and **none has been discriminated**:

| # | Hypothesis | Gap | What would test it |
|---|---|---|---|
| **H1** | The **downstream** step saturates before the receptor does — cGMP or PKG output plateaus while NPR2 occupancy still rises | `g_mr002_h1` (species_gap, tract 3) | Measure growth plate cGMP and PKG activity at sub-saturating vs saturating NPR2 occupancy in the same animal |
| **H2** | The **tissue** concentration saturates regardless of plasma AUC — diffusion into avascular, charge-dense cartilage is the limiting step | `g_mr002_h2` (method_blocked, tract 3) | Measure intracartilaginous drug concentration across a plasma AUC range |
| **H3** | The approved vosoritide dose sits on a **tolerability** ceiling (blood pressure), not an efficacy plateau, and efficacy would keep rising above it | `g_mr002_h3` (known_unknown, tract 5) | Dose-escalation above 15 µg/kg/day with blood-pressure management |

The one independent datum favours a saturable step: the FDA label reports that **urinary cGMP
response is already near saturation at the approved 15 µg/kg/day dose**. That is consistent with
H1 and H3 and silent on H2. And CORR-003 (L3) sharpens H1 into a specific mechanistic suspicion:
if PKG-II is not in fact the effector — losing it **expands** the plate 2.6× while losing NPR2
shrinks the hypertrophic layer to 23% — then the "downstream availability" the ceiling would be
set by may not be the molecule the field names (`g_l12b_003`). **Three independent routes —
C-L3-03, CORR-003 and MR-002 hypothesis H1 — now converge on the same suspicion about
CNP-analogue mechanism.**

**The FGFR3 inhibitor class works while its stated premise is false, and the atlas records the
scope limit on the node.** `fgfr3_tyrosine_kinase_inhibitor` carries an explicit **ALLELE
MISMATCH** flag: *published FGFR3-inhibitor potency data are on kinase-domain alleles (K650E,
K650M, N540K); the clinical achondroplasia target is the transmembrane **G380R**; whether potency
rank order transfers across activation mechanism is untested.* The potency panel: infigratinib
IC50 0.66 nM wild-type, **0.5 nM K650E, 44.4 nM K650M (89-fold weaker), 505.9 nM V555M**
(`ryu2022`, ATP concentration not stated). **The IC50 against G380R — the allele the drug is
licensed-track to treat — has never been measured** (`g_l12b_005`, tract 5). And severity is
non-monotonic within the kinase domain (L11): K650M has ~3× the activity of the lethal K650E and
is survivable. So "reduce kinase output, reduce severity" is false as a general rule (C-L12-03),
a phase 3 nonetheless produced +1.74 cm/yr, and the mechanism of clinical benefit is
under-specified.

**Two clinical failures are unattributable, and for the same reason.** Recifercept, a soluble
FGFR3 decoy, prevented premature synchondrosis ossification in *Fgfr3*-ach/+ mice and produced
**observed/expected height-change ratio 1.0 (95% CI 0.8–1.1) at 12 months in all three dose arms**
in children; both trials terminated for "lack of efficacy at any of the tested doses ... not
related to a safety concern" (C-L12-04). Meclizine reduced death or paralysis and increased body,
cranial and long-bone length in *Fgfr3*-ach mice at 2 mg/kg/day, and in a 26-week open-label
phase 2 (n = 9, with concomitant GH) moved height velocity **+0.11 cm/yr** — despite a dedicated
paediatric phase 1b confirming adequate systemic exposure (Cmax **167 ng/mL** 95% CI 83–250,
t½ 7.4 h, AUC₀₋₂₄ 1,170 ng·h/mL) (C-L12-05). In neither case can failure be attributed between
mouse-specific mechanism and failure of delivery into cartilage, **because tissue exposure was
never measured in either species** (`g_l12b_006`, `g_l12b_007`, `g_l12l7_007`).

**Two nodes are held at low grade for honest reasons.** `mecasermin_rinfabate` is **grade X**:
the claim that the rhIGF-1/rhIGFBP-3 complex improves growth is repeated in reviews and no
retrievable cohort reports height velocity or adult height on it — a search returning 865 hits
finds only bronchopulmonary dysplasia trials of the same molecule as OHB-607 and an unrelated
genotyping assay now occupying the "iPlex" query (x-L12-01, `g_l12b_012`).
`statin_ipsc_achondroplasia` is grade D with **no human in vivo data and no independent
replication of the 2014 iPSC rescue in twelve years** (x-L12-02).

**And nobody knows the conversion factor.** `g_l12b_016` (tract 4): what fraction of a
pharmacologically induced increment in annualised growth velocity is converted into **attained
adult height**, and does the factor differ between mechanisms? `trial_endpoint_annualized_growth_velocity`
and `final_adult_height_endpoint` are both grade A as methods, and the mapping between them is
unmeasured. `g_l12pharm_001` asks the same question of the CNP class specifically: does childhood
therapy raise final adult height, or redistribute growth in time?

---

## 3. The load-bearing assumption

**That plasma exposure is a valid surrogate for growth plate exposure — i.e. that the drug
concentrations achieved at the physis by systemic therapy are adequate.**

This is x-L12-03, and it is the **unstated premise of every dose selection in growth
pharmacology**. It is implicit throughout the CNP-analogue, FGFR3-inhibitor and growth-hormone
literatures, all of which report only plasma pharmacokinetics.

**0 of 12 audited agents has a published growth plate tissue concentration measurement, in any
species.** The audit covered vosoritide, navepegritide, infigratinib, recifercept, meclizine and
seven others, checked against Europe PMC (253 hits, 25 screened), the openFDA structured
labelling for eight products, and posted ClinicalTrials.gov results (`g_l12b_002`, logged
2026-08-05). The imaging methods exist and have been applied to subchondral bone, joint lipids and
periprosthetic bone — **never to a therapeutic agent in the physis**.

The reason this is load-bearing rather than merely absent: the growth plate is **avascular,
aneural and alymphatic**, and every solute must diffuse from its margins through a dense,
negatively charged proteoglycan matrix with fixed charge density around −0.19 to −0.35 mol/L
(L5). A ~100 kDa soluble decoy and a 21-minute-half-life 39-residue peptide face very different
diffusion problems, and neither has been measured. `growth_plate_drug_exposure` is graded **B with
`human_evidence: absent`** — the only intervention-adjacent node in the layer with no human
evidence at all, in a layer that is otherwise 83% direct-human.

Every unresolved question in §2 routes through it. H2 of the CNP puzzle **is** this assumption.
The recifercept failure cannot be attributed without it. The meclizine failure cannot be
attributed without it — measured plasma exposure was adequate, which removes the simplest
explanation and leaves either mouse-specific mechanism or failure of cartilage delivery. And the
G380R IC50 gap is only half the FGFR3 problem: knowing the potency would still not tell you the
concentration at the target.

---

## 4. What would change everything

**Measure the concentration.** Two routes, both available now.

**(i) The regulatory route, and it may already be done.** `g_l12b_024` (method_blocked, tract 5):
do the FDA multidisciplinary and pharmacology/toxicology review documents for vosoritide,
navepegritide and infigratinib contain **animal tissue distribution data** showing drug in
cartilage? Sponsors routinely run quantitative whole-body autoradiography for IND-enabling
toxicology. If those data exist in a review document, the atlas's most exposed grade-X claim
resolves without a single new experiment, and 12 nodes gain a real exposure term.

**(ii) The tissue route.** MALDI mass-spectrometry imaging on physeal tissue obtained at
limb-lengthening osteotomy in children on CNP-analogue therapy. Achondroplasia limb lengthening
is performed in the same population and often in the same centres as the trials, and the tissue is
discarded (`g_l12pharm_002`, `g_l12b_025`).

The discrimination is clean. If intracartilaginous CNP concentration **plateaus** as plasma AUC
rises across the vosoritide/navepegritide range, **H2 is confirmed**: the 300-fold plasma
difference never reaches the tissue, the whole next-generation-formulation programme is
optimising the wrong variable, and the efficacy ceiling is a diffusion ceiling that no
formulation change can lift. If tissue concentration **tracks plasma**, H2 is dead, the ceiling is
pharmacodynamic, and the field's next move is H1/H3 — measure whether cGMP and PKG output saturate
(which CORR-003 says may not even be the right effector), and test dose escalation above the
tolerability cap.

Either answer redirects a therapeutic programme worth billions, and neither requires a new trial.

---

## 5. Numbers

| Parameter | Value | Unit | Species | Spread / n | Source | Flag |
|---|---|---|---|---|---|---|
| **Agents with a measured growth plate tissue concentration** | **0 of 12** | agents | any | 253 hits screened; 8 FDA labels | — | **grade X (x-L12-03)** |
| Vosoritide plasma half-life | **21.0–27.9** | minutes | **human** | SD 4.7–9.9; n = 58 | `fda_voxzogo_label_2025` | — |
| Navepegritide-released CNP half-life | **5.3** (prodrug 6.7) | days | **human** | population PK model, no CI | `fda_yuviwel_label_2026` | — |
| Exposure-duration ratio | **~300** | fold | human | derived from the two labels | — | `value_unverified` |
| Vosoritide velocity gain | +1.57 | cm/yr | **human** | 95% CI 1.22–1.93; n = 121 | `savarirayan2020` | — |
| Navepegritide velocity gain | +1.49 | cm/yr | **human** | 95% CI 1.05–1.93; n = 57/27 | `nct05598320` | **no head-to-head trial** |
| CNP class pooled effect | +1.36 | cm/yr | **human** | 95% CI 1.05–1.68; 4 RCTs, n = 326 | `kamrulhasan2026` | — |
| Navepegritide arm velocities | 5.89 vs 4.41 | cm/yr | **human** | 95% CI 5.66–6.13 / 4.04–4.77 | `nct05598320` | — |
| Urinary cGMP response at 15 µg/kg/day | **near saturation** | — | **human** | label statement, no CI | `fda_voxzogo_label_2025` | supports a saturable step |
| Infigratinib velocity gain / height z | +1.74 / +0.32 | cm/yr / z | **human** | 95% CI 1.31–2.17; 96% CI 0.23–0.41 | `savarirayan2026infig` | — |
| Infigratinib IC50: WT / K650E / K650M / V555M | 0.66 / 0.5 / **44.4** / 505.9 | nM | in vitro human cell | **ATP concentration not stated**; no CIs | `ryu2022` | — |
| Infigratinib IC50 vs **G380R** (the clinical allele) | **never measured** | nM | — | — | — | `g_l12b_005` (tract 5) |
| Recifercept observed/expected height change | **1.0** | ratio | **human** | 95% CI 0.8–1.1, all 3 dose arms | `nct04638153` | terminated, no safety signal |
| Meclizine velocity change (26 wk, + GH) | **+0.11** | cm/yr | **human** | n = 9, no control arm, no CI | `matsushita2025` | — |
| Meclizine paediatric Cmax / t½ / AUC₀₋₂₄ | 167 / 7.4 / 1,170 | ng/mL / h / ng·h/mL | **human** | 95% CI 83–250 / 6.7–8.0 / 765–1,570 | `matsushita2023` | **exposure was adequate** |
| Meclizine effective mouse dose | 2 | mg/kg/day | mouse | single dose level | `funahashi2024` | contradicted in humans |
| rhGH velocity / height gain | +3.0 to +5.0 / +0.3 to +0.9 | cm/yr / SDS | **human** | 20 studies, n = 21,812; discontinuation <2% | `martn2026` | moderate–serious bias risk |
| Inhaled budesonide adult height effect | −1.2 | cm | **human** | 95% CI −1.9 to −0.5, P = 0.001 | `kelly2012` | −0.1 cm per µg/kg/day |
| Aromatase inhibition, 3 y predicted adult height | +1.3 | cm | **human** | p = 0.043, n = 79; **year-1 gain not sustained** | `zegarra2024` | single dose level each |
| Anastrozole vs letrozole + rhGH, adult height SDS | 0.81 vs 0.60 | SDS (target-adjusted) | **human** | SD 0.34 / 0.28; p < 0.01 | `cui2025` | propensity-matched |
| Velocity-gain → adult-height conversion factor | **unmeasured** | — | human | — | — | `g_l12b_016` (tract 4) |
| Mecasermin rinfabate growth outcomes | **none retrievable** | — | human | 865 hits, 25 screened | — | **grade X (x-L12-01)** |
| Statin trials with a linear-growth endpoint in FGFR3 dysplasia | **0** | trials | human | 12 years since the iPSC report | — | **grade X (x-L12-02)** |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l12b_002` / `g_l12b_024` / `g_l12pharm_002`** (search_established + method_blocked, tract
   3–5) — measure, or retrieve, the tissue concentration. See §4. This is the highest-leverage
   unresolved item in the layer and possibly in the atlas, because it gates the interpretation of
   two clinical failures, one efficacy ceiling and every future dose selection.
2. **`g_mr002_h1` / `g_mr002_h2` / `g_mr002_h3`** (tract 3–5) — the three competing explanations
   of the CNP exposure paradox, each with a stated discriminating measurement (table in §2). They
   are mutually exclusive in their predictions for tissue concentration vs plasma AUC and for cGMP
   output vs receptor occupancy, so one experiment each settles them.
3. **`g_l12b_005` + `g_mr002_allele`** (quantitative_gap + search_established, tract 4–5) —
   infigratinib IC50 against **G380R**, at a stated ATP concentration, in the same panel as K650E,
   K650M and N540K. The class is being dosed against an allele whose potency is unknown, and the
   K650E→K650M 89-fold swing shows allele-dependence is large and real.
4. **`g_l12b_004`** (contradiction, tract 5) — is infigratinib potent enough against N540K to be
   therapeutic in hypochondroplasia? `demuynck2025` says yes (docking, in vitro, *Fgfr3*-N534K/+
   mouse rescue); `ursachi2026_2` says it is a weak inhibitor of that mutant, published months
   later in the same journal with an author reply. Resolvable only by one laboratory comparing
   wild-type, G380R, N540K and mouse N534K in one assay.
5. **`g_l12b_016`** (quantitative_gap, tract 4) — the velocity→adult-height conversion factor, by
   mechanism. Discriminator: pool the long-term extensions of GnRHa, aromatase-inhibitor, rhGH and
   CNP-analogue trials and regress attained adult height on first-year velocity increment,
   stratified by mechanism. If the factor differs by mechanism, velocity is not a valid common
   surrogate and cross-class comparisons of "cm/yr gained" are meaningless.
6. **`g_l12b_015`** (known_unknown, tract 4) — why does the aromatase-inhibitor predicted-height
   gain appear at year 1 and vanish by year 3? Discriminator: serial bone age plus estradiol with
   an ultrasensitive assay through years 1–3. Escape via rising estradiol predicts convergence;
   stable suppression with vanishing gain means the year-1 gain was a bone-age-prediction artefact,
   which would also indict the endpoint (`g_l7fuse_007`).
7. **`g_l12b_023`** (known_unknown, tract 4) — can glucocorticoid anti-inflammatory efficacy be
   separated from growth suppression at the human plate? This is L4's `g_l4endo_011` viewed from
   the therapeutic side, and `deflazacort`/`glucocorticoid_sparing_strategy` (both grade B, human)
   are the existing partial answers.

---

## 7. Human-translation status

**30 of 36 nodes (83%) carry direct human evidence and 26 (72%) are replicated-human — the
highest replication fraction in the atlas.** Sixteen nodes are grade A. Twenty-six carry low or
not-applicable translation risk. Randomised human perturbation is the strongest causal evidence
this atlas contains, and it is concentrated here.

The residual translation risk is precisely locatable and it is not distributed noise.

**Six nodes carry high translation risk**, and every one of them is a place where an animal result
has not survived contact with humans or has not yet been tested in them: `soluble_fgfr3_decoy`
(mouse rescue, human O/E ratio 1.0, terminated), `meclizine_repurposing` (mouse rescue,
+0.11 cm/yr in humans with adequate measured exposure), `statin_ipsc_achondroplasia` (iPSC and
mouse only, unreplicated in 12 years, no human data), `teriparatide` and `abaloparatide`
(`he=absent` — PTH1R agonists have **never** been given to a human with open epiphyses with a
prospectively reported linear-growth endpoint, `g_l12l7_006`, `g_l12b_019`), and
`growth_plate_drug_exposure` (`he=absent`, the subject of §3).

That list is the layer's most useful output as a *mechanistic probe* rather than as therapeutics:
**three mouse-validated mechanisms have now failed or under-performed in humans (recifercept,
meclizine, statins), and in none of the three can the failure be attributed**, because the
measurement that would attribute it — drug concentration at the growth plate — has never been made
for any agent in any species. The atlas's contribution here is not to explain the failures. It is
to establish that the field is structurally unable to explain them, and to name the single
measurement that would change that.
