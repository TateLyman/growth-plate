# L5 — Matrix and mineralization

**41 nodes (0 stubs) · 280 edges touching the layer · 32 gaps · ~90 refs**
Confidence: A 4 · B 19 · C 14 · D 3 · E 1. `human_evidence` direct 18 / indirect 16 / absent 7.
`translation_risk` moderate 17 / low 11 / high 13.

This layer produced two of the atlas's three mechanism corrections (CORR-001 ANKH, CORR-002
collagen X) and two of its ten grade-X claims. It is also the layer where the atlas most
often found that a number everyone quotes was measured in a different tissue.

---

## 1. The settled core

**Mineralization is controlled by opposing enzymes whose human mutations cancel.** TNAP
(*ALPL*) destroys PPi; ENPP1 makes it; loss of TNAP gives hypophosphatasia with
undermineralization, loss of ENPP1 gives GACI with ectopic mineralization, and the double
mutants correct each other. `tnap_alpl`, `enpp1_enzyme`, `inorganic_pyrophosphate` are all
grade A with direct human evidence. **`Enpp1`⁻/⁻ mouse bone contains <2.5% of wild-type PPi**
(`szeri2022`) — a bound, not an estimate.

**Mineral initiates inside matrix vesicles and propagates outside them, and the TNAP null
separates the two steps.** In 10-day *Alpl*⁻/⁻ mouse tibia, **intravesicular crystals are
present and normal**; the failure is **extravesicular** (`anderson2004`, high-resolution TEM).
NPP1, but not ANK, localises to matrix vesicles (`harmey2004`).

**Aggrecan sets the swelling pressure and the numbers are real, if not physeal.** Fixed charge
density −0.19 to −0.35 mol/L in calf epiphyseal cartilage by sodium NMR (n = 10, NMR:ICP
visibility ratio 1.02, SD 0.04, `lesperance1992`). Measured osmotic swelling pressure is
**~0.33× the ideal Donnan prediction** (18 immature bovine, 6 mature human specimens,
`zimmerman2021`) — i.e. the textbook Donnan calculation overestimates the real pressure
threefold. Aggregate modulus swings 0.420→1.266 MPa (bovine) and 0.499→1.597 MPa (human)
between 2 M and 0.001 M NaCl, so any stiffness figure quoted without its ionic strength is
uninterpretable to within a factor of three.

**Collagen X acts one zone upstream of where it is made.** CORR-002. In the `Col10a1` null the
**proliferative** zone is more compressed than the hypertrophic — "opposite that seen in the Tg
mice", in the primary's own words — with ~14% overall plate-width reduction at day 21,
**~10.8% perinatal and ~14% total lethality**, marrow aplasia and lymphoid organs at ~80% of
control (`gress2000`). Human `COL10A1`⁻/⁻ iPSC chondrocytes are null for differentiation
markers but have a **significantly larger** transplanted bone-area fraction in one of two
backgrounds, with the transcriptome shifting from proliferating-phase toward calcification-phase
genes (`kamakura2023`). Both systems point the same way: losing collagen X does not block
hypertrophy, it shifts the proliferation/ossification balance toward ossification. A collagen
expressed **exclusively** in hypertrophic chondrocytes producing its clearest effect in the
proliferative zone is a non-cell-autonomous action through an unnamed intermediate, and it is
the most interesting thing in this layer.

---

## 2. The live disagreements

**CORR-001: ANKH exports ATP, not pyrophosphate.** The canonical model — ANK as a
plasma-membrane PPi transporter — was assigned in cells where the alternative was present and
never removed. In HEK293 engineered to lack ENPP1 entirely, ANKH gives **robust ATP release
with 0 detectable increase in extracellular PPi** (`szeri2022`). ANKH is therefore *upstream*
of ENPP1, supplying ~25% of plasma PPi as NTP substrate (ABCC6 supplies 60–70%). The
structural signature that the correction landed: **no `ankh_transporter → inorganic_pyrophosphate`
edge exists in the graph**, though under the old model it would have been the central edge of
the cluster. One quantitative row ("~75% of mouse bone PPi attributable to Ank") now carries
`superseded_model: true`, propagated into `parameters.csv` as a machine-readable column.
`wang2005` is classified **interpretation_superseded**, not discarded: blocking Ank really does
change chondrocyte PPi handling — the study simply had no way to distinguish direct PPi export
from ATP export plus endogenous ENPP1 on the same cells (`g_l5matrix_006`).

