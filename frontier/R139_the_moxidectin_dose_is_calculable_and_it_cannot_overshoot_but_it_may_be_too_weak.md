# F-R139 — **THE MOXIDECTIN DOSE IS NOW CALCULABLE. IT IS STRUCTURALLY INCAPABLE OF OVERSHOOTING — WHICH REMOVES THE BIGGEST RISK AND CREATES A NEW ONE. AND THERE IS A COLLISION INSIDE OUR OWN STACK.**

Three human PK papers supplied and read in full: `Cotreau 2003` (J Clin Pharmacol; first-in-human
single ascending dose 3–36 mg, n=37), `tropmed 2012` (Am J Trop Med Hyg; **the approved 8 mg tablet**,
n=27 fasted, food effect), `CPDD 2012` (Clin Pharmacol Drug Dev; 10 mg tablet vs liquid, n=58).

**R138 left the exposure gap as a hand-wave. It is now arithmetic.**

---

## => THE HUMAN PHARMACOKINETICS, CONVERTED TO MOLARITY

**Moxidectin MW = 639.82 g/mol → 1 ng/mL = 1.563 nM.**

| regimen | Cmax ng/mL | **Cmax µM** | source |
|---|---|---|---|
| 3 mg liquid | 22.4 | **0.035** | Cotreau |
| ⭐ **8 mg TABLET fasted — THE APPROVED DOSE** | **58.9 ± 12.5** | ⭐ **0.092** | tropmed 2012, n=27 |
| 8 mg tablet with high-fat food | ~79 | **0.123** | tropmed (+44% AUC) |
| 10 mg tablet | 67.1 ± 27.4 | **0.105** | CPDD 2012, n=29 |
| 18 mg liquid | 141 | **0.220** | Cotreau |
| ⭐ **36 mg — THE HIGHEST DOSE EVER GIVEN TO A HUMAN** | **289–296** | ⭐ **0.452–0.463** | Cotreau |

**Supporting parameters (8 mg tablet):** t½ **784 ± 347 h = 32.7 ± 14.5 days**; Vλz/F **2,829 L**;
CL/F **2.76 L/h = 66.2 L/day**; tmax 3.7 h. The 10 mg study gives t½ **1,032 ± 502 h = 43 days**,
Vd/F 3,635 L. **PK is linear and dose-proportional across 3–36 mg.** High-fat food: **+44% AUC**,
−40% Vd, −35% CL, no significant Cmax change.

---

## => THE COMPARISON THAT R138 COULD NOT MAKE

**`Melotti`'s active concentrations:** moxidectin BrdU IC50 *"comparable to Ivermectin"* → **~1.0–2.5 µM**;
ivermectin 1.0–2.4 µM; ⭐ **selamectin 0.08–0.14 µM.**

Fractional pathway engagement, Hill n=1, **IC50 taken as 1.5 µM**:

| regimen | Cmax µM | **% engaged at peak** |
|---|---|---|
| 3 mg | 0.035 | 2.3% |
| ⭐ **8 mg (approved)** | 0.092 | ⭐ **5.8%** |
| 8 mg fed | 0.123 | 7.6% |
| 18 mg | 0.220 | 12.8% |
| ⭐ **36 mg (max ever dosed)** | 0.452 | ⭐ **23.1%** |

> **R138 guessed "~2 orders of magnitude below." THE REAL GAP AT THE APPROVED DOSE IS 16-FOLD, AND AT
> THE MAXIMUM TESTED HUMAN DOSE IT IS 3-FOLD. That is far closer than I estimated, and the estimate
> I flagged as `value_unverified` was wrong in the conservative direction.**

### BUT Cmax IS A 3.7-HOUR SPIKE. GROWTH INTEGRATES OVER MONTHS. THE NUMBER THAT MATTERS IS SUSTAINED EXPOSURE.

**Css,avg = AUC per dose / τ** (this already contains the accumulation term; no double counting):

