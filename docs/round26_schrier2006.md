# Round 26 — `schrier2006` read in full: the yield hypothesis is twenty years old, and it is a residual, not a guess

## What was asked for and why

CORR-034 recorded that I asked the user for a paper the atlas had held since 2026-08-05 —
`schrier2006`, PMID 16614378, *Depletion of resting zone chondrocytes during growth plate senescence*,
J Endocrinol 189:27–36 — because its key result had never been extracted into any node. The atlas was
carrying that result at second hand, from `nilsson2014` citing it. The user supplied the PDF. This
round reads it.

## The result the atlas came for

**Dexamethasone uncouples exit rate from renewal rate, and it is a direct measurement.**

4-week-old rabbits, dexamethasone 0.5 mg/kg s.c. daily for two weeks, n = 6–7 per group:

| measurement | result |
|---|---|
| resting zone BrdU-labelling index | **decreased**, P < 0.001 (both epiphyseal and reserve regions) |
| number of resting zone chondrocytes | **greater**, P = 0.016 — driven by the **reserve** region (P < 0.001), not the epiphyseal |
| serum IGF-I | 112 ± 8 vs 108 ± 6 ng/mL, not significant |

The authors' own inference: the increased cell number *occurred despite* decreased proliferation, so
dexamethasone must slow the transition from resting to proliferative chondrocytes. Pool size is inflow
minus outflow, and this moves outflow independently of inflow. That is the existence proof the
exchange-rate model needed, and it is now sourced to the primary rather than to a paper citing it.

The cost is the obvious one: the dose is supraphysiological and chosen because it inhibits growth.
Dexamethasone buys capacity by not using it. It is not a height therapy; it is a demonstration that
the two fluxes are separable.

## The result the atlas did not know was there — and it matters more

**The paper has a third arm, and the abstract does not foreground it.**

Schrier pre-specified the two mechanisms by which oestrogen could accelerate senescence through the
resting zone: it speeds resting zone proliferation, spending capacity sooner; or it speeds the
numerical loss of resting zone cells. Both were measured, in 4-week-old male rabbits on estradiol
cypionate 70 µg/kg i.m. weekly for two weeks (serum E2 11 ± 2 pg/mL vs < 5 in vehicle).

**Oestrogen did neither.**

- Resting zone BrdU index **fell** (P = 0.011) — the wrong direction for the first hypothesis
- Resting zone cell number **unchanged** — no effect at all for the second
- Serum IGF-I 88 ± 6 vs 108 ± 6 ng/mL, not significant

So after two weeks of oestrogen, the two measurable state variables of the pool — how fast it divides,
and how many cells it holds — are moving the wrong way and not at all respectively, while senescence
accelerates. Something is being spent that neither number sees.

**That residual is the yield.** The authors name it: oestrogen might accelerate senescence *by a
proliferation-independent mechanism or by increasing the loss of proliferative capacity per cell
cycle*. That second clause is the quantity this atlas has spent three rounds arguing is the only
untouched lever, and it was stated in 2006 — eight years before `nilsson2014` restated it from a
different direction, and twenty years before this project reached it.

**The epistemic status changes, and upward.** The atlas had been treating the yield as an inference
drawn from a discussion paragraph. It is the residual of a completed elimination: two candidate
mechanisms pre-specified and both excluded *by measurement*. That is a stronger object than a
speculation, and it is why the node's confidence note was rewritten rather than just its summary.

## A third finding: the decline is not gradual

Distal femur resting zone BrdU-labelling index by age (1 week of continuous BrdU, n = 6–12 per group):

| age | labelling index |
|---|---|
| 0 weeks (late fetal) | 95.6 ± 0.8 % |
| 5 weeks | 9.2 ± 1.2 % |
| 9 weeks | 9.2 ± 1.1 % |
| 17 weeks | 7.6 ± 1.5 % |

A tenfold fall before 5 weeks, then essentially nothing across the next twelve — over an interval in
which the rabbit is still growing and will eventually fuse. If resting zone proliferation is flat from
5 to 17 weeks while senescence continues, falling resting zone proliferation cannot be what drives
senescence over most of the growing period. That is a **second, independent** reason the driver has to
be something other than the two observables.

(Limits: four timepoints, the fetal point is a different tissue architecture and its cell count is a
lower bound only, and 95.6 % is at ceiling so the first interval is partly a ceiling effect.)

## And it cuts against us: `C-L2-06`

