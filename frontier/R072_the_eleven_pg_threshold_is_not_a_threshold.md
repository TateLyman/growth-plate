# F-R072 — The OSK direction problem dissolves, the 11 pg/mL threshold is not a threshold, and the pool collapses before five weeks

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-29
**Status:** Nilsson 2005 and Schrier 2006 read in full. Both had been supplied earlier and I asked for them
again — **`frontier/SUPPLIED_INDEX.md` now lists all 126 supplied files so this stops.**

**Four findings. Two resolve open questions, one corrects a number the branch has used for twenty-five
rounds, and one changes the shape of the problem.**

---

## 1. The OSK direction problem dissolves — the assay had no site resolution

F-R071 §3 raised the strongest objection yet to the OSK route: growth-plate senescence is **methylation
loss**, while OSK's chondrocyte mechanism is **DNMT-down / TET2-up**, i.e. demethylation. Same direction as
senescence.

**The methods section settles it.** Nilsson's assay, headed *"Assessment of **global** DNA methylation"*:

> MspI digestion (or its methyl-sensitive isoschizomer **HpaII** as control) at **CCGG sites**, ³²P 5′
> end-labelling, nuclease P1 digestion, **thin-layer chromatography**; readout = *"100 times the
> radioactivity in the methyl-dCMP spot divided by the sum of the radioactivity in the methyl-dCMP spot and
> the dCMP spot."* (Bestor et al. 1984 method.)

> ### This is a **bulk, genome-averaged** measurement of what fraction of CCGG cytosines carry a methyl group. **It has zero site resolution.** It cannot distinguish global hypomethylation from focal hypermethylation at CpG islands and PRC2 targets — it returns one number for the whole genome. **It therefore cannot conflict with the site-specific clock data or with the PRC2-target convergence result (F-R070).** The objection is withdrawn.

**And the internal comparisons make the point for me.** The same assay, same animals:

| tissue / condition | global CCGG methylation with age or division |
|---|---|
| growth plate resting zone, in vivo | **decreased** (P = 0.004) |
| all three zones, distal ulna, in vivo | **decreased** (P < 0.001) |
| **liver, in vivo** | **INCREASED** (P < 0.001) |
| **cultured RZ chondrocytes** | **INCREASED**, +0.21% per population doubling (P = 0.012) |

**Global methylation moves in opposite directions in different tissues and in vitro versus in vivo.** A
measure that behaves like that is a context-dependent aggregate, not a clock.

---

## 2. The capacity result is sharper than the abstract, and it is the strongest fact in the branch

Nilsson tested Hayflick directly in these cells:

- RZ chondrocytes **do** undergo replicative senescence in culture — cumulative growth plateaus at
  **~14 population doublings**, cells enlarge, lose alcian blue and alkaline phosphatase staining, and
  **gain senescence-associated β-galactosidase.**
- Context: adult rabbit **articular** chondrocytes manage 8–10 PD; young adult **human** articular
  chondrocytes **35–40 PD**.
- **But the maximum number of population doublings did not depend on donor age (P = 0.36).**

> ### The cells possess a finite in-vitro replicative counter — **and living in an old animal does not spend it.** A 16-week rabbit's resting-zone chondrocytes have the same remaining capacity as a fetal one's. **Whatever the animal does to those cells in vivo is not consuming their intrinsic division budget.**
>
> **Two clocks, not one.** The in-vitro Hayflick counter is real and untouched by in-vivo ageing. The in-vivo limit is separate, reversible in principle, and is what actually stops growth. **This is the single most favourable fact the programme has**, and it is why an epigenetic intervention is the right class of answer rather than a cell-replacement one.

---

## 3. The 11 ± 2 pg/mL "threshold" is not a threshold

Since F-R047 the branch has treated **11 ± 2 pg/mL** as *the oestradiol level at which resting-zone
self-renewal is measurably suppressed* — a threshold, used to judge whether anastrozole or letrozole clears
it (F-R063, F-R065).

**Here is where the number actually comes from.** Schrier gave rabbits **estradiol cypionate 70 µg/kg i.m.
weekly** for two weeks and then measured:

> *"Serum estradiol concentration, measured 7 days after the second injection of estradiol cypionate, was
> **11 ± 2 pg/mL**, compared to **<5 pg/mL** in animals treated with the vehicle."*

**That is the achieved serum concentration produced by one dose, in one two-week experiment. There is no
dose–response.** Nothing was tested at 7, or 15, or 30 pg/mL. The finding is *"E2 at 11 pg/mL slowed RZ
proliferation relative to <5 pg/mL"* — **two points, not a threshold.**

