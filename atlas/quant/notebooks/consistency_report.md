# Consistency report — parameter-flow model vs organism targets

**Phase 6 quantitative closure.**
Model: `atlas/quant/notebooks/flow_model.py`
Inputs: `atlas/quant/parameters.csv` (820 rows), `atlas/quant/organism_targets.csv` (103 rows)
Gap register: `atlas/gaps/gaps.yaml` (279 gaps)
Reproduce everything below with:

```bash
python3 atlas/quant/notebooks/flow_model.py --selftest
python3 atlas/quant/notebooks/flow_model.py --all
python3 atlas/quant/notebooks/flow_model.py --consistency
python3 atlas/quant/notebooks/flow_model.py --mode closure --site human_distal_femur
python3 atlas/quant/notebooks/flow_model.py --mode sensitivity --n 40000
```

---

## 0. What was built, and what was deliberately not built

A mechanistic ODE model of the growth plate was **not** attempted. The atlas's own record
forbids it: human growth plate pO2 has never been measured (`p00263`), 1378 of 1516
node-level parameter names appear exactly once, 65 of them as point values with no stated
uncertainty at all, and the central human kinetic constant is a derived quantity rather
than an observation. An ODE model would have had to invent a diffusion coefficient, a
consumption rate, a matrix synthesis rate and a mechanical constitutive law, none of which
exists for human tissue. It would have run beautifully and meant nothing.

What was built instead is an **arithmetic chain that carries provenance and refuses to
guess**. Each step multiplies a measured quantity by a conversion factor; each factor is
fetched by `param_id` from `parameters.csv` with its `source_ref`, its recorded spread and
its `reliability_class` (computed with the identical rule used by
`atlas/tools/compile_query.py`, so `single_source_point_no_uncertainty` means the same
thing here as everywhere else in the atlas). Where the factor the arithmetic needs has
never been measured, the model raises `MissingParameter`, prints the name of the factor,
the reason it is needed and the gap register entry that records its absence, and stops.

---

## 1. Does the model run end to end?

**No. It halts, and it halts in the same place for seven of the eight named sites.**

```
SUMMARY - where the chain halts
  7 site(s): step 2: hypertrophic volume expansion -> axial length
  1 site(s): step 1: proliferative output
```

| step | what it needs | status |
|---|---|---|
| 1 proliferative output | cells per proliferative column ÷ cell cycle time | **runs** for human (24 cells `p00176` / 20 d `p00177` = 1.20 cells/day/column) and for rat proximal tibia (8 cells/day/column measured directly, `p00163`). **Halts** for rat proximal radius: no cells-per-column row exists for any non-human species. |
| 2 hypertrophic volume → axial length | terminal hypertrophic cell **height**, µm/cell | **HALT, all sites.** The atlas records terminal hypertrophic *volume* (mouse, 5000–23000 fl, `p00230`/`p00232`) and a 4-fold rat *height increase* (`p00214`), but no absolute axial height in µm for any species and no transverse cross-sectional area with which volume could be converted to height. Gap **g_l1arch_009**. |
| 3 matrix + division → total elongation | human elongation partition | would halt: only rat values exist (9/32/59 % fast plate, 44 % hypertrophy / 49 % matrix slow plate, `p00185`–`p00189`). Gap **g_l1arch_001**. |
| 4 mineralisation / chondro-osseous removal | — | **identity, not a factor.** Steady state forces removal = production. No measurement in any species records net axial length lost at the junction, so the model asserts 1:1 and says so. Matrix synthesis cannot enter as a *rate* because human zonal pO2 is unmeasured (`p00263`, gap g_l1arch_007); it enters only as a partition share. |
| 5 mechanical modulation | in vivo human physeal stress | would halt: `p00664` records the human value verbatim as **"not measured"**. Gap **g_l6mech_003**. |
| 6 µm/day → cm/yr | ×365.25 / 10000 | exact, asserted, round-trip tested. |
| 7 site → stature | per-plate vertebral rate | would halt: `p00323` records it as **"not reported"**, across >130 vertebral plates (`p00321`). Gap **g_l1arch_011**. |

The single most useful result of the exercise is that **step 2 is a species-independent
wall**. It is not that human data are missing and rodent data would do. Nobody, in any
species, has published the number that converts a chondrocyte flux into a length flux in a
form this chain can use. Cooper 2013 measured volumes; Hunziker 1987 measured a fold-change;
Wilsman 1996 measured a partition. The absolute terminal cell height in micrometres, paired
with a site and a measured elongation rate, is not in the record.

