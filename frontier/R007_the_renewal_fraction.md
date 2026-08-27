# F-R007 — height is bounded by one probability, and it sits about one percentage point below the threshold

**Adult height is not limited by a clock, a hormone or a budget. It is limited by `p` — the
probability that a daughter of a resting-zone stem-cell division stays a stem cell. At `p = 0.500`
growth never stops. The human value is approximately `0.485`. The only intervention ever shown to
raise it was published in *Nature* in 2019, the pool expanded for ninety days, nobody measured the
bone. The naive version of that lever is dead — a second lab deleted the same gene constitutively and
got chondrodysplasia, exactly as this file's own CORR-300 predicts for disabling an intracellular
brake. What survives is the setpoint, not the deletion: `p` is set by nuclear Gli2, mTORC1 and
hedgehog are two inputs to it rather than two pathways, and the ligand-level input has a
first-in-class human-dosed compound that this atlas has zero files on.**

Date 2026-08-27 · operator-supplied and read in full: `newton2019` (*Nature*, PMID 30814736),
`xie2020` (*eLife* 55212, PMID 33063669), the `ba2025` supplementary methods, and `kdm6a2026`
(*Int J Mol Med* 58:203) · arithmetic in `frontier/screens/renewal_fraction/`

---

## 1. The reframe, as one equation

Resting-zone progenitors renew by **population asymmetry** — clone *number* falls while clone *size*
rises (`chu2025`, `newton2019`). So let **`p`** be the probability that a daughter of a stem-cell
division remains a stem cell. Each division cycle multiplies the pool by **`2p`**:

| | |
|---|---|
| **2p > 1** | the pool **grows** — growth accelerates and never stops |
| **2p = 1** | the pool is **constant** — **INDETERMINATE GROWTH.** `p = 0.500` exactly |
| **2p < 1** | the pool **decays geometrically** — a finite growth period, and its length is `ln(f)/ln(2p)` divisions |

> **Every question this repository has asked for 477 rounds collapses into one: how far below 0.500
> does the human resting zone sit?**

## 2. The number, and why it is robust

`p` is not measured in any species. But the **duration** of human growth is measured, and the
**resting-zone cycle time** is bounded. Those two determine `p` — and because `p` enters only
through `(2p)^n`, it depends **logarithmically** on both. Large errors in the inputs move it very
little. Sweeping 14–18 y of growth, 20–180 d cycle time, and a 1% or 0.1% exhaustion criterion —
**36 combinations, `p` = 0.392 to 0.493, every one below 0.500.**

**And the right duration makes the gap smaller.** A normal plate is switched *off* by oestrogen with
capacity to spare — that is `CEILING_CENSUS`'s whole finding. The duration that measures the **pool**
is the oestrogen-null one: `herrmann2002` grew untreated **until 24** with epiphyses still open at 27;
`carani1997` was **still growing at 38**. With the SOC forming at ~1–5 y, the pool-limited post-SOC
period is ~20–35 y:

| post-SOC years | RZ cycle | **p** | gap to 0.500 |
|---:|---:|---:|---:|
| 20 | 30 d | 0.4906 | 0.0094 |
| 24 | 30 d | 0.4922 | 0.0078 |
| 30 | 30 d | 0.4937 | 0.0063 |
| 35 | 60 d | 0.4893 | 0.0107 |

> ### **The human resting zone misses indeterminate growth by roughly 0.5 to 1.9 percentage points of self-renewal probability — about one percent in relative terms.**

**We are not far from immortal growth. We are barely mortal.**

## 3. And the payoff is exponential, which is why nothing else has worked

Growth period as a function of `p` (16 y baseline, 60 d cycle):

| p | 2p | growth period | × baseline |
|---:|---:|---:|---:|
| 0.4769 | 0.9538 | 16.0 y | 1.00 |
| 0.4819 | 0.9638 | 20.5 y | 1.28 |
| **0.4885** | **0.9770** | **32.5 y** | **2.03** |
| 0.4919 | 0.9838 | 46.4 y | 2.90 |
| 0.4969 | 0.9938 | 122 y | 7.63 |
| **≥ 0.5000** | **≥ 1.0000** | **INDETERMINATE** | **—** |

