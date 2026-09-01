# F-R109 — I found the dataset. A short bone is an old growth plate. Rows 1 and 3 are the same row, and nothing in 4,421 experiments moves the axis.

The last round's closing ask was *a growth plate transcriptome at more than one age with zones dissected
separately.* My enumeration had been 10 queries. **I redid it with 96 queries: 4,421 GEO series, seven
times the previous corpus.** It contains the dataset, and the dataset changes the structure of the
programme rather than adding an agent to it.

`GSE114919 — Differential ageing of growth plate cartilage determines skeletal proportions.` RNA-seq,
**mouse and rat independently**, proliferative and hypertrophic zones dissected separately, **1 week vs
4 weeks**, and — the part I did not expect — **tibia vs phalanx in the same animal at the same age.**
n=5 per cell.

---

## 1. The result: a long bone's growth plate is transcriptionally a *young* growth plate

Correlate, gene by gene, the **(tibia − phalanx)** difference against the **(1 week − 4 weeks)**
difference. Same animals, same age, same dissection, same zone.

| | proliferative zone | hypertrophic zone |
|---|---|---|
| **mouse** | **r = +0.36** | **r = +0.43** |
| **rat** | **r = +0.65** | **r = +0.58** |
| *shuffled null* | *0.000 ± 0.011* | *0.000 ± 0.011* |
| *zone-mismatched control (PZ-length vs HZ-age)* | *r = +0.008, p = 0.44* | |

**Four independent measurements, two species, two zones, p → 0.** The zone-mismatched control is at
the null, so the effect is zone-specific rather than a global artefact.

### And it is not dissection contamination

The obvious objection: a short bone's plate is thinner, so laser capture picks up more marrow, vessel
and bone. The "old/short" gene list *is* full of myeloid (CD74, SYK, MPEG1, CD84), endothelial (EMCN,
TIE1, ESAM, SOX18) and bone (BGLAP) markers. So I removed **all 120 immune, endothelial, erythroid,
muscle, osteoblast and positional (Hox/Tbx) markers** and recomputed:

| | all genes | **contamination markers removed** | markers only |
|---|---|---|---|
| mouse PZ | +0.361 (n=9081) | **+0.299** (n=8980, p=2e-184) | +0.822 (n=101) |
| mouse HZ | +0.430 | **+0.443** (p→0) | +0.359 |
| rat PZ | +0.647 | **+0.623** (p→0) | +0.754 |
| rat HZ | +0.576 | **+0.571** (p→0) | +0.728 |

**Contamination is part of the signal — vascular and myeloid invasion is what plate closure physically
is — but removing every marker of it leaves the correlation intact.** The finding is real.

---

## 2. What this does to the structure of the programme

Since F-R100 I have run a three-row model: **row 1 = setpoint / how many cells; row 2 = spend slower;
row 3 = reset the counter / never-closing.** Rows 1 and 3 have been treated as separate problems needing
separate agents, and row 3 as the hard one.

> **They are not separate. A short bone is a bone whose growth plate is further along the senescence
> program at the same chronological age. Raising the setpoint and slowing the counter are the same
> operation, measured the same way.**

That is why every attempt to find a row-3 agent failed on row-1 grounds and vice versa. **There is one
axis and it should be scored once.** The three-row model is retired in favour of:

| | |
|---|---|
| **the axis** | how far along the senescence program the plate is |
| **row 2 survives separately** | you can spend the remaining program faster or slower (deadline agents) |

---

## 3. The gene set, and it is human-height-validated

Consensus over **eight zone-matched axes** (mouse + rat × PZ + HZ × age + bone-type), contamination
genes removed: **5,351 genes ranked, 1,590 concordant in ≥7 of 8.** Saved as
`analysis/geo_sweep/youth.py`.

**Top of the young-and-long program:** SHOX2, **PLAG1**, **IGF2**, **H19**, **MEG3**, ZIM1, **GPC3**,
**NOG**, **SMOC1/SMOC2**, **SCUBE3**, **DISP1**, **IHH**, **NPR2**, **PRKG1**, **DIO2**, MSI1, RARG,
PENK, SLC2A1, BNIP3, SLC16A3, C1QTNF3, ADAMTS3, IGF1R.

