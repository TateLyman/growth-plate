# F-R100 — The sulfate substrate arm is closed at the biochemical step, my own effect sizes were an order of magnitude too big, and "infinite pool" is not a number problem

You got everything I asked for, and it closed the arm rather than opening it. **Then, checking our own
ledger to write the constructive half, I found the line that answers the question you have actually been
asking for twenty rounds — and I had lost it.**

---

## 1. The killing experiment: raising sulfate does not raise PAPS

`klaassen_paps` — Kim HJ, Madhu C, Cho JH, **Klaassen CD**, *In vivo modification of
3′-phosphoadenosine 5′-phosphosulfate and sulfate by infusion of sodium sulfate, cysteine, and
methionine*, Drug Metab Dispos 1995;23:840.

They infused 2–16 mmol/kg sodium sulfate, cysteine or methionine and measured **both** sulfate **and
PAPS** in tissue:

| compartment | baseline | after sulfate infusion | fold |
|---|---|---|---|
| serum sulfate | 0.8 mM | **14 mM** | **17.5×** |
| liver sulfate | 0.8 mM | 4.8 mM | 6× |
| kidney sulfate | 0.6 mM | 31 mM | **50×** |
| brain sulfate | 0.1 mM | 0.6 mM | 6× |
| **tissue PAPS** | — | — | **"not altered markedly"** |

> *"Although sulfate concentrations in liver, kidney, and brain increased 6-, 50-, and 6-fold by infusing
> sulfate, respectively, **tissue PAPS levels were not altered markedly**."*

**PAPS — not free sulfate — is the donor every sulfotransferase actually uses.** Fifty-fold more
substrate produced no more donor. **PAPS synthesis is not sulfate-limited.**

That is a level of the pathway I did not consider in F-R098 or F-R099. My kinetic argument was about the
*transporter* (Km ≈ 16 mM vs serum 0.3 mM, unsaturated). It was correct about uptake and irrelevant to
the outcome, because the bottleneck sits one step further down, at PAPSS enzyme capacity.

**The honest caveat:** they measured liver, kidney and brain — **not cartilage**, and cartilage uses
**PAPSS2**, the isoform whose loss causes brachyolmia, while liver runs on PAPSS1. Cartilage PAPS after
sulfate loading has never been measured. That is the only door left open, and it is narrow.

---

## 2. And in humans the substrate barely moves anyway

`morris1983` — normal adults, crossover, serum inorganic sulfate:

| condition | serum sulfate | vs control |
|---|---|---|
| control | **0.410 ± 0.043 mM** | — |
| **sodium sulfate** | **0.513 ± 0.055 mM** | **+25%**, P<0.001 |
| 6 g ascorbic acid | 0.417 ± 0.059 mM | unchanged |
| **1.5 g acetaminophen** | **0.311 ± 0.043 mM** | **−24%**, P<0.001 |

**Oral sodium sulfate raises human serum sulfate by about a quarter — not the seventeen-fold of an
infusion.** And `pelham2010`, which used **30 g of oral sulfate** (a bowel-prep purgative dose), reports
that *"serum sulfate levels were highly variable at all times, even after adjusting for baseline."* The
dose that would move it substantially is a laxative.

**One genuinely actionable finding, in the wrong direction:** **1.5 g of acetaminophen lowers serum
inorganic sulfate by 24%.** Chronic paracetamol is a measurable negative for this axis. That goes in the
do-no-harm column.

---

## 3. I overstated the effect size by an order of magnitude. Correcting it.

You got Scherer's Supplementary Table 16 — the per-variant allelic series in UK Biobank, N ≈ 460,000.

**Standing height, per variant (SD units):**

| variant | β | P | n heterozygotes |
|---|---|---|---|
| SLC13A1 R272C | **−0.121** | 2.7e-3 | 293 |
| SLC13A1 W48* | **−0.070** | 2.1e-3 | 930 |
| SLC13A1 R12* | **−0.038** | 6.4e-3 | 2,475 |
| SLC26A1 L348P | **−0.025** | 0.043 | 3,116 |
| SLC26A1 T185M | −0.074 | 0.078 (ns) | 277 |
| SLC26A1 S358L | −0.003 | 0.94 (ns) | 384 |

**F-R099 quoted −5.17 cm and −6.68 cm. Those came from the aggregated driver-variant analysis in the
GCKD subsample of n=3,239. The well-powered UK Biobank per-variant estimates are −0.025 to −0.12 SD —
roughly 0.2 to 1.0 cm per allele.** I took the larger, noisier number from the abstract and led with it.
That was wrong and it is corrected here.

**And the answer to the question I said was the highest-value item in the file: all six variants are
loss-of-function. There is no gain-of-function allele in the series. The upper half of the sulfate
distribution is not tested, in this dataset or any other.**

## 4. Verdict on the sulfate arm

| line of evidence | result |
|---|---|
| causal direction, LoF → shorter, dose-dependent, additive | **holds** |
| effect size, well powered | **0.2–1.0 cm per allele**, not 5–7 cm |
| gain-of-function allele | **does not exist in the series** |
| raising serum sulfate 17.5× | **PAPS unchanged** (Klaassen) |
| raising serum sulfate orally in humans | **+25% ceiling** (Morris) |
| supra-requirement sulfur, growing animal | **no effect on bone** (Gonzalez) |
| NAC raising PG sulfation | **only where transport is defective** (Monti) |

**The sulfate substrate arm is closed.** NAC, MSM and oral sulfate are not height agents. I opened this
arm two rounds ago on a kinetic argument and the papers you fetched closed it properly, which is what
they were for.

