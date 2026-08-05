# L1 — Growth plate architecture

**48 nodes (0 stubs) · 595 edges touching the layer · 28 gaps · 62 distinct refs · 218 quantitative rows**
Confidence: A 4 · B 11 · C 28 · D 4 · E 1. `human_evidence` direct 20 / indirect 12 / absent 16.
`translation_risk` high on 25 of 48.

---

## 1. The settled core

**The growth plate is a steady-state conveyor.** Cell production at the top equals cell
loss at the chondro-osseous junction; `wilsman1996` calculated both independently in four
rat plates and they agree. In rat proximal tibia the plate makes 16,400 chondrocytes/day
and loses 8 cells per column per day, one every three hours (`hunziker1987`,
`chondro_osseous_junction`, `clonal_column`). Grade C — rat, replicated across two
laboratories and two methods, no human measurement.

**Elongation is not mostly proliferation.** The partition in 28-day rat proximal tibia is
**9% cell division / 32% matrix synthesis / 59% hypertrophic enlargement** (`wilsman1996`,
node `elongation_budget`). This is the single most useful number in the layer and it is
routinely misquoted. Its more interesting half is the *shift*: in the slowest of the four
plates, proximal radius, hypertrophy falls to **44%** and matrix synthesis rises to **49%**,
so matrix becomes the majority contributor in a slow plate. Growth plates do not scale one
mechanism up and down; they change which mechanism dominates. Grade C, rat, single study.

**The hypertrophic phase has fixed duration and variable amplitude.** `hunziker1989`:
2 days, constant across 21-, 35- and 80-day rats spanning a wide range of elongation rates,
while final cell height rises. `cooper2013` resolves the amplitude into three phases in
mouse — true hypertrophy 600→2,000 fl at constant dry-mass density 0.183 pg/fl, then
swelling 2,000→8,000 fl with dry mass diluted ~60% to 0.07 pg/fl, then a third
IGF-dependent phase to 14,000 fl. Slow plates truncate phase 3 (mouse proximal radius,
5,000 fl); the jerboa metatarsal extends it (23,000 fl). Grade C.

**Human plate shares of bone length are grade A and are the only human numbers here that
are absolute.** Distal femur 70% of femoral length, rising 55–60% at age 7 to 90% at 14–16;
proximal tibia 57%; proximal humerus 80%; distal radius 80%; distal ulna 85%
(`pritchett1988`, `pritchett1991`, `pritchett1992`; n = 200–244, serial teleroentgenograms).
Nodes `distal_femur_plate`, `proximal_humerus_plate`, `distal_radius_plate`.

**Site-specific growth is set by eight variables, not one.** `wilsman1996` decomposes
differential growth into eight chondrocytic parameters, seven of which vary between plates
in the same animal at the same moment. Proliferative cycle time alone spans 2.5-fold within
one 28-day rat — 30.9 h proximal tibia, 34.0 h distal radius, 48.7 h distal tibia, 76.3 h
proximal radius (`wilsman1996a`) — against a 50–400 µm/24 h elongation range. Any
single-parameter account of why one plate outgrows another is wrong by construction.

---

## 2. The live disagreements

**Columns may not be the elongation machine.** This is the layer's most destabilising open
question, logged as C-L1-01 and gap `g_l1arch_004`. A century of histology plus the mutant
literature (`aszodi2003` Itgb1, `romereim2014`, `greer2024` N-cadherin/β1, `yuan2023`
α-parvin) treats columnar stacking as the structure that channels hypertrophic volume into
axial displacement. `rubin2024`'s 3D Confetti clonal analysis says columns are *rare exactly
when elongation is fastest*: only **17.6%** (distal femur, n = 1,044 doublets) and **19.4%**
(proximal tibia, n = 805) of E18.5 clonal doublets have completed the 60–90° division-plane
rotation, and most embryonic clones are ellipsoids oriented *orthogonal* to the growth axis.
Even at P40, inside structures scored as columns, only 36.4–39.5% of divisions completed
rotation and 8.2–9.6% were near-perfect. What settles it: a perturbation that removes
stacking without touching cell volume, matrix or proliferation. Every published "column
disorganisation" mutant perturbs at least one of the three, so shortening has never been
attributed to loss of stacking alone. Until that experiment exists, every chondrodysplasia
described as a column disorder is an inference from correlation.

