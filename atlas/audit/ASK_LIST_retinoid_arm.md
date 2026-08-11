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

---

# ADDENDUM, round 266 — new asks under the standing paywall rule

The rule set this session is: **never drop a source because it is paywalled. Always ask.** These are the outstanding requests as of round 266, in priority order.

### 1. `marchanalvarez2026` — PMID 42464284, BMC Biology 2026, **not open access**
*Dynamin inhibitor dynasore modulates longitudinal bone growth in a hormetic manner.*

**The only genuinely new node found this session, and the only candidate with a wild-type length result on a non-signalling control point.** 40 µM dynasore *significantly increased* longitudinal bone growth in ex vivo mouse metatarsals; 220 µM abolished chondrocyte proliferation. I need:
- the **effect size** at 40 µM — the abstract says "significantly increased" and gives no number
- the **EdU and matrix quantification**, and whether **resting-zone cell number** was measured at all (this decides whether it is discharge or depletion)
- the **full dose-response** between 40 and 220 µM — the therapeutic window is the whole question
- whether FGFR3 or any receptor internalisation was measured, since that is the specific collision risk with erdafitinib

### 2. `hirota2022` — the dual-FRET biosensor paper
Held in the atlas and cited by `is_the_cnp_arm_redundant_with_fgfr3_blockade`, but I have not read it in full. It carries the **H89 necessity test** that makes the CNP axis two arms rather than one — which is now one of the three legs holding vosoritide in the stack. If that test is weaker than the summary implies, the redundancy question reopens.

### 3. Anything that resolves the hedgehog contradiction
`resting_zone_niche` records that **both Smoothened agonism *and* antagonism reduce the number of columns formed from labelled resting cells.** Round 251 proposed hedgehog *withdrawal* as the discharge signal. Both cannot be right as stated. The primary behind that statement, read in full, is what settles it — and it may invalidate the discharge model built in round 265.

---

# ADDENDUM, rounds 268–269 — current asks

Standing rule: a paywall is never a reason to drop a source. These are outstanding, in priority order.

### 1. ~~`brjesson2010`~~ — **SUPPLIED AND CLOSED, round 270.** PMID 20564247, and it is *J Bone Miner Res* 25:2690–2700, not Endocrinology — my journal attribution was wrong. Read in full; Figure 5A digitised (`atlas/tools/round270_borjesson2010_fig5A.py`): femur **+3.17 % at 12 months**, growth increment **2.93× control** between 4 and 12 months, n = 9–12. Crown-rump **+2.1 % ± 1.7, n.s.** — appendicular only. Serum IGF-1, sex steroids, BMD and cortical dimensions all unchanged. It also **reversed** round 269's GPER-1 claim via its own reference list (CORR-278).

### 1b. `brjesson2010` — original entry, retained for the record
*The role of estrogen receptor α in growth plate cartilage for longitudinal bone growth.* Börjesson AE et al.

**The single most useful document on this list.** Its abstract carries the load-bearing result of round 269 — cartilage-specific ERα-null mice **continued to grow after 4 months while controls stopped, giving increased femur length at 1 year** — and I hold nothing else. I need:
- **the magnitude of the one-year femur difference**, with group sizes and sex distribution (the abstract gives none)
- whether **body length** was measured as well as femur, and whether the plates were still open
- the **high-dose oestradiol challenge** numbers, since that is the arm showing the brake is ERα-mediated and local
- whether **GPER-1 or ERβ** were measured in the same animals — nobody has deleted both, and that is the experiment round 269's open proposal turns on

### 2. The **Yakar 2009** four-genotype comparison — primary not yet identified by PMID
Quoted in `dobie2015`'s introduction: ALSKO −60 % serum IGF-1 → 8 % shorter; **BP3KO −40 % → 5 % LONGER**; LID −80 % → equal length; triple-null at 2.5 % of wild-type IGF-1 → only 6 % shorter. This is the four-genotype demonstration that **serum IGF-1 does not predict linear growth potential**, and it bears directly on the case fact of IGF-1 = 198. I have it only as a secondary citation, which CORR-268 and CORR-270 say is not good enough to grade on. **The primary, or its PMID, would let this move off D.**

