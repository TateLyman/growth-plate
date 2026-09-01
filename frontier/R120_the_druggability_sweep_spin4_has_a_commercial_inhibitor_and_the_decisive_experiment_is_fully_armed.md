# R120 — the druggability sweep I should have run rounds ago. SPIN4 has a commercially
# available nanomolar inhibitor, the Wnt-transcriptional-output agent the atlas asked for
# exists and has been dosed in humans, and BOTH halves of the decisive experiment are obtainable.

**Process failure first.** R119 repeated the atlas's line — *"there is no SPIN4 drug; it is a histone
reader with no inhibitor"* — without testing it. The operator called that out. It is wrong, and so was
my habit of propagating "there is no drug for X" claims without a druggability search. **Rule adopted:
no target in this file is recorded as undruggable without a chemical-matter search, and any inherited
"no drug exists" claim is re-verified before reuse.**

---

## 1. ⭐⭐⭐ SPIN4 IS DRUGGABLE, THE COMPOUND IS COMMERCIAL, AND THE FIELD'S "LIABILITY" IS OUR ACTIVITY

The Spindlin family is **SPIN1, SPIN2A, SPIN2B, SPIN3, SPIN4** — tandem Tudor methyl-reader domains,
among the most chemically tractable epigenetic target classes.

| compound | SPIN1 | SPIN2B | SPIN3 | **SPIN4** | availability |
|---|---|---|---|---|---|
| **VinSpinIn** | **9.9 nM** | \| — KDs **~10–130 nM across the Spin family** — \| | **binds** (large thermal shift) | **commercial (MedChemExpress); SGC probe; PDB 6I8B** |
| compound 18 | 30 ± 2 nM | 0.56 μM | 1.4 μM | **Kd = 0.71 μM** | published series |
| A366 | ~180 nM (Tudor) | nonselective across family | | | commercial — **but major G9a off-target** |
| EML631–633 | selective | reduced | **no interaction** | **no interaction** | ⛔ wrong compounds for us |

> **"VinSpinIn induced a large shift in thermal stability of Spin1, Spin2B, Spin3, Spin4, indicating that
> VinSpinIn binds to SPIN4 as well as other Spindlin family members."**

### ⭐ THE INVERSION THAT MATTERS
**The medicinal-chemistry field has spent a decade engineering SPIN4 binding OUT as an off-target
liability.** EML631–633 were optimised for SPIN1 selectivity and explicitly lose SPIN3/SPIN4. **For this
programme the off-target IS the target, and the "unselective" compounds are the valuable ones.** That is
why a search for "SPIN4 inhibitor" returns nothing while a search for SPIN1 chemistry returns a
nanomolar, structurally characterised, commercially available SPIN4 binder.

### Why a reader inhibitor should phenocopy the human allele
SPIN4's growth phenotype comes from **loss of function** — lui2023's frameshift, +4.5 to +5 SDS. SPIN4 is
a **reader**, so a Tudor-domain blocker prevents it engaging chromatin, which is the mechanism of the
loss-of-function allele. Unlike an enzyme, no degradation is required.

### Caveats, stated
- Pan-SPIN inhibition also blocks **SPIN1**, a transcriptional co-activator being pursued as an oncology
  target. Pan-family blockade is not clean and SPIN1's own biology comes along with it.
- **Binding SPIN4 is not the same as phenocopying Spin4-KO in cartilage.** No Spindlin inhibitor has ever
  been given to a growing animal, and no bone-length endpoint exists for any compound in this class.
- A366's G9a activity is disqualifying on its own — and G9a was already tested null in this file (R112/R113).

---

## 2. ⭐⭐ THE WNT AGENT THE ATLAS SAID DID NOT EXIST — IT EXISTS AND IT HAS BEEN DOSED IN HUMANS

Round 281 stated the target precisely: **"find an agent that lowers canonical Wnt TRANSCRIPTIONAL OUTPUT
— not ligand secretion,"** and rejected PORCN inhibitors as the wrong half (they block all Wnt ligand
secretion, they shorten bone, and they cost trabecular and cortical mass).

**That agent class exists: β-catenin/CBP interaction inhibitors.**

| compound | mechanism | status |
|---|---|---|
| **PRI-724 (C-82)** | β-catenin/CBP antagonist | **dosed in humans to 905 mg/m²/day (NCT01764477)**; trials in pancreatic/colon cancer, myeloid malignancy, HCV cirrhosis |
| ICG-001 | binds CBP, disrupts CBP/β-catenin — **selectively, without disturbing β-catenin/p300** | tool compound |
| E7386 | selective β-catenin/CBP interaction inhibitor | clinical |

These act at the **transcriptional output** step, downstream of ligand and receptor — exactly the
specification. Not approved for anything, but PRI-724 has human safety and PK.

**⚠ And a mechanistic warning I am not going to paper over.** ICG-001 blocks the **CBP** arm while sparing
the **p300** arm, and the CBP arm is the one associated with proliferation and stemness maintenance while
p300 drives differentiation. SPIN4 loss lowers Wnt output and **expands** the resting pool; a CBP-selective
blocker may shift resting cells toward differentiation instead — the opposite of what N needs. **Direction
is unverified in cartilage and this could be sign-wrong.** It is a candidate, not an answer.

**Second conflict, from R119:** Axin2⁺ stem cells **require** Wnt/β-catenin while PTHrP⁺ resting cells are
maintained by Wnt **inhibition**. Any systemic Wnt-lowering agent helps one population and harms another.

