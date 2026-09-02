# F-R097 — The let-7 confound is closed by a 364 kb deletion, the growth-curve shape says pool rather than deadline, and there is a counterexample I am putting at the top

Five papers, and between them they settle the question F-R096 left open, answer the pool question from
curve shape rather than histology, and produce one case that cuts against everything else. **I am
leading with the counterexample.**

---

## 1. The counterexample first

`nihms2079836` — Taliercio et al., University of Utah / Undiagnosed Diseases Network.

A 17-year-old female with clinical Gorlin–Goltz syndrome. Panel, exome and genome sequencing were
non-diagnostic; reanalysis found **a novel de novo paracentric inversion truncating *PTCH1***. That is
an unambiguous *PTCH1* loss-of-function.

**She is short.**

| | |
|---|---|
| height at 7 years | tracking **3rd percentile** |
| **height at 14 y 5 m** | **141.9 cm, z-score −3 SD** |
| bone age at 14 y 5 m | 13 y 6 m |
| GH axis | **normal** — IGF-1 166 ng/mL, IGFBP3 2830 ng/mL |
| thyroid | normal (TSH 1.82, free T4 0.95) |
| puberty | adrenarche present (Tanner 2 pubic hair); **no central puberty — no breast development**, estradiol 3.0 pg/mL |

**A truncating *PTCH1* variant with height at −3 SD.** Every other case in this file goes the other way.

**The confound, which the authors themselves raise:** the same patient carries **a variant of uncertain
significance in *CHD7***, and they explicitly propose **a dual genetic diagnosis**. *CHD7* is the CHARGE
gene, and CHARGE causes short stature and hypogonadotropic hypogonadism. **Her absent central puberty at
14 y 5 m with estradiol 3.0 pg/mL is the hypogonadotropic pattern, not the *PTCH1* pattern** — and
absent puberty by itself suppresses height at that age.

So the case is genuinely confounded. **But it is not nothing: it establishes that *PTCH1* truncation is
not sufficient for tall stature**, and the honest version of our claim has to accommodate it.

---

## 2. The let-7 confound is closed

F-R096 left this open: the 9q22.3 deletions that cause overgrowth also remove **let-7a-1, let-7f-1,
let-7d** in 10 of 11 patients, and the Lin28/let-7 axis is a real human growth and puberty axis
(my own GWAS check: LIN28B, 39 height associations, p<1e-300).

**`ajmg.a.62224` — Ewing et al. 2021 — is the case that separates them.**

| | |
|---|---|
| deletion | **chr9:95,403,395–95,804,680** — *"a 364 Kb deletion"* |
| ***PTCH1*** | **deleted** (gene begins 9:95,442,xxx) |
| ***FANCC*** | **intact** — *"this deletion did not include the FANCC gene"* |
| ***ERCC6L2*** | intact |
| **let-7a-1 / let-7f-1 / let-7d** | at ~chr9:94.18 Mb — **≈1.2 Mb outside the deletion. INTACT.** |

**And he has the overgrowth phenotype:**

| | |
|---|---|
| birth length | 51.5 cm, **75th centile** |
| birth head circumference | 37.7 cm, 99th centile |
| **growth** | ***"His height and weight tracked with the 97th centile for age from age 4 months"*** |
| **height at 16 years** | **184 cm** |
| father / mother | 176 cm / 168 cm |
| **mid-parental predicted height** | **178.5 cm** |
| **excess over prediction** | **+5.5 cm** |
| **puberty at 16** | ***"Puberty is currently well advanced"*** |

**Three things fall out at once.**

1. **The overgrowth occurs with let-7 intact.** *PTCH1* is doing it.
2. **My F-R096 discriminator resolves in favour of *PTCH1*.** I predicted: *let-7 repression delays
   puberty, so if these patients have delayed puberty it is let-7; if puberty is normal it is PTCH1.*
   **Puberty was well advanced.** Not delayed.
3. **Postnatal onset again.** Born at the **75th** centile for length; on the **97th** by four months and
   held it for sixteen years. This is now the third independent case of postnatal-onset overgrowth
   (Yamada's daughter, +0.8 → +2.3 SD; Redon's patient, 95 cm at 2 years; Ewing).

**The magnitude is more modest than F-R096's headline, and I want that on the record:** +5.5 cm over
mid-parental prediction ≈ +0.8 SD, against +2.9 SD in Yamada's mother and +3.4 SD in the Italian
frameshift case. **The honest range for human *PTCH1* haploinsufficiency is roughly +0.8 to +3.4 SD,
with one case at −3 SD that carries a second diagnosis.**

---

## 3. The reciprocal, with numbers

`izumi2011` — familial 9q22.3 **microduplication** spanning *PTCH1*:

| | propositus | sister |
|---|---|---|
| birth length | 44 cm (~25th centile) | birth weight 2.0 kg (<5th) |
| height at 3 y | **92.5 cm (~3rd centile)** | 77.5 cm (<3rd; 50th centile for a 15-month-old) |
| later height | 108.4 cm (~3rd centile) | persistently <3rd centile |
| head circumference | <5th centile | <3rd centile |
| **puberty** | **precocious, treated** | — |

**The complete human dose–response:**