> ### **Correction to F-R047 through F-R065.** "Below 11 pg/mL" is not a validated target; it is the lower of two tested concentrations. **The anastrozole-versus-letrozole argument in F-R063/R065 rested partly on which agent clears "the threshold," and that framing is unsupported.** What survives is the ranking: less oestrogen is better, and both agents get well below the level that was shown to slow RZ proliferation. **What does not survive is the idea that 11 pg/mL is a cliff.** The decision between the two agents should rest on the outcome data (anastrozole +1.0 vs letrozole +0.5 cm PAH; velocity and IGF-1 preserved) — which is where F-R063 landed anyway, for better reasons than the threshold.

---

## 4. The pool collapses before five weeks, and dexamethasone is the only agent that banks cells

**Schrier's age series — resting-zone BrdU labelling index, distal femur:**

| age | RZ labelling index |
|---|---|
| **0 weeks (late fetal)** | **95.6 ± 0.8%** |
| **5 weeks** | **9.2 ± 1.2%** |
| 9 weeks | 9.2 ± 1.1% |
| 17 weeks | 7.6 ± 1.5% |

> ### A **ten-fold collapse between fetal and five weeks, then flat.** Resting-zone proliferation is not a gradual decline across the growth period — **almost the entire fall happens before the animal is five weeks old**, and the remainder of postnatal growth runs on a compartment already at ~9% labelling. **The "senescence" the branch has been trying to postpone has mostly already happened by early postnatal life.**

RZ chondrocyte **number** per mm of growth plate also fell with age (P < 0.001) in the overall, epiphyseal
and reserve resting zones.

**And the dexamethasone/oestrogen dissociation, measured:**

| | RZ BrdU labelling index | **RZ cell number** | serum IGF-1 |
|---|---|---|---|
| **dexamethasone** 0.5 mg/kg/day s.c. | **decreased** (P<0.001), both regions | **INCREASED (P = 0.016)** — in the **reserve** RZ (P<0.001), not the epiphyseal | unchanged |
| **estradiol cypionate** 70 µg/kg/wk | **decreased** (P = 0.011) | **not significantly affected** | unchanged |

> ### Both slow resting-zone division. **Only dexamethasone increases the number of cells.** That is the difference between banking and merely braking — and it is the direct measurement behind Baron's own inference that oestrogen acts *"by a proliferation-independent mechanism, or by increasing the loss of proliferative capacity per cell cycle."* **F-R071's per-cycle-cost escape survives contact with the primary data, and this is its evidential basis.**

---

## 5. What this does to the programme

| line | status after this round |
|---|---|
| cells are intrinsically capable | **PROVEN, and stronger than stated** — Hayflick counter exists and is **untouched by in-vivo ageing** |
| the in-vivo limit is separate and epigenetic | **Baron's own conclusion**, and the two-clock reading is now explicit |
| OSK direction problem | **DISSOLVED** — the conflicting measurement was a bulk assay with no site resolution |
| cost per division is modulable | **survives on primary data** — dex banks cells, oestrogen does not, both slow division |
| 11 pg/mL threshold | **RETRACTED** — one achieved concentration, no dose–response |
| when the pool is spent | **mostly before 5 weeks in rabbit** — a new and unwelcome constraint |
| OSK reaches the resting zone | **still no** — no serotype characterised; working skeletal AAV uses secreted factors |
| reversal extends longitudinal growth | **still never attempted** |

**The new problem §4 creates:** if resting-zone proliferative collapse is ~90% complete before five weeks
in the rabbit, then interventions applied during puberty are acting on a compartment that has already
undergone most of its decline. **That does not make them useless** — Schrier's dexamethasone arm banked
cells at four weeks, KY19382 worked in seven-week-old (late pubertal) mice, and the human ESR1-null and
aromatase-null men grew into their thirties. **But it reframes "preserve the pool" as "operate a pool that
is already mostly spent," and it raises the value of anything that *restores* rather than *preserves*.**
That is an argument for the reprogramming arm over the banking arm.

---

## 6. What I need

**Nothing that I have not already been given, as far as I can determine — I checked the manifest.** Two
genuine gaps remain and neither is a document:

1. **An AAV serotype screen that includes the growth-plate resting zone.** Does not exist; every cartilage
   tropism study is intra-articular/articular, and the successful skeletal AAV work (AAV8-CNP) uses a
   **secreted** factor and never transduces a plate chondrocyte.
2. **Any epigenetic clock, site-specific, measured in growth-plate tissue across ages.** Does not exist.
   §1 shows the only growth-plate methylation data is a 2005 bulk assay. **The Petkovich (PMC5578459) and
   Stubbs (PMC5389178) mouse clocks are open and would answer it directly.**

*If either has appeared in the literature since my search, that is what I would want. Otherwise both are
experiments, not papers.*