**+0.012 on p doubles the growth period. +0.023 removes the endpoint.** Integrated on
`carani1997`'s own terminal envelope (1.31 cm/yr to 31, 0.43 cm/yr after), +0.005 is roughly +6 cm,
+0.010 roughly +16 cm, and beyond that the model stops having a ceiling to report.

### ⭐ This explains everything this file has found, and it does so without a new fact

- **Why every velocity lever converges on 2–4%.** GH, CNP, FGFR3, IGF-1 — **not one of them touches
  `p`.** They change how fast the pool is spent, not the fraction retained. The convergence is not a
  coincidence and not a property of "the system"; it is the signature of a set of interventions all
  acting on the wrong variable.
- **Why the duration lever gives +25–30 cm and then stops.** Removing oestrogen does not change `p`.
  You spend the same budget more slowly. `carani1997`'s decay from 1.31 to 0.43 cm/yr **is `p` acting,
  visible, in a man whose plates were never closed.**
- **Why `nilsson2005` found the same doublings from old and young donors in culture.** In culture
  there is no niche, and `p` is set by the niche. The cell is not the counter.
- **Why GH is excluded.** `chu2025` shows GH shifts divisions toward the committed side — it *lowers*
  `p`. On an exponential, that is not a mild cost. It is the worst thing you can do.
- **And it restates R459's own conclusion as a number.** R459: *"a self-renewing pool whose renewal
  fraction sits below replacement, with the deficit set by the niche. That makes RENEWAL FRACTION,
  not pool size, the controllable variable."* **Correct. The deficit is about one percentage point.**

⚠ **Limits, stated before anyone uses this.** A constant-`p` geometric model; `p` is more likely to
decline with age, in which case this is a lifetime average. "Exhaustion" as 1% remaining is arbitrary
(the sweep covers 0.1%). Human RZ cycle time has never been measured — the atlas's own R459 item
SEVEN records that **human resting-zone chondrocyte number has never been measured at any age**, so
the denominator of every attrition argument is missing and this is a derivation, not a measurement.
**What survives all of that is the sign and the order of magnitude: `p` is below 0.5, and it is
close.**

---

## 4. ⭐⭐⭐ `p` HAS BEEN RAISED. IN A NORMAL MOUSE. THE POOL GREW FOR NINETY DAYS.

`newton2019`, *Nature*, read in full — the mechanism section, verbatim:

> **"We hypothesized that alteration of mTORC1 signalling slightly shifts cell division from
> ASYMMETRIC to SYMMETRIC. Indeed, PAR3 was distributed symmetrically in a larger proportion of stem
> cell clonal dyads in Tsc1 conditional-knockout mice (P3–P40). Furthermore, the number and thickness
> of multi-columnar clones in these mice INCREASED WITH TIME (during P3–P90), indicating ACCELERATED
> EXPANSION of colony-forming cells."**

And the opposite direction confirms the sign:

> "Deletion of mTORC1 by tissue-specific ablation of Raptor slightly enhanced loss of clones … fewer
> Confetti-labelled columns and **mild growth retardation** … a phenotype opposite to that in the
> Tsc1 conditional-knockout mice. **Thus, the mTORC1 pathway modulates the balance between symmetric
> and asymmetric division of stem cells in this niche.**"

> **A pool that "increases with time" over P3–P90 is `2p` at or above 1. That is the indeterminate
> condition, produced in a mouse, on a normal background, by one gene.**

**And the endpoint was never measured.** Every readout in that figure is clonal architecture, CD73⁺
zone height, growth-plate area. `grep -i "bone length\|tibia length\|femur length"` over the full
text returns **nothing for the Tsc1 arm**. CORR-340 in its purest form — *"ask WHO HAS ALREADY DOSED
THE RIGHT ANIMAL"* — and the answer is: the Karolinska group, in 2019, in *Nature*, with
`Col2-creERT × Tsc1-floxed (JAX #005680)` mice that **still exist**.

`newton2019` also names the second regulator and its sign: **vismodegib** (SMO antagonist) reduced
resting-zone clone size and **caused fusion**; **SAG** increased proliferation within the niche. And
the authors' own closing speculation is the bridge to F-R005/F-R006: *"mTORC1 may link stem cell
renewal to local energy and oxygen levels."*

