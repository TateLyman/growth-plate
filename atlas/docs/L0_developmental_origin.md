# L0 — Developmental origin

**25 nodes (0 stubs) · 72 edges touching the layer · 26 gaps · 41 distinct refs · 10 quantitative rows**
Confidence: A 2 · B 10 · C 8 · D 5 · E 0. `human_evidence` direct 8 / indirect 11 / absent 6.
`translation_risk` high on 10 of 25.

**Ten quantitative rows for twenty-five nodes.** That ratio is the layer's diagnosis: L0 is
a rich qualitative embryology attached to almost no measurement, and three of its ten rows
are *null results of literature searches* rather than measurements. This layer knows what
happens and cannot say how much.

---

## 1. The settled core

**Endochondral and intramembranous ossification are distinct routes with distinct
consequences for growth, and both are grade A with direct human evidence.** The long bones,
vertebrae and cranial base grow by plate; the calvaria, most of the face and the clavicle
grow by suture. The clinically load-bearing consequence is that they stop at different times
and by different mechanisms, which is why craniofacial and limb growth dissociate in the
same patient (`endochondral_ossification`, `intramembranous_ossification`).

**The joint, not the plate, defines where an element ends.** The interzone is a three-layered
flattened-cell domain that interrupts a continuous cartilage rod; element length is measured
between interzones, so interzone position is the boundary condition on every subsequent
growth calculation (`interzone_formation`, grade B). GDF5 resolves the dose-response in both
directions in humans: receptor-interaction-site activating mutations give proximal
symphalangism (joint fails to form), inactivating ones give brachydactyly type C
(`seemann2005`, `gdf5_gene`, grade B, direct human).

**The primary ossification centre is the event that makes two growth plates out of one rod.**
Vascular invasion of the hypertrophic core creates the chondro-osseous junction that remains
the plate's lower boundary for the rest of life (`vascular_invasion_poc`, `maes2010`).

**The secondary ossification centre is mechanically protective, and not by stiffening.**
`xie2020`: under 1 N vertical load, **40%** of epiphyseal chondrocytes die in a SOC-negative
P10 rat tibia (propidium iodide⁺, n = 3), while size- and stiffness-matched SOC-positive
mouse tibiae tolerate a load **one order of magnitude higher**. Crucially, epiphyseal
cartilage stiffness was **not** different between arms (8.1 vs 10.5 kPa nanoindentation,
n = 6/7, **p = 0.37**), so the protection is geometric load-shielding, not a material
property. Grade B.

**Human SOC timing is measurable and slow.** Distal femoral centre first visible on
ultrasound at **30 weeks** gestation, 100% by 35 weeks; proximal tibial at **33 weeks** and
present in only **73.7%** of fetuses at 37 weeks (`funaki2020`, n = 199). This matters
because mouse SOCs all appear inside a two-week window while human SOCs appear bone by bone
across roughly two decades — the timing structure of the two species is not the same object.

**Positional identity persists postnatally in mouse.** Hoxa11-CreERT2 marking shows
Hox11-expressing cells remain in the postnatal skeleton, and *adult* conditional deletion of
Hoxd11 on a Hoxa11 background alters bone (`pineault2015`, `pineault2019`, `song2020`,
`hoxa11_gene`, `hoxd11_gene`). Grade D — mouse, and the atlas holds it at D deliberately.

---

## 2. The live disagreements

**Does patterning set growth rate, or merely growth *identity*?** `hox_code_limb` carries
`CONTRADICTS: [rux2016]`. The atlas's interest in HOX is entirely instrumental: it is the
only candidate explanation for L1's site-specific growth rates — why the distal femur runs
faster than the proximal femur in the same individual at the same moment (`g_l1arch_010`).
But the causal chain has a hole in the middle that a literature search made explicit:
**0 studies report zone-resolved HOX expression within a growth plate, in any species,
including human** (`g_l0dev_004`, tract 5, logged). Nobody has shown HOX proteins are even
present in the chondrocytes whose rate they are said to set. `rux2016` restricts Hox function
to marrow multipotent stromal cells rather than to chondrocytes, which is a different cell
compartment doing the work.