**Hypertrophic volume as a growth surrogate fails outside mammals.** `breur1991` gives
r = 0.98 (rat) and r = 0.83 (pig) between final hypertrophic volume and elongation rate —
but the regression *slopes* already differ between rat and pig, so this is not a mammalian
constant, and `barreto1994` failed to reproduce the relationship in duckling and chick
weight-bearing plates with direct fluorochrome measurement. Three L1 nodes carry
`CONTRADICTS: [barreto1994]`. Consequence: hypertrophic cell size is used as a preclinical
surrogate endpoint for elongation, and its validity is species-contingent with no human
anchor at all (`g_l1arch_009`).

**Saltation versus continuity has never been tested in one preparation.** `lampl1992`:
0.5–2.5 cm bursts, 2–63 day stases, 90–95% of days growth-free in 31 infants — surface
anthropometry whose technical error exceeds the mean daily increment. `klein1994`: rabbit
proximal tibia measured with implanted markers at ~15-fold better precision gives a single
Gaussian velocity distribution, and recomputes the saltation model as requiring >350 cm/year
instantaneous velocity. `hermanussen1998` offers a third position (chaotic mini-spurts, no
true stasis). The two camps have never measured the same tissue. One discontinuity is not in
dispute: `noonan2004`'s implanted microtransducers show ≥90% of lamb tibial elongation occurs
during recumbency, so elongation is load-gated on a diurnal cycle whatever the multi-day
statistics say — which by itself makes any human measurement interval shorter than 24 h
uninterpretable.

**Two canonical facts are grade X — repeated everywhere, traceable nowhere.** (i) The
oxygen gradient. `brighton1971` is the universal citation for physeal hypoxia and has no
indexed abstract and no reachable full text; **no pO₂ value in mmHg for any zone in any
species could be retrieved**, and a targeted search for human physeal oxygen returned four
records, none measuring it (`g_l1arch_007`, x-L1-01). The claim survives only on the mouse
genetics (`schipani2001`) and on chondrocyte haemoglobin bodies with P50 left-shifted to
27.6–27.9 mmHg vs 58.2 mmHg for red cells (`zhang2023`). (ii) The septoclast.
`septoclast*` returns 54 records, all screened; **every primary observation is mouse, rat or
calf** (x-L1-02, `g_l1arch_003`). A cell type with an assigned lineage (`sivaraj2022`:
mesenchymal, PDGFRα-reporter-positive, more abundant than osteoclasts at the interface,
n = 6) and a druggable dependency has been established without one human observation.

---

## 3. The load-bearing assumption

**That the growth plate is in kinetic steady state, so unmeasurable rates can be inferred
from static histology plus a bulk elongation rate.**

Nothing else in this layer carries as much. It licenses `hunziker1987`'s 8 cells/column/day
(inferred from column height and elongation), `wilsman1996`'s entire eight-variable
decomposition and the 9/32/59 budget, `hunziker1989`'s invariant 2-day hypertrophic phase,
and — decisively — the only human kinetic number the atlas holds. `kember1976` derives a
human distal-femoral proliferative cycle time of **~20 days** from 24 cells per column and
1.4 cm/year. It was never measured. Kember states the rodent comparison as ~2 days;
`wilsman1996a` measured 30.9 h in rat proximal tibia. That is a **~15-fold** human/rodent
divergence resting entirely on an assumption of steady state and a 100% growth fraction.

