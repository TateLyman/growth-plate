# F-R005 — the ceiling is avascularity, and the ladder out of it

**Every hard constraint this repository has found is downstream of one anatomical fact. A mammal
already exists that removed that fact and does endochondral ossification 365× faster. This is the
ladder from the rung available today to the rung whose ceiling is not set by growth-plate biology at
all.**

Date 2026-08-27 · operator-supplied primary read in full: `loopmans2025`, *Nature Metabolism* 7:182–195,
PMID 39794539 · new local analysis in `frontier/screens/redox_axis/`

---

## 0. The reframe

The atlas has, independently and in different rounds, priced six limits on elongation:

| round | the limit found |
|---|---|
| R454 | the chondrocyte secretes matrix **at the plasma-cell ceiling** — the maximum rate known for any animal cell |
| R461 | the Golgi module is limited by **acceptor and donor supply**, not by enzymes |
| R448 | elongation is **extensibility-limited**, not pressure-limited; and **animals have no expansin** |
| R450 / R452 | the plate is **advection-fed**, its interior half as diffusive as its periphery, permeability **exponentially strain-dependent** |
| R315 / enum-10 | a hard **molecular-weight wall**: 332 Da–10 kDa enter, **≥40 kDa does not** |
| `loopmans2025` (new) | in hypoxia, output generates ROS faster than **NADPH** can pay it down, and the failure mode is **ferroptosis** |

**Six limits, one cause. The growth plate has no blood supply.** Not one of these limits exists in a
perfused tissue. And the atlas already holds the counterexample and did not follow it:

> **`ba2025`: the deer antler growth centre, growing by ENDOCHONDRAL OSSIFICATION, elongates up to
> TWO CENTIMETRES PER DAY, against ~2 cm per YEAR for a human growth plate. 365-fold. In a mammal.
> In the same tissue type.** Among the five things its authors attribute it to is **"a richly
> vascularised niche."**

R199 recorded this and stopped at the fork:

> **"FIFTH, THE VASCULAR INVERSION, WHICH IS EITHER THE LEVER OR THE TRIGGER.** One reading is that
> the human reserve is starved and vascularity is part of what the antler buys. Against it: hypoxia
> is what keeps resting-zone cells quiescent and stem-like, and vascular invasion of a growth plate
> **IS** fusion. **Nothing in this atlas distinguishes the two, and they predict opposite signs."**

**`loopmans2025` distinguishes them.** It shows the cost of avascularity is not merely slower
delivery — it is a **redox debt that scales with output and kills the cell that incurs it.** The
antler's 365× is what endochondral tissue does when that debt is paid by perfusion. The reason a
human growth plate cannot go faster is not its signalling. **It is its plumbing.**

---

## 1. What the operator-supplied paper actually contains (read in full)

Beyond the abstract, four things:

1. **Ferroptosis is the third most upregulated pathway in the knockout growth plate, and it is
   specifically the HYPERTROPHIC zone** (Fig. 3c) — the compartment carrying 44–59% of elongation.
2. **Lipid peroxidation is measured two ways in vivo**: 4-HNE immunostaining in mutant plates, and
   oxidised BODIPY-C11 by flow cytometry; `Ptgs2`, the ferroptosis-onset marker, is up.
3. ⭐ **The tax is not a knockout artefact.** Verbatim: *"hypoxia increased lipid peroxidation in
   cultured proliferating and differentiating chondrocytes of **both genotypes**, but the most
   pronounced increase was observed in G6PDH-null differentiating hypoxic chondrocytes."*
   **Wild-type chondrocytes accumulate lipid peroxidation under hypoxia. The knockout only makes the
   bill larger.**
4. ⭐ **The lesion is worst in the CENTRE of the plate** — *"disorganization of the columnar and
   hypertrophic zone, especially in the central region"* — which is exactly the compartment `cohen1994`
   and R452 identify as **half as diffusive as the periphery.** The spatial signature of the phenotype
   matches the transport physics.
5. **Proliferation is unaffected** (BrdU and flow). This is a **survival** phenotype, not a
   proliferation one — it is the **yield** term R470 measured and could not explain.
6. **The rescue is a nutrient.** Glutathione ethyl ester (1 mM) or **N-acetyl-cysteine (500 µM)**
   restore H₂O₂, free cysteine thiols, ubiquitination, all three proteasome activities, lipid
   peroxidation and **cell viability**. ⛔ **In vitro only. There is no in vivo NAC arm and no rescued
   bone length.**

---

## 2. ⭐⭐ The new local finding: the growth plate is a cysteine auxotroph with a weak importer

Run against the atlas's own `query/human_growth_plate_expression*.csv` (GSE288028, 4 human donors),
% of cells detected, by zone:

| gene | stem | prolif | prehyp | hyper | what it is |
|---|---:|---:|---:|---:|---|
| **CBS** | **0.0** | **0.4** | **0.3** | **0.6** | **transsulfuration step 1 — the committed step of making cysteine from methionine** |
| **SLC7A11** | **1.1** | **2.9** | **3.2** | **1.1** | **system xc⁻ — the cystine importer. Lowest transporter on the entire panel.** |
| SLC1A4 (ASCT1) | 5.1 | 11.2 | 14.0 | 7.9 | the reduced-cysteine importer — modest |
| CTH | 6.3 | 14.1 | 15.3 | 11.1 | transsulfuration step 2 — **downstream of the step that is absent** |
| GCLC · GSS · GSR | 11.5 · 8.7 · 10.2 | 10.7 · 19.5 · 16.7 | 16.5 · 19.7 · 21.3 | 9.9 · 13.6 · 22.2 | the entire glutathione synthesis and recycling apparatus — **present** |
| GPX4 | 35.1 | 43.1 | 50.2 | 43.2 | the consumer — **abundant** |
| *SLC38A1 · SLC7A5 · SLC1A5* | *15.6 · 16.3 · 23.8* | *36.2 · 40.9 · 33.0* | *40.0 · 39.7 · 36.6* | *31.9 · 28.6 · 22.7* | *other amino-acid transporters, for scale — all 5–30× SLC7A11* |

> **The tissue has the complete downstream glutathione machinery, an abundant consumer, no ability to
> synthesise the substrate, and the weakest importer on its own transporter panel — in the one tissue
> in the body with no blood supply.**

That is a supply bottleneck sitting precisely where `loopmans2025` predicts one, and it is a
**nutrient**, not a drug target.

**And it closes a loop this atlas opened and never joined.** R320/R321 took **SLC13A1**, a
*shortening* gene, and reached **oral sodium sulfate** by supplying the substrate — the only
obtainable compound this file has ever produced, and the origin of CORR-344's "different shelf."
That arm is about **sulfur for proteoglycan sulfation**. **Cysteine is the body's principal sulfur
source and the precursor of that sulfate.** One tissue, two sulfur sinks — matrix sulfation and
redox defence — and the atlas found the first limiting and never asked about the second.

⚠ `transsulfuration` returns **0 files** here. `system xc` **0**. `ERO1` **0**. `QSOX1` **0**.
`chondromodulin` / `LECT1` **0**.

⚠ **Limits.** Percent-of-cells-detected is dropout-dominated; CBS is a low-expresser in many tissues
and a 0.0–0.6% read is at the floor of what this assay resolves, so *"absent"* here means *"not
resolved above the assay floor, in a panel where its neighbours are"* — it needs a targeted qPCR or a
proteomic read, not more scRNA-seq. This is a hypothesis-generating contrast, not a measured
auxotrophy.

---

## 3. THE LADDER — ranked by CEILING, not by tractability

The atlas ranks by what can be done. This ranks by **how tall it could make someone if it worked**,
which is the question that was asked.

### RUNG 1 — supply the substrate · ceiling: small · available today
**Genes:** SLC7A11, SLC1A4, CBS, GCLC, GSS, GPX4, SELENOS/SELENOP.
**The manipulation:** raise cysteine and selenium availability to a tissue that can neither make
cysteine nor import it well. NAC is the exact agent `loopmans2025` used to restore chondrocyte
viability; selenium is GPX4's cofactor and its deficiency disease (Kashin-Beck) has a stature
phenotype.
⛔ **Every result is a rescue of a deficit — CORR-203 governs, and the elevation direction is
unmeasured in every species.** No length endpoint exists in either direction. **This is the rung with
evidence and the smallest ceiling, and it is not a recommendation to take anything.**

### RUNG 2 — make the output cheaper instead of the defence bigger · ceiling: 10–30% · untouched
Collagen folding is the ROS source. **ERO1α oxidises PDI and makes H₂O₂ as a stoichiometric byproduct.
PRDX4 does the same job and CONSUMES H₂O₂.** Same folding flux, opposite sign on the redox ledger.
**Genes:** ERO1A, ERO1B, PRDX4, QSOX1, VKORC1L1, TXNDC5, PDIA4, P4HB.
**And the local data already says something about it.** PRDX4 runs **31–51% by zone against ERO1A's
12–29% — roughly 2:1 in favour of the peroxide-CONSUMING oxidase, in every zone.**
> **The growth plate has already evolved toward the cheap oxidase. That is not a reason to dismiss the
> axis — it is the strongest evidence in this document that the peroxide load is a real selective
> pressure on this tissue.** It also means the headroom on *rerouting* is smaller than it looked, and
> the live question moves to the **capacity** of the PRDX4 branch and what limits it.
⛔ No ER-oxidase manipulation has ever been done in cartilage in any species.