### 3. `lui2019` — PMID 30765323, PMC6404097, **OA: N** (PMC record is abstract-only)
*Cartilage-Targeted IGF-1 Treatment to Promote Longitudinal Bone Growth.* The first CV1574-1 paper. `tailor2024` (the sequel) is open and I have read it in full. From `lui2019` I need: the **dosing**, and above all whether **any bone length** was measured in the lit mouse — both papers report growth plate height only, and that is the step that decides whether this molecule is a height agent or another taller-plate result.

### 4. `mizuhashi2018` Methods — Nature 563:254, PMC6251707
The deposited author manuscript has **no Methods section**. I need the **dose, route and schedule for SAG and LDE-225**, which is the only thing separating its early-treatment regime from `newton2019`'s late one. Not load-bearing after round 268, but it is the last loose end on the hedgehog line.

### 5. `troib2013` — PMID 23715123, **OA: N**
SOCS2 elevated in CKD growth retardation, impairing growth-plate GHR–JAK2/STAT5 signalling. Would make the SOCS2 loop of round 269 a two-context result rather than one ex vivo model.

---

### AND ONE THING I DO NOT NEED FROM YOU — the 231

`atlas/data/round269/length_endpoints_sweep.tsv` lists **231 references already in this bibliography that report a bone, limb or body length endpoint and from which no number has ever been extracted**, 83 of them reporting a gain. Most are open access. **That list is cheaper than any new search and should be worked through before the next external sweep.** No action needed from you.

---

# ADDENDUM, round 270 — what the supplied PDF closed, and the two it opened

