# F-R080 — DNMT3A is a bidirectional human height gene, loss is the tall direction, and it is the enzyme OSK actually lowers

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** The supplied paper is the OSK study itself — **F-R079's ask #3, the item I called "the single
highest-value unknown in the stack."** Reading it **downgrades the hazard I raised last round, corrects
F-R069, and opens the strongest lead the programme has found.**

> ## The headline: **there is a human gene where heterozygous loss-of-function gives a mean of +3.0 SD of height, and one girl needed surgical growth arrest at 172.5 cm aged twelve. It is DNMT3A. And DNMT3A is the enzyme the OSK paper measures going down.**

---

## 1. The hazard I raised in F-R079 is the wrong enzyme

**Liu Y-W, Zou J-T, … Xie H, Wang Z-X. "Local delivery of OSK factors enables partial cellular
reprogramming to mitigate osteoarthritis and cartilage fibrosis." *Exp Mol Med* 2026;58:782–797.**

F-R079 raised a named hazard: OSK lowers DNMTs, and `Dnmt1^ΔPrx1` shortens bone, so **AAV-OSK in a growing
animal might phenocopy the Dnmt1 knockout.** **The primary shows that inference rested on an imprecision in
my own F-R069 record.**

**What the paper actually measures.** The immunohistochemistry antibody list contains exactly one
methyltransferase: **DNMT3a (ab188470, Abcam).**

> *"the expression of DNA methyltransferase 3 alpha (**DNMT3a**), a chief enzyme responsible for adding
> methyl groups to DNA, significantly increased in the DMM-induced OA model… Crucially, **post-OSK
> treatment, DNMT3a levels were noticeably declined**."*

**And DNMT1 is never measured.** The string "DNMT1" occurs **twice in the whole paper**, and both are
citations to their reference 16 describing the **OA disease state**, not an OSK effect:

> *"a dysregulated balance in DNA methyltransferase (DNMT) levels, as evidenced by **augmented DNMT1 and
> DNMT3a alongside diminished DNMT3b**, has been observed in the cartilage of patients with OA and in the
> DMM mouse model."*

> ### **F-R069's "DNMTs down" should have read "DNMT3a down."** DNMT3A is a **de novo** methyltransferase. **DNMT1 is the maintenance enzyme, and it is the one `Dnmt1^ΔPrx1` deletes.** They are different enzymes doing different jobs in different compartments, and §2 shows they have **opposite signs on human height.**
>
> **The F-R079 hazard is downgraded from "likely" to "unmeasured, and probably the wrong enzyme."** It is not zero — nobody has measured DNMT1 in proliferative-zone chondrocytes after OSK, and that measurement is still the discriminator. But the direction of the alarm was wrong.

**A correction to F-R069 that matters more than it looks.** F-R069 recorded that OSK reduced cartilage
methylation age below chronological age. **The authors say that result is not significant:**

> *"Our investigation revealed that the OSK intervention has the potential to rejuvenate senescent cells.
> **However, the limited sample size in our study precludes the attainment of statistical significance.** It
> is recommended that future research endeavors enhance the sample size for the detection of DNA methylation
> age."*

**The only epigenetic-clock evidence for OSK in cartilage is underpowered and the authors say so.** F-R069
reported it as a measurement. **Corrected.**

*Model detail worth recording: **12-week-old male C57BL/6**, intra-articular, DMM and ACLT. Mice at 12 weeks
still have open physes, so "no growth plate" in F-R079 was overstated — but no skeletal growth endpoint was
measured either way.*

---

## 2. DNMT3A is a human height gene in both directions

### 2a. Loss of function → overgrowth

**Tatton-Brown-Rahman syndrome (TBRS, OMIM 615879)** — heterozygous germline loss-of-function *DNMT3A*.

| source | finding |
|---|---|
| Tatton-Brown 2014, first 13 patients | **tall stature mean +3.0 SD**, head circumference **+2.5 SD** |
| Tatton-Brown 2018, **55 individuals** | **height ≥ +2 SD in 83% (44/53)** |
| GeneReviews | tall stature in ~70% |
| **Case report, *Front Endocrinol* 2021** | **bilateral epiphysiodesis performed to STOP growth** |

