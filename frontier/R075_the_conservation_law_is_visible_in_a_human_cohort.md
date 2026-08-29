# F-R075 — The conservation law is visible in a human birth cohort, and the HH array data exists but was filtered

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** Supplied HH methylation paper read in full with its four supplementary tables; ALSPAC epigenetic
clock analysis retrieved. **The growth-pacing hypothesis now has human cohort support with the correct
signature, and one specific dataset request that is worth making.**

---

## 1. The supplied paper is the right disease and the wrong analysis — but the data exists

**Suzuki E, Nakabayashi K, Aoto S, Ogata T, Kuroki Y, Miyado M, Fukami M, Matsubara K. "DNA methylation
changes in the genome of patients with hypogonadotropic hypogonadism."**

**Why it is the right population:** hypogonadotropic hypogonadism — including Kallmann syndrome — is
*absent or delayed puberty*, and untreated HH is the classic cause of **eunuchoid proportions from
prolonged epiphyseal opening.** This is the delayed-fusion population F-R074 asked for.

**What they did:** Infinium **MethylationEPIC** BeadChip on **9 patients** (patients 1–9: six *ANOS1*,
one *SOX2*, two *SOX10*) and **12 controls** (eight boys, four adults), peripheral blood; then
pyrosequencing of selected sites in 35 more patients (44 total).

**And why it cannot answer the question as published:**

> *"Probes known to show **aging-related** or sex-biased DNA methylation changes were also **excluded**
> [14–16]."*

**Their reference 14 is Horvath 2013.** **They deliberately removed the epigenetic-clock CpGs before
analysis.** The array measured them; the analysis discarded them.

**Their result, for completeness:** hierarchical clustering did **not** distinguish patients from controls;
they conclude *"most of these changes are likely to be physiological epigenetic polymorphisms, rather than
HH-associated epi-signatures,"* with a possible *ZNF254* promoter hypermethylation signal. **So there is no
HH epi-signature** — which is a clean negative and does not bear on epigenetic age either way.

**The data availability statement is the actionable part:**

> *"The data associated with this study **has not been deposited into a publicly available repository. Data
> will be made available on request**."*

> ### The raw EPIC data for 9 delayed-puberty patients and 12 controls exists and is obtainable by request. **Computing Horvath DNAm age on those IDATs is a laptop-scale reanalysis of data that has already been generated**, and it directly tests whether delayed fusion tracks a delayed clock.

**Two things would have to be requested alongside it, and the paper does not report either:** the patients'
**chronological ages**, and their **androgen treatment status.** Table 1 lists diagnosis, gene, cDNA,
protein and zygosity only. Since this is a paediatric research institute and the controls were *"eight boys
and four adults,"* **the cohort may be too young for the post-20 test** — a child with HH has not yet had
the opportunity to diverge from the normal fusion timeline. **That caveat is why this is worth requesting
rather than assuming.**

---

## 2. The human cohort test — and the answer has the right signature

Rather than wait on that, I looked for the same question already answered at cohort scale.
**It has been.**

**Simpkin AJ et al., "The epigenetic clock and physical development during childhood and adolescence:
longitudinal analysis from a UK birth cohort," *Int J Epidemiol* 2017;46(2):549** — **ALSPAC, n = 1,018**,
methylation measured at **birth, age 7, and age 15–17.**

**The result that matters, and it is a pair of coefficients with opposite signs:**

| epigenetic age acceleration at **age 7**, per 1 year | effect |
|---|---|
| **average height across childhood** | **+0.23 cm** (95% CI 0.04–0.41; **p = 0.018**) |
| **subsequent height growth velocity** | **−0.031 cm/year** (95% CI −0.057 to −0.005; **p = 0.021**) |

> ### A child who is epigenetically **older** at seven is **taller already** and then **grows more slowly afterwards.** That is the budget model made visible: **more of the programme already spent, less remaining.** The two coefficients point in opposite directions from the same variable, and **that opposite-sign pattern is precisely what a spent-capacity model predicts.**