### The unit layer passes

`--selftest` asserts every conversion and then cross-checks the atlas against itself:
kember1976 records **both** 1.4 cm/yr (`p00206`) and 38 µm/day (`p00207`) for the same
plate. 38 × 365.25 / 10000 = 1.3880 cm/yr, a residual of **−0.012 cm/yr (0.86 %)**. The two
rows are arithmetically consistent. This tests arithmetic only — they are one measurement
expressed twice.

---

## 2. Closure mode — running the chain backwards

Since the forward chain halts, it was run **backwards** from the measured elongation rate to
solve for the value the missing factor must take. Nothing is invented; the output is a
falsifiable prediction.

**Human distal femur.** 38 µm/day ÷ 1.20 cells/day/column = **31.67 µm of axial length
required per cell cycle**, of which, under the rat partition (44–59 %), **13.9–18.7 µm is
terminal hypertrophic cell height**. If the terminal cell had the mouse fast-plate volume
of 14000 µm³ it would have to be 30.9 µm wide; at the mouse slow-plate volume of 5000 µm³,
18.5 µm wide. These are ordinary mammalian chondrocyte dimensions. The prediction is
specific and directly measurable.

**Rat proximal tibia.** 8 cells/day/column against the 50–400 µm/day range wilsman1996a
reports across four plates gives **6.25–50.0 µm per cell** (2.75–29.5 µm as cell height).
The interval is wide because the atlas does not resolve the per-plate elongation rate — a
recording gap, not a biological one.

---

## 3. The residual, and its four possible sources

### 3.1 Against the site-level human data: the residual is zero, and that is the problem

The human chain reproduces 38 µm/day exactly. **This is not a success. It is circularity.**
`p00177` carries the uncertainty field *"derived quantity, not measured"*: Kember & Sissons
obtained the ~20-day human cycle time by dividing the column count by the growth rate. Using
it to predict the growth rate is an identity. The model prints a `CIRCULARITY WARNING` at
step 1 whenever it uses a row whose uncertainty field contains "derived".

> **Residual = 0 by construction. Source: (3) wrong model structure — specifically, the
> model and the parameter share an input. Not (1), (2) or (4).**

This is the strongest single conclusion of Phase 6. **There is at present no independent
human test of the cell-kinetic account of human bone elongation.** The literature reads as
though there is one because the derived number has been quoted as a measurement for fifty
years.

### 3.2 Against the organism targets: 70–81 % of stature velocity is unaccounted

Stature velocity = femur + tibia + foot + spine + skull base (one side). The atlas supplies
exactly one of those terms from measured rows.

| target | value | accounted by measured plate rows | residual | unaccounted |
|---|---|---|---|---|
| t001 peak height velocity, male (chun2024) | 9.61 cm/yr | 1.86 cm/yr | **+7.75 cm/yr** | 81 % |
| t003 peak height velocity, female (chun2024) | 8.32 cm/yr | 1.86 cm/yr | **+6.46 cm/yr** | 78 % |
| childhood 8–11 y (dalskov2016, `p00478`) | 6.10 cm/yr | 1.86 cm/yr | **+4.24 cm/yr** | 70 % |

The accounted term is the femur: distal femur 1.3 cm/yr (`p00208`) ÷ 0.70 distal share
(`p00309`) = 1.86 cm/yr. The tibia has a recorded *share* (57 %, `p00310`) but **no absolute
rate**. The spine has >130 plates and a per-plate rate recorded as "not reported". The foot
and skull base have no rows at all.

The age-matched comparison is the fair one — the pritchett rates are means over ages 7 to
maturity, so 6.10 cm/yr for 8–11 year olds is the right target, giving **+4.24 cm/yr, 70 %
unaccounted**.

**Attributing this residual.** All four sources are present and they are *partially*
separable:

1. **Wrong parameter value** — small contribution, and *bounded* for the one term we have.
   The femoral term rests on a 244-child serial radiographic series with 6-monthly
   teleroentgenograms (`p00208`) and is cross-checked by a second independent source for the
   same plate (kember1976, 1.4 cm/yr, `p00206`), agreeing to 7 %. Two sources at 7 % cannot
   generate a 4.24 cm/yr residual. **Distinguishable, and largely excluded for the femur.**
   Nothing can be said about the terms that have no rows.