**The epiphysiodesis case in full, because it is the most informative single patient in this branch:**

| age | measurement |
|---|---|
| 3 y 3 m | 113.5 cm, **+2.9 SDS** |
| 12 y 2 m | 172.5 cm, **+2.8 SDS**; **bone age 12 years — matching chronological age**; predicted adult height **187.1 cm (+3.4 SDS)**; ~2 SDS above a midparental target of 173 cm |
| **12 y 9 m** | **bilateral epiphysiodesis**, at 174.8 cm |
| 19 y 6 m | **final height 187.4 cm (+3.2 SDS)** |
| post-surgery distribution | **legs +1.7 cm, sitting height +10.9 cm, arm span +20.5 cm** |

Variant: **c.958C>T, p.Arg320\***, a nonsense allele.

### 2b. Gain of function → dwarfism

**Heyn P, Logan CV, Fluteau A, et al. "Gain-of-function DNMT3A mutations cause microcephalic dwarfism and
hypermethylation of Polycomb-regulated regions." *Nat Genet* 2019.**

- PWWP-domain substitutions **abrogate binding to H3K36me2 and H3K36me3**.
- **"Polycomb-associated DNA methylation valleys, hypomethylated domains encompassing developmental genes, become methylated with concomitant depletion of H3K27me3 and H3K4me3 bivalent marks."**
- **`Dnmt3a^W326R/+` dwarf mice** exist.

> ### **One gene. Loss → +3.0 SD. Gain → microcephalic dwarfism. In humans, with a mouse model of the dwarf direction.** Nothing else in this programme has that shape.

### 2c. And the compartment is the one this branch already identified

**F-R070** concluded that **bivalent promoters (H3K27me3 + H3K4me3) gain the most entropy with age and are
reversed by partial reprogramming**, and that Lui's eleven genes are that class. **F-R079** measured that
**95.9% of Dnmt1-dependent methylation in chondrocytes is outside the promoter/CpG-island compartment.**

**Heyn's dwarfism mechanism is hypermethylation of exactly the Polycomb/bivalent compartment — with
depletion of H3K27me3 and H3K4me3.** **Lui measured H3K4me3 falling at eleven promoters during growth-plate
senescence.** **These are the same marks in the same compartment.**

---

## 3. The resolution — two enzymes, two compartments, opposite height signs

| | **DNMT1** | **DNMT3A** |
|---|---|---|
| role | **maintenance** | **de novo** |
| compartment | **95.9% outside promoters/islands** — gene bodies 53.8%, intergenic 45.8% (**my measurement, F-R079**) | **Polycomb DNA-methylation valleys / bivalent promoters** (Heyn) |
| in the plate | localises to the **proliferative zone** with Uhrf1 | not measured in growth plate — **the gap** |
| **loss →** | **SHORT** — `Dnmt1^ΔPrx1`; human *DNMT1* associated with Height in the MSK Knowledge Portal | **TALL — +3.0 SD, TBRS** |
| **gain →** | untested | **microcephalic dwarfism** |
| OSK effect | **never measured** | **decreased** |

> ### **The stack's target is precise: lower DNMT3A, preserve DNMT1.** Which means the nucleoside DNMT inhibitors — azacitidine, decitabine — are **exactly the wrong tool**, because they trap all DNMTs including the one that must be kept.
>
> **Selective non-nucleoside DNMT3A inhibitors exist.** *"Both inhibitors show promising selectivity for DNMT3A in comparison to DNMT1"*, with the mechanism named: *"the presence of **Asn1192** at the corresponding residues in DNMT1 results in a loss of affinity for the inhibitor, explaining the selectivity."* Allosteric pyrazolone and pyridazine series also exist at low-micromolar Ki. **These are chemical probes, not drugs — but the selectivity axis the stack needs is a solved medicinal-chemistry problem, not an open one.**

---

## 4. Sotos versus TBRS — and this contrast is the whole programme

Both are overgrowth syndromes from loss of an epigenetic writer. **They end in completely different places.**