`schrier2006` and `nilsson2014` disagree on the sign of the parameter this atlas's whole depletion
model rests on:

| | `schrier2006` | `nilsson2014` |
|---|---|---|
| compound, dose, route | estradiol cypionate, 70 µg/kg, i.m. weekly | **identical** |
| duration | 2 weeks | 5 weeks (+ 5 week washout) |
| animals | 4-week-old intact males | ovariectomised females from 11 weeks |
| **resting zone cell number** | **unchanged** | **irreversibly reduced** |

Same laboratory, same drug, opposite outcome. The economical reading is **duration** — depletion is
cumulative and two weeks is below detection — which would make `schrier2006` a bound on the *rate*
rather than a counter-claim. But sex, age at start and the washout all differ too, and no
dose–duration series exists. Opened as gap `g_l2_oestrogen_depletion_time_course`, tractability 4,
with the note that the reconciliation may be recoverable from the published figures without new animal
work.

**The stake is not cosmetic.** The atlas uses the schrier2006 null to argue that oestrogen spends
something neither observable captures. If that null is merely underpowered (n = 6–7, no power
calculation) or too short, the yield argument loses its footing. This is recorded on the node as a
limit, not buried.

## Changes committed

- `the_exchange_rate_between_growth_and_pool_depletion` — 3 new quantitative rows (oestrogen double
  null; the age curve; the epiphyseal/reserve subcompartment dissociation), summary and confidence
  note rewritten. Stays at **B**.
- `rz_depletion_causes_fusion` — the "AT SECOND HAND" caveat retired; the two-week/five-week tension
  recorded.
- `g_l2_raise_the_yield_per_progenitor` — origin of the yield concept corrected to `schrier2006` 2006;
  new missing-item (e) for the duration question.
- New gap `g_l2_oestrogen_depletion_time_course`; new contradiction `C-L2-06`.
- `schrier2006` reclassified `primary_abstract_only` → `primary`, `full_text_read: 2026-08-07`.

## CORR-035, and the schema change it forced

Checking a count for the correction entry exposed something larger. I was about to write "N references
are `primary_abstract_only`, each a place where a result like this could be sitting," and to propose a
rule: *don't cite from an abstract when the atlas holds the PDF.*

The rule was unstatable, because **`has_full_text` never meant the atlas held anything.**
`atlas/tools/addref.py:150`:

```python
"has_full_text": rec.get("hasTextMinedTerms") == "Y" or rec.get("inEPMC") == "Y",
```

Both are Europe PMC metadata. The flag means *a full text exists in Europe PMC* — a fact about a third
party's database. That is why 1,006 of 1,068 references carried it. CORR-034 had already flagged this
field as misleading and characterised it as "records that a PDF was obtained"; **that
characterisation was itself too generous, and is corrected here.**

Three changes made:

1. `has_full_text` → **`in_epmc`** across bibliography, 26 shards, 3 tools.
2. **`local_pdf: true`** added where a file is actually on disk with a basename matching the ref_id —
   **38 references**, against 1,006 under the old flag. That ratio is the size of the error. (It
   under-counts: held PDFs with non-matching filenames are missed, so 38 is a floor.)
3. **New validator check `held_but_unread`**: `local_pdf: true` + `type: primary_abstract_only` + cited
   by ≥1 node.

**It fired on two references immediately — `glasson2005` and `williams2001`.** Both held, both cited
from their abstracts, neither read. The same failure as `schrier2006`, still live, and invisible until
the field was replaced with one that means what its name says.

## What this round changes about the height problem

The yield term is no longer this project's conjecture. It is a twenty-year-old published hypothesis
that survived an elimination and that **nobody has measured in any species since.** The gap
`g_l2_raise_the_yield_per_progenitor` now records that explicitly, and its discriminating experiment
is unchanged and still cheap: count resting zone cells per mm and proliferative divisions per column
in one animal series, take the ratio, then perturb with dexamethasone. Two papers each measured one
numerator. Neither reported the quotient.

## Addendum — the gap misstated what `nilsson2014` contains, and the yield is closer than recorded

Following the round through to the gap's discriminating experiment, I re-read `nilsson2014` to check
its claim that *"`nilsson2014` and `lui2018` each measured one of the two numerators and neither
reported the quotient."*

**That is wrong about `nilsson2014`, which measured both.** In the same animals, at the same
timepoints, reported as adjacent panels of one figure:

| term | where |
|---|---|
| proliferative chondrocytes per column | Figure 2 C, D |
| resting zone chondrocytes per mm growth plate width | Figure 2 G, H |
| proliferation rate (BrdU-labelled cells per proliferative column) | Figure 3 |

Oestrogen and vehicle, proximal tibia and distal radius, 16 and 21 weeks. **Every term needed to
construct a yield is in one paper.** The gap has been recording a two-paper synthesis problem when it
is a one-paper arithmetic problem.

**Two things stop it from being done in this round, and both are stated rather than worked around.**

1. **Mechanical.** Both figures are raster images in the PDF the atlas holds — there is no source data
   table and no supplemental values. I checked for vector coordinates in both papers; `schrier2006`'s
   pages carry 130–209 vector objects but they are body-text glyph outlines, not plot markers, and the
   figures themselves are embedded images. Recovering the values means pixel digitisation with axis
   calibration, which carries read error. Any number from that route is a **re-analysis of plotted
   values, not a measurement**, and would be graded as such. Asking the authors for the underlying
   values is the clean route and is cheap.

2. **Conceptual, and it would have been an easy error.** Cells per column and cells per mm are
   **standing stocks**. A yield is a flux over a flux. The ratio of two stocks at one timepoint is not
   the quantity — the correct construction is proliferative divisions *accumulated over an interval*
   divided by resting zone cells *lost over that interval*. That is why the 16-week and 21-week pair
   matters, and why a single-timepoint quotient would produce a confident wrong number.

Both are now recorded in the gap's `discriminating_experiment`, along with the correction to
`nearest_evidence_note`.

**One free precision improvement while in the file.** The node's TUNEL row carried the qualitative
statement that apoptosis did not account for the resting zone loss. The numbers are in the text:
**4.6 ± 0.6 % (oestrogen) vs 4.4 ± 1.0 % (vehicle), P = 0.87**, n = 6 per group, two sections each,
counted blinded. Now recorded.

## What I need next

The single highest-value item is **the source data behind `nilsson2014` Figures 2 and 3** — the
per-animal or per-group values for proliferative chondrocytes per column, resting zone chondrocytes per
mm, and proliferation rate. With those, the yield is computed rather than estimated, and the claim that
oestrogen lowers it becomes tested rather than asserted. That is a request to the corresponding author,
not a paper to download.

Failing that: `lui2018` (PMID 30036371) in full text. It is currently in the atlas at
`primary_abstract_only` and carries the fold-changes and statistics behind the three-pathway senescence
signature, which the `senescence_rate_is_a_regulated_variable` node explicitly records as missing
because that paper was read through a summarisation step.

---

# Round 27 — the yield, computed

The user supplied `lui2018` and asked whether I could recreate the source data from the figures rather
than obtain it. The answer turned out to be better than that: **`lui2018` is PLoS Biology, CC-BY, and
publishes its per-animal raw values as an open supplementary workbook.** No digitisation was needed.
`S1 Data` (s020) downloaded, vendored at `atlas/data/lui2018/` with attribution, and it contains — in
the same mice at the same ages — both terms of the yield:

| term | sheet | units |
|---|---|---|
| calcein-labelled bone growth rate | `Fig1C` | µm/day |
| resting zone cell count | `Fig2B-G` | cells per **500 µm** plate width |

## The construction

A yield is a flux over a flux, so the single-timepoint ratio of two standing stocks — the obvious move,
and the wrong one — would have produced a confident wrong number. Over an interval:

> **yield = µm of bone elongated between t₁ and t₂ ÷ resting zone cells lost between t₁ and t₂**

Physically: take a 500 µm-wide slab of plate. It elongates by *L* µm while its resting zone loses *N*
cells. *L/N* is µm of bone per progenitor. Implemented in `atlas/tools/yield_lui2018.py`; 20,000-resample
bootstrap over animals.

## The result

**The 1–2 week interval is excluded, not down-weighted.** `lui2018` defines the resting zone's upper
margin as the *future* secondary ossification centre at 1 week and as the *lower margin of the actual
SOC* from 2 weeks on. The 50–60 % fall in RZ count across that interval is substantially the SOC
forming, not progenitors being spent — an inflated denominator, which is why all four bones returned a
suspiciously uniform 20–28 there. Dropped.

What survives, over the **same interval, in the same mice, by the same method**:

| bone | interval | grown (µm) | RZ lost | **yield** | 95 % CI |
|---|---|---|---|---|---|
| **metacarpal** — fuses at 2–3 wk | 2–3 wk | 344 | 24.6 | **14** | [12, 18] |
| **femur** — never fuses | 2–3 wk | 1840 | 12.6 | **146** | [110, 208] |
| tibia — never fuses | 2–3 wk | 2042 | 8.3 | 247 | [98, 2774] |
| femur | 3–4 wk | 1494 | 19.0 | 78 | [65, 98] |
| femur | 4–8 wk | 3054 | 13.9 | 219 | [164, 318] |
| tibia | 3–4 wk | 1715 | 9.4 | 183 | [120, 410] |
| tibia | 4–8 wk | 3282 | 22.1 | 148 | [125, 176] |

**A bone about to fuse gets roughly a tenth as much length per progenitor spent as a bone that will
keep growing for months — inside one animal, with non-overlapping confidence intervals.**

The tibia's 2–3 wk interval has a denominator of 8.3 cells and a CI spanning 28-fold; only the femur and
metacarpal rows are tight enough to carry weight. The headline is the femur/metacarpal pair.

## Why it matters

`schrier2006` predicted exactly this shape. Having excluded both observables — oestrogen neither sped
resting zone proliferation nor depleted resting zone number — they proposed **loss of proliferative
capacity per cell cycle**. That is efficiency, and this is the first number this atlas holds that is
consistent with efficiency being the variable: in the run-up to fusion, **growth falls faster than the
pool empties.** Constant-efficiency exhaustion would not look like that.

## What this is not

Recorded on the node as `value_unverified: true` and graded as a re-analysis, per the standing rule that
a re-analysis enters the graph at the grade its data support and no higher. The limits, all carried with
the number:

1. **Net is not gross.** A fall in a standing stock is outflow minus self-renewal, so true consumption is
   at least the denominator used. **Every value here is an upper bound.**
2. **Two separate cohorts.** Calcein and histology animals are not the same mice; numerator and
   denominator are matched by age and bone, not by individual.
3. **Density, not count.** Cells per 500 µm is a density, and the plate widens with age.
4. **Part of the gap is not progenitor efficiency at all.** `lui2018` reports smaller terminal
   hypertrophic cells in the small bones, which lowers µm per division independently of how many
   divisions a progenitor yields. This atlas cannot decompose the two without matched terminal-cell and
   progenitor data in one cohort.
5. **A circularity, stated plainly.** The metacarpal is fusing, so both terms are collapsing, and a low
   ratio partly restates that. The non-trivial content is the *direction*.
6. **Mouse**, and mouse femur and tibia never fuse — their yields are not spend-to-exhaustion curves.

## What changed in the atlas

- `the_exchange_rate_between_growth_and_pool_depletion` — new quantitative row with the computed yields;
  summary rewritten to lead with the number. Node stays at **B**; the row is `value_unverified`.
- `g_l2_raise_the_yield_per_progenitor` — **partially closed.** "Never measured in any species" is still
  true of *measurement* and no longer true of *estimation*. Sub-question (b), whether the yield varies
  between bones, is now answered in the affirmative. **Sub-question (c) — whether anything raises it — is
  untouched and is now the whole gap.** The estimate is observational: it says the yield *differs*, not
  that it can be *moved*.
- `lui2018` — `primary_abstract_only` → `primary`, `full_text_read`, `local_pdf`; note rewritten. The
  transcriptomic fold-changes are still unextracted and that is stated.
- `senescence_rate_is_a_regulated_variable` — the "read through a summarisation step" caveat partly
  retired; the node stays at **C** because its central claim still rests on two culture nulls.
- `atlas/data/lui2018/` — S1 Data vendored under CC-BY with `SOURCE.md` attribution, so the computation
  reproduces without a network fetch.

## The question this now opens

Every intervention this atlas has examined moves pool size or exit rate. The yield varies tenfold
between bones in one animal, which means it is **a real regulated quantity with a large dynamic range** —
and nothing has ever been tested for its effect on it. The next question is no longer *is there a yield*
but **what raises it**, and the cheapest first probe is the one `schrier2006` already handed us:
dexamethasone conserves the pool by slowing exit, so does it preserve yield or spend it? That experiment
needs RZ counts and growth rate in one cohort under dexamethasone — which is `schrier2006`'s design plus
a calcein injection.
