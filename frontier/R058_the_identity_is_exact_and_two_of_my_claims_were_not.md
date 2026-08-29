# F-R058 — The identity closes to 0.1%, τ is not a constant, and the jerboa is not what I said it was

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** All five requested items received and read in full — Breur 1991, Breur 1997, Kuhn 1996,
Wilsman 1996, and both Cooper 2013 supplements. Every regression below was **recomputed from the published
tables rather than quoted.**

**The result:** `dL/dt = flux × terminal chondrocytic domain volume` is not a model. It is an identity, it
was derived independently in 1996, and it closes on Wilsman's own data to **8.42× against a measured 8.43×**.
**Two claims from F-R057 do not survive contact with these papers, and one thing I dropped entirely comes
back.**

---

## 0. The thing I dropped: the ALT argument for GH

**GH is not in this stack as a rate driver. It is in the stack as AKT support for erdafitinib.** FGFR3
blockade alone is **apoptotic** in growth-plate chondrocytes; IGF-1 signalling through sustained AKT
rescues it. That is why the GH line exists at all, and `STACK_STATE.md` §3.2 described its job as
`h_term` delivery and then complained it was in the wrong compartment. **Wrong job description. The
compartment complaint was answering a question nobody asked.**

**And the second half, which is the strongest single result in the branch** (F-R029 §3):

> **"When GH hypersecretion is accompanied by gonadotropin deficiency, accelerated linear growth may
> persist for DECADES."** — the standard description of pituitary gigantism

**That is all three terms at once — fast, unlimited, never-closing — in a documented, repeated human
phenotype, and it runs through the systemic GH axis.** It is the only existence proof the goal has. Any
statement that writes off the systemic axis has to answer it, and F-R057 and `STACK_STATE` did not.

**The reconciliation with the pool-depletion result is a sign flip, stated by the authors themselves**
(F-R032):

> *"it is plausible that GH augments both stem cell number and activity **under physiological conditions**
> but causes stem cell depletion **under pharmacological exposure**."*

**So the GH dose question is not "which number." It is "which side of the sign flip."** 2 IU/day
(≈0.067 mg/kg/wk at 70 kg) sits in the physiological range; 0.35 mg/kg/wk is roughly 5× higher and sits in
the pharmacological range where Chu's depletion applies. **The low dose is not a compromise — it is the
side of the flip where GH adds to the pool instead of spending it, and it still supplies the AKT tone
erdafitinib needs.** That is a much better answer than the one I left in the ledger.

---

## 1. The identity, derived — not fitted

**Wilsman NJ, Farnum CE, Leiferman EM, Fry M, Barreto C. J Orthop Res 1996;14(6):927–936.** Two independent
equations, every parameter measured separately.

**Production:** `N_new = (Vv_pz / v(c)_pz) · (π·0.5²·H_pz) · GF · (24 / T_cycle)`
**Loss:** `N_lost = (Vv_thz / v(c)_thz) · (π·0.5²) · elongation`

At steady state `N_new = N_lost`, and solving for elongation:

```
dL/dt  =  N_lost/day  ×  v(d)_terminal          v(d) = v(c) + v(m)  =  v(c) / Vv
          └─ flux ─┘     └── domain volume ──┘
```

**I tested it on Wilsman's Table 2/3/4, fastest plate against slowest:**

| | proximal tibia | proximal radius | ratio |
|---|---|---|---|
| elongation | 396 µm/day | 47 µm/day | **8.43×** |
| N_lost / day | 14,200 | 4,500 | **3.16×** |
| terminal domain volume `v(c)/Vv` | 21,894 µm³ | 8,204 µm³ | **2.67×** |
| **flux × domain** | | | **8.42×** |

**8.42 against 8.43. The identity is exact.**

And **Breur GJ, Lapierre MD, Kazmierczak K, Stechuchak KM, McCabe GP. Calcif Tissue Int 1997;61:418–425**
confirms it empirically from the other direction — his best model, `R² = 0.992`, contains exactly two
variables plus their interaction: **hypertrophic cell volume and the rate of cell loss/cell proliferation.**
I refit it from his Table 1 and reproduced `R² = 0.997`.

