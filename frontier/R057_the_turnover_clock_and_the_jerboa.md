# F-R057 — The turnover clock, the jerboa, and why every banking agent so far has bought time instead of speed

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** Four supplied items read in full, plus Cooper 2013, Wilsman 1996, Bush 2010, Abubakar 2022,
Gerber 1999 and Voss 2015 retrieved and read.

**The finding that reorganises the whole branch:** the hypertrophic zone turns over on a roughly fixed
clock, so `dL/dt = N_h · h_term / τ`. Every intervention I have called "banking" — dexamethasone,
resveratrol, VEGF blockade — raises the numerator **and** lengthens τ, which is why each one delays
fusion and yields almost no extra length. **One system in nature raises the numerator without touching
τ, and it is the jerboa metatarsal.** Its mechanism is named, local, and IGF-1-dependent.

---

## 0. Corrections to my own prior rounds, first

**F-R055 read Haraguchi's *Hhip1* limb cKO as a clock lever. It is not.** The figure the user supplied
gives the numbers I had asked for twice, and they say the opposite of what I assumed.

| | 10 wk male | 53 wk male |
|---|---|---|
| bone length, control → mutant | ~1.49 → ~1.53 cm (**+2.7%**), * | ~1.55 → ~1.62 cm (**+4.5%**), *** |
| body weight | ns | ns |
| growth-plate area | 0.44 → 0.62 mm² (**+41%**), ** | 0.29 → 0.42 mm² (**+45%**), ** |

Look at the two plate-area columns down the page rather than across it. **Control falls 0.44 → 0.29
(−34%). Mutant falls 0.62 → 0.42 (−32%).** The decline is parallel. Deleting *Hhip1* raised the
amplitude of the plate by ~43% and **left the senescence slope untouched.** The length gap widens from
2.7% to 4.5% because a larger plate produces more per unit time for as long as it lasts — not because
the clock stopped. *Hhip1* is an `A`-type free multiplier, not a `(b−a)` lever. F-R055 said otherwise
and was wrong.

**Second correction, pre-emptive.** Karimian's discussion says *"less than 10% of bone growth has been
linked to cell proliferation while 60% results from chondrocyte hypertrophy and the rest from matrix
deposition,"* citing Wilsman 1996. I nearly took that at face value, because it flatters the branch's
central claim. It does not mean what it appears to mean. Wilsman decomposes the **height a single
column gains**, not the sensitivity of growth rate to division rate. Read correctly it says: *a
chondrocyte's own starting height is under 10% of the height it eventually occupies* — i.e. the
per-cell amplification from flattened proliferative cell to terminal hypertrophic cell is roughly
tenfold. That is a strong result for `h_term`. It is **not** a licence to say λ is free. Karimian's own
data show why (§3).

Wilsman's actual numbers, across four rat growth plates at 28 days: in more slowly elongating plates the
contribution from cellular enlargement **falls from 59% to 44%**, with matrix synthesis rising from
**32% (proximal tibia) to 49% (proximal radius).** So enlargement and matrix together carry ~91% of
column height in every plate measured, and the split between them is what differs between fast and slow
plates.

---

## 1. Xiu — too little and too much Hedgehog both close the plate early

**Xiu et al., Frontiers (supplied as `r_p3.txt`).** The result that constrains the entire Hedgehog arm:

> *"ablation of either Smo or Sufu in chondrocytes of juvenile mice caused **premature closure of growth
> plates and shorter limbs**."*

Smo loss accelerated hypertrophy; Sufu loss suppressed it; **both decreased proliferation.** Hh acts in
the **resting and columnar** chondrocytes — Osx-Cre, hitting prehypertrophic cells, produced no defect.
The paper's own conclusion is that *"tightly-regulated Hh signaling"* is required.

Smo is the transducer. Sufu is the intracellular brake on Gli. Deleting either — one loss of signal, one
loss of restraint — produces the same phenotype: **premature closure.** The Hedgehog response is
bell-shaped and the plate sits near the top of the bell.

**This does not kill the Hedgehog arm; it specifies it.** Haraguchi's *Hhip1* cKO lengthened bones and
expanded plates for 53 weeks. HHIP1 is a **secreted, extracellular, ligand-sequestering** brake: removing
it raises the effective ligand concentration and shifts the gradient. Sufu and Ptch1 are **intracellular
transducer-level** brakes: removing them decouples output from ligand entirely and destroys the gradient.

