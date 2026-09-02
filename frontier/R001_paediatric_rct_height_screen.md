# F-R001 — the paediatric RCT height screen

**A randomised, human, BIDIRECTIONAL height instrument. It validates on this atlas's own positive
control, it gives the field its first measured base rate, and it closes `g_l12_457c` with human data
that runs against the cAMP arm.**

Date: 2026-08-27 · branch `claude/height-enhancement-research-v34b4r` · code and tables in
`frontier/screens/ctg_paediatric_rct/`

---

## 0. Why this instrument, and why now

This repository's structural negatives are all statements about **instruments**:

| round | instrument | why it cannot find a height-raising lever |
|---|---|---|
| R298 / CORR-347 | Open Targets "known drugs" | lists clinical agents only; the plate's targets are matrix, channels and secreted modulators |
| R437 | FAERS disproportionality (20.7 M reports) | **"getting taller is not an adverse event"** — the favourable direction is structurally blind |
| R457 / CORR-350 | Drugs@FDA + EPAR juvenile toxicity | **"a juvenile toxicity package is an adverse-findings document"** — same blindness, different corpus |
| CORR-295 | PubMed / disease literature | short stature brings a child to clinic; tall stature does not. Syndrome genes are 5× more likely to shorten than lengthen |
| CORR-358 | rare-variant burden tests | cannot contain a recessive; `bartell2026` has zero chrX rows |

Four of the five fail in **the same direction**: they see harm and not benefit. The atlas has
correctly concluded, four separate times, that its instruments are one-sided — and has not had an
instrument that is two-sided.

**A continuous height outcome in a randomised trial is two-sided.** Every long-term paediatric drug
trial records height as a safety variable, at scheduled visits, against a randomised concurrent
control, and posts the arm-level numbers. A drug that makes children taller is exactly as visible in
that table as one that makes them shorter. Nothing else in the atlas's instrument set has that
property.

### And this repository already knew

`docs/acquisition_sweep_round18.md`, 2026-08-06, §2.2, verbatim:

> **678** trials carry a genuine stature/length endpoint … **506** of those have **results posted**.
> All 506 full records downloaded. **269** of those are **in children, on an intervention that is
> not already a growth drug** — i.e. **natural experiments on human height that nobody has
> aggregated.** Extraction produced **5,445 arm-level height numbers**.

`query/acquisition/ctg_measures.csv`, 5,445 rows, has been on disk for 459 rounds.
`grep -rn "ctg_measures" atlas docs query CLAUDE.md` returns **three hits: two inside
`atlas/tools/ctg_extract.py`, the script that wrote the file, and one inside the R18 sweep document
that announced it.** Zero in any node, zero in any gap, zero in `CLAUDE.md`. R18's own §3 and §4
findings are about the *expression*-data hole and about `chu2025` — the trial corpus was acquired,
described as unaggregated, and never aggregated.
That is CORR-328 verbatim — *writing "no data exists" without querying the bulk datasets you already
have* — and this is its largest instance in the file.

---

## 1. Method

Re-harvested rather than re-used, because the registry has moved since 2026-08-06 and because the
R18 query set was five hand-written expressions.

1. **Harvest.** ClinicalTrials.gov v2 API, `aggFilters=results:with`, thirteen
   `AREA[OutcomeMeasureTitle]` terms (height, stature, growth velocity, height velocity, height SDS,
   height z-score, linear growth, body length, growth rate, final height, adult height, height
   percentile, height standard deviation). **841 unique studies** with results posted and a
   height-like outcome title — a superset of R18's 506.
2. **Filter.** Interventional · `allocation: RANDOMIZED` · `stdAges` includes CHILD or ADOLESCENT ·
   at least one DRUG / BIOLOGICAL / DIETARY_SUPPLEMENT / COMBINATION_PRODUCT intervention.