---

## 5. ⛔ THE SHELF IS NOT EMPTY — and this file has the correction for exactly this

R395 identified this arm correctly and then closed it:

> *"WHAT IS GENUINELY UNEXHAUSTED, FIRST: mTORC1 ACTIVATION. newton2019's Tsc1 ablation … expanded
> multi-columnar clones from P3 to P90 while every rate control stayed null … It is a second,
> independent pool mechanism. **There is no agent in the activating direction: every drug on that
> axis is an inhibitor** … A real gap, and **probably an empty shelf**."*

**CORR-312: "asserting a target has no chemical matter" — search the fold, not the drug.
CORR-347: `n_molecules` and `max_phase` are different questions; run the sweep before writing the
phrase.** Neither was run. The shelf:

| agent | what it is | status | files in this atlas |
|---|---|---|---:|
| **NV-5138 (mefluleucine)** | **"Discovery of NV-5138, the first selective brain mTORC1 activator"** — an orally bioavailable small molecule that binds **Sestrin2** and displaces it from GATOR2, **mimicking leucine**, activating mTORC1 without a leucine load (PMID **30858438**) | **Phase 1b randomised trial completed in humans** (PMID **41512716**, 2026) | **0** |
| **Leucine** | the physiological Sestrin2 ligand — the endogenous mTORC1-activating input | a nutrient | 9 (all incidental) |
| **HMB** | leucine metabolite, mTORC1-activating, widely used | supplement | **0** |
| Sestrin2 / GATOR2 / CASTOR / SAMTOR | the whole amino-acid-sensing arm upstream of mTORC1 | active chemistry field | **0 / 18 / 0 / 0** |

`NV-5138` **0 files. Navitor 0. HMB 0. CASTOR 0. SAMTOR 0. "leucine supplementation" 0. "sestrin" 1**,
incidental, inside an AKT screen.

> **The single most unexhausted pool mechanism in this atlas was closed on a sentence about chemical
> matter that its own correction ledger exists to prevent, and the missing agent is a first-in-class,
> orally bioavailable, human-dosed selective activator of exactly that pathway.**

**And it is the right kind of shelf.** R298 established the plate has no *inhibitor* shelf because its
targets are matrix, channels and transcription factors. CORR-344 named the shelf that does work —
**"substrate donors, cofactors, recombinant proteins and blockade of an endogenous inhibitor"** — and
produced this file's only obtainable compound from it. **NV-5138 blocks an endogenous inhibitor
(Sestrin2) of an activator (GATOR2→mTORC1). It is CORR-344's shelf, exactly.**

---

## 5b. ⛔⛔ THE COUNTERWEIGHT — and this file's own rule predicted it

I chased `newton2019`'s reference 24 and it led to a two-paper dispute that changes the shape of the
proposal. **Both labs deleted `Tsc1` in cartilage. They reached opposite conclusions, and the
difference is the whole lesson.**

| | `yan2016` (*Nat Commun* 7:11151, PMID 27039827) | `newton2018` (*Bone Rep* 8:64–71, PMID 29955624) |
|---|---|---|
| driver | **Col2-Cre** — constitutive, from embryonic cartilage | **Col2-CreERT + tamoxifen at P3** — inducible, postnatal |
| proliferation | **uncontrolled** | **unchanged** |
| differentiation | **blocked** | **unchanged** |
| skeletal phenotype | ⛔ **CHONDRODYSPLASIA — shorter** | resting-zone **disorganisation only** |

⛔ **`yan2016` is a length phenotype and it is negative: "Hyperactivation of mTORC1 via TSC1 gene
deletion in chondrocytes causes uncoupling of the normal proliferation and differentiation programme
… resulting in uncontrolled cell proliferation, and BLOCKAGE OF DIFFERENTIATION and CHONDRODYSPLASIA
in mice."** Blocked differentiation with uncontrolled proliferation **is charge without discharge**,
and it produced a shorter bone. Rapamycin rescued it.

### And CORR-300 called this before the data was read