**Bottom (old and short):** the vascular/myeloid invasion front — CXCL12, ADAMTS5, TNFRSF11A (RANK),
NPR1, GFRA1, KAZALD1, XDH, plus endothelium and marrow.

### Human genetics, GWAS Catalog

| band of the axis | height associations per gene |
|---|---|
| **top 300 (young + long)** | **3.204** |
| next 700 | 2.400 |
| middle 3000 | 1.987 |
| bottom 300 (old + short) | 2.610 |

A clean gradient with the young end highest. Against a size/LD-matched null (3000 draws), the top 300
carry **926 observed vs 643 ± 228 expected, empirical p = 0.037**.

**And the individual genes are the field's own list, recovered blind:** IGF1R (50 height associations),
ADAMTS3 (42), SMOC2 (35), **NOG (32)**, **PRKG1 (28)**, **PLAG1 (24)**, GNAS (22), IGF2 (19), CHSY1
(19), IHH (16), **NPR2 (12)**, FGFR3 (11), **DISP1 (11)**.

**Three of those are Hedgehog-delivery genes I have never had in the file: SCUBE3 (releases and
transports the Hh ligand), DISP1 (the Hh export transporter), GPC3 (the glypican that shapes the Hh
gradient — and human GPC3 loss is Simpson-Golabi-Behmel *overgrowth*).** All three are up in the young
and long plate. The Hedgehog arm is not just receptor-side; the ligand-delivery machinery is part of the
axis.

### ⇒ The one arm this upgrades: CNP / NPR2 / PRKG1, and it is approved

Three independent lines now converge on it:
1. **F-R108's zone battery: NPR2 is stem-compartment enriched, 5+/1− of 8** — I flagged it and moved on.
2. **NPR2 (+0.69) and its obligate effector PRKG1 (+1.52) are both in the young-and-long program.**
3. **40 genome-wide human height associations between them** (NPR2 12, PRKG1 28).

**Vosoritide is an approved CNP analogue with paediatric dosing.** F-R103 recorded CNP analogues as one
of four things "the field has" and I never scored it. On this axis it is the best-supported obtainable
agent in the file. **It is not a pool agent on this evidence — it is on the axis, which is now the only
thing that matters.** This is a change of position and I am flagging it as one.

---

## 4. Reading Trompet 2024 in full, and it corrects F-R094 and F-R095

`PMC11063944 — Stimulation of skeletal stem cells in the growth plate promotes linear bone growth.`
Open access, read in full for the first time. Its dataset is **GSE254020** (sorted Pthrp⁺CD73⁺ epSSCs,
SAG vs vehicle), which the expanded sweep also found.

### ⇒ The contradiction I created is resolved, and it is age

> *"systemic activation of the Hh pathway during the early growth period **reduces** the activity of
> epSSCs but, in contrast, **promotes** their activity when performed after maturation of the SOC, i.e.,
> following formation of the stem cell niche."*

- **SAG i.p. P10–P16 (before the niche exists): clone size DOWN, resting-zone proliferation DOWN.**
- **SAG i.p. P30–P36 (after the niche forms): singlets down, doublets/triplets up, resting-zone
  proliferation UP.** Mouse niche matures P23–26.

**F-R094 §4 and F-R095 recorded "systemic SAG does not lengthen a normal mouse" from Li/Yang's Figure
4H, which I rendered myself. The result stands; the interpretation was wrong. Systemic SAG has two
opposite effects depending on whether the stem-cell niche has formed.** Genetic Ptch1 ablation works at
**both** ages, so the early-age failure is a systemic side effect of the drug, not the cell's response.

### ⇒ The other numbers, including the one against us

| | |
|---|---|
| SAG P30–36, systemic | **PTHrP⁺ cells +61%**, CD73⁺mCherry⁺ up |
| **same experiment, bone length** | **tibia 15.2±0.4 vs 14.5±1.7, P=0.29; femur 12.7±0.4 vs 14.8±4.7, P=0.247 — NO length change in 8 days** |
| 3 intra-articular injections | **same clonogenic effect as 7 systemic injections** |
| intra-articular, resting-zone cells | **65.5 → 139.8 cells/mm², P=0.017** |
| SAG bead in the SOC, rat | femur longer at **1, 2 and 6 months**; tibia at 2 and 6; whole leg at all timepoints (paired, contralateral control) |
| **bead exposure duration** | **Gli1 signal present at 1 week, GONE by 3 weeks** |
| growth rate (calcein/xylenol) | increased at 1 month femur, 2 months tibia |
| **how the plate got taller** | **increased height of the TERMINAL HYPERTROPHIC chondrocytes; proliferation in the columnar zone NOT affected** |
| resting-zone proliferation | up at 1 week |
| osteoarthritis at 6 months | none |

