# Round 25 — the residual route, and two heights the census said did not exist

**Date:** 2026-08-07 · **Branch:** `claude/growth-system-atlas-yl5esl`

Duration is the last open lever. This round went at the two things standing in its way: **what closes
a growth plate when ERα is absent**, and **whether the bone cost can be separated from the growth
benefit.** Both are literature questions. One got a real answer.

---

## 1. The dissociation cannot be bought at the receptor-subtype level

The atlas has been carrying an open therapeutic idea: oestrogen closes the plate *and* builds bone,
so if those two actions ran through different receptors you could block one and keep the other.

`kang2020` was designed for exactly that — the authors state the aim as raising final adult height
without markedly reducing BMD by manipulating binding to each subtype. Ovariectomised rats, ERα-selective
PPT vs ERβ-selective DPN, n=10, 5 weeks:

| | control | PPT (ERα) | DPN (ERβ) | P |
|---|---|---|---|---|
| total body BMD (g/cm²) | 0.121 | **0.146** | 0.124 | **0.003** |
| lumbar BMD (g/cm²) | 0.135 | **0.155** | 0.138 | **0.038** |
| crown–rump length (cm) | 21.0 | 20.44 | 20.94 | 0.083 (ns) |
| plate thickness (µm) | 91.25 | 89.51 | 82.36 | 0.251 (ns) |

**The bone side answered cleanly. The growth side did not answer at all.** BMD is ERα's, twice over.
Neither agonist significantly changed length or plate thickness — a null, in ovariectomised animals
past their fastest growth, over five weeks. And the PPT group is the *shortest* of the three at
P=0.083, a trend in the costly direction.

**The composite conclusion, using this study only for the bone side and human ESR1-null genetics for
the fusion side: both effects point at ERα.** A subtype-selective drug therefore cannot separate them.
Any dissociation has to be **tissue-selective — growth plate versus bone — which is a SERM problem,
not a receptor-subtype problem.** That closes a route the atlas had left open, and it saves the effort.

## 2. ERβ is not eliminated as the residual route, and now I know why

Smith & Korach named four candidates for what advances bone age without ERα: **ERβ, truncated ERα,
non-classical receptors, androgen.** Unresolved for sixteen years. The clean test is whether an
ERβ-null human shows delayed bone age or continued adult growth.

There is exactly one — `langmuritano2018`, a 16-year-old woman with a dominant-negative ESR2 mutation.
**And she has streak gonads.** She makes no oestrogen, so she lacks the *ligand* as well as the
receptor, and any skeletal delay in her is explained without invoking ERβ at all. She was also 16 at
report, far too young for the endpoint. **The elimination test exists and is spoiled by the patient's
own phenotype.** The atlas can now say *why* the question is open, not merely that it is.

---

## 3. Two censored observations recovered — including the first adult growth velocity

The census concluded that a survival analysis on **height** could not be done: only 1 of 14 male
aromatase cases reports a height in its abstract. **The heights are in the full texts.** Two of the
fourteen turned out to be reachable:

**`chen2015arom` (PMC4457386)** — compound heterozygous CYP19A1, untreated:

> **172 cm at age 20 → 182.5 cm at age 24.** Bone age delayed 6–8 years, tibial and fibular epiphyses
> incompletely fused at 24. Oestrogen started at 24.

**10.5 cm over four adult years — a sustained 2.6 cm/year through the whole of the early twenties.**
That is the first measured adult growth velocity in an oestrogen-null man in this atlas, and it is
**higher than the 1–2 cm/yr terminal velocity assumed** when extrapolating a final height for the
Smith propositus. It does not transfer directly — this man is aromatase-deficient, not ERα-null, so
he has an intact receptor and was treatable — but it converts one of the sixteen censored observations
from *an age* into *an age, a height and a rate*.

**`baykan2013` (PMC3701920)** — homozygous R375H: **187 cm at 27, bone age 15, open metacarpal and
phalangeal epiphyses**, treated at 27. A twelve-year bone-age deficit, and then stopped.

---

## 4. Two corrections, both new failure modes

### CORR-024 — a summarisation step got a derived number wrong by 4×

It reported the heights correctly (172 at 20, 182.5 at 24) and in the same answer stated the velocity
as **"10.5 cm/year"**. That is the total gain over four years. The true value is **2.6 cm/year**. At
10.5 it would have implied ~50 cm of remaining growth and corrupted every ceiling estimate downstream.

CORR-023 established that *identifiers* from a summarisation step are unverified data. **This extends
it to arithmetic.** A summarisation step is reliable for **transcription** and unreliable for
**inference**, and the two arrive looking identical. Derived quantities must be recomputed from the
primaries in the same answer; where the primaries are absent, the derived number cannot be used at all.

### CORR-025 — I minted a ref_id that already existed

I created `chen2015` for the aromatase case. That key was already **Chen 2015, PMID 25779879, on
losartan and chondrocyte hypertrophy**, cited by `perichondrial_tgfb_restraint`. YAML resolves
duplicate keys silently to the last, so the file parsed cleanly and that node's citation would have
been **rebound to an unrelated paper** — the same end state as a fabricated citation, by a different
route. Caught by the validator's PMID-mismatch check. Renamed `chen2015arom`; both verified.

---

## 5. Where duration stands

- The ceiling extrapolation (~208–215 cm) still rests on **n=1, two bone ages**.
- The bone-cost dissociation **cannot** be had by receptor subtype. It is a SERM problem.
- The residual fusion route remains **unidentified**, and the one human who could settle it is confounded.
- **12 of the 14 male aromatase case reports remain paywalled**, and their heights are the difference
  between a degenerate survival analysis and a real one.

## 6. Atlas state

634 nodes · 1,226 edges · 313 gaps · 1,129 refs · **0 validator errors**

New refs `kang2020`, `langmuritano2018`, `chen2015arom`, `baykan2013`. Four new rows in
`the_human_ceiling_has_never_been_observed`. Corrections **CORR-024**, **CORR-025**.