> **Design rule, refined from F-R055:** remove brakes that act on the **ligand**, never brakes that act on
> the **transducer**. HHIP1 is on the safe side of that line; Sufu and Ptch1 are not; and pushing Smo with
> an agonist sits on the wrong side too, which is a second, independent reason systemic SAG did nothing
> in wild-type animals (F-R053, F-R054).

---

## 2. Karimian — the first agent to move every term of the identity in the right direction at once

**Karimian E, Tamm C, Chagin AS, Samuelsson K, Kjartansdóttir KR, et al. PLoS ONE 2013;8(6):e67859.**
*trans*-resveratrol, **200 mg/kg/day orally, 16 weeks**, pre-pubertal New Zealand White rabbits, n=12/group,
plus an OVX arm with an E2 positive control. Rabbits chosen because fusion *"normally occur[s] at the time
of sexual maturation, just like in [humans]."* Fusion scored blind as ≥50% of cartilage replaced by bone
bridges.

**Fusion, OVX rabbits — percentage with plates still unfused:**

| plate | timepoint | control | RES | E2 |
|---|---|---|---|---|
| distal tibia | 4 wk | 6% (1/17) | **57% (8/14)** * | 0% |
| distal femur | 7 wk | 90% | **100%** | 60% |
| distal femur | 10 wk | 10% | **33%** | — |
| proximal tibia | 7 wk | 100% | 100% | 100% |
| proximal tibia | 10 wk | 50% | **100%** * | — |

**Fusion was delayed at all three sites, including the proximal tibia — the last plate to fuse and
therefore the one that sets final length.**

**Distal femur morphometry at 7 weeks (Table 1), read against my identity:**

| identity term | measurement | control | RES | E2 |
|---|---|---|---|---|
| **n** — resting pool | resting-zone area (mm²) | 0.11 ± 0.02 | **0.26 ± 0.05** ** | 0.08 ± 0.02 |
| **λ** — division rate | BrdU incorporation | — | **significantly lower** * | trend lower |
| — | proliferative cells/column | 5.2 ± 0.9 | 4.5 ± 0.6 (ns) | 3.2 ± 1.3 |
| **A** — amplification | hypertrophic cells/column | 3.3 ± 0.1 | **5.0 ± 0.1** * | 2.6 ± 1.1 |
| **h_term** — terminal height | terminal cell size (µm) | 10.5 ± 0.6 | **12.4 ± 0.6** * | 10.0 ± 0.6 |
| — | hypertrophic zone height (µm) | 71 ± 5 | **95 ± 5** ** | 51 ± 14 |
| — | whole plate height (µm) | 133 ± 40 | **284 ± 19** ** | 72 ± 31 |
| — | apoptosis (%) | 0.2 ± 0.1 | 0.2 ± 0.1 | **1.1 ± 0.4** * |
| — | serum IGF-I (ng/mL) | 191 ± 11 | 203 ± 23 (ns) | 208 ± 16 |

**Every term moved the way the identity wants, simultaneously, in a fusing species, with no apoptosis —
and E2 moved every one of them the opposite way.** That is the cleanest mirror-image pair in the branch.

**And the length gain was 1.5–2%.**

- ovary-intact tibia: 111.6 ± 0.6 vs 109.5 ± 0.6 mm (**+1.9%**, p<0.05)
- ovary-intact femur: 103 ± 0.8 vs 101.5 ± 0.6 mm (+1.5%, **p=0.1**)
- OVX femur: 102.4 ± 0.6 vs 100.9 ± 0.4 mm (**+1.5%**, p<0.05)
- OVX tibia: 107.5 ± 0.5 vs 107.1 ± 0.6 mm (**ns**)

Plate height doubled. Resting-zone area more than doubled. `A` rose 52%, `h_term` rose 18%. Length rose 2%.

**Something in the identity is missing, and §4 names it.**

Two further details worth keeping. **Serum IGF-I was identical across all groups at both 7 and 10 weeks**,
and RES worked in cultured fetal rat metatarsals with no blood supply — so the effect is **local to the
plate and orthogonal to the systemic GH/IGF-1 axis.** That orthogonality is what makes it stackable with a
rate arm rather than redundant with one. And the ex-vivo dose-response is **biphasic**: +0.3 µM stimulated
(125.3 ± 2.1% vs 118.7 ± 1.9% length increase at 19 days, p<0.05), while **10 µM and 50 µM suppressed
growth.** Any RES-like agent has a narrow window on the correct side of a hormetic curve.

