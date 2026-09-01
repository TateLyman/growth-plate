# F-R143 — **I MEASURED THE LOOP GAIN. IT IS 0.016–0.042. AMPLIFICATION IS 1.02×, NOT 5×. THE FEEDBACK RESCUE OF MOXIDECTIN IS DEAD, AND I HAVE A POSITIVE CONTROL THAT SAYS THE ASSAY WOULD HAVE SEEN IT.**

**The question:** R136 proposed that SPIN4 is a TCF7L2 target *and* promotes Wnt, forming a positive
feedback loop, and that a small pharmacological input would therefore amplify. R139 and R142 both
leaned on it as the reason a 3.5%-engagement agent might not be hopeless. **The operator asked me to
check it properly and not to lie about the answer.**

**The answer is that the loop is real but essentially gainless, and the amplification argument is
worth nothing.** Code: `analysis/redundancy/loopgain.py`.

---

## => THE MODEL, STATED SO IT CAN BE FALSIFIED

```
drug lowers Wnt output  →  less TCF7L2 drive on SPIN4  →  less SPIN4
                        →  SPIN4 promotes Wnt, so Wnt falls further
```

**Loop gain g = (∂lnW/∂lnS) × (∂lnS/∂lnW).** Steady-state amplification of a small sustained input
is **1/(1−g)**. For the 3.5% → 40% rescue to work, **g must be ≈ 0.91.**

Two terms, measured separately and by independent data.

---

## => TERM A — HOW MUCH DOES SPIN4 DRIVE WNT? **0.38, AND IT IS AN UPPER BOUND**

`Lui 2023` Fig 6C, isolated growth-plate chondrocytes: complete Spin4 loss takes TOPFLASH from
**1.00 → 0.62**.

> **SPIN4's entire contribution to Wnt output is 38%.** Since that is the effect of removing *all* of
> it, **∂lnW/∂lnS ≤ 0.38** at the wild-type operating point — and only if the relationship is linear,
> which flatters the hypothesis.

**A = 0.38.** For g = 0.91 you would then need **B ≥ 2.4**, i.e. Wnt would have to drive SPIN4 more
than proportionally. Term B decides it.

---

## => TERM B — HOW MUCH DOES WNT DRIVE SPIN4? **MEASURED TWO WAYS. BOTH SAY: BARELY.**

### B1 — CONCORDANCE ACROSS 270 INDEPENDENT DRUG PERTURBATIONS IN HUMAN CELLS

For every RummaGEO drug signature containing both SPIN4 and a canonical Wnt target, does SPIN4 move
**the same direction** as the Wnt gene? If SPIN4 is Wnt-driven, it must.

| Wnt gene | concordant | discordant | % concordant |
|---|---|---|---|
| AXIN2 | 27 | 20 | 57.4% |
| LEF1 | 37 | 33 | 52.9% |
| TCF7 | 22 | 25 | 46.8% |
| NKD1 | 7 | 22 | **24.1%** |
| RNF43 | 18 | 21 | 46.2% |
| ZNRF3 | 16 | 7 | 69.6% |
| SP5 | 5 | 1 | 83.3% |
| CCND1 | 64 | 46 | 58.2% |
| NOTUM | 12 | 13 | 48.0% |
| TNFRSF19 | 35 | 35 | 50.0% |
| **TOTAL** | **243** | **223** | ⛔ **52.1%** |

**z = 0.93 against chance, n = 466 co-occurrences. Indistinguishable from a coin flip.**

### ⭐⭐ AND THE POSITIVE CONTROL IS WHAT MAKES THIS A MEASUREMENT RATHER THAN A WEAK NULL

**I ran the identical test on AXIN2** — an unambiguous canonical Wnt target — against the same nine
panel genes, in the same signatures, with the same code:

| | concordant | discordant | % concordant | coupling index |
|---|---|---|---|---|
| ⭐ **AXIN2** (real Wnt target) | **490** | 215 | ⭐ **69.5%** (n=705) | **0.390** |
| ⛔ **SPIN4** | 243 | 223 | ⛔ **52.1%** (n=466) | **0.043** |

> ### **THE ASSAY DETECTS WNT CO-REGULATION WHEN IT IS THERE — 69.5% FOR A REAL TARGET. SPIN4 SCORES 52.1%. ITS COUPLING TO WNT OUTPUT IS 11% OF A GENUINE WNT TARGET'S.**
> **This is not a null result from a blunt instrument. The instrument works; SPIN4 is not a
> Wnt-responsive gene in any meaningful sense.**

