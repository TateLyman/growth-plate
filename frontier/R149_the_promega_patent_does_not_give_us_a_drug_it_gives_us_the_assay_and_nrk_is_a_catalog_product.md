# F-R149 — **THE PROMEGA ROW IS NOT A DRUG HIT AND MUST NOT BE READ AS ONE. IT IS SOMETHING BETTER: THE FIRST DIRECT EVIDENCE THAT SMALL MOLECULES OCCUPY NRK'S ATP POCKET IN LIVING CELLS — AND NRK TURNS OUT TO BE AN OFF-THE-SHELF CATALOG ASSAY (NV3831 + TRACER K-11). R148's ONE UNKNOWN IS NOW DIRECTLY MEASURABLE.**

**Direct answer to "does this at all give you a better idea for NRK?": yes, substantially — but not for
the reason it appears to. Read carefully, this row does not say two compounds inhibit NRK. It says
NRK's pocket is ligandable in cells, and it points at a catalog product that turns R148's decisive
unknown from a custom protein-science project into an ordered plasmid.**

---

## => ⛔ FIRST, THE ERROR THIS COULD HAVE BECOME

`US20200003771A1 / US11442063B2 / US12078634 — "Broad spectrum kinase binding agents," Promega Corp.`

**CC-1817, CC-1804 and CC-1294 are not inhibitors. They are fluorescent tracers.** Each is a
broad-spectrum kinase-binding core with a fluorophore hung off a PEG linker:

| tracer | core it derives from | what the core is |
|---|---|---|
| CC-1803, **CC-1804** | **CC-1861** | broad-spectrum kinase binder |
| CC-1290, **CC-1294** | **CTx-0294885** | bisanilinopyrimidine, a promiscuous kinome-enrichment reagent |
| **CC-1817** | CC-1852 / CC-1861 series | broad-spectrum kinase binder |

They exist to be *displaced*. Their entire purpose is to be promiscuous — a tracer that bound
selectively would be useless. **A promiscuous tracer binding NRK is weak evidence about whether a
selectivity-optimised drug binds NRK.** Reading "HIT" here as "we found an NRK inhibitor" would be the
exact error I have been named for three times in this file — *localisation ≠ intervention*, now wearing
a chemistry costume. **It is not a drug. It buys us nothing about rentosertib's affinity directly.**

### ⚠ And one honest downgrade of the numbers as they were passed to me

The patent's own colour scale is: **green >3× = robust · yellow 2–3× = moderate · red 1.5–2× = marginal.**

| entity | conc. | BRET | ⭐ **the patent's own call** |
|---|---|---|---|
| CC-1817 | 0.5 µM | **2.85×** | ⚠ **yellow — MODERATE, not robust** |
| CC-1804 | 0.5 µM | **1.51×** | ⚠ **red — MARGINAL, barely over threshold** |
| CC-1294 | 1 µM | 1.09× | ⛔ negative |

**So "HIT / HIT / negative" is closer to "moderate / marginal / negative."** NRK is not a top-tier binder
for these cores. That matters, and I am not going to round it up.

---

## => ⭐⭐ NOW WHAT IT ACTUALLY BUYS, WHICH IS MORE THAN THE MISREADING WOULD HAVE

### 1. ⭐ **NRK's ATP pocket is ligandable IN LIVING CELLS. This is the first direct evidence of it.**

R145 established NRK is **Pharos Tdark — 0 ligands, 0 drugs, not a ChEMBL target.** R147's entire
druggability case was **inference**: 77.4% ATP-pocket identity to MAP4K4/TNIK/MINK1, identical
`HRDIGVDFG`, conserved Met gatekeeper (Met129), calibrated against 68–94% measured within-clade
carry-over. Every bit of that was sequence reasoning.

> ### ⭐ **This row replaces inference with measurement. A cell-permeable small molecule enters a live cell, crosses into NRK's ATP site, and produces a 2.85× energy-transfer signal. NRK's pocket is open, accessible at cellular ATP concentrations, and druggable by permeable chemistry. That was assumed. It is now observed.**

### 2. ⭐ **The negative is informative too — NRK's pocket has real chemotype preference.**

CC-1294 scores **1.09× at 1 µM — double the concentration** at which CC-1817 and CC-1804 register. So
NRK takes the CC-1852/CC-1861 cores and **rejects the CTx-0294885 bisanilinopyrimidine core even at 2×.**

**This cuts both ways and I will state both:**
- ⛔ **Against us:** the pocket is *not* an indiscriminate sponge. That argues slightly *down* on R147's
  ~70% blanket carry-over estimate for an arbitrary clade inhibitor.
- ✅ **For us:** it means a negative result in the real experiment would be **interpretable as biology
  rather than dismissed as assay failure** — the assay demonstrably discriminates.

### 3. ⭐⭐⭐ **THE ONE THAT ACTUALLY CHANGES WHAT WE CAN DO: NRK IS A CATALOG PRODUCT.**

| component | ⭐ **catalog** | detail |
|---|---|---|
| ⭐ **NanoLuc®-NRK Fusion Vector** | ⭐ **NV3831** | 20 µg · **N-terminal** NanoLuc–human NRK fusion |
| ⭐ **NanoBRET® TE Tracer K-11** | ⭐ **N2650** (100 assays) / **N2651** (1,000) | the tracer Promega's own NRK example data uses |
| counter-screen vectors | same catalog line | Promega lists **>340 kinases**; MAP4K4 / TNIK / MINK1 are all standard |