3. **Outcome selection.** Outcome title matches a height/stature/body-length/growth-velocity pattern
   **and** a change pattern (`change|velocity|rate of|gain`), and does not match the noise pattern
   (peak height of a wave, fundal height, jump height, weight-for-height, BMI, blood-pressure
   percentile-for-height, participant counts). Categories whose label contains "baseline" are
   dropped — an absolute height reported under a "change from baseline" title is the single largest
   source of spurious effects in this corpus and it produced four of the top five hits before it was
   filtered.
4. **Contrast.** Within each outcome category, the reference arm is the largest arm whose title
   matches `placebo|control|vehicle|comparator|standard of care|no treatment|observation|untreated|
   usual care|sham`, excluding arms that are themselves growth-active. Every other arm with n ≥ 10
   is contrasted against it.
5. **Statistics.** SE of the difference from the posted dispersion, honouring `dispersionType`:
   `√(SE₁²+SE₂²)` for standard errors, `√(SD₁²/n₁+SD₂²/n₂)` for standard deviations. Two-sided
   normal p. **These are approximations** — LS means from one model are correlated, so the SE is
   conservative if the correlation is positive — and they are reported as screening statistics, not
   as the trial's inference.
6. **Labels, not exclusions.** Each contrast is tagged `growthdrug` (the arm is a known growth
   agent), `growthdx` (the indication is a growth disorder) and `restore` (the indication is a
   deficit state, so any effect is restoration and CORR-203 governs). Nothing is silently dropped.

### Positive controls, run before reading any result

**External** — the atlas's own hand-read value. R18 required its extractor to reproduce
NCT00429364's `Annual Rate of Change in Height`. This one does, independently:

> **RECOVERED: Losartan = 0.935 vs Atenolol = 0.822 cm/yr.** Matches the value already in this atlas.

**Internal** — the instrument must recover the agents that are *known* to raise height. It does:

| stratum | unit | n | median | positive |
|---|---|---:|---:|---|
| **growth drugs / growth diagnoses** | cm | 37 | **+0.99** | **35/37 (95%)** |
| **growth drugs / growth diagnoses** | cm/yr | 23 | **+1.07** | 17/23 (74%) |
| **growth drugs / growth diagnoses** | height-Z | 11 | **+0.30** | **11/11 (100%)** |

An instrument that returns 95–100% positive on the agents this atlas grades A for raising height,
from an unfiltered registry scrape, is measuring what it claims to measure.

---

## 2. THE BASE RATE — the number this field has never had

CORR-329 is the rule: *in any screen where one direction dominates, only the rare direction is
informative* — and the atlas has that number for IMPC knockouts (63.7% shorter) and for nothing
else. **Here it is for drugs, in humans, randomised.**

153 arm-vs-control contrasts from **42 randomised paediatric trials**; 82 contrasts from 28 trials
after removing growth drugs and growth diagnoses.

| unit | stratum | n | median | positive |
|---|---|---:|---:|---|
| **cm** | all | 77 | +0.30 | 51/77 (66%) |
| **cm** | **non-growth drug, non-growth diagnosis** | 40 | **−0.01** | 16/40 (40%) |
| **cm** | …and non-deficit indication | 27 | **−0.11** | **6/27 (22%)** |
| **cm/yr** | all | 38 | +0.20 | 22/38 (58%) |
| **cm/yr** | **non-growth drug, non-growth diagnosis** | 15 | **−0.27** | 5/15 (33%) |
| **cm/yr** | …and non-deficit indication | 12 | **−0.24** | 4/12 (33%) |
| **height-Z** | non-growth drug, non-growth diagnosis | 27 | +0.02 | 16/27 (59%) |

> **Read a candidate against this.** A drug given to a growing child for a reason unrelated to growth
> has a median effect on linear growth of about **−0.25 cm/yr**, and only **22%** of contrasts in a
> normal (non-deficit) indication are positive at all. **A +0.2 cm/yr signal is the 70th percentile
> of noise in this corpus, not a lever.** Any future proposal in this repository that rests on a
> sub-half-centimetre-per-year human signal now has a null distribution to be scored against, and it
> did not before.