---

## 3. Karimian's mechanism is vascular, and that is a fourth arm

RES suppressed the angiogenic machinery at the chondro-osseous junction:

| marker | control | RES | E2 |
|---|---|---|---|
| VEGF⁺ cells/mm² | 626 ± 50 | **265 ± 54** (−58%, p<0.01) | 632 ± 153 (ns) |
| laminin⁺ cells/mm², plate | 27.4 ± 1.04 | **17.7 ± 0.6** (−35%, p<0.001) | **44.4 ± 0.8** (+62%, p<0.001) |
| laminin⁺ cells/mm², junction | 515 ± 40 | **368 ± 39** (−29%, p<0.05) | 458 ± 57 (ns) |
| osteoclasts (TRAP⁺/plate) | 22.4 ± 3.2 | 15.2 ± 4.9 (ns) | **6 ± 1.6** (p<0.01) |

**E2 raised laminin 62%.** So part of what oestrogen does at closure is recruit the vasculature that
executes it. Fusion is not only a chondrocyte-intrinsic program; it has an executioner arriving from
outside the plate, and that executioner has its own pharmacology.

**Gerber HP, Vu TH, Ryan AM, Kowalski J, Werb Z, Ferrara N. Nat Med 1999;5:623–628.** Systemic
Flt-(1-3)-IgG — a soluble VEGF receptor chimera — given to **24-day-old mice**: blood-vessel invasion
almost completely suppressed, **hypertrophic zone expanded**, chondroclast recruitment and terminal
chondrocyte resorption decreased, trabecular bone formation impaired. **On cessation: capillary invasion
resumed, bone growth was restored, hypertrophic cartilage was resorbed and growth-plate architecture
normalised.**

Read that last sentence carefully, because it cuts both ways.

- **For "never close":** a systemic protein stops the executioner in a mammal, and the plate survives it
  intact — full architectural restoration on withdrawal. This is the only intervention in the branch that
  demonstrably **pauses** the terminal step and is then **released** with the plate still functional.
  Aflibercept is the marketed descendant of exactly this molecule class.
- **For "fast":** *"restoration of bone growth"* on cessation means growth was **impaired during
  treatment.** VEGF blockade is a pure banking agent. It buys τ and costs rate.

**And it reaches humans already.** **Voss SD et al., Pediatr Blood Cancer 2015 (COG Phase I Consortium):**
5 of 53 paediatric patients (**9.4%**) on VEGF/VEGFR blockade (pazopanib n=4, sunitinib n=1) had growth-plate
abnormalities — **four with plate widening on two or more successive radiographs, one with progressive
widening plus physeal cartilage hypertrophy confirmed on MRI.** Sunitinib produces **reversible** physeal
dysplasia in rats and monkeys (Patyna 2008); bevacizumab produces plate thickening in monkeys.

**The human growth plate widens under systemic VEGF blockade. That is not an inference from a mouse; it is
a radiographic finding in children, reported as a toxicity.**

The ceiling on it is mechanical, not biological. **Hall AP, Mitchard T, Rolf MG, Stewart J, Duffy P,
Toxicol Pathol 2016** — off-target antiangiogenic treatment in **juvenile rabbits** produced femoral-head
growth-plate dysplasia **and fracture.** A widened plate is a weaker plate. This is the same envelope I
raised in F-R048 around SCFE, arriving from an entirely independent direction, and it is a genuine physical
limit on how far the numerator can be pushed — nothing to do with risk tolerance, everything to do with
whether the tissue holds.

---

## 4. Cooper 2013 — the missing variable is τ, and the jerboa beats it

**Cooper KL, Oh S, Sung Y, Dasari RR, Kirschner MW, Tabin CJ. Nature 2013;495:375–378 (PMC3606657).**
Quantitative phase microscopy on dissociated live chondrocytes, dry mass and volume measured per cell.

**Hypertrophic enlargement is three distinct phases, not one:**

| phase | volume | mechanism | dry mass density |
|---|---|---|---|
| 1 | ~600 → 2,000 fl (3×) | true hypertrophy — proportionate mass and fluid | 0.183 pg/fl held |
| 2 | 2,000 → 8,000 fl (4×) | **swelling** — fluid uptake outruns mass production | diluted to **0.07 pg/fl** |
| 3 | 8,000 → 14,000 fl (2×) | proportionate mass and fluid **at the new low density** | 0.07 pg/fl held |