### RUNG 3 — ⭐⭐ perfuse the plate without ossifying it · ceiling: the antler's 365× · the real prize
This is the rung the whole document is about.

**The plate is not passively avascular. It spends heavily to stay that way, and the local data shows
how heavily:**

| gene | stem | prolif | prehyp | hyper | |
|---|---:|---:|---:|---:|---|
| **CNMD** (chondromodulin-I) | **52.6** | **67.8** | 50.8 | 39.8 | the classical cartilage anti-angiogenic factor |
| THBS1 | 66.8 | 62.1 | 52.5 | 54.6 | thrombospondin-1 |
| SPARC | 83.6 | 79.6 | 76.8 | 75.5 | osteonectin |
| TIMP3 | 29.4 | 33.3 | 57.1 | 31.5 | |
| *VEGFA* | *12.3* | *15.2* | *17.1* | ***21.0*** | *the pro-angiogenic switch, rising as the brakes fall* |

**CNMD is one of the most abundant transcripts on any panel I have run here — more broadly detected
than ACAN in the proliferative zone — and `chondromodulin` and `LECT1` return ZERO files in this
atlas.** The gene that keeps the growth plate avascular has never been named in 477 rounds.

**The precedent that makes this more than a fantasy: cartilage canals.** Epiphyseal cartilage is
penetrated in development by vascular canals that nourish it **without ossifying it**, and they carry
their own progenitors. `cartilage canal` is a **tier-ZERO** concept in R436 — enumerated, never
scored — with the atlas's own note recording that canals *"exist in the AXIAL skeleton too"* and
*"can be perturbed experimentally in rat tibia."*

**So a vascular architecture compatible with living cartilage already exists in this animal. It is
built, used, and then given up.**

**The manipulation, stated precisely:** permit or reinstate cartilage-canal-type perfusion in the
growth plate while excluding the **osteogenic cargo** that makes vascular invasion equal fusion.
Those are separable at the gene level: type-H vessels (CD31^hi EMCN^hi) are the osteogenically
coupled ones and are induced by **PDGF-BB from preosteoclasts**; type-L are not. **The target is the
cargo, not the vessel.**
**Genes:** CNMD, THBS1/2, TIMP3, SERPINF1 (brakes to lift, locally and transiently) · PDGFB, SLIT3,
DLL4, KDR (the coupling to break) · VEGFA (the switch already rising).
⛔ **The hazard is the mechanism.** Vascular invasion of a growth plate *is* fusion — grade A, human.
This rung asks for the one intervention whose failure mode is the exact outcome we are trying to
prevent, and it must be shown to be separable before it is shown to be useful. **The discriminating
experiment is the sign test: does a canal-permissive, cargo-excluded perfusion of an epiphysis
lengthen the bone or fuse it?** Nobody has run it in either direction.

### RUNG 4 — ⭐⭐ don't build the secondary ossification centre · ceiling: the whole of fusion
Three ZERO concepts, from three independent R436 domain agents, never put side by side:

> **"Teleosts keep entirely cartilaginous epiphyses for life, providing a virtually unlimited
> chondro-progenitor pool. The SOC — an adaptation to land — is formed AT THE EXPENSE of those
> chondroprogenitors."** · *"Indeterminate growth is ANCESTRAL and permanent arrest DERIVED; arrest
> evolved by mechanistically DISTINCT routes in closely related taxa."* · *164-species squamate µCT
> survey: complete growth-plate-cartilage resorption is the predominant finding.*

**This names what imposes `nilsson2005`.** Rabbit resting-zone chondrocytes from old and young donors
do the **same number of population doublings in culture** — *"the proliferative limit is not carried
by the cell. It is imposed by the plate"* — and `THE_CLOCK.md` has called that imposed limit a target
since Phase 1 without naming what imposes it. **If the SOC is built out of the epiphyseal progenitor
pool, then fusion is not a clock running out. It is a structural trade-off with an anatomical
location, made once when vertebrates came onto land.**

**And it collides with this file's own best local result.** `trompet2024` put a SAG bead **into the
rat femoral SOC** and got femur **+2.75 / +2.64 / +3.63%** at 1, 2 and 6 months, effect **growing**,
6/6, 9/9, 8/8 animals, with proliferation and terminal cell height unchanged — pure **N**. **The one
place a local intervention has worked is the structure this hypothesis says is doing the damage.**
Reviewed in `PMID 33091640` (Bone 2021), which is one of the very few papers ever written on the
SOC's function.
**The free first step:** the atlas already holds `xie2020`'s comparative microCT **across bats,
jerboa, whales and the fossil record**. Does SOC size or timing predict residual progenitor pool and
age at arrest, across species? That is a re-read.
⛔ **The species trap in its purest form: the mouse never fuses, so the easiest model to run is the
one least able to answer this.**