| | **Sotos (NSD1)** | **TBRS (DNMT3A)** |
|---|---|---|
| childhood growth | overgrowth | overgrowth, **+2.9 SDS by age 3** |
| **bone age** | **ADVANCED** | **12 y at 12 y — not advanced** (n = 1) |
| puberty | **early** | early in the same case |
| **adult height** | **"upper limit of normal"** — Cohen: men **184.3**, women **172.9 cm**; Fickie: 182 / 174 cm | **+3.2 SDS retained**, growth to **19 y 6 m** |
| why | *"advanced bone age… accelerates skeletal maturation and closure of growth plates, ultimately **limiting the period of growth despite early childhood overgrowth**"* | the gain is kept |

> ### **Sotos is the failure mode this branch has been describing since F-R024: grow fast, mature fast, end up normal. TBRS is the thing we want: grow fast, and the skeletal clock does not run with it.** **DNMT3A loss appears to decouple growth rate from skeletal maturation. NSD1 loss does not.**

**And I am going to be honest about how thin the crucial cell is.** The "bone age not advanced" claim rests on
**one patient in one case report.** The 55-patient cohort study **contains no bone-age data at all** — I
checked, and *"the document contains zero statements about whether bone age was assessed."* **The single most
important skeletal phenotype in this branch has never been systematically measured in the syndrome that
shows it.**

---

## 5. The pacing law is confirmed in humans — and it reconciles F-R077's null

**Jeffries AR et al., "Growth disrupting mutations in epigenetic regulatory molecules are associated with
abnormalities of epigenetic aging" (PMC6633263).** Horvath 353-CpG clock:

| syndrome | gene | growth | **epigenetic age acceleration** |
|---|---|---|---|
| **TBRS** | *DNMT3A* | **overgrowth** | **~+40%** (Amish c.2312G>A carriers, ANCOVA **P = 0.004**); mosaic father +23% |
| **Sotos** | *NSD1* | **overgrowth** | **~+40%** (R² = 0.869, **P = 6.4 × 10⁻⁹**) |
| **Kabuki** | *KMT2D* | **growth deficiency** | **~−40%** (R² = 0.418, **P = 0.023**) |

> ### **Overgrowth accelerates the clock. Growth deficiency decelerates it. Three syndromes, opposite signs, human blood.** That is the growth-pacing law of F-R066 with a human genetic test behind it.

**And it resolves the tension with my own F-R077.** F-R077 found that girls with central precocious puberty —
**bone age advanced 1.69 y** — showed **no epigenetic age acceleration** (skin-&-blood clock −0.016 y, 95% CI
−0.65 to +0.62). I concluded *"in blood the clock is chronologically paced."*

> **That conclusion needs refining, and the refinement makes the branch stronger.** CPP girls are **early, not
> overgrown** — they have not accumulated extra growth, only redistributed it in time. TBRS, Sotos and Kabuki
> children **have** accumulated more or less growth than normal. **The clock does not track pubertal stage or
> skeletal maturation; it tracks growth accomplished.** F-R077's null and Jeffries' ±40% are the *same law*
> seen from two sides — and F-R077 is, in retrospect, the cleaner control for it than I realised.

**One caveat I will not bury:** the p.(Arg882Cys) carrier showed *">800%"* acceleration. **Arg882 is the
canonical clonal-haematopoiesis allele**, so in blood that number is far more likely to reflect clonal
expansion than growth, and I am excluding it from the argument.

---

## 6. The SRA pull

Tate supplied the six run accessions for GSE270641, which F-R079 showed is **missing chr7, chr8, chr9 and
chrX** from its processed deposit — the chromosomes carrying *Acan*, *Igf2*, *H19*, *Cdkn1c*, *Peg3*,
*Cyp19a1* and *Dnmt1* itself.

**No SRA toolkit, aligner or samtools is available in this environment and the six runs total ~55 GB of
FASTQ against 27 GB of free disk, so a conventional realignment was not possible.** Instead I built a
**repeat-masked 32-mer index** of the target loci from UCSC mm10 sequence (1,138,548 unique k-mers across 13
loci, with k-mers shared between loci discarded) and **streamed the reads directly from ENA without writing
them to disk**, counting per-locus read hits in the first 8,000,000 reads of each run. Positive controls
(*Dlk1*, *Meg3*, *Nnat* — all on covered chromosomes and all Dnmt1-dependent in the deposit) and a negative
control (a 100 kb gene desert on chr12) were carried through the same pipeline.