Tomographic phase microscopy independently confirmed the largest cells reduce dry-mass density by ~60%.
Phase 2 is a real, regulated swelling and not an artefact of hypotonic medium — repeating the measurement
in 424 mOsm medium reproduced all three phases.

**Phase 3 is the variable one, and it is where species and elements differ:**

| growth plate | max volume | trajectory |
|---|---|---|
| mouse proximal radius (slow) | ~5,000 fl | truncates Phase 2, **eliminates Phase 3** |
| mouse metatarsal (intermediate) | ~8,000 fl | completes 1 and 2, truncates Phase 3 |
| mouse proximal tibia (fast) | ~14,000 fl | all three phases |
| **jerboa metatarsal** | **~23,000 fl** | all three, **Phase 3 extended** |

The jerboa metatarsal enlarges **~40-fold from its starting volume**, exceeding the tibia of either
species, with individual hypertrophic cell height **+58%** vs the homologous mouse plate (p<10⁻⁵). The
jerboa *tibia* is only slightly larger than the mouse tibia and the jerboa *metacarpals* are
indistinguishable from mouse — so this is element-specific and locally controlled, not a systemic body
plan.

**Phase 3 is IGF-1-dependent, and locally so.** *Igf1^fl/fl; HoxB6-Cre* limb-conditional deletion:
terminal cell height **−34% in tibia, −23% in metatarsal**; mutant cells complete Phases 1 and 2 to
~7,000 fl and then **fail to progress to Phase 3**, never doubling again. Systemic IGF-1 is not what is
being tested here — limb-local Igf1 is.

**And now the constraint that explains everything in §2.** Citing Farnum's neonatal bat and mouse work,
and confirming it directly by BrdU pulse-chase:

> *"the entire hypertrophic zone of each growth plate turns over once in about 24 hours regardless of the
> maximum volume attained by individual chondrocytes, the number of hypertrophic chondrocytes, or rate of
> growth plate elongation."*

Cooper's own measurement: cells **more than triple their height within ~12 hours** of the last mitosis,
then **sit at terminal size for a further ~12 hours** before turnover at the chondro-osseous junction.

**Therefore:**

```
dL/dt  =  N_h · h_term / τ            N_h = hypertrophic cells per column
                                      τ   = hypertrophic zone turnover time (~24 h)
L∞     =  ∫ dL/dt  until (b − a) runs out
```

**This is the variable my identity was missing, and it dissolves the paradox in §2.**

- **Resveratrol** raised `N_h` 52% and `h_term` 18% — numerator up ~1.79× — and delivered +2% length.
  It must therefore have raised **τ** by very nearly the same factor. Cells sitting longer in a taller
  plate is precisely what "delayed senescence" looks like histologically. RES bought τ and spent the
  numerator paying for it.
- **VEGF blockade** raises `N_h` (expanded hypertrophic zone) by *blocking turnover at the junction* —
  it raises τ **directly and by definition**, and Gerber measured the consequence: growth impaired.
- **Dexamethasone** (Gafni: fusion 88% control vs 14% treated at 16 weeks) suppresses λ and banks
  capacity — the same trade in a different currency.

> ### Every banking agent found so far raises the numerator by lengthening τ. That is not a coincidence and it is not bad luck. It is the *same act*: cells linger, so the zone is taller and the clock is slower, and the ratio barely moves. This is the structural reason "fast" and "unlimited" have refused to combine for fourteen rounds.

**The jerboa metatarsal is the existence proof that they can be separated.** It reaches 23,000 fl — 4.6×
the volume of the mouse radius and 1.6× the mouse tibia — and it is a *fast* plate, not a slow one. It
raises `h_term` inside an unchanged 24-hour envelope by **extending Phase 3**, the phase that adds mass at
the already-diluted density.

And Cooper's timing measurement says there is room to do it: **the cell reaches terminal size at ~12 h and
then waits ~12 h.** Half of the hypertrophic lifetime is spent at a size the cell already attained. The
schedule is not saturated. That slack is the target.