**And the two-sided instrument comes back one-sided anyway.** This was built specifically because
FAERS and the juvenile-toxicity packages can only see harm. This corpus *can* see benefit — it
proves it on the internal positive control — and among 27 non-deficit contrasts it returns **six
positives, none significant, none mechanistically coherent**. That is a fourth structural negative,
and it is the strongest of the four, because for the first time the blindness is not in the
instrument.

---

## 3. Every significant contrast, signed

p < 0.05, excluding growth drugs and growth diagnoses, of 77 contrasts with computable p:

| Δ | unit | z | p | trial | n | indication | arm vs control |
|---:|---|---:|---:|---|---|---|---|
| **−1.70** | cm | −2.17 | **0.030** | NCT04175600 | 59/64 | pulmonary hypertension | **selexipag** vs placebo, wk 96 |
| −1.10 | cm | −2.72 | 0.007 | NCT00000575 | 311/418 | asthma (CAMP) | budesonide vs placebo, 4–6 y |
| −0.44 | cm/yr | −2.55 | 0.011 | NCT00449072 | 134/133 | perennial allergic rhinitis | triamcinolone acetonide aq vs placebo |
| −0.30 | cm | −3.05 | 0.002 | NCT02075047 | 86/85 | bipolar disorder | **ziprasidone** vs placebo |
| +0.38 | cm | +2.89 | 0.004 | NCT04753697 | 225/115 | eosinophilic oesophagitis | CC-93538 vs placebo *(deficit)* |
| +0.30 | cm | +2.12 | 0.034 | NCT02514473 | 98/97 | cystic fibrosis | lumacaftor/ivacaftor vs placebo *(deficit)* |
| +1.12 | Z | +2.99 | 0.003 | NCT02915705 | 22/22 | X-linked hypophosphataemia | burosumab vs active control *(deficit)* |
| +1.03 | Z | +2.15 | 0.031 | NCT02915705 | 22/22 | XLH | burosumab, growth-velocity Z, wk 40 *(deficit)* |
| +0.15 | Z | +2.01 | 0.045 | NCT02915705 | 28/32 | XLH | burosumab, height-for-age Z *(deficit)* |
| +0.13 | Z | +2.15 | 0.032 | NCT02915705 | 28/32 | XLH | burosumab, height-for-age Z, wk 40 *(deficit)* |

**Every significant positive is a deficit correction.** Burosumab restores phosphate in XLH,
lumacaftor/ivacaftor restores CFTR, CC-93538 removes an inflammatory brake in eosinophilic
oesophagitis. CORR-203 governs all four: a result from a deficient system is a claim about the
deficit. **Not one significant positive is an elevation of a normal plate.**

**Two of the four significant negatives are already in this atlas** — budesonide (this file holds
−1.2 cm for inhaled budesonide; the screen returns −1.1 cm from CAMP independently) and the
intranasal corticosteroid class. That is a third validation, arrived at without being told to look.

---

## 4. ⭐ THE FINDING — selexipag, and it closes `g_l12_457c`

R457, twelve rounds ago, on the FDA nonclinical review:

> **SELEXIPAG** (prostacyclin IP agonist): by 39 weeks, **2 of 3 low-dose and ALL mid- and high-dose
> males had increased ossification of the femoral shaft**, with delayed sexual maturation in both
> sexes and physes still open. The review's "no treatment-related effects on growth" refers to
> **body size**. **CORR-340 in its purest form — nine months of dosing in a large animal with open
> physes, and the missing measurement is a pair of calipers.** `g_l12_457c`

**The calipers exist. They are human, randomised, double-blind and placebo-controlled.**

`NCT04175600` — phase 3, randomised, double-blind, placebo-controlled, parallel-group, selexipag as
add-on to standard of care in paediatric pulmonary arterial hypertension, **ages 2–17**, n = 138
enrolled, 59 selexipag / 64 placebo in the double-blind period. Change from baseline in growth
parameter: **height**, LS means ± SE, a prespecified secondary outcome:

| week | placebo | selexipag | Δ | SE | z | p |
|---:|---:|---:|---:|---:|---:|---:|
| 24 | +1.9 ± 0.51 | +1.1 ± 0.52 | −0.8 | 0.73 | −1.10 | 0.272 |
| 48 | +3.8 ± 0.51 | +2.8 ± 0.53 | −1.0 | 0.74 | −1.36 | 0.174 |
| 72 | +5.8 ± 0.52 | +4.4 ± 0.54 | −1.4 | 0.75 | −1.87 | 0.062 |
| **96** | **+7.3 ± 0.54** | **+5.6 ± 0.57** | **−1.7** | **0.79** | **−2.17** | **0.030** |

**Monotone, growing, and significant by two years: −0.8 → −1.0 → −1.4 → −1.7 cm.** An implied
velocity deficit of **−0.92 cm/yr** sustained over 96 weeks. A rate effect that shrinks as a
fraction would not do this; a sustained reduction in growth rate is exactly this shape — the same
reasoning R285/R293 used, in the opposite direction, to promote `haraguchi2025`.

### ⛔ The confound, stated first because it is large

**Body weight moved further than height and earlier.**

| week | placebo | selexipag | Δ kg | z | p |
|---:|---:|---:|---:|---:|---:|
| 48 | +2.5 ± 0.60 | +0.3 ± 0.63 | −2.2 | −2.53 | 0.011 |
| 72 | +4.5 ± 0.62 | +0.5 ± 0.65 | **−4.0** | **−4.45** | **1×10⁻⁵** |
| 96 | +5.4 ± 0.65 | +1.7 ± 0.69 | −3.7 | −3.90 | 9×10⁻⁵ |

Selexipag's characteristic adverse effects are nausea, vomiting, diarrhoea and headache. **The
weight signal is larger, earlier and far more significant than the height signal, which is the
signature of a nutritional mechanism, not a physeal one.** `campion2022tofacitinib`'s rule — read
length against weight — applies with full force here. This is **not** established as a direct
growth-plate effect and is not written as one.

### Why it matters anyway, and it matters twice

**① It is the caliper R457 asked for, and it is in the right species.** The rat and dog studies gave
chondroid dysplasia and increased femoral-shaft ossification with no length endpoint. The human
randomised length endpoint exists and it is negative. `g_l12_457c` can be closed as *measured in
humans, negative, with a weight confound that prevents attribution to the plate* — which is a
strictly better state than "nobody has measured it."

**② It is a human randomised counterweight on the cAMP arm, and this file has none.** The cAMP arm
is live here: CORR-330 reinstated PDE3 as an *independent* handle on cAMP after `hirota2022` showed
PDE3 is not in CNP's chain, and CORR-333 records `kawabe2025` — cilostazol 10 mg/kg/day IP × 4 wk
in juvenile **wild-type** mice, naso-anal **93.6 → 95.3 mm**. Selexipag is an IP-receptor agonist:
Gs → adenylyl cyclase → cAMP. **Two cAMP-raising agents with a length endpoint, and they disagree
by species and by sign:**

| agent | route to cAMP | species | length |
|---|---|---|---|
| cilostazol (`kawabe2025`) | PDE3 inhibition — blocks degradation | juvenile WT mouse | **+1.8% naso-anal** |
| **selexipag (NCT04175600)** | **IP agonism — drives production** | **human children, RCT, 96 wk** | **−1.7 cm (p=0.030)** |

The atlas's own CORR-300 predicts the sign of this disagreement before the data is read: *flooding
with an agonist* is the category that saturates a pathway and subtracts length, while a modulator
that shifts a set point inside a feedback-regulated envelope adds it. **Blocking degradation is the
set-point manoeuvre; agonist flooding is not.** Selexipag is CORR-300's third category and it
behaves like CORR-300's third category. That is a prediction this file made and did not know it had
tested.

⚠ Grade **C**. Human, randomised, prespecified secondary outcome, monotone across four timepoints —
but a single trial, in a disease population with a cardiopulmonary limitation on growth, with a
weight confound larger than the effect. It is not evidence that raising cAMP shortens a normal
plate. It is evidence that **the one human randomised test of an agonist-flooding cAMP agent with a
height endpoint is negative**, which is the strongest statement the record supports.