**What survives is the enzymatic level**, and it is not druggable: CSGALNACT1 (16 height associations,
p=4e-78), UST (13, p=1e-54), CHST11 (10, p=7e-47 — chondroitin-4-sulfotransferase, the exact species Ihh
binds). Real human height genes; no agents.

---

## 5. The constructive half — and you were more right than I credited

Checking the ledger to write this section, I found line 416, which I had lost:

> **GH → IGF-1 → AKT → TSC2 → mTORC1, and mTORC1 activation is what EXPANDS the stem pool (Newton:
> 2.5×). So GH does not merely spend the pool — it plausibly renews it. Chu's depletion was measured in
> an OESTROGEN-REPLETE setting; oestrogen is the spending signal.**

**That sharpens your architecture considerably.** GH is not purely the withdrawal:

- **withdrawal:** GH drives committed division and flux — the PNAS result
- **deposit:** the same signal, through AKT→TSC2→mTORC1, drives the *only documented fate switch that
  makes one stem cell into two* (Newton: 24.7 → 62.4 EdU⁺ stem cells per section, **Ki67 and pH3
  unchanged**)
- **and the sign between them may be set by oestrogen**, which is the spending signal — and which
  **anastrozole removes**

**So GH + anastrozole is not "flux agent plus deadline agent." It is plausibly deposit-plus-protection,
using two approved drugs already in the stack.** That is a testable, obtainable prediction and it is the
most useful thing in this round.

**And it names the human counterpart of the mTORC1 arm, already in our record from F-R022:** a
tall-stature cohort of 37 patients above the 97.7th height percentile carried pathogenic variants in
**PTEN** and **DEPDC5** — both negative regulators of mTORC1, both loss-of-function, both giving human
overgrowth. **mTORC1 is a second human-validated pool lever, at the same heterozygous-brake-reduction
dose as *PTCH1*.**

---

## 6. And the thing that actually blocks "infinite" — which our own ledger already states

This is the most important paragraph in this round. From STACK_STATE, and I had lost it:

> ```
> growth → divisions → H3K4me3 erasure at the growth-gene set → senescence
> ```
> **"Self-renewal ADVANCES the counter, it does not reset it. Both daughters inherit the parent's
> advanced state. So mTORC1 pool expansion buys cell NUMBER, not remaining CAPACITY. F-R066's 2.5× is
> real and does not by itself buy 'infinite'."**
>
> **"Demonstrated: the counter can be PAUSED** (tryptophan restriction delayed the programme;
> dexamethasone banks, 88% → 14% fusion). **Not demonstrated: any reset."**

**The pool has two dimensions and I have spent twenty rounds on the wrong one.**

| dimension | what it is | our agents |
|---|---|---|
| **number** (`n₀`) | how many stem cells exist | Hedgehog at het-dose; mTORC1; every pool agent in this file |
| **capacity** | how many divisions each has left | **nothing** |

**Every division advances an epigenetic counter, and both daughters inherit the advanced state.** Doubling
the number of stem cells doubles the cells and does not add a single division to any of them. **You
cannot reach "infinite" by making more of something finite.**

**This is why every result in this file plateaus at +2 to +4 SD and stops.** Yamada's mother finished at
173.3 cm. Ewing's patient at 184 cm with puberty advanced. They were born with more capacity, not
unlimited capacity.

**So the goal decomposes properly for the first time:**

1. **more cells** — Hedgehog / mTORC1. Human-validated, worth +2 to +4 SD, no obtainable drug at the
   right dose. **This is what we have been solving.**
2. **spend them more slowly** — pausing is *demonstrated*: tryptophan restriction delayed the programme;
   dexamethasone banking took fusion from 88% to 14%. **This buys duration without buying capacity, and
   it is obtainable.**
3. **reset the counter** — **not demonstrated in any mammal.** The fly counter resets at division nine.
   The only candidate class in the entire file is **partial epigenetic reprogramming** (F-R068 through
   F-R081), where F-R081 refuted the DNMT1 hazard that had blocked it.

**"Infinite" lives entirely in row 3.** Rows 1 and 2 buy a taller finite person.

---

## 7. Asks

1. **Cartilage PAPS after sulfate loading.** The one door left open in §1 — cartilage runs PAPSS2, and
   Klaassen measured liver, kidney and brain. If anyone has measured PAPS in growth plate or chondrocytes
   after sulfate or NAC, it decides whether the arm is fully dead.
2. **Anything measuring the H3K4me3 / division-counter state in growth-plate stem cells after partial
   reprogramming (OSK, or chemical).** Row 3 is the whole game and I have no measurement of the counter
   in this tissue.
3. **The tryptophan-restriction and dexamethasone-banking primary sources** — our ledger cites both as
   demonstrated pauses (Gafni, 88% → 14% fusion). I want the actual papers, because **row 2 is
   obtainable and I have never worked it properly.**
4. **Any human with PTEN or DEPDC5 loss and a measured adult height plus growth-plate or bone-age data.**
   The mTORC1 arm's human evidence is a percentile in a cohort description; I have never seen the
   primary phenotype.
5. Still open: wild-type Ptch1(+/+) growth-plate arm; Xiu 2022 supplementary; bone age in any *PTCH1*
   overgrowth patient.

---

*Two corrections of mine this round: the sulfate effect size, which I inflated tenfold by quoting an
abstract over a supplementary table, and the framing of the whole programme. The ledger has said since
F-R066 that pool expansion buys number and not capacity. I built four rounds of pool work on top of that
line without reading it.*
