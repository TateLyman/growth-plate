# F-R082 — The epigenetic clock and the height lever are the same molecule, and the growth plate reads it in both directions

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** Five documents supplied; four are new and all four are load-bearing. **Both F-R081 asks are
answered.** `Dnmt3a` mutant mice have **longer bones and thicker growth plates**; `Dnmt3a` gain-of-function
mice have **thinner growth plates and half the lifespan**; and a 2026 *Nature Genetics* paper shows the
CpGs that DNMT3A gain-of-function hypermethylates **predict chronological age as well as the Horvath clock
CpGs do.**

> ## **The branch has spent sixteen rounds treating "the senescence clock" and "the height lever" as two problems. They are one molecule.**

**And this round also finds the largest liability in the DNMT3A arm: the mice get longer bones and
mechanically weaker ones.**

---

## 0. What was supplied

| document | identity |
|---|---|
| `4e53e7ef-viewcontent.cgi.pdf` | **Bell-Hensley et al., *Bone* 2024;183:117085** — "Skeletal abnormalities in mice with Dnmt3a missense mutations" — **F-R081 ask #2** |
| `f3caf31b-s41467021248007.pdf` | **Smith et al., *Nat Commun* 2021;12:4549** (Ley lab) — humans and mice with DNMT3A Overgrowth Syndrome |
| `28d0f5b8-s41588026026338.pdf` | **Jackson lab, *Nat Genet* 2026;58:1632** — "A progeria syndrome links DNA hypermethylation to age-related pathology" |
| `e8cf4dcd-s41467025651459.pdf` | Yanagihara, the Dnmt1 paper, full PDF with figures |
| `8e4ca4b9-…andespediatr…` | duplicate of the Chilean case already read in F-R081 |

---

## 1. Ask #2 answered — Dnmt3a mutant mice have longer bones, and the growth plate is the mechanism

**Smith 2021, `Dnmt3a^R878H/+`** (paralogous to human R882H):

- **Normal weight and size at birth, no developmental defects.** Weights identical before 100 days, then diverge: **37.73 g vs 31.2 g at 380 days (p ≤ 0.0001)**.
- **micro-CT at 210 days: significantly longer FEMUR lengths (but not humerus), n = 4 pairs.**
- Body composition: **fat mass up, lean mass NOT** — the weight divergence is adiposity.
- No significant macrocephaly in mouse.

**Bell-Hensley 2024, both `Dnmt3a^R878H/+` and `Dnmt3a^P900L/+`** (paralogous to human R882H — severe — and P904L — mild):

| readout | result |
|---|---|
| **tibial length, 30–36 wk** | **small significant increase in R878H**; trend in P900L, **significant in P900L females** |
| body weight | up **only** in R878H → the P900L tibial gain is **not** mechanical loading |
| **proximal tibial growth plate, juvenile** | **significantly thicker** in both mutants |
| zone proportions | **unchanged — the thickening is not zone-specific** |
| **PCNA⁺ cells** | **no change in density or cross-sectional area** |

> ### **The plate is thicker and proliferation is unchanged.** In `dL/dt = flux × v(d)`, that puts the gain in **`v(d)` or in duration, not in flux** — which is the same place F-R058's identity says the largest untapped headroom sits.

**Honest calibration, and it matters:** the mouse effect is **modest** — *"a small significant increase in tibial length"*, a femur difference at **n = 4**, and no phenotype at all before 100 days. **The human syndrome is +3.0 SD with 13/13 penetrance. The mouse does not reproduce the magnitude**, and I am not going to let the mouse carry more weight than it can.

---

## 2. The liability — longer bones, weaker bones

**This is the most important negative finding in several rounds.**

| readout, mature `Dnmt3a` mutants | result |
|---|---|
| **cortical thickness, femur AND tibia mid-diaphysis** | **thinner**, both mutants |
| three-point bend | **significantly lower stiffness, yield load, maximum load** |
| **normalised to cross-sectional area** | **reduced Young's modulus, yield stress, ultimate stress** |
| post-yield displacement, work-to-fracture | **unchanged** — brittleness is not increased |
| tissue mineral density | **unchanged** |
| osteoblast activity (dynamic histomorphometry) | **unchanged** |
| osteoclast number / surface (TRAP) | **unchanged** |
| bone marrow adipose | up in 2/9 R878H females; trend in P900L |

> ### **The bones are longer and materially weaker, and normalising for geometry does not remove the deficit — so this is not just a thinner tube.** The authors could not assign it to osteoblasts or osteoclasts and say so: *"it is unclear if osteoblasts or osteoclasts are responsible for the cortical thinning."* They recommend *"extend[ing] clinical assessments of patients with this condition to include bone density and quality testing."*

**This is STACK_STATE §3.6 — the mechanical ceiling — appearing inside the DNMT3A lever itself.**

> ### **And it makes F-R078's CCN2 finding load-bearing rather than incidental.** Cartilage-specific CCN2 over-expression raised **cortical thickness (0.060 vs 0.049 mm), total mineral content (1.36 vs 1.10 mg/mm) and trabecular mineral**, all P<0.05, while lengthening bone. **CCN2 is the specific, measured counter to the specific, measured liability of DNMT3A. That pairing is no longer a hopeful inference — the two papers report the same variables with opposite signs.**

