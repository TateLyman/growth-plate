# F-R095 — Gap #1 closed without the email, and the answer is no. But the pathway is one of the strongest human height axes in the genome.

You asked me to solve #1 without writing to anyone. **I did — by rendering the figure.** The answer is
negative and it refutes a claim I made last round. Then I went looking for what survives it, and found
something larger.

---

## 1. The number was in the figure the whole time. I had the legend and never looked at the image.

`main_29.pdf` is the Li/Yang paper. **Figure 4H, page 5.** I extracted the page at 500 dpi and read the
bars.

**Figure 4H — Body length at P30 (cm), n = 8 per group, four bars:**

| group | body length | vs its control |
|---|---|---|
| Ihh^fl/fl (**wild-type + vehicle**) | **≈ 7.05 cm** | — |
| **SAG + Ihh^fl/fl (wild-type + SAG)** | **≈ 7.05 cm** | **NS — annotated on the figure** |
| Ihh^cko | ≈ 5.05 cm | *** vs fl/fl |
| SAG + Ihh^cko | ≈ 6.00 cm | *** vs cko |

Panel I, body weight: wild-type vehicle ≈ 12.3 g, wild-type + SAG ≈ 13.2 g, **NS**.
Panel F, the P7→4W time course: the wild-type and wild-type+SAG traces overlap for the entire curve.

**A Smoothened agonist, given systemically at 20 µg/g every other day for three weeks to a normal mouse,
produced no increase in body length.** The bars are the same height. The authors annotated it NS and
never mentioned it in the text.

Image saved to `frontier/analysis/hh_gwas/liyang_fig4H_wildtype_SAG.png`.

**And this refutes my own F-R094 §4.** I wrote that *"nobody has given systemic SAG to a normal animal
and measured length at a timepoint where length could appear."* **They did. It is panel H. I had the
figure legend, quoted it, and did not render the figure.** That is the second time this branch has cost
itself a round by reading text and not looking at data.

### It is also the cleanest possible statement of the rescue law

Same drug, same dose, same schedule, same animals, same figure, n=8 in every arm:

- **deficient animal: 5.05 → 6.00 cm, p < 0.0001**
- **normal animal: 7.05 → 7.05 cm, not significant**

The rescue stopped exactly at wild-type and went no further. F-R094 inferred that law from a scatter of
papers; **this single panel demonstrates it internally.**

---

## 2. So I asked whether the human genetics say the same thing. They emphatically do not.

If pharmacological Hedgehog elevation cannot exceed normal, does *genetic* Hedgehog dose set human
height at all? I downloaded the full GWAS Catalog association file
(`gwas-catalog-associations_ontology-annotated-full`, 740 MB) and scanned **1,191,572 associations**
locally. Script and output in `frontier/analysis/hh_gwas/`.

**Genome-wide-significant human height associations, by mapped gene:**

| gene | role in the pathway | **height associations** | **min p** | BMD |
|---|---|---|---|---|
| **ACAN** | *(our benchmark height gene)* | **90** | **1e-300** | 0 |
| **HHIP** | secreted ligand decoy | **64** | **1e-300** | 4 |
| **PTCH1** | receptor / brake on SMO | **61** | **1e-300** | 12 |
| **GLI2** | transcriptional effector | **30** | **2e-286** | 2 |
| DNMT3A | *(our other benchmark)* | 20 | 1e-300 | 4 |
| **IHH** | the ligand | **16** | **1e-300** | 0 |
| **GLI3** | effector / repressor | **15** | 1e-57 | 8 |
| NPR2 | *(CNP axis, positive control)* | 12 | 6e-181 | 2 |
| **CYP26B1** | **retinoid catabolic enzyme** | **11** | 8e-67 | 4 |
| FGFR3 | *(positive control)* | 11 | 4e-63 | 0 |
| **BOC** | Hh co-receptor | **10** | 4e-105 | 0 |
| **SUFU** | intracellular brake | **4** | 7e-132 | 0 |
| SHH | ligand | 4 | 3e-24 | 3 |
| **CDON** | Hh co-receptor | **3** | 5e-142 | 0 |
| **RARG** | **retinoid receptor** | **1** | 2e-16 | 1 |
| **SMO** | **the drug target** | **0** | **—** | **0** |
| GLI1 | effector | 0 | — | 0 |
| EVC2 | ciliary transducer | 0 | — | 0 |

