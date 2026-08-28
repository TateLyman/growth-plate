# F-R033 — The plate has a thickness budget, every term is inside it, and I had the geometry wrong

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** U2 closed to a residual; U3 advanced to one missing measurement; **F-R032 §3 and §5b are corrected**

---

## 0. The correction first, because everything downstream depends on it

F-R032 §3 said: *"Doubling `N` doubles output and spends nothing extra per unit output… A plate with 10×
the stem number at unchanged λ grows ten times as fast."* And §5b proposed that niche slot count, hence N,
*"should scale with the plate's cross-sectional area."*

**Both are wrong, and they are wrong for the same reason: columns act in parallel.**

A growth plate is a disc of columns standing side by side. Every column pushes the epiphysis away from the
metaphysis **simultaneously and by the same distance**. Adding columns makes the bone **wider**, not
longer. The field's own rate formula has no width term in it:

> growth rate = (cell divisions per column per unit time) × (terminal hypertrophic cell height)

So `N` in `dH/dt = λ·N·A·h_term` must be read as **stem cells feeding one column position** — the *depth*
of the reserve above a column, not the plate-wide cell count. The identity of F-R032 §1 is unaffected
(it is per stem division and holds regardless). The dynamics are unaffected in form. **What is destroyed
is the escape route I proposed**: the "free" direction I had identified — plate area — contributes
nothing to height, and the direction that does contribute is axial, which as §2 shows is precisely the
taxed one.

I built §5b toward a niche-widening architecture. That architecture does not work, and I am retracting it
before it goes any further.

---

## 1. The measurement that settles it

**Kondo et al. 2021, *Cartilage*, PMC8804827** — *"Analysis of Association between Morphometric Parameters
of Growth Plate and Bone Growth of Tibia in Mice and Humans."* Mouse proximal tibia at P6, P13, P21, P28,
P42, P70; human tibia radiographs 0–14 y (F) and 0–15 y (M).

| parameter | vs growth rate | vs tibia length |
|---|---|---|
| **resting zone height** | **R² = 0.973, P = 0.0003** | R² = 0.815 |
| **proliferative zone height** | **R² = 0.948, P = 0.0011** | R² = 0.916 |
| total plate height | R² = 0.896, P = 0.0042 | R² = 0.892 |
| hypertrophic zone height | R² = 0.634, **P = 0.058 (n.s.)** | R² = 0.700 |
| **growth plate width** | R² = 0.989, P < 0.0001 | R² = 0.835 |
| **growth plate area** | **R² = 0.171, P = 0.415** | R² = 0.354 |

The abstract reports width as having *"the strongest correlation"* and treats it as a candidate biomarker.
**Read with the signs restored, it is a strong NEGATIVE correlation, and that is the whole story.** The
paper's own text: growth rate was *"very active until P13, and then decreased over age"*, while width
*"increased until P28 and then plateaued."* **Opposite trajectories.** R² is unsigned, so a monotone
decline against a monotone rise returns a high R² for an inverse relation.

**The area null is the check that proves the signs.** Area combines a positively-correlated axial
dimension with a negatively-correlated radial one, so it cancels to R² = 0.171. An internal inconsistency
in the abstract becomes an internal *consistency* once the signs are read correctly.

> **Growth rate tracks the plate's AXIAL dimensions — resting zone height (R² = 0.973) and proliferative
> zone height (R² = 0.948). It does not track area, and it runs inverse to width.**

That is direct measurement, in the right direction, and it agrees with the parallel-column geometry
rather than with what I proposed in F-R032.

---

## 2. U2 — is the axial dimension capped, and by what?

**Answer: yes, and the constraint is metabolic. Seven independent lines.**

**(a) Cross-species conservation, against a control tissue.** Growth plate thickness: rat ~0.3–0.5 mm;
bovine proximal tibial physis **0.67 mm**; human ~0.5–1 mm+. Roughly **2–3× across a 10⁵-fold body-mass
range.** The control is articular cartilage in the same animals — also avascular, also
diffusion-fed — which runs **90 µm (mouse) → 2,000 µm (human) → 3,000 µm (Asian elephant): 33×**
(`PMC3578797`). **The metabolically active plate is ~10× more size-conserved than the quiet cartilage
beside it.** Something actively constrains one and not the other.