> ### The single most important consequence: flux contributes 3.16× and terminal volume contributes 2.67× across the rat's natural range, and **they multiply.** Both extreme positions in this branch are dead. "λ is worthless, never buy speed with it" (F-R044) is wrong — flux is the *larger* of the two factors. "`h_term` is the free multiplier" (F-R043 onward) is overstated — it is a free multiplier, of comparable size, and it does not act alone.

---

## 2. Correction 1 — τ is not a constant, and F-R057 built its spine on the assumption that it is

F-R057 took Cooper's inherited claim — *"the entire hypertrophic zone turns over once in about 24 hours
regardless of… rate of growth plate elongation"* — and made `dL/dt = N_h · h_term / τ` the organising
identity of the round. **Wilsman's Table 2 lets me test it, and it fails.**

| plate | elongation | plate height | **whole-plate transit** |
|---|---|---|---|
| proximal tibial | 396 µm/day | 619 µm | **1.56 d** |
| distal radial | 269 µm/day | 515 µm | **1.91 d** |
| distal tibial | 138 µm/day | 326 µm | **2.36 d** |
| proximal radial | 47 µm/day | 181 µm | **3.85 d** |

**A 2.46× range, varying inversely with growth rate.** Transit time is not conserved; slow plates hold
cells longer.

**What survives.** Cooper's claim is narrower than the use I made of it: it is about the **hypertrophic zone
specifically**, in **bat and mouse forelimb**, cited to reference 7 — and Cooper did not independently
re-measure it as a constant across rates. Cooper's own supplementary BrdU series runs to **18 h, 30 h and
42 h**, not to 24. So the τ framing is not refuted for the hypertrophic zone; **it is unverified, and I
presented it as measured.**

**The correct form is the one in §1, which needs no τ assumption at all:** flux × domain volume. Flux
already contains transit implicitly and is directly measurable.

---

## 3. Correction 2 — the jerboa is not a pure `h_term` demonstration

F-R057 §4 read the jerboa metatarsal as the existence proof for raising cell volume with the clock held
fixed. **Cooper Supplementary Figure S3, which I asked for and now have, says otherwise:**

> *"The jerboa distal metatarsal growth plate is proportionately approximately **three-times taller in each
> zone** compared to the mouse metatarsal."*

**Each zone — resting, proliferating and hypertrophic.** The jerboa is a coordinated scale-up of the entire
plate, not a selective volume trick. It raises `n`, flux and volume together, which is exactly what §1 says
is required and **not** what I claimed it demonstrated.

**It still works quantitatively.** Cooper Fig. S2 gives the mouse rates directly — **proximal tibia 158 ±
24.1 µm/day, metatarsal 102 ± 14.5 µm/day at P5.** Two points against Cooper's volumes (14,000 fl and
8,000 fl) give a mouse slope of ≈**0.0093 µm/day per fl**; at the jerboa's 23,000 fl that predicts
≈**241 µm/day**, i.e. **2.4× the mouse metatarsal** — against the ~2.5× relative proportion the paper
reports. *(A line through two points is an estimate, not a fit. I am labelling it as such.)*

**And the coefficient does not transfer between species.** Breur's rat slope over-predicts the mouse badly
(256 µm/day predicted vs 158 measured for the proximal tibia). The measured slopes:

| species | equation | fit |
|---|---|---|
| rat | `GR = −40.71 + 0.0212·v(c)` | r = 0.98 |
| pig | `GR = −40.68 + 0.0338·v(c)` | r = 0.83 |
| **rabbit, 5 wk** | `GR = −197 + 0.061·v(c)` | r² = 0.81 |
| **rabbit, 8 wk** | `GR = −47 + 0.034·v(c)` | r² = 0.91 |
| **rabbit, 12 wk** | `GR = −57 + 0.030·v(c)` | r² = 0.87 |
| mouse (my 2-point estimate) | `GR ≈ 27 + 0.0093·v(c)` | — |

