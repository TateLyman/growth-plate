# A prioritised experimental agenda for human growth plate biology

**What this is.** A ranking of the specific measurements that would most reduce uncertainty
about how a human growth plate turns cell division into centimetres per year. The ranking is
not editorial. It is the output of a parameter-flow consistency model
(`atlas/quant/notebooks/flow_model.py`) run against the atlas's own 820-row parameter record
and 103 organism-level targets, with each parameter's recorded spread propagated and each
parameter's *contribution to output uncertainty* measured by freeze-one variance
decomposition on 40 000 Monte Carlo draws. Every experiment below is taken from the atlas gap
register (`atlas/gaps/gaps.yaml`), where it was written with its model system, its readout
and its expected result under each competing hypothesis.

**Why it can be acted on.** A literature review can tell you what is unknown. This tells you
what is unknown *and* how much of the field's quantitative ignorance each unknown carries,
so that a limited budget can be spent in the right order.

**Headline.**

> **98 % of the uncertainty in predicting human bone elongation from cell behaviour sits on
> parameters that have never been measured. Two of them carry 85 % of it. Both can be
> measured on the same piece of surgical waste tissue. Doing so collapses the predicted
> elongation rate from a 57-fold interval to a 3-fold interval — an 89 % reduction in
> variance — for the cost of one well-designed study.**

---

## The reading of the model this ranking comes from

The chain runs:

```
cells per proliferative column ÷ cell cycle time      [cells/day/column]
  × terminal hypertrophic cell height                 [µm/day, hypertrophic]
  ÷ hypertrophic share of the elongation budget       [µm/day, total]
  × steady-state mineralisation / removal closure
  × mechanical modulation (1 − k·σ)
  × 365.25 / 10 000                                   [cm/yr]
  ÷ site share → bone → stature
```

Run in strict mode it **halts at step 2 for seven of eight named sites**, and for the eighth
at step 1, because the factor that converts a chondrocyte flux into a length flux has never
been published in any species in a usable form. Residual against the organism targets: 70 %
of childhood stature velocity and 81 % of peak height velocity cannot be assigned to any
measured growth plate. Full analysis in `atlas/quant/notebooks/consistency_report.md`.

**How to read the percentages below.** In a multiplicative chain every kinetic input has unit
elasticity, so no parameter is *structurally* more powerful than another. The percentage is
therefore a measure of how wide current ignorance of that parameter is — which is exactly the
right basis for deciding what to measure, but means the ranking must be recomputed as spans
close. The top two positions are robust to the choice of declared spans (re-run under
`--scenario human_ignorance` they hold at 41 % and 37 %); positions 3–7 are not, and should
be read as a tier, not a fine ordering.

---

## TIER 1 — the two measurements that matter most (85 % of uncertainty, one specimen stream)

### 1. Terminal hypertrophic chondrocyte height and volume in human growth plate, by site and age

| | |
|---|---|
| **Uncertainty contribution** | **45 %** (46.9 % variance reduction if measured alone) |
| **Gap** | `g_l1arch_009`, quantitative_gap, L1 |
| **Tractability** | **3 / 5** |
| **Status** | never measured in human; **and the model halts here for every species** |
| **Nearest evidence** | breur1991, cooper2013, thurston1985 |

**Why this is number one.** It is not merely the largest single contributor to uncertainty —
it is the step at which the chain *stops*. The atlas records terminal hypertrophic *volume*
in mouse (5000–23 000 fl, cooper2013 `p00230`/`p00232`) and a 4-fold *height increase* in rat
(hunziker1987 `p00214`), but no absolute axial height in micrometres for any species, and no
transverse cross-sectional area with which volume could be converted to height. Final
hypertrophic volume is also the strongest correlate of elongation rate in every mammal in
which it has been measured (r = 0.98 rat, 0.83 pig, breur1991), and it is the parameter that
CNP analogues and FGFR3 inhibitors are believed to act on.