| *PTCH1* copies | Hedgehog tone | stature |
|---|---|---|
| **1** | elevated | **97th centile → +2.9 SD; 184 cm at 16, +5.5 cm over target** |
| 2 | normal | normal |
| **3** | suppressed | **~3rd centile, two family members** |

*(The duplication's precocious puberty is consistent with **both** let-7 gain and *PTCH1* gain, so it does
not discriminate — only Ewing's deletion does.)*

---

## 4. The growth-curve shape answers the pool question without a histology slide

You keep asking for the pool, and this is the closest thing to an answer that human data can give.

**The observation:** Ewing's patient *"tracked with the 97th centile for age from age 4 months"* — for
sixteen years — and finished 5.5 cm above his mid-parental prediction. Yamada's mother: *"overgrowth was
observed **throughout childhood**"*, ending at +2.9 SD at 17. Yamada's daughter: +0.8 SD at birth,
progressively to +2.3 SD by nine.

**Now put that against our own identity,** `dL/dt = flux × v(d)`, with `L∞ ∝ n₀`:

| mechanism | predicted growth curve | matches? |
|---|---|---|
| **raised n₀ (bigger pool)** | more columns → higher dL/dt **at every age** → parallel upward shift held to adult height | **yes** |
| **delayed closure (longer deadline)** | normal childhood height, then **late** divergence as peers stop | **no** — he was 97th centile at four months |
| raised v alone (faster rate) | early divergence, then earlier exhaustion; final height not necessarily raised | partly — but does not explain the tracking held to 16 |

**The human *PTCH1* phenotype is a parallel upward shift of the whole growth curve carried to adult
height. That is the signature of a raised pool, not a delayed deadline.**

This matters because it is the first human evidence that the Hedgehog axis moves `n₀` rather than
merely `v` — and it is consistent with `trompet2024`'s bead, where the exposure ended at three weeks and
the divergence kept widening for five months, which is also an `n₀` signature rather than a rate one.

---

## 5. And the limit it exposes, which is the whole problem

**Every one of these patients stops.** Yamada's mother finished at 173.3 cm. Ewing's patient is 184 cm at
16 with puberty well advanced. Nobody in this literature keeps growing.

**Halving *PTCH1* raises the setpoint and carries it to adult height. It does not remove the deadline.**

So the human genetics now say, cleanly:

- **Hedgehog buys pool.** Confirmed — dose–response, postnatal, persists to adult height.
- **Hedgehog does not buy duration.** No case shows delayed fusion or continued growth.

**"Fast + unlimited + never-closing" is therefore not one lever.** The Hedgehog arm delivers the second
term and possibly the first. **The third term still has to come from somewhere else** — which in this
file means the RARγ/retinoid axis (F-R093, F-R094) or the oestrogen axis (anastrozole), and neither has
yet been shown to add length on its own.

---

## 6. Where the argument stands

**Closed this round:**
- **let-7 vs *PTCH1*** — closed for *PTCH1* by a 364 kb deletion with let-7 1.2 Mb away, and by the
  puberty discriminator resolving as predicted.
- **Pool or rate?** — the growth-curve shape says pool.
- **Reciprocal dosage** — duplication family, ~3rd centile, with numbers.
- **Postnatal window** — now three independent cases.

**Open, and honestly ranked:**
1. **Why is the Utah patient short?** If *CHD7* explains it, fine. If not, *PTCH1* LoF has a bimodal
   height effect and we need to know what splits it. **The F-R095 sterol-sensing-domain hypothesis is
   the obvious candidate and this case can test it** — where does her inversion breakpoint fall relative
   to the SSD (aa 426–616)?
2. **Growth-plate histology in *Ptch1*⁺/⁻ mice** — resting-zone cell number, column count. Unchanged
   from F-R096; the mouse is standard and someone has stained a physis. **This converts §4's inference
   from curve shape into a direct pool measurement.**
3. **Has chronic low-level partial SMO agonism ever been given to a growing animal?** F-R096's central
   proposal, still unfound.
4. **Bone ages in the overgrowth cases.** Redon lists advanced bone age as a general overgrowth-syndrome
   feature; none of these papers reports it for *PTCH1* patients. **If bone age is advanced, the pool
   gain is being partly spent on faster maturation and the ceiling is lower than +2.9 SD suggests.**
5. **Xiu 2022 supplementary** — open since F-R094.

## 7. Asks

1. **Any *Ptch1*⁺/⁻ mouse paper with growth-plate histology or bone length.** These mice are on the
   shelf in a hundred labs; the phenotype is usually reported for tumours, but somebody has measured a
   femur. **This is the single most valuable outstanding item — it turns §4 from inference into
   measurement.**
2. **Bone age or pubertal staging in any 9q22.3-deletion or *PTCH1*-LoF overgrowth patient** (§6.4).
3. **Ewing et al. supplementary figures** — specifically whether they report a growth-velocity curve
   rather than only centile tracking.
4. Still open from earlier rounds: chronic low-dose SMO agonist in a growing animal; Xiu 2022
   supplementary.

---

*The let-7 objection took one patient with a small enough deletion to settle. What I would flag for
myself: I proposed the puberty discriminator last round as a thing to look for, and the case that
resolved it was in the same literature I had already been reading — the discriminating fact was a
deletion boundary, and boundaries are in figures and coordinates rather than abstracts.*