### RUNG 5 — ⭐⭐⭐ add growth plates in series · ceiling: not set by growth-plate biology at all
Everything above negotiates with a per-plate budget. **This one changes the number of plates.**

The arithmetic is the entire argument. **Adult height is a sum over plates, and this atlas's ceiling
is derived per plate.** The vertebral column already demonstrates the principle at scale: **48 endplate
physes in series produce ~70 cm of trunk.** A femur has two and produces ~48 cm. **If each physis
carries its own progenitor pool and its own exhaustion budget — which is exactly what the atlas's
model asserts — then N physes carry N budgets, and the ceiling is linear in N.**

**Why this is not science fiction:** a physis is not a mysterious organ. It forms wherever a
cartilage anlage is bisected by an ossification front, it is patterned by the **PTHrP–IHH loop**, and
it is bounded and fed by the **perichondrial groove of Ranvier**. Every one of those parts exists as
a manipulable module, and enumeration 19 already records **growth-plate organoids** and **hPSC-derived
skeletal assembloids** as built — filed as *in vitro models, not therapies*, which is the whole point:
**nobody has asked what they are for.** Meanwhile **distraction osteogenesis creates a de novo
elongation zone mechanically and delivers 14.5 cm per person over 3.7 procedures** (F-R001 §5) — the
largest number in the entire intervention landscape, and it works **after** fusion.

**The manipulation:** an oriented, perichondrium-bounded engineered physis implanted mid-diaphysis, or
a distraction regenerate converted into a persistent physis rather than allowed to consolidate.
⛔ **Nothing here is close.** Orientation, vascular exclusion, mechanical integrity, and the fact that
a physis in the middle of a bone has no epiphysis to push against are all unsolved. **But its ceiling
is the only one in this document that is not set by the biology of the plate, and that is why it is
ranked last and matters most.**

---

## 4. The honest arithmetic of +50 cm

| route | plausible ceiling | why it stops there |
|---|---|---|
| every velocity lever ever tried | **+2 to +4%** | thirty years, unrelated mechanisms, same answer |
| duration lever run to its true limit | **+25 to +30 cm** | `CEILING_CENSUS`: the plate exhausts with the door open; ~197 cm observed, ~208–215 cm extrapolated |
| duration **+** a working yield lever | **unknown, and the only compound bet in the file** | yield has never been raised in any species |
| **surgical, staged, repeated** | **14.5 cm mean, tail to ~25 cm** | soft tissue, not bone (F-R001 §5) |
| **more plates** | **linear in N** | nothing exists |

**Two things follow and neither is comfortable.** First, **no single lever gets to +50 cm**, and any
document that implies otherwise is wrong. Second, the only combination whose product is large is
**duration × yield** — hold the plate open *and* stop it draining — and **yield is the term with no
mechanism, no agent and no measurement in any species.** That is why this round is about yield.

## 5. What I would rule out, so this is not a wish list

- **More velocity pharmacology.** R298's base rate is a property of the target class, not bad luck.
- **Raising the drive on h_term.** R448 computed the drive is already ~3,000-fold sufficient and the
  limit is matrix yield. Osmolytes and channel agonists are pushing on a term that is not binding.
- **Impact and vibratory loading.** R448's poroelastic penetration depth says 1–20 Hz cannot ventilate
  the plate, by two orders of magnitude. The ventilating timescale is **postural and diurnal**.
- **Human height GWAS as a source of large levers.** It is a within-body-plan instrument. The genes
  that set vertebrate scale do not vary in humans and are invisible to it by construction.

## 6. What I want next

1. ⭐ **`PMID 33091640`** (Bone 2021, *The epiphyseal secondary ossification center: evolution,
   development and function*) — full text. The abstract is four sentences; the argument for Rung 4 is
   in the body, and this is one of the only papers ever written on what the SOC is *for*.
2. ⭐ **The teleost / indeterminate-growth primaries and the 164-species squamate µCT survey** —
   PMIDs are in `atlas/concepts/enumerations/12_comparative_evolutionary.md`, rows for *"Teleost fish
   — permanently cartilaginous epiphyses"*, *"Indeterminate growth as the ancestral vertebrate
   condition"*, *"Squamate reptiles (164 species µCT survey)"*.
3. **`ba2025`** (the deer antler single-nucleus atlas) in full — specifically its **vascular** and
   **redox/metabolic** modules. If the antler growth centre upregulates cysteine import, glutathione
   synthesis or the PPP relative to a normal plate, Rung 3's mechanism is confirmed from the one
   animal that solved it.
4. **Any measurement of oxygen tension, cysteine or glutathione by zone in a growth plate, any
   species.** Enumeration 10 lists two as ZERO concepts — *"direct zone-resolved oxygen tension of the
   epiphyseal plate"* and *"oxygen tension of the epiphyseal plate distal to an arteriovenous
   fistula"* — and I cannot retrieve either.