> **The correct h_term strategy, stated precisely for the first time in this branch:** do not slow the
> junction and do not slow the clock. **Extend Phase 3 into the second twelve hours** — the interval the
> cell currently spends idle at terminal size — via local IGF-1 signalling in the hypertrophic zone. This
> raises `N_h · h_term` with `τ` fixed, which is the only combination that raises `dL/dt` without spending
> `(b − a)`. It is the one manoeuvre in the branch that is *fast* and *not* a withdrawal from the account.

---

## 5. The h_term accelerator gap, stated honestly

Phase 2 is osmotic. Three transporters have been tested in the mammalian plate, and every one of them was
tested by **taking it away**:

| transporter | probe | result |
|---|---|---|
| **NKCC1** | bumetanide, rat metatarsals/metacarpals P7, 24 h | **~35% reduction in bone growth**, dose-dependent, via reduced hypertrophic-zone height. NKCC1 mRNA rises proliferative → hypertrophic; localisation moves from intracellular to plasma membrane on hypertrophy. (Bush PG et al., JBMR 2010;25:1594–1603) |
| **NHE1** | EIPA 444 µM, rat P10, 48 h ex vivo | metatarsal growth **18.1% → 5.5%**; tibial **15.6% → 4.6%**; via reduced HCZ length, total plate length unchanged |
| **AE2** | DIDS 250 µM, same model | metatarsal **16.3% → 7.4%**; tibial **16.1% → 7.5%** |

(NHE1/AE2: Abubakar AA et al., *Roles of NHE1 and AE2 across Chondrocytes Plasma Membrane during
Longitudinal Bone Growth*, PMC9321928.)

That paper's discussion speculates that *"increasing the localization of NHE1 and AE2 either individually
or in combination may promote hypertrophy"* — **but every citation behind that sentence is a non-chondrocyte
cell type** (kidney, hepatocellular carcinoma, ventricular myocyte, gastric cancer, airway epithelium). I
read the reference list rather than the sentence. It is a hypothesis, not a result.

> **The honest state of the h_term arm:** NKCC1, NHE1 and AE2 are each **necessary** for hypertrophic volume
> and each abolishes 35–70% of longitudinal growth when blocked. **Not one has been shown sufficient to
> increase it.** There is no published pharmacological agent that raises terminal chondrocyte volume in a
> mammalian growth plate. Local IGF-1 → Phase 3 is the only positive-direction mechanism identified anywhere
> in this literature, and it comes from a conditional knockout read backwards.

---

## 6. Link 11, restated with what is now known

**The question:** does removing oestrogen *prevent* proliferative arrest or merely *postpone* it?

**What has hardened against the optimistic answer:** Weise's vehicle rabbits (E2 < 5 pg/mL) fused the
distal tibia at 2–6 weeks. Karimian's OVX controls fused the distal tibia in 94% of animals (16/17) by
**four weeks** post-OVX, and 50% of proximal tibiae by ten weeks. **Ovariectomy does not prevent fusion in
the rabbit. It is not close to preventing it.** Two independent laboratories, same species, same direction.

**What is new, and is the first affirmative crack in it:** the residual, oestrogen-independent fusion in
the OVX rabbit was **delayed at all three plates by an agent with no anti-oestrogen mechanism**, acting
locally, without changing serum IGF-I, and by suppressing the vascular executioner. Whatever drives fusion
after the ovaries are gone, **it is druggable, and not through the oestrogen axis.**

That does not resolve link 11 — RES delayed, it did not prevent, and the proximal tibia was still only
followed to ten weeks. But it converts link 11 from *"is there anything at all to grip?"* to *"how far can
the vascular and Hedgehog grips be pushed, and do they compound?"*

The residual fusion driver in the OVX rabbit still has an unexcluded oestrogen explanation, and F-R049
supplies it: the plate makes its own. Ovariectomy removes the ovary, not intracrine CYP19A1, not STS, and
not adrenal DHEAS. **The CYP19A1⁻/⁻ rabbit (F-R056 §1) remains the only experiment that separates these
two readings, and those animals are alive.**

---

## 7. Where the stack stands

Four arms are now distinguishable, and they act on different terms:

| arm | term | best evidence | direction |
|---|---|---|---|
| **pool** | `n`, `(b−a)` | FoxA2⁺ serial transplant; dexamethasone banking (Gafni) | banks — raises τ |
| **oestrogen** | `w(E₂)` | Weise, Nilsson, aromatase-deficiency case reports | removes a write-off, does not stop the count |
| **Hedgehog (ligand-level only)** | `A` | Haraguchi *Hhip1* cKO, +4.5% at 53 wk | amplitude, slope unchanged |
| **vascular** | `τ` | Gerber Flt-(1-3)-IgG; Voss human paediatric widening; RES | banks — raises τ, reversible |

