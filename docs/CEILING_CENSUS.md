# The ceiling census — has any human ever grown to a stop without oestrogen?

**Date:** 2026-08-06 · 743 records screened, 45 open-access full texts read, one published
tabulation of every reported male case.

## The answer

**No. Not one.**

At least **twenty people** are documented with complete loss of oestrogen signal or synthesis.
**None has a reported final height reached without intervention.**

| class | people | status at last report |
|---|---|---|
| **ESR1 loss of function** | ≥6 | Smith propositus (male): 204 cm at 28, epiphyses open, bone age 15→17.5 by ~31, **no report since**. Bernard 2017: two sisters + one brother, homozygous R394H, **did not enter puberty, delayed bone maturation**. Brakta 2020: female, followed **8 years** to 24, **75 compounds screened**, DES worked in vitro and **failed in her** over 2.5 years — no height reported. Plus a 13-year-old girl, 2024. |
| **Aromatase deficiency, males** | 14 tabulated | **11 of 14** described at report as tall, with delayed skeletal age, or with **unfused/open epiphyses**. Phenotypes include *"persistent linear growth"*, *"progressive height gain, unfused epiphyses"*, *"progressive increase in height"*. |

**Every one was either given oestrogen — which closes the plate, and in the aromatase cases is
given explicitly to stop growth — or was last seen still growing.**

The verbatim sentence from the 2022 index case, a 24-year-old with undetectable oestradiol and
open wrist and knee epiphyses:

> *"started on oral estradiol valerate for epiphyseal closure to prevent further increase in
> height"*

## Why this is the answer and not an evasion

The question was whether 204 cm is a ceiling. It is not a ceiling — **it is a censoring point.**
The distribution of oestrogen-null final heights has never been observed because the condition is
diagnosed and treated, and the treatment *is* plate closure. The field has been reading a
management decision as a biological limit, and so was this atlas until today.

**Two people could not be treated.** The Smith propositus's receptor is absent — six months of
transdermal oestrogen raising free oestradiol tenfold did nothing. Brakta's patient failed
diethylstilbestrol after 75 compounds were screened against her variant receptor. They are the
only two humans whose growth plates could not be switched off by any available means, and
**neither has a published endpoint.** The Smith propositus would now be in his sixties.

**The single most informative measurement in this field is a number sitting in two sets of
clinical notes.**

## Two things the census turned up that change the therapeutic picture

### 1. The oestrogen-independent route is named, and unresolved

The propositus advanced **2.5 years of bone age in 3.5 chronological years with no functional
ERα.** Something matures the plate without it. Smith & Korach (2010) name four candidates:

- **ERβ**
- **truncated ERα forms** — his mutation is a premature stop in *exon 2*, which permits
  downstream translation initiation
- **non-classical / membrane oestrogen receptors**
- **androgen**, which they single out as *"augmenting both periosteal and epiphyseal growth"*

Sixteen years later none is resolved. **This is the unblocked term.** If ERα blockade is bounded
by its bone cost, the residual route is what still closes the plate in the one person missing the
main one — and nobody knows which of the four it is. Note they are not equivalent hypotheses:
androgen is named as *growth-promoting*, not fusion-promoting.

### 2. The bone cost may not be permanent

Also from Smith & Korach 2010:

> *"estrogen replacement in these individuals, even if provided late in the third decade, may
> normalize aBMD. Less certain is whether there is complete recovery of normal skeletal
> architecture and strength."*

The atlas has been treating **BMD Z −3.85** as the fixed price of the duration lever. If areal
density recovers on late replacement, the price is **temporary** — pay it during growth, recover
it after. That would change the arithmetic of the entire lever class.

**The qualification is the authors' own and is not minor.** Areal BMD is not architecture. The
propositus had cortical thickness 641 µm, trabecular volume 10.6%, trabecular thickness 76.2 µm
and an activation frequency of 0.099/yr — structural deficits a normalised areal density can
conceal. Recorded as a possibility that changes the calculus **if true**, not as a licence.

## What follows