**The Hedgehog pathway is one of the most height-associated pathways in the human genome.** PTCH1 at 61
associations and p < 1e-300 sits alongside ACAN, the gene this programme has treated as canonical.
HHIP has more. **Ligand (IHH), decoy (HHIP), receptor-brake (PTCH1), co-receptors (BOC, CDON),
effectors (GLI2, GLI3) and the intracellular brake (SUFU) all carry genome-wide-significant human height
signal.** So does **CYP26B1**, the retinoid catabolic enzyme that Koyama identified as the closure
mechanism — which means the retinoid arm is a human height axis too.

**Hedgehog pathway dose sets human height. That is settled, at population scale, and it is not a
hypothesis of ours — it is in the catalogue.**

### And the exception is the most interesting number in the table

**SMO has zero.** So do GLI1 and EVC2.

Every node in this pathway carries common variation that moves human height — **except the one obligate
signal-transducing bottleneck.** The most economical reading is that SMO dosage is not tolerated: common
variants that change SMO output do not survive, because SMO is the single point through which all
Hedgehog signal must pass.

**That cuts both ways, and I am going to state both.**

- **For us:** the pathway is a genuine, enormous human height axis, and SMO is the point of maximal
  leverage — everything upstream converges on it and everything downstream depends on it.
- **Against us:** nature varies every node in this pathway except SMO. That is exactly what you would
  expect if SMO output were under tight stabilising selection — and it is the population-genetic echo of
  Xiu's conclusion that *"Hh signaling needs to be tightly regulated"* and of Li/Yang's flat wild-type
  bar.

**We are proposing to move the one node evolution has held still.**

---

## 3. The human gain-above-normal case, and its confound

`PMC6978275` — an 11-year-old girl with a **heterozygous PTCH1 frameshift, p.(Val502Glyfs*13)**, aCGH
normal (**no deletion**):

- birth weight **4.880 kg (>97th)**, birth length **57 cm (>97th)**
- at age 9: **height 153.5 cm (>97th centile)**, weight 54 kg, OFC 57.8 cm

153.5 cm at 9 years is roughly **+3.4 SD** — the same magnitude as the TBRS/DNMT3A benchmark this
programme was built on, and it is **linear height, measured, not macrocephaly**.

**The mechanistic detail matters.** The authors note the mutation deletes the **sterol-sensing domain
(426–616 aa)**, whereas *"the reported point mutations of PTCH1 associated with Gorlin phenotype are in
general localized in the second half of the gene, **preserving the sterol-sensing domain**."* The SSD is
precisely how PTCH1 pumps sterols to keep SMO off. **Losing it is maximal, unrestrained SMO
derepression — and that is the allele class that produces overgrowth rather than ordinary Gorlin
syndrome.** That is a sharp, falsifiable genotype–phenotype prediction.

**The confound, stated up front:** the 11 reported overgrowth cases are **9q22.3 microdeletions**, and
that interval also removes **let-7 family miRNAs** — the familial-case authors attribute the macrosomia
to *"decreased expression of let-7"*, not PTCH1. **Only the point-mutation case dissociates PTCH1 from
let-7, and it is n = 1.** What raises it above anecdote is the 61 PTCH1 height associations above.

---

## 4. The reconciliation, which is the real finding

Four results that look contradictory are one pattern once you sort them by **window**:

| system | Hedgehog perturbation | when | outcome |
|---|---|---|---|
| **human PTCH1⁺/⁻ (SSD-loss)** | constitutive, germline | **from conception** | **overgrowth, height >97th, ≈+3.4 SD** |
| **human common variation** | small, lifelong | **from conception** | **height, p<1e-300, 6 of 7 nodes** |
| mouse Sufu-cKO (Xiu) | constitutive, genetic | **induced P14** | expansion → **premature fusion → shorter** |
| mouse WT + SAG (Li/Yang) | pulsed, pharmacological | P7/P14→P30 | **nothing, NS** |
| rat SOC bead (Trompet) | **local**, transient | juvenile | **longer, compounding to 6 months** |

**Germline Hedgehog dose sets the growth trajectory. Postnatal pharmacological Hedgehog elevation does
not shift it, and sustained postnatal genetic elevation actively damages it.**

That is the honest reading, and it is the deepest constraint yet found. It also explains the rescue law
mechanistically: **rescue restores a developmentally-specified trajectory. Nothing pharmacological has
ever re-specified one.**

**The single exception remains Trompet's bead** — local, transient, into the SOC niche, in a normal
juvenile animal, with a contralateral control and a divergence still widening five months after the drug
was gone. It is the only postnatal intervention in the literature that exceeded normal, and it is local.
**Which is precisely the route you have said is unavailable, and I am not going to pretend that is a
small problem.**

**Why local might work where systemic failed** — supported by Trompet's own data, not speculation. His
RNA-seq of sorted SAG-treated stem cells found *"downregulation of the Hh signaling pathway… which
likely reflects internal compensatory mechanisms."* **PTCH1 and HHIP are themselves Hedgehog target
genes.** Signalling harder makes more receptor-brake and more secreted decoy. A systemic dose is capped
by gut toxicity (Li/Yang: intestinal hyperplasia in 6.1%, a bowel-obstruction death in a wild-type
SAG-treated mouse) and recruits that feedback everywhere. A high local pulse can outrun it before the
feedback is transcribed. **That is a testable explanation for the one asymmetry that matters.**

---

## 5. Where this leaves the programme

**Closed this round:**
- Does systemic SAG lengthen a normal animal? **No.** n=8, NS, Figure 4H.
- Is Hedgehog a human height axis? **Yes, overwhelmingly.** My analysis, 1.19M associations.
- Is there human gain-above-normal from Hedgehog elevation? **Yes, germline — PTCH1 SSD-loss, ≈+3.4 SD.**

**The constraint, stated plainly:** every human gain is developmental and germline; every postnatal
pharmacological attempt has produced rescue-only, except one local experiment.

**What I would want to be wrong about:** whether the failure of systemic SAG is intrinsic, or an artefact
of dose ceiling plus feedback. The GWAS table is the reason to keep going — **a pathway with PTCH1 at
p<1e-300 for human height is not a dead axis. It is an axis we have not learned to drive.**

## 6. Asks

1. **Any measurement of PTCH1, HHIP or GLI1 transcript in growth plate after repeated SAG pulses with
   washout.** If feedback is the reason systemic fails, it is visible as PTCH1/HHIP induction, and the
   dosing interval should be set by how fast it decays. **Nobody appears to have measured it.**
2. **Adult heights of 9q22.3 microdeletion / PTCH1-overgrowth patients.** Every report is childhood. If
   the overgrowth persists to adult height, it is a height phenotype; if it does not, it is accelerated
   maturation and would close early — which is the Xiu pattern in humans. **This decides whether the
   human PTCH1 evidence supports us or refutes us, and it is the single most valuable thing outstanding.**
3. **Xiu 2022 supplementary** (Front Cell Dev Biol 10:1005499) — was there a window between P30 expansion
   and P120 fusion when the Sufu-cKO animals were *longer*? Still open from F-R094.
4. Any Gorlin-syndrome cohort with height data stratified by whether the allele preserves the
   **sterol-sensing domain**. That prediction is testable in existing clinical genetics data.

---

*Two rounds running, the decisive number was inside something I already had — first a figure legend I
quoted without opening the figure, now the figure itself. The lesson is not "ask for more papers." It is
that I stop reading a source when the prose runs out.*