**Three of the four buy τ. Only Hedgehog-at-the-ligand raises the numerator, and it does so weakly (+43%
plate area → +4.5% length over a year).**

**The stack cannot be built yet, and I am not going to build it.** A stack of four τ-lengtheners is a stack
that never closes and barely grows, which fails the brief exactly as badly as one that grows fast and
closes. The missing component is a numerator-raiser that leaves τ alone, and Cooper says where it lives:
**Phase 3, locally IGF-1-driven, with twelve hours of unused schedule to expand into.**

---

## 8. What I need next

Ranked by how much each would move the model, not by how hard it is to get.

1. **Farnum CE, Wilsman NJ. "The domain of hypertrophic chondrocytes in growth plates growing at different
   rates." Calcif Tissue Int 1997;61(4):323–328. PMID 9351885.** Cooper's reference 7 and **the single most
   important outstanding paper in the branch.** Europe PMC: closed, no PMC copy, not OA. This is the τ
   measurement. **Is τ ≈ 24 h a constant across species, ages and rates, or does it simply happen not to
   co-vary in that dataset?** The entire `dL/dt = N_h · h_term / τ` framing stands or falls on it, and so
   does §4's claim that resveratrol and VEGF blockade bought τ.
2. **Breur GJ, VanEnkevort BA, Farnum CE, Wilsman NJ. "Linear relationship between the volume of hypertrophic
   chondrocytes and the rate of longitudinal bone growth in growth plates." J Orthop Res 1991;9(3):348–359.
   PMID 2010838.** Closed, not OA. If the relationship really is **linear**, this is the coefficient that
   converts a volume gain into a length gain — the number the identity has been missing since F-R043. It
   would tell me directly what the jerboa's 23,000 fl is worth in centimetres.
3. **Kuhn JL, DeLacey JH, Leenellett EE. "Relationship between bone growth rate and hypertrophic chondrocyte
   volume in New Zealand White rabbits of varying ages." J Orthop Res 1996;14(5):706–711.** Closed. Same
   relationship **in the rabbit** — the species that fuses, that Weise, Gafni, Nilsson and Karimian all used,
   and **across ages**, which means it may also carry how `h_term` changes as the plate senesces.
4. **Wilsman NJ, Farnum CE, Leiferman EM, Fry M, Barreto C. "Differential growth by growth plates as a
   function of multiple parameters of chondrocytic kinetics." J Orthop Res 1996;14(6):927–936. PMID
   8982136.** Wiley, closed. I have the abstract-level numbers (enlargement 59%→44%, matrix 32%→49%) and need
   the full eight-variable decomposition and the equations.
5. **Cooper 2013 Supplementary Figures S3 and S5** — `NIHMS440348-supplement-1.docx` and `-2.pdf` at
   PMC3606657. **These are not paywalled**; PMC serves them behind a proof-of-work bot challenge that I will
   not solve, and they open normally in a browser. S3 has **total cell number per zone in the jerboa
   metatarsal**, which decides whether the jerboa raises `h_term` alone or `N_h` with it. S5 is the BrdU
   pulse-chase behind the 12 h + 12 h schedule.
6. **Any measurement of τ under an intervention.** Nobody appears to have asked whether resveratrol,
   dexamethasone, oestrogen or VEGF blockade changes hypertrophic-zone transit time. If such a number exists
   anywhere it converts §4's central claim from an inference into a measurement. I could not find one.
7. **Growth-plate histology or radiographs from the CYP19A1⁻/⁻ rabbits** (standing request, F-R056 §1).
8. **Voss SD et al., Pediatr Blood Cancer 2015;62(1):45–51** in full — the **magnitude** of physeal widening
   in the children, the agent-by-agent breakdown, and whether any patient's height velocity was recorded.

---

*This round corrects F-R055's reading of Haraguchi, declines a misreading of Wilsman that Karimian's own
discussion invites, and adds τ as a term the identity did not have. The oestrogen side of the stack remains
unbuilt, per the standing instruction, and now has a second reason to stay unbuilt: until something raises
the numerator with τ held fixed, there is nothing for it to protect.*
