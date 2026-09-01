# F-R099 — Stock is not flow: three experiments made the plate more cellular and none made the bone longer. And plasma sulfate is a causal human height variable with a measurable readout.

Ten sources. Two of them overturn things I have been assuming, and one is the strongest human evidence
for any lever in this entire file.

---

## 1. First, the GEO structure — and it changes how Orikasa should be read

`GSE244884` is a SuperSeries containing exactly two samples, and `GSE244880` / `GSE244881` are those same
two samples as SubSeries. **There is no third arm and no wild-type deposit.** But the labelling matters:

| SubSeries | sample | genotype | **the authors' label** |
|---|---|---|---|
| GSE244880 | GSM7831318 | `Ptch1(fl/fl)` | — |
| **GSE244881** | GSM7831319 | **`Ptch1(fl/+)`** | **"Control"** |

**Orikasa's entire published conclusion — "Hedgehog activation promotes osteogenic fates of growth plate
resting zone chondrocytes" — is derived from fl/fl compared against fl/+.** Their control *is* the human
tall genotype.

So F-R098's finding is really this: **the paper that F-R088 used to disqualify Hedgehog treats the human
genotype as normal, and only the homozygote does anything.** That is a stronger statement than I made
last round, and it comes free from the metadata.

---

## 2. The hard result: more chondrocytes, identical bone length

`hilton2005` — Hilton MJ et al., *EXT1 regulates chondrocyte proliferation and differentiation during
endochondral bone development.*

EXT1 heterozygous mice — reduced heparan sulfate, which per Koziel **enhances Ihh diffusion**:

> *"cytological examination of the growth plates of adult EXT1⁺/⁻ long bones show **an increase in
> chondrocyte numbers within the columnar growth plate**, although **the overall length of long bones are
> comparable to those of wild-type mice**."*

And the abstract's mechanism is exactly what we wanted: *"defects in EXT1 and the resulting reduction in
HS lead to **enhanced Indian Hedgehog diffusion causing an increase in chondrocyte proliferation and
delayed hypertrophic differentiation**."*

**Enhanced Ihh diffusion. More chondrocytes. Delayed hypertrophy. Same bone length.**

### This is the third time, and it is now a pattern I have to name

| experiment | what went up | **bone length** |
|---|---|---|
| Xiu, Sufu-cKO | growth plate *"obviously expanded"* at P30 | **shorter** (premature fusion by P120) |
| Koyama, CD2665 alone | *"slight increase in overall growth plate height"*, expanded ColII and ColX zones | **"essentially unaffected"** |
| **Hilton, EXT1⁺/⁻** | **chondrocyte number in the columnar zone** | **"comparable to wild-type"** |

**Three independent laboratories, three different molecular routes, three plates made larger or more
cellular, and not one longer bone.**

### The resolution, and it sharpens the whole programme

I have been sloppy, and our own identity says why. `dL/dt = flux × v(d)`: **length accrues from the
*rate at which cells complete the journey and are replaced by bone*, multiplied by the height each one
contributes.** Neither term is "how many cells are standing in the plate."

**Plate cellularity is a stock. Length accrual is a flow.** Adding cells to the columnar zone lengthens
the queue; it does not raise throughput. A plate with more chondrocytes and a normal transit rate
produces exactly as much bone per day as before — which is precisely what Hilton measured.

And this retro-validates the one experiment that worked. **Trompet measured the right things:** his +61%
was in **PTHrP⁺ cells** — the stem compartment, upstream of the queue — and his bead raised the
**calcein/xylenol growth rate**, which is flux. Everything that failed measured stock.

**Operational consequence, and I am putting it in the ledger:** plate height, plate thickness and
chondrocyte number are **not** valid endpoints for this programme. The endpoints are **flux** (calcein
double-label growth rate, or column production rate) and **stem-compartment number** — and they are not
the same as each other either.

---

## 3. And the heparan-sulfate arm's dose-response runs opposite to PTCH1's

`showPdf 3` — Koziel L et al., *Dev Cell* 2004;6:801–813, the paper I asked for by name.

Confirmed mechanism: reduced HS → **Ihh protein distribution expanded**, *Ptch* and *Pthlh* upregulated,
the strong-*Ptch* domain **expanded toward the joint**. Proliferation:

| zone | wild-type | **Ext1^Gt/+** | Ext1^Gt/Gt |
|---|---|---|---|
| zone II (columnar, high-proliferating) | 20–24% | 20–24% | 20–24%, **no significant difference** |
| **zone I (periarticular, low-proliferating)** | **12%** | **12%** | **increased** |