**Kuhn J L, DeLacey JH, Leenellett EE. J Orthop Res 1996;14(5):706–711** adds the constraint that matters
most: **the 5-week rabbit slope is almost exactly twice the 8- and 12-week slope** (Bonferroni p < 0.01),
and **no linear relationship exists at all at 2 and 3 weeks.**

> **A second senescence mechanism, independent of cell number and cell size: the plate's conversion
> efficiency per unit cell volume degrades with age.** Restoring `v(c)` in an old plate buys roughly half
> what it buys in a young one. Nothing in the branch had this.

---

## 4. What Wilsman actually decomposed — and where F-R057 was right for the wrong reason

The published numbers:

| plate | cell duplication | matrix production | hypertrophic enlargement |
|---|---|---|---|
| proximal tibia, 396 µm/day | **9%** | 32% | **59%** |
| proximal radius, 47 µm/day | **7%** | 49% | **44%** |

**So Karimian's "less than 10% of bone growth linked to cell proliferation" is numerically correct.**
F-R057 said it was a misreading of what Wilsman measured and described it as a decomposition of *column
height*. **That description was wrong** — it decomposes the **daily turned-over volume by source.**

**The substantive objection stands, and is now sharper.** A source decomposition is not a sensitivity
coefficient. `N_lost` multiplies through **all three** components — halve the flux and the cellular, matrix
and enlargement contributions all halve together. §1 measures the actual sensitivity: **flux 3.16× against
volume 2.67×.** Karimian used a 9% source share to argue that suppressing proliferation was nearly free.
It is not.

**And the neglected third of the answer:** **matrix production is 32–49% of daily elongation** — larger than
cellular enlargement in the slow plate — and **this branch has never once addressed it.** Breur adds that
matrix volume per cell is essentially **age-invariant** (proximal tibia 8,950 µm³ at D21 vs 8,880 µm³ at
D35) and *"may be predetermined and may remain constant during the period of active growth."* A third of
growth, apparently under separate control, entirely unexamined here.

---

## 5. The hard ceiling I did not know about

**Wilsman Table 2 — growth fraction, measured by continuous BrdU to plateau:**

| plate | growth fraction |
|---|---|
| proximal tibial | **0.99** |
| distal radial | **0.99** |
| distal tibial | **0.98** |
| proximal radial | **0.89** |

> **Essentially every proliferative-zone chondrocyte is already in cycle.** There is no quiescent
> proliferative reserve to recruit. Any intervention whose mechanism is "wake up resting proliferative
> cells" is capped at **1–11%** before it starts. Flux can only be raised through **cell-cycle time**
> (which spans 30.9 → 76.3 h, a 2.47× range) or through **proliferative-zone height** (43 → 137 µm,
> 3.19×) — and those two account for essentially the whole 8.4× natural range.

---

## 6. Senescence is carried by cell volume, not by flux

I computed this from Breur's Table 1, comparing each plate against itself at 21 and 35 days:

| plate | elongation | terminal cell volume | **flux** | matrix/cell |
|---|---|---|---|---|
| proximal radius | −12.5% | −26.7% | **+7.4%** | −8.2% |
| distal radius | −29.2% | −18.7% | −16.6% | −2.2% |
| proximal tibia | −26.9% | −22.9% | −12.1% | −0.8% |
| distal tibia | −39.5% | −41.3% | −7.7% | −20.7% |

**Growth tracks volume, not flux. In the proximal radius flux actually rose 7.4% while growth fell 12.5%.**
Breur states it outright: there was *"no statistically significant difference between the standardized rate
of cell loss of identical growth plates collected at 21 days and at 35 days."*

**Kuhn supplies the same dissociation inside a single bone, which is stronger because systemic hormone
exposure is identical:** at 12 weeks the rabbit **proximal radius is "almost fused" at v(c) = 2,590 µm³**,
while the **distal radius of the same animal is still growing at 290 µm/day with v(c) = 11,770 µm³** — only
35% below its own 2-week value. And the two plates that showed **no significant volume decline with age**
(proximal tibia, distal radius) are precisely the two still growing at 12 weeks.