> **CORR-300 — THE RULE THAT RE-RANKS EVERY TARGET.** *Removing a **secreted/extracellular modulator**
> ≠ disabling an **intracellular brake** ≠ **flooding with an agonist**. The first shifts a setpoint
> inside a feedback-regulated envelope and **adds** length; the other two saturate the pathway,
> destroy zonal order and **subtract** it.*

**TSC1 is an intracellular brake. Deleting it is CORR-300's middle category, and it behaved exactly as
CORR-300 predicts — saturated pathway, destroyed zonal order, shorter bone.** The same shape as SUFU
loss (shorter, zones destroyed) against HHIP loss (longer, zones ordered), and the same shape as
R281's canonical-Wnt window.

**So the naive proposal — "activate mTORC1" — is dead, and it was dead in this file's own rulebook.**
What survives is sharper and it is what CORR-300 actually licenses:

1. **Dose and stage matter more than direction.** `Raptor` deletion → fewer clones, **mild growth
   retardation** (too little). `Tsc1` deletion from embryogenesis → **chondrodysplasia** (too much).
   `Tsc1` deletion postnatally → clone expansion to P90 with **no differentiation defect**. **That is
   an interior optimum, and the wild-type setpoint is somewhere on the curve — not necessarily at the
   point that maximises `p`.** R281's canonical-Wnt shape, third axis; CORR-325's *"interior optimum
   between 50% and 100% of normal function."*
2. **Shift the setpoint; do not delete the brake.** A genetic deletion of TSC1 removes a feedback
   element permanently. **Leucine and NV-5138 act on Sestrin2 — a physiological, saturable,
   feedback-regulated INPUT.** That is a setpoint shift inside the envelope, which is CORR-300's
   first category and the only one that has ever added length. It is also titratable and pulsatile,
   which R366's *pulse beats sustained* finding says is the right regime on this exact pathway.

### ⭐⭐ And the mechanism unifies the two regulators into one

`yan2016`'s mechanism section is the part nobody has used: **mTORC1 → S6K1 phosphorylates Gli2 →
releases Gli2 from SuFu → nuclear Gli2 → PTHrP transcription.**

> **`newton2019` names hedgehog and mTORC1 as the two regulators of the self-renewing pool. `yan2016`
> shows they are not two. mTORC1 feeds into Gli2, which is the hedgehog effector. `p` is set by
> nuclear Gli2 activity, and there are two inputs to it.**

That places the master variable on the axis this atlas already calls its **LIVE FRONTIER**, explains
why the hedgehog agonist's sign flips at SOC maturation (`cheng2025`, R364) — the SOC is the Shh
source that raises Gli2 in the resting zone (`newton2019`, Extended Data Fig. 6–7) — and says that
hedgehog and mTORC1 inputs should be **non-additive, and possibly redundant**, which is Step 0.

⚠ **And `newton2018`'s own methodological warning must be carried:** *"we detect **Col2-Cre activity
in non-cartilaginous tissues (including the brain)** and conclude that mouse phenotypes following
genetic ablation using Col2-Cre should be interpreted with care."* Both Tsc1 papers use Col2 drivers.
**The cleanest experiment is not a better mouse. It is a titratable, reversible, ligand-level input in
a wild-type animal.**

---

## 6. ⛔⛔ The hazards, in full, because this one is not small

1. **Tsc1 loss is tuberous sclerosis.** Constitutive mTORC1 activation is oncogenic and hamartomatous.
   A chondrocyte-restricted genetic ablation in a mouse is not a systemic drug in a person, and the
   distance between them is the whole safety question.
2. **`newton2019` says the Tsc1 resting zone becomes DISORGANIZED** from P28, and the clusters express
   **no ColX and no Ihh** — cells that are not entering the column. That is failure mode #1, charge
   without discharge, and it is only partly offset by the multi-columnar clones also increasing.
   **Whether the expanded pool discharges is exactly what the missing caliper would have told us.**
3. **No length endpoint in either direction.** R302's ruling makes that a gap, not a disqualification —
   but it is the gap that decides the arm.