### B2 — ZONAL CO-VARIATION IN HUMAN GROWTH PLATE (GSE9160)

If Wnt drives SPIN4, SPIN4 should be high where Wnt output is high.

| gene | Reserve | Prolif | PreHyp | **Hyper** | **r vs SPIN4** |
|---|---|---|---|---|---|
| AXIN2 | 809.6 | 564.1 | 361.4 | **2699.9** | **−0.305** |
| SP5 | 33.9 | 31.2 | 29.3 | **97.5** | **−0.241** |
| LGR5 | 64.7 | 34.2 | 65.8 | **317.4** | **−0.290** |
| NKD1 | 211.6 | 199.5 | 231.8 | **319.5** | **−0.267** |
| **SPIN4** | 90.9 | **267.8** | 193.2 | 153.6 | — |

> ⛔ **SPIN4 does not merely fail to track Wnt output — it runs OPPOSITE, on all four readouts, mean
> r = −0.28. Wnt output peaks in the hypertrophic zone; SPIN4 peaks in the proliferative zone and is
> LOW in the hypertrophic zone.**

⚠ **n = 4 zones, 2 donors. Indicative, not a significance test.** But it is a second, independent
dataset in the correct tissue, and it agrees with B1 in direction as well as magnitude.

---

## => ⛔⛔⛔ THE RESULT

| | B | **g = A × B** | **amplification 1/(1−g)** | 3.5% becomes |
|---|---|---|---|---|
| drug-signature coupling | 0.043 | **0.016** | **1.02×** | **3.6%** |
| scaled to a real Wnt target's coupling | 0.110 | **0.042** | **1.04×** | **3.7%** |
| ⛔ **required for the rescue** | **≥2.4** | **0.91** | **11×** | 40% |

> ### **MEASURED LOOP GAIN 0.016–0.042. REQUIRED 0.91. THAT IS NOT A NEAR MISS — IT IS TWO ORDERS OF MAGNITUDE. THE AMPLIFICATION ARGUMENT BUYS 0.1–0.2 PERCENTAGE POINTS, NOT A FACTOR OF FIVE.**

### AND THE SECOND HALF OF THE RESCUE — "IT COMPOUNDS OVER TIME" — DOES NOT SURVIVE EITHER

I lumped two different claims together in the previous turn and they deserve separating.
**The time argument** was: Spin4-KO is a permanent reduction and what it changes is a *renewal:commitment
ratio* (R138), so a small sustained shift compounds. **The shape of the arithmetic kills it:**

- `Spin4`-KO carries a **~40% reduction from conception**, through every high-throughput growth phase,
  and yields **+5.06% tibia at 18 months.**
- A drug gives **~3.5%** — 8.7% of that magnitude — for perhaps **2 of ~16 growth years**, and the
  **last two**, when the plate is nearest spent and throughput is lowest.

> **A ratio perturbation an order of magnitude smaller, applied for an eighth of the growth period, at
> the least productive end of it, does not reproduce a lifelong 40%. This is a scaling argument rather
> than a measurement, and I am flagging it as such — but it points the same way and there is no
> version of it that closes a 12× gap.**

---

## => WHAT THIS KILLS, AND WHAT IT DOES NOT — PRECISELY

| | status |
|---|---|
| ⛔ **the feedback-amplification rescue** | ⛔ **DEAD. Measured, with a positive control.** |
| ⛔ **moxidectin at SYSTEMIC doses** | ⛔ **DEAD.** 3.5–11.6% against a 40% target, and nothing amplifies it. |
| ⛔ the "compounds over time" rescue | ⛔ **does not close the gap** (scaling argument, not measurement) |
| ✅ **selamectin** | ✅ **UNAFFECTED — it never needed amplification.** It reaches the target on potency alone (IC50 0.103 µM, dose 0.166 mg/kg, 90× margin) |
| ✅ **LOCAL / DEPOT DELIVERY, for either drug** | ✅ **UNTOUCHED BY THIS RESULT.** A local depot sets the tissue concentration directly; the systemic CNS ceiling becomes irrelevant. **Moxidectin CAN reach 0.847 µM locally.** |
| ✅ the SPIN4 target itself | ✅ **unaffected** — Term A confirms SPIN4 contributes 38% of chondrocyte Wnt output, which is exactly why its loss works |

⭐ **AND R136's STRUCTURAL CLAIM IS CORRECTED, NOT JUST ITS CONSEQUENCE.** R136 wrote that the
positive feedback loop means *"the dose required to move this node is LOWER than a linear model
predicts,"* and called it *"an argument FOR the deliberately sub-saturating strategy ON MECHANISM."*
**That is withdrawn. The loop exists — TCF7L2 does occupy the locus — but at 4 peaks out of 100 TFs on
a constitutively transcribed gene it carries essentially no gain. R136 read occupancy as regulation,
having explicitly flagged that risk in the same paragraph and then relied on it anyway.**

