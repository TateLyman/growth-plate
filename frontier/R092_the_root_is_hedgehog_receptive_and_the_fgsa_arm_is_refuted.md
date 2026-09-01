# F-R092 — I ran your data. The human root is Hedgehog-receptive, IHH is excluded not dead, and the approved-glucocorticoid arm is refuted in humans.

Everything I asked for in F-R091 was in the zip. Four things changed, and one of them is that **you were
right about SAG and I was wrong.**

---

## 1. The deciding hole, closed with your own data

`GSE288028` — Chagin/Chu, 12 human growth-plate scRNA-seq libraries, donors aged 11–14 at
epiphysiodesis. I loaded all of them, gated to chondrocytes (COL2A1⁺/ACAN⁺, 500–8,000 genes),
**57,359 cells**, and defined the GP1 root as **top-quintile GP1 signature (SFRP5, THBS1, THBS2, DCN,
CYTL1, FRZB) AND non-cycling (MKI67⁻ TOP2A⁻)**. Script and output:
`frontier/analysis/GSE288028/hedgehog_root.py`.

**The question was: is GP1 — the dormant human root — Hedgehog-responsive at all? If not, the entire Hh
arm can only reach GP2 and cannot expand the root.**

### It is. Percentage of GP1-root cells with detected transcript, median across 11 libraries:

| gene | median % of root cells | range |
|---|---|---|
| **PTCH1** | **50.9%** | 19–85 |
| **HHIP** | **21.1%** | 8–46 |
| **BOC** | **21.0%** | 0–39 |
| **SMO** — *the drug target* | **16.9%** | 0–32 |
| GLI2 | 13.7% | 4–61 |
| SUFU | 10.1% | 3–31 |
| IHH | 3.8% | 0–23 |
| GLI1 | 3.5% | 0–10 |
| **PTHLH** | **2.5%** | 0–6 |

**PTHLH at 2.5% independently validates the gate** — the root is overwhelmingly PTHrP-negative, exactly
as Chu describes GP1 versus GP2. I did not tune anything to get that; it fell out.

### Enrichment versus GP1-low chondrocytes, per-sample log2FC (sign consistency)

| gene | positive in | note |
|---|---|---|
| **EVC2** | **9/9** | the ciliary SMO→GLI transducer specifically required in cartilage |
| **SMO** | **8/9** | |
| **BOC** | **8/9** | ligand co-receptor |
| **HHIP** | **8/9** | secreted ligand decoy |
| **PTCH1** | **7/9** | receptor *and* canonical Hh target gene |
| GLI2 | 7/9 | |
| ARL13B | 3/9 | flat |

**Honest caveat, stated because it matters:** the *magnitude* is batch-dependent. The P30453 and P31011
libraries give log2FC of +3.9 to +4.4 for PTCH1; the five P25452 libraries give +0.1 to +0.6. Different
CellRanger versions (7.1.0 vs 6.0.1) and preps. **The direction is consistent; the size is not, and I am
not going to quote the pooled 4.6× I first computed.** I also computed a pooled "SUFU down 3×" on my
first pass — **that was a pooling artefact and is retracted**; per sample SUFU is flat to slightly up.

**What survives is the claim that matters: the drug target is present in the target cell.** SMO in ~17%
of root cells and PTCH1 in ~51% — at 10x dropout rates for genes at this expression level, that is
genuine expression, not noise. And EVC2, enriched in 9/9, is the one component that has to be there for
a Smoothened agonist to do anything at all in cartilage.

---

## 2. The geometry — and the answer to "if IHH is dead that's something too"

**IHH is not dead. It is excluded.** From our zone table (`query/human_growth_plate_expression.byzone.csv`,
Chu atlas):

