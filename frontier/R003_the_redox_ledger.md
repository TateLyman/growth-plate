# F-R003 — R436's blind spot was never scored, and working one of its unscored domains returns an axis this atlas does not contain

**THE BUDGET MAY NOT BE A DIVISION COUNTER. IT MAY BE A REDOX LEDGER — and that is the only lever class
that raises YIELD without raising RATE, which is the trap every other arm in this file falls into.**

Date 2026-08-27 · branch `claude/height-enhancement-research-v34b4r` · data
`frontier/screens/redox_axis/` · every PMID below resolved live against Europe PMC in this session

---

## 1. The instrument failure, with numbers

R436 is the largest coverage instrument in this repository: 21 external domain agents, 2,562 rows,
2,193 unique concepts, scored against 941 nodes / 521 gaps / 1,903 refs / CLAUDE.md. It found
**825 ZEROs (37.6%)** — concepts never mentioned anywhere in the atlas. Its conclusion:

> Filtering them to concepts that are simultaneously **cartilage-enriched at or above the ACAN
> benchmark**, at or above **20 CPM in the purity-corrected human growth plate**, AND recorded with a
> **direction pointing TALL or LONGER**, returns FOUR — and all four are syndromes rather than
> levers… **The blind spot is real and large and it does not hide an obvious missed compound.**

**Two things are wrong with that, and the second is fatal.**

### 1a. The triage ran on 23% of the blind spot

`atlas/data/round436/zero_triage.json`, 866 rows, counted directly:

| field | populated |
|---|---|
| `symbols` (gene symbols extracted) | **369 / 866 (43%)** |
| `annotations` (any expression lookup) | **199 / 866 (23%)** |
| `best_burden_cm` (any human genetic effect size) | **12 / 866 (1.4%)** |

**667 of 866 zeros were never scored at all.** The filter that "returns FOUR" could only ever run on
the 199 that had annotations. This is CORR-348 exactly — *reading an ABSENT PARAMETER as a MEASURED
NULL* — at the scale of the whole coverage map. And the extractor's failures are not random: it
returned `symbols=[]` for **"αKlotho (KL)"** and `['IGFBP','IGF']` for **"IGFBP-6"**.

### 1b. The unscored 667 are concentrated in exactly the mechanism domains

| domain | unscored / zeros |
|---|---|
| **mechanics** | **32 / 32 (100%)** |
| **cell_biology** | **70 / 72 (97%)** |
| **intervention_landscape** | 56 / 57 (98%) |
| **environment** | 50 / 51 (98%) |
| **nutrition** | 28 / 29 (97%) |
| **pharmacology** | 99 / 105 (94%) |
| **vascular_neural_immune_microbiome** | 86 / 91 (95%) |
| **comparative_evolutionary** | 46 / 52 (88%) |
| dysplasia_nosology | 10 / 41 (24%) |
| matrix | 9 / 44 (20%) |
| endocrine | 8 / 26 (31%) |

**The domain where the extractor worked is dysplasia nosology — syndromes.** So the filter's third
criterion, *"a recorded direction pointing TALL or LONGER,"* could essentially only be satisfied by a
syndrome, which is why all four hits are syndromes. **The result is a property of the extractor's
coverage profile, not of the blind spot.**

### 1c. And all three filters are ones this file's own corrections forbid

| filter used | the correction that forbids it |
|---|---|
| cartilage-enriched **≥ ACAN** | **CORR-349** — *"Abundance finds the tissue's structural proteins; enrichment plus a SIGNED effect finds levers."* **CORR-363** — the screen is structurally blind to universal machinery, so a low ratio is **not** a kill. ACAN-level enrichment is the most restrictive possible threshold and it selects for matrix proteins. |
| **≥20 CPM in the growth plate** | **CORR-342** — *"an absence is only a kill for a lever that acts THERE."* The file's own cleanest local-depot result (`trompet2024`, SAG bead, +3.63% femur) acts in the **secondary ossification centre**, and its largest arm (oestrogen) acts in the gonad. |
| direction recorded **TALL / LONGER** | **CORR-295** — being short brings a child to clinic and being tall does not, so requiring a recorded TALL direction **re-imposes the exact ascertainment bias the file identified.** **CORR-344** — *the elevation direction was never run*; and the file's only obtainable compound (oral sodium sulfate) came from **SLC13A1, a SHORTENING gene**, by supplying the substrate. |