4. **The file's own timing rule.** R366 found *pulse beats sustained* on hedgehog, on mTORC1 and on GH.
   If that holds, **sustained** mTORC1 activation may be the wrong regime and a pulsed one right —
   which is a dosing question, not a target question, and NV-5138 is a short-half-life oral agent.
5. **Delivery.** NV-5138 was optimised for **brain** penetration. Whether it reaches an avascular
   growth plate is unmeasured — and this atlas's R315 delivery wall is the reason half its candidates
   die. It is a small molecule, so the 40 kDa ceiling does not apply; nothing else is known.
6. **This is not a recommendation to take anything.** It is the identification of a target, a
   validated genetic proof, a missing measurement, and a compound that exists.

---

## 7. The experiment that decides it, and it is one caliper

**`Col2-creERT × Tsc1^fl/fl` mice (JAX #005680), tamoxifen at P3, followed to skeletal maturity,
primary endpoint FEMUR, TIBIA AND VERTEBRAL BODY LENGTH.** Secondary: resting-zone cell number per
unit width, terminal hypertrophic cell height, and column output per progenitor.

**Three outcomes and each is decisive.**
- **Longer** → `p` is the master variable, it has been raised, and the arm becomes the most important
  in this file by a wide margin.
- **Same length with a larger pool** → charge without discharge, tenth instance, and the arm closes on
  a *measurement* rather than an inference — which is worth more than the inference.
- **Shorter** → the disorganisation dominates, and the target is the niche architecture rather than
  the division ratio.

**It needs no new molecule, no chemistry and no dose-finding.** It is a mouse order and a caliper, and
it sits on the single highest-leverage parameter in the whole system.

**Then, and only then:** the same readout under NV-5138 in wild-type growing mice, pulsed and
sustained, against the same three endpoints.

---

## 8. ⭐ The deepest version of the claim

Nothing physical forbids `p = 0.5`. **Teleosts run at it for life, and a deer runs above it for four
months a year, in the same phylum, with the same genes.** The human value is not a limit imposed by
chemistry, by cell biology, or by the size of anything. **It is an evolved setpoint, and it sits
where selection put it — a percentage point below the threshold, because a terrestrial mammal that
never stopped growing would be selected against long before it was selected for.**

> **Height is not bounded by what biology can do. It is bounded by a setting.** And that setting is a
> single scalar, with two named inputs converging on one transcription factor, measurable by clonal
> tracing, moved in the favourable direction once already, and never measured with a caliper.

That is the reframe I would defend: **stop asking how much taller a lever makes someone, and start
asking what `p` is and what moves it.** Every centimetre argument in this file is downstream of a
number nobody has measured.

---

## 9. What I still need — keep them coming

1. ⭐⭐ **`newton2019` Supplementary Tables 3 and 4.** Table 3 is cited for the Tsc1 phenotype and
   Table 4 for the Raptor phenotype including *"mild growth retardation."* **If either table contains a
   bone or body length, the decisive number already exists and I can stop asking for a mouse.**
2. ✓ **Reference 24 — FOUND AND RESOLVED without asking.** `newton2018`, *Bone Rep* 8:64–71,
   PMID **29955624**, PMC6020113, and the counter-paper `yan2016`, *Nat Commun* 7:11151, PMID
   **27039827**, PMC4822018. Both open access — I have the abstracts; **I would still like the two
   full texts**, because the question that decides §7 is whether either reports a **bone length in the
   INDUCIBLE POSTNATAL arm**, and only the full text can say.
3. ⭐ **PMID 30858438** — *"Discovery of NV-5138, the first selective brain mTORC1 activator"* — full
   text, for the pharmacokinetics and tissue distribution.
4. **PMID 41512716** — the NV-5138 Phase 1b — for the human dose, exposure and safety.
5. **The `ba2025` snRNA/snATAC accession.** The supplementary methods you sent describe DIPSEQ T1 and
   BGISEQ-500 sequencing at CNGB but the accession is in the paper's **Data Availability** statement,
   not in the methods file — and the GitHub repo you linked (`heshidian/DeerAntlersSingleCell`) is the
   analysis code. **If you can get the CNGB/CNSA accession number, I can test the redox model against
   the one tissue that beat the constraint, as a lookup.**