**What dominates differential elongation — hypertrophic volume or proliferation per column?**
Contradiction c002, gap `g_l0dev_009` (tract 5). `cooper2013` (Nature) measured hypertrophic
enlargement by quantitative phase microscopy and attributed the fast/slow difference to the
duration of the third, IGF-dependent enlargement phase. `lui2018` (PLoS Biol) measured both
variables **in the same animals** and found proliferation per column dominant: at 1 week the
mouse metacarpal elongated at **49%** of the tibial rate while proliferation per column was
**46%** of tibial (n = 6, calcein double labelling and BrdU per column), with hypertrophic
cell height differing little at that age — and note the per-**cell** BrdU labelling index did
not differ between bones, so the difference is in column-level output, not cell-level cycling.
Neither group reanalysed the other. L1's rat data suggest the answer is age- and
rate-dependent rather than fixed: hypertrophy's share falls from 59% to 44% as plates slow
(`wilsman1996`). Two competent mouse studies, different ages, different bones, different
definitions of "hypertrophic size" (section height vs true volume with dry-mass correction).

**L0 contradicts L2 by construction.** `secondary_ossification_center` carries
`CONTRADICTS: [soc_formation_triggers_stemness]`. The SOC is where L2's central hypothesised
mechanism lives, and L0 declines to supply it: `xie2020` demonstrates a **mechanical**
function for the SOC with a measured effect size, and no experiment anywhere manipulates SOC
formation and reads out resting-zone stemness (0 studies, `g_l2stem_003`). The atlas keeps
the mechanical account graded B and the stemness account speculative, and does not blend them.

**Mice fuse some plates, and this layer holds the number.** `lui2018`: the mouse phalanx
fuses at **3 weeks** and the metacarpal early, while tibia and femur remain unfused at 12
weeks (the last timepoint studied). This is a direct qualification on C-L7-02's "rodents do
not fuse" and on every claim that fusion cannot be modelled in mouse — it can be, in the
autopod, in a bone whose plate is the slowest and earliest-senescing in the animal.

---

## 3. The load-bearing assumption

**That all long-bone mesenchymal condensations begin at approximately the same size, so the
10–20-fold differences in adult element length are generated entirely by differential
growth.**

This is grade X (`x002`). It is what licenses the atlas — and the field — to treat skeletal
proportion as a growth-plate phenomenon and to hand the whole question to L1. If
condensations differ in founding cell number, then some fraction of adult proportion is set
before a growth plate exists, and every L1 site-specific rate comparison is measuring the
residual of an unmeasured initial condition.

Its evidence: **none traceable.** `lui2018` states it in its introduction and cites two Hall
& Miyake *review* articles (1992, 2000). A targeted Europe PMC search (363 hits, 20 screened)
returned **no primary measurement of condensation cell number, volume or density compared
across elements of different final length, in any species** (`g_l0dev_003`, logged). Ten rows
in this layer, and the assumption on which the layer's relevance depends is one of the three
that is a search null.

The related result that *is* real cuts the other way: `mesenchymal_condensation` (grade D)
records that the condensation is already spatially partitioned at formation. Partitioned is
not the same as equally sized, and no one has weighed them.

---

## 4. What would change everything

A cell-count comparison of femoral and phalangeal condensations at the same embryonic stage —
light-sheet imaging of a SOX9 reporter with automated nuclear counting, femur vs metacarpal
vs distal phalanx, three stages. It is a two-month experiment on existing mouse lines and
nobody has done it.

If founding cell number scales with final length, `x002` falls, L1's site-specific rate
comparison acquires a covariate it has never adjusted for, `g_l0l9_008` (does condensation
progenitor number set total proliferative capacity?) becomes answerable, and the finite-budget
models in L2/L7 gain their missing initial condition. If founding number is genuinely
constant across a 10–20-fold length range, then the assumption is finally evidence rather than
citation, and the layer's licence to hand everything to L1 is earned rather than assumed.

Second, smaller but sharper: RNAscope for HOXA11/HOXA13/HOXD13 on zone-annotated growth plate
sections from three sites in one animal. A negative result retires the HOX→rate hypothesis
that four L0 nodes exist to carry.

---

## 5. Numbers