**Zonal stiffness disagrees on magnitude by three orders of magnitude and on direction by
species.** `zonal_stiffness_gradient` carries **four** `contradicts` refs and is held at grade
D. `sergerie2009` (newborn porcine distal ulna, unconfined compression, transversely isotropic
biphasic fit): PZ and HZ are **half** as stiff as reserve axially, a **third** transversely, and
three times as permeable radially — reserve is stiffest. `eckstein2022` (9-week rabbit proximal
tibia, microindentation, n = 15 hydrated): Hertz reduced modulus **380–690 kPa peaking in the
upper hypertrophic zone**. `radhakrishnan2004` (rabbit cranial base, AFM): monotonic rise
0.57 MPa (reserve, SD 0.05) → 1.41 MPa (mineralizing, SD 0.19), with significant anisotropy
(0.77 MPa longitudinally in the reserve zone). `xie2025` (human, sharp 9-nm-tip AFM on 150 µm
hydrated cryosections, 10 donors): **HZ 416.20 MPa (SD 107.18) > RZ 130.70 MPa (SD 36.56)**.
That is **380 kPa to 416 MPa** — a factor of ~1,100 — which by itself proves the four methods
are not measuring the same physical quantity. The confound is fourfold and simultaneous:
species, site, age and length scale. Two gaps split the question: `g_l5matrix_008` (direction)
and `g_l6l5_005`/`g_l5matrix_001` (the missing hydrated tissue-scale human number). Everything
downstream — every finite-element model of physeal loading, guided growth and Salter-Harris
fracture propagation — currently picks one of these four and does not say why.

**Nobody knows how aggrecan is cleared from the hypertrophic zone.** `g_l5matrix_007` and
`g_l6l5_006`. Mineral cannot form through an intact proteoglycan gel, so aggrecan must be
removed ahead of the front; the porcine microprobe shows extracellular sulphur falling
**3.5% → 0.3% of dry mass** across the front (`althoff1982`, with the authors' own caution that
dry-mass normalisation exaggerates the fall). But **neither MMP cleavage at N341–F342 nor
aggrecanase cleavage accounts for it in growth plate**, and `adamts4`/`adamts5` carry reciprocal
`CONTRADICTS` — `Adamts5` nulls are protected in the murine OA model while `Adamts4` nulls are
not (`glasson2005`), which is an articular result being asked to cover a physeal process. **No
protease has been identified for the step.**

**The 3.4-year aggrecan half-life is an articular figure applied to a tissue that turns over in
days.** `maroudas1998` measured aspartate racemization in *adult human articular* cartilage:
large-monomer turnover constant 0.206/year (half-life 3.4 years), free G1 half-life 25 years.
The growth plate's own hypertrophic zone turns over completely in ~24 h (`cooper2013`, L1). The
only physeal turnover data are bovine explant rank orders — synthesis and breakdown RZ/PZ >
upper HZ > lower HZ, ~90% of newly synthesised proteoglycan aggregate-competent
(`shapses1994`). `g_l6l5_007` exists specifically to stop the articular figure being quoted as
physeal.

**Two grade-X claims underpin the layer's teaching.** x-L5-01: the "collagens II:IX:XI at
8:1:1" ratio. `mendler1989` is an immunoelectron-microscopy paper whose abstract establishes
the three collagens are in the *same fibril* and says nothing about a ratio; the nearest
traceable source is a review giving ≤80% II / ≥10% IX / ≥10% XI **by mass** for *bovine* growth
cartilage, and `blaschke2000`'s independent eight-fold II:XI **molar** ceiling for
fibril-diameter control is routinely conflated with it. **No stoichiometry of human physeal
collagen exists at all** (`g_l5matrix_003`). x-L5-02: see §3.