| regimen | Css ng/mL | **Css µM** | % engaged |
|---|---|---|---|
| 8 mg fasted **monthly** | 4.7 | 0.0074 | 0.5% |
| 8 mg fasted **weekly** | 20.2 | 0.032 | 2.1% |
| ⭐ **8 mg FED weekly** | **29.0** | ⭐ **0.045** | ⭐ **2.9%** |
| **8 mg FED twice-weekly** (= 16 mg fed weekly) | 58.1 | **0.091** | **5.7%** |
| 36 mg fasted monthly | 15.0 | 0.024 | 1.5% |
| 36 mg fasted weekly | 64.4 | 0.101 | 6.3% |

**Accumulation on weekly dosing is 7.3× (t½ 32.7 d) to 9.4× (t½ 43 d). Time to 90% of steady state is
109–143 days** — nearly five months, which is why a loading dose is not optional.

---

## => ⭐⭐⭐ THE CENTRAL RESULT: **MOXIDECTIN CANNOT OVERSHOOT AT ANY TOLERABLE DOSE**

**Dose required for a target sustained concentration**, from Css,avg = Dose / (CL/F × τ), CL/F = 66.2 L/day:

| target Css | ng/mL | mg/day | **mg/week** | 6-month cumulative | verdict |
|---|---|---|---|---|---|
| 0.010 µM | 6.4 | 0.42 | **3.0** | 77 mg | trivially safe |
| 0.020 µM | 12.8 | 0.85 | **5.9** | 154 mg | ~approved dose weekly |
| ⭐ **0.030 µM** | 19.2 | 1.27 | ⭐ **8.9** | **231 mg** | ⭐ **≈ 8 mg weekly** |
| 0.050 µM | 32.0 | 2.12 | 14.8 | 386 mg | beyond data |
| 0.100 µM | 64.0 | 4.24 | 29.7 | 771 mg | ⛔ far beyond data |
| **0.375 µM (= 20% engagement)** | 240 | 15.9 | ⛔ **111** | ⛔ **2,890 mg** | ⛔⛔ **impossible** |

> ### **A TOLERABLE HUMAN REGIMEN DELIVERS A SUSTAINED 2–6% ENGAGEMENT OF THE WNT-LOWERING PHARMACOLOGY. IT CANNOT DELIVER 20%. REACHING THE ICAT REGIME WOULD REQUIRE ~110 mg/WEEK AGAINST A 36 mg SINGLE-DOSE SAFETY CEILING.**

**This inverts the risk profile that R137 and R138 were built on.**

| | R137/R138 assumed | **R139 measures** |
|---|---|---|
| dominant risk | ⛔ **overshoot into the ICAT regime → SHORTER bone** | ✅ **structurally impossible at tolerable doses** |
| dominant risk | — | ⛔ ⭐ **TOO WEAK — a null result** |

> **The drug is SAFE-BY-CONSTRUCTION on the magnitude ladder and UNPROVEN on efficacy. That is the
> opposite of what I feared two rounds ago, and it is a much better problem to have: a null is
> recoverable, a shortened bone is not.**

⭐ **AND IT MAKES THE EXPLANT CHEAPER AND SHARPER.** We no longer need to find the peak of the
dose-response. **We need to know whether the curve has ANY positive region between 0.01 and 0.5 µM —
and those are precisely the concentrations a human can safely achieve.** A 5-point explant across
0.01 / 0.03 / 0.1 / 0.3 / 1.0 µM answers the entire question, and every point is human-relevant.

⭐ **AND IT GIVES SELAMECTIN A NEW ROLE.** Selamectin's IC50 is **0.08–0.14 µM — 10–25× more potent,
and INSIDE the range human moxidectin dosing already reaches.** If the explant shows the effect needs
0.1–0.5 µM, the chemotype can get there; moxidectin is simply the wrong member. ⛔ Selamectin is
veterinary-only, so this is a direction, not a prescription.