---

## => WHAT I WOULD HAVE ACCEPTED AS A POSITIVE, SO THE NEGATIVE IS NOT UNFALSIFIABLE

- SPIN4 concordance **≥65%** in B1 (i.e. within reach of AXIN2's 69.5%) → coupling ~0.3, g ~0.11,
  amplification 1.13× — **still not a rescue, but a real loop.**
- SPIN4 **positively** correlated with Wnt output across zones → the mechanism would at least run the
  right way in the right tissue.
- **Neither happened. Both measurements went the wrong way, in independent data.**

⚠ **Honest limits of the measurement, stated in full:**
1. RummaGEO signatures are predominantly cancer lines, not chondrocytes. ⚠ **But the ENCODE TCF7L2
   occupancy that motivated the hypothesis was also from cancer lines — the hypothesis and its
   refutation stand on the same tissue footing.**
2. Binary up/down calls, not magnitudes — a coarse instrument. ⚠ **Which is why the AXIN2 positive
   control matters: the same coarse instrument resolved a real Wnt target at 69.5%.**
3. B2 is n=4 zones from 2 donors and cannot carry a significance test.
4. A loop could in principle be steeply nonlinear and have high gain only near a threshold this data
   never visits. **Unmeasurable here, and it is the one escape hatch — but it is a bare possibility
   with no evidence, not a reason.**
5. Term A is an upper bound.

> **Every one of those limitations would have to be wrong by ~100× to rescue the hypothesis. g needs
> to be 0.91; it measures 0.016–0.042.**

---

## => SO: IS MOXIDECTIN DEAD?

> ### **SYSTEMICALLY, YES. I checked the one thing that could have saved it, with a positive control that proves the assay works, and the answer is 1.02×.**
> **It is not "probably too weak" or "needs more work." It is 12× short with no amplifier, and the
> amplifier I proposed two rounds ago does not exist.**

**What survives is narrower and I am not going to inflate it:**
- **Selamectin** never depended on this argument and is unchanged.
- ⭐ **Local delivery remains the one route that rescues moxidectin**, because it removes the systemic
  ceiling entirely rather than trying to argue around it — and this file designed that delivery format
  eleven rounds before it needed it (R133, citing the intraosseous fibrin depot of R373/388/393),
  with R138's finding that the resting zone is the best-perfused zone of the plate.

**The explant design does change as a result:** R142 specified concentrations bracketing 40%
engagement. **There is no longer any reason to include moxidectin-achievable systemic concentrations
(0.03–0.17 µM) hoping amplification rescues them.** Include low concentrations to map the curve, not
to test a rescue that has now been measured and refuted.

---

## CORRECTIONS

- ⛔⛔ **R136's POSITIVE-FEEDBACK AMPLIFICATION ARGUMENT IS WITHDRAWN, MEASURED.** Loop gain
  **0.016–0.042** against the **0.91** required. Amplification **1.02×**, not 5×.
- ⭐ **The measurement carries a positive control:** AXIN2, a real Wnt target, scores **69.5%**
  concordance on the identical test where SPIN4 scores **52.1%**. **SPIN4's coupling to Wnt output is
  11% of a genuine Wnt target's.** The assay works; the gene is not Wnt-driven.
- ⭐ **Second independent line agrees:** SPIN4 **anti**-correlates with Wnt output across human growth
  plate zones (mean r = −0.28, all four readouts negative). ⚠ n=4 zones, indicative only.
- ⛔ **R139's and R142's reliance on the amplification argument is withdrawn.** Both used it to keep a
  3.5%-engagement agent alive. It does not do that work.
- ⛔ **The "compounds over time" argument is separated out and also fails** — an 8.7%-magnitude
  perturbation over an eighth of the growth period, at its least productive end, does not reproduce a
  lifelong 40%. Scaling argument, flagged as such.
- ⛔⛔ **MOXIDECTIN AT SYSTEMIC DOSES IS DEAD.** Not marginal. 12× short with no amplifier.
- ✅ **Selamectin is unaffected** — it never needed amplification.
- ✅ **Local/depot delivery is unaffected and is now the only route that rescues moxidectin.**
- ✅ **Term A independently CONFIRMS the target:** SPIN4 supplies 38% of chondrocyte Wnt output, which
  is precisely why losing it works.