1. **Get the two missing numbers.** Both are chart reviews. The Smith propositus was followed at
   NIEHS and in Cincinnati/Ohio and reported in 1994, 2008 and reviewed in 2010. Brakta's patient
   was followed for 8 years at an academic centre and reported in 2020.
2. **Separate the never-treated subgroup** of the 88-patient Brazilian CYP17D cohort. 51 final
   heights exist; the untreated ones are the distribution nobody has published.
3. **Re-read all 14 male aromatase cases as censored observations** — height at diagnosis, height
   at treatment start, pre-treatment velocity — which converts a set of case reports into a
   survival problem with an estimable endpoint. `query/acquisition/arom_male_table.json` is the
   starting list.
4. **Identify the residual maturation route.** ERβ, truncated ERα, non-classical receptor, or
   androgen. This is now the highest-value mechanistic question in the atlas, because it is the
   term that is still running when the main one is switched off.

Items 1–3 are correspondence and desk work on data that exists. Item 4 is a research programme,
and the human tissue to start it on — Chu's two-month growth-plate explant — is already
characterised.

---

# Part 2 — the analyses, run

## A. Survival on age: sixteen observations, zero events

The intended analysis was a survival curve on **height**. It cannot be done: only **1 of the 14**
tabulated male aromatase cases reports a height in its abstract, and the rest are old, paywalled
case reports. **Ages are recoverable where heights are not.**

Ages at last observation with open epiphyses or ongoing growth:
**17.0, 24.0, 24.0, 24.25, 25.0, 27.0, 27.0, 29.0, 31.5, 37.0 years.**

| | |
|---|---|
| observations | 16 |
| with a recoverable age | 10 |
| **events (spontaneous closure)** | **0** |
| all observations | **right-censored** |
| maximum age with open epiphyses | **37 years** |

**Kaplan-Meier: S(t) = 1.00 at every observed age. Median age at closure: undefined.**

That is the formal statement of the census — *the survival function never falls*. Six of the
sixteen have no recoverable age at all, so 37 years is a floor on what the **literature** contains,
not on what the **clinical records** contain.

## B. The one measured rate, and what it predicts

The Smith propositus is the only person in the entire record with **two bone ages**:

**15 → 17.5 over 3.5 chronological years = 0.71 bone-age years per year — 71% of normal, with no
functional ERα.**

Extrapolating: from bone age 17.5 at ~31.5, he reaches **18 at ~32** and **19 — where male fusion
is typically complete — at ~34**.

> **So even the man whose growth plate could not be switched off was probably within a few years
> of stopping when last seen.** At 204 cm at 28 and a declining terminal velocity of 1–2 cm/yr over
> the remaining five to eight years, **a final height around 208–215 cm follows.**

n=1, two points, and read as an order of magnitude rather than a prediction. **His own numbers say
the rate is not constant** — a lifetime average (bone age 15 at 28) is 0.54 y/y against the 0.71
measured in his late twenties. **The residual maturation appears to accelerate with age**, which is
what an androgen-driven route would do and an intrinsic clock would not.

## C. The residual route: the logic is clean and the data is one point short

|  | ligand | ERα | ERβ / non-classical |
|---|---|---|---|
| **ESR1-null** | present, in excess | **absent** | liganded, functional |
| **Aromatase-null** | **absent** | intact | unliganded |

If residual maturation ran through **ERβ or a non-classical receptor**, the aromatase-deficient man
— who has no ligand at all — should mature **more slowly** than the ESR1-null man. **Matching rates
would exclude every ligand-dependent oestrogen route** and leave androgen or the intrinsic
senescence programme.

**The test needs two bone ages in an aromatase-deficient patient. No published case has them.**
Morishima gives one point (bone age 14 at 24.25); a single point yields no velocity without
assuming when divergence began, and that assumption swings the answer between 0.16 and 0.58 y/y —
which spans the entire question.

**A second bone age in any living aromatase-deficient patient would settle it, and roughly fifteen
are described in the literature.** That is a radiograph.

## What this changes

The honest ceiling is **not unlimited and probably not far above 210 cm** — because removing
oestrogen does not stop skeletal maturation, it slows it to about 71%. The intrinsic programme
runs regardless. **Oestrogen is an accelerator on a clock that ticks anyway.**

