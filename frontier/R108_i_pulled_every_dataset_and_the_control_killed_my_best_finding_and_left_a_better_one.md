# F-R108 — I pulled every dataset. The zone result confirms SMO in six species. My best new finding died to its own control. What survived inverts how the stack should be built.

You said: *test everything, get every dataset.* I did. **622 GEO series enumerated, all 622 downloaded,
264 loaded to gene symbols across 7 species, 205 scored.** Scripts and outputs in
`frontier/analysis/geo_sweep/`; the full corpus listing with every sample label is `catalog.txt`.

**Three things happened. One arm was confirmed harder than it has ever been. One of my own previous
rounds failed to replicate. And the most exciting result of this round was killed by the control I ran
on it — which left behind something better and more actionable.**

---

## 1. The zone battery: nine datasets, six species. SMO is confirmed, and four agents move.

Full table: `analysis/geo_sweep/zone_battery.out`. Stem/resting compartment minus differentiated, log2.

Datasets: rat (Baron, GSE16981/23432), **human (GSE9160)**, rat femur (GSE9537), rat 10-day (GSE54216),
**mouse (GSE87605)**, **bovine (GSE18738)**, **mouse label-retaining stem cells (GSE160364)**,
**chick (GSE18568)**.

### ⇒ SMO: 5 positive, 0 negative, 4 at zero, of 9. **It is not depleted in the stem compartment in any species.**

| | rat | rat2 | **HUMAN** | rat-femur | mouse | bovine | mouse-LRC | rat-10d | chick |
|---|---|---|---|---|---|---|---|---|---|
| **SMO** | +0.44 | +0.68 | **+0.45** | **+2.44** | +0.46 | +0.07 | +0.17 | −0.22 | +0.02 |

**And the pathway *output* is low in the same cells:** GLI1 4/8 negative, PTCH1 3/9 negative, IHH 6/9
negative, **BOC (the positive co-receptor) 6/8 positive**. **Receptor present, co-receptor high, ligand
absent, output off — the maximum-headroom configuration for an agonist, now in six species instead of
one.** This is the strongest form F-R092's argument has ever taken.

**SUFU is 0 positive / 5 negative of 8** — the Hedgehog brake is already low in the resting zone. That
is a mechanistic reason Xiu's Agc1-Cre Sufu deletion shortened bones (F-R105): deleting a brake that is
already off in the target cell does most of its work in the wrong zone.

**HHIP splits by clade:** rodent RZ +1.63/+2.91/+0.86/+1.16, but **human −0.57** and chick −0.64. The
decoy enrichment I have quoted since F-R092 is a rodent feature. **The human root has less HHIP than its
proliferative zone, not more** — which makes the human case for a SMO agonist better, not worse.

### ⇒ Four agents move on this table

| gene | result | consequence |
|---|---|---|
| **PTH1R** | **1+/7−/1· of 9** | **abaloparatide is demoted.** PTHLH is 8+/0− (the RZ *makes* the ligand); the receptor is in the proliferative zone. Abaloparatide acts on the PZ, so it is a **rate/deadline agent, not a pool agent.** F-R089's "maintains RZ quiescence" framing was wrong about the cell it acts on. |
| **ESR1 / ESR2** | 2+/4− and **1+/6−** | **oestrogen receptors are not resting-zone-enriched.** F-R083's "ESR1 is a resting-zone gene" does not replicate. Nilsson 2014's irreversible RZ depletion is real but the mechanism is **indirect**. Anastrozole survives on its measured outcome, not on this mechanism. |
| **NPR2** | **5+/1− of 8** | **new.** The CNP receptor *is* enriched in the stem compartment. **Vosoritide (approved) may have a pool component nobody has looked for.** Not an arm yet — flagged. |
| **FGFR3** | 2+/5− | erdafitinib acts on the proliferative zone. **Confirms its placement as a flux agent, not a pool agent.** |

---

## 2. F-R107 §1 does not replicate — and the reason retires four rounds of argument