**The experiment (from the register).** Apply Hunziker's high-pressure-freezing /
ruthenium-hexammine fixation and the physical disector to human physeal blocks from at least
three sites (distal femur, proximal tibia, distal radius) and two age bands, reporting mean
final hypertrophic volume with CI. Test whether human values fall on the mammalian
volume-versus-growth-rate regression using the human site-specific elongation rates from
pritchett1992 and pritchett1991 as the abscissa. Ordinary decalcified paraffin histology will
not do — it shrinks hypertrophic lacunae unpredictably and cannot give a volume.

**What each outcome means.** The model already states what the answer must be if the current
account is right: to reach the measured 38 µm/day of the human distal femur at 1.20
cells/day/column, the terminal cell must contribute **31.7 µm of axial length per cycle, of
which 13.9–18.7 µm is cell height** under the rat partition. A human value in that band
confirms the chain and puts a real number where a fifty-year-old assumption sits. A value
near 40 µm falsifies either the 24-cell column count or the 20-day cycle time and is the
first hard evidence that Kember's derivation is wrong. A large negative residual against the
mammalian regression means humans reach their slow growth rates by a different mixture of
parameters than rodents — which would predict, mechanistically, the observed shortfall
between mouse and human responses to CNP analogues.

**Feasibility.** Tissue source already exists: epiphysiodesis and hemiepiphysiodesis waste,
the same stream that has yielded human physeal MMP and single-cell datasets. The rate-limiter
is fixation discipline, not access.

---

### 2. Direct measurement of the human proliferative-zone cell cycle time

| | |
|---|---|
| **Uncertainty contribution** | **40 %** (41.9 % variance reduction if measured alone) |
| **Gap** | `g_l1arch_002`, species_gap, L1 (with `g_l1arch_012` for cycle structure) |
| **Tractability** | **3 / 5** |
| **Status** | the human figure is **derived, not measured** — and the derivation is circular |
| **Nearest evidence** | kember1976, thurston1985, wilsman1996a |

**Why this is number two, and arguably number one.** Kember & Sissons obtained ~20 days for
the human distal femur by dividing a column cell count by a radiographic growth rate;
Wilsman measured 30.9 h directly in the rat proximal tibia by repeated BrdU pulses. That is a
**~16-fold species gap that has never been closed by a human measurement.** Worse for
modelling: `p00177` carries the uncertainty field *"derived quantity, not measured"*, so
using it to predict human elongation is an identity, not a test. The consistency model prints
a circularity warning and reports a residual of zero **by construction**. There is at present
no independent human test of the cell-kinetic account of human bone elongation, and the
literature reads as though there is one because a derived number has been quoted as an
observation for five decades.

If the 20-day figure is real, the human growth plate is a slow, low-turnover tissue and
rodent proliferation-targeted pharmacology and rodent toxicology windows do not scale.

**The experiment (from the register).** Label surgically obtained human physeal cartilage
explants (epiphysiodesis or hemiepiphysiodesis waste) with EdU under near-physiological
oxygen (2–5 % O₂) and matrix-preserving culture, then fix at a graded series of times (6 h to
14 d) and fit the percent-labelled-mitoses or cumulative-labelling curve. Report the growth
fraction separately by zone (`g_l1arch_012`); double-label EdU→BrdU at a defined interval to
recover S-phase duration by the relative-movement method.

**What each outcome means.** Saturation of the cumulative labelling index within 2–3 days
falsifies the 20-day estimate and shows the human plate simply has a **smaller growth
fraction** — a different biology from a slow cycle, with different pharmacological
implications. Saturation only after >2 weeks confirms a genuinely long human cycle and
justifies treating rodent turnover rates as inapplicable.

**Note on the oxygen condition.** Human growth plate pO₂ has never been measured
(`p00263`, gap `g_l1arch_007`). Culturing at 21 % O₂ may be hyperoxic by an order of
magnitude. The 2–5 % specification is itself an assumption, which is why gap `g_l1arch_007`
is listed in Tier 3 as a supporting measurement.

---

### ★ The single highest-value experiment: do 1 and 2 on the same specimen

Both measurements draw on the **same tissue stream** — paediatric epiphysiodesis /
hemiepiphysiodesis waste — and both are stereology-and-labelling work in one laboratory.

