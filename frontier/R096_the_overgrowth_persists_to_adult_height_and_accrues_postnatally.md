# F-R096 — It persists to adult height, and it accrues after birth. Both of F-R095's constraints break, and the dose regime we have been testing is the wrong one.

`yamada2020` answered the question I called *"the single most valuable thing outstanding"* in F-R095,
and it answered a second one I had not thought to ask.

---

## 1. Adult height: the overgrowth persists

**Patient 1 — the mother, whole-*PTCH1* deletion (9q22.3 microdeletion):**

| | value | SD |
|---|---|---|
| birth weight | 4100 g | **+2.7** |
| **birth length** | **56 cm** | **+3.9** |
| head circumference | 37 cm | +2.9 |
| **height at 17 years** | **173.3 cm** | **+2.9** |
| weight at 17 years | 75.2 kg | +2.8 |

> *"Overgrowth was observed **throughout childhood** (height 173.3 cm, +2.9 SD… **at 17 years of age**)."*

**At 17, a female is at or within a centimetre of final adult height. The overgrowth is not accelerated
maturation that burns out — it is carried to adult stature at +2.9 SD.**

That was the question that decided whether the human *PTCH1* evidence supports or refutes this
programme. **It supports it.** The Xiu pattern — expand, then fuse early, end up shorter — does **not**
describe the human haploinsufficient phenotype.

---

## 2. And the growth happens after birth — which breaks F-R095's central constraint

**Patient 2 — the daughter, same deletion:**

| | value | SD |
|---|---|---|
| birth weight | 3070 g | +1.3 |
| **birth length** | **48.9 cm** | **+0.8 — essentially normal** |
| head circumference | 35.5 cm | +2.1 |
| **height at 9 years** | **143.8 cm** | **+2.3** |

The paper's own framing: *"**prenatal-onset overgrowth in a mother and postnatal-onset overgrowth in her
daughter**."*

**She was born at +0.8 SD in length and reached +2.3 SD by age nine. Roughly +1.5 SD accrued entirely
postnatally, on growth plates that were normal-sized at birth.**

F-R095 concluded: *"every human gain is developmental and germline… germline Hedgehog dose sets the
growth trajectory; postnatal pharmacological elevation does not shift it."* **The first half of that is
now wrong.** The genotype is germline, but **the growth is postnatal**, and it happened in a child whose
skeleton started at normal size. Reduced *PTCH1* dose adds height to a postnatal growth plate over nine
years.

**That is the human existence proof that the postnatal window is open for this axis.** It is the single
most important thing in this round.

---

## 3. The reciprocal, which makes it a dose–response rather than a syndrome

From the discussion, citing Izumi et al. 2011:

> *"a patient with **9q22.3 microduplication** spanning let-7 and PTCH1 developed type 2 diabetes
> mellitus, precocious puberty, and **short stature**."*

| *PTCH1* copies | Hedgehog tone | stature |
|---|---|---|
| **1** (deletion / LoF) | **elevated** | **tall — +2.9 SD at 17** |
| 2 | normal | normal |
| **3** (duplication) | **suppressed** | **short** |

**A bidirectional human gene-dosage–to–height relationship across the full copy-number range, in the
direction we need.** Combined with F-R095's GWAS result — *PTCH1*, 61 genome-wide-significant height
associations, p < 1e-300 — the human genetics on this gene are now about as strong as they get.

---

## 4. The let-7 confound: I tested it, and it is narrowed but not closed

The authors favour a different explanation: the deleted interval also removes **let-7a-1, let-7f-1 and
let-7d** (in 10 of 11 reported overgrowth patients), and the Lin28/let-7 axis governs growth and puberty.

I still had the full GWAS Catalog on disk, so I ran the discrimination directly — every gene in the
minimal deleted region against the let-7 cluster:

| gene | region | height associations | min p |
|---|---|---|---|
| **PTCH1** | 550 kb common | **61** | **1e-300** |
| FANCC | 550 kb common | 6 | 3e-108 |
| C9orf3, ACTL7A, ACTL7B | 550 kb common | 0 | — |
| MIR23B, MIR27B, MIR24-1, MIR3074, MIR6081 | 550 kb common | 0 | — |
| **MIRLET7A1, MIRLET7F1, MIRLET7D** | **outside, deleted in 10/11** | **0** | **—** |
| **LIN28B** | *control — the let-7 repressor* | **39** | **1e-300** |
| LIN28A | control | 7 | 4e-254 |

**Within the deleted interval, essentially all human height signal maps to *PTCH1*. The three let-7 genes
carry none.**

**But I am not going to overclaim this, for two reasons.**

1. **miRNA genes are ~80–100 bp; *PTCH1* is ~70 kb.** GWAS gene-mapping assigns variants to
   overlapping/nearest genes, so a small miRNA is far less likely to be named even when it is causal.
   Zero let-7 associations is **weak** evidence, not strong.
2. **LIN28B has 39 height associations at p<1e-300.** The Lin28/let-7 axis is unambiguously a real human
   height axis — it simply registers at the repressor, where common variation sits. **So let-7 loss
   cannot be dismissed as a mechanism for this overgrowth.**

**What does dissociate them is F-R095's point-mutation case:** *PTCH1* frameshift p.(Val502Glyfs\*13),
**aCGH normal — no deletion, let-7 intact** — with height 153.5 cm at age 9 (≈ +3.4 SD). One patient,
but the right one.

