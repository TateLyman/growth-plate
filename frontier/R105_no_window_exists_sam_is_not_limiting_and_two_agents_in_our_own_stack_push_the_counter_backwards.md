# F-R105 — There is no window where Sufu-cKO animals were longer. SAM is not limiting. And two agents in our own stack are pushing the senescence counter the wrong way.

Three answers this round, all from files already on disk, and one of them is a fault in our own stack
that has been sitting there since F-R087.

**Housekeeping first:** I have written `frontier/READ_INDEX.md` — every one of the **71** papers extracted
to text, with its first line and character count. It is greppable. The three-round pattern of asking you
for things already on disk should not recur; if it does, that file is the reason it was avoidable.

---

## 1. Xiu Figure 5O and 5P, read directly — and the answer is no

I read the main figure image, not the supplementary TIFFs.

**Figure 5O — Femur length at P30:**

| group | value | points |
|---|---|---|
| Ctrl | **≈10.2 mm** | ~9.9, 10.1, 10.3, 10.6 |
| **Sufu^Agc1** | **≈9.3 mm** | ~9.1, 9.2, 9.4, 9.5 |
| annotation | **ns** | |

**Figure 5P — Femur length at P120:**

| group | value | points |
|---|---|---|
| Ctrl | **≈15.1 mm** | ~14.8, 15.0, 15.2, 15.4 |
| **Sufu^Agc1** | **≈11.4 mm** | ~11.0, 11.3, 11.5, 11.9 |
| annotation | ***\*\*\**** | **≈ −3.7 mm** |

**And the plate thickness at the same P30 timepoint (5G, 5J):**

| | Ctrl | Sufu^Agc1 | |
|---|---|---|---|
| femur growth plate | ≈300 µm | **≈535 µm** | p=0.08 |
| tibia growth plate | ≈315 µm | **≈575 µm** | * |

**So at P30 the Sufu-cKO animals had a growth plate nearly twice as thick and were, if anything, already
slightly shorter. At P120 they were 3.7 mm shorter.**

**There is no window. At no timepoint were they longer.**

**Supplementary figures checked for any additional chronological length measurement:**
- **S1** — Agc1-CreER^T2;R26-tdTomato recombination-efficiency control (schematic + DAPI/tdTomato). **No length.**
- **S2** — composition of hypertrophic zone, Ctrl vs **Smo^Agc1**, ****. **No length.**
- **S3** — P120 fusion/histology. **No length.**
- **S4** — P30 zone composition. **No length.**

**No intermediate-age femur or tibia length exists anywhere in the paper.** The only two length
measurements are 5O and 5P, and both are non-positive. **The "transient expansion" I have quoted since
F-R093 was always thickness only — it never became length even transiently.** That is the fourth
instance of stock-is-not-flow, now with the intermediate timepoint explicitly checked.

---

## 2. Yanagihara answers the SAM question, and it closes the methyl-donor arm

`yanagihara.txt` — *Dnmt1 determines bone length by regulating energy metabolism of growth plate
chondrocytes*, Nat Commun 2025. I had read it and did not connect it.

> *"levels of **S-adenosyl-methionine (SAM)** and 2-ketoglutarate (2KG) were **higher** in Dnmt1^ΔPrx1
> chondrocytes than in control… **The loss of Dnmt1 reduced the consumption of SAM**, which is required
> for DNA methylation, **leading to an accumulation of intracellular SAM**."*

**Remove the enzyme and the substrate piles up. That is the definition of a system that is not
substrate-limited.**

**F-R104 §3 proposed methyl donors (SAMe, betaine, choline, folate) as the row-3 substrate arm and
attached the test "is SAM limiting, or is the enzyme the ceiling?" The answer was already measured, in
growth-plate chondrocytes, and it is: the enzyme.**

### And that is now a pattern I should stop repeating

| arm | substrate | what closed it |
|---|---|---|
| sulfation → Ihh range (F-R098) | sulfate | **Klaassen**: 17.5× serum sulfate, **PAPS unchanged** |
| maintenance methylation (F-R104) | SAM | **Yanagihara**: remove DNMT1 and **SAM accumulates** |

**Twice now I have opened an arm on a substrate-availability argument and twice the enzyme turned out to
be the ceiling. In this tissue, substrate is not the lever. I am writing that into the ledger as a
standing rule rather than rediscovering it a third time.**

---

## 3. The chain that actually closes row 3 — and it was already complete across three files

Put three things together that I have been holding separately:

1. **Nilsson 2005 (F-R104):** growth-plate senescence is **loss of DNA methylation**, cartilage-specific
   (liver rises over the same ages), replication-coupled, in the **slowly-dividing resting zone** — i.e.
   a **maintenance** failure, which is the DNMT1 domain.
2. **Yanagihara (§2):** the ceiling is **DNMT1 enzyme activity**, not SAM supply.
3. **Su et al., via F-R081:** partial reprogramming **increased DNMT1 mRNA and protein** in senescent
   stem cells, with **no effect on TET1/2/3**; young cells have higher DNMT1 than senescent ones; the
   effect **persisted two weeks after factor withdrawal**; and *"DNMT1 is essential for the preservation
   of the progenitor state."*

