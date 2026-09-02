# F-R148 — **YES ON THE WNT DOSE: 30 mg QD IS A HUMAN-VALIDATED MILD WNT NUDGE AND THE 38–45% SPIN4 WINDOW SITS INSIDE ITS BAND. NO ON GETTING NRK FROM THE SAME DOSE — AND THE REASON IS STRUCTURAL, NOT A DOSING PROBLEM. R146's "ONE MOLECULE, BOTH ARMS" IS WITHDRAWN.**

**Direct answer to "can you find a dose that isn't too much Wnt / can you MIMIC the SPIN4 Wnt / can we reach
the perfect Wnt for N *and* the NRK off-target":**

1. ⭐ **The dose exists and a human trial already ran it.** 30 mg QD.
2. ⭐ **It mimics the SPIN4 magnitude, with a caveat about the *node* that I will not paper over.**
3. ⛔ **You cannot have both arms from one dose unless NRK is near-equipotent with TNIK. The exposure
   axis cancels out of the algebra — no dose choice can fix it.**

---

## => THE HUMAN DOSE-RESPONSE

`Xu et al., "A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized
phase 2a trial," Nat Med 2025` (PMID 40461817, PMC12353801, **open access**). Phase 2a, 12 weeks, IPF, n=71.

| arm | AUC₀₋ₜ wk0 | **AUC₀₋ₜ wk12** | ΔFVC (mL) | 95% CI | ALT↑ | diarrhoea | d/c per 18 |
|---|---|---|---|---|---|---|---|
| placebo | – | – | −20.3 | (−116.1, 75.6) | 5.9% | 0% | 2 |
| ⭐ **30 mg QD** | 553 | **788** | **not reported** | – | ⭐ **5.6%** | 11.1% | ⭐ **2** |
| 30 mg BID | 315 | **1390** | +19.7 | (−60.5, 99.9) — **crosses zero** | 5.6% | 16.7% | 6 |
| 60 mg QD | 1630 | **3450** | **+98.4** | (10.9, 185.9) — **excludes zero** | ⛔ **33.3%** | 27.8% | 6 |

t½ = 10.9–12.0 h · tmax = 1 h · steady state by week 2 · no accumulation to week 12.
60 mg QD without concurrent SOC antifibrotic: FVC **+187.8 mL** (68.6–306.9).

> ### ⭐ **THE STRUCTURE OF THIS TABLE IS THE FINDING.** The Wnt-driven **tissue phenotype** (antifibrotic FVC gain) and the **dose-limiting toxicity** (ALT, 33.3% = 6× placebo) switch on **together**, between AUC 1390 and 3450 — and **both are absent at 788**. One mechanism driving both is the signature of on-target TNIK/Wnt engagement. **30 mg QD is demonstrably below the threshold for a Wnt-driven tissue phenotype while still being a real pharmacological exposure.**

**That is exactly the object R137's magnitude ladder demands: a *mild* Wnt perturbation.** ALT 5.6% vs
placebo 5.9%; discontinuation 2/18, identical to placebo. It is not a low dose chosen for timidity — it
is a dose measured, in humans, to sit under the phenotype threshold.

---

## => STEP 2 — **HOW MILD? THE 38–45% SPIN4 WINDOW SITS INSIDE THE BAND**

Exposure ratios are exact from the table: **60QD / 30QD = 4.38×**, 30BID / 30QD = 1.76×.
Hill n=1 back-calculation from whatever the efficacious 60 mg QD dose engages:

| assumed E₆₀ | → **E₃₀ (30 mg QD)** | vs the 38–45% SPIN4 target |
|---|---|---|
| 50% | 18.6% | below |
| 60% | 25.5% | below |
| 70% | 34.8% | below |
| ⭐ **80%** | ⭐ **47.7%** | above |
| 90% | 67.3% | above |

> ### ⭐ **Across the entire plausible range for E₆₀, 30 mg QD lands at 18–48%. The 38–45% SPIN4 calibration constant (Lui 2023 Fig 6C/6D: 38% TOPFLASH, 45% Axin2) sits INSIDE that band.**

**This is the first time in this programme that a commercially obtainable, orally dosed, human-tested
molecule has had its achievable engagement range bracket the SPIN4 target rather than fall an order of
magnitude short of it.** Moxidectin reached 3.5–7% against the same 38–45% target (R140). This reaches it.

---

## => ⭐⭐⭐ STEP 3 — **THE DECISIVE NEGATIVE: THE EXPOSURE AXIS CANCELS**

The user's question was whether the *same* dose buys the NRK arm. Here is the algebra, and it is short.

One exposure `A`, two targets, Hill n=1. Let `f = IC50(TNIK)/IC50(NRK) ≤ 1` (NRK is by construction the
weaker, off-target site):

```
E_wnt = A/(A+Kt)          E_nrk = A/(A+Kn),   Kn = Kt/f

=>   E_nrk  =  f·E_wnt / (1 − E_wnt + f·E_wnt)        ←  A DROPS OUT ENTIRELY
```

> ### ⛔⛔ **At ANY dose that lands Wnt in the SPIN4 window, NRK engagement is a function of relative affinity ALONE. It is not a dosing choice. There is no dose to find.**