**Why this is not simply confounding.** The obvious confounder is nutrition or socioeconomic advantage —
but a better-nourished child is **taller *and* continues to grow well.** Confounding of that kind produces
**same-sign** coefficients. **The observed pattern is opposite-signed**, which is the signature of a
conserved quantity being drawn down, not of a shared upstream driver.

**The other results, reported in full because they are not all favourable:**

| | finding |
|---|---|
| **age at peak height velocity** | **NULL at all three timepoints** — birth r = 0.006 (p=0.85), age 7 r = 0.014 (p=0.67), age 17 r = 0.014 (p=0.66) |
| Tanner, boys, AA at birth | testes development OR **1.10** (1.01–1.20, p = 0.03) |
| AA at birth → fat mass | **+1,321 g** across childhood (386–2,256; p = 0.006), with **slower** trajectory (−112.5 g/yr, p = 0.007) |
| AA at birth → height | **no association** (0.16 cm, p = 0.19) |

**On the PHV null, which looks like a refutation and is not.** Age at peak height velocity is a **timing**
variable. Growth-pacing says the clock advances with **growth accomplished**, a **cumulative** quantity. Two
children can reach peak velocity at different ages having accumulated the same total growth — the
hypothesis makes no prediction about when the peak occurs. **The cumulative variable (height attained) is
associated; the timing variable is not. That is the expected pattern, not a contradiction** — though I note
that this is an argument I am making, not one the authors make.

**And note the fat-mass result has the same opposite-sign structure** (higher average, slower trajectory),
which suggests the pattern may be a general property of epigenetic age acceleration in childhood rather
than something skeletal-specific. **That weakens the growth-plate-specific reading and I am flagging it
rather than burying it.**

---

## 3. Where this leaves the pacing law

F-R066 proposed it, F-R071 corrected it (cost per division is modulable, not fixed), F-R074 found the
Horvath clock's logarithmic childhood transformation consistent with it. **This round adds human cohort
data with the discriminating signature.**

| evidence | strength |
|---|---|
| Lui: tryptophan restriction **delayed the programme** — *"driven by body growth itself rather than age"* | **direct experimental, rat, multi-organ** |
| Horvath clock is **logarithmic below 20, linear above**; tick rate "exponential between 0 and 20" | **fitted empirical necessity**, shape correspondence only |
| **ALSPAC: epigenetically older at 7 → taller now, slower after** | **human, n=1,018, opposite-sign, p≈0.02 both** |
| ALSPAC: age at PHV null | expected — timing vs cumulative, but an argument of mine |
| ALSPAC: fat mass shows the same pattern | **weakens skeletal specificity** |

> **The pacing law is now supported in three independent ways — a direct rat experiment, the internal structure of the standard human clock, and a human birth cohort with the correct opposite-sign signature.** It remains an association in humans, in blood, with small effect sizes, and with a non-skeletal analogue that argues against specificity. **Supported, not proven.**

---

## 4. What I need

**One request, and it is specific enough to be actionable:**

**Raw Infinium MethylationEPIC data (IDAT files or the pre-filtering β matrix) from Suzuki et al.**, for the
9 HH patients and 12 controls — **together with each subject's chronological age and androgen treatment
status**, neither of which the paper reports. **The corresponding authors are Maki Fukami and Keiko
Matsubara, National Research Institute for Child Health and Development, Tokyo**, and the paper states data
are available on request.

**Why it is worth the request:** the aging probes were excluded analytically, not at the assay level, so
**the clock CpGs are present in the raw data.** Computing Horvath or Skin-&-Blood DNAm age on 21 existing
samples would directly test whether delayed fusion tracks a delayed clock — **the question that has been
the crux since F-R066** — with no new sample collection.

**Its known weakness, stated up front so the request is honest:** if the patients are pre-pubertal
children, they have not yet had the chance to diverge from the normal fusion timeline and the test will be
underpowered. **The ages are the first thing to ask for**, and they determine whether the rest is worth
pursuing.