Which means the height question resolves into two, and only the second is open:

1. **Slow the accelerator** — oestrogen blockade. Ceiling ≈ +30 cm, threshold-gated, bone cost
   possibly recoverable. *Bounded, and now roughly quantified.*
2. **Slow the clock itself** — the intrinsic, division-dependent senescence programme. **Never
   attempted in any species.** This is where the remaining headroom is, and it is the same
   quantity as the stem-cell budget, the growth fraction, and population asymmetry.

---

# Part 3 — 2026-08-07: five full texts, and the analysis the census said could not be run

Five of the paywalled case reports were supplied and **read in full**. Part 2 concluded that a
survival analysis on height was impossible because the heights were not in the abstracts. **They were
in the bodies.** See CORR-026.

## A. The untreated trajectories

| patient | untreated heights | velocity | bone age |
|---|---|---|---|
| `morishima1995` brother | 170.2 cm @ 14y8m → **204.0 @ 24y3m** | 3.53 cm/yr | ~14 @ 24y3m, **still growing** |
| `carani1997` | 170 @ 18 → 187 @ 31 → **190 @ 38** | **1.31 → 0.43 cm/yr** | 14.8 @ 31, **frozen to 38** |
| `maffei2004` | 172 @ 21 → 177 @ 25 → 183.5 @ 29 | 1.25 → 1.63 cm/yr | 15, **frozen 25→29** |
| `chen2015arom` | 172 @ 20 → 182.5 @ 24 | 2.6 cm/yr | delayed 6–8 y @ 24 |
| `maffei2007` | **191.8 @ 25** | — | 15.3, unfused |
| `baykan2013` | 187 @ 27 | — | 15, open |
| `miedlich2016` | 180 @ 25y2m | — | 15.0 |

**All seven are still censored.** Every one was treated or last seen growing. The conclusion of
Part 1 stands — only the analysis is now possible.

## B. The velocity decays

`carani1997` is the only man followed far enough to show a trajectory rather than a point:

> **1.31 cm/yr from 18 to 31, then 0.43 cm/yr from 31 to 38.**

A threefold fall across two decades in a man whose plates were never closed. Extrapolating from
190 cm at 38 gives a few more centimetres at most. **The duration lever has an asymptote.** One man,
two intervals, and the earlier one includes the tail of his pubertal growth — so this is a shape, not
a curve.

## C. And the deceleration is not the oestrogen clock

This is the part that matters most. In both men with serial bone ages, **bone age did not move at
all** — 14.8 for seven years, 15 for four — while height kept rising and, where followed, kept
slowing.

> **The maturation clock was stopped and the growth slowed anyway.**

Which is exactly what division-dependent depletion predicts and what a pure clock model does not.
**Stopping the clock does not stop the spending.**

## D. Androgen is out

Two men, ~33 patient-months of physiological-to-supraphysiological testosterone, in a background where
none of it can be aromatised:

- `carani1997`: 250 mg enanthate q10d × 6 months → *"His bone age did not change."*
- `maffei2004`: 250 mg q21d ×6mo, then q15d ×8mo, then transdermal 6 mg/d ×13mo → **bone age 15 at
  every phase.**

Meanwhile transdermal oestradiol closed the same two men's plates in **nine** and **six** months.

Of Smith & Korach's four candidates for the residual route, **androgen is eliminated by direct
intervention.** The three that remain — ER-β, truncated ER-α, non-classical receptors — are all
oestrogen-mediated, which is what the ligand-versus-receptor contrast independently predicts:

| condition | ligand | ER-α | bone-age velocity |
|---|---|---|---|
| aromatase deficiency, untreated | **absent** | intact | **≈ 0** |
| ESR1-null (Smith propositus) | present | **absent** | **0.71 /yr** |
| aromatase deficiency + oestradiol | restored | intact | 0.86 – ≥2.1 /yr |

New node `residual_maturation_route_is_oestrogen_dependent` (C). New gap
`g_l7_residual_maturation_route`, whose cheapest step is a **Western blot** for truncated ER-α in the
Smith propositus's archived material — a positive result collapses three candidates into one with no
new patient.