F-R107's headline was that the resting zone is a **DNMT3A compartment (8.9× DNMT1)**, and I used it to
reject pirfenidone *"on the data rather than on the caution."*

**Across nine datasets and six species:**

| gene | verdict |
|---|---|
| DNMT3A | 4+/2−/3· — **human −0.01** |
| DNMT1 | 4+/2−/3· |
| TET1 | 3+/3− |
| TET2 | 3+/1−/3· |

**None of it replicates. The 8.9× was one array in one species and I built a conclusion on it.**

**And the deeper finding, which is the useful part.** When I score the methylation machinery across the
eleven length-varying contrasts (§4), it moves — but it moves **in lockstep with the cell-cycle module**,
because DNMT1, UHRF1 and PCNA are replication-coupled. Once the cell-cycle component is removed, the
methylation signal has no independent existence.

> **DNMT/UHRF/TET *expression* in bulk cartilage is a proliferation readout, not a methylation readout.**

**F-R104, F-R105, F-R106 and F-R107 all argued about row 3's direction from exactly this kind of
transcript evidence. That entire line of argument is uninterpretable and I am retiring it.** Pirfenidone
stays out, but on F-R106's reason — it raises DNMT3a at p<0.0001 and DNMT3A loss is +3.0 SD in humans —
which is human genetics and does not depend on any of this.

*One correction inside the correction:* F-R107 §3 said **DNMT1 produces no height phenotype in humans.**
That is true of the rare HSAN1E allele. It is **false of common variation** — the GWAS Catalog carries
**10 genome-wide height associations at DNMT1, minimum p = 5×10⁻¹⁵⁴**, and **18 at TET1, p = 9×10⁻²³²**.
I overstated it.

---

## 3. Two datasets in the corpus where the phenotype *is* bone length

Nobody in this file has ever looked at an experiment where length itself was the variable.

- **GSE189528 — Longshanks.** Mice selectively bred 13 generations for longer tibiae; **+11–12%**.
  Proximal tibial growth plate at P14, vs random-bred controls from the same stock. n=3 pairs.
- **GSE53277 — Great Dane vs Miniature Poodle growth plate.** The largest within-species length
  difference obtainable. n=6 vs 5.

Concordant genes (Longshanks all-3-pairs, dog p<0.05, same sign): **100.** The negative half is
erythroid and muscle contamination (GATA1, KLF1, HBB, MYH2) and I discarded it. The positive half was
dominated by one thing:

**PAPSS2 +0.51/+1.91 · GFPT1 +0.39/+1.10 · GFPT2 +0.41/+0.61 · HAS2 +0.58/+1.46 · CSGALNACT1
+0.56/+0.91 · HAPLN1 +0.94/+1.45 · SLC2A1 +0.57/+0.98 · PGK1 +0.46/+1.07 · MEST +0.60/+0.70**

The hexosamine → UDP-sugar → PAPS → GAG-chain supply chain. **The proteoglycan synthesis pathway —
which I closed in F-R100.**

### It validated everywhere I pointed it

Scoring the whole pathway (not just the concordant genes) across eight independent contrasts, every
sign was correct: **Longshanks +, Great Dane +, enchondroma +, dexamethasone +, skeletal stem cell +;
Dnmt1-cKO −, Fgfr3-gain-of-function −, human late-puberty −.** The human growth plate loses the entire
module between pre-puberty and late puberty (PAPS −0.73, UDP-sugar −0.74, GAG-chain −0.42). **8/8.**

### And the human genetics is real, and it is not a tissue artefact

GWAS Catalog, height associations:

| gene | hits | min p | | reference tier | hits | min p |
|---|---|---|---|---|---|---|
| **CHSY3** | 10 | **8×10⁻²⁴⁰** | | ACAN | 90 | 1×10⁻³⁰⁰ |
| **CHSY1** | 19 | **3×10⁻²⁰⁸** | | HHIP | 64 | 1×10⁻³⁰⁰ |
| **CSGALNACT1** | 16 | 4×10⁻⁷⁸ | | PTCH1 | 61 | 1×10⁻³⁰⁰ |
| **B4GALT7** | 1 | 9×10⁻⁷⁸ | | DNMT3A | 20 | 1×10⁻³⁰⁰ |
| **GFPT2** | 11 | 1×10⁻³⁰⁰ | | NPR2 | 12 | 6×10⁻¹⁸¹ |
| **UST / EXTL3 / CHST11 / XYLT1 / PAPSS2** | 13/12/10/6/1 | 1e-54 … 3e-35 | | FGFR3 | 11 | 4×10⁻⁶³ |

**134 genome-wide-significant height associations across 49 pathway genes.** Against a null matched on
each gene's total GWAS record count (a proxy for gene size, LD and study power), 3000 draws:
**observed 134 vs null mean 69.5 ± 21.8, empirical p = 0.009.**

---

## 4. Then I ran the control, and it killed it

The obvious confound: a growth plate sample from a Great Dane may simply be **purer cartilage**. Every
chondrocyte gene would rise together and the module would ride along.

**So I re-scored every module against the general cartilage-matrix program (ACAN, COL2A1, COMP, MATN1,
COL9/11, SOX9, …) instead of against the dataset mean. If a module is only tracking how much cartilage
is in the sample, it sits at zero.**

| module, normalised to matrix | Longshanks | GreatDane | Dnmt1cKO | Fgfr3GOF | enchondroma | HUMAN late-pub | dex |
|---|---|---|---|---|---|---|---|
| HEXOSAMINE | −0.13 | +0.17 | +0.48 | +0.53 | +0.02 | +0.73 | +0.14 |
| PAPS / SULFATE | −0.15 | +0.33 | +0.30 | +0.37 | −0.04 | +0.39 | +0.11 |
| GAG CHAIN | −0.15 | −0.14 | +0.30 | +0.46 | −0.06 | +0.75 | +0.12 |
| SULFOTRANSFERASES | −0.35 | −0.11 | +0.31 | +1.13 | −0.53 | +0.88 | −0.02 |
| **METHYLATION** | −0.50 | −0.37 | +0.26 | +1.07 | −0.80 | +1.23 | −0.27 |

**Every sulfation and hexosamine module collapses to noise, and where it is not noise it points the
wrong way.** The 8/8 in §3 was the cartilage-matrix program, and the module was a passenger.

**The sulfation arm stays closed. It is now closed for a better reason than F-R100's:** not "the
substrate is not limiting," but **"the pathway carries no signal independent of the general chondrocyte
program in any system where length varies."** The GWAS enrichment is real and is not subject to this
confound — genetics does not care about dissection purity — so I am keeping it on the ledger as a
**lead, not an arm**, with the note that expression evidence does not support it.

**I am reporting this because I nearly wrote you the opposite round.** The exciting version of §3 was
written before I ran §4.

---

## 5. What survived the control — and it inverts how the stack should be built

One module got **stronger** after normalisation, in the opposite direction: **the cell cycle.**

`analysis/geo_sweep/cycle_matrix.out` — 40 cell-cycle genes minus 17 matrix genes:

| contrast | expect | CART | **CYCLE − CART** | |
|---|---|---|---|---|
| Longshanks (LONGER) | + | +0.39 | **−0.73** | OK |
| Great Dane (LONGER) | + | +0.32 | **−0.74** | OK |
| enchondroma vs growth plate | + | +0.43 | **−1.26** | OK |
| enchondroma vs growth plate, 2nd set | + | +0.60 | **−1.14** | OK |
| dexamethasone (banking) | + | +0.13 | **−0.33** | OK |
| Dnmt1-cKO (SHORT) | − | −0.73 | **+0.35** | OK |
| Fgfr3-GOF 3–4wk (SHORT) | − | −1.04 | **+1.60** | OK |
| *Fgfr3-GOF 1–2wk (pre-phenotype)* | − | +0.18 | −0.36 | XX |
| HUMAN late vs pre puberty | − | −1.20 | **+0.87** | OK |
| HUMAN late vs early puberty | − | −1.16 | **+1.00** | OK |
| rat PZ 12wk vs 3wk | − | −0.13 | **+0.19** | OK |