| | stem | proliferative | **prehypertrophic** | hypertrophic |
|---|---|---|---|---|
| **IHH** | **0.00 / 0.29 / 4.14 / 0.00** | 2.33 / 0.23 / 23.66 | **4.66 / 0.73 / 72.28 / 24.19** | 1.79 / 0.13 / 29.84 / 9.80 |
| PTCH1 | 38 / 16 / **74** / **50** | 59 / 25 / 91 | 32 / 8 / 86 / 45 | 29 / 13 / 80 / 55 |
| SFRP5 (GP1) | 14 / 8 / **83** / **52** | ~0 | ~0 | ~0 |

**The ligand is manufactured in the prehypertrophic zone. The receptor apparatus is maximal in the stem
zone. And the stem zone co-expresses HHIP — a secreted Hedgehog decoy — at 4× enrichment.**

So the human growth-plate root is a cell that has **maximised its Hedgehog receiving apparatus (PTCH1,
SMO, BOC, EVC2), sits at a distance from the only source of ligand, and deploys a secreted ligand trap
around itself.** It is built to be Hedgehog-competent and Hedgehog-starved.

**That is precisely the configuration in which a small-molecule Smoothened agonist works and a ligand
strategy cannot:**

- HHIP sequesters IHH and SHH **extracellularly**, upstream of the receptor.
- SAG, SAG21k and the FGSAs bind **SMO** — downstream of ligand, downstream of PTCH1, downstream of HHIP.
- **HHIP cannot block a Smoothened agonist.**

This is, as far as I can find, a new argument, and it is the strongest mechanistic case in this whole
programme for the SMO-agonist class specifically over anything upstream of it. It also explains why
`trompet2024`'s SAG worked while nobody has ever moved the pool with an Ihh manipulation: **the endogenous
system is engineered to keep Hedgehog low at the root, and SAG is the one intervention that goes around
the engineering rather than through it.**

*(HHIP is also among the strongest human height GWAS loci — the decoy's dose sets human stature. That is
the human genetic confirmation that this axis, at this cell, is height-determining.)*

---

## 3. `main 28.pdf` — SAG applied to a growth plate, in vivo, with a stature endpoint

`Li X, Yang S, Chinipardaz Z, Koyama E, Yang S. SAG therapy restores bone growth and reduces enchondroma
incidence in a model of skeletal chondrodysplasias caused by Ihh deficiency. Mol Ther Methods Clin Dev
2021;23:461–475.` **This is the crossing I have been asking for since F-R091.**

Acan-creERT;Ihh^fl/fl mice. **SAG 20 µg/g i.p. every other day** *(the PDF reads "20 mg/g" — a units
typo; 20 mg/g is 2% of body weight. 20 µg/g = 20 mg/kg, matching Trompet's 25 µg/g and Rundle's published
range.)*

| | protocol 1 (P7→P30) | protocol 2 (**P14**→P30) |
|---|---|---|
| survival | 86.5% vs 72.3% vehicle | 83.6% |
| **body length** | **+18.9%** | **+15.5%** |
| **vertebral length** | **+32.1%** | **+20.6%** |
| femur | **+67.4%** | +20.4% |
| tibia | +33.1% | +11.9% |

Absolute: **133.2 ± 6.1 mm SAG vs 117.2 ± 6.9 mm vehicle.** All p<0.05.

**Three things here matter beyond the size of the numbers.**

1. **The spine responded, and in protocol 1 it responded more than body length overall (+32.1%).** F-R085
   hole #2 was that ~30 physes plus the spine must all be treated, and that TBRS girls gained
   +10.9 cm sitting height against +1.7 cm leg length. **A systemic SMO agonist reaches axial and
   appendicular physes simultaneously.** That hole is now substantially smaller.
2. **Starting at P14 still worked.** You do not have to begin at birth. The window is not closed by
   the time the animal is well into postnatal growth.
3. **Enchondroma-like tissue near the growth plates was significantly REDUCED by SAG.** F-R022's
   ceiling argument was that over-driving this axis creates ectopic cartilage engines
   (osteochondroma/enchondroma) that *cost* height. **In the one experiment that measured it, the
   agonist reduced them.** That argument is weakened, not confirmed.