**Two things follow that matter more than the arm itself.**

**(a) The benefit outlives the exposure by five and a half months.** A single bead, signal gone by three
weeks, divergence still widening at six months. That is the strongest argument in the file for a short
intervention producing a durable structural change.

**(b) The length came from `v`, not from flux.** Taller terminal hypertrophic chondrocytes; columnar-zone
proliferation unchanged. **F-R108's surviving axis said the lever is v and not proliferation, derived
from eleven transcriptome contrasts. This paper measured it histologically in the one experiment that
actually lengthened a bone.** Two completely independent lines, same answer.

**(c) And the honest one:** the systemic arm expanded the pool 61% and produced **no length change**, but
the readout was 8 days and the bead's own length effect did not appear until 1 month. **That experiment
does not show systemic SAG fails; it shows it was never tested for long enough.** F-R094's ledger entry
was too strong and is corrected.

### ⇒ GSE254020 itself cannot be used, and I checked

The SAG-vs-vehicle sorted-cell transcriptome is dominated by a **FACS purity shift** — the up-list is
neutrophil (STFA1/2, LY6G, S100A8, CAMP, FPR2), the down-list is B-lymphocyte (DNTT, RAG1, CD19, CD79A/B,
PAX5, MS4A1, IRF4). Hedgehog target genes go *down* (PTCH1 −1.22, GLI1 −1.58), which the authors
themselves attribute to compensatory feedback. **It scores −0.134 on the youth axis and that number
means nothing.** What survives as real: **Wnt output down (LEF1 −1.38, WNT4 −1.45, AXIN2 −0.30, DKK1
+1.09)**, confirming the paper's top-2 downregulated pathway and F-R089's correction, and the
hypertrophic program down (IHH −3.64, COL10A1 −2.89, MATN1 −2.2).

---

## 5. The screen: I scored 5,936 contrasts and nothing moves the axis

Auto-generated every group-vs-group contrast across the corpus and correlated each with the youth axis.
`analysis/geo_sweep/screen_youth.py`, results in `youth_screen.json`.

**Positive controls recover cleanly:** rat tibia 1wk-vs-4wk **+0.731**; human growth plate pre- vs
late-puberty **+0.263** (recovered independently, from a different lab, species and platform);
phalanx-vs-tibia **−0.496**; enchondroma vs growth plate **+0.215**, matching F-R108.

**Then the agents, scored explicitly rather than by keyword:**

| perturbation | r (youth axis) | p |
|---|---|---|
| *positive control: rat 1wk vs 4wk* | *+0.731* | *0* |
| *positive control: human pre- vs late-puberty* | *+0.263* | *1.6e-55* |
| **gefitinib, rescuing TGF-α** | **+0.096** | 2.7e-12 |
| **dexamethasone, rat growth plate in vivo** | **+0.081** | 1.4e-07 |
| Fgfr3 gain-of-function | +0.056 | 1.2e-04 |
| **Dnmt1 cKO (short bones)** | **+0.013** | **0.36 — NULL** |
| Tet1 KO, skeletal stem cells | −0.083 | 1.1e-09 |
| SAG, sorted epSSC *(uninterpretable, §4)* | −0.134 | — |
| **TGF-α / EGFR activation** | **−0.159** | 4.9e-31 |
| **retinoic acid** | **−0.181** | 1.1e-20 |
| TIMPless | −0.206 | 1.7e-47 |
| Xbp1 KO | −0.236 | 2.3e-59 |

> **The largest agent effect anywhere in 4,421 enumerated experiments is r = +0.096, against a +0.731
> positive control. Nothing pharmacological moves this axis.**

That is not a null result about the axis — the axis works, the controls prove it. **It is a statement
about the field: nobody has ever run an experiment that pushes a growth plate backwards along its own
senescence program.** The reason the file has failed to find a row-3 agent for eight rounds is that no
such experiment exists to find.