---

## 5. Second finding — the per-person cumulative lengthening figure the SCALE section does not have

Not from the screen; from a grep that returned zero. `repeat lengthening`, `serial lengthening` and
`total lengthening` return **0, 0 and 3** files in this repository, and the three are incidental.
The SCALE section prices distraction osteogenesis at **6.7 cm in one segment** (`giorgino2025`,
`marwan2020`, adults, aesthetic indication) and **12.4 cm across four segments in one session**
(`shabtai2021`, R418). Both are **per-episode** numbers. **There is no per-person lifetime figure
anywhere in this file.**

**`PMID 40101878`** (Bone, 2025; not in `bibliography.yaml`, verified absent) — the largest
international survey of limb lengthening in achondroplasia, 467 respondents across 16 countries and
11 languages, 90 (19.3%) underwent lengthening:

> mean age at first surgery **10.5 y (SD 4.5)** · on average **3.7 (SD 2.9) procedures** ·
> **14.5 cm (SD 10.4) added** · final adult height 137.1 cm female, 142.1 cm male ·
> **23% would recommend it, 28% would not, 49% uncertain**

- **14.5 cm mean per person, and the SD of 10.4 puts the upper tail near 25 cm.** A 2026 case report
  (`PMID 42131679`) documents **17 cm** of lower-limb lengthening in one woman with achondroplasia.
- **That is not one procedure. It is 3.7.** R418 corrected the field's 6.7 cm from a *convention*
  to a *ceiling* by finding simultaneous four-segment work; this extends the same correction one
  level further — the real-world practice is **staged and repeated**, and the atlas has priced only
  a single episode of it.
- ⛔ **The number is self-reported, in achondroplasia, from a survey with obvious selection.** The
  soft-tissue envelope caveat R418 already records applies with more force across repeated rounds,
  and the recommendation split (23/28/49) is the patient-experience result, not a footnote.

**Against the whole pharmacological stack at 1–3 cm, and against the duration lever's genetic
ceiling of +25 to +28 cm, the surgical route's per-person mean is 14.5 cm and its documented tail
reaches the same order as the genetic ceiling.** No drug proposal in this file should be ranked
without that number visible.

---

## 6. What the screen does NOT establish, listed so nobody overreads it

- **It sees only placebo/control-named arms.** 339 of 529 contrasts in the wider harvest are
  active-comparator; those are in `results_all_contrasts.csv` and are **not** in the base rate. The
  atlas's own losartan positive control is one of them.
- **It sees only trials that posted results in a machine-readable outcome table.** Height recorded
  and published only in a paper is invisible. R18's 678-vs-506 split is the visible part of that.
- **n is small where it matters.** Twelve non-deficit cm/yr contrasts is a base rate with wide
  uncertainty; treat the *direction* as established and the *magnitude* as provisional.
- **Absolute-height outcomes were dropped, not differenced.** Trials reporting height at baseline
  and at follow-up as separate categories under an absolute-value title can yield a within-arm
  change; that extraction is not written. It is the single cheapest extension and would roughly
  double n. → `frontier/ASKS.md` item 5.
- **No multiplicity correction.** With 77 computable p-values, ~4 significant results are expected
  at α = 0.05 by chance; ten were observed, six of them a coherent deficit-correction cluster in
  four trials. Selexipag survives on shape (monotone across four timepoints) rather than on p alone,
  and that is the claim being made for it.
- **Nothing here is a recommendation to take or avoid a drug.** The negatives are watch-items of the
  same class as R477's tetracycline note: free to ask about, free to substitute.

## 7. Reproduce it

```bash
cd frontier/screens/ctg_paediatric_rct
python3 ctg_harvest.py     # 841 studies from the CTG v2 API into ctg_raw/studies.json
python3 screen3.py         # randomised + placebo-controlled contrasts, base rates, p-values
python3 screen2.py         # all-pairs mode; recovers the losartan/atenolol positive control
```
`results_randomised_placebo_controlled.csv` (153 contrasts) and `results_all_contrasts.csv`
(529 contrasts) are committed.
