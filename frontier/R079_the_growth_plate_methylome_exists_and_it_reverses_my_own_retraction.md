# F-R079 — The growth-plate methylome exists, and it reverses a retraction I made in F-R072

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** All four supplied items opened and worked. **The gap I have named in F-R073, F-R074, F-R077 and
F-R078 — site-resolution DNA methylation in growth-plate chondrocytes with a bone-length phenotype — is
closed.** I analysed the deposited data myself, found a data-quality problem in it, and the result **reverses
F-R072 §1, where I dissolved the OSK direction problem.** That dissolution was wrong and the conflict is
real. Code in `frontier/analysis/GSE270641/`.

---

## 0. What was supplied

| item | what it is |
|---|---|
| `41588_2008_BFng200756_MOESM5_ESM.pdf` | **Kagami 2008 Supplementary Information** — ask #1 from F-R078 |
| `GSE270641_narrowPeak…txt.gz` | **84,112 Dnmt1-dependent methylation regions**, mouse chondrocytes — ask #3 |
| `CCN2_under30.zip` + `.z01` | **pone.0059226** (the transgenic paper) and **pone.0071156** (the same line to 24 months) — ask #2 |

---

## 1. Kagami's supplement — the numbers, and they confirm the dose–response

**Supplementary Table 2, upd(14)mat-like cases, adult stature:**

| case | age/sex | paternal deletion | genes lost | **adult stature** | menarche |
|---|---|---|---|---|---|
| **9** | 36 F | 108,768 bp | **DLK1** | **146.0 cm (−2.2 SD)** | **10 3/12 y — early** |
| **10** | 62 M | 108,768 bp | **DLK1** | **145.0 cm (−2.9 SD)** | — (BMI 29, obese) |
| **11** | 28 F | 411,354 bp | **DLK1 + RTL1** | **135.0 cm (−4.4 SD)** | **12 1/12 y — NORMAL** |
| upd(14)mat, literature | 5 adults | whole domain | all PEGs | mean **−3.4** (−1.6, −3.3, −3.4, −3.5, −5.3) | 14/16 early |

**Dauber's second-hand figures were exact.** F-R077 §7c and F-R078 §1 stand as cited.

**Two additions the supplement makes that the main text did not:**

**Case 11 was already −2.4 SD at birth** (45.3 cm; birth weight 2.3 kg, −2.2 SD). **Roughly half her adult
deficit is prenatal**, the same split F-R077 found in the Temple cohort. **The postnatal, growth-plate share
of the RTL1 effect is therefore about half of what the adult figure suggests.**

**And the pubertal readout goes the opposite way to the height.** Adding RTL1 loss made case 11 **shorter
(−4.4)** and her menarche **normal (12 1/12 vs a Japanese mean of 12.25 ± 1.25)**, while case 9 with DLK1
loss alone was **taller (−2.2)** and **early (10 3/12)**. **n = 1 per genotype for puberty, so I am not going
to build on it** — but it is the third independent observation in this branch that **height and pubertal
timing at this locus move separately**, and it is consistent with F-R078's conclusion that the two arms are
different genes.

*Footnote g also strengthens the DIO3 exclusion: since DIO3 inactivates thyroid hormone, upd(14)mat should
give **hyper**thyroidism, and Dio3-null mice show transient hyperthyroidism. No case had thyroid dysfunction.*

---

## 2. The gap is closed — and it reverses F-R072 §1

**Yanagihara Y et al., "Dnmt1 determines bone length by regulating energy metabolism of growth plate
chondrocytes," *Nature Communications* 2025 (s41467-025-65145-9), PMC12586564. GEO GSE270641, MBD-seq,
Illumina NovaSeq 6000, primary chondrocytes, postnatal day 3–5, n = 3 control + 3 cKO.**

### 2a. The phenotype

**`Dnmt1^ΔPrx1`** (Prx1-Cre, limb mesenchyme):