---

## => ⛔⛔ THE COLLISION INSIDE OUR OWN STACK — AND I ONLY FOUND IT BY PUTTING R460 NEXT TO THIS ROUND

**`choi2019cxxc5`, already in the atlas at R460:**
- **17β-estradiol INDUCES CXXC5** in human chondrocytes, with β-catenin falling at 24 h
- **CXXC5 is a canonical Wnt BRAKE**
- **`Cxxc5−/−` → delayed growth-plate senescence and +3.8% tibial length**

**Therefore, in a subject on an aromatase inhibitor:**

```
anastrozole  →  ↓ oestradiol  →  ↓ CXXC5  →  ↑ canonical Wnt in chondrocytes
moxidectin   →                              ↓ canonical Wnt in chondrocytes
```

> ### ⛔ **ANASTROZOLE IS ALREADY PUSHING CHONDROCYTE WNT *UP*, AND IT MAY ALREADY BE DELIVERING PART OF THE `Cxxc5−/−` PHENOTYPE. A WNT-LOWERING AGENT ADDED ON TOP RUNS DIRECTLY AGAINST IT. THE TWO MAY CANCEL.**

⚠ **This is NOT a clean contradiction** — R137 established that SPIN4 loss (Wnt-down) and CXXC5 loss
(Wnt-up) **both** lengthen bone, acting on different terms (N vs duration) and plausibly on R117's two
opposing-Wnt-requirement stem populations. **But "they are orthogonal" is a hypothesis, and adding a
Wnt-lowerer to a stack whose AI is already raising Wnt is exactly the case where it has to be right.**

> ⭐ **THIS PROMOTES R137's Spin4 × Cxxc5 DOUBLE-PERTURBATION EXPERIMENT FROM "INTERESTING" TO
> "REQUIRED BEFORE MOXIDECTIN GOES NEAR A STACK CONTAINING AN AROMATASE INHIBITOR."** If the double
> exceeds both singles, the arms are orthogonal and additive. If it is worse than either, they share
> one shelf and the AI has already spent it.

⚠ Caveat kept: **R462 flagged the oestrogen sign as CONTESTED** — `yan2022` has E2 → ERα/β → DMP1 →
**raising** GSK-3β/β-catenin → closure, the opposite β-catenin direction to `choi2019`. **Unresolved,
and it matters here: if `yan2022` is right, anastrozole LOWERS Wnt and moxidectin is ADDITIVE rather
than antagonistic. The sign of this interaction is genuinely unknown and it flips the recommendation.**

---

## => ⛔ THE SAFETY HOLE THAT IS SPECIFIC, NAMED, AND CHECKABLE: **P-GLYCOPROTEIN**

`Cotreau` states the safety mechanism explicitly:

> *"macrocyclic lactones are generally excluded from the cerebrospinal fluid when the blood-brain
> barrier is intact **due to the presence of the ABC transporter, P-glycoprotein (P-gp)**… In vitro
> data support that MOX is also a substrate for this transporter."*

**Moxidectin's entire CNS safety margin is P-gp efflux at the blood-brain barrier.** Collie dogs with
an MDR1 deletion are the natural knockout, and they are macrocyclic-lactone-sensitive.

**Cotreau's own dose-limiting signal was CNS:** dizziness and somnolence/lethargy in 8 subjects,
rising in frequency at 18 and 36 mg, and **the study was terminated before the 54 mg cohort** for that
reason — all events grade 1–2, and on unblinding the frequency was low, so 36 mg is a cautionary
ceiling rather than a toxic one.

### ⭐ AND OUR STACK CONTAINS A DRUG WHOSE P-gp STATUS IS UNTESTED

I checked erdafitinib's clinical DDI data. **`PMID 39044705` (2024) probed erdafitinib against
midazolam (CYP3A4) and metformin (OCT2) at steady state, n=25:**