---

## 3. The load-bearing assumption

**That the Pi/PPi ratio controls where the growth plate mineralizes.**

This is the organising principle of the entire mineralization literature — the framing
statement of the field's reviews, the explanation offered for hypophosphatasia, GACI,
craniometaphyseal dysplasia and the action of asfotase alfa, and the interpretive frame for the
*ALPL*, *ENPP1*, *ANKH* and *PHOSPHO1* genetics in both mouse and human. In this atlas it is
load-bearing for `pi_ppi_ratio`, `inorganic_pyrophosphate`, `tnap_alpl`, `enpp1_enzyme`,
`ankh_transporter`, `mineralization_front`, `matrix_vesicle`, `hydroxyapatite_nucleation`, and
for the L11 hypophosphatasia and GACI nodes downstream of them.

**The ratio has never been measured in a growth plate.** Human plasma PPi is well measured —
3.50 µmol/L, SE 0.11, 99% range 1.19–5.65, n = 73 (`russell1971`) — and porcine growth plate
elemental Ca and P are mapped at ~50 µm resolution (`althoff1982`), but the microprobe measures
**total phosphorus, not Pi/PPi speciation**, and plasma is the wrong compartment. A Europe PMC
search for zone-resolved PPi or Pi concentration in growth plate tissue returned **13 records,
all matrix-vesicle, cell-culture, plasma or biomimetic** (`g_l5matrix_002`, logged 2026-08-05).
The atlas's own circulating Pi:PPi ratio row (~300–600 mol:mol) is flagged `value_unverified`
because its numerator is a reference range, not a measurement in the same subjects.

The principle is strongly supported by **convergent genetics** — opposing mutations cancel — and
that support is real. But the layer also holds a direct dissociation of the plasma proxy from
the tissue phenotype: TNAP transgenic overexpression **normalised plasma PPi in `Phospho1`⁻/⁻
mice and produced 0 correction of the bone phenotype** (`yadav2011`). Plasma PPi and skeletal
mineralization came apart in the same animals. If the controlling quantity is a local ratio
rather than a systemic one, the genetics still stand and every quantitative inference drawn
from plasma PPi does not.

---

## 4. What would change everything

A zone-resolved, in situ measurement of Pi and PPi in growth plate extracellular fluid.
Cryo-sectioned physis with a PPi-selective fluorescent or enzymatic probe read against a
matched Pi map, calibrated on `Alpl`⁻/⁻ and `Enpp1`⁻/⁻ tissue as positive and negative controls.

If the ratio falls monotonically toward the mineralization front, the organising principle is
converted from convergent-genetics inference into a measured gradient, `g_l5matrix_002` closes,
and every mineralization model gains a boundary condition it currently guesses. If the ratio is
**flat** across zones — which the porcine microprobe's finding that the Ca×P ion product exceeds
the mineralization threshold *in every zone* (`althoff1982`) makes entirely possible — then
something other than the Pi/PPi ratio localises the front, the candidate list shifts to
collagen X's non-cell-autonomous organising role (CORR-002), aggrecan clearance
(`g_l5matrix_007`) and matrix-vesicle positioning, and a large fraction of this layer's
mechanistic narrative is redirected.

The second-order rewrite would come from the human tissue-scale stiffness measurement
(`g_l6l5_005`): a hydrated, weight-bearing, tissue-scale human modulus profile would collapse
the four-way stiffness contradiction to at most a two-way one and give L6's finite-element
models their first non-borrowed material property.

---

## 5. Numbers