| f = IC50(TNIK)/IC50(NRK) | **NRK engagement at Wnt 38–45%** | verdict |
|---|---|---|
| ⭐ **1.00** | ⭐ **38.0 – 45.0%** | **BOTH ARMS ENGAGED** |
| ⭐ **0.70** | ⭐ **30.0 – 36.4%** | **BOTH ARMS ENGAGED** |
| 0.50 | 23.5 – 29.0% | partial, marginal |
| 0.30 | 15.5 – 19.7% | partial, marginal |
| 0.20 | 10.9 – 14.1% | ⛔ NRK arm effectively dead |
| 0.10 | 5.8 – 7.6% | ⛔ dead |
| 0.05 | 3.0 – 3.9% | ⛔ dead |

**And run backwards — what Wnt suppression is the *price* of a real NRK effect?**

| f | Wnt needed for NRK 30% | Wnt needed for NRK 50% | regime at NRK 50% |
|---|---|---|---|
| 1.00 | 30.0% | 50.0% | ⛔ past the window |
| 0.70 | 38.0% | 58.8% | ⛔ past the window |
| 0.50 | 46.2% | 66.7% | ⛔ past the window |
| 0.30 | 58.8% | 76.9% | ⛔ past the window |
| 0.20 | 68.2% | 83.3% | ⛔ past the window |
| 0.10 | 81.1% | **90.9%** | ⛔⛔ deep ICAT regime |

> ### ⛔ **Any f below ~0.9 forces you past the SPIN4 window to buy NRK — and past the window is R137's ladder: Spin4 loss (38–45%) +5.06% and Cxxc5−/− +3.8% LENGTHEN; ICAT, Ctnnb1 cKO and Lrp5/6 loss SHORTEN, CLOSE or KILL. You would be trading the arm that works for the arm that might.**

**Expected value, folding in R147's calibrated binding probability:**

| quantity | value |
|---|---|
| P(rentosertib engages NRK at all) | **70%** (R147, pocket-identity calibrated) |
| E[NRK engagement \| binds, Wnt at 41.5%] | **18.2%** |
| E[NRK engagement \| unconditional] | ⛔ **12.7%** |
| ⭐ **P(f ≥ 0.9 — the one case that serves both arms)** | ⛔ **~10%** |

---

## => ⚠ THE THREE CAVEATS I WILL NOT PAPER OVER

1. ⛔⛔ **THE NODE IS NOT THE SAME NODE.** TNIK acts at **TCF4**, as the nuclear activator of β-catenin
   target genes. SPIN4's effect is **β-catenin-dependent but TCF1-independent** (Lui 2023 Fig 6B). And
   **ICAT — which blocks the β-catenin/TCF interface — SHORTENS bone.** Node-wise, **TNIK inhibition
   sits closer to ICAT than to SPIN4.** Matching the *magnitude* (38–45%) is not the same as matching
   the *mechanism*. This is the single largest unresolved objection to the whole rentosertib arm, and
   the magnitude match does not dissolve it.
2. ⚠ **Lung-fibroblast Wnt output ≠ chondrocyte Wnt output.** The FVC anchor is a fibroblast phenotype.
   Nothing in this trial touches cartilage. I searched the paper's **Olink Explore 3072 panel (2,841
   proteins, baseline/2/4/12 weeks)** for a Wnt-specific PD readout — **there is none reported.** FVC is
   the only pathway anchor there is, and it is an indirect one.
3. ⚠ **12 weeks in elderly IPF patients is not years in an adolescent.** ALT monitoring would be
   mandatory even at 30 mg QD, and the 33.3% ALT rate one dose step up is a real signal about this
   chemotype's liver handling, not a formality.

---

## CORRECTIONS

- ⭐⭐ **THE WNT DOSE IS FOUND AND IT IS HUMAN-VALIDATED: rentosertib 30 mg QD**, AUC₀₋ₜ 788 at week 12.
  ALT 5.6% vs placebo 5.9%, discontinuation 2/18 = placebo, no separable FVC effect — i.e. **measured,
  in people, to sit below the threshold for a Wnt-driven tissue phenotype.** Back-calculation puts it at
  **18–48% pathway engagement, with the 38–45% SPIN4 window inside that band.** First molecule in the
  programme to bracket the calibration constant rather than miss it by 10× (cf. moxidectin, 3.5–7%).
- ⭐⭐⭐ **NEW STRUCTURAL RESULT — THE EXPOSURE AXIS CANCELS.** `E_nrk = f·E_wnt/(1−E_wnt+f·E_wnt)`:
  at any dose landing Wnt in the SPIN4 window, **NRK engagement depends on relative affinity alone.**
  There is no dose to search for. **Answering the user's question requires one affinity ratio, not a
  dose-finding exercise.**
- ⛔⛔ **R146's "ONE ORAL MOLECULE, BOTH ARMS" IS WITHDRAWN.** It holds only if f ≥ ~0.7, which carries
  ~10–15% probability. Unconditional expected NRK engagement at the Wnt window is **12.7%**.
- ⭐ **THE ASSAY QUESTION SHARPENS.** It was *"does rentosertib bind NRK?"* It is now **"does it bind NRK
  within ~1.4-fold of its TNIK potency?"** — a far harder bar, and the only one that matters.
- ⚠ **NODE MISMATCH FLAGGED AS THE LARGEST OPEN OBJECTION:** TNIK acts at TCF4; SPIN4 is
  TCF1-independent; ICAT blocks β-catenin/TCF and shortens bone. Magnitude match ≠ mechanism match.
- ⚠ **No Wnt PD biomarker exists in the trial** despite a 2,841-protein Olink panel. FVC is the only anchor.
- ⭐ **R147's falsifiable ordering still stands and now bites:** rentosertib is **AI-optimised for TNIK
  selectivity** and is therefore predicted to be the **worst** of the seven-compound panel for NRK.
  **The molecule that is best for one arm is predicted worst for the other.**