**10 of 11, across six species, four independent laboratories, and every kind of perturbation in the
corpus. The single failure is the Fgfr3 mutant at 1–2 weeks — the timepoint before its phenotype
appears.**

> **Relative to what its cells produce, a growth plate that makes long bones cycles LESS. A growth plate
> that is closing, or that is genetically short, cycles MORE.**

**This is F-R058's identity — `dL/dt = flux × v(d)` — recovered from transcriptomes I had never
looked at. It says the lever is v, not flux.** And it makes the acceleration seen in a closing plate
legible: **a plate spending its last divisions cycles hard. A plate holding a pool cycles slowly.**

### What it does to the stack, plainly

| agent | mechanism | sign on this axis |
|---|---|---|
| **dexamethasone** | lowers cycling, raises matrix | **correct** — and it is the banking agent, so this is a second independent reason for it |
| **erdafitinib** | FGFR3-GOF raises cycling **+1.60**; inhibition lowers it | **correct** |
| **abaloparatide** | PZ-acting (§1) | rate axis, correct sign, **wrong row** — it is not a pool agent |
| **SMO agonist** | Gli1+ progenitors carry the long-bone program (+0.41) | **correct**, and §1 makes the target cell certain |
| **somatropin / mecasermin** | act by **raising proliferation** | **WRONG SIGN on the axis that survived every control in this round** |

**F-R089 already had somatropin as pool-negative at 0.07 mg/kg/day and I reduced it toward
physiological. This is an independent second reason, from a different kind of evidence, and it applies
to mecasermin too, which F-R089 established buys zero pool.** I am not going to keep an agent in the
stack whose only mechanism is the one variable that runs backwards in ten of eleven length systems.

---

## 6. Two things worth having that I am not overselling

**Enchondroma is the corpus's only "never-closing" cartilage, and it scores where the theory says.**
Ollier enchondromas are persistent ectopic growth-plate cartilage. In two independent datasets they sit
**above normal growth plate** on the length program and have the **lowest relative cycle load of
anything measured (−1.26, −1.14)** — while chondrosarcoma scores *below* enchondroma, so this is not a
generic tumour effect. They are IDH1/2-mutant. **I checked whether the methylation machinery explains
it and it does not** (DNMT1 −0.61, UHRF1 −1.72 in enchondroma) — so I am not building the hypermethylation
story I started to write. What enchondroma gives is a **phenotype that matches the target state**, in
human tissue, with no obtainable agent attached.

**Glucosamine + chondroitin, oral, is the one agent that moves this pathway — and the experiment is
the rescue law again, with one exception.** `PMC4286662`, OVX rats, 60 days, n=10/group. Comparisons in
the paper are all against **OVX-vehicle**, not against sham. Reading the sham column myself:

| | GS-treated OVX (GE60GS) | **sham control (GC60)** | OVX vehicle (GV60) |
|---|---|---|---|
| resting-zone chondrocytes (%) | **19.5 ± 0.5** | **15.0 ± 0.4** | 8.0 ± 1.2 |
| proliferative (%) | **58.5 ± 0.6** | 47.5 ± 3.7 | 43.0 ± 3.0 |
| proliferative thickness (µm) | **81.5 ± 1.5** | 66.5 ± 0.0 | 48.0 ± 1.4 |
| hypertrophic (%) | 22.0 ± 0.8 | 37.5 ± 0.1 | 49.0 ± 2.2 |
| **total cartilage thickness (µm)** | **156.5 ± 5.0** | **156.5 ± 1.4** | 158.5 ± 1.4 |