| probe | GMR 90% CI | interpretation |
|---|---|---|
| midazolam | 86.3 / 88.5 / 82.1% | **no clinically meaningful CYP3A4 inhibition** |
| 1-OH midazolam | 99.8 / 97.4 / 101.5% | unchanged |
| **metformin** | 108.7 / 119.0 / 113.9% | ⭐ **no meaningful OCT2 interaction — the metformin arm is compatible with erdafitinib** |

> ⛔ **BUT NEITHER PROBE TESTS P-gp. Erdafitinib's effect on P-gp is not established by this study,
> and P-gp is the exact transporter on which moxidectin's CNS safety depends. This is a specific,
> checkable, REQUIRED interaction study before co-administration — not a formality. I am flagging it
> as an unresolved hazard rather than asserting a direction, because I do not have the data.**

⚠ **Also required for the same reason:** any P-gp inhibitor of any kind (including common ones —
verapamil, ketoconazole, ritonavir, quinidine, and grapefruit, which Cotreau's protocol explicitly
prohibited for two weeks post-dose).

⚠ **And an erdafitinib cost this file should have on record:** FGFR-inhibitor retinopathy occurred in
**13.7% (43/314, RAGNAR) to 21.5% (103/479, pooled mUC)** of erdafitinib-treated patients, **78.6%
within 90 days**, mostly grade 1/2, grade 3 in 1.0–2.3%, managed by interruption or dose reduction,
**92% of visual acuity returning to baseline.** For a multi-year growth protocol this is a scheduled
ophthalmology requirement, not a footnote.

---

## => THE REGIMEN, IF IT WERE TO BE RUN — AND WHY IT STOPS WHERE IT STOPS

**Shape:** load to overcome the 4–5 month time-to-steady-state, then maintain low.

| element | value | rationale |
|---|---|---|
| **loading dose** | ⭐ **36 mg once, WITH A HIGH-FAT MEAL** | **Load = Css_target × Vd/F. For 0.020 µM that is EXACTLY 36 mg — the largest dose ever given to a human. The arithmetic and the safety ceiling coincide precisely.** |
| **maintenance** | **8 mg weekly, with food** | Css,avg ≈ **0.045 µM ≈ 2.9% engagement**; 8 mg is the approved unit dose; food adds +44% AUC |
| **formulation** | **tablet** (the approved form) | liquid gives ~28% higher Cmax/AUC — a hidden dose escalation if substituted |
| **6-month cumulative** | **≈ 244 mg** | ⛔ **see below** |
| **monitoring** | CNS symptom diary; ophthalmology (erdafitinib); **no P-gp inhibitors, no grapefruit** | |

> ### ⛔⛔ **AND HERE IS WHERE I STOP, AND IT IS NOT A FORMALITY.**
> **THE ENTIRE HUMAN MOXIDECTIN DATABASE IS SINGLE DOSES.** Cotreau: single ascending 3–36 mg.
> tropmed: single 8 mg. CPDD: single 10 mg. Mass drug administration: **annual**.
> **244 mg cumulative over six months is ~7× the largest single dose ever administered to a human,
> delivered into a drug with a 33–43 day half-life and a 7–9× accumulation ratio on weekly dosing.
> NO ONE HAS EVER DONE THIS. There is no repeat-dose human safety data at any interval shorter than
> a year, and the dose-limiting toxicity is CNS and exposure-dependent.**
> **The regimen above is arithmetically correct and empirically unsupported. It is what the numbers
> say, not what the evidence permits.**

---

## => CARTILAGE PENETRATION: REASONED FROM FIRST PRINCIPLES, BECAUSE NO MEASUREMENT EXISTS

I searched again and there is **no measurement of macrocyclic lactone concentration in cartilage or
synovial fluid.** What can be said:

