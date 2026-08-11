# ASK LIST — the retinoid / RARγ arm, as of round 260 (2026-08-11)

Every open question on this line, what would close it, and whether I can close it myself.
Ordered by how much it changes the answer.

---

## A. THINGS I NEED FROM YOU — I have tried and failed to reach these

### A1. `uchibe2017` full text — PMID 27325507, **not open access**
*Genetic and pharmacological inhibition of retinoic acid receptor γ function promotes endochondral bone formation.* Uchibe K et al., 2017.

**Why it matters most of anything on this list.** Every systemic claim about 7C in this atlas currently rests on **one citing sentence** in `tateiwa2022`. This paper holds:
- the **systemic dose, route and schedule** for 7C — without which the arm cannot be specified as a protocol at all
- the **RARγ-null control experiment** (`tateiwa2022` asserts it in discussion; it is not shown there)
- the **genetic arm** — what genetic RARγ inhibition does to endochondral bone, which is the internal control on the pharmacology
- possibly selectivity data and any **basal-repression / co-repressor assay**, which would settle 7C's class the way `le2019a` settled CD2665's

### A2. `tateiwa2022` Supplementary Figure S1 — the numbers, read off by eye
Open access, and I **have** the file — `atlas/data/round260/s1/image1.emf`. Its legend states it contains **MW, IC50 and EC50 for 7C and NRX204647** plus both chemical structures. The EMF stores its text as **vector paths, not text records**, so string extraction returns only font names, and LibreOffice on this machine refuses to load the container.

**All I need is four numbers and a structure:** 7C's molecular weight, its IC50, NRX204647's EC50, and whether any RARα/RARβ selectivity ratio is printed. Any machine that opens the .docx will show it.

### A3. `koyama2021` full text — PMID 33724538, PMC9661967, **OA: N**
I have only the abstract. The load-bearing arm is the **CD2665-monotherapy** one, where the abstract says only *"the expected maturation delay and growth plate expansion"*. I need:
- whether **any bone length** was measured in the CD2665-alone arm, and its magnitude
- the zone heights and any cell counts
- whether resting-zone/progenitor number was measured under CD2665 alone — this is the arm that would show whether it spends the pool

### A4. `matsuoka2025a` — PMID 40714875 (growth plate injury, retinoid antagonist), and `Shield et al. 2020`
Lower priority. `matsuoka2025a` is the third protective result on this axis and I hold only its title and opening lines. Shield 2020 is the NRX204647 PLA-nanoparticle safety/tolerability precedent.

---

## B. THINGS I CLOSED THIS ROUND WITHOUT HELP

- **CD2665's class** — `le2019a`. At RARγ it **cannot dissociate SMRT**; at RARα it **does**, and with a rexinoid it **activates**. Not an inverse agonist, and not RARγ/β-selective.
- **7C's chemotype** — patent **WO 2005/066115 A2** is titled *"Disubstituted chalcone oximes having RARγ retinoid receptor antagonist activity"*. A **chalcone oxime** — a completely different scaffold from CD2665 (adamantyl arotinoid), BMS204,493 (dihydronaphthalene/phenylethynyl) and AGN193109 (acetylenic). Structural class transfer between these compounds is therefore invalid.
- **7C's sourcing** — custom-synthesised by Atomax Chemicals (Shenzhen) from the patent; **no CAS number**. Not a catalogue reagent. Its matched agonist NRX204647 **is** catalogued (CAS 1351452-80-6).
- **7C's local doses** — 50 nM in vitro; 0.3 / 1.0 / 5.0 µg per PLA-nanoparticle pellet in vivo, dose-dependent, n = 17–25.
- **RARγ expression and zonality in the human plate** — round 256/257, from archived GSE288028.

---

## C. THINGS NOBODY CAN GIVE ME — they do not exist and must be generated

### C1. **Has any RARγ antagonist ever been given to a normal growing animal with a bone LENGTH endpoint?**
**No.** Every published skeletal use of 7C is BMP-induced ectopic bone, spinal fusion, or protection of an *injured* plate. Every use of CD2665 is rescue of drug- or injury-induced closure. **Nobody has asked whether a normal bone gets longer.** This is the experiment, it is specified in `g_l3_does_an_rargamma_antagonist_add_length_to_a_normal_animal`, and no amount of literature access closes it.

### C2. **Is 7C an inverse agonist or a co-repressor-preserving antagonist at RARγ?**
Its own authors list *"RARγ inverse agonist"* among the paper's **keywords** — a designation, not a measurement. The assay that would settle it (SMRT/NCoR recruitment by subtype, as `le2019a` ran for CD2665) **has never been run on 7C**. After round 259 this matters less than it did — in a zone where repression is already saturated, preserving it is sufficient — but it is unresolved.

### C3. **The BMP-Smad1 conflict — the sharpest open objection on this arm.**
`tateiwa2022` shows RARγ antagonists (7C **and** CD2665) **raising** pSmad1 and Id1-luc, with agonists suppressing. This atlas's root cell is defined by holding **BMP-Smad1/5 down** (rounds 241, 243); `ambrosi2025` independently derived a **BMP inhibitor** (DMH1) as half its combination; and `orikasa2024` named osteogenic conversion of resting-zone cells as the failure mode.

Three reconciliations, none established: different compartments; an artefact of the ectopic BMP-2 model; or genuine incompatibility, in which case 7C buys amplification while spending the pool — the growth-hormone failure mode in a new molecule. **Only C1 discriminates**, because option three shows up as resting-zone depletion and the other two do not.

### C4. **Does endogenous RARγ ligand tone exist in the postnatal growth plate?**
Round 259 inferred that it must, because a compound that cannot enhance repression nonetheless had a monotherapy effect. `williams2009` measured the zones as retinoid-free in mouse. Nobody has measured retinoid concentration in a **human** growth plate, and nobody has measured it in a postnatal mouse plate under the conditions `koyama2021` used.

---

## D. STANDING ITEMS FROM EARLIER ROUNDS, STILL OPEN

- **PLAGL1 as the senescence-counter link** (round 257) — `williams2009`'s co-repressor Zac1/PLAGL1 is one of eleven imprinted genes that `arm3` records as declining with age in step with growth rate. Whether PLAGL1 decline weakens RARγ repression has never been tested. Graded E.
- **The `yamaguchi1998` Hox prediction** (round 258) — resolved by inference; nobody measured posterior Hox genes in those transgenics.
- **Term attribution for intermittent PTH1R agonism** (round 254 table, row four) — whether it raises amplification or spends pool; the same missing decomposition as C1, for a different compound.