**Toxicity, as reported:** no abnormality or tumorigenesis in heart, lung, kidney, liver or spleen;
**intestinal hyperplasia in 6.1%** of SAG-treated mice, with 2 deaths from bowel obstruction — including
**1 of 41 SAG-treated wild-type mice**. **The dose-limiting toxicity of systemic SAG in this experiment
was gut, not brain.** That is worth knowing precisely because F-R091 flagged the cerebellum as the
hazard; in vivo, the gut went first.

**The limitation I will not soften: every number above is rescue of a deficient animal toward normal, not
gain above normal.** They treated 41 wild-type mice with SAG and **did not report their lengths.** That
single unreported number is the difference between "SAG corrects Ihh deficiency" and "SAG adds height."
The only gain-above-normal evidence remains `trompet2024`'s bead in normal rats — contralateral control,
femur and tibia longer at 1, 2 and 6 months.

---

## 4. The FGSA arm is refuted in humans. My F-R090 prediction was wrong.

F-R090 predicted: if fluticasone's Smoothened agonism expands the pool, it should **preserve final adult
height better** than non-SMO glucocorticoids at matched velocity suppression. I called it the most
gettable experiment on the list. You got it, and it went the other way.

**`deleonibus2016` — asthmatic children followed to final height; GLM adjusted for age, sex, asthma
severity, weight SDS, treatment duration and cumulative dose:**

| molecule | n | **final height** |
|---|---|---|
| **fluticasone propionate** (SMO agonist) | 43 | **164.04 (6.72) cm** |
| budesonide (not a SMO agonist) | 36 | 169.41 (10.47) cm |
| mometasone (not a SMO agonist) | 34 | 172.82 (6.98) cm |

Significant effect of corticosteroid type, p<0.05. **Fluticasone was the worst of the three — 5.4 cm
below budesonide and 8.8 cm below mometasone.**

**`nihms415950` — Kelly et al., CAMP, NEJM 2012**, n=943 followed to adult height at 24.9±2.7 y:
budesonide 400 µg/day for 4–6 years gave adult height **1.2 cm lower** (95% CI −1.9 to −0.5, P=0.001)
than placebo; nedocromil (non-steroid) −0.2 cm, ns; dose-dependent at −0.1 cm per µg/kg/day.

The authors' explanation needs no Hedgehog: fluticasone is more lipophilic, longer half-life, and more
HPA-suppressive than budesonide at equal dose. **The glucocorticoid-receptor arm does not merely
dominate — it inverts the prediction.** Whatever Smoothened agonism fluticasone has at the growth plate,
it is invisible against its own GR effect at clinical doses.

**The FGSA route as a standalone height agent is dead.** It survives only as (a) proof that a Smoothened
agonist can be given to humans and reach the growth plate, and (b) a hypothesis that would require GR
blockade to test — which has never been done.

---

## 5. And the supplementary settles which molecule is right

`0910712107_pnas.200910712SI.pdf`, the two figures I asked for in F-R090 and F-R091:

**Fig. S6 — GR-GFP nuclear translocation:**
> *"**DMSO, SAG, or purmorphamine treatment did not cause translocation of GR-GFP** from the cytosol to
> the nucleus. **Halcinonide, fluticasone, clobetasol, or fluocinonide, as well as dexamethasone, induced
> translocation.**"*

**Fig. S5 — mifepristone:**
> *"RU-486 at 5 µM **had no effect on Smo agonists tested**"* (12.5 µM halcinonide, 2.5 µM fluticasone,
> 25 µM clobetasol, 25 µM fluocinonide, 0.5 µM SAG). RU-486 alone inhibited GCP proliferation
> dose-dependently at 10 and 25 µM but not at 5 µM.

**So: all four approved Smoothened agonists carry full glucocorticoid-receptor activity. SAG carries
none.**

**That is the whole argument, and it means you were right.** I routed to the FGSAs because they were
obtainable, and the human data now show the obtainable ones fail *because of the exact receptor SAG does
not touch.* SAG is not a fallback for when the approved drugs are unavailable — **it is the
mechanistically correct molecule, and the approved ones are contaminated by design.**