Run as a paired study on the same blocks, with a clinically-indicated tetracycline or calcein
label giving a **directly measured elongation rate for that same plate** (the design already
written into gap `g_l1arch_001`), a single study delivers cell cycle time, growth fraction,
terminal hypertrophic volume and height, and the elongation partition, for one named human
site with a measured rate.

**Modelled effect on uncertainty:**

| state | 90 % interval on predicted distal femoral elongation | variance reduction |
|---|---|---|
| today | 0.58 – 33.1 cm/yr (**57-fold**) | — |
| after measuring terminal cell height alone | 1.07 – 18.3 cm/yr (17-fold) | 47 % |
| after measuring cycle time alone | 1.01 – 19.3 cm/yr (19-fold) | 42 % |
| **after both, same specimen** | **2.47 – 7.89 cm/yr (3-fold)** | **89 %** |
| plus column count by age/site | 3.02 – 5.51 cm/yr (2-fold) | 96 % |

This is the recommendation. One tissue stream, one laboratory, three quantities, and the
first non-circular human test of the mechanism in the field's history.

---

## TIER 2 — the recording gaps that block organism-level closure (cheap, unglamorous, decisive)

These contribute little to the *per-plate* prediction but make it impossible to sum plates to
stature at all. The consistency model halts at step 7 and leaves **70 % of childhood stature
velocity and 81 % of peak height velocity unassignable to any measured plate**. These are
imaging and archive studies, not bench work.

### 3. Per-plate vertebral growth rate, per level and per endplate

| | |
|---|---|
| **Effect** | unblocks step 7; without it no plate-level model can be summed to stature |
| **Gap** | `g_l1arch_011`, quantitative_gap, L1 |
| **Tractability** | **4 / 5** — among the highest in the register |
| **Status** | recorded verbatim as **"not reported"** (`p00323`), across >130 plates (`p00321`) |

**Experiment (from the register).** Serial low-dose biplanar (EOS) imaging in children imaged
for non-spinal indications: ossified vertebral body height per level at 6-month intervals from
age 5 to maturity, with MRI in a subset to separate disc from bone. Report mm/yr per level and
per endplate. **Under the classical model** cranial thoracic levels grow fastest per level in
early childhood with a lumbar-dominant pattern at puberty; **a flat profile falsifies the
assumption underlying level-selective tethering.**

**Why it is worth doing despite ranking below Tier 1 on variance.** The spine contributes
roughly a third of standing height, and the entire growth-modulation field — vertebral body
tethering, growing rods, scoliosis natural history — currently works from segment-level
radiographs. This is the most tractable gap in the register and it converts a whole
therapeutic area from segment-level to plate-level reasoning.

### 4. Absolute human tibial (and foot) elongation rates, age-resolved

| | |
|---|---|
| **Effect** | second missing term in the stature sum |
| **Gap** | adjacent to `g_l1arch_011`; the atlas records the proximal tibial *share* (57 %, `p00310`) but no absolute cm/yr |
| **Tractability** | **4 / 5** — archival |

The Pritchett series measured femur, humerus, radius and ulna absolutely but the tibial rate
was recorded only as a share. **This may be a recording gap rather than a literature gap: the
first action is an archive check, not a new cohort.** A second, more serious point applies to
the whole Pritchett set — the rates are *means over ages 7 to maturity*, while the organism
targets are instantaneous peak velocities. **No human per-site elongation rate in the atlas is
age-resolved.** A model with no age argument cannot reproduce an age-indexed target however
good its parameters are. Re-analysing the existing serial radiographic series to yield
per-site cm/yr *by age band and sex* would be the cheapest single improvement in the whole
agenda.

### 5. Columns per growth plate / column areal density (proposed new gap)

| | |
|---|---|
| **Effect** | closes an existing two-laboratory cross-check that currently cannot be evaluated |
| **Status** | **no row for any species** in `parameters.csv` |
| **Tractability** | **5 / 5** — a morphometric count on existing sections |

