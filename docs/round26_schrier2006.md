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