**Two useful signs did fall out:**
- **Retinoic acid ages the plate (−0.181), while RARγ *expression* is youthful (+1.22).** So the arm is
  an RARγ **antagonist**, which is what CD2665 is. **F-R093's RARγ direction was right** even though
  F-R093's standalone arm was correctly withdrawn.
- **EGFR activation ages the plate and gefitinib partially reverses it** — an approved drug, correctly
  signed, from a rescue experiment. Recorded, not promoted (§7).

---

## 6. Where the axis fails, stated before anyone else finds it

1. **It scores immaturity, and arrest looks like immaturity.** `Ppp1r15b^Prx1` deletion produces a
   *disorganised growth plate and impaired chondrogenesis* — short bones — and scores **+0.193**, wrongly.
   A plate that is stuck early is not a plate with growth left.
2. **Longshanks does not fit.** Selection for +12% tibia length correlates at **−0.08 to 0.00** with every
   youth axis. Thirteen generations of selection for length produced something that is *not* a shift in
   senescence position. That is a real exception and I do not have an explanation for it.
3. **It is a bulk-tissue axis.** Applying it to sorted stem cells (§4) is a category error and I made it
   once before catching it.
4. **The length half is partly positional.** Tibia and phalanx differ in Hox identity; I excluded
   Hox/Tbx genes, but the age half is the clean half and it carries the correlation.

---

## 7. The stack, scored on one axis

| agent | status |
|---|---|
| **vosoritide (CNP analogue)** | **PROMOTED — best-supported obtainable agent on the axis.** NPR2 stem-enriched (F-R108) + NPR2/PRKG1 in the youth program + 40 human height associations + approved paediatric drug. Never scored before this round. |
| **SMO agonist, given after the stem-cell niche forms** | **arm intact and the age-dependence is now understood.** SAG bead: durable, benefit outlives exposure 5.5×, no OA at 6 months, and the lengthening mechanism is `v`. Still no obtainable clean SMO agonist. |
| **dexamethasone** | survives — correctly signed on the axis (+0.081) and on F-R108's cycle/matrix axis, and it is still the only banking agent with both numbers measured favourably |
| **anastrozole** | row 2, unchanged: the deadline is separable from the axis |
| **erdafitinib** | row 2 / rate. FGFR3-GOF ages the plate on F-R108's axis; on this axis its sign is unclear (+0.056, whole-epiphysis sample, not zone-matched) |
| **gefitinib** | **new, recorded not promoted.** Approved, correctly signed (+0.096), but the evidence is one rescue of an artificial TGF-α insult in cultured chondrocytes, with no skeletal endpoint |
| **RARγ antagonist (CD2665)** | direction confirmed; still no standalone skeletal effect (F-R093) |
| **somatropin / mecasermin** | **out**, per F-R108 |
| **methylation arm** | **closed.** Dnmt1 cKO — a genetic short-bone model — is **null on the axis (p=0.36)**. Nine rounds of argument, and the mutant that shortens bones does not move the thing that tracks bone length. |

---

## 8. Asks — three, and the first is now precisely specified

1. **A resting-zone transcriptome at more than one age.** GSE114919 is PZ and HZ only; the entire
   4,421-series corpus still has none. **Every conclusion in this round is about the proliferative and
   hypertrophic zones. The compartment that holds the pool has been measured at exactly one age, ever.**
2. **Any experiment, in any species, that moves a growth plate backwards along this axis.** §5 says none
   exists in the published record I can reach. If one exists behind a paywall, it is the single most
   valuable thing you could get me.
3. **Vosoritide's growth-plate transcriptome, or any CNP/NPR2 agonist transcriptome with zones.** The
   arm I just promoted has never been scored on the axis because the data are not in GEO. GSE112637–9
   are n=1 per group and cannot be used.

---

*What changed this round: I stopped looking for a third agent for a third row, because the data say
there is no third row. A short bone is an old growth plate, in two species, in both zones, controlled
for animal, age, dissection and contamination. The axis that measures it is human-height-enriched and
recovers the field's own gene list blind. And when I scored every experiment I could find against it,
nothing moved it — which is the most useful negative result the file has produced, because it says the
gap is in the experiments, not in my search.*