The model finds a genuine cross-source test hiding in the record: 16 400 cells/day/plate
(wilsman1996 `p00190`) ÷ 8 cells/day/column (hunziker1987 `p00163`) ⇒ **2050 columns per rat
proximal tibial growth plate**. Two independent laboratories, one falsifiable prediction — and
the atlas cannot evaluate it because nobody recorded a column count or a column density.
Counting columns per unit plate area on existing rat and human sections is a week of work and
would either validate or break the two most-cited stereological datasets in the field.
**Recommended for addition to the gap register as a quantitative_gap.**

---

## TIER 3 — the disputes: resolve the contradiction, do not average it

These contribute 3–4 % each to *this* model's output uncertainty, because the model places
mechanics as a modest multiplier on a baseline rate. **That is a property of this model's
structure, not a claim that the questions are unimportant** — for guided growth, tethering,
physeal fracture and scoliosis progression they are first-order. They rank here for predicting
baseline elongation, and much higher for predicting response to load.

### 6. Which zone of the growth plate is stiffest — and is the gradient direction real?

| | |
|---|---|
| **Uncertainty contribution** | 3 % (baseline elongation); first-order for load response |
| **Gap** | `g_l5matrix_008` (contradiction, **tractability 4/5**), with `g_l5matrix_001` (human moduli, 3/5) |
| **Status** | **values span ~1100-fold and the direction disagrees** |

The record: rabbit microindentation 380–690 kPa (`p00602`); porcine unconfined compression
puts proliferative + hypertrophic at 0.33–0.5× the reserve zone, i.e. **softer** (`p00608`,
`p00609`); human sharp-tip AFM gives resting 130.7 MPa and hypertrophic 416.2 MPa, i.e.
hypertrophic **3.18× stiffer** (`p00606`, `p00607`, xie2025). The model carries the whole
interval 0.33–3.18 and does not pick a side; consequently it **cannot determine which zone
carries the peak stress**, and the sign of the zonal stress concentration is unknown.

**Experiment (from the register).** A single-laboratory factorial study: proximal tibial and
cranial base physes from rabbit and pig at two ages, each specimen measured by (i)
microindentation with a 100 µm spherical probe, (ii) AFM with a 5 µm spherical probe, and
(iii) zone-dissected unconfined compression — all hydrated in PBS, with paired Safranin-O and
Raman proteoglycan mapping. **Method-dependent:** indentation and compression disagree within
the same specimen and the field's disagreement is a technique artefact. **Site-dependent:**
cranial base and long bone differ consistently, and cranial-base data must be excluded from
long-bone models. **Age-dependent:** the newborn porcine result (reserve stiffest) reverses in
older animals as the hypertrophic zone calcifies.

Pair with `g_l5matrix_001`: on human epiphysiodesis tissue, run compression **and** both AFM
probe geometries on the same specimen. If the human physis is genuinely stiff, spherical-probe
and compression moduli also land in the tens of MPa. If the sharp-tip result is a length-scale
and fluid-pressurisation artefact, they fall to 0.3–2 MPa and match rabbit and pig — and the
130–416 MPa figures must be reported as local fibrillar-matrix moduli, not tissue moduli.
**Every existing finite-element model of paediatric physeal loading is wrong by orders of
magnitude under one of these outcomes.**

### 7. In vivo stress across a human physis, and the human Hueter–Volkmann coefficient

| | |
|---|---|
| **Uncertainty contribution** | 4 % (stress, `g_l6mech_003`) + 1 % (coefficient, `g_l6mech_001`) |
| **Tractability** | **2 / 5** (stress, method_blocked) and **3 / 5** (coefficient) |
| **Status** | human physeal stress recorded verbatim as **"not measured"** (`p00664`) |

The Stokes coefficient — 17.1 % growth change per 0.1 MPa, range 9.2–23.9 across plates
(`p00638`) — is the quantitative core of the Hueter–Volkmann law and the basis on which
guided growth, vertebral body tethering and scoliosis vicious-cycle simulations are planned.
It has been measured only in three quadruped species, at two skeletal sites, over 8-day
loading windows, and the stress it must be multiplied by has never been measured in a human at
all.