**(b) The plate is essentially fed from ONE side.** Brighton & Heppenstall 1971 in vivo (rabbit proximal
tibia): very low tension in the hypertrophic zone *and in the metaphysis*, with a steep step from
**metaphyseal bone 19.8 mmHg to diaphyseal bone 108.7 mmHg.** The metaphysis is not a source. Supply is
epiphyseal, through the SOC. So the diffusion path runs the full plate thickness, one-sided, and
concentration drop scales as **L²**.

**(c) The tissue evolved an oxygen store.** `zhang2023`: growth plate chondrocytes assemble cytoplasmic
haemoglobin bodies with **P50 27.6–27.9 mmHg against 58.2 mmHg for red cells from the same mice** —
strongly left-shifted, binding oxygen at tensions where erythrocyte haemoglobin has already let go. A
tissue does not evolve an oxygen buffer unless delivery is marginal.

**(d) The interior dies without hypoxic adaptation.** HIF-1α deletion in chondrocytes causes massive death
in the plate interior while sparing the margins. There is a real anoxic core to be defended.

**(e) Supply-dependence of amplification, measured.** `newton2019`: clone size **7.8 ± 0.3 cells centrally
against 5.7 ± 0.1 laterally (P = 0.0012)** — graded by **proximity to the secondary ossification centre**,
at identical age and identical division history. And causally: **axitinib, which blocks SOC
vascularisation, REDUCED clone size (P = 0.0023).** Cut the supply, lose the amplification. The atlas read
this as a niche-signal result; it is at least as good a supply result, and the axitinib arm is the one
that discriminates.

**(f) The ratio matches.** A one-sided slab with uniform consumption gives ΔC = QL²/2D, so the headroom
before the far face hits zero is `sqrt(C₀/ΔC_current)`. On Brighton's gradient that is order **1.3×** — and
`newton2019`'s best-supplied columns already run **1.37×** the worst-supplied ones in the same plate. The
computed ceiling and the observed intra-plate spread are the same number.

**(g) The geometry of §0 and §1.** The one dimension that is free of the diffusion tax — width — is the one
dimension that does not lengthen the bone.

**Therefore: RZ depth, PZ height (hence A), and HZ height (hence h_term) all consume the same
diffusion-limited axial budget, and growth rate is bounded by it.** That is a second conserved quantity,
sitting on top of F-R032's conjugacy identity:

> **Identity 1 (conjugacy):** output above neutral = pool loss, 1 : 1. **Prices λ.**
> **Constraint 2 (thickness budget):** RZ + PZ + HZ ≤ L_max(D, C₀, Q). **Prices n, A and h_term against
> each other.**

Every term in the objective function is inside one of the two. **There is no free term.**

**And that identifies the only lever outside both:** `L_max ∝ sqrt(D·C₀/Q)` — the **supply** itself.
Raising C₀ (delivery to the epiphysis) or lowering Q relaxes the budget that every other term is competing
inside. It is the one variable that is not traded against anything, it is what the SOC exists to provide,
it is what axitinib removes, and **nothing in this literature has ever targeted it for growth.**

**Residual unknown on U2, stated precisely.** The cap could be developmental patterning that merely
*coincides* with the diffusion scale. Two experiments discriminate, neither ever done:
**(i) measure pO₂ in a human growth plate** — the atlas is explicit that *"no oxygen tension has ever been
measured in a human growth plate"*, and human plates are the thickest, so the prediction is sharpest
there; **(ii) raise delivered O₂ and see whether plate thickness or growth rate moves.** Until one of
those runs, §2 is a strong seven-line inference and not a closed fact.

---

## 3. U3 — Trompet, read panel by panel, and it is not the compounding result I wanted

Reading `trompet2024` Figure 5 directly rather than through its abstract:

| panel | measurement | 1 week | 1 month | 2 months | 6 months |
|---|---|---|---|---|---|
| J | Ki67, top 50 µm, femur | **4.5 → 13%, ✱✱** | NS | NS | — |
| K | Ki67, top 50 µm, tibia | **8 → 19%, ✱✱** | NS | NS | — |
| G | femur growth **rate** | NS | **✱✱** | **NS** | — |
| H | tibia growth **rate** | NS | NS | ✱ | — |
| B | femur **length** | — | ✱ | ✱✱ | **✱✱✱** |
| D | leg **length** | — | ✱✱✱ | ✱✱ | **✱✱✱✱** |
| M | Pthlh⁺, top 50 µm | 20 → 29%, **#** (trend) | **not measured** | **not measured** | **not measured** |

