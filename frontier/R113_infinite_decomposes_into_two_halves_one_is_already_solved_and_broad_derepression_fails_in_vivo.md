# F-R113 — "Infinite" decomposes into two halves. One is already solved in humans. And the chromatin class raises the network, then shortens the bone.

You said stop asking and go find. Four of the things in this round were answerable from data I already
had, and one of them I had been sitting on since F-R103 without seeing what it was.

---

## 1. The decomposition, which I should have written down twenty rounds ago

**"Infinite" is not one property. It is two, and they are separable:**

| | |
|---|---|
| **never-closing** | the plate does not fuse |
| **non-senescing** | the plate does not run out of program |

**And they come apart in humans, cleanly, in both directions.**

### ⇒ The never-closing half is already solved, and it is an approved drug class

**Aromatase deficiency (CYP19A1) and oestrogen-receptor-α mutation in men:** absent pubertal growth
spurt, delayed bone maturation, **unfused epiphyses into the mid-twenties and beyond, continued linear
growth into adulthood, tall stature >3 SD.** The ERα case (Smith 1994) was **204 cm and still growing at
28 with open epiphyses.** Oestradiol replacement fuses the plates within six months.

**That is a human, genetic, permanent never-closing growth plate. The pharmacological equivalent —
aromatase inhibition — has been in this file as a "row 2 deadline agent" since F-R087 and I never
labelled it as what it is.**

### ⇒ And the ceiling of that half is about +3 SD, because the counter runs anyway

**They stop.** They land around 200–204 cm, not indefinitely. Something ends growth that is not fusion.

**I can prove what, from data I have had since F-R103 and mis-framed as an incidental detail.**
`GSE16981`'s proliferative-zone time course is **castrated rats — gonadal steroid removed from 3 weeks.**
**That is the animal model of the aromatase-deficient man**, and I described the castration as
"the *intrinsic* clock" in F-R103 without ever running the right test on it.

**The imprinted gene network in castrated rats, against an expression-matched null:**

| | 6 wk vs 3 wk | 9 wk vs 3 wk | 12 wk vs 3 wk |
|---|---|---|---|
| **imprinted network** | **−0.67, z = −7.9** | **−0.83, z = −7.1** | **−0.93, z = −6.7** |
| cell cycle | +0.22 | +0.28 | +0.18 |
| chondrogenic | −0.14 | −0.18 | −0.11 |

IGF2 −6.35, MEST −2.82, SLC38A4 −1.65, H19 −1.63, NDN −1.12.

> **With oestrogen removed, the counter runs at full strength. Removing the deadline does not slow the
> program; it only stops the plate being closed before the program finishes.**

**So: `infinite = never-closing × non-senescing`. The first factor is solved and buys roughly +3 SD.
The second is the entire remaining problem, and it is the imprinted-network collapse.**

---

## 2. Ask #4 from last round, answered from disk, and the answer is no

I asked you for "what a fracture does to an open growth plate." **`GSE3298` was already in my corpus and
its own summary is the sentence I had been looking for:**

> *"**Mid-shaft fracture stimulates bone lengthening by increasing linear growth at the growthplate.**"*

Rat proximal femoral **growth plate** after a **distant mid-shaft fracture**, seven timepoints,
paired time-matched controls. So: does the remote injury signal reach the plate and reactivate the
network?

| | 1 d | 3 d | 1 wk | 2 wk | 3 wk | 4 wk | 6 wk |
|---|---|---|---|---|---|---|---|
| **imprinted network** | +0.19 | −0.09 | −0.07 | −0.08 | −0.09 | +0.15 | **−0.48** |
| z vs matched null | +0.16 | −0.64 | +0.47 | −0.88 | −1.35 | +1.40 | **−3.47** |