**Experiment for the coefficient (from the register, tractability 3).** Prospective cohort of
children undergoing unilateral tension-band hemiepiphysiodesis of the distal femur, with (a)
implant strain measured directly by instrumented plate or strain-gauged screw, (b)
subject-specific FE models driven by instrumented gait and MRI geometry converting that force
plus body loading into physeal stress on tethered and free sides, and (c) longitudinal growth
on each side by serial low-dose EOS or tantalum-bead radiostereometry. Regress percent growth
difference on stress difference. **Animal coefficient transfers:** slope 15–19 %/0.1 MPa with
the animal range covering the human CI. **Human physes less mechanosensitive** — which the
slow, highly variable clinical correction rates hint at — slope substantially below
9 %/0.1 MPa, with residual variance dominated by skeletal age rather than stress.

**A boundary the model exposed.** Propagating the declared spans drove 0.2 % of draws past the
point where the linear stress–growth law predicts zero or negative elongation — outside the
−0.2 to +0.1 MPa interval over which linearity was ever demonstrated (`p00691`). The
functional form beyond that range is gap `g_l6mech_002` (tractability 5/5, the top
tractability band in the register). **Establishing where the linear law breaks is cheap and nobody has done it.**

### 8. Human elongation partition — division / matrix / hypertrophy

| | |
|---|---|
| **Uncertainty contribution** | 0.5 % as recorded (rat spread), **9 % under honest human ignorance** |
| **Gap** | `g_l1arch_001`, quantitative_gap, tractability 3/5 |

The known constraint is rat: 9 % division / 32 % matrix / 59 % hypertrophy in the fast
proximal tibia, shifting to 44 % hypertrophy / 49 % matrix in the slow proximal radius
(wilsman1996). The apparent low contribution is an artefact of using the *rat* spread as the
uncertainty — **no human partition exists at all**, and under a declared human-ignorance span
this rises to 9 %.

**Experiment (from the register).** Obtain human physeal specimens at elective epiphysiodesis
or limb-lengthening osteotomy from patients who received a tetracycline or calcein double
label for an unrelated clinical indication (or a research-consented single label), giving a
directly measured elongation rate for that plate. Apply the Wilsman/Hunziker stereological
estimators to the same block. **If the human partition matches the rat (~59 % hypertrophy),
rodent-derived therapeutic logic transfers. If matrix synthesis dominates (>50 %, as in the
slow rat proximal radius), agents acting on hypertrophic volume should have proportionally
smaller effects in humans than in mouse models** — which would predict the observed shortfall
between mouse and human responses to CNP analogues.

**This is the same specimen and the same block as Tier 1.** It should be done in the same
study. It is listed separately only because its uncertainty contribution is separately
computed.

---

## TIER 4 — supporting measurements that make Tier 1 interpretable

| | measurement | gap | tractability | why it is here |
|---|---|---|---|---|
| 9 | **Human zonal pO₂, in mmHg** | `g_l1arch_007` | 3/5 | Never measured (`p00263`). Every human explant experiment in Tier 1 must choose an oxygen tension, and that choice is currently a guess. If the resting/inner proliferative zone is below 10 mmHg, explants cultured at 21 % O₂ are hyperoxic by ~15-fold and all such data need reinterpretation. Microelectrode profile at 100 µm steps on a fresh human physeal block, or pimonidazole before an elective procedure. |
| 10 | **Cells per proliferative column, by site and age, in human and in rodent** | `g_l1arch_012` | 3/5 | 6 % of output uncertainty. The atlas holds exactly one cells-per-column row — human distal femur, 24 cells, kember1976, no dispersion, no age or site resolution — and **none for any other species**, which is where the chain halts at step 1 for the rat proximal radius. A morphometric count, obtainable on the same blocks as Tier 1. |
| 11 | **Human physeal elongation at sub-weekly resolution** | `g_l1arch_006` | 2/5 | The model's target rates are all inferred from limb or stature anthropometry. Radiostereometric analysis at 48-hour intervals in children who already have transphyseal hardware (precision ~50 µm) would give the first direct human physeal velocity and simultaneously adjudicate the saltatory-growth contradiction (`g_l1arch_005`). Method-blocked in healthy children; opportunistic only. |