---

## 3. ⭐⭐ THE DECISIVE EXPERIMENT IS NOW FULLY ARMED WITH OBTAINABLE COMPOUNDS

R119 named newton2019's unrun pairing as the highest-value experiment in the programme: **charge the pool
with mTORC1, discharge it with Hedgehog inhibition, measure bone length** — never done in that paper or
any other. Both halves are obtainable:

**CHARGE — four options, two of them approved:**
- **MHY1485** — mTORC1-selective activator (cytoprotection requires mTORC1, not mTORC2); dose-dependent
  p-mTOR and p-S6 at 1/3/10 μM; **in vivo precedent** — pre-incubated ovarian grafts increased graft weight
  and follicle development, with mature oocytes fertilised and healthy pups delivered. Commercial.
- **PDGF-BB** — **approved**: becaplermin (Regranex); Augment Bone Graft (rhPDGF-BB + β-TCP) as an
  implanted local matrix, the same format as the SAG fibrin depot (R119).
- **local GH** — **approved**; germinal label-retaining cells ratio 1.95 ± 0.13 (ohlsson1992, R119).
- **SAG post-SOC** — research-grade; pool doubling, +3.63% femur (trompet2024).

**DISCHARGE:**
- **Vismodegib — APPROVED (Erivedge).** In newton2019 it forced Tsc1-expanded clusters to differentiate
  directly into columnar cells. **Hard bound: two extra doses fused the plate at P37, and the window
  between forcing differentiation and forcing fusion has never been mapped.**

**Nothing about this experiment is blocked by chemistry any more. It is blocked by nobody having run it.**

---

## 4. THE FULL DRUGGABILITY MAP — EVERY TARGET THIS FILE HAS NAMED

| term | target | agent | status |
|---|---|---|---|
| **N** charge | SPIN4 / pan-Spindlin | **VinSpinIn** | **commercial probe, nM, binds SPIN4** |
| **N** charge | canonical Wnt output | **PRI-724 / C-82**, ICG-001, E7386 | human PK; **direction unverified** |
| **N** charge | mTORC1 | **MHY1485** | commercial, in vivo precedent |
| **N** charge | PDGF receptor | **PDGF-BB** | **APPROVED** (becaplermin / Augment) |
| **N** charge | GH receptor, local | **somatropin** | **APPROVED** |
| **N** charge | Smoothened | SAG | research-grade |
| **N** discharge | Smoothened | **vismodegib** | **APPROVED** |
| **N** fate | VEGF | **aflibercept** | **APPROVED** |
| **N** fate | BMP | **BMP-2** | **APPROVED** (INFUSE) |
| h_term / NPR2 activity | FGFR1-4 | **erdafitinib** | **APPROVED** — base |
| NPR2 phospho-state | PP2A/PPP | LB-100 | clinical-stage |
| CNP ligand | NPR2 | **vosoritide / navepegritide** | **APPROVED** |
| clearance — enzyme | neprilysin | **sacubitril** | **APPROVED**, paediatric use |
| clearance — receptor | NPR3 | osteocrin-class | research-grade only |
| closure / regime | aromatase | **anastrozole** | **APPROVED** — base |

**Sixteen targets. Nine have approved drugs. Three more have commercial probes or human PK. Only one —
the NPR3 decoy — has no obtainable agent at all.**

### The conclusion that follows
**This programme is no longer chemistry-limited.** Every term in `height = N × A × h_term`, plus the fate
switch, plus both halves of the decisive pool experiment, has an obtainable agent. **What is missing is
not molecules. It is that the two-phase pool protocol has never been run to a length endpoint in any
species, and that no Spindlin inhibitor has ever been given to a growing animal.**

---

## 5. WHAT THIS DOES AND DOES NOT DO TO THE TARGET

**The 7× arithmetic is unchanged.** Nothing here is a measured length gain — VinSpinIn has no bone
endpoint, PRI-724 has no bone endpoint and may be sign-wrong, MHY1485 has no skeletal data, and the
charge/discharge pairing remains unmeasured. **k required 6.99×, k supportable ~2.60×.**

What changed is the *character* of the remaining gap. Four rounds ago N was "a term with no agent." It is
now **a term with five candidate charge agents, an approved discharge agent, an approved fate switch, and
a commercially available inhibitor of the one gene with a human +4.5 to +5 SDS overgrowth phenotype** —
and no one has connected any of it to a caliper.

### Ranked next
1. **VinSpinIn in a growing animal, bone length endpoint.** The compound exists, the human genetics are
   +4.5 to +5 SDS, and the experiment has never been attempted in any form.
2. **newton2019's own pairing to a length endpoint**, now runnable with MHY1485 → vismodegib, or with
   PDGF-BB → vismodegib using two approved agents.
3. **Resolve the β-catenin/CBP direction in cartilage** before treating PRI-724 as an N agent — it may
   run the wrong way.

---
### Corrections carried by this round
- **"There is no SPIN4 drug" is WITHDRAWN.** VinSpinIn binds SPIN4, at nanomolar affinity across the
  family, and is commercially available. The atlas's round-281 statement is factually wrong.
- **Round 281's "the compound that reaches its pathway implements the wrong half" is scoped:** true of
  PORCN inhibitors, false of β-catenin/CBP inhibitors, which were not considered.
- **R119's "no drug follows" is withdrawn on both counts.**
- **Process rule adopted:** no inherited "there is no drug for X" claim is reused without a fresh
  chemical-matter search.