**Closed:** `brjesson2010`. Every question I listed against it is answered — magnitude, group sizes, sex, the high-dose E2 numbers, and whether the other oestrogen receptors were measured in the same animals (they were not, but the paper's reference list answered the question anyway).

**Opened, and both are low priority because the abstracts may be enough:**

### ~~`windahl2009`~~ — **SUPPLIED AND CLOSED, round 272.** PMID 19088255. Read in full: E2 decreased femur length in WT and not in GPR30-null, and reduced plate height, PZ, HZ **and terminal hypertrophic cell height** in WT only, while eight other oestrogenic responses were intact across five doses. GPR30 is a **brake transducer**, not an accelerator.

### ~~`mrtensson2009`~~ — **SUPPLIED AND CLOSED, round 272.** PMID 18845638. The baseline deficit is proportional, female-only, with reduced serum IGF-I and a full metabolic syndrome — systemic, not cartilage.

### (original entries retained below)

### `windahl2009` — PMID 19088255, Am J Physiol Endocrinol Metab, **OA: N**
*The role of the G protein-coupled receptor GPR30 in the effects of estrogen in ovariectomized mice.* This is the paper that **reversed** round 269's GPER-1 claim: oestradiol reduced femur length and growth plate height in wild-type but not GPR30-null mice. From the abstract I have the direction and the five doses. I would want the **magnitude of the femur-length difference** and whether growth plate **zone** heights were resolved — but the direction is what mattered and it is already unambiguous.

### `mrtensson2009` — PMID 18845638, Endocrinology, **OA: N**
*Deletion of GPR30 impairs glucose tolerance, reduces bone growth...* I need only to know **how much** of the body-growth deficit tracks the reduced serum IGF-1, since that decides whether the smaller GPR30-null mouse is a cartilage result at all. Lower priority than the above.

**Neither is worth interrupting you for.** The GPER-1 sign is recorded as unresolved and the ERα line does not depend on it.

---

# ADDENDUM, round 272 — three new asks, all from the supplied papers' reference lists

Both GPR30 papers are closed. Their bibliographies opened three more, and the first is the one that makes the argument stage-dependent.

### 1. `chagin2007a` — PMID 17878253, J Clin Endocrinol Metab 92:4873–4877, **OA: N**
*GPR30 estrogen receptor expression in the growth plate declines as puberty progresses.*

**Human growth plate tissue, and from exactly our population.** Tibial growth plate biopsies from **14 boys and 7 girls at epiphysiodesis**, performed for leg-length inequality or **extreme tall stature**, across pubertal stages. From the abstract I have only the direction. I need:
- the **quantification of the decline** and its statistics — how much is left at Tanner 4–5, which is the subject's stage
- the **zonal detail** (abstract says highest in hypertrophic chondrocytes; the resting-zone signal is mentioned in `windahl2009`'s citation of it but not quantified in the abstract)
- whether **ERα and ERβ were measured in the same sections** — `windahl2009` says they do not decline, citing other papers, and a within-section comparison would be much stronger

### 2. `chagin2004` — PMID 14753739, J Bone Miner Res 19:72–77, **OA: N**
*Estrogen receptor-beta inhibits skeletal growth and has the capacity to mediate growth plate fusion in female mice.*

**The only brake in this set that reaches the AXIAL skeleton** — which is the half of standing height that CORR-279 showed the cartilage-ERα lever misses. I need the **magnitudes** for appendicular versus axial growth in ERβ-null females, the ages, and whether any male data exist at all (`windahl2009` states ERβ modulates growth in female but not male mice, which if true removes this for a male subject).

### 3. `heino2008` — PMID 18434348, J Endocrinol 197:R1–R6, **OA: N**
Lower priority. GPR30 in human bone cells declining through puberty (osteocytes R = −0.56). The growth-plate paper above matters more.

---

# ASK — round 281, the SPIN4 arm (opened 2026-08-11)

**One item, and it is the highest-value paywalled item this file has had in a while.** It is the third
independent human report of the axis that round 281 identified as the cleanest resting-pool lever in the
atlas, and the adult-height evidence for that axis currently rests on **n = 2 carriers in one family**.

### 1. `SPIN4-related X-linked overgrowth in a family` — **REQUESTED**
- PMID **41780720** · DOI **10.1016/j.ejmg.2026.105073** · *European Journal of Medical Genetics*, 2026
- Not open access. No PMC record. No preprint found.
- **Why it matters:** the third SPIN4 family. `lui2023` is family 1 (the only source of ADULT attained
  heights — mother and maternal grandmother, each +2 SDS above their own midparental height). `chawla2025`
  is family 2 (replicates overgrowth and segregation, but reports no adult height, and its affected sibling
  had **bone age 9–11 at chronological age 8**, which removed "overgrowth without bone-age cost" as a class
  property). A third pedigree is the difference between grade **D** and grade **B/C** on the claim that
  partial SPIN4 loss raises **attained adult** height in humans.
- **What is needed from it, specifically:** (a) any **adult/final** heights in carriers, with midparental
  heights; (b) **bone age vs chronological age** for every measured individual; (c) whether heterozygous
  females are affected and by how much; (d) IGF-1 values, to test whether the normal-IGF-1 finding
  (179 ng/mL in the `lui2023` proband, *below* this subject's 198) replicates.

### Already obtained without asking — recorded so it is not re-requested
- `lui2023` (SPIN4, JCI Insight) — full text, read.
- `lui2026` (Spin4 at 18 months, bioRxiv) — abstract only; full text not retrievable, but the abstract
  carries the load-bearing facts (length gain persists at 18 mo, BMD normal, tumour count up).
- `chawla2025` (family 2) — full text, read.
- `gao2024`, `mirzamohammadi2016`, `shao2021`, `killinger2025`, `dreyer2025` — full text, read.
- `dudakovic2015`, `camilleri2018` — abstract only; both are conditional-KO direction results and the
  abstracts state the direction explicitly, so full text is not blocking.
- Avijgan human growth-plate spatial transcriptomics — already in the graph as `avijgan2026br`.