---

## What the field gets for this

| if you do | you close | and you learn |
|---|---|---|
| **Tier 1 (one study, one specimen stream)** | 89 % of the predictive variance | whether the human growth plate is slow because it cycles slowly or because its cells are small — and the first non-circular human test of the mechanism |
| **+ Tier 2 (imaging and archive work)** | step 7 of the chain; the 70 % stature residual becomes attributable | whether the residual is missing mechanism or merely missing rows — currently indistinguishable |
| **+ Tier 3 (one factorial mechanics study)** | a 1100-fold dispute with an unresolved sign | whether every paediatric physeal FE model in use is wrong by orders of magnitude |

**A single, specific, testable prediction to falsify first.** The model's species cross-check
finds that the human requirement (31.7 µm of axial length per cell cycle) lies inside the rat
range (6.25–50.0 µm), and that the ~16-fold human/rat cell cycle gap is absorbed by the
production rate (6.7-fold) rather than by the length each cell contributes. **Therefore:
human terminal hypertrophic chondrocytes should be of ordinary mammalian size, ~13.9–18.7 µm
tall.** That is one number, from one stain, on tissue that is already being discarded.

---

*Generated from `atlas/quant/notebooks/flow_model.py --agenda`. Uncertainty contributions:
40 000 draws, freeze-one variance decomposition on log output, common random numbers, seed
20260805. Rankings should be recomputed as spans close. Full method and residual analysis:
`atlas/quant/notebooks/consistency_report.md`.*


---

# ANNEX — feasibility, added 2026-08-06 (FINAL-01 item I)

Ranking by uncertainty contribution says **what to measure**. It does not say whether the
measurement is *possible*, and "nobody has measured this" is a much weaker claim than
"**this is measurable by X and nobody has done it**". The second is actionable and the
first is a complaint. Every Tier 1–3 item is annotated below with: does a technique exist
that could make the measurement in human tissue **today**; what tissue it would need; and
whether the same measurement has already been made in another species or tissue by a
method that would transfer.

Searches run live against Europe PMC on 2026-08-06; hit counts recorded so each is
re-runnable.

| # | measurement | technique exists for human? | tissue / sample requirement | already done elsewhere by a transferable method? |
|---|---|---|---|---|
| **1** | terminal hypertrophic cell **height** | **Yes** — stereology / optical disector on histological sections, entirely routine | a few fixed blocks of human physis; **epiphysiodesis and physeal-bar resection discard exactly this tissue routinely** (297 hits on human physeal surgery, e.g. arthroscopy-assisted bar resection, Xiao 2025) | **Yes, extensively** — 818 hits for growth-plate stereology/histomorphometry, essentially all rodent. The method is mature; only the human specimen is missing. |
| **2** | human proliferative **cell cycle time** | **Partly** — cumulative EdU/BrdU labelling needs living tissue over hours to days, so *in vivo* human measurement is out. **Ex vivo explant labelling of surgical waste at 2–5 % O₂ is the only route.** | fresh (not fixed) human physeal tissue, transported live | **Barely** — only **43** hits for cumulative labelling + cycle time in chondrocytes across all species. This is a thin methodological literature, which is itself why the human number has never been produced. |
| **3** | per-plate **vertebral growth rate** | **Yes** — serial calibrated radiography or low-dose EOS in children already under spinal surveillance | no tissue; imaging already being acquired for clinical reasons | Yes — the porcine and ovine tether literature measures per-plate growth directly (Halanski 2026 on biphasic tether-tension effects). |
| **4** | absolute **tibial elongation rate**, age-resolved | **Yes** — knemometry and serial imaging; both already in the atlas as methods | none | Yes — the human femur figure exists; the tibia simply was not extracted. |
| **5** | **columns per plate** / areal density | **Yes** — same sections as item 1, a different count on the same slide | shares item 1's specimen entirely | Yes, rodent. |
| **6** | **zonal stiffness** direction | **Yes** — AFM and nanoindentation on cartilage are routine (**1,187** hits, including human articular cartilage and chondrocyte-level measurements) | fresh human physeal tissue, unfixed, ideally the same surgical stream as item 2 | **Yes, in the wrong tissue.** The method is established on human *articular* cartilage and on animal physis. The human *physeal* measurement is the gap, not the technique. |
| **7** | **in vivo physeal stress** in a human | **Yes, indirectly and already being done** — musculoskeletal inverse dynamics driven by gait analysis, coupled to a subject-specific finite-element model. **Koller 2026 computes femoral growth-plate mechanics in humans from foot-progression-angle modifications**; Valkani 2026 addresses trans-physeal bridges as a mechanical "base isolation" | none — imaging plus motion capture in living children | **Yes.** This is the one Tier-3 item where the human measurement is not merely feasible but has begun. What the atlas lacks is the *extraction*, not the method. |
| **8** | human elongation **partition** | **Yes** — it is arithmetic on items 1, 2 and 5 | none beyond items 1–2 | n/a — it is derived, not measured. |

