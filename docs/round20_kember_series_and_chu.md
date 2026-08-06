# Round 20 — the Kember kinetics series and Chu 2026: a correction, and a lever

**Date:** 2026-08-06 · **Branch:** `claude/growth-system-atlas-yl5esl`

Four sources read in full: `kember1993` (review), `kember1987` and `kember1990` (primaries),
and `chu2026` (Sci Transl Med). The first one contradicts something I told you last round.

---

## 1. CORR-014 — I overstated my own headline

Last round I wrote: *"Human proliferative cell cycle time is 20 days. The rat figure is 2
days"* — as a **ten- to fifteen-fold species difference in cycling speed**. And: human
terminal cell height has **"no age dependence."**

`kember1993` is Kember reviewing his own method seventeen years later. It supplies two things
I quoted the 1976 numbers without:

**Precision.** The method gives data of *about ±50%*. Twenty days is **10–30 days**. And
*changes smaller than 20% are beyond the limits of detection* — so "no age dependence" means
**no trend larger than ~20% was detectable in twelve subjects**, not that the parameter is
fixed. The observed 29–38 µm span is itself ±14% around 33.

**An alternative explanation, stated by the author, that I did not consider.** The low human
labelling percentage *"is not unequivocal evidence that the dividing cells cycle more slowly."*
Human chondrocytes may have a **low growth fraction** — most proliferative-zone cells not in
cycle at all — and *"the cells in cycle could be dividing as rapidly as in rodents."* This
cannot be settled, because **the duration of S phase in human growth cartilage has never been
measured**, and every route from labelling percentage to proliferation rate needs it.

**Withdrawn:** the claim of a species difference in *cycling speed*.
**Survives:** a 10–15× difference in *mean cell production per proliferative-zone cell* — a
different quantity, which does not license the mechanistic gloss.

**Also survives untouched:** the load-bearing claim — human terminal cell size does not move
anywhere near enough to carry the several-fold variation in growth velocity across childhood,
so cell production must. A ±20% detection limit does not rescue a parameter asked to explain a
several-fold change. Grades held; nothing downstream reversed.

This is a **new failure mode**, not a repeat of CORR-009→013. Those were all *a source existed
and was not read*. Here the source **was** read, in full, the same day — and the qualifying
sentences were in a different paper by the same author. Reading a primary does not retrieve
its author's later assessment of its own precision, and a 1976 measurement and a 1993 review
of how good such measurements are share no topic, only an author. New standing rule recorded.

---

## 2. What the correction opens: the growth fraction

New node `growth_fraction_human_proliferative_zone` (L1, grade **D**).

Cell production = **growth fraction × cycle speed**. A labelling percentage bounds the product
and neither factor. The human plate labels **4.4% and 3.4%** — against **10–15%** across nine
bird species (`kember1990`, 68 growth plates). Human is ~3× below the lowest bird.

The two readings are not equally actionable:

- **Slow cycling** → to grow more you must accelerate the cell cycle of a differentiated cell.
  Hard, no precedent.
- **Low growth fraction** → most of the human proliferative zone is **idle at any moment**, and
  recruitment is a multiplicative term sitting far below 1 — in a compartment already shown to
  be releasable, because human resting-zone cells held out of cycle *in a child* re-enter it
  within days of explant (`avijgan2026br`).

**Nobody has measured it, in either direction, in a human.** That is now the single unmeasured
human parameter in this atlas with the largest ratio of leverage to cost.

---

## 3. The avian primaries kill terminal cell size as a growth driver

`kember1987`, chicken tibiotarsus: **~1000 µm/day of elongation on 15 µm terminal cells**
(SE 0.4, n=75), ~60 new cells per output channel per day, cycle time near 1 day. Human distal
femur at ages 5–8: **38 µm/day on 33 µm cells**.

**A chicken plate elongates ~26× faster than a human one using cells less than half the
height.** The human has the largest cells and the slowest growth.

`kember1990`, the within-clade version across 68 growth plates and nine species: terminal cell
size **10–18 µm with no clear trend** against growth rate; labelling percentage **10–15% with
little variation**; and the major cause of between-species growth-rate differences is **the
size of the flat cell zone**. Growth rate per flat cell does not scale with adult body weight
(r = −0.22, n = 6, ns) — so cycle time appears independent of body size and metabolic rate.

Written into `hypertrophic_volume_increase`, whose central claim now stands as a
between-site/within-species-and-age mammalian regression, and is contradicted as a general
determinant of growth rate both **across birds** and **across human development** (C-L1-09).

---

## 4. Chu 2026 — there is a human growth assay and I did not know it

New node `human_growth_plate_explant_assay` (L13, grade **B**).

`chu2026` sections human growth plate cartilage into 1 mm slices and maintains them **ex vivo
for two months** with preserved histology and Safranin O proteoglycan. GH produces measurable
cartilage expansion, raises PZ proliferation (**P = 0.013**) and the 24-h S-phase fraction
(**P < 0.0001**). **Bone does not expand** in the same cultures — the internal negative
control. `avijgan2026br` runs the complementary sequential EdU→IdU→CldU protocol on the same
tissue type.

Every candidate in this atlas has been judged on mouse growth, human genetics, or a transcript
in the right human cells — **never on whether it makes human cartilage grow.** That assay
exists.

**Its real limit, which neither paper states as a design constraint:** GH — the best-validated
growth drug in medicine — **failed to produce an effect in some donors.** Donor-to-donor
variance is large enough to hide the positive control, so any screen needs several donors per
arm and is underpowered for anything weaker than GH.

Also from the full text: two resting-zone stem populations — PTHrP-**negative** `Prrx1+` "root"
cells in a low-WNT/low-TGF-β niche, and `SFRP5+`/PTHrP+ cells; mouse clonal tracing confirms
the root cells generate extensive clones and stromal/osteoblastic progeny. `chu2026` is now
marked read and its type corrected from `primary_abstract_only`.

---

## 5. The experiment this round nominates

New gap `g_l13_human_explant_screen`: **run sacubitril in the `chu2026` explant**, vehicle
control, GH positive control, several donors per arm.

`hakata2024` showed the effect survives in isolated fetal tibia with no circulation, pituitary
or liver — exactly what an explant can detect. And the atlas holds the complication that makes
the null informative: **NPPC sits at the detection floor in human growth plate scRNA-seq.** If
the local ligand really is absent, an inhibitor of its degradation should do *nothing here*
while still being able to work in a child through *circulating* CNP. So the explant tests the
local-ligand question as well as the drug, and a null is informative rather than merely
disappointing — the condition this atlas requires before nominating an experiment.

Two more gaps opened: `g_l1arch_human_growth_fraction` (cumulative labelling in explant; the
plateau *is* the growth fraction) and `g_l1arch_human_s_phase` (double-label at hours rather
than days — the cheapest unmeasured constant in human growth biology).

---

## 6. Atlas state

628 nodes · 1,220 edges · 305 gaps · 1,095 refs · **0 validator errors**
A 156 · B 189 · C 187 · D 81 · E 13 · X 2

New: `growth_fraction_human_proliferative_zone` (D), `human_growth_plate_explant_assay` (B).
New refs: `kember1993`, `kember1987`, `kember1990`. `chu2026` marked read, type corrected.
`CORR-014` recorded. Rows qualified at row level in `human_growth_plate_age_trajectory` and
`cell_cycle_time_pz`.