**And there is a clean discriminator nobody has applied.** Zhu et al.: *"Overexpression of Lin28a or
**repression of let-7 delayed onset of puberty**."* The duplication case had **precocious puberty and
short stature** — let-7 gain. So:

> **If 9q22.3-deletion overgrowth patients have *delayed* puberty, the height is let-7. If puberty timing
> is normal, it is *PTCH1*.**

That is answerable from existing case reports and needs no new work. **It is now my top ask.**

The authors also concede the let-7 story is incomplete: *"there are several patients with chromosomal
deletions spanning let-7 and PTCH1 that **do not** show prenatal-onset overgrowth."*

---

## 5. The synthesis that changes the target: we have been testing the wrong dose regime

Sort every result in this file by **how much of the Hedgehog brake is removed, and for how long**:

| system | brake removed | duration | outcome |
|---|---|---|---|
| **human *PTCH1*⁺/⁻** | **~50%** | **lifelong, every cell** | **+2.9 SD, persists to adult height, accrues postnatally** |
| mouse Sufu-cKO (Xiu) | **100%**, constitutive | permanent from P14 | expansion → **premature fusion → shorter** |
| mouse WT + SAG (Li/Yang) | high, **intermittent** | 20 mg/kg q2d × 3 wk | **nothing, NS** |
| rat SOC bead (Trompet) | high **locally**, transient | 3 wk exposure | **longer, compounding to 6 months** |

**The human tall phenotype is chronic, low-level, partial pathway elevation — roughly half the brake,
continuously, for years. Every pharmacological experiment in this file is the opposite: high dose,
intermittently, for weeks.**

Xiu's "tightly regulated" result is not evidence that the axis cannot be pushed. It is evidence that
**total** brake removal decompensates. **Fifty percent, chronically, gives +2.9 SD in a human and carries
it to adulthood.** That is the same shape as F-R085's engagement bracket for *DNMT3A*, where germline
heterozygosity — 50% — gave +3.0 SD.

**Nobody has tested chronic low-level partial Smoothened agonism.** It fits every observation in the
file, and it is the regime the human phenotype actually occupies.

**The honest counterweight:** the reason nobody has is that chronic low-level SMO agonism is precisely
what you would expect to be tumourigenic, and Li/Yang's toxicity was gut (intestinal hyperplasia 6.1%,
a bowel-obstruction death in a wild-type SAG-treated mouse) at intermittent high dose. Chronic low dose
trades an acute ceiling for a cumulative one. That is a real trade and I am recording it as one.

**And the F-R095 caution stands unchanged: SMO carries zero human height associations** while every other
node in the pathway carries many. Nature varies *PTCH1* — the brake — and does not vary *SMO* — the
transducer. **The human experiment that produces tall people is upstream of the drug target we can
reach.**

---

## 6. State of the argument

**Closed:**
- Does *PTCH1* overgrowth persist to adult height? **Yes — +2.9 SD at 17.**
- Can it accrue postnatally? **Yes — +0.8 → +2.3 SD between birth and age 9.**
- Is it a dose–response? **Yes — duplication gives short stature.**
- Is Hedgehog a human height axis? **Yes — F-R095, *PTCH1* p<1e-300, 6 of 7 nodes.**
- Does systemic high-dose intermittent SAG lengthen a normal animal? **No — F-R095, Figure 4H, NS.**

**Open, ranked:**
1. **Puberty timing in 9q22.3-deletion overgrowth patients** — the let-7 vs *PTCH1* discriminator (§4).
2. **Has chronic low-dose SMO agonism ever been given to a growing animal?** The regime the human
   phenotype occupies, and I cannot find it.
3. **Adult heights for more *PTCH1* LoF patients** — n=1 for adult height is thin. Gorlin cohorts
   stratified by whether the allele preserves the sterol-sensing domain would settle both this and
   F-R095's SSD prediction.
4. **Xiu 2022 supplementary** — was there a window where Sufu-cKO animals were *longer*? Open since
   F-R094.
5. **Does *PTCH1* haploinsufficiency expand the resting-zone pool, or raise the rate?** No one has
   looked at a growth plate in this genotype. It is the difference between our pool arm and a rate arm,
   and *Ptch1*⁺/⁻ mice exist.

## 7. Asks

1. **Any 9q22.3 microdeletion or Gorlin case report with pubertal staging or bone age.** This decides
   let-7 versus *PTCH1* and it is buried in case reports rather than requiring new work.
2. **Growth-plate histology or stereology in *Ptch1*⁺/⁻ mice** — resting-zone cell number, plate height,
   column count. The mouse is standard and widely held; someone has stained a physis.
3. **Izumi et al. 2011** (9q22.3 microduplication, short stature, precocious puberty) — full text. The
   reciprocal case, and the puberty phenotype in it is half the discriminator.
4. Long-term or chronic low-dose Smoothened agonist dosing in any growing animal, any endpoint.

---

*What this round did: reversed F-R095's central conclusion using the paper F-R095 asked for. The
developmental window is not closed — a child with half the normal PTCH1 dose gained a standard deviation
and a half of height after birth. What it did not do is close the let-7 confound, and I would rather
leave that visible than argue past it.*