| barrier | verdict |
|---|---|
| **size** | ✅ **NOT a barrier.** 640 Da. Cartilage matrix passes solutes well below ~10 kDa; a 640 Da neutral molecule equilibrates across cartilage in hours. |
| **charge** | ✅ **NOT a barrier.** Cartilage GAGs impose Donnan exclusion on cations/anions; moxidectin is neutral. |
| ⚠ **lipophilicity** | ⚠ **THE PROBLEM.** logP ~5–6, Vd/F 2,829–3,635 L (≈ 38–48 L/kg) — the drug partitions overwhelmingly into **fat and liver**. Cartilage is ~75% water and lipid-poor. **Tissue-average concentration is ~1,000× plasma; cartilage concentration is plausibly at or BELOW plasma.** |
| ⚠ **protein binding** | ⚠ unknown for moxidectin in humans from these three papers; only free drug diffuses |
| ⭐ **perfusion of the target zone** | ⭐ **FAVOURABLE.** The **resting zone is supplied by epiphyseal cartilage canals** and is the best-perfused zone of the growth plate. **The compartment we are targeting is the one closest to blood supply** — the hypertrophic zone, which we must NOT deplete, is the furthest. |

> ⭐ **That last row is not a small point: the delivery gradient and the therapeutic gradient run the
> same way. Whatever reaches the plate reaches the resting zone first and the hypertrophic zone last,
> which biases a systemic dose toward the compartment we want and away from the one that ICAT
> destroys.** ⚠ Reasoning, not measurement — flagged as such.

---

## => ⛔ THE CALIBRATION CONSTANT THAT IS STILL MISSING, AND IT IS NOW THE #1 HOLE

**I can now state what fraction of the Wnt pathway a given moxidectin dose engages. I still cannot
state what fraction Spin4 loss engages.**

`Lui 2023` measured it twice — reduced baseline TOPFLASH in Spin4-KO chondrocytes (Fig 6C) and reduced
**Axin2 mRNA** (Fig 6D) — **but both are FIGURE-ONLY. No percentage appears in the text.**

> ### **THAT NUMBER IS THE CALIBRATION CONSTANT FOR THE ENTIRE DOSING CALCULATION. Without it, "2–6% engagement" cannot be compared to the target. With it, the dose is fully determined.**

**What can be bounded from the ladder:** `Cxxc5−/−` removes **one of several DVL scaffolds** → +3.8%;
`Col2a1-ICAT` is near-complete blockade → shortens. **A single-reader LOF plausibly sits at 10–30%
pathway reduction, which would put a tolerable moxidectin regimen BELOW the effective window** — the
"too weak" failure mode, not the "overshoot" one.

---

## => WHAT CHANGES

| | |
|---|---|
| ⭐⭐ **the exposure gap** | **CLOSED as arithmetic.** 16× at the approved dose, **3× at the maximum human dose** — not the 100× I guessed in R138. |
| ⭐⭐⭐ **the risk profile INVERTS** | **overshoot is structurally impossible at tolerable doses; the real risk is a NULL.** Better problem. |
| ⭐ **the explant gets cheaper** | one 5-point curve across **0.01–1.0 µM**, every point human-achievable |
| ⭐ **selamectin re-roled** | its IC50 (0.08–0.14 µM) sits **inside** achievable exposure — the chemotype can reach the window even if moxidectin cannot |
| ⛔⛔ **a stack collision found** | **anastrozole → ↓CXXC5 → ↑Wnt vs moxidectin → ↓Wnt.** May cancel. **Sign contested (`choi2019` vs `yan2022`) and the contest flips the recommendation.** |
| ⛔ **a named safety hole** | **erdafitinib's P-gp status is untested**, and P-gp is moxidectin's entire CNS safety margin |
| ✅ **one interaction cleared** | **erdafitinib does NOT meaningfully affect metformin (OCT2) or CYP3A4** — the metformin arm is compatible |
| ⛔ **still nothing enters** | no repeat-dose human data at any interval under a year; calibration constant missing |

---