> ### ⭐⭐⭐ **THIS KILLS THE COST-AND-FEASIBILITY OBJECTION TO THE #1 DECISIVE EXPERIMENT.**

**Why that objection was serious.** The R146/R147 experiment was *"recombinant NRK activity assay vs a
seven-compound panel."* NRK is Tdark: **no established physiological substrate, no validated activity
buffer, no known activation state.** Building an *activity* assay for a Tdark kinase is the expensive,
slow, may-simply-fail step — and it was the real reason that experiment kept being described rather than run.

**NanoBRET does not need activity at all.** It measures **binding by tracer displacement** in live
HEK293 cells. Transfect NV3831, add Tracer K-11, titrate the competitor, read the BRET ratio.
**Plasmid + tracer + cells.** No purification, no substrate, no activity conditions.

**And it measures the *right* quantity.** Intracellular occupancy in a living cell — permeability
included, competing against real cellular ATP. That is precisely the number R148 needs, not a
buffer-condition IC50 that would then need translating.

---

## => ⭐⭐⭐ THE EXPERIMENT, REWRITTEN — TWO VECTORS, ONE NUMBER

R148 proved the exposure axis cancels: at **any** dose landing Wnt in the 38–45% SPIN4 window,

```
E_nrk = f·E_wnt / (1 − E_wnt + f·E_wnt)          f = IC50(TNIK)/IC50(NRK)
```

**Everything hinges on the single scalar `f`.** NanoBRET returns it directly:

| run | vector | readout |
|---|---|---|
| A | ⭐ **NV3831 (NRK)** + Tracer K-11 | cellular IC50 of rentosertib on **NRK** |
| B | **TNIK vector** + its tracer | cellular IC50 of rentosertib on **TNIK** |
| ⭐ **f = IC50(TNIK) / IC50(NRK)** | | ⭐ **the whole answer** |

| **f comes back** | **verdict** |
|---|---|
| ⭐ **≥ 0.7** | ⭐⭐ **R146 is reinstated — one oral, human-tested molecule serves BOTH arms at 30 mg QD** |
| 0.3 – 0.7 | partial: real Wnt arm, weak NRK arm; NRK needs a separate agent |
| ⛔ **< 0.2** | ⛔ **rentosertib is a Wnt-arm-only drug. The NRK arm needs its own molecule, and NV3831 is how you screen for it.** |

**Same plate, extra wells, near-zero marginal cost:** PF-06260933 · GNE-495 · NCB-0846 · bosutinib ·
lestaurtinib · dovitinib. R147's falsifiable ordering goes in as a **pre-registered prediction** —
**rentosertib is AI-optimised for TNIK selectivity and is predicted to be the WORST of the panel for NRK.**
If it comes back best, my selectivity model is wrong and I want to know that.

⚠ **Prices are login-gated on Promega, so I will not invent them.** What I can say factually: **these are
catalog line items, not a custom protein-science project** — which was the entire objection.

---

## CORRECTIONS

- ⛔ **THE PATENT ROW IS NOT A DRUG HIT — CC-1817/CC-1804/CC-1294 ARE FLUORESCENT TRACERS**, promiscuous
  by design, built to be displaced. Reading it as "two compounds inhibit NRK" would repeat this file's
  recurring error in a new costume. **It gives us nothing directly about rentosertib's affinity.**
- ⚠ **NUMBERS DOWNGRADED AGAINST THE PATENT'S OWN SCALE:** >3× robust / 2–3× moderate / 1.5–2× marginal.
  **CC-1817 at 2.85× is MODERATE; CC-1804 at 1.51× is MARGINAL.** Not "HIT / HIT."
- ⭐⭐ **BUT NRK'S POCKET IS NOW EMPIRICALLY LIGANDABLE IN LIVE CELLS** — cell-permeable small molecules
  occupy it at cellular ATP. **R145's Tdark / 0-ligands status and R147's pure-inference druggability
  argument are both upgraded to observation.**
- ⭐ **CHEMOTYPE DISCRIMINATION MEASURED:** NRK accepts the CC-1852/CC-1861 cores, **rejects the
  CTx-0294885 bisanilinopyrimidine core at 2× the concentration.** Argues slightly *down* on R147's ~70%
  blanket carry-over, but makes a future negative result interpretable rather than ambiguous.
- ⭐⭐⭐ **NRK IS AN OFF-THE-SHELF ASSAY: NanoLuc-NRK Fusion Vector NV3831 (20 µg, N-terminal) + NanoBRET
  TE Tracer K-11 (N2650/N2651).** The #1 decisive experiment no longer requires building an activity
  assay for a substrate-less Tdark kinase — **it requires ordering two catalog items.**
- ⭐⭐ **THE EXPERIMENT IS REWRITTEN AS TWO VECTORS AND ONE NUMBER.** R148 showed everything reduces to
  `f = IC50(TNIK)/IC50(NRK)`; NanoBRET returns exactly that, as **intracellular** occupancy, which is the
  correct quantity rather than a buffer IC50 needing translation. **f ≥ 0.7 reinstates R146; f < 0.2
  makes rentosertib a Wnt-arm-only drug.**
- ⭐ **AND NV3831 IS ALSO THE SCREENING TOOL FOR THE FALLBACK** — if rentosertib misses NRK, the same
  vector is how you find the molecule that does not.