**A filter built from three forbidden criteria, applied to 23% of the set, returning four hits, was
read as "the blind spot hides nothing."** It hides most of the mechanism space. This round works one
domain of it.

---

## 2. What the unscored cell-biology domain contains

Verbatim from `zero_triage.json`, all tier ZERO — never mentioned in a node, a gap, a reference or
the ledger. A partial list, because the point is the class:

> Ferroptosis of growth-plate chondrocytes · Chondrocyte pentose-phosphate pathway → oxidative
> protein folding · Histone lactylation under intermittent hypoxia · Mitochondrial transfer between
> cells via Cx43 · Quiescence entry/exit of the resting cell · Reduced glycolysis as the resting-cell
> state · Lipid metabolism control in chondrocytes · Physeal bar as "local fusion" — **and it is
> nerve-driven** · α-parvin / focal-adhesion control of column formation · Ferritinophagy · Capillary
> end morphology invading the plate

And from mechanics, all ZERO: *temperature-dependent solute transport into growth-plate cartilage*
(the mechanism for **local limb warming**, which is one of only three items on R436's own
positive-length-endpoint-in-a-normal-animal list available to a person today) · *supraphysiological
distraction rate + drug rescue* (the 37.1 days/cm limiter) · *primary cilium transduces HYDROSTATIC
loading of Ihh*.

This round takes the first two, because they are the same axis.

---

## 3. The axis is not thinly covered here. It is absent.

`grep -ril` over `atlas/nodes`, `atlas/gaps/gaps.yaml`, `atlas/edges`, `docs`:

| term | files | term | files |
|---|---:|---|---:|
| **selenium** | **0** | **oxidative protein folding** | **0** |
| **selenoprotein** | **0** | **reactive oxygen** | **0** |
| **G6PD** | **0** | **deferoxamine / deferiprone** | **0** |
| glucose-6-phosphate dehydrogenase | 0 | **FSP1** | **0** |
| NADPH | 1 *(a cortisol enzyme node)* | Kashin-Beck | 2 *(both incidental, inside ADAM12 rounds)* |
| glutathione | 5 *(all inside the **sulfate** arm — sulfur pool, not redox)* | ferroptosis | 32 files, **0 nodes of its own, 0 gaps, 0 questions** |

Ferroptosis appears only as a side mention of one paper inside `piezo1_channel.yaml` and
`scoliosis_vertebral_growth.yaml`, and once in `search_log.yaml` where it is **explicitly set aside**:
*"The nearest existing result, chen2025a, measures ferroptosis rather than the Pi/PPi system."*
That paper is **`PMID 40714837`, Advanced Science 2025 — "PIEZO1-GPX4 Axis Mediates Mechanical
Stress-Induced Vertebral GROWTH PLATE Dysplasia via Ferroptosis Activation."** This atlas holds, in
its own bibliography, a paper putting ferroptosis in a growth plate, and has it filed under scoliosis.

---

## 4. ⭐ The bridge, and it is explicitly about bone lengthening

**`PMID 39794539` — Nature Metabolism, 2025 — "The pentose phosphate pathway controls oxidative
protein folding and prevents ferroptosis in chondrocytes."** Abstract, verbatim in part:

> **"Bone lengthening** and fracture repair depend on the anabolic properties of chondrocytes that
> function in an **avascular milieu. The limited supply of oxygen and nutrients calls into question
> how biosynthesis and redox homeostasis are guaranteed."** … Loss of **glucose-6-phosphate
> dehydrogenase** in chondrocytes does not affect proliferation … "However, the decreased NADPH
> production reduces **glutathione recycling**, resulting in decreased protection against the **ROS
> produced during oxidative protein folding**. The disturbed proteostasis activates the unfolded
> protein response and protein degradation. Moreover, the oxidative stress **induces ferroptosis**,
> which, together with altered matrix properties, results in a **chondrodysplasia phenotype**."

**This paper joins four things this atlas holds separately and has never connected:**