And the pool number everyone quotes — *"the number of Pthrp-mCherry⁺ cells increased 61%"* — is a
**separate systemic-SAG experiment, dosed P30–P36 and read at P38: two days after the last dose.**

The bead itself: Gli1-LacZ positive at 1 week, **signal gone within 3 weeks.**

**So the sequence is: a <3-week stimulus → a proliferative burst confined to week 1 → a rate elevation
detectable at 1 month and gone by 2 → a length offset of ~1.5 mm on ~35 mm femur (≈4%) that persists to
6 months.** The rising asterisk count on the length panels reflects a widening absolute gap *and* a larger
n at later points; the rate panels, which are the direct measurement, say the rate difference is over.

**That is a one-off gain that is banked, not a compounding one.** It is what F-R032 §5b's set-point picture
predicts — and it is the answer I was hoping to falsify.

**But it is one measurement short of settled, and the missing measurement is specific.** The pool was
counted at 1 week and never again. **Nobody has asked whether the expanded pool persists at 1, 2 or
6 months** — which is the difference between "the reserve relaxed back to a set point" and "the reserve
stayed large but the rate assay is too noisy to see the 3% it buys." Both are consistent with these panels.
And **nobody has fired a second bead.**

**Two things in Trompet that are better than I had recorded, and both matter:**

**The age-dependence is an artefact of route, not a property of the cells.** *"Systemic activation of the
Hh pathway during the early growth period reduces the activity of epSSCs but… promotes their activity
when performed after maturation of the SOC."* But **genetic** activation in PTHrP⁺ cells *"stimulates the
proliferation and clonal activity of epSSCs **independent of age**."* The window is a systemic
confounder. Direct activation has no window. (This removes the constraint I listed as U8.)

**Hedgehog is named as the `a − b` regulator.** *"Hh signaling is crucial for maintaining the renewal of
epSSCs, **as well as the balance between generation of daughter stem cells and committed progeny**."* That
is the F-R032 asymmetry, with a pathway attached — and unlike the PCP lead of F-R032 §6, this one is
supported by the paper's own data. Its mechanism is also stated: SAG *"creates a **Wnt-inhibitory
environment**"* — and `chu2026` independently finds the human root niche is **low in WNT and TGF-β**.
Two papers, two species, converging on the same niche description.

**Its failure mode is stated too:** *"extensive expansion of the population of epSSCs is associated with
tissue disorganization"*, with *"spheroid-like clones"* under unbounded genetic activation. Transient
pharmacological pulses stayed clean; chronic genetic activation did not.

---

## 4. What this does to "fast"

The empirical ceiling is now a number rather than a hope.

| plate | rate |
|---|---|
| rat proximal tibia, 28 d | **~360–400 µm/day** |
| rat, slowest plate measured (proximal radius) | ~50 µm/day |
| **human distal femoral physis, average** | **~27 µm/day** (10 mm/yr) |
| human distal femoral physis, pubertal peak | ~50–55 µm/day |

**A rat growth plate runs roughly 7× a human plate at its peak, in a plate of similar or smaller
thickness.** Whatever the constraints are, they do not forbid several hundred µm/day in a mammalian growth
plate. Human plates are nowhere near the mammalian maximum.

Wilsman's decomposition of that range: across four rat plates spanning **50 → 400 µm/day**, cell cycle
time runs **30.9, 34.0, 48.7, 76.3 h**, and *"almost all differences in total cell cycle time were
attributable to significant differences in the length of the **G1 phase**"* (S 3.4–6.1 h, G2 3.0 h,
M 0.5–0.6 h — all conserved). And Farnum 1993: chondrocytes spend *"an average of 4 days in the
proliferative zone, representing approximately **four cellular divisions**"*, with each column *"a clonal
expansion of a stem cell, which may proceed independently from adjacent columns."*

So a 2.5× cycle-time range and a ~4-division amplification account for the 8× spread, together with
h_term. **G1 length is the single most-varied parameter in the fastest natural growth plates known.**