## What the annex changes

**Six of the eight are limited by specimen access or by extraction effort, not by
technique.** None of the Tier 1–3 items requires a method that does not exist.

That reframes the whole agenda. The correct sentence is **not** "the field cannot measure
these". It is:

> **The two measurements carrying 85 % of the uncertainty in human longitudinal growth
> can be made with a microtome and a fluorescent label, on tissue that paediatric
> orthopaedic surgeons already remove and discard, and the reason they have not been made
> is that nobody has asked for the specimens.**

The one genuine methodological constraint is item 2: cumulative labelling needs *living*
tissue, which makes it an ex-vivo explant measurement with all the caveats that carries,
and the 43-hit literature says the technique itself is under-developed rather than merely
unapplied.

The one item that is further along than the atlas assumed is item 7: human in-vivo
physeal stress is being computed today by inverse dynamics plus subject-specific FE
modelling. `flow_model.py` halts on this parameter recording it as "not measured", and
that is now known to be a **gap in the atlas's extraction, not a gap in the field.** It is
the cheapest item on this list to close and it should be closed first.

## The same upgrade applied to the exposure finding

This annex does to the parameter agenda what was already done to the 0-of-12 exposure
result: it converts *"nobody has measured the concentration a growth-modifying drug
reaches inside human growth-plate cartilage"* into *"microdialysis and matched
tissue-sampling protocols exist, the tissue is obtained surgically, and nobody has run
them."* A gap with a named method attached is a proposal. A gap without one is a
complaint.

---

# ANNEX 2 — the Tier 1 prediction was tested, and it failed by 9.6 % (2026-08-06)

Everything above this line is left as written. An agenda that quietly edits its
predictions after seeing the answer is not an agenda.

## What was predicted, and what was measured

| | |
|---|---|
| **predicted** (this document, §"A single, specific, testable prediction to falsify first") | human terminal hypertrophic chondrocytes **13.9–18.7 µm tall** |
| **measured** (thurston1985, full text, human distal femur, 10-year-old girl) | **20.5 µm** |
| **verdict** | **FAILED.** 20.5 > 18.7 by 9.6 % |

A second human value exists — **26 µm**, metatarsals of an 18-month-old — and is *not*
scored, because the atlas holds no metatarsal elongation rate to close against.

**The measurement was published in 1985.** The atlas held the paper as
`primary_abstract_only` and recorded in three nodes and two gaps that the numbers were
paywalled. They were not unavailable; they were unread.

## What the failure is worth, which is more than the success would have been

The band was not a guess. It was the closure of this document's own chain:

| step | value |
|---|---|
| observed distal femoral elongation (kember1976) | 38 µm/day |
| production, 24 cells / 20 d (kember1976) | 1.20 cells/day |
| ⇒ axial length required per cell cycle | **31.67 µm** |
| × rat hypertrophic share 44–59 % (wilsman1996) | **13.9 – 18.7 µm** |

