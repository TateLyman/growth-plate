# F-R051 — The gap between pharmacological ablation and genetic absence, measured

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** I searched the things I had been asking you for and found most of them. **One result goes
directly against my sulfatase argument and I am reporting it first.** The human receptor map is now
quantitative and it reframes ERβ a third time. **And there is a number I should have gone looking for
rounds ago: what oestradiol level an aromatase inhibitor actually achieves in a man. It is about twice the
level Nilsson showed damages the resting zone.**

---

## 1. The result that goes against me — the IRIS trial

**Coombes RC et al., *"IRIS study: a phase II study of the steroid sulfatase inhibitor Irosustat when
added to an aromatase inhibitor in ER-positive breast cancer patients"* (PMC5543190, open access).**

**Irosustat 40 mg/day added to a first-line AI in 27 postmenopausal women:**

| endpoint | result |
|---|---|
| **oestradiol** | **below detection at baseline AND at every subsequent timepoint** (LOD 2 ng/dl) |
| **oestrone** | **below detection throughout** (LOD 10 ng/dl) |
| **oestrone sulfate** | **40.0 ng/dl → 40.0 ng/dl at 3 months, P = 0.53 — no change** |
| DHEA | **decreased, P < 0.01** |
| DHEAS | **increased, P = 0.02** |
| DHEA:DHEAS ratio | **decreased, P < 0.01** |

> ### Adding a steroid sulfatase inhibitor to an aromatase inhibitor produced no further measurable suppression of oestradiol, oestrone, or oestrone sulfate.

**That is the closest thing to a direct human test of the Layer 2 argument I built in F-R047 to F-R050, and
it is negative on its primary readout.** I am not going to bury it.

**Four things bound how negative it is, and they are all real:**

1. **The assays could not see the range that matters.** LOD for E2 was **2 ng/dl = 20 pg/mL**. Nilsson's
   demonstrated biological threshold is **11 ± 2 pg/mL**. **The assay floor sits above the concentration
   that damages the resting zone.** "Below detection" here means "below 20 pg/mL", which is not the same as
   "suppressed".
2. **The E1S result looks like an assay floor, not a null.** Baseline median 40.0 ng/dl with an IQR whose
   *lower bound is also 40.0* — that is a pile-up at the limit of quantification.
3. **The target was engaged.** DHEA fell, DHEAS rose, and the DHEA:DHEAS ratio fell, all significantly.
   **The enzyme was inhibited; the oestrogen readout simply could not resolve the consequence.**
4. **Postmenopausal women on an AI have a small reservoir to begin with.** A young male's E1S pool is far
   larger, and this is a serum measure in any case — the sulfatase argument is about **local intracrine
   formation inside cartilage**, which no serum assay reports.

**Honest verdict: IRIS neither confirms nor refutes the sulfatase arm. It shows target engagement and a
null on an insensitive readout in the wrong population.** The mechanism (F-R050 §1–2) stands on the enzyme
data. **The human confirmation does not exist, and the one attempt could not have detected it.**

**And the tolerability is poor:** dry skin **77% (28% grade 3–4)**, nausea 48%, fatigue 40%, three
discontinuations, median treatment duration **2.8 months**.

---

## 2. The number I should have looked up rounds ago

I have been treating "total oestrogen ablation" as an engineering target without asking what an aromatase
inhibitor actually achieves in a male. Here it is:

| setting | oestradiol achieved |
|---|---|
| **anastrozole**, men on testosterone therapy with elevated E2 | **65 → 22 pg/mL** (~66% reduction) |
| **letrozole**, obese hypogonadotropic men, 6 weeks | **120 → 70 pmol/L** (≈ 33 → 19 pg/mL, ~42%) |
| clinical titration target in men on AI | **20–40 pg/mL** |
| **normal adult male range** | 10–40 pg/mL |
| **Nilsson's demonstrated threshold for resting-zone suppression** | **11 ± 2 pg/mL** |
| **aromatase deficiency (Rochira's men)** | **undetectable on a 0.6 pg/mL assay** |

> ### Standard aromatase inhibition in a man lands oestradiol around 20 pg/mL — roughly twice the concentration Nilsson showed measurably suppresses resting-zone self-renewal, and around thirty times higher than the genetic deficiency state that actually produces non-fusing plates.

**This is the real hole, and it is quantitative rather than bibliographic.** The human existence proof —
*"epiphyseal fusion never takes place in men with estrogen deficiency or estrogen resistance"* — comes from
people with a **complete, congenital, lifelong absence of the enzyme or the receptor**. Pharmacology has
never been shown to reach that state.

**Two caveats in the other direction, so the gap is not overstated:** both datasets above are in men with
*elevated* substrate (exogenous testosterone) or *elevated* aromatase (obesity), which is the hardest case;
and neither used GnRHa or CYP17 blockade to remove substrate upstream. A lean man on letrozole **plus**
gonadal and adrenal substrate ablation would go considerably lower. **But nobody has measured how much
lower, and that measurement is the thing this whole arm turns on.**

**Which makes the specification precise:** the target is not "suppress oestrogen." It is
**"hold serum oestradiol below ~10 pg/mL continuously, verified by an assay with sub-picomolar sensitivity"**
— and, because §1 says serum is not the compartment that matters, ideally to know what that corresponds to
inside cartilage, which nobody has ever measured in a human at any age.

---

## 3. The human receptor map, quantified — and ERβ reframes a third time

### Nilsson O, Chrysis D, Pajulo O, Sävendahl L et al., J Endocrinol 2003;177(2):319

**Proximal tibial growth plate biopsies at epiphyseal surgery, 16 boys and 8 girls, Tanner 1–5.** Percent
receptor-positive chondrocytes by zone, individual patients (Table 1 examples):

| patient | Tanner | **ERα** RZ/PZ/HZ | **ERβ** RZ/PZ/HZ | **AR** RZ/PZ/HZ |
|---|---|---|---|---|
| 1 (F) | B3/Ph4 | 58 / 83 / 55 | 54 / 55 / 73 | 60 / 47 / 42 |
| 4 (F) | B2/Ph1 | 58 / 76 / 50 | 53 / 68 / 45 | 41 / 15 / 75 |
| 7 (F) | B1/Ph1 | 75 / 67 / 59 | 56 / 73 / 68 | 88 / 54 / 65 |
| 9 (M) | G1/Ph1 | 50 / 60 / 42 | 52 / 74 / 50 | 64 / 32 / 69 |

**Pattern across all 24:** all three receptors in **all zones of every specimen**, nuclear, abolished by
antigen preadsorption. **ERα and ERβ higher in the resting and proliferative zones than hypertrophic; AR
higher in resting and hypertrophic than proliferative.** No sex difference.

**The one thing that changes with puberty:**

> **ERβ decreases in the proliferative zone across pubertal development (P < 0.05):
> y = 79.7 − 4.8 × pubertal stage, R = 0.43.** ERα and AR are flat.

### And the authors' interpretation inverts ERβ yet again

> *"studies on estrogen receptor-mediated transcription have suggested that **ERβ acts as a negative
> regulator of ERα-mediated transcription** at estrogen response elements. It could thus be speculated that
> the observed **decrease in ERβ during pubertal development could cause an enhanced ERα-mediated signaling
> in the growth plate during late puberty**."*

**So ERβ, in the human plate with ERα present, is a brake on ERα — and it is being released during
puberty.** Set against everything else:

| source | ERβ's role |
|---|---|
| **Nilsson 2003 (human)** | **negative regulator of ERα transcription — protective; declines at puberty** |
| Chagin 2004 (ERα⁻/⁻ mice, 18 mo, high E2) | **mediates fusion when ERα is absent** |
| jin2021 / ERβ⁻/⁻ mice | blockade **increases growth**, transiently |

**These are consistent if ERβ is a weaker transactivator that competes with ERα for the same response
elements.** With ERα present it dampens; with ERα gone it becomes the only ER and takes over.

> ### Which is precisely the fulvestrant scenario. Fulvestrant removes the receptor ERβ was restraining and simultaneously upregulates ERβ — converting a brake into the sole driver. F-R050's demotion of the SERD to tier 3 was right, and this is a second, independent reason for it.

**And it strengthens the ligand strategy again:** with the ligand gone, none of this matters — no receptor
signals without a ligand, and the human proof (aromatase deficiency, both receptors intact) is exactly that
configuration.

### Li 2011 — the spine carries the same machinery

**Li XF, Wang SJ, Jiang LS, Dai LY, Histochem Cell Biol 2012;137:79–95.** Rat **spinal and tibial** growth
plates, both sexes, 1 / 4 / 7 / 12 / 16 weeks, qPCR plus immunohistochemistry:

- ERα and ERβ nuclear immunoreactivity in **both spinal and tibial** growth plate chondrocytes, both sexes
- ***"spatial differences of region-related ERα and β expression were not observed"*** — the receptors sit
  in the same cells in spine and limb
- What differs is **temporal pattern and the ERα/ERβ ratio**: in female limb the ratio falls during
  puberty while spine does not change; in males the ratio rises through puberty in **both** regions then
  falls
- After puberty in females, ERα localisation narrows to *"late proliferative and hypertrophic
  chondrocytes"*, while in males it still extends from resting to hypertrophic

**So the axial plates are not receptor-privileged.** Ligand ablation reaches them. **What the eunuchoid
phenotype of aromatase-deficient men shows is that the axial plates respond *less*, not that they lack the
machinery** — F-R040's FLAW 1 survives in a weaker form.

---

## 4. NCT04265651 identified — it is PROPEL 2, and it is exactly the dose–response study

I have been asking for this by number for three rounds. It is:

> **PROPEL 2 — "Phase 2, Open-Label, Dose-Escalation and Dose-Expansion Study of Infigratinib in Children
> With Achondroplasia."** QED Therapeutics / BridgeBio. Ages 3–11. **84 enrolled, 72 dosed in five
> sequential cohorts: 0.016, 0.032, 0.064, 0.128 and 0.25 mg/kg/day** for 6 months plus 12 months
> extension. Started March 2020, **completed 21 October 2024. No results posted on the registry.**
>
> Published as **Savarirayan R et al., *"Oral Infigratinib Therapy in Children with Achondroplasia"*,
> N Engl J Med 2025, PMID 39555818.**

**The abstract reports cohort 5 only:** AHV change from baseline at 18 months **+2.50 cm/yr** (95% CI
1.22–3.79, P = 0.001); height z-score **+0.54**; **upper-to-lower segment ratio −0.12**.

**A 16-fold dose range with annualised height velocity at each level is the dose–response curve I have been
saying does not exist. It exists. It is in that paper's figures, and the abstract does not carry it.**

**Two caveats to hold:** this is **mutant** FGFR3 in achondroplasia, not wild-type; and at the top dose
infigratinib yields **+2.5 cm/yr** where erdafitinib at 5 mg/day produced **19 cm/yr** in a
non-dysplastic 15-year-old. Different agents, different receptors, different ages. **But it is the only
graded dose–growth relationship for FGFR inhibition anywhere.**

---

## 5. Hole 3 partly resolved — no named second sulfatase

Muir's Eadie–Scatchard nonlinearity suggested *"more than one sulfatase isozyme in bone."* Chasing it:
**ARSA and ARSB are lysosomal**, with cerebroside sulfate and dermatan sulfate as substrates; **STS (ARSC)
is exclusively endoplasmic-reticulum-localised** and is the steroid sulfatase. **There is no named
alternative E1S-hydrolysing enzyme.** Irosustat's IC₅₀ is 8 nM against STS in placental microsomes.

**Downgraded from a hole to an unexplained kinetic observation.** Nonlinearity could equally reflect
multiple binding sites, substrate transport limitation, or product inhibition.

---

## 6. Where the oestrogen question actually stands

**What is settled:**

- The endpoint is real and human: fusion **never** occurs in congenital oestrogen deficiency or resistance
- The plate is an **intracrine organ** — aromatase, 17β-HSD1 and STS all present and active in chondrocytes
- **STS activity exceeds aromatase activity by 265–660× in the growth plate** and by two orders of
  magnitude in bone
- **11 ± 2 pg/mL of oestradiol measurably suppresses resting-zone self-renewal**
- Both ERα and ERβ are present in **every zone of every human growth plate sampled**, in spine and limb
- Fulvestrant degrades ERα and **upregulates** ERβ; ERβ is a brake on ERα that puberty releases
- **Therefore ligand ablation, not receptor ablation, is the strategy** — three independent reasons now

**What is not settled, and is the whole remaining question:**

> **Can pharmacology reach the state that genetics reaches?** An AI in a man gets to ~20 pg/mL. The
> threshold is ~11. The genetic state is undetectable at 0.6. **Nobody has measured oestradiol by a
> sub-picomolar assay in a human under combined aromatase + sulfatase + CYP17 blockade, and nobody has
> ever measured oestradiol inside human growth-plate cartilage at any age under any condition.**

**That is not a paper I can ask you for. It is a measurement that does not exist.** What can be asked for
are the four things below.

---

## 7. What I want, named exactly

**Tier 1 — specific figures inside specific papers:**

1. **Savarirayan R et al., N Engl J Med 2025, PMID 39555818, "Oral Infigratinib Therapy in Children with
   Achondroplasia."** I need **the change in annualised height velocity by cohort — cohorts 1 through 5
   (0.016 / 0.032 / 0.064 / 0.128 / 0.25 mg/kg)** — plus the corresponding safety table by cohort. **This
   is the FGFR-inhibitor dose–response curve. It is the single most valuable item outstanding.**

2. **Nilsson O et al., J Endocrinol 2003;177:319 — Figure 3 and Figure 4 source values.** I have Table 1
   (per-patient) but not the pooled means ± SEM per zone, and not the Tanner-stage regression underlying
   *y = 79.7 − 4.8×stage*. **This is the only quantitative human map of where the closure receptors sit and
   how ERβ declines.**

3. **Any phase 1 or phase 2 report of an HSD17B1 inhibitor with steroid endpoints** — FOR-6219 (Forendo /
   Organon) is the furthest advanced. F-R050 §1 promoted this enzyme to the pubertally-regulated node
   (absent at 1 week, present at 7), and I have no clinical pharmacology for the class at all.

4. **Stanway SJ et al., "Phase I dose escalation… optimal biological dose of irosustat" (PMID 23797179)**,
   and **the IPET FLT-PET window study (PMC5668341)** — I want the **STS enzyme inhibition versus dose**
   curve and whether tissue oestrogen was measured. IRIS used 40 mg with insensitive assays; the phase I
   may have the enzymology.

**Tier 2:**

5. **Any measurement of oestradiol or oestrone in human growth-plate or articular cartilage tissue**, at
   any age, by any method. I could not find one. If none exists, that is itself the finding.
6. **Whether any PROTAC ER degrader — vepdegestrant (ARV-471), ERD-3111, AC699 — engages or degrades ERβ**,
   and **palazestrant (OP-1250) against ERβ / AF2.** If one degrades ERβ, §3 reverses and the SERD returns.
7. **Weise M et al., PNAS 2001;98:6871**; **Muruganandan S et al., Nat Commun 2022;13:2515** full text.