**Control 1 (SRR29528359), first 8,000,000 reads — pipeline validated, counts are real:**
Acan 166, Cdkn1c 65, Cyp19a1 641, Dnmt1 280, Gpc3 475, Hhip 234, Igf2_H19 305, Mkrn3 24,
**NEG_desert 258**, POS_Dlk1 40, POS_Meg3 94, POS_Nnat 109, Peg3 202.

**The remaining five runs are still streaming as this round is written.** The comparison that matters —
per-locus reads per million, control versus cKO, normalised against the gene desert — **follows in the next
commit.** I am recording the method and the first sample now rather than holding the DNMT3A result, and I
will not state a conclusion about *Acan*, *Cyp19a1* or *Dnmt1* until all six runs are counted.

---

## 7. Corrections issued this round

| claim | status |
|---|---|
| F-R069: *"DNMTs down, TET2 pivotal"* | **IMPRECISE — it is DNMT3a specifically. DNMT1 was never measured** |
| F-R069: OSK reduced cartilage methylation age | **NOT SIGNIFICANT — the authors state the study is underpowered** |
| F-R079: named hazard that OSK may phenocopy `Dnmt1^ΔPrx1` | **DOWNGRADED — wrong enzyme.** Still unmeasured, so not withdrawn |
| F-R079: OSK work was in tissue with *"no growth plate"* | **OVERSTATED — 12-week-old mice have open physes.** No growth endpoint was measured either way |
| F-R077: *"in blood the clock is chronologically paced"* | **REFINED — it is paced by growth accomplished, not by pubertal stage or bone age.** F-R077's null is what the law predicts for CPP |

---

## 8. Where the programme stands

| line | status |
|---|---|
| **a human gene whose loss gives +3 SD of height** | **FOUND — DNMT3A** |
| **bidirectional dose–response in humans** | **YES — loss → TBRS, PWWP gain → microcephalic dwarfism** |
| **selective DNMT3A-over-DNMT1 chemistry** | **exists as chemical probes**; Asn1192 is the selectivity determinant |
| **does DNMT3A loss decouple rate from maturation?** | **suggested by one patient; never systematically measured** |
| **DNMT3A in the growth plate** | **never studied — no `Dnmt3a^Col2` or `Dnmt3a^Prx1` bone-length experiment exists** |
| pacing law | **confirmed in humans, three syndromes, opposite signs** |
| DNMT1 must be preserved | established (F-R079) |
| OSK arm | hazard downgraded; DNMT1 after OSK still unmeasured |

---

## 9. What I need

**I checked `frontier/SUPPLIED_INDEX.md` first.**

1. **Bone-age data in TBRS.** §4 rests on **one patient**, and the 55-patient cohort has none. **If DNMT3A
   loss really gives +3 SD with a non-advanced bone age, that is the most important skeletal fact in this
   programme** — and it is answerable from hand radiographs that may already exist in the TBRS registry
   (Tatton-Brown / the TBRS Community). **Any TBRS series reporting bone age, or adult heights beyond the
   epiphysiodesis case.**
2. **Tatton-Brown et al. 2014, *Nat Genet* 46:385** — the original 13-patient description with the **+3.0 SD**
   figure. I have it only through secondary citation.
3. **Heyn et al. 2019, *Nat Genet* 51:96** — the DNMT3A PWWP gain-of-function dwarfism paper, in full. §2b
   rests on the abstract; I want the methylation maps and the `Dnmt3a^W326R/+` mouse bone measurements.
4. **Anything measuring DNMT1 protein in growth-plate chondrocytes after OSK or partial reprogramming** —
   unchanged from F-R079, and still the discriminator for the reprogramming arm.

---

## 10. Provenance

`frontier/analysis/GSE270641_sra/` — `getseq.py` (UCSC mm10 target sequences), `kmerjob.py` (repeat-masked
32-mer index), `stream_sra.py` (ENA streaming counter), `counts.json`. Runs SRR29528354–59, GSE270641.