| Parameter | Value | Unit | Species / tissue | Spread / n | Source | Flag |
|---|---|---|---|---|---|---|
| Zonal modulus, sharp-tip AFM | RZ **130.70** → HZ **416.20** | MPa | **human** phalangeal physis | SD 36.56 / 107.18; 10 donors | `xie2025` | direction: HZ stiffest |
| Zonal modulus, microindentation | 380–690 (peak upper HZ) | kPa | rabbit prox. tibia | n = 15; neighbouring zones p<0.05 | `eckstein2022` | **1,000× lower than `xie2025`** |
| Zonal modulus, AFM | 0.57 → 1.41 (transverse); RZ 0.77 longitudinal | MPa | rabbit cranial base | SD 0.05 / 0.19 / 0.12 | `radhakrishnan2004` | anisotropic |
| Zonal stiffness, biphasic compression | PZ,HZ = **0.5×** RZ axial, 0.33× transverse; 3× permeability | ratio | newborn porcine ulna | — | `sergerie2009` | **direction inverted** |
| Modulus step, cartilage → bone | 130.70→11,920 (epiphyseal) / 416.20→3,220 (metaphyseal) | MPa | **human** | SD 6.60 / 1.53 GPa | `xie2025` | single source |
| Fixed charge density | −0.19 to −0.35 | mol/L | bovine epiphyseal | n = 10; articular −0.28, SD 0.03 | `lesperance1992` | not physeal-zonal |
| Osmotic swelling pressure vs ideal Donnan | **0.33** | fold | 18 bovine + 6 **human** | — | `zimmerman2021` | single source |
| Aggregate modulus, 2 M → 0.001 M NaCl | 0.499 → 1.597 (human); 0.420 → 1.266 (bovine) | MPa | human / bovine articular | SD 0.208/0.455; 0.109/0.438 | `zimmerman2021` | ionic-strength dependent |
| Plasma PPi, healthy adults | 3.50 | µmol/L | **human** | SE 0.11; 99% range 1.19–5.65, n = 73 | `russell1971` | — |
| Bone PPi, `Enpp1`⁻/⁻ | **<2.5** | % of WT | mouse | upper bound | `szeri2022` | — |
| Extracellular PPi rise from ANKH, ENPP1-null cells | **0** | detectable | in vitro human cell | ATP release robust in same cells | `szeri2022` | **CORR-001** |
| Plasma PPi from ANKH / ABCC6 | ~25 / 60–70 | % | mouse | by difference | `szeri2022` | — |
| Bone PPi attributable to Ank (old estimate) | ~75 | % | mouse | — | `szeri2022` | **`superseded_model: true`** |
| Growth plate width, `Col10a1` null | −14 | % | mouse, day 21 | PZ more compressed than HZ | `gress2000` | **CORR-002** |
| `Col10a1` null lethality | 10.8 perinatal / 14 total | % | mouse | colony-scale | `gress2000` | single source |
| Long bone length, `Col10a1` null | **0** detectable | difference | mouse | power not stated | `rosati1994` | interpretation superseded |
| Extracellular S across the front | 3.5 → 0.3 | % dry mass | porcine | authors caution normalisation | `althoff1982` | single source |
| Aggrecan half-life | **3.4 years** | — | **human ARTICULAR**, adult | k = 0.206/yr; G1 25 yr | `maroudas1998` | **wrong tissue for this layer** |
| Physeal aggrecan half-life | **never measured** | — | any | — | — | `g_l6l5_007` |
| Protease clearing HZ aggrecan | **none identified** | — | any | MMP N341-F342 and aggrecanase both insufficient | — | `g_l5matrix_007` |
| Zonal Pi/PPi in growth plate | **never measured** | µmol/L | any | 13 records, all wrong compartment | — | **grade X (x-L5-02)** |
| Human physeal collagen II:IX:XI stoichiometry | **never measured** | mol or mass | human | — | — | **grade X (x-L5-01)** |
| Plasma PPi normalisation vs bone phenotype | PPi normalised, **0** bone correction | — | mouse | `Phospho1`⁻/⁻ + TNAP transgene | `yadav2011` | dissociation |
| PHOSPHO1 IC50, esomeprazole / pantoprazole | 0.73 / 19.27 | µM | in vitro | no TNAP inhibition | `staines2021` | single source |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l5matrix_002`** (search_established, tract 3) — zonal Pi and PPi in situ. See §4. This
   is the single highest-value measurement in the layer because the principle it tests is
   assumed everywhere and measured nowhere.
2. **`g_l5matrix_006`** (contradiction, tract 4) — repeat the *Ank*-manipulation chondrocyte
   phenotype in an **`Enpp1`-null background** with paired ATP and PPi readouts. Under ATP
   export, the `wang2005` phenotype is abolished; under direct PPi transport, it persists. The
   decisive experiment was done in HEK293 overexpression and never in chondrocytes.
3. **`g_l5matrix_008` + `g_l6l5_005`** (contradiction + quantitative_gap, tract 2) — one method,
   one species, all zones, hydrated and at tissue scale, on **human** weight-bearing physis. The
   four-way disagreement cannot be resolved by adding a fifth method at a fifth length scale.
4. **`g_l5matrix_007` / `g_l6l5_006`** (known_unknown, tract 4) — identify the aggrecan-clearing
   activity. N-terminomics on hypertrophic-zone matrix to find the actual cleavage neoepitopes,
   then knock out the responsible protease. If no proteolytic neoepitope dominates, the removal
   is non-proteolytic (endocytic or osmotic) and the whole framing changes.
5. **`g_l5matrix_003`** (search_established, tract 3) — human physeal collagen stoichiometry by
   quantitative mass spectrometry, zone by zone. This retires x-L5-01 either way.
6. **`g_l6l5_013`** (method_blocked, tract 4) — cartilage-specific lysyl oxidase deletion.
   `lysyl_oxidase` is grade **E** in a layer whose central structural claim is that crosslinked
   collagen sets physeal tensile strength. Nobody has made the mouse.
7. **`g_l5matrix_010`** (quantitative_gap, tract 3) — does human physeal matrix change measurably
   *before* radiographic fusion, and can it be measured non-invasively? This is the only route
   from L5 into a clinically usable prediction, and it connects directly to L7's fusion timing.

---

## 7. Human-translation status

**18 of 41 nodes (44%) carry direct human evidence and 13 have replicated human evidence** —
respectable, and better than L1, L2 or L3. But the composition matters more than the fraction,
and in this layer the human evidence is systematically displaced in one of two ways.

**Displaced by tissue.** The aggrecan half-life (3.4 years), the free G1 half-life (25 years),
the osmotic swelling measurements, the PCM:ECM modulus ratio (~0.35) and the aggrecanase
genetics are **articular** cartilage — a tissue that turns over in years next to one whose
hypertrophic zone turns over in a day. The atlas holds `g_l6l5_007` open specifically to keep
these apart, and `aggrecan_acan` was one of the ten **rejected** confidence upgrades in Phase 3
for exactly this reason: ACAN gene dosage is not aggrecan turnover kinetics.

**Displaced by compartment.** Plasma PPi is human, well measured and in the wrong compartment;
serum phosphate likewise. The two grade-A nodes that are genuinely human and genuinely physeal
— `tnap_alpl` and `enpp1_enzyme` — are graded A on human **disease genetics**, which establishes
necessity and not concentration.

The genuinely human, genuinely physeal measurements in this layer number about three:
`xie2025`'s AFM modulus profile (10 donors, but at 9 nm tip radius on cryosections),
`wells2003`'s link protein : aggrecan G1 molar ratio (<1 in human cartilage >13 years), and
`zoehrer2025`'s ToF-SIMS calcium/organic peak at the calcified interface (n = 3 polydactyly
specimens, p < 0.0001). Thirteen nodes remain high translation risk, and the structural
properties on which every physeal biomechanics model depends are, in humans, one AFM study.
