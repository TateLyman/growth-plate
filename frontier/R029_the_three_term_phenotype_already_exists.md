# F-R029 — The three-term phenotype already exists in humans, and I had two conclusions wrong

Two corrections to my own rounds, then the finding.

---

## 1. Correction to F-R027: the load-bearing assumption is not untested. It is demonstrated.

F-R027 said the whole framework rests on an untested claim — *"recruitment has never been shown to
exceed the set point; everything demonstrated is homeostatic restoration."*

**I already had the paper that refutes that and had read it twice without extracting the sentence.**
`trompet2024` (Trompet D et al., *Stimulation of skeletal stem cells in the growth plate promotes
linear bone growth*, **JCI Insight 2024;9(6):e165226**, PMID 38516888 — open access; I pulled the
manuscript PDF this round and archived it):

> "Here, we used an alternative approach that **enhanced the number of stem cells, which subsequently
> converted into the leg length outgrowth, thus demonstrating that the GROWTH POTENTIAL CAN BE
> IMPROVED by the increased number of stem cells.**"

Not a rescue. Not homeostasis. **Normal rats, contralateral internal control, one leg made longer than
the other and the gap widening at 2 and 6 months.** F-R027's assumption is met.

**And the mechanism is the one this branch derived independently.** Their Figure 3 is titled *"SAG
administration expands the growth plate skeletal stem cell pool and **creates a Wnt-inhibitory
environment**"*:

- **A six-day systemic SAG pulse (P30–P36) increased Pthrp-mCherry⁺ resting-zone stem cells by 61%.**
- RNA-seq: *"**Wnt signaling pathway was among the top 2 downregulated pathways**."*
- Their reading: *"the activation of Hh pathway creates a Wnt-inhibitory microenvironment, **which was
  recently reported to be permissive for these epiphyseal stem cells**"* — and the citation is
  `hallett2021`, the exact paper F-R017 built the Wnt-inhibitory-niche argument on.

**Hh → Wnt-inhibitory niche → stem-cell retention → pool +61% → length.** F-R017 reached that through
oxygen and Frzb/Dkk1; `trompet2024` reached it through Hedgehog. **Two routes into the same niche, and
they close the loop on each other.**

One honest note: the same paper reports that the *systemic* 6-day pulse gave **no length change**
(tibia p=0.29, femur p=0.247) — but that was measured **two days after the pulse ended**, far too soon
to convert pool into bone. It is a timing result, not a systemic-versus-local result, and I will not
use it as one.

---

## 2. Correction to F-R025: serum IGF-1 is a bad proxy for drive, and I built a conclusion on it

F-R025 concluded **"the drive is not endocrine"** from `smith2008`'s IGF-1 of 528 ng/ml against a
reference range of 123–465. I called that *supranormal*. **It is 1.14× the upper limit of normal.**

Against that, the Endotext illustrative case of pituitary gigantism: **growth velocity 19 cm/year**,
with **IGF-1 720 ng/ml against a normal range of 123–701 — 1.03× the upper limit.**

> **A gigantism patient at 1.03× ULN grew 19 cm/yr. An ESR1-null man at 1.14× ULN grew 0.3 cm/yr.**
> **Serum IGF-1 does not measure the drive.** GH pulse amplitude, local IGF-1 production in the plate,
> and receptor signalling all sit between the tumour and the tissue, and the venous number sees none
> of them.

**F-R025's conclusion survives in a narrower form and fails in its general form.** Narrow form, still
true: *a normal endocrine axis, however far toward the top of its range, does not restore adult growth
velocity.* General form, now false: *the endocrine axis is not a lever.* At tumoral output it is the
largest lever ever documented — §3.

---

## 3. The three-term phenotype exists, has occurred repeatedly, and is described in one sentence of the
standard literature

> **"When GH hypersecretion is accompanied by gonadotropin deficiency, accelerated linear growth may
> persist for DECADES."** — the standard description of pituitary gigantism

That is all three terms at once:

| the goal | how gigantism-with-hypogonadism supplies it |
|---|---|
| **never closes** | gonadotropin deficiency → no sex steroid → no oestrogen-driven fusion. The same term A as `smith2008`, reached from upstream. |
| **constant** | *"may persist for decades"* |
| **fast** | tumoral GH/IGF-1 output — velocities up to **19 cm/yr** |

### And the growth curve of the tallest documented case says the quiet part

**Robert Wadlow** — pituitary hyperplasia from age 2, no puberty, 271.8 cm at death at 22:

| age | height | interval velocity |
|---|---|---|
| 8 | 183 cm | |
| 10 | 196 cm | ~6.5 cm/yr |
| 13 | 224 cm | **9.3 cm/yr** |
| ~21 (Feb 1939, Washington University, barefoot) | 265 cm | **5.1 cm/yr** |
| 22 (27 June 1940, final measurement) | **272 cm** | **~5.2 cm/yr** |