**No.** The dataset is not underpowered — 427 and 573 genes move by more than 1 log2 at day 1 and week 1
— but what moves is an **interferon/macrophage signature** (ISG15, MX2, AIF1, MPEG1, MRC1, CCL2, GPNMB,
CHI3L1). MEST +0.62 is the only imprinted gene that rises.

> **The limb overgrowth after childhood fracture is real, and it does not work by reactivating the
> imprinted network in the growth plate. F-R112's callus result stays local to the callus.**

---

## 3. Hedgehog is orthogonal to the counter — which is good news, not bad

| contrast | imprinted network |
|---|---|
| **Gli1⁺ progenitors vs Gli1⁻ cells** (GSE249831) | **+0.08, z = +0.07 — null** |
| rat resting zone vs proliferative zone | −0.10, z = −0.52 — null |
| SAG vs DMSO, sorted epSSC *(contaminated, F-R110)* | −0.39, z = −2.38 |

**Hedgehog does not touch the imprinted network.** That is exactly what F-R096 predicted from the human
genetics without being able to test it: **every PTCH1⁺/⁻ patient is +0.8 to +3.8 SD tall and every one of
them stops.** Hedgehog buys pool; it does not buy program.

**The useful consequence: pool and counter are independent axes, so their effects should be additive
rather than redundant.** The stack does not have to choose between them.

---

## 4. I corrected F-R112 against myself: the chromatin class is NOT null

F-R112 tested **G9a inhibitors only** and reported the class null. That was too narrow. I built a proper
screen — **204 drug-versus-control contrasts across 654 cached datasets**, each scored against an
expression-matched null.

| compound | imprinted network | z |
|---|---|---|
| **vorinostat / SAHA 10 µM** | **+0.85** | **+2.81** |
| **romidepsin 30 nM** | **+0.69** | **+2.57** |
| romidepsin 10 nM / 2 nM | +0.39 / +0.14 | +2.15 / +2.22 |
| **JQ1 500 nM** (BET) | **+0.44** | **+3.53** |
| JQ1 50 nM / 100 nM | +0.14 / +0.08 | +2.37 / +2.17 |
| MS-275 / entinostat | +0.36 | +2.62 |
| **trichostatin A** | +0.23 / +0.23 | +2.53 / +1.98 |
| I-BET151 | +0.09 | +1.98 |
| GSK126 (EZH2i) | +0.06 / +0.14 | +2.54 / +2.15 |
| **dexamethasone, primary chondrocytes** | +0.17 | +2.19 |
| G9a inhibitors (UNC, BIX) | ~0 | ≤ +1.8 |

**Romidepsin is dose-responsive across three doses; JQ1 across five datasets and three doses.
So HDAC and BET inhibitors do raise total imprinted-network dose — my F-R112 "null" was specific to
G9a and I over-generalised it.**

**The magnitudes, in context:** +0.06 to +0.85 log2, against a deficit of **−3.09** in the ageing
resting zone. **A quarter to a thirtieth of the hole.**

---

## 5. Then the top hit killed the whole class, in vivo, with a length endpoint

The strongest result in the screen was not a drug — it was **`GSE84198`, Ezh1⁻/⁻; Col2-Cre Ezh2^fl/fl vs
littermates, laser-microdissected growth plate, P3, n=6 per group.** The right tissue, in vivo, well
powered.

| | imprinted network | cell cycle | chondrogenic |
|---|---|---|---|
| **proliferative zone** | **+0.28, z = +7.53** | −0.07 | −0.01 |
| hypertrophic zone | +0.18, z = +2.75 | −0.01 | −0.39 |

PEG10 +0.81, PPP1R9A +0.69, DLK1 +0.61, GPC3 +0.52, RIAN +0.50, NNAT +0.47, GNAS +0.45, MEG3 +0.40,
AIRN +0.38, MEST +0.37. **Broad, coherent, not proliferation-driven.** For about ten minutes this was the
best result in the file — the network raised at z=+7.5 in growth plate in vivo, by a target with an
**FDA-approved inhibitor** (tazemetostat).