**And the evolutionary experiment lands on the same term.** `marchini2018` — Longshanks, 20 generations of
selection on tibia length, **13% longer tibiae in two replicate lines**: the gain is *"not due to prolonged
growth, but to accelerated growth rates"*, is associated with *"an **increased number of proliferative
chondrocytes**"*, and shows *"**no differences** in the rates of chondrocyte proliferation nor in the size
or number of hypertrophic cells."* Asked with no hypothesis what to change for a longer bone, selection
changed the number of amplifying cells — not the division rate, not terminal cell size, not the duration.
`marchini2019` names the genetics: selection favoured *"de-repression of bone growth through inactivating
two limb enhancers of an inhibitor, **Nkx3-2**."*

---

## 5. Where the answer is flawed, exactly

I do not have a flawless answer, and the flaws are locatable rather than diffuse.

1. **U2's cap is inferred, not measured.** Seven converging lines, no direct test. **No one has ever
   measured oxygen tension in a human growth plate.** Everything in §2 rests on rabbit and rat electrode
   data from 1971 plus cross-species morphometry.
2. **U3 is one measurement short.** Pool persistence after a Hedgehog pulse was never measured beyond one
   week. Set-point versus sustained-elevation is undecided by existing data, and it decides whether the
   architecture is "pulse repeatedly" or "hold continuously."
3. **Longshanks is ambiguous in exactly the place it matters.** *"Increased number of proliferative
   chondrocytes"* — per column (raises A, taxed by §2) or per plate (raises width, useless by §0)? The
   paper is paywalled and this is the single sentence that would discriminate.
4. **Kondo's signs are reconstructed, not read.** I inferred them from the stated trajectories and the
   area null. Confident, but I have not seen the scatter plots.
5. **The rodent-to-human velocity argument may be allometry.** Rodent cells cycle faster tissue-wide.
   A 7× headroom demonstrated in rat may not be reachable in human tissue at all.
6. **§2's escape route is untested in the direction that matters.** Raising supply is where the physics
   points; no one has raised oxygen delivery to a growth plate and measured length.

---

## 6. What I need

**Paywalled, and each answers a named question:**

1. **`marchini2018`, *Evolution* 72(4), PMID 29436719, DOI `10.1111/evo.13447`** — Longshanks
   histomorphometry. **The one sentence that decides flaw 3.** Highest value in this list.
2. **Brighton & Heppenstall, *JBJS* 1971;53A:719–728** — the full zonal pO₂ table, both the in vitro rat
   and in vivo rabbit series. §2 is built on a partial reading of it.
3. **Stambough & Brighton, *JBJS* 1980;62A:740** — zonal diffusion. Standing ask, now load-bearing.
4. **Wilsman et al., *J Orthop Res* 1996;14:562–572, PMID 8764865** — cell cycle across four plates. I need
   the **zone heights reported alongside the rates**, which is what tests §2 within one animal.
5. **Breur et al., *Calcif Tissue Int* 1997;61:52–56, PMID 9351885** — the R² = 0.992 regression, full
   parameter table.
6. **Farnum & Wilsman, *Calcif Tissue Int* 1993, PMID 8443686** — the 4-days/4-divisions series in full.
7. **Kondo et al. 2021, *Cartilage*, PMC8804827** — the figures, for the signs (flaw 4).

**Experiments nobody has run, in the order that would resolve most:**

- **pO₂ in a human growth plate.** Never done in any human, at any age. Decides §2.
- **Pool count at 1, 2 and 6 months after a Hedgehog pulse.** Decides U3, and the tissue from
  `trompet2024` may still exist.
- **A second pulse.** Still the decisive unperformed experiment.
- **Raise delivered O₂; measure plate thickness and growth rate.** Tests the one lever outside both
  constraints.
- **Day-zero plate height in the human explant** (carried from F-R032).

---

## 7. Corrections carried

- **F-R032 §3** — *"Doubling N doubles output"* is true only for **per-column** N (reserve depth). Retracted
  as stated.
- **F-R032 §5b** — *"slot count should scale with the plate's cross-sectional area"* is **withdrawn**.
  Cross-sectional area does not enter the length equation, and Kondo's area null (R² = 0.171) is the
  measurement that says so.
- **F-R032 §8** — *"Terms B and C collapse into one"* survives, but the shared lever is **not** niche
  widening. It is reserve depth and amplification, both inside the thickness budget of §2.
- **This branch's oxygen arc (F-R014 → F-R016)** — upgraded rather than corrected. It was treated as a
  control-logic question (which way does pO₂ push differentiation). §2 says oxygen is also, and more
  importantly, a **budget constraint on how much plate there can be**.