**One caveat that cuts in our favour and that I am flagging because it is not resolved:** these are **missense** alleles — R878H is a **dominant negative** — and the authors note their result *"conflict[s] with these previous studies on Dnmt3a knockout mice and Dnmt3a overexpression in vitro,"* where *"partial loss of Dnmt3a may increase cortical thickness."* **True haploinsufficiency may not carry the cortical penalty. Human TBRS includes both nonsense (p.Arg320\*, p.Arg771\*, p.G587fs) and missense alleles, and nobody has compared their skeletons.**

---

## 3. The growth plate reads the axis in BOTH directions

**Jackson lab 2026, `Dnmt3a^W326R/+` — the gain-of-function, Heyn–Sproul–Jackson syndrome (HESJAS):**

- **Median life expectancy 12.8 months, against the expected 26–29 for C57BL/6J — half.**
- **Postnatal growth failure**; frailty from 6 months; cataracts, kyphosis, reduced coat, loss of subcutaneous fat.
- **Osteoporosis with dramatic loss of trabecular bone and increasing fragility at 6 months.**
- **In 10–12-month mutants, GROWTH PLATE THICKNESS WAS REDUCED**, with decreased BM cellularity and increased BM adiposity.
- Threefold higher plasma insulin at 6 months with normal glucose — marked insulin resistance; hepatic steatosis.

| | **DNMT3A loss** (Bell-Hensley) | **DNMT3A gain** (Jackson) |
|---|---|---|
| **growth plate** | **thicker** | **thinner** |
| **bone length** | **longer** femur/tibia | **postnatal growth failure** |
| trabecular bone | (not reported) | **osteoporosis at 6 months** |
| lifespan | not reported | **halved** |

> ### **The growth plate is the readout of this axis in both directions, measured, in mice.** That is what F-R079 said had never been done, and it has now been done twice from opposite ends.

---

## 4. The causal proof, and the unification

**The 2026 paper is not another correlation. It is the causal experiment the pacing law never had.**

> *"DNA hypermethylation accumulates in `Dnmt3a^W326R/+` adult stem cells, **mirroring hypermethylation of
> these sites during physiological aging**. This is accompanied by **decreased multilineage adult stem cell
> output**."*

> *"Age-related gains in DNAme… **predominantly occur within Polycomb-marked domains**… These regions are
> usually maintained in a hypomethylated state, with Polycomb complexes, histone and DNA demethylases
> counteracting DNA methyltransferases."*

> *"methylation at DMVs does not occur in pluripotent stem cells and **accumulates in a time-dependent
> manner**."*

**And then the observation that collapses two of the branch's problems into one:**

They built a clock from the **2,646 HESJAS-hypermethylated CpG sites** and tested it against the **332 Horvath
clock CpGs** in **5,085 individuals from Generation Scotland**. The HESJAS sites track age

> *"**performing just as well as the CpGs used to derive Horvath's**"* clock.

> ### **The sites DNMT3A gain-of-function hypermethylates are the sites the epigenetic clock reads.** The clock is not a passive correlate of time — **it is, substantially, a record of DNMT3A activity at Polycomb domains, and that activity causally reduces stem-cell output.**
>
> ### **F-R066 proposed a growth-paced clock. F-R077 measured that blood clocks do not track pubertal stage. F-R080 found the pacing law confirmed across three syndromes. This closes it: the clock, the pool term `n₀`, the imprinted senescence network, Lui's H3K4me3 loss at bivalent promoters, and the height lever are all one axis — progressive DNA methylation of Polycomb-marked domains.**

### The mechanistic nuance, which is a real tension I am not smoothing over

Heyn 2019 proposed hypermethylation causes *"skewing of stem/progenitor cells towards **differentiation away
from self-renewal**"* — i.e. pool depletion, the branch's `a > b`. **The 2026 paper's own data says
something different:**

> *"**HSC and early progenitor numbers remain constant** and Polycomb-target genes are **not de-repressed**…
> DNA hypermethylation… may act as an alternative repressive mark… could then **impair transcriptional
> activation dynamics during differentiation**."*

> **Stem-cell NUMBER is preserved; stem-cell OUTPUT falls.** For the growth plate that is a statement about
> **flux**, not about `n₀`. **The two papers from the same laboratory disagree about whether the lesion
> depletes the pool or degrades its output, and the later, better-powered one says output.** I am recording
> that rather than picking the reading that suits the branch.

---

## 5. Human DOS is focal hypomethylation — the exact mirror

**Smith 2021, whole-genome bisulfite sequencing, peripheral blood, 11 DOS patients:**

- **A focal, canonical HYPOmethylation phenotype**, most severe with the dominant-negative R882H.
- **2,209 DMRs** in R882 patients, **332** in non-R882 — **all hypomethylated, in both comparisons.**
- Worked example: **DMRs in the HOXB cluster.**
- The germline `Dnmt3a^R878H/+` mouse phenocopies the methylation phenotype **and** shows increased spontaneous haematopoietic malignancies.