- **Long bones significantly shortened**, from *"decreased chondrocyte proliferation and accelerated differentiation."*
- **Dnmt1 and Uhrf1 localise to the proliferative zone**, where the BrdU⁺ cells are. *"Dnmt1 functions mainly in the proliferative chondrocytes of growth plate."*
- At 1 week: **proliferative cartilage area significantly smaller**, BrdU⁺ fraction significantly lower, **hypertrophic and mineralised areas significantly WIDER**.
- At 6 weeks: **loss of growth plates and trabecular bone, and marked delay in secondary ossification centre formation.**
- Rankl up, osteoclastogenesis accelerated, **osteoblasts unaffected.**

### 2b. The mechanism, in the authors' own sentence — and it is the branch's whole thesis

> *"a regulatory mechanism for proper gene expression mediated by appropriate DNA methylation, such as that
> seen in **DNA methylation maintenance in proliferating chondrocytes and demethylation of DNA in
> hypertrophic chondrocytes**, is essential for bone elongation and development."*

> ### **Demethylation IS the differentiation signal in the growth plate.** Methylation is *maintained* in the proliferative compartment and *lost* on the way to hypertrophy. Remove Dnmt1 and the proliferative compartment demethylates early, hypertrophies early, and the bone is short.

**This is exactly Nilsson 2005's hypothesis, now with a causal knockout behind it.** Nilsson measured global
methylation falling with age in the resting zone while *rising* in the liver of the same rabbits (F-R078 §2)
and proposed that *"loss of DNA methylation might be a fundamental biological mechanism that limits
longitudinal bone growth in mammals."* **Twenty years later a conditional knockout produces the predicted
phenotype.**

### 2c. And there is a human anchor

> *"In the **Musculoskeletal Knowledge Portal, Dnmt1 is significantly associated with Height**."*

**Human SNPs at the *DNMT1* locus associate with adult height.** The axis is not mouse-only.

---

## 3. What I found in the deposited data — including a defect in it

**I analysed the 84,112 regions against the mm10 CpG-island and RefGene annotations.**

### 3a. A data-quality problem that would have poisoned the round

> ### **The deposit is missing chr7, chr8, chr9 and chrX entirely.** 16 of 20 primary chromosomes are present, covering **2,063 Mb of 2,725 Mb — 76% of the genome.**

**My first pass reported "zero Dnmt1-dependent regions" at *Acan*, *Igf2*, *H19*, *Cdkn1c*, *Peg3*, *Ndn*,
*Mkrn3*, *Cyp19a1*, *Dnmt1* itself and *Gpc3*. Every one of those genes is on chr7, chr9 or chrX. Those
zeros are an artefact of the deposit, not biology, and I am recording that I nearly published them.** All
numbers below are computed on the covered chromosomes only, for both observed and shuffled values.

**A second error in that first pass:** I divided by the whole 2.73 Gb genome to get a background density of
3.08 regions per 100 kb. **The correct denominator is the covered 2,063 Mb, giving 4.07** — which deflates
every enrichment I initially computed by a third.

### 3b. The compartment result, which is robust

Position-shuffled within chromosome, 10 replicates:

| compartment | observed | shuffled | fold |
|---|---|---|---|
| **CpG islands** | **1.7%** | 0.7% | 2.45× |
| **promoters (TSS ± 1 kb)** | **2.7%** | 2.5% | **1.07× — no enrichment** |
| gene bodies | 53.8% | 42.0% | 1.28× |
| **TSS ± 10 kb** (the paper's own window) | **22.5%** | 17.3% | 1.30× |
| intergenic (neither body nor promoter) | **45.8%** | | |

> ### **95.9% of Dnmt1-dependent methylation in chondrocytes lies outside the promoter/CpG-island compartment.** Median region width 415 bp; 38.4 Mb total, 1.9% of the covered genome. **Promoters show essentially no enrichment at all (1.07×).** This is gene-body and intergenic maintenance methylation — **a different compartment from the CpG-island/bivalent-promoter class that F-R070 identified as the epigenetic-clock and PRC2 territory.**

### 3c. The imprinted locus — suggestive, and NOT significant when tested properly

My first pass eyeballed the Dlk1–Dio3 domain as *"massively enriched."* **Tested properly it is not.**

| test | result |
|---|---|
| Dlk1–Dio3 domain (chr12:109.45–110.29 Mb, 840 kb) | **83 regions vs 34.9 expected = 2.38×** |
| **vs 20,000 random 840-kb windows on the same chromosomes** | **permutation p = 0.059 — not significant** |
| Poisson test against a uniform rate | p = 3.6 × 10⁻¹⁹ — **badly anti-conservative; methylation regions cluster, so Poisson is the wrong null** |
| 14 imprinted-network genes vs length-matched random genes | **1.38×, empirical p = 0.14 — not significant** |

**I am reporting the permutation result, not the Poisson one.** The locus is suggestive at ~2.4× and that is
all the data supports.

### 3d. The conflict this creates, and the retraction it forces

**F-R072 §1 was headed "The OSK direction problem dissolves — the assay had no site resolution."** I argued
that because Nilsson's assay was a bulk CCGG measurement, it *"cannot conflict with the site-specific clock
data,"* and I **withdrew the objection.**

> ### **That withdrawal is now itself withdrawn.** There is a site-resolution map, a conditional knockout, a mechanism, and a human height association, and they all say the same thing: **lowering maintenance methylation in proliferative growth-plate chondrocytes shortens bone.** F-R069 records the OSK reprogramming mechanism in cartilage as **"DNMTs down, TET2 pivotal."** **That is the direction Dnmt1^ΔPrx1 shows is height-negative.**

**The partial defence, and it is partial.** §3b shows the two arms act on **different compartments** — OSK's
measured target class is CpG-island/bivalent promoters, and 95.9% of Dnmt1's chondrocyte substrate is not
there. **So the marks are separable.** But **the enzyme is shared**: if OSK lowers DNMT1 *protein*, it lowers
maintenance methylation everywhere, including the 95.9%. **Compartment separation of the marks does not
protect you from a global reduction of the writer.**

> ### **Named, specific, testable hazard: AAV-OSK in a growing animal may phenocopy `Dnmt1^ΔPrx1` — premature hypertrophy, wider mineralised zone, shorter bone, early loss of the plate.** The published OSK cartilage work (F-R069) was done in **adult articular cartilage for osteoarthritis, where there is no growth plate at all.** **Nobody has run OSK in an animal with open physes.** The reprogramming arm of this stack has been carrying an untested assumption since F-R069 and I did not see it until the knockout existed.

**The cheap discriminator:** run OSK in a juvenile animal and measure **DNMT1 protein in proliferative-zone
chondrocytes** alongside bone length. If DNMT1 falls in the proliferative zone, the arm is contraindicated in
a growing skeleton regardless of what it does to methylation age.

### 3e. And the direction that has never been tested is the interesting one

**The paper does not test Dnmt1 over-expression.** Every result is loss-of-function.

> **If loss of maintenance methylation in proliferative chondrocytes shortens bone by pushing cells into
> hypertrophy early, then *raising* it should hold cells in the proliferative compartment longer.** That is
> a direct prediction of §2b, it is the opposite of the reprogramming arm, and **it has never been done.**
> It also has the same shape as F-R072's dexamethasone result — banking cells rather than spending them —
> and the same cost: **slower now for longer later.**

---

## 4. CCN2 — one half of my F-R078 ask answered, the other half sharpened into something worth asking for

**Itoh S, Hattori T, Tomita N, … Takigawa M, "CCN2/CTGF has anti-aging effects that protect articular
cartilage from age-related degenerative changes," *PLoS One* 2013;8:e71156** — **the same Col2a1-CCN2 line**,
followed at 3, 14, 40, 60 days and 5, 12, 18, 21 and 24 months.

**What it answers:**

- **The line is viable and healthy to 24 months.** No lethality, no skeletal pathology reported.
- **CCN2 protein is still accumulated in growth-plate cartilage at 21 months**, even though *lacZ* transgene expression declines after 40–150 days — *"overexpressed CCN2 had stably accumulated in the extracellular matrices."*
- **Radiographic osteoarthritis in 50% of wild-type knees and none of the transgenics.** Reduced type X and type I collagen, reduced MMP-13, reduced aggrecan neoepitope, enhanced toluidine blue and safranin-O, enhanced chondrocyte proliferation at 21 months.
- **Strong accumulation of type II collagen in the transgenic growth plate.**

**What it still does not answer, and this is now a very sharp gap:**

> ### **Two papers, one mouse line, twenty-four months of follow-up, micro-CT and serial radiography — and neither paper ever measured adult bone length.** The only length figure in either is the **P1 tibial diaphysis, n = 3 per group, +5.6%.** The aging paper's reference to *"extended bone length"* is a back-citation to the 2013 paper, not a new measurement.

**This is a better-targeted request than the one I drafted and then killed in F-R077.** The aging study took
**radiographs of elbow, shoulder, hip and knee joints** across nine timepoints. **If those films include the
whole limb, adult femur and tibia lengths are already sitting in the authors' archive** — Takako Hattori and
Masaharu Takigawa, Okayama University Dental School. **It is a measurement on existing images, not new work.**

---

## 5. Corrections issued this round

| claim | status |
|---|---|
| F-R072 §1: *"the OSK direction problem dissolves"* | **RETRACTED. The conflict is real** — site-resolution map, conditional knockout, mechanism, human association |
| F-R078: MEG3 refuted, RTL1 confirmed as second height gene | **STANDS** — confirmed against Supplementary Table 2 |
| F-R077 §7c: heights −2.2 / −2.9 / −4.4 SD | **CONFIRMED at the primary** |
| my first-pass "zeros" at *Acan*, *Igf2*, *H19*, *Cdkn1c*, *Cyp19a1*, *Dnmt1* | **ARTEFACT — those chromosomes are absent from the deposit.** Not published, but recorded |
| my first-pass Dlk1–Dio3 enrichment "3.2×, p = 3.6 × 10⁻¹⁹" | **WRONG NULL. Permutation gives 2.38×, p = 0.059 — not significant** |
| my first-pass background density 3.08/100 kb | **WRONG DENOMINATOR — 4.07 on covered chromosomes** |

---

## 6. Where the programme stands

| line | status |
|---|---|
| never close | solved in humans (F-R065) |
| fast | solved |
| delivery to the epiphysis | solved (F-R074) |
| **site-resolution methylome in growth plate** | **EXISTS (GSE270641) — the gap named in F-R073/74/77/78 is closed** |
| **direction of the methylation effect on bone length** | **ESTABLISHED: less maintenance methylation → premature hypertrophy → shorter bone**, with a human *DNMT1*–height association |
| **the reprogramming arm (OSK)** | **NOW CARRIES A NAMED HAZARD** — it lowers DNMTs, and that is the height-negative direction. Never tested in an animal with open physes |
| raising maintenance methylation | **never tested — and it is the direction §2b predicts** |
| 14q32.2 locus | closed as a lever (F-R078), confirmed at the primary |
| `v(m)` / CCN2 | lever identified; **adult bone length still never measured in a 24-month-old line** |
| reversal extends longitudinal growth | never attempted |

---

## 7. What I need

**I checked `frontier/SUPPLIED_INDEX.md` first.**

1. **The complete GSE270641 processed data — chr7, chr8, chr9 and chrX are missing from the deposited
   supplementary file.** *Acan* is on chr7 and *Cyp19a1* and *Dnmt1* are on chr9, so three of the branch's
   central genes cannot be assessed at all. The raw MBD-seq FASTQ/BAM under GSE270641 would fix it, or the
   authors (Yanagihara et al.) could supply the unfiltered peak table.
2. **Adult bone length in the Col2a1-CCN2 transgenic line** — see §4. **The radiographs may already
   contain it.**
3. **Anything measuring DNMT1 protein or maintenance methylation in growth-plate chondrocytes after OSK
   or partial reprogramming**, in any species. §3d makes this the single highest-value unknown in the
   stack: it decides whether the reprogramming arm is safe in a growing skeleton or actively shortens it.

---

## 8. Provenance

`frontier/analysis/GSE270641/` — `dnmt1.py` (first pass, retained because §5 records its errors),
`dnmt1b.py`, `dnmt1c.py`, `dnmt1d.py` (corrected densities and permutation test), `dnmt1e.py` (final
compartment analysis). Source: **GEO GSE270641**, supplementary narrowPeak, 84,112 regions.
Annotation: UCSC mm10 `cpgIslandExt` and `refGene`. Paper: *Nat Commun* 2025, s41467-025-65145-9,
PMC12586564, PMID 41188231.