| the atlas already holds | this paper supplies |
|---|---|
| **R454** — a growth-plate chondrocyte **secretes at the plasma-cell ceiling** while matrix per cell stays constant across a ninefold range of growth rate | …and the **cost of secreting at that ceiling is ROS**, because collagen is disulfide-folded |
| **R461** — the Golgi/matrix module runs in ten minutes and is limited by **acceptor and donor supply**, not enzymes | …and the **reducing power** is a second supply term nobody has priced |
| **R450/R452/R448** — the plate is **avascular, transport-limited**, its interior half as diffusive as its periphery, permeability exponentially strain-dependent | …which is exactly the milieu the paper names as the problem |
| **R459** — the resting pool **drains by a route nobody has named**: human `emons2009` finds **not one TUNEL-positive cell** and EM showing **hypoxia and necrosis**; rabbit `roach2000` cannot find **a single** classically apoptotic chondrocyte in vivo; chick `erenpreisa1998` finds **dark chondrocytes at 10–35%** with nuclear features of **both apoptosis and necrosis** | …a **named, non-apoptotic, TUNEL-poor, necrosis-like, iron-and-lipid-driven regulated death** with a **skeletal length phenotype** |

R459 asked what the route is and answered *nobody has named it*. **The candidate name was sitting in
this atlas's own unscored blind spot, and the decisive paper was published in Nature Metabolism with
"bone lengthening" in its first sentence.**

## 5. ⭐⭐ What it changes: the budget becomes a ledger, and yield becomes controllable

This file's central trap, stated in `POSITIVE_LEDGER.md` and re-derived in R199, R459 and R470:
**growth-plate senescence is division-dependent, so velocity and duration draw on one pool, and every
agent that raises rate spends the reserve faster.** That is why thirty years of independent velocity
levers all converge on 2–4% of final height. R470 then measured the **yield** term — oestrogen
roughly halves the output per resting-zone cell spent, on three independent computations — and never
found a mechanism for it.

**If attrition is redox-mediated, yield has a mechanism and it is a supply term:**

> The chondrocyte's own productivity is what kills it. Secreting collagen at the plasma-cell ceiling
> generates ROS through oxidative protein folding. In an avascular compartment the ROS is paid down
> by NADPH from the pentose phosphate pathway, through glutathione, through selenoprotein GPX4. When
> the supply cannot meet the demand, the cell ferroptoses. **The output IS the attrition.**

Three consequences, and the third is the reason this round exists:

1. **It explains the shape R459 could not.** A self-renewing pool whose renewal fraction sits below
   replacement, with the deficit set by the niche — R459's own model — now has a physical deficit
   term: cells lost to a redox tax that scales with output.
2. **It predicts `nilsson2005`.** Rabbit resting-zone chondrocytes from old and young donors do the
   **same number of population doublings in culture** — the limit is *imposed by the plate*, not
   carried by the cell. In culture the redox tax is abolished: oxygen is plentiful, cystine is in the
   medium, and nothing is secreting collagen against a diffusion barrier. **A redox model predicts
   that result; a division-counter model has to explain it away.**
3. ⭐ **It is the only lever class that raises YIELD without raising RATE.** Every arm in this stack —
   CNP, FGFR3, GH, hedgehog — buys centimetres by making the plate work faster, and pays for them out
   of the same pool. **Supplying reducing power does not make the plate work faster. It makes each
   cell survive more of its own output.** That is the one direction the file's central constraint does
   not tax.

## 6. The free local query, run before any more literature (CORR-316) — and it is two results, one of which is against me

`query/human_growth_plate_expression.csv` and `.byzone.csv` — GSE288028, four human donors, the
atlas's own files. Full table in `frontier/screens/redox_axis/`.

### 6a. The receiver test PASSES, and it is not close

CORR-327's rule killed the nitrate shelf, the whole ARB shelf and sacubitril for this atlas, because
the drugged node was not in the tissue. Here it is, % of cells detected, against this file's own leads:

| gene | d1 | d2 | d3 | d4 | donors |
|---|---:|---:|---:|---:|---:|
| **GPX4** *(the brake, a selenoprotein)* | 13.8 | 34.0 | **63.5** | 44.4 | **4/4** |
| **ACSL4** *(the executioner)* | 29.1 | 26.2 | 23.5 | 23.5 | **4/4** |
| **FTH1 / FTL** *(iron store)* | 49/36 | 88/88 | 95/96 | 86/74 | **4/4** |
| **NFE2L2** *(NRF2)* | 57.3 | 49.7 | 18.2 | 29.0 | **4/4** |
| **P4HB / PDIA3 / ERO1A** *(oxidative folding + its ROS source)* | 36/43/13 | 39/52/19 | 96/89/27 | 49/54/18 | **4/4** |
| **SELENOS / SELENOP** | 19.8/15.3 | 22.5/34.9 | 69.1/21.7 | 33.4/53.0 | **4/4** |
| G6PD · PGD · TKT · GCLC · GSS · GSR | all present | | | | **4/4** |
| *FGFR3 (atlas lead)* | 23.6 | 9.7 | 91.4 | 26.6 | 4/4 |
| *NPR2 (vosoritide's receptor)* | 2.9 | 2.5 | 8.7 | 8.4 | 4/4 |
| *HHIP (atlas lead)* | 16.0 | 5.7 | 36.2 | 7.8 | 4/4 |

**GPX4 is detected in more cells than NPR2 in every donor, and more than HHIP in three of four.**
The complete axis — import, storage, reduction, synthesis, recycling, execution — is present in all
four. GPX6 is 0.00–0.01% (correctly: it is olfactory-restricted), which is a useful internal negative
and means the Kashin-Beck GPx6 result is about **articular** cartilage, not the physis.

### 6b. The zonal gradient argues AGAINST the simple version, and refines it

Zone controls behave: SFRP5 39.6 → 3.7 (resting marker, ratio 0.09), MKI67 peaks in the proliferative
zone, IHH peaks prehypertrophic (9.4×), COL10A1 rises to hypertrophic. **The labels are sound.**

The naive ferroptosis prediction is *brake down, executioner up* toward hypertrophy. **It is not
there.** GPX4 rises 35.1 → 43.2 (1.23×). ACSL4 rises 21.3 → 26.2 (1.23×). **Stated plainly: the
simple "GPX4 is switched off at the bottom of the plate" model is not supported by this atlas's own
human data, and I am not going to soften that.**

What does move is a different and more specific pair:

| gene | stem | hyper | ratio | what it is |
|---|---:|---:|---:|---|
| **STEAP3** | 2.00 | 11.59 | **5.80×** | ferrireductase — makes the **redox-active Fe²⁺** that drives Fenton chemistry |
| **SLC40A1** | 43.91 | 22.74 | **0.52×** | ferroportin — the **only** iron export route |
| ERO1A | 11.93 | 20.46 | 1.72× | ER oxidase — the ROS source of oxidative folding |
| GSR / G6PD / TKT | — | — | 2.19 / 1.87 / 1.66× | NADPH and glutathione **recycling** |

> **Reduced iron up 5.8-fold, iron export halved, ER ROS production up 1.7-fold — and the defence
> upregulated to match rather than withdrawn.** That is not a cell being permitted to die. It is a
> cell under rising oxidative load that is paying for it.

**And that reading is the more useful one, because it makes the axis SUPPLY-limited rather than
REGULATION-limited** — which is the third time this tissue has come back that way: R461 (the Golgi
module is acceptor- and donor-limited, not enzyme-limited), R448 (elongation is extensibility-limited,
not pressure-limited), and now this. **Three independent modules of the growth plate, three
supply limits.** A regulation-limited system needs an inhibitor, and R298 established this tissue has
no inhibitor shelf. **A supply-limited system needs substrate — which is CORR-344's "different
shelf," the one that produced this file's only obtainable compound.**

⚠ **Limits of this query, stated before anyone builds on it.** Percent-of-cells-detected is a
dropout-dominated statistic, not an expression level, and this matrix is **not purity-corrected** —
PTPRC runs 21–32% and HBB 15–19% *within* the zone labels, so CORR-339 governs. Most of these genes
are universal machinery, and CORR-363 says this screen is structurally blind to that class: presence
is **necessary and not sufficient**, and the informative content is the internal contrast (selenoproteins
and ER oxidases high, the lipoxygenase arm — ALOX15 0.03–0.20% — essentially absent), not the levels.
**Above all: ferroptosis is a LIPID phenotype and RNA cannot see it.** No transcript table can confirm
or refute it. What this establishes is that the receiver is present and the iron-handling gradient is
real; nothing more.

## 7. The human natural experiment, with CORR-203 applied first

**Kashin-Beck disease** — endemic osteochondropathy of selenium- and iodine-deficient regions, with
chondronecrosis, epiphyseal and physeal involvement and **short stature**. Its 2026 mechanism is this
axis, in three independent primaries resolved live:

- `PMID 42384133` (Apoptosis 2026) — **GPx6 down in KBD cartilage from children**, worst in the deep
  zone where death and matrix loss are worst; `Gpx6` knockout mice show ECM degradation and enhanced
  T-2 toxin susceptibility; knockdown suppresses **SLC7A11, SLC3A2 and GPx4**; **ferrostatin-1
  partially reverses it.**
- `PMID 42275919` (Int Immunopharmacol 2026) — **selenoprotein S deficiency** reduces cartilage
  thickness and drives terminal differentiation via **Wnt/β-catenin**, in KBD patients, low-selenium
  rats and SelS-knockout mice. *(SELENOS is 20–69% of cells in the human growth plate — §6a.)*
- `PMID 42103195` (2026) — **deferoxamine**, an approved iron chelator, rescues T-2-toxin chondrocyte
  ferroptosis via Nrf2/xCT/GPX4.

⛔ **CORR-203 governs and I am applying it, not writing around it.** KBD is a **deficiency** state.
Correcting selenium in a selenium-deficient child is **restoration, not elevation**, and says nothing
about supplying a replete plate. What KBD supplies is **direction and human relevance**: the redox
axis controls human skeletal length, in the deficiency direction, at population scale. The elevation
question is untouched — which is precisely CORR-344's point about the direction nobody runs.

## 8. What is missing, in this file's canonical form

**No ferroptosis inhibitor, no selenium load, no NADPH or glutathione support has ever been given to a
NORMAL growing animal with a bone-length endpoint, in any species.** Searched and confirmed:

- The chondrocyte-ferroptosis literature is ~9,800 records and is **essentially all osteoarthritis and
  articular cartilage.** The exceptions are `40714837` (vertebral growth plate — but the endpoint is
  *pathological ossification and scoliosis*) and `39794539` (endochondral, but a **loss**-of-function
  chondrodysplasia). **The ferroptosis field found the wrong cartilage** — the same shape as R459's
  finding that the ~100-record `chondroptosis` literature is entirely OA, alkaptonuria and disc.
- The one chronic normal-animal safety anchor: `PMID 40162524` (Adv Sci 2025) — ferrostatin-1 for
  **over six months** in mice, "does not adversely affect body weight," extends healthspan across
  species. **No skeletal measurement of any kind.** Chronic dosing is tolerated; the caliper was never
  used.

**The experiment, specified.** Wild-type growing mice, weaning to skeletal maturity, four arms:
vehicle · a ferroptosis inhibitor (liproxstatin-1 or ferrostatin-1, at the published chronic dose) ·
a selenium load · an NADPH/GSH support arm (N-acetylcysteine + glycine). Primary endpoint **femur,
tibia AND vertebral body length**; secondary, resting-zone cell number per unit width, terminal
hypertrophic cell height, and 4-HNE / MDA staining by zone. It uses the same animals, calipers and
histology as the 51 other gaps in `WHAT_THIS_ATLAS_NEEDS.md` that say *put a caliper on a mouse*, and
it is the first one where the intervention arm is a **substrate rather than an inhibitor**.

**The cheaper discriminator, needing no animal:** stain a human growth-plate section for **4-HNE**
(lipid-peroxidation adduct) and **transferrin receptor**, by zone. If the dark chondrocytes of
`roach2000` and `erenpreisa1998` are 4-HNE-positive, the sixty-year-old morphology has a mechanism.
Per R449 the tissue is being **surgically removed and discarded at epiphysiodesis**.

## 9. Honest position

⚠ Graded **D**, and the grade is the argument's weakest link, not its average.

**For:** the receiver is present in four human donors above two of this file's own lead targets · the
death morphology R459 assembled across three species matches a named regulated non-apoptotic route ·
a 2025 Nature Metabolism paper puts G6PD → NADPH → GSH → ferroptosis on **bone lengthening** with a
skeletal phenotype · a human deficiency disease sits on the axis with a stature phenotype · the
mechanism explains `nilsson2005`'s culture result, which a division-counter does not · and it is
supply-shaped, like the two other modules of this tissue that have been priced.

**Against:** the zonal gradient does **not** show the naive signature and I have said so · every
mechanistic result is loss-of-function or a deficit model, so CORR-203 applies throughout · the
lipoxygenase arm is nearly absent from the human plate · no length endpoint exists in either direction
· RNA cannot see a lipid phenotype · and this file has been wrong before by promoting a mechanism with
a coherent story and no caliper — that is failure mode #1, *charge without discharge*, and this round
has no discharge measurement.

**What it is not.** It is not a recommendation to take selenium, NAC or an iron chelator. Iron
chelation in a growing child has its own well-documented skeletal toxicity, and the direction of a
redox intervention in a **replete** plate is unmeasured in every species.

**What it is.** The first candidate mechanism for the term R470 measured and could not explain, in a
class of lever this file's central constraint does not tax — recovered from a blind spot this file
measured, mis-scored, and closed.