Its evidence is one internal consistency check: in `wilsman1996`, calculated cell production
and calculated cell loss came out approximately equal in all four rat plates. That is real
support, and it is also the only support. `thurston1985` is the nearest human probe and it
is a warning — 2 of 4 human specimens yielded *no* labelled cells after in vitro tritiated
thymidine, which the authors themselves could not distinguish from technical failure.

---

## 4. What would change everything

A direct measurement of human proliferative-zone cycle time. Not another inference — a
clock. If ¹⁴C bomb-pulse dating or somatic-mutation phylogeny of microdissected human
physeal columns returned a cycle time near 1–3 days, then Kember's 20 days is an artefact of
a broken growth-fraction assumption, the human plate is a fast rodent plate operating with a
much larger latent progenitor pool, and the arithmetic of finite division budgets that L2
and L7 inherit from it changes by an order of magnitude. If it returned ~20 days, human
chondrocyte kinetics are genuinely a different regime from every animal in this layer and
essentially all 25 high-translation-risk nodes need re-grading downward rather than upward.

Second: any experiment that dissociates columnar stacking from hypertrophic volume. If
elongation survives loss of stacking, `chondrocyte_column_formation` stops being a mechanism
node and becomes a descriptive one, and the interpretive frame of L11's dysplasia histology
goes with it.

---

## 5. Numbers