**Resting and proliferative fractions exceed the sham control; the authors never tested that comparison.
But total plate thickness is identical in every group and no bone length was measured.** That is
F-R099's stock-is-not-flow, and RZ *thickness* actually fell (31.5 vs 39.5) while RZ *percentage* rose,
so part of the effect is re-proportioning. **This is the second experiment in the entire file where a
parameter exceeds the normal control** (after Trompet's bead) — and it is a composition percentage in an
adult ovariectomised rat with no length endpoint. **Recorded, not promoted.**

---

## 7. Corrections to my own file

1. **F-R107 §1 (RZ is a DNMT3A compartment, 8.9×) — does not replicate.** 9 datasets, 6 species.
2. **F-R107 §3 (DNMT1 has no human height phenotype) — overstated.** True for HSAN1E; false for common
   variation (10 hits, p = 5×10⁻¹⁵⁴).
3. **F-R104/105/106/107's whole argument from DNMT/TET expression — uninterpretable.** It is a
   proliferation readout. The conclusion (no pirfenidone) survives on F-R106's human-genetics reason.
4. **F-R083 (ESR1 is a resting-zone gene) — does not replicate**, 1+/6− for ESR2, 2+/4− for ESR1.
5. **F-R089's abaloparatide framing — wrong cell.** PTH1R is 7/9 depleted in the resting zone.
6. **F-R092's HHIP-decoy geometry is rodent-specific.** The human reserve zone has *less* HHIP.
7. **GSE23432 is not simply a duplicate of GSE16981** (F-R107 working note). Samples 0–14 are shared;
   GSE23432 adds epiphyseal cartilage and the proliferative-hypertrophic transition zone. The
   "3 independent RZ-vs-PZ datasets" count was right; the dataset is not redundant.
8. **F-R100's sulfate closure was right, for an incomplete reason.** Substrate is not limiting *and*
   the pathway carries no length signal independent of the general chondrocyte program.

---

## 8. Where the rows stand

| row | status after the sweep |
|---|---|
| **1. setpoint / cells** | **strengthened.** SMO enriched or neutral in the stem compartment in 6 species, 0/9 negative, with ligand absent and output off in the same cells. Gli1+ progenitors carry the long-bone program. Still no obtainable clean SMO agonist. |
| **2. spend slower** | **strengthened, and re-derived.** Dexamethasone is correctly signed on the one axis that survived every control. Anastrozole survives on outcome; its RZ mechanism is indirect. Abaloparatide moves to the rate axis. |
| **3. never-closing** | **the methylation route is retired as unmeasurable from these data.** What replaces it is a *readout*, not an agent: relative cycle load is a transcriptome-measurable proxy for whether a plate is holding or spending. Enchondroma is the phenotype; no agent attaches to it. |
| **removed** | **somatropin and mecasermin are wrongly signed** on the surviving axis. |

## 9. Asks — and they are narrower than they have ever been

1. **Any experiment that lowers chondrocyte proliferation without lowering matrix output and measures
   bone length.** That is the single test of §5. Dexamethasone does both halves and was never measured
   for length past control fusion. *(Searched; not found.)*
2. **Any bone-length endpoint after glucosamine or N-acetylglucosamine in a normal, non-ovariectomised
   growing animal.** PMC4286662 is the only in-vivo growth-plate experiment and it has no length. *(Searched.)*
3. **Stevens, Boyer & Bowen 1999** — still outstanding, four rounds now.
4. **Any transcriptome of a growth plate at more than two ages with the resting zone dissected
   separately.** The whole corpus has none; GSE16981's RZ is 1-week only. This is the measurement that
   would let §5 be tested where the pool actually lives.

---

*The honest summary of the round: I got every dataset, as you asked. The zone result is the strongest
confirmation the Hedgehog arm has ever had. My best new finding — a human-genetics-backed proteoglycan
axis at p=0.009 — did not survive its own control, and I am telling you that rather than the version I
had already written. What survived is smaller, holds in 10 of 11 systems across six species, and says
two of the agents in our stack are pushing the wrong variable.*
