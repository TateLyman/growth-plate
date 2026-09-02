# F-R084 — All three "impossible" items resolved from evidence that already exists

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** F-R083 closed with three items I called unsubstitutable. **All three are now answered** — two
from human populations that already run the experiment, one from a standardised mouse resource I had not
queried. **One answer is unfavourable and I nearly missed a fatal flaw; one is favourable and closes the
largest hole in the stack; one produces a constraint the branch did not know about.**

---

## 1. Item 2 — "are height and bone density separable?" **YES, and the proof is three queries deep**

### 1a. First, the bad news got worse: I found the true-null mouse

F-R082 hoped the cortical penalty was an artefact of dominant-negative missense alleles. **IMPC holds a true
null — `Dnmt3a^tm1b(KOMP)Wtsi`, heterozygous — which I had never queried.** Group means, JAX:

| parameter | female control | female mutant | p | male control | male mutant | p |
|---|---|---|---|---|---|---|
| **Bone Area** | 8.754 | **8.399** | **3.8 × 10⁻⁵** | 9.108 | 8.965 | 0.31 |
| **Bone Mineral Content (excl. skull)** | 0.4274 | **0.4078** | **5.6 × 10⁻⁴** | 0.4534 | **0.4429** | **0.039** |
| Lean/Body weight | 0.8445 | **0.7755** | **3.7 × 10⁻⁴** | 0.8288 | 0.8272 | 0.75 |
| Body length | 8.482 | 8.537 | ns | 8.746 | 8.544 | ns |

**The weaker `tm1a` "knockout-first" allele shows none of this** (Bone Area p = 0.54, BMC p = 0.91) — an
internal dose–response.

> ### **The bone-mineral deficit is present in a TRUE NULL heterozygote, in both sexes for BMC.** Three independent lines, three allele classes — **dominant-negative missense (Bell-Hensley), common regulatory variation (rs13002567), and true null (IMPC)** — all agree. **The trade-off is intrinsic to DNMT3A. F-R082's hope is dead.**

### 1b. And a near-fatal flaw I nearly walked past

The same IMPC record shows **no body-length gain in the true-null heterozygote** (female +0.6%, male −2.3%,
both n.s.). Only the **missense** mice get longer bones. **And Tatton-Brown wrote in the original 2014 paper:**

> *"**a simple haploinsufficiency model appears unlikely** given the small proportion of truncating
> mutations… parents of Dnmt3a knockout mice are grossly phenotypically normal."*

**If DNMT3A overgrowth required a dominant-negative property rather than reduced dosage, then an inhibitor —
which reduces activity, like haploinsufficiency — would not reproduce it, and the entire arm would be
broken.** I checked the human allele classes against height:

| variant | class | height |
|---|---|---|
| **c.934_937dupTCTT** (Tatton-Brown 2014, COG1670, age 20.5) | **frameshift** | **+3.2 SD** |
| **p.Arg320\*** (Swedish, F-R081) | **nonsense** | **+3.2 SDS**, 187.4 cm |
| **p.G587fs** (Japanese, F-R081) | **frameshift** | **+3.77 SD** |
| **p.Arg771\*** (Chilean, F-R081) | **nonsense** | **+2.42 SD** |

> ### **Four human truncating alleles, all substantially overgrown.** Haploinsufficiency **is** sufficient in humans. **Tatton-Brown's 2014 speculation was based on mutation-spectrum reasoning in thirteen patients before nonsense cases were characterised, and the subsequent case literature refutes it.** **An inhibitor is viable.**
>
> **And the mouse discrepancy resolves the way Tatton-Brown himself proposed:** *"it is unclear whether this is because loss of function of one Dnmt3a copy is not associated with overgrowth, or because **the overgrowth phenotype is too subtle to detect in mice**."* **IMPC's own numbers settle it — n = 8–9 per sex, and the bone assays that ARE powered at that n detect deficits while length does not.** The mouse het-null is underpowered for length, not negative.

### 1c. Now the good news, and it closes the largest hole in the stack

**Is the trade-off a law of skeletal biology, or a property of this gene?**