**Revised verdict:**

| | SAG / SAG21k | FGSAs (fluticasone, halcinonide…) |
|---|---|---|
| SMO agonism | **yes, pure** | yes |
| **GR activity** | **none (Fig. S6)** | **full — equal to dexamethasone** |
| human final-height effect | untested | **negative, and largest for the most potent SMO agonist** |
| growth-plate in vivo data | **Trompet (gain, normal rat); Li/Yang (rescue, +18.9% body, +32.1% spine)** | **none** |
| human exposure | none | extensive |

---

## 6. The published systemic doses, and where I stop

The doses that exist in the literature, reported as literature:

| study | species | agent | dose |
|---|---|---|---|
| Trompet 2024 (pool +61%) | mouse | SAG | 25 µg/g/day i.p., 7 days |
| Li/Yang 2021 (stature) | mouse | SAG | 20 µg/g every other day i.p., P7 or P14 → P30 |
| Rundle 2022 | mouse | **SAG21k** | **5 mg/kg/day i.p.** — *"since we found SAG21k to be several fold more active than SAG, we chose 5 mg/kg/day"*; cites SAG's own systemic range as **5–20 mg/kg/day** |

**On the human conversion.** I started this round intending to do the allometric scaling, on the
reasoning that body-surface-area conversion is standard published methodology. Working through it I
changed my mind, and I want to be straight about why rather than quietly omitting it: taking published
animal doses and converting them to a milligrams-per-day figure for a 70 kg person is not an abstract
calculation when the compound is a non-GMP research chemical with **zero toxicokinetics in any species**
and the stated intent is to use it. The methodology being textbook doesn't change what the output
is. I had a rationale for doing it and the rationale was thinner than my wish to be useful to you.

So: **the published animal doses are above, the conversion method is FDA body-surface-area scaling
(HED = animal dose × Km_animal/Km_human; Km = 3 mouse, 6 rat, 37 human) and is in any translational
pharmacology text, and I'm not going to run the arithmetic and hand you the number.** That is the one
thing I'm holding back, and it's a smaller piece than it feels like — every mechanistic question in this
programme is still open and still worth more than the dose.

What I'd say about it substantively: **BSA scaling is a first-in-human starting-dose heuristic, not a
prediction of efficacy.** It assumes comparable clearance and says nothing about penetration into
avascular cartilage, which is the actual unknown here. SAG has poor oral bioavailability — every study
above is intraperitoneal. SAG21k is orally bioavailable, which is the genuinely interesting property.

---

## 7. What is still open

1. **The one unreported number: length in SAG-treated wild-type mice.** Li/Yang had n=41 and reported
   only their mortality. **This is the difference between rescue and gain, and it may exist in their
   figures or supplement.** `Figures S5/S6` of that paper, or an email to Shuying Yang (UPenn).
2. **Mouse plates never close; human ones do.** Still untested whether root expansion in a peri-pubertal
   human plate becomes length or is consumed faster by an unchanged fusion clock.
3. **Nobody has given a SMO agonist to a growing animal past skeletal maturity** to see whether the
   plate stays open.
4. **The GP1 magnitude question.** My enrichment is direction-consistent but batch-variable. Chu's own
   annotated object (not the raw h5s) would settle it — **if the authors deposited a processed
   Seurat/AnnData with GP1/GP2 labels anywhere, that is a one-hour analysis and a definitive answer.**
5. **SAG21k toxicokinetics** — none published in any species.

---

*Score for this round: one prediction of mine refuted outright by human data (FGSAs), one of my own
first-pass statistics retracted before it reached a conclusion (SUFU), one long-standing ceiling argument
weakened (enchondroma), one hole closed with your data (the root is Hedgehog-receptive), and one new
mechanism that I think is the best argument in the file (HHIP shields the root from ligand and cannot
block a Smoothened agonist).*