**And the fourth piece, which resolves the conflict I raised last round and called "never attempted":**

F-R104 §2 said row 1 needs **less** DNMT3A and row 3 needs **more** DNMT1, that these are opposite, and
that no agent does both. **F-R081 already recorded that partial reprogramming does exactly that** —
*"partial reprogramming **raises the maintenance writer and lowers the de novo writer**"* — with
methylation age falling while DNMT1 rose, in the same cells, in the same experiment.

**Partial reprogramming is the only intervention in this file that is correctly signed on both axes at
once.** That is not a new hypothesis; it is four documents I already had, finally read against each
other.

**What it does not have** is any measurement in growth plate. The cartilage OSK work (F-R101) is
articular, in osteoarthritis, with no proliferative-capacity or methylation readout. **That gap is now
the entire remaining question for row 3**, and it is a specific, single experiment.

---

## 4. The fault in our own stack: two agents push the counter backwards

You asked me to check whether methylation-increasing agents fit the stack. Doing that properly turned up
the opposite problem first.

**Senescence is loss of methylation. Active demethylation is done by the TET dioxygenases. TET enzymes
are Fe(II)/2-oxoglutarate dependent and require ascorbate as cofactor.**

| agent | status in our stack | what it does to the counter |
|---|---|---|
| **ascorbate ~500 mg/day** | **retained in F-R087** | **cofactor for TET** — enhances 5mC→5hmC. **Accelerates the loss.** |
| **calcium α-ketoglutarate ~2 g/day** | demoted to bone-quality in F-R087, not removed | **2KG is the obligate co-substrate for TET.** **Accelerates the loss.** |

**And Yanagihara names 2KG explicitly in exactly this role:** *"2KG is a substrate for demethylation of
methyl groups"*, and it rises alongside SAM when DNMT1 is lost.

**So the two nutritional agents left in the stack are both TET co-factors, and TET-mediated demethylation
is the direction senescence already runs.** F-R087 evaluated both on bone quality and length and never
asked what they do to the methylation counter, because the counter's direction was not established until
this round.

**Recommendation: remove calcium AKG entirely, and demote ascorbate to the minimum required for collagen
hydroxylation rather than a supplemented dose.** The collagen argument for ascorbate is real (F-R087) and
that is why I am saying minimum-required rather than zero — prolyl hydroxylase needs it too. But
supplementing it above requirement is, on this round's evidence, buying collagen at the cost of the
counter.

**This is the kind of hole you have been asking me to find, and it was inside the stack rather than
outside it.**

---

## 5. What raises DNMT1 — the honest survey

| candidate | evidence | obtainable |
|---|---|---|
| **partial reprogramming (OSK)** | **direct: DNMT1 mRNA and protein up, persists 2 weeks post-withdrawal, methylation age down** (Su, F-R081) | **no — AAV, no human skeletal use** |
| removing TET cofactors (ascorbate excess, AKG) | indirect — reduces the opposing reaction | **yes, and free: it is a subtraction** |
| SAM / methyl donors | **closed — not substrate-limited** (§2) | n/a |
| DNMT1 transcriptional activators | none identified | — |

**The subtraction is the only obtainable move, and it is a subtraction from our own stack.** That is not
nothing — it is free, immediate, and correctly signed — but it is not an agent.

---

## 6. Where the three rows stand

| row | status |
|---|---|
| **1. setpoint** | DNMT3A inhibition +3.0 SD, Hedgehog het-dose +2.9 SD — **human-validated, pharmacologically empty** |
| **2. spend slower** | dexamethasone (banking) + anastrozole (now pool-preserving and front-loaded) — **both approved** |
| **3. counter** | **direction known** (maintenance methylation loss), **ceiling known** (DNMT1 enzyme, not SAM), **agent identified and correctly signed on both axes** (partial reprogramming), **never measured in growth plate** |

## 7. Asks — three, all genuinely absent from the 71 files indexed

1. **Any OSK / partial-reprogramming experiment with a growth-plate, bone-length, or chondrocyte
   proliferative-capacity endpoint.** §3 is one experiment away from being an arm and I cannot find it.
2. **Stevens DG, Boyer MI, Bowen CV 1999** — the transplantation primary source. Identified from
   Nilsson's reference list, not on disk, and it is the constraint that rules out systemic agents for
   row 3.
3. **Any measurement of DNMT1 protein or global methylation in growth-plate cartilage after any
   intervention** — reprogramming, drug, or diet. Nilsson 2005 measured the natural decline; nobody
   appears to have tried to move it.

*(`318.pdf` is the Funaba sheep paper — noted, already read as `Funaba1990.txt` in batch14.)*

---

*Everything decisive this round was on disk: the Xiu figure, the Yanagihara SAM measurement, and the
F-R081 DNMT1 result that resolves last round's conflict. The index now exists so that the failure mode
is fixable by grep rather than by you re-sending files.*