2. **Missing mechanism** — **not distinguishable from (1) or (3) here**, because the terms
   that are missing are missing as *rows*, not as *biology*. The tibia and the spine
   certainly elongate; the atlas simply does not record how fast. Until those rows exist, no
   claim about a missing mechanism can be made from this residual. Anyone who reads the 70 %
   as evidence for an unknown growth process is over-reading it.
3. **Wrong model structure** — **partly distinguishable and demonstrably present.** Two
   structural faults are visible. (a) The circularity in §3.1. (b) The recorded human
   per-site rates carry no age resolution at all: `p00208` is a mean over ages 7 to
   maturity, while t001 is an instantaneous peak. A model with no age argument cannot
   reproduce an age-indexed target however good its parameters are. This is why the model's
   `--age` argument changes nothing and says so.
4. **Measurement error in the organism target** — **excluded as a major source.** t001 is a
   SITAR fit to 1519 heights in 123 boys with a stated SE of 1.26 cm/yr; the residual is
   6 SE. The targets are far better measured than the parameters.

> **Verdict: the residual is dominated by (3) model structure — chiefly missing age
> resolution and an incomplete plate inventory — with (2) missing mechanism unresolvable
> from these data. It is not evidence of a wrong parameter value, and it is not measurement
> error in the target.**

### 3.3 Against the accuracy ceiling

SITAR fits serial heights in the same age band with a residual SD of **0.79 cm in height**
(t028, cole2010). Integrating the parameter-flow shortfall over one year leaves **4.24 cm of
height unaccounted after twelve months — about 5× the SITAR floor**, and growing linearly
with the prediction window. A statistical model that knows nothing about chondrocytes
describes these children five times more accurately than the mechanism-derived chain does.
That gap is the honest measure of how far the mechanistic account is from being
quantitatively useful at the organism level.

---

## 4. The checks that *did* pass, and what they buy

### 4.1 Species cross-check — the only non-circular test available

| | rat proximal tibia | human distal femur |
|---|---|---|
| production | 8 cells/day/column (`p00163`) | 1.20 cells/day/column (derived) |
| elongation | 50–400 µm/day (`p00192`) | 38 µm/day (`p00207`) |
| **required length per cell** | **6.25–50.0 µm** | **31.67 µm** |

The human requirement lies **inside** the rat range. The ~16-fold human/rat cell cycle gap
(20 d vs 30.9 h) is absorbed almost entirely by the production rate (6.7-fold) and **not**
by the length each cell contributes.

This yields a substantive, falsifiable prediction: **human terminal hypertrophic chondrocytes
should be of ordinary mammalian size, and the human plate should be slow because it cycles
slowly, not because its cells are small.** Measuring human terminal hypertrophic cell height
(gap g_l1arch_009) tests it directly. A human value near 15 µm confirms the chain; a value
near 40 µm would falsify either the 24-cell column count or the 20-day cycle time and would
be the first hard evidence that Kember's derivation is wrong.

### 4.2 A cross-source check inside the rat data that the atlas cannot close

16400 cells/day/plate (wilsman1996, `p00190`) ÷ 8 cells/day/column (hunziker1987, `p00163`)
⇒ **2050 columns per rat proximal tibial growth plate**.

`parameters.csv` contains no columns-per-plate and no column-density row for any species, so
this prediction — which spans two independent laboratories and would be a genuine test —
cannot be evaluated. **New quantitative gap, recommended for the register.**

### 4.3 Site-to-site coherence, and what it exposes

Applying the same human constants to every site with a recorded rate:

| site | required length per cell |
|---|---|
| distal radius, girls | 20.53 µm |
| distal radius, boys | 22.82 µm |
| proximal humerus, boys | 29.66 µm |
| distal femur (pritchett1992) | 29.66 µm |
| distal femur (kember1976) | 31.67 µm |

A 1.54-fold spread. But the human kinetic constants are held fixed across sites because the
atlas has only one human value for each, so **all** site-to-site variation is forced onto the
one factor that has never been measured. The model cannot distinguish "human plates differ
in terminal cell size" from "human plates differ in cycle time" — gap g_l1arch_010, and the
reason it cannot is a recording gap, not a modelling choice.