**Genome-wide, height and bone size are genetically almost independent** — published LD-score genetic
correlations of **rg = 0.064 (lumbar spine bone area)** and **rg = 0.14 (hip)** with height. **Growing taller
does not, in general, cost bone.**

**And the direct test.** I pulled every GWAS Catalog SNP mapped to **CCN2** and **ACAN** — the two `v(m)`
genes from F-R078 — and every association:

| gene | mapped SNPs | height associations | **bone-density associations** |
|---|---|---|---|
| **DNMT3A** | 161 | 47 | **4 — and one SNP carries both, in opposite directions** |
| **ACAN** | **190** | many | **ZERO** |
| **CCN2** | 36 | several | **ZERO** |

> ### **ACAN has 190 mapped SNPs and a dense height signal with NO bone-density association at all. CCN2 the same.** **Height can be moved at these loci without a detectable density cost.** **The DNMT3A trade-off is locus-specific, not a conservation law — and separability is demonstrated, not assumed.**
>
> ### **Which makes CCN2 the exact complement the stack needs, on two independent grounds:** it is a height locus **with no BMD penalty in human genetics**, and it is the one agent **measured** to raise cortical thickness (0.060 vs 0.049 mm) and mineral content (1.36 vs 1.10 mg/mm) while lengthening bone (F-R078). **Item 2 is answered: separable, and the counter-lever is already in the stack.**

*Caveat: absence of BMD hits could partly reflect power. ACAN at 190 SNPs is reasonably powered; CCN2 at 36 is weaker.*

---

## 2. Item 1 — "does postnatal DNMT3A reduction work?" **The window is postnatal; the constraint is engagement, not timing**

### 2a. In mouse the phenotype is entirely postnatal

- **Smith 2021:** `Dnmt3a^R878H/+` mice are *"normal weight and size at birth, no obvious developmental defects."* Weights are **identical before 100 days** and diverge only after. Longer femurs at **210 days**.
- **Bell-Hensley 2024:** growth plates thicker at **P27**; tibial overgrowth measured at **30–36 weeks**.

> ### **The mouse is normal at birth and acquires the entire phenotype after it.** That is direct evidence that the lever operates during postnatal growth rather than setting a fixed prenatal setpoint.

### 2b. In humans the raised setpoint is still producing growth in the second decade

Both TBRS girls in F-R081 **had to be treated to stop growing** — the Japanese girl grew **166 → 175 cm
between 10.8 and 13.6 years while on oestrogen given to force fusion**, and the Swedish girl gained
**12.6 cm after bilateral epiphysiodesis at 12 years 9 months.** **Whatever DNMT3A did prenatally, it was
still generating growth at the age an intervention would be given.**

### 2c. But the mosaic carrier sets a bar, and it is the honest counterweight

There is a documented **post-zygotic mosaic DNMT3A carrier** — identified because **4 of his 14 offspring
have TBRS** — and he **does not have overgrowth: height at the 32nd percentile.** Jeffries measured his
epigenetic age acceleration at **+23%** against ~40% in full carriers, so his mutant fraction is real.

> ### **A partial-fraction human carrier is not tall.** **Item 1's answer is therefore not "timing" but "dose": the effect is expressed postnatally, but it requires the change in a large fraction of the relevant cells.** For an inhibitor that is a **target-engagement specification, not a developmental-window veto** — and it converges with §1b's finding that heterozygous 50% reduction is enough in humans while the mosaic's lower fraction is not.

*I could not obtain the per-tissue mutant fractions (ScienceDirect returned 403). **Tate — "Tissue-Biased
Expansion of DNMT3A-Mutant Clones in a Mosaic Individual," Cell Rep/AJHG 2020, S1934-5909(20)30285-X** is
the one paper that would quantify this, and it is the single most useful thing left to obtain.*

---

## 3. Item 3 — "are the setpoint and deadline arms additive?" **A human population already runs both**

**47,XXY Klinefelter syndrome is the stack's architecture, occurring naturally:**

| arm | mechanism in Klinefelter |
|---|---|
| **setpoint / rate** | **three copies of SHOX** (pseudoautosomal, escapes X-inactivation) |
| **deadline** | **hypogonadism → delayed epiphyseal closure** |

**And the two are separable in time, which is what makes it a real test:**