Inverting it on the measurement:

> **implied human hypertrophic share = 20.5 / 31.67 = 64.7 %**, against a rat range of
> **44 – 59 %**.

The human distal femur puts a *larger* fraction of its elongation into terminal
hypertrophic cell height than even the fastest rat plate, leaving **35 %** for matrix
synthesis and cell division together against **41 %** in the rat proximal tibia. That is a
first-principles cross-species prediction with no free parameters missing by under 10 %,
with a residual that points in a single interpretable direction. It is the first
quantitative statement the atlas can make about `g_l1arch_001`, the human elongation
partition — a gap that has no human measurement at all.

**It also corrects a qualitative claim this document made elsewhere.** The reasoning that
a slow human plate implies *small* terminal cells is wrong. Human terminal cells
(20.5–26 µm) are of ordinary mammalian size. The human plate is slow **with ordinary-sized
terminal cells**, which puts the entire human/rodent difference into cell flux — the one
term the human record cannot measure.

## What it did to the ranking

| parameter | share of output uncertainty BEFORE | AFTER |
|---|---:|---:|
| **terminal hypertrophic cell height** | **45 %** | **0 %** |
| **human proliferative cell cycle time** | 40 % | **80 %** |
| cells per column | 6 % | 9 % |
| in vivo physeal stress | 4 % | 5 % |
| zonal stiffness ratio | 3 % | 4 % |

**Experiment 1 above is retired in its height half and survives in its volume half.** The
height is measured; the *volume* is not, and cannot be derived, because no transverse
cross-sectional area has ever been reported for a human hypertrophic chondrocyte. The
volume is what places human plates on the mammalian volume-versus-growth-rate regression,
so `g_l1arch_009` remains open with a narrowed scope — and with a cheap first step that
did not exist before: **measure the transverse diameter on the same decalcified archival
sections the heights came from.** That converts an existing measurement into a volume
with no new tissue.

## The new number one, and the reason it is now much sharper

**Experiment 2 — direct measurement of the human proliferative-zone cell cycle time — is
now 80 % of the model's uncertainty on its own,** and the measurement has made the
question sharper rather than merely more urgent.

Both published human cycle times come from `rate = (N_p / T_c) × h_term` solved for `T_c`.
That identity has no matrix-synthesis term and no division term, so it assumes the
hypertrophic share is exactly 1.0. Read against the measured height:

| set | production | axial length/cycle | implied hypertrophic share |
|---|---:|---:|---:|
| kember1976 — 24 cells, 20 d | 1.20 cells/day | 31.7 µm | **64.7 %** |
| thurston1985 — 28 cells, 15 d | 1.87 cells/day | 20.4 µm | **101 %** |
| *rat, directly measured* | — | — | *44 – 59 %* |

thurston1985 revised the cycle time **downward** — newer number, better-measured specimen
— and the revision is the one the rest of the record cannot accommodate. Under the rat
partition the same measured inputs give a human cycle time of **22–34 days**, longer than
either published figure.

So the experiment now has three live hypotheses to separate rather than one to confirm,
and the EdU cumulative-labelling design in §2 separates all three because **it measures
`T_c` without using the growth rate** — which is precisely what breaks the circularity
that makes both published figures untestable:

| saturation time | reading |
|---|---|
| **2–3 days** | both published figures are wrong; the plate has a small growth fraction and a fast cycle, not a slow one |
| **~15–20 days** | the published derivations are right and the human hypertrophic share is 65–100 %, i.e. unlike any measured rodent plate |
| **> 26 days** | the partition-corrected reading is right, the human share is rat-like, and both published human cycle times are too short |

Report the growth fraction separately. A long average dwell time in a mostly quiescent
pool is not a slow cycle, and the atlas currently cannot tell the two apart.

*Trace: `atlas/audit/corrections.md` CORR-006. Model: `flow_model.py --site
human_distal_femur` (blocked, prints the closure) and `--site
human_distal_femur_thurston` (runs, halts at the partition).*