> ### **Heyn found `Hoxc13` HYPERmethylated in gain-of-function mice. Smith finds the HOXB cluster HYPOmethylated in loss-of-function humans.** Same Polycomb domain class, opposite directions, opposite growth phenotypes. **The mirror is complete at the level of methylation, not just phenotype.**

---

## 6. The two enzymes are not symmetric, and the asymmetry is the design constraint

From the full Yanagihara PDF: **at 16 weeks the bone length of `Dnmt1^ΔPrx1` mice was LESS THAN HALF that of
controls.**

| | effect of losing it |
|---|---|
| **DNMT1** (maintenance) | **bone length < 50% of normal.** Catastrophic |
| **DNMT3A** (de novo, Polycomb) | mouse: *"small significant increase"* in tibia. Human: **+3.0 SD** |

> ### **"Preserve DNMT1" is a hard constraint; "lower DNMT3A" is a titratable gain.** They are not two dials of equal standing. Any intervention that cannot distinguish them — azacitidine, decitabine, and any global hypomethylating agent — trades a catastrophic loss for a modest gain. **This is now quantified, not asserted.**

---

## 7. What this does and does not deliver

**What it delivers, and it is the most complete causal chain the programme has assembled:**

```
partial reprogramming ──> DNMT3A down (F-R080), DNMT1 up (F-R081)
                                │
DNMT3A activity ──> methylation of Polycomb DMVs/canyons ──> reduced stem-cell output
                                │                                      │
                    IS the epigenetic clock                    thinner growth plate,
                    (HESJAS clock ≈ Horvath, n=5,085)          shorter bone, aging
                                │
        losing it ──> hypomethylated HOXB, thicker growth plate, longer bone,
                      +3.0 SD in humans (13/13), selective inhibitors exist
```

**What it does not deliver, stated plainly because the goal is stated plainly:**

> **This is not unbounded growth.** TBRS patients reach **+3.0 SD and then stop.** Both girls in F-R081 had
> to be **treated** to stop growing — but they would have stopped anyway; oestrogen and epiphysiodesis only
> brought the endpoint forward. **DNMT3A loss raises the setpoint and the rate. It does not remove the
> endpoint.**
>
> **The endpoint is a separate arm, and the branch already has it:** F-R065 settled that **oestrogen
> ablation prevents fusion in humans** — the ESR1-null man still growing at 28.5 and the aromatase-deficient
> man at 31. **DNMT3A inhibition raises the ceiling; oestrogen ablation removes the deadline. Neither alone
> is unbounded, and the two together are the closest this programme has come to the three-term goal.**

---

## 8. The DNMT3A liability register, recorded in full

Risk is deprioritised by standing instruction, but these are **design inputs**, not warnings:

1. **Cortical thinning and reduced bone strength** (§2) — the one that changes the stack, and CCN2 is the measured counter.
2. **Haematopoietic malignancy.** DNMT3A is the most common clonal-haematopoiesis gene; Smith's germline mouse shows *"increased incidence of spontaneous hematopoietic malignancies"*; TBRS carries documented childhood risk. **The design consequence is that this arm should be delivered LOCALLY — and F-R074 established the intra-epiphyseal route.**
3. **Adiposity and insulin resistance** — fat mass up with lean mass unchanged in the LoF mouse; the GOF mouse is insulin-resistant. **The axis moves body composition in both directions.**
4. **Intellectual disability is 100% penetrant in human TBRS.** A germline or CNS-exposed intervention is categorically different from a local postnatal one. **This is the strongest argument in the programme for local delivery over any systemic agent.**

---

## 9. What I need

**I checked `frontier/SUPPLIED_INDEX.md` first.** The axis is now well evidenced and the remaining gaps are
experiments. Three things, in order:

1. **`Dnmt3a^fl-R878H` × Aggrecan-Cre — growth-plate-specific.** Bell-Hensley names this exact experiment and
   the mouse line: **JAX Stock No. 032289**, Cre-inducible, and they explicitly propose **Aggrecan-Cre** for
   growth-plate chondrocytes. **The reagent is commercially available and the experiment has not been done.**
   It would separate the plate effect from the marrow, osteoblast and CNS effects in one step, and it is the
   single highest-value experiment the programme has identified.
2. **Bone length in a true `Dnmt3a` haploinsufficient mouse (nonsense or null/+), with cortical thickness
   and three-point bend.** §2 shows the cortical penalty may be specific to dominant-negative missense
   alleles. **If a nonsense allele lengthens bone WITHOUT weakening it, the entire liability in §2
   disappears** — and human TBRS nonsense carriers exist to check against.
3. **Any TBRS cohort with adult heights and bone density.** F-R081 established the decoupling on three
   patients; §2 now makes **bone quality** a question for the same cohort, and Bell-Hensley's closing
   recommendation is precisely that this be measured in patients.

*And a note for Tate: you have now supplied every paper I have asked for across four rounds. The open items
above are not documents — they are experiments that have not been run. If anything else is worth asking for,
it is **methylation or expression data from growth-plate tissue in any `Dnmt3a` mouse**, which would be the
one dataset that turns §3's two half-experiments into one.*