Two things fall out, and both are cautions:

1. **The increase is confined to zone I — the periarticular, low-proliferating compartment**, which is
   the embryonic antecedent of the resting zone. Increased Ihh range activates the *reserve* compartment.
   Under our own framework that is ambiguous: it could mean founding more columns, or it could mean
   spending the reserve.
2. **Ext1^Gt/+ was identical to wild-type.** Only the homozygote — which retains **3% of full-length
   Ext1** — differed. **And that animal has *"a reduced skeleton size with fused vertebrae, shortened
   [elements]"* and syndactyly.**

**So the HS arm inverts the PTCH1 pattern.** For *PTCH1*, heterozygous is the effective and beneficial
dose and homozygous is catastrophic. For *EXT1*, heterozygous does nothing measurable and the severe
hypomorph is smaller. **Reducing heparan sulfate is not a usable lever**, and the human phenotype agrees:
hereditary multiple exostoses (EXT1 LoF) includes **short stature**.

---

## 4. Now the finding that changes the sulfate arm — human, causal, quantitative

`41588_2024_Article_1965` — **Scherer N et al., *Nature Genetics* 2025;57:193–205**, coupling
metabolomics to exome sequencing in 4,737 GCKD participants with follow-up in UK Biobank.

> *"Allelic series of functional variants in transporters responsible for transcellular sulfate
> reabsorption (**SLC13A1, SLC26A1**) exhibited **graded effects on plasma sulfate and human height**."*

| finding | value |
|---|---|
| correlation of genetic effect sizes: plasma sulfate vs **standing height** | **Pearson r = 0.70** |
| same, vs sitting height | r = 0.57 |
| **SLC13A1 driver variants, effect on height** | **−0.54 SD = −5.17 cm**, P = 1.6e-3 (n = 3,239) |
| **SLC26A1 driver variants** | **−0.73 SD = −6.68 cm**, P = 1.7e-6 |
| SLC13A1 p.Arg12* heterozygotes | **0.95 SD lower plasma sulfate** (n=22, P=9.9e-10); 0.08 SD lower sitting height (n=2,480, P=2.2e-7) |
| NaS1 p.Arg272Cys | *"Age- and sex-specific z scores for human height showed a **clear dose–response effect**"* |
| double heterozygotes (NaS1 **and** SAT1) | stronger than either alone — *"support **additive effects across the pathway** for human growth"* |

And the authors' own conclusion:

> *"These observations support a **causal relationship** between transcellular sulfate reabsorption and
> human height and **designate plasma sulfate as an intermediate readout**."*

**This is the strongest human evidence for any lever in this file, and it is the only one with a
directly measurable, directly manipulable intermediate biomarker.** Not a genotype we cannot change —
a plasma metabolite.

### Why this is structurally different from every other arm, and may escape the rescue law

F-R094's rescue law holds because every other lever sits at a **defended setpoint**: push a receptor
system above normal and it counter-regulates (Sufu-cKO decompensates; SAG does nothing in a wild-type
mouse; PTCH1 and HHIP are themselves Hedgehog target genes, so signalling harder builds more brake).

**Plasma sulfate is not defended by anything that cares about height.** Its level is a by-product of
renal tubular reabsorption capacity — a transporter Vmax — not of a feedback loop sensing skeletal
growth. There is no sensor in the growth plate instructing the kidney to hold sulfate at 0.33 mmol/L.

Combined with the kinetics from F-R098 — chondrocyte sulfate transporter **Km ≈ 16 mM against serum
≈ 0.3 mM**, roughly **2% of Km** — and with Scherer's demonstration that a **0.95 SD reduction in plasma
sulfate costs measurable height**, the picture is of a system operating **on a steep, unsaturated,
undefended part of its dose–response curve.**

### The counterweights, and there are real ones

**`cole1980` — and it initially looked fatal.** Serum sulfate falls from 0.47 mmol/L on day 1 to
0.33 mmol/L at 36 months, and *"thereafter the mean value is about 0.33 mmol/l"* — **flat from age three
through adolescence into adulthood.** If sulfate supply drove growth, it should track the pubertal
growth spurt. It does not.