| Parameter | Value | Unit | Species / site | Spread | Source | Flag |
|---|---|---|---|---|---|---|
| Elongation partition | 9 / 32 / 59 | % division/matrix/hypertrophy | rat, prox. tibia, 28 d | → 44% hypertrophy, 49% matrix in prox. radius | `wilsman1996` | single source |
| PZ cell cycle time | 30.9 / 34.0 / 48.7 / 76.3 | h | rat, 4 plates, 28 d | 2.5-fold within one animal, p<0.05 | `wilsman1996a` | single source |
| PZ cell cycle time | ~20 | days | **human**, distal femur | none — point estimate | `kember1976` | **derived, not measured** |
| Chondrocyte output | 16,400 vs 3,700 | cells/day/plate | rat, prox. tibia vs prox. radius | 4.4-fold | `wilsman1996` | single source |
| Cell loss rate | 8 (1 per 3 h) | cells/column/day | rat, prox. tibia | — | `hunziker1987` | single source |
| Hypertrophic phase duration | 2 | days | rat, prox. tibia | constant at 21/35/80 d | `hunziker1989` | single source |
| Hypertrophic column turnover | 24 (12 enlarging + 12 terminal) | h | mouse | — | `cooper2013` | single source |
| Final hypertrophic volume | 600 → 14,000 | fl | mouse, prox. tibia | 5,000 (slow plate) – 23,000 (jerboa) | `cooper2013` | single source |
| Dry mass density fall | 0.183 → 0.07 | pg/fl | mouse | ~60% dilution | `cooper2013` | single source |
| Volume–rate correlation | 0.98 / 0.83 | Pearson r | rat / pig | slopes differ; fails in birds | `breur1991`/`barreto1994` | contradicted |
| Completed division rotations | 17.6–19.4 (E18.5) / 36.4–39.5 (P40) | % | mouse, femur+tibia | n = 805–1,044 doublets; 512–737 columns | `rubin2024` | single source |
| Distal femur share of femur | 70 (55–90 by age) | % | **human** | n = 244 | `pritchett1992` | — |
| Prox. humerus share of humerus | 80 (<75 → 90) | % | **human** | n = 200 | `pritchett1991` | — |
| Saltation amplitude / stasis | 0.5–2.5 / 2–63 | cm per event / days | **human** infants | 90–95% of days growth-free | `lampl1992` | contradicted |
| Elongation during recumbency | ≥90 | % | ovine, implanted transducer | — | `noonan2004` | single source |
| Chondrocyte Hb body P50 | 27.58–27.85 (vs 58.2 RBC) | mmHg | mouse | two reported values | `zhang2023` | single source |
| Zonal pO₂, human | **not measured** | mmHg | human | — | — | grade X (x-L1-01) |
| Human septoclast observations | **0** | studies | human | 54 records screened | — | grade X (x-L1-02) |
| Per-plate vertebral growth rate | **not reported** | mm/year | human, >130 plates | — | `dimeglio2020` | null |
| Ca:organic peak at calcified front | p < 0.0001 | — | **human** polydactyly, ToF-SIMS | n = 3 | `zoehrer2025` | single source |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l1arch_001`** (quantitative_gap, tract 3) — the human elongation budget. Discriminator:
   fluorochrome double-labelling plus unbiased stereology on surgical physeal specimens
   (epiphysiodesis, limb reconstruction). Under transfer from rat, hypertrophy ≈ 59%; under a
   slow-plate regime, matrix synthesis should exceed it, as it does in rat proximal radius (49%).
2. **`g_l1arch_002` / `g_l1arch_012`** (species_gap + search_established) — is the 20-day human
   cycle time real? Discriminator: somatic-mutation phylogeny of laser-microdissected human
   columns; branch lengths give divisions since the last common ancestor without any labelling.
   A ~20-day cycle predicts ≲20 divisions per column lifetime; a rodent-like cycle predicts hundreds.
3. **`g_l1arch_004`** (contradiction) — are columns required? Discriminator: acute, reversible
   disruption of division-plane rotation (β1-integrin degron, N-cadherin blockade) with
   simultaneous readout of elongation rate *and* terminal hypertrophic volume in the same plate.
   If elongation falls while volume is preserved, columns are load-bearing; if both fall, the
   existing mutants remain uninterpretable.
4. **`g_l1arch_007`** (quantitative_gap) — human zonal pO₂. Discriminator: needle
   phosphorescence-quenching oximetry at the time of epiphysiodesis, three depths. The claim is
   currently supported by genetics alone.
5. **`g_l1arch_003`** (search_established, tract 4) — does the septoclast exist in humans?
   Discriminator: FABP5/cathepsin B/PDGFRα immunostaining on the existing human chondro-osseous
   junction blocks. `walzer2014` had the tissue and stained CD34/CD31/RANK instead.
6. **`g_l1arch_011`** (quantitative_gap) — per-plate vertebral contribution. >130 human vertebral
   plates exist and not one has a published individual growth rate; only segment-level rates.
   Discriminator: serial CT/MRI vertebral body height across a growth interval, per level.

---

## 7. Human-translation status

**Every kinetic and volumetric number in this layer is animal.** The cell cycle, the
elongation budget, the hypertrophic trajectory, the rotation statistics, the removal rate,
the oxygen physiology and the septoclast are rat, mouse, pig, rabbit, sheep, chick and
jerboa. 25 of 48 nodes carry `translation_risk: high`; 16 have `human_evidence: absent`.

The 20 nodes with direct human evidence are of exactly two kinds. **(a) Radiographic
share-of-growth** — `pritchett1988/1991/1992`, n = 200–244, grade A, and the anchor for the
whole clinical use of this layer. **(b) Human histomorphometry that the atlas could only
retrieve as directions, not magnitudes** — `byers2000` (rib, birth to adolescence: zone
heights decreasing, proliferative septal number decreasing, hypertrophic septal number
unchanged) is abstract-only, so eight L1 quantitative rows sourced to it carry the direction
of change and no absolute value. `white2008` is n = 1 adolescent distal tibia. `kember1976`
supplies the only human cell counts (24 cells per proliferative column) and its cycle time is
a derivation, not a measurement.

The honest statement: **L1 knows the human growth plate's output very well and its internal
mechanics not at all.** The share-of-growth numbers describe what plates deliver; every claim
about *how* they deliver it is transferred from rodents whose proliferative chondrocytes may
cycle fifteen times faster.