**Then I read the paper the dataset comes from.**

> `Lui JC et al., **EZH1 and EZH2 promote skeletal growth by repressing inhibitors of chondrocyte
> proliferation and hypertrophy.** Nat Commun 2016;7:13685.`

**The title is the result. Those mice have *reduced* skeletal growth.** EZH1/2 normally repress
inhibitors of chondrocyte proliferation and hypertrophy; remove them and those inhibitors come up, and
the bone gets **shorter** — while the imprinted network goes **up**.

> ### **This is the one experiment in existence where the imprinted network was raised in a growth plate
> and bone length was measured. The network went up and the bone got shorter.**

**And it generalises to the whole class, including your list.** Broad chromatin de-repressors — HDAC,
BET, EZH2, and by the same logic G9a — do not selectively lift the imprinted domains. **They lift
everything, and "everything" includes the brakes on chondrocyte proliferation and hypertrophy.**

**EZH2 inhibition is out. And the +0.2 to +0.85 the HDAC and BET inhibitors buy has to be weighed against
an unmeasured de-repression of growth inhibitors, in a class where the single in-vivo skeletal test came
out negative.** I am not adding any of them.

---

## 6. Where this leaves the whole programme, stated once and plainly

| factor of "infinite" | status | agent | ceiling |
|---|---|---|---|
| **never-closing** | **SOLVED** — human genetic proof (unfused at 28, 204 cm, >3 SD) | **aromatase inhibition** — approved, in the stack since F-R087, mislabelled until now | **~+3 SD alone** |
| **more cells (pool)** | human-validated (PTCH1 dose-response), **orthogonal to the counter, therefore additive** | SMO agonism — still no clean obtainable agent; local SOC delivery is the only demonstrated route | +2 to +4 SD claimed by genotype |
| **faster / v** | measured; the lever is hypertrophic size, not proliferation | erdafitinib, vosoritide, GH+AI (+7.5 cm) | small |
| **non-senescing** | **the entire remaining problem.** Runs at full strength without oestrogen (z = −6.7 to −7.9), untouched by Hedgehog, not reachable by remote injury, and the one in-vivo test of raising it shortened the bone | **none** | — |

**The honest summary of the stack: we can stop the plate closing, we can put more cells in it, and we can
make each cell contribute more. We cannot stop it running out of program, and the two strategies that
looked like they might — broad chromatin de-repression and injury signalling — have now both been tested
and both failed on a length endpoint.**

---

## 7. What is actually still open, and it is now three specific things

1. **A selective de-repressor of imprinted domains** — something that lifts the imprinted network
   *without* lifting the chondrocyte-proliferation brakes. §5 says the broad ones cannot. Whether
   anything selective exists, I do not know; nothing in 5,591 series does it.
2. **Whether raising the imprinted network in the *resting zone specifically* lengthens bone.**
   GSE84198 is PZ and HZ. F-R111 showed the RZ collapse is 4× larger and the RZ ages by a different
   program (r = +0.16 with PZ). The Ezh2 result may simply be the wrong compartment.
3. **Whether the never-closing and pool arms are genuinely additive in vivo.** They are orthogonal on
   the transcriptome (§3). Nobody has combined a SMO agonist with oestrogen blockade in any animal, and
   on the arithmetic that combination is the whole obtainable programme: **+3 SD of deadline × the pool
   effect, with no overlap between them.**

---

*Four things in this round were on my disk: the castrated-rat time course that proves the counter is
oestrogen-independent, the growth-plate-after-fracture dataset that answers last round's ask with a no,
the Gli1 dataset that shows Hedgehog is orthogonal, and the Ezh2 growth plate that raises the network
and shortens the bone. You were right that I should have found them rather than asked. The one thing I
would still genuinely like is any measurement in a resting zone rather than a proliferative one — but I
am not going to hold up the work for it again.*