**Reconciliation:** Cole measured variation *with age within the population*; Scherer measured variation
*between individuals genetically*. Both are correct and they answer different questions. Sulfate is not
a developmental timing signal — it is a **setpoint/rate variable**, constant across development but
differing between people, and those differences set height. **This is exactly the shape of the *PTCH1*
result: a parallel shift of the growth curve, not a change in its timing.**

**`monti2015` — the proof that the substrate arm can move the endpoint.** NAC 30 g/L in drinking water to
pregnant dtd mice (SLC26A2-deficient) produced *"a marked increase in PG sulfation"* in newborns and
*"a partial rescue of abnormal bone morphology."* **N-acetylcysteine demonstrably raises proteoglycan
sulfation in vivo.** The authors' own caveat is the rescue law stated plainly: NAC is useful *"when
extracellular sulfate supply is reduced."*

**`gonzalez1993` — the closest thing to a gain-direction test, and it is negative.** Broilers, days 1–21,
factorial sulfate supplementation: *"SAA supplementation up to 65% in excess of the requirement… **did
not affect bone mineralization**"*, and excess inorganic sulfate from the potassium salt *"may adversely
affect Ca deposition in bone."* **The endpoint is mineralisation, not length**, and the species is avian —
but it is a supra-requirement sulfur experiment in a fast-growing animal and it showed no benefit.

**`antioxidants-14-00216` — MSM, and it does not test this arm.** 73-week-old mice, 8 weeks, an
*age-induced bone loss* model with resorption endpoints. Nothing about growth plates or length.

**`TJP-595-7093` — the NAC safety counterweight.** Pre-clinical NAC in mdx mice *"reveals side effects"*.
Recorded, not yet read in detail.

---

## 5. Where this leaves the programme

| term | best lever | evidence class | status |
|---|---|---|---|
| **pool `n₀`** | Hedgehog at the *PTCH1*-heterozygous dose | human dose–response, +0.8 to +3.8 SD (F-R096/97); mouse dose–response in PTHrP⁺ cells (F-R098) | **no drug reproduces the chronic 50% regime** |
| **flux — newly separated from pool** | — | Trompet's bead is the only agent that raised calcein/xylenol growth rate | **this, not plate thickness, is the endpoint** |
| **matrix / Ihh range — sulfate** | plasma sulfate | **human causal, r=0.70, −5.17 to −6.68 cm for het LoF, dose–response, additive** | **gain direction untested; substrate demonstrably raisable (NAC)** |
| matrix / Ihh range — heparan sulfate | EXT1 reduction | het does nothing; severe hypomorph is smaller | **dead** |
| duration | anastrozole | human LoF (aromatase/ESR1 non-fusion); Klinefelter additivity | intact; RARγ dead as a second lever (F-R094) |
| rate `v` | erdafitinib, mecasermin | — | unchanged |

**Two things changed this round.** The first is a correction I should have made rounds ago: **we have
been chasing plate cellularity and it is the wrong variable.** The second is that the sulfate arm, which
I introduced last round on a kinetic argument, now has human causal genetics behind it with an effect
size of **5 to 6.7 cm per heterozygous loss-of-function allele** and **a blood test as its readout.**

## 6. Asks

1. **Any study that raised plasma sulfate above normal in a growing animal and measured BONE LENGTH.**
   Gonzalez measured mineralisation in birds. Monti measured rescue in a deficient mouse. **The
   gain-direction experiment with a length endpoint does not appear to exist, and it is now the single
   most important missing result in the file.**
2. **Scherer et al. Supplementary Fig. 3 and Supplementary Tables 15/16/39** — I have the main text. I
   want the full allelic series with per-variant plasma sulfate and height, to see whether the
   dose–response extends into the **upper** half of the sulfate distribution. **If people with
   genetically higher plasma sulfate are taller, that is the gain direction, already measured, in UK
   Biobank.** This is the highest-value item on the list and it may be one supplementary table.
3. **Plasma sulfate reference range versus height in any cohort** — same question from the phenotype
   side.
4. **Whether oral NAC, MSM or sodium sulfate raises plasma sulfate in humans, and by how much.** The
   pharmacokinetics decide whether the lever is even reachable.
5. Still open: wild-type Ptch1(+/+) growth-plate arm; Xiu 2022 supplementary; bone age in any *PTCH1*
   overgrowth patient.

---

*The correction that matters most this round is mine, not the literature's. Three papers told me a
bigger growth plate is not a longer bone, and I had been treating "expand the plate" as the goal since
F-R088. Our own identity had `flux` in it the whole time.*