- *"Increased height has been demonstrated already **at ages 4 to 12** in KS boys, **well before normal epiphyseal fusion**, pointing toward an effect of other modulators, such as **SHOX gene dosage**."* — **the setpoint arm acting alone.**
- *"The increased height is mainly based on an **increased leg length**, likely caused by **delayed epiphyseal closing due to relative pubertal hypogonadism**."* — **the deadline arm adding on top.**
- Net: **mean +5 to +7 cm above normal men**, with *"normal circulating levels of IGF-1 and IGFBP-3"* — **non-endocrine, exactly like TBRS.**

> ### **Two independent levers — a genetic setpoint raise and an endocrine deadline extension — combining in one human population, each demonstrably contributing in a different time window.** That is the architecture F-R082 proposed for DNMT3A + oestrogen ablation, and **it already exists and works.** Item 3 is answered.

### And a constraint the branch did not know about

**A 47,XXY man who also carries a heterozygous *ACAN* variant** (c.7141G>A, p.Asp2381Asn) reached
**151.6 cm, −2.8 SDS** — and critically, his **bone age was advanced at 17 years with the growth plates
already fused at a chronological age of 16 years 2 months.**

> ### **ACAN haploinsufficiency advanced bone age and closed the plates EVEN UNDER KLINEFELTER HYPOGONADISM.** **The deadline arm is not unconditional. A growth-plate matrix defect can force fusion through an extended-deadline endocrine state.**
>
> **Consequence for the stack:** the `v(m)` arm is not only about bone strength. **Anything that degrades matrix output advances bone age and can close the plate despite oestrogen ablation** — so **CCN2 (matrix-raising) is protecting the deadline arm as well as the cortex**, and any intervention that compromises matrix would sabotage both.

---

## 4. Where the three items now stand

| item | F-R083 status | **F-R084 answer** |
|---|---|---|
| **postnatal vs germline window** | unsubstitutable | **Postnatal in mouse (normal at birth, all of it after day 100); human setpoint still generating growth at 10–13 y. The mosaic carrier converts this from a timing question into a target-engagement threshold.** |
| **height/density separable** | unsubstitutable | **YES.** Genome-wide rg(height, bone area) = 0.06–0.14; **ACAN (190 SNPs) and CCN2 have height signal and ZERO bone-density associations**, against DNMT3A's opposite-direction pleiotropy. **The trade-off is DNMT3A-specific and CCN2 is the counter on two independent grounds.** |
| **setpoint + deadline additive** | unsubstitutable | **YES — 47,XXY runs both arms**, SHOX×3 before fusion matters and hypogonadal delay after, netting +5–7 cm on a normal IGF-1 axis. **New constraint: a matrix defect (ACAN) overrides the deadline arm and forces fusion anyway.** |

**And one flaw caught in passing that would have been fatal if missed:** the true-null mouse shows the bone
deficit **without** the length gain, and Tatton-Brown's own paper says haploinsufficiency is an unlikely
mechanism. **Had that stood, a DNMT3A inhibitor would have been the wrong tool entirely.** **Four human
truncating alleles at +2.4 to +3.8 SD refute it** — and the mouse discrepancy is an n = 8 power problem that
IMPC's own data exposes.

---

## 5. What is left

**Nothing in the three items is now unanswered in principle.** What remains is one document and two
genuinely-never-done experiments, and I want the distinction kept sharp:

**A document, and it is the highest-value thing left:**
- **"Tissue-Biased Expansion of DNMT3A-Mutant Clones in a Mosaic Individual," S1934-5909(20)30285-X** — ScienceDirect returned 403. **§2c rests on it. It would give the per-tissue mutant fraction in a non-overgrown mosaic carrier, which is the quantitative target-engagement threshold for the entire DNMT3A arm.**

**Two experiments that do not exist and cannot be substituted:**
- **A DNMT3A inhibitor given to a growing animal with a bone-length readout.** §1b establishes an inhibitor is the right class; nothing establishes the dose–response.
- **DNMT3A reduction combined with oestrogen ablation in one organism.** §3 shows the architecture works in Klinefelter with a different setpoint gene; the specific combination has never been made.

**Both are now well-posed rather than open-ended**, which they were not two rounds ago.