## => WHAT I NEED — RANKED, AND THE FIRST ONE IS NOW DECISIVE

1. ⭐⭐⭐ **The PERCENTAGE Wnt reduction in Spin4-KO chondrocytes** — `Lui 2023` Figures 6C and 6D, or
   the source data. **This is the calibration constant. Everything else in the dosing calculation is
   solved; this single number converts "2–6% engagement" from a floating figure into a verdict.**
2. ⭐⭐ **Any repeat-dose moxidectin human data** — the DOLF programme, or the mini-SPIOMET-style
   trials; anything with an interval shorter than annual. **Without it the regimen above cannot be run.**
3. ⭐ **`Melotti` Figure 2E's concentration** — the table showing moxidectin's AXIN2/LGR5 suppression
   does not state the concentration in the text I extracted. It anchors moxidectin's own IC50 rather
   than inheriting ivermectin's.
4. **Erdafitinib and P-gp** — the FDA clinical pharmacology review, or any transporter DDI study.
5. **Moxidectin plasma protein binding**, and **anything on macrocyclic lactone partition into
   cartilage or synovial fluid.**
6. Still outstanding: **erda hand/wrist films**; **sitting height vs subischial leg length +
   ring-apophysis staging**; **NT-proCNP**; **liver fat**.

---

## CORRECTIONS

- ⭐⭐ **R138's "~2 orders of magnitude below" is WRONG and was wrong in the conservative direction.**
  The approved 8 mg dose reaches **0.092 µM against a ~1.5 µM IC50 — a 16-fold gap; 36 mg reaches
  0.45 µM, a 3-fold gap.** I had flagged it `value_unverified`; it is now measured.
- ⭐⭐⭐ **The RISK PROFILE OF THE WHOLE PROPOSAL INVERTS.** R137 and R138 were built on the fear of
  overshooting into the ICAT regime. **At any tolerable human dose that is arithmetically impossible —
  20% engagement would require ~110 mg/week against a 36 mg ceiling. The real risk is that the agent
  is TOO WEAK.**
- ⭐ **R138's "sub-saturating dosing may be the therapeutic window" — flagged there as the most
  motivated-reasoning-prone claim — is now SUPPORTED BY ARITHMETIC rather than by hope.** The
  sub-saturating regime is not a hopeful choice; it is the only regime available.
- ⛔⛔ **A STACK COLLISION FOUND AND NAMED:** anastrozole lowers oestradiol → lowers CXXC5 → **raises**
  chondrocyte Wnt, which a Wnt-lowering agent opposes. **Promotes the Spin4 × Cxxc5 double-perturbation
  from "interesting" to "required before moxidectin goes near an AI."** ⚠ Sign contested
  (`choi2019` vs `yan2022`) and the contest reverses the conclusion.
- ⛔ **P-gp named as the specific safety hole** — moxidectin's CNS margin depends entirely on it, and
  **erdafitinib's P-gp status is untested** (the 2024 DDI study probed only CYP3A4 and OCT2).
- ✅ **Erdafitinib × metformin CLEARED** (OCT2 GMR 108.7–119.0%) — the metformin arm is compatible.
- ⚠ **Erdafitinib retinopathy quantified for the record:** 13.7–21.5% incidence, 78.6% within 90 days,
  grade 3 in 1.0–2.3%, 92% of visual acuity recovering. A scheduled ophthalmology requirement.
- ⛔ **The regimen is stated as arithmetically correct and EMPIRICALLY UNSUPPORTED** — 244 mg over six
  months is ~7× the largest single human dose, into a drug with a 33–43 day half-life, and **no human
  has ever received repeat moxidectin at an interval under a year.**
- ⭐ **Cartilage penetration reasoned rather than measured:** size and charge are not barriers,
  lipophilicity and protein binding are the unknowns, **and the resting zone — our target — is the
  best-perfused zone of the plate while the hypertrophic zone is the furthest from supply.**