---

## 5. Sensitivity: where the uncertainty actually lives

Declared spans were propagated through the forward chain (40000 log-uniform draws,
freeze-one variance decomposition on log output, common random numbers). Every span is
stamped either `MEASURED_SPREAD` (taken off a recorded row) or `DECLARED_SPAN` (the factor
has never been measured; the bracket is stated with the rows it is bracketed from). The
disputed zonal stiffness is carried at its genuine range — 380 kPa (rabbit, `p00602`) to
416 MPa (human, `p00607`), ~1100-fold — and with its **direction unresolved**: xie2025 makes
the hypertrophic zone 3.18× stiffer than resting, sergerie2009 makes proliferative +
hypertrophic 0.33–0.5× *softer* than reserve. The model uses the whole interval 0.33–3.18
and does not pick a side.

**Output: predicted distal femoral elongation, median 4.44 cm/yr, 90 % interval
0.58–33.1 cm/yr — a 57-fold span.** The measured 1.3–1.4 cm/yr lies inside it, which tells
us essentially nothing.

| rank | parameter | share of output uncertainty | status | gap |
|---|---|---|---|---|
| 1 | terminal hypertrophic cell height | **45 %** | UNMEASURED | g_l1arch_009 |
| 2 | human proliferative cell cycle time | **40 %** | UNMEASURED (derived) | g_l1arch_002 |
| 3 | cells per proliferative column | 6 % | UNMEASURED dispersion | g_l1arch_012 |
| 4 | in vivo human physeal stress | 4 % | UNMEASURED | g_l6mech_003 |
| 5 | zonal stiffness ratio / gradient direction | 3 % | DISPUTED, direction unresolved | g_l5matrix_008 |
| 6 | growth-rate sensitivity to stress | 1 % | measured, animal only | g_l6mech_001 |
| 7 | elongation partition | 0.5 % | measured, rat only | g_l1arch_001 |

**98 % of the output uncertainty is carried by parameters that have never been measured.**

0.2 % of draws drove the Stokes linear stress–growth law past zero elongation — outside the
−0.2 to +0.1 MPa interval over which linearity was actually demonstrated (`p00691`). Those
draws are reported, not clipped; the functional form beyond that range is gap g_l6mech_002.

### Robustness of the ranking

In a multiplicative chain every kinetic input has |∂lnY/∂lnX| = 1 by construction — the
model confirms elasticities of exactly ±1.00 for the kinetic terms and −0.05 for the
mechanical terms (which enter as a near-unity multiplier at median stress). **No input is
structurally more powerful than another; the ranking is entirely a statement about how wide
current ignorance is.** That is precisely the right basis for an experimental agenda, but it
means the ranking must be recomputed whenever a span changes.

Re-run under `--scenario human_ignorance`, which widens the elongation partition from the
rat spread (0.44–0.59) to genuine human ignorance (0.20–0.80), the top two are unchanged
(41 % and 37 %) and the partition rises to 9 %. **The top two are robust; positions 3–7 are
not, and should not be read as a fine ranking.**

One honest caveat on positions 4 and 5: the model places mechanics as a modest multiplier on
a baseline rate, so the three-order-of-magnitude stiffness dispute contributes only ~3 % of
*this* output's uncertainty. That is a consequence of this model's structure, not a claim
that the stiffness question is unimportant — for guided growth, tethering and scoliosis
progression it is first-order. It is second-order **for predicting baseline elongation**.

---

## 6. What a reader should take away

1. The chain from cell cycle to centimetres per year **cannot be closed with measured
   numbers in any species**, and it breaks at the same step everywhere: nobody has published
   the terminal hypertrophic cell height that converts cells per day into micrometres per day.
2. The one human closure that appears to work is **circular** — the human cell cycle time was
   derived from the growth rate it is used to predict.
3. Against the organism targets, **70–81 % of stature velocity cannot be assigned to any
   measured growth plate**, because the tibial rate, the per-vertebra rate and the foot are
   not in the record. This is a recording gap first and a mechanism gap only possibly.
4. The mechanistic account is currently **~5× less accurate over one year than a SITAR curve
   fit that contains no biology at all.**
5. **98 % of the predictive uncertainty sits on parameters nobody has measured**, and two of
   them carry 85 % of it. Those two are the agenda: see
   `docs/experimental_agenda.md`.