> **From 13 to 22 — nine years — he grew at approximately 5 cm/yr with no detectable deceleration.
> His velocity in the final year equalled his velocity across the preceding eight.**

Against `maffei2004`'s 1.3 cm/yr and `smith2008`'s 0.3 cm/yr in the same age band, **that is a four- to
seventeen-fold difference, sustained, in a human, for nine years, in a plate that could not close.**

**He did not stop. He died** — of an infected blister from a leg brace, at 22, still growing.

### Which means both natural experiments have the same missing endpoint

- **Aromatase/ESR1 census** (F-R024): 743 records, 20 people, *"NOT ONE has a reported final height"*
  without intervention — because clinicians closed them.
- **Pituitary gigantism with hypogonadism**: *"may persist for decades"* — and the recorded cases
  either died of the tumour and its complications, or were treated to stop it.

> **Both human phenotypes that satisfy all three terms have existed. Neither has ever been permitted,
> or survived long enough, to reach an endpoint. The ceiling on human height has never been observed
> in either population.**

---

## 4. What this does to the model

F-R027's balance holds, with drive entering as a coefficient rather than a separate term:

```
dH/dt      =  DRIVE  ×  pool  ×  λ  ×  h_term
d(pool)/dt =  inflow(recruitment, self-renewal)  −  outflow(DRIVE, pool)
```

**Drive multiplies both terms.** It raises velocity *and* accelerates depletion — which is exactly
`PMC12685065`'s finding that **GH depletes the resting-zone stem pool by driving committed division.**

That predicts the shape of every case:

| | drive | closure | pool | observed |
|---|---|---|---|---|
| gigantism child | tumoral | blocked | fresh | **19 cm/yr** |
| **Wadlow, 13→22** | **tumoral** | **blocked** | **being spent for 20 years** | **~5 cm/yr, flat for nine years** |
| oestrogen-null adult | physiological | blocked | spent for ~25 y | **0.3–1.3 cm/yr** |
| normal adult | physiological | fused | spent | 0 |

**Wadlow's flat nine-year curve is the anomaly worth staring at.** Under a pure spend model, maximal
drive on a finite pool should decelerate visibly across nine years. It did not. Either the pool was far
larger than the aromatase cases suggest, or **high drive recruits as well as spends** — which is
precisely what `trompet2024` shows Hedgehog doing (+61% pool), and `rosellodiez2025` shows the
perichondrium doing on demand.

**That is the single most important open question in this project now**, and it is answerable from
existing case material rather than new experiments: **do adults with untreated gigantism plus
hypogonadism decelerate, or hold velocity?**

---

## 5. Asks

**#1 — untreated adult gigantism growth curves.** Serial heights in patients with GH excess **and**
hypogonadism, followed **untreated** into the third decade or beyond. Search terms that would work:
*gigantism untreated adult continued growth serial height*, *acrogigantism hypogonadism growth
velocity adult*, *X-LAG untreated final height*. The **AIP** and **X-LAG (GPR101 duplication)**
cohorts are the modern, genetically defined gigantism populations and have systematic follow-up —
a review of those is where the deceleration-or-not answer lives.

**#2 — the Wadlow measurements from a primary source.** His serial heights were taken by physicians at
Washington University; the 1939 measurement is cited to them. **A published clinical account would
turn a table I assembled from secondary sources into data.** (Charles Humberd examined him in 1936 and
published; that account is the primary record.)

**#3 — `trompet2024`'s Figure 5 source data** — the actual millimetres of leg-length difference at 1, 2
and 6 months. The paper is open access at `insight.jci.org/articles/view/165226`; the figures carry the
numbers and I have only the text. **This is the effect size of the only intervention that has ever
made a normal mammal's bone supranormally long by pool expansion.**

**Still standing:** the Safranin-O on `carroll2018`; the Leiden group's citation; Brighton thesis
(UIC ILL `10027/14248`); JBJS 1980;62A:740; Surgical Forum 1970:465–467; `stegen2019` DCA+BPTES tibia
length; the lateral thoracolumbar film.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
The instrument here was a tape measure at Washington University in February 1939 and again in June
1940, and the two readings differ by seven centimetres in a twenty-one-year-old. Every argument in this
branch about whether adult growth is possible was settled before any of the papers in it were written.*

---

## 6. Atlas coverage

| term | files |
|---|---|
| `pituitary gigantism` | 27 |
| `GPR101` / `X-LAG` / `AIP` | 26 / 18 / 98 |
| **`gonadotropin deficiency`** | **3** |
| **`Wadlow`** | **0** |
| **`Humberd`** | **0** |

**The atlas holds the gigantism genetics thoroughly and the combination barely at all.** `AIP` in 98
files is a somatotroph-adenoma gene; `gonadotropin deficiency` in 3 is the term that makes the growth
*continue*. **The conjunction — GH excess AND hypogonadism, which is the entire three-term phenotype —
is not a concept anywhere in the graph**, and the single best-documented human instance of it has no
entry at all.