> ### Maintenance of terminal hypertrophic cell volume is the signature of a plate that stays open, and its collapse is the signature of one that closes — locally, within one bone, under one hormonal environment. **For the "never close" objective this is the most directly actionable finding in the branch, and nothing in the stack protects `v(c)`.**

---

## 7. Where this leaves the stack

**The identity, in its final measured form:**

```
dL/dt  =  flux  ×  v(d)_terminal        flux = N_lost/day, gated by T_cycle and PZ height (GF is saturated)
                                        v(d) = v(c) + v(m)   — cell volume plus matrix per cell
```

| lever | natural range | in the stack? |
|---|---|---|
| cell-cycle time | 2.47× | **erdafitinib** — FGFR3 blockade acts here |
| proliferative-zone height | 3.19× | nothing |
| growth fraction | **saturated at 0.89–0.99** | closed — no headroom |
| terminal cell volume `v(c)` | 3.63× | **nothing** |
| matrix per cell `v(m)` | 32–49% of growth | **nothing, ever** |
| conversion efficiency (age) | ~2× loss, 5→8 wk rabbit | **nothing** |

**GH 2 IU** supports erdafitinib's AKT requirement and sits on the physiological side of the stem-pool sign
flip. **Abaloparatide 80 µg** holds the mechanical envelope. **Neither is a term in the identity** — they
are enablers, and that is the correct reading of both.

**So the stack currently moves one of six levers.** F-R057 concluded the missing piece was "a
numerator-raiser with τ held fixed." **That framing is retracted** — there is no τ to hold fixed. The
correct statement is simpler and worse: **the stack raises flux through one channel and does nothing at all
to terminal domain volume, which is 2.67× of the natural range and carries senescence and closure both.**

**The oestrogen side stays unbuilt** — standing instruction, and now a third reason: §6 says what closure
looks like mechanically (volume collapse), and until something defends `v(c)` there is nothing for an
anti-oestrogen arm to preserve.

---

## 8. What I still need

1. **Farnum CE, Wilsman NJ. "The domain of hypertrophic chondrocytes in growth plates growing at different
   rates." Calcif Tissue Int 1997;61(4):323–328. PMID 9351885.** **Still outstanding** — the bundle
   contained **Breur et al., Calcif Tissue Int 1997;61(5):418–425**, a different paper with a nearly
   identical title in the same volume. Breur's paper does not measure transit time. This is the one that
   tests whether hypertrophic-zone τ is conserved, which §2 leaves open.
2. **Cooper 2013 reference 7** — the bat and mouse forelimb study behind the 24-hour claim. Likely
   **Farnum CE, Wilsman NJ, et al.** on neonatal bat forelimb growth plates. I need the primary source
   rather than Cooper's one-sentence summary of it.
3. **Any measurement of terminal hypertrophic chondrocyte volume in a human growth plate.** I have rat, pig,
   rabbit, mouse and jerboa and **no human number at all** — so I cannot place the human plate on any of
   the regressions in §3, and every quantitative claim about human headroom is currently unanchored.
4. **Anything on pharmacological control of matrix volume per chondrocyte** (§4). Breur calls the
   regulators *"largely unknown"* as of 1997; I want to know whether that changed. 32–49% of growth is
   sitting untouched.
5. **Growth-plate histology or radiographs from the CYP19A1⁻/⁻ rabbits** (standing since F-R056).
6. **Voss SD et al., Pediatr Blood Cancer 2015;62(1):45–51** in full (standing since F-R057).

---

*This round retracts F-R057's τ identity and its reading of the jerboa, corrects F-R057's mischaracterisation
of what Wilsman measured, restores the GH argument I dropped, and replaces all of it with an identity that
was derived in 1996, closes to 0.1%, and says both factors must move together.*