| Parameter | Value | Unit | Species | Spread / n | Source | Flag |
|---|---|---|---|---|---|---|
| Metacarpal elongation rate vs tibia | 49 | % of tibial rate | mouse, 1 week | n = 6/group, calcein | `lui2018` | single source |
| Metacarpal proliferation per column vs tibia | 46 | % of tibial | mouse, 1 week | n = 6; per-**cell** BrdU index unchanged | `lui2018` | single source |
| Mouse phalanx vs tibia fusion age | 3 vs >12 | weeks | mouse | 12 weeks was the last timepoint | `lui2018` | single source |
| Chondrocyte death under 1 N load, SOC-negative | 40 | % PI⁺ epiphyseal chondrocytes | rat, P10 | n = 3; SOC⁺ tolerated 10× the load | `xie2020` | single source |
| Epiphyseal cartilage stiffness, vehicle vs axitinib | 8.1 vs 10.5 | kPa (nanoindentation) | mouse | n = 6/7, **p = 0.37 (n.s.)** | `xie2020` | negative result |
| Distal femoral SOC first visible | 30 (100% by 35) | weeks gestation | **human** | n = 199 | `funaki2020` | single source |
| Proximal tibial SOC first visible | 33 (73.7% at 37 wk) | weeks gestation | **human** | n = 199 | `funaki2020` | single source |
| Zone-resolved HOX expression in a growth plate | **0** | studies | any, incl. human | full screen | — | null (`g_l0dev_004`) |
| Condensation size compared across elements | **0** | studies | any | 363 hits, 20 screened | — | **grade X `x002`** |
| SOC-manipulation experiments with stemness readout | **0** | studies | any | full screen | — | null (`g_l2stem_003`) |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l0dev_003`** (quantitative_gap, tract 4) — do condensations of very different final
   length differ in founding cell number? Light-sheet + automated nuclear counting on a SOX9
   reporter, femur vs metacarpal vs distal phalanx, matched stages. Equal counts → `x002`
   confirmed, all proportion is plate-generated. Scaling counts → part of adult proportion
   predates the plate.
2. **`g_l0dev_009`** (contradiction, tract 5) — hypertrophic volume or proliferation per
   column? Measure *both*, by quantitative phase microscopy **and** per-column BrdU, in the
   same animals, at three ages spanning the fast→slow transition. `cooper2013` predicts
   phase-3 duration tracks rate at all ages; `lui2018` predicts proliferation per column
   dominates at 1 week and hypertrophy takes over later.
3. **`g_l0dev_004`** (search_established, tract 5) — are HOX genes expressed in growth plate
   chondrocytes at all, and in which zone? RNAscope with zonal annotation, three sites, one
   animal, plus human physeal blocks. Negative retires four nodes' rationale.
4. **`g_l0dev_002`** (search_established, tract 3) — is there any developmental antecedent
   distinguishing species that fuse from species that do not? Comparative SOC-timing and
   epiphyseal-architecture series across mouse, rat, rabbit, pig and human. This is the only
   route to a non-human model of fusion and it has never been searched systematically before.
5. **`g_l0dev_005`** (species_gap, tract 2) — human SOCs appear across two decades, mouse SOCs
   across two weeks. Does resting-zone stemness therefore arrive bone by bone in humans?
   Discriminator: zone-resolved profiling of human physes from bones with SOC present vs
   absent at matched chronological age (e.g. distal femur vs proximal humerus in infancy).
6. **`g_l0dev_012`** (quantitative_gap, tract 3) — in the *same* human individuals, when does
   calvarial growth stop relative to long-bone growth? Serial CT in a longitudinal cohort. The
   dissociation is assumed clinically and never quantified.

---

## 7. Human-translation status

**8 of 25 nodes (32%) carry direct human evidence; 6 have none; 10 of 25 carry high
translation risk.** But the raw fraction flatters the layer, because of the eight
human-evidenced nodes, six are human **genetics** — TBX5/Holt-Oram (`basson1997`),
GDF5/symphalangism-brachydactyly (`seemann2005`), HOXA13/hand-foot-genital (`mortlock1997`),
HOXD13/synpolydactyly (`muragaki1996`), the ZRS/preaxial polydactyly enhancer
(`lettice2003`). Human genetics establishes that a gene is **required** for a structure in
humans. It says nothing about rate, amount, or mechanism, which is what this atlas needs from
L0.

Of the ten quantitative rows, exactly **two are human** and both are the same ultrasound
cohort (`funaki2020`). The mechanistic measurements — condensation partitioning, SOC
mechanical protection, differential elongation, postnatal HOX function — are mouse, rat and
chick without exception. `to2024`'s human embryonic multi-omic atlas is the layer's most
cited human resource (5 nodes) and it is descriptive: it maps cell states, not rates.

The honest statement: **L0 supplies the atlas with boundary conditions it cannot measure.**
It tells you that element identity, joint position and ossification-centre timing are set
before the growth plate runs, and it cannot tell you by how much any of them constrains what
the plate then does. The one assumption that would let L0 be safely ignored — equal starting
condensations — is the one thing in the layer that no one has ever measured.
