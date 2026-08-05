# Phase 7 — Falsification baseline

**What this measures.** Whether the atlas predicts findings it has never seen, or merely
organises findings it has. 63 propositions were extracted from post-cutoff papers **before**
`graph.json` was opened, then put to the graph under the `QUERY.md` protocol and scored.

**BASELINE NUMBER (before any fix): 32 / 50 scored = 64.0% hit rate.**
Against the full held-out set including correct refusals: **32 / 63 = 50.8%**.
**SILENTLY_ABSENT = 16.** That is the number that matters.

**POST-FIX NUMBER: 32 / 50 = 64.0% — identical. Zero graph edits were applied.** See
`query/falsification_corrections.md` for why every candidate fix would have imported
held-out evidence, and what was logged instead.

---

## 1. Design

| | |
|---|---|
| Cutoff date | **2026-02-01** (Europe PMC `FIRST_PDATE` strictly after) |
| Papers held out | **64 selected, 63 scored** (1 excluded — see §1.1) |
| Layers spanned | **14** (L0–L13, all of them) |
| Non-ingestion check | every DOI **and** PMID against `atlas/sources/bibliography.yaml` **and** `graph.json.refs` |
| Blinding | propositions committed (`d6e5a1a`) **before** the first read of `graph.json` |
| Search | Europe PMC REST, `resultType=core`, `PUB_TYPE:"Journal Article" NOT PUB_TYPE:"Review"` on the primary sweep, 14 layer-scoped query pairs + supplementary L2/L5/L8 sweeps |

Held-out papers per layer: L0 5, L1 6, L2 3, L3 5, L4 5, L5 5, L6 3, L7 4, L8 5, L9 4,
L10 3, L11 6, L12 5, L13 4.

### 1.1 One contamination, found and removed — report it, don't hide it

`P38` (Wang X *et al.*, ancestry-modelled height PGS in HCHS/SOL,
`10.1016/j.xhgg.2026.100597`, PMID 41904631) passed the non-ingestion check at sweep time
and **failed it at scoring time**: it had been added to `bibliography.yaml` as `wang2026_2`
and cited in the `height_gwas` node by a concurrent process running in this repo between
the two checks (`refs` went 1036 → 1037 mid-session).

It is **excluded** from all counts. Two lessons, both structural:

1. A non-ingestion check taken once at the start of a run is not sound in a repo with
   concurrent writers. It must be re-run against the *scoring-time* state, and against
   `graph.json.refs` as well as the bibliography — the graph is the thing being tested.
2. Had it been left in, it would have scored CORRECT_PREDICTION and lifted L8's hit rate
   from 20% to 33%. The single most flattering item in the weakest layer was the
   contaminated one. That is the direction contamination always runs.

### 1.2 Scoring rules (fixed before scoring, applied to all 63)

| Bucket | Operational test |
|---|---|
| **CORRECT_PREDICTION** | A node claim or a `traversal_usable` signed path asserts the same directional statement, and the paper confirms it. |
| **WRONG_PREDICTION** | The atlas asserts the opposite sign, or a quantity the paper contradicts. |
| **CORRECTLY_OUTSIDE** | A key entity has no node **and** the atlas declares the ignorance — a registered gap, an explicit in-node statement of what is missing, or an `adversarial.yaml` scope boundary. Returning "no coverage" is the *correct* answer under `QUERY.md` §7. |
| **SILENTLY_ABSENT** | **Every** constituent entity exists as a node, **no** edge or claim links them in the asserted direction, and **no** gap flags the link as unknown. The atlas had the pieces and never joined them. |

Hit rate denominators. `hit = C / (C + W + S)` — a correct refusal is not a failed
prediction, so `CORRECTLY_OUTSIDE` is excluded from the denominator. `raw = C / n` is also
reported, because a layer that refuses everything should not score 100%.

---

## 2. Results

### 2.1 Buckets

| Bucket | n | % of 63 |
|---|---:|---:|
| CORRECT_PREDICTION | **32** | 50.8% |
| WRONG_PREDICTION | **2** | 3.2% |
| CORRECTLY_OUTSIDE | **13** | 20.6% |
| **SILENTLY_ABSENT** | **16** | **25.4%** |

### 2.2 Hit rate per layer — the real signal

| Layer | n | C | W | OUT | **SILENT** | **hit** | raw | reading |
|---|--:|--:|--:|--:|--:|--:|--:|---|
| L9 whole_organism_growth | 4 | 4 | 0 | 0 | 0 | **100%** | 100% | mechanistic |
| L6 mechanobiology | 3 | 3 | 0 | 0 | 0 | **100%** | 100% | mechanistic — but see §2.3 |
| L5 matrix_and_mineralization | 5 | 3 | 0 | 2 | 0 | **100%** | 60% | mechanistic |
| L3 signaling_networks | 5 | 2 | 0 | 3 | 0 | **100%** | 40% | knows its own edges |
| L0 developmental_origin | 5 | 3 | 0 | 2 | 0 | **100%** | 60% | knows its own edges |
| L10 environment_and_population | 3 | 2 | 0 | 1 | 0 | **100%** | 67% | mechanistic |
| L7 fusion_and_cessation | 4 | 3 | 0 | 0 | 1 | 75% | 75% | mechanistic |
| L11 pathology | 6 | 3 | 0 | 1 | 2 | 60% | 50% | mixed |
| L13 methods_and_data | 4 | 2 | 0 | 0 | 2 | 50% | 50% | mixed |
| L12 pharmacology | 5 | 2 | 0 | 1 | 2 | 50% | 40% | **bibliography** |
| L1 growth_plate_architecture | 6 | 2 | 1 | 1 | 2 | 40% | 33% | **bibliography** |
| L4 endocrine_and_systemic | 5 | 2 | 0 | 0 | 3 | 40% | 40% | **bibliography** |
| **L8 genetics_and_heritability** | 5 | 1 | 1 | 0 | **3** | **20%** | 20% | **bibliography** |
| L2 stem_and_progenitor | 3 | 0 | 0 | 2 | 1 | **0%** | 0% | honest refuser |
| **TOTAL** | **63** | **32** | **2** | **13** | **16** | **64.0%** | **50.8%** | |

Three findings the aggregate hides.

**The per-layer spread is 0%–100% on a 64% mean.** The atlas is not uniformly mechanistic.
Where the graph carries signed, human, within-layer edges (L5 mineralisation, L9 whole-organism,
L3 signalling core) it predicts. Where it carries a well-cited node list with few outbound
edges (L8, L4, L12) it does not.

**`coverage.md`'s layer warnings do not predict the hit rate — and are partly stale.**
`coverage.md` names **L2 as "the layer to distrust"** and **L8 as "nearly empty (3 nodes)"**.
L8 has since been built to **39 nodes** and is still the worst predictor here (20%), while
L2 produced no wrong answers at all — it refused, correctly, twice out of three. The document
warns about *evidence quality*; this test measures *connectivity*, and they come apart.
`coverage.md` also still reports 612 nodes / 764 edges against an actual **614 / 1181**.

**L2 scoring 0% is the least alarming number in the table.** Two of its three items were
correct refusals against declared boundaries. A layer that says "I don't know" and is right
is doing its job; the hit-rate denominator just has nothing left in it.

### 2.3 Two hits that should be discounted

`P31` and `P32` (both L6, both CORRECT) are the next instalments of a modelling programme
the atlas **already indexes** — `finite_element_model_physis` cites `koller2026` and
`computational_model_growth_plate` cites `koller2025`, and the held-out papers are
adjacent FE-model papers on the juvenile femur. That is bibliographic adjacency, not
prediction. L6's 100% rests on 3 items, 2 of which are cheap. **Discounting them the
overall hit rate is 30/48 = 62.5%.**

---

## 3. SILENTLY_ABSENT — 16 items, and what they have in common

These are the findings the atlas held every piece of and could not reach.

| id | layer | the edge that does not exist | layers it would cross |
|---|---|---|---|
| P06 | L1 | metaphyseal vascular insult → physeal output | L1→L1 |
| P11 | L4 | photoperiod / circadian → plate morphology, puberty onset | L4→L1 |
| P14 | L2 | growth-plate IHH → juvenile metaphyseal osteoblast window | L3→L1/L2 |
| P20 | L4 | hypothalamic IGF1R → pubertal timing, somatic growth | L4→L4 |
| P21 | L4 | GH **discontinuation** → adult height | L12→L7 |
| P23 | L4 | rhGH dose → scoliosis (via Hueter-Volkmann) | L12→L6 |
| P36 | L7 | endocrine state → bone-age landmark **order** | L11→L7 |
| P37 | L8 | height GWAS → skeletal **proportion** | L8→L9 |
| P39 | L8 | natural selection → population stature | L8→L10 |
| P41 | L8 | residual (non-genetic) height → later-life outcomes | L8→L7/L10 |
| P53 | L11 | FGFR1 → multiple epiphyseal dysplasia | L3→L11 |
| P55 | L11 | CNP agonist → cranial-base synchondrosis | L12→L9 |
| P56 | L12 | CNP agonist → vertebral growth plate | L12→L1 |
| P60 | L12 | GH intervention → non-GH pituitary axes | L12→L4 |
| P61 | L13 | post-pubertal velocity variance → growth-curve model | L9→L7 |
| P64 | L13 | late-adolescent hand-BA saturation → second skeletal site | L7→L13 |

### What they have in common — three overlapping patterns

**1. They are cross-layer edges. 14 of 16.** Only P06 (L1→L1) and P20 (L4→L4) are
intra-layer. `coverage.md` already states the mechanism — *"edge density is 1.25/node;
intra-layer edges dominate, so long mechanistic chains break at layer boundaries"* — and
this test converts that self-assessment into a measured failure rate. The atlas's layers
are well-built and weakly welded. **Every silent absence is a seam.**

**2. Pharmacology is a terminal layer. 5 of 16 have an L12 source** (P21, P23, P55, P56,
P60). `recombinant_human_gh` has 5 outbound edges, all inside the GH/IGF axis or to
whole-organism velocity; `vosoritide` has 4, all inside the CNP/FGFR3 cassette;
`npr2_receptor` has 24 edges and **not one** reaches a named skeletal site. The graph can
say a drug raises growth velocity and cannot say where else it acts, or what it costs.

**3. The atlas has exactly ONE growth plate. 5 of 16** (P06, P23, P55, P56, P64). It holds
`vertebral_growth_plate`, `cranial_base_synchondrosis`, `metacarpal_plate`,
`distal_femur_plate`, `proximal_tibia_plate`, `distal_radius_plate`,
`proximal_humerus_plate` and `mandibular_condylar_cartilage` as nodes — and wires signalling
and pharmacology to none of them. `vertebral_growth_plate` has 5 inbound edges, all from
mechanics and proportion. `cranial_base_synchondrosis` has 2 outbound edges, both
`traversal_usable: false`. Site-specific growth is a node list, not a subsystem.

**A fourth, weaker pattern: L8 is a citation shelf.** 3 of 16 (P37, P39, P41) plus the one
WRONG_PREDICTION (P42) are L8. Its nodes are A-graded and richly referenced, and their
`structural_confidence` is 0.27–0.38 — `sitting_height_ratio` has two edges, both
unusable; `height_gwas` scores 0.319. L8 was rebuilt from 3 to 39 nodes and the nodes were
never wired to the phenotypes in L7, L9 and L10 they explain.

### The generative form of the failure

Every one of the 16 is the same shape: **the atlas records what an entity IS and not what
it DOES to a neighbour in another layer.** A node is written from its own literature, with
its own refs and grades, and the edges that leave it point at its immediate mechanistic
family. Nothing in the build process asks "which node in a *different* layer does this
change?" — so the answer, 16 times out of 63, is nothing.

---

## 4. WRONG_PREDICTION — 2 items

**P09 (L1) — sign conflict on Hedgehog output under EVC2 loss.**
`evc_evc2_complex` states, from `ruizperez2007` in the Evc-null mouse growth plate:
*"Ihh expression is normal but the Ihh target genes Ptch1 and Gli1 are markedly **reduced**."*
The held-out paper reports that conditional Evc2 disruption in Gli1+ cells **augmented**
Gli1 and mechanosensor expression, and calls the result paradoxical itself.
**Mitigation:** different site (TMJ enthesis–condyle interface vs long-bone physis) and
different genetic design (Gli1-CreER vs germline). Recorded as a genuine sign conflict with
a context caveat, not as a refutation of the node.

**P42 (L8) — single number where a spread was required.**
`rare_variant_height` and `missing_heritability_height` both carry `wainschtein2026`'s
*"~68% common, ~20% rare"*, so the atlas answers **~20%** for the rare-variant share of
height heritability. The held-out WGS analysis reports **0.37** for standing height
specifically. Same direction, ~2× magnitude. The denominators genuinely differ (pedigree h²
pooled across 34 traits vs LD-independent rare-variant h² for one trait) — **which is
exactly the methodological spread `QUERY.md` type-7 requires be reported rather than
collapsed.** The defect is not the number; it is that a method-dependent quantity is stated
as a point estimate and is not in `parameters.disputed`.

---

## 5. CORRECTLY_OUTSIDE — 13 items

These are wins, and they are why the raw rate (50.8%) understates the atlas. Four sources:

- **Declared scope boundaries** (`adversarial.yaml`) — P12 (OA pathogenesis, a09), P47
  (SARS-CoV-2 and childhood growth, a02, verbatim).
- **Registered gaps** — P29 against `g_l9organism_006` (does the catch-up rate constant
  scale with duration of preceding suppression?).
- **In-node statements of ignorance** — P03 (`septoclast`: *"their origin has been assigned
  variously to pericytes and to the perichondrium"* — the paper resolves it), P15
  (`dkk1_antagonist`: *"What is missing is the physeal half"*).
- **Entity genuinely absent, no false coverage claimed** — P02 (USP26), P08 (adrenergic),
  P13 (glycolysis), P16 (sulfatases), P17 (lipotoxicity), P27 (prolyl hydroxylases), P52
  (MIMS1), P58 (INSL3).

P03 is the exemplar of what this atlas is for: it had located the precise open question
years of literature had left, and a paper published after the cutoff answered it.

Two of these deserve a second look as coverage holes rather than clean refusals: the graph
has **no autonomic/neural input to the growth plate at all** (P08) and **no chondrocyte
energy metabolism at all** (P02, P13) across 614 nodes. Both are logged in §7.

---

## 6. Per-item record

`SC` = `structural_confidence` of the anchor node (`atlas/tools/structural_confidence.py`);
it reports **graph completeness in that region, never evidence quality**.

### L0

**P01** · **CORRECT_PREDICTION** · `10.3390/genes17020238` · 2026-02-15

> Duplication of PAR1 spanning SHOX (increased SHOX dosage) produces tall stature in a human male, the directional mirror of SHOX haploinsufficiency.

- **Traversal:** NODE klinefelter_syndrome (states: extra X = extra SHOX copy, phenotype is tall stature); edges e00246 shox_gene-correlates_with(+)->klinefelter_syndrome, e00248 ->adult_height_attainment, BOTH traversal_usable=false
- **structural_confidence:** 0.221
- **Note:** Graph asserts the dose direction in prose; it cannot DERIVE it - both edges are correlates_with. Answer is [ATLAS] node-read, not [ATLAS-INFERRED] traversal.

**P02** · CORRECTLY_OUTSIDE · `10.1038/s41413-026-00517-5` · 2026-04-09

> USP26 deubiquitinates FBP2, raising mitochondrial oxidative phosphorylation in chondrocytes, and is required for chondrocyte hypertrophy and mineralization during endochondral ossification; compression loading induces it via ERalpha S118 phosphorylation.

- **Traversal:** alias_to_id: 'usp26' -> none; 'fbp2' -> none; no chondrocyte energy-metabolism node ('oxidative phosphorylation','glycolysis' return 0 nodes)
- **structural_confidence:** n/a
- **Note:** Correct answer is 'no coverage' per QUERY.md §7. Note: hypertrophic_chondrocyte DOES record 2-5x mitochondrial expansion (hunziker1987) - the phenomenology without the control logic.

**P03** · CORRECTLY_OUTSIDE · `10.1038/s41467-026-71952-5` · 2026-04-14

> CD55+CD90+ mesenchymal cells transiently give rise to FABP5+ septoclasts at the chondro-osseous junction and drive osteoclastogenesis in the primary ossification centre before LepR+ stroma assumes that role.

- **Traversal:** NODE septoclast: 'their origin has been assigned variously to pericytes and to the perichondrium' - explicit statement of ignorance
- **structural_confidence:** 0.768
- **Note:** Atlas declared the exact unknown the paper resolves (CD55+CD90+ mesenchyme). Textbook correct-negative.

**P04** · **CORRECT_PREDICTION** · `10.1038/s41598-026-46913-z` · 2026-04-19

> Podoplanin-positive osteolineage cells arise in the bone collar concurrently with primary ossification centre initiation and contribute to metaphyseal trabecular bone.

- **Traversal:** NODE bone_collar_formation: 'the collar's inner surface is the source of the osteoblast precursors that will occupy the POC; Osterix+ precursors travel into the cartilage with the invading vessels'; e01046 vascular_invasion_poc-required_for(+)->stem_cell_niche_vascular_coupling
- **structural_confidence:** 0.226
- **Note:** PDPN is a new marker on an asserted route. Node has only ONE outbound edge and it is precedes(unknown) - sc 0.226.

**P05** · **CORRECT_PREDICTION** · `10.1016/j.jot.2026.101123` · 2026-05-16

> A CD140a+PDPN+ skeletal stem/progenitor population peaks at E14.5 in the limb bud and is chondrogenically primed by a specific type-E endothelial subset via direct cell-cell communication.

- **Traversal:** NODE stem_cell_niche_vascular_coupling: 'VEGF blockade during BMP2-induced ossicle formation shifts the output from bone to predominantly cartilage, showing that vascular signalling steers skeletal progenitor fate'
- **structural_confidence:** 0.714
- **Note:** Endothelial control of SSPC chondrogenic fate is asserted; paper supplies the EC subset. REACH is EMPTY DICT (only outbound edge is hypothesized_link e00056).

### L1

**P06** · **SILENTLY_ABSENT** · `10.3349/ymj.2025.0111` · 2026-02-01

> Metaphyseal drill holes distal to an intact physis change long-bone length: a single hole causes overgrowth, whereas two holes cause growth suppression, i.e. the metaphyseal vascular response modulates physeal output without any physeal injury.

- **Traversal:** NODES metaphyseal_vasculature(L1), growth_velocity_longitudinal(L1), physeal_bar_formation(L6), guided_growth_tension_band(L6, context literally 'extraperiosteal two-hole'). NO edge metaphyseal perturbation -> longitudinal growth
- **structural_confidence:** 0.803
- **Note:** Atlas wires metaphyseal vessels only forward to primary_spongiosa (e00023). The retrograde arm - metaphyseal vascular insult changes physeal OUTPUT - is absent though both endpoints are nodes.

**P07** · **CORRECT_PREDICTION** · `10.1038/s41413-025-00500-6` · 2026-02-09

> Growth-plate chondrocytes transition to an osteoblast phenotype during normal postnatal bone formation, and the switch is governed by NOTCH, BMP and MAPK signalling with Mesp1/Alx1/Grhl3/Hmx3 as transcriptional markers.

- **Traversal:** NODE chondrocyte_to_osteoblast_transdifferentiation ('~63% of trabecular osteocalcin+ cells chondrocyte-derived at 1 month'); e01072 hypertrophic_chondrocyte-differentiates_into(+)->, e00321 beta_catenin_ctnnb1-activates(+)->
- **structural_confidence:** 0.831
- **Note:** Atlas asserts the process flatly and quantitatively. NOTCH/BMP/MAPK detail is new but non-contradicting.

**P08** · CORRECTLY_OUTSIDE · `10.1093/jbmrpl/ziag021` · 2026-02-14

> Chondrocyte-specific loss of the beta2-adrenoceptor REDUCES long bone growth by accelerating the proliferative-to-hypertrophic transition, so sympathetic beta2-AR signalling in chondrocytes is growth-permissive.

- **Traversal:** alias 'adrenergic' -> 0 nodes; 'catecholamine' -> 0 nodes. No autonomic/neural input to the plate anywhere in 614 nodes
- **structural_confidence:** n/a
- **Note:** Correct 'no coverage' answer, but flagged: the atlas has NO sympathetic-innervation subsystem at all, and no gap claims one is needed.

**P09** · **WRONG_PREDICTION** · `10.3390/ijms27073324` · 2026-04-07

> Gli1+ slow-cycling progenitors occupy the TMJ enthesis-condyle interface, and Evc2 loss in them paradoxically increases Gli1 and mechanosensor (Yap/Wwtr1/Piezo1) expression and expands transit-amplifying cells.

- **Traversal:** NODE evc_evc2_complex: 'Ihh expression is normal but the Ihh target genes Ptch1 and Gli1 are markedly REDUCED' (Evc-null mouse growth plate, ruizperez2007). Paper: Evc2 loss in Gli1+ cells AUGMENTED Gli1 + mechanosensors
- **structural_confidence:** n/a
- **Note:** Opposite sign on the same readout. Mitigating: atlas claim is growth-plate, paper is TMJ enthesis-condyle - a site the atlas holds only as mandibular_condylar_cartilage (conf D). Records as a genuine sign conflict with a context caveat.

**P10** · **CORRECT_PREDICTION** · `10.1016/j.bone.2026.117913` · 2026-05-01

> Osteochondromas in hereditary multiple osteochondroma arise from perichondrial progenitors, and the inner (Pdgfra+) rather than the outer (Fgf18+) perichondrial layer supplies the tumour-initiating cells.

- **Traversal:** NODE groove_of_ranvier ('cell flow from perichondrium into the plate margin'; CD90+/CD105+ progenitors; osteochondroma named in node); NODE bone_collar_formation ('the perichondrium is not scaffolding but a progenitor reservoir')
- **structural_confidence:** 0.645
- **Note:** Perichondrial origin asserted. Inner-vs-outer layer resolution is beyond the graph's granularity.

**P11** · **SILENTLY_ABSENT** · `10.1016/j.bone.2026.118036` · 2026-08-03

> Prepubertal blue-light exposure advances puberty onset and alters epiphyseal plate and proliferative-zone thickness with changed local IGF-1/IGFBP-3 expression, in a dose (duration)-dependent and sex-dependent way.

- **Traversal:** NODES circadian_growth_regulation(L4), seasonality_growth_velocity(L4), igf1_local_growth_plate(L4), growth_plate(L1), pubertal_growth_spurt(L4). Only light-related edges: e00487 hypothesized_link(unknown) and e00486 correlates_with(+) - BOTH traversal_usable=false
- **structural_confidence:** n/a
- **Note:** Every photoperiod edge in the graph is sign-exempt, so no light->plate or light->puberty statement can be derived even though both endpoints exist.

### L2

**P12** · CORRECTLY_OUTSIDE · `10.1002/advs.75725` · 2026-05-19

> A Prg4+ chondroprogenitor-like population is electro-mechanically responsive and mediates cartilage anabolism via an ECM-FAK-PI3K-Akt axis.

- **Traversal:** adversarial.yaml a09: 'What causes osteoarthritis in articular cartilage? articular_cartilage node exists; OA pathogenesis does not'
- **structural_confidence:** n/a
- **Note:** Declared scope boundary.

**P13** · CORRECTLY_OUTSIDE · `10.1016/j.bone.2026.117980` · 2026-06-16

> Skeletal stem/progenitor cells do NOT depend on high glycolytic flux: PFKFB3 deletion cuts glycolysis by >=30% yet leaves SSPC function and bone mass intact through compensatory substrate uptake.

- **Traversal:** 'glycolysis' -> 0 nodes; 'pfkfb3' -> 0 nodes; no metabolic-flux node in L2
- **structural_confidence:** n/a
- **Note:** Correct 'no coverage'. Chondrocyte/SSPC bioenergetics is a wholly unbuilt subsystem.

**P14** · **SILENTLY_ABSENT** · `10.1038/s41467-026-74929-6` · 2026-06-26

> Juvenile metaphyseal osteoblast proliferation is sustained by growth-plate Indian hedgehog and ceases at growth-plate maturation, so growth-plate IHH output is the permissive condition for the juvenile metaphyseal window in which osteosarcoma arises.

- **Traversal:** NODES ihh_protein(L3), growth_plate_senescence(L2), primary_spongiosa(L1), chondrocyte_to_osteoblast_transdifferentiation(L2, holds shu2021: 'chondrocyte-derived osteoblasts dominate only before adolescence'). NO edge ihh -> any metaphyseal osteoblast compartment
- **structural_confidence:** 0.799
- **Note:** The atlas already holds the juvenile-window observation (shu2021) AND the IHH node, and never asks what sustains the window. Nine IHH outbound edges, none leaving the cartilage compartment toward metaphyseal bone.

### L3

**P15** · CORRECTLY_OUTSIDE · `10.1242/bio.062540` · 2026-03-01

> FGFR3 gain-of-function raises Dkk1 in cartilage, and Dkk1 inhibition (de-repressing canonical Wnt/beta-catenin) restores growth in an achondroplasia model — i.e. FGFR3 acts partly by suppressing Wnt.

- **Traversal:** NODE dkk1_antagonist: 'What is missing is the physeal half: no report establishes DKK1 protein in the human or mouse growth plate by zone, and no chondrocyte-restricted Dkk1 deletion'
- **structural_confidence:** 0.766
- **Note:** Explicit ignorance statement covering exactly this. Note the graph could otherwise have chained FGFR3->DKK1->LRP5/6(e00310/e00311)->reduced canonical WNT->dwarfism (wnt_canonical_chondrocyte, sc 0.954) - one missing edge from a derivation.

**P16** · CORRECTLY_OUTSIDE · `10.1016/j.jbc.2026.113111` · 2026-05-06

> ARSL is a Golgi chondroitin-4-O-sulfatase; its loss hypersulfates chondroitin sulfate, alters chondrocyte TGF-beta responsiveness and causes chondrodysplasia punctata-like skeletal malformation.

- **Traversal:** 'sulfat' returns no sulfatase node; no chondroitin-sulfate node (aggrecan_acan exists, its GAG sulfation state does not)
- **structural_confidence:** n/a
- **Note:** Correct 'no coverage'. GAG sulfation chemistry is absent from L5 despite 41 matrix nodes.

**P17** · CORRECTLY_OUTSIDE · `10.3390/biom16050746` · 2026-05-19

> Palmitic acid REDUCES longitudinal bone growth while INCREASING collagenous matrix deposition and mineralization — growth length and matrix maturation dissociate under lipotoxic exposure.

- **Traversal:** 'fatty acid' -> gut_microbiome_growth, microbiome_igf1_axis only; no lipotoxicity node
- **structural_confidence:** n/a
- **Note:** Correct 'no coverage'.

**P18** · **CORRECT_PREDICTION** · `10.3892/ijmm.2026.5874` · 2026-05-29

> The oxygen-sensing demethylase KDM6A promotes chondrocyte-to-osteoblast transdifferentiation by activating Wnt/beta-catenin, linking the local oxygen gradient to the fate of hypertrophic chondrocytes.

- **Traversal:** e00321 beta_catenin_ctnnb1-activates(+)->chondrocyte_to_osteoblast_transdifferentiation (usable, mouse hypertrophic chondrocytes); NODE wnt_canonical_chondrocyte
- **structural_confidence:** 0.954
- **Note:** Sign-bearing core (WNT/beta-catenin drives transdifferentiation) predicted and confirmed. The oxygen-sensing arm is absent: hypoxic_gradient_signaling reaches only hif1a_chondrocyte (e00348) and never beta-catenin.

**P19** · **CORRECT_PREDICTION** · `10.1016/j.diff.2026.100978` · 2026-07-13

> A synonymous NPR2 variant (c.2484C>T) causes acromesomelic dysplasia Maroteaux type by creating a splice donor, producing frameshift and NMD — i.e. NPR2 loss of function can be produced by a protein-silent change.

- **Traversal:** e00207 npr2_receptor-required_for(+)->acromesomelic_dysplasia_maroteaux (usable, human, 21 families); e00983 npr2_gene-required_for(+)->npr2_receptor
- **structural_confidence:** 0.904
- **Note:** 'Biallelic NPR2 LoF -> AMDM' is asserted with an A-grade human edge. A synonymous splice-gain allele is a new route to LoF, not a new biology.

### L4

**P20** · **SILENTLY_ABSENT** · `10.1016/j.molmet.2026.102355` · 2026-03-16

> IGF1R signalling in LepRb (hypothalamic leptin-receptor) neurons is required for normal pubertal timing and transient postnatal somatic growth, so part of IGF-1's growth action is central, not growth-plate-local.

- **Traversal:** NODES leptin_receptor(L4, 'ObRb in hypothalamic neurons transduces energy sufficiency to the kisspeptin-GnRH axis'), igf1_receptor(L4), kisspeptin_kiss1(L4), gnrh_hormone(L4), igf1_systemic(L4). NO edge igf1_receptor -> any hypothalamic node
- **structural_confidence:** 0.846
- **Note:** Atlas routes IGF-1 to the plate only. A central (hypothalamic) IGF1R arm setting pubertal timing has no representation despite every endpoint being a node in the SAME layer.

**P21** · **SILENTLY_ABSENT** · `10.1210/clinem/dgaf626` · 2026-04-01

> In adolescents with childhood idiopathic isolated GHD who retest GH sufficient at mid-puberty, STOPPING rhGH does not reduce near-adult height relative to target height compared with continuing it.

- **Traversal:** NODES gh_deficiency(L11), recombinant_human_gh(L12), adult_height_attainment(L7), pubertal_growth_spurt(L4). e00726 rhGH-activates(+)->growth_velocity_longitudinal exists; nothing represents DISCONTINUATION
- **structural_confidence:** 0.882
- **Note:** The graph can only say 'more GH, more growth'. It has no representation of treatment withdrawal, so it cannot express 'stopping costs nothing once the axis has normalised'.

**P22** · **CORRECT_PREDICTION** · `10.1302/2046-3758.155.bjr-2025-0563.r1` · 2026-05-13

> In Pappa2-null mice, rhGH or rhPAPP-A2 (but not rhIGF1 equally) rescues body length, and the rescue is sex-specific and involves cannabinoid receptor and STAT3 signalling in bone.

- **Traversal:** NODE pappa2_deficiency ('separates total from BIOAVAILABLE IGF-I'); NODE pappa2_protease; e01113 pappa_protease-activates(+)->ihh_protein
- **structural_confidence:** n/a
- **Note:** Rescue-by-restoring-IGF-bioavailability is implied. Sex-specificity and the cannabinoid-receptor/STAT3 arm are outside (no cannabinoid node).

**P23** · **SILENTLY_ABSENT** · `10.1080/07853890.2026.2697592` · 2026-07-10

> rhGH treatment of short stature increases incident scoliosis (HR ~2.7) with a positive dose-response on cumulative GH dose — a growth-acceleration cost paid in spinal deformity.

- **Traversal:** NODES recombinant_human_gh(L12), scoliosis_vertebral_growth(L6), vertebral_growth_plate(L1), hueter_volkmann_law(L6, e00521 required_for(+)->scoliosis_vertebral_growth). NO edge rhGH -> scoliosis or rhGH -> vertebral_growth_plate
- **structural_confidence:** 0.849
- **Note:** The pieces for 'accelerating growth in an already-asymmetric spine amplifies the curve via Hueter-Volkmann' are all present and unjoined. rhGH has 5 outbound edges, all to the GH/IGF axis or to whole-organism velocity; none to any site-specific plate.

**P24** · **CORRECT_PREDICTION** · `10.1210/clinem/dgag309` · 2026-08-01

> Once-weekly somapacitan is non-inferior to daily GH for 52-week height velocity in prepubertal girls with Turner syndrome (9.0 vs 9.5 cm/yr).

- **Traversal:** NODE transcon_growth_hormone ('a controlled test of whether the growth plate integrates GH exposure or responds to its pulsatility... weekly dosing is at least as effective'); NODE turner_syndrome; guzzetti2024 in recombinant_human_gh lists Turner as licensed
- **structural_confidence:** 0.767
- **Note:** Weekly-equals-daily is an explicit atlas claim, correctly hedged by nct02413138 (somavaratan phase 3 terminated for non-inferiority failure).

### L5

**P25** · **CORRECT_PREDICTION** · `10.1093/jbmr/zjaf136` · 2026-03-01

> Inhibiting ENPP1 lowers plasma PPi and improves skeletal mineralization in a late-onset hypophosphatasia model — i.e. ENPP1 is the dominant generator of the PPi that accumulates when TNAP is deficient, and is druggable.

- **Traversal:** NODE enpp1_enzyme: 'deleting Enpp1 genetically rescues the hypomineralization of Akp2(Alpl)-/- mice, the cleanest demonstration that the phenotype of TNAP loss is caused by PPi excess'; NODE tnap_alpl; NODE pi_ppi_ratio
- **structural_confidence:** 0.849
- **Note:** Strongest hit in the run. The atlas states the genetic proof of concept; the paper is its pharmacological execution (REV102). This is the CORR-001 ANKH/ENPP1 correction paying off.

**P26** · **CORRECT_PREDICTION** · `10.1210/clinem/dgaf585` · 2026-03-01

> Calcitriol MONOTHERAPY (no oral phosphate, no burosumab) improves rickets severity and mineral markers in XLH over 12 months without worsening nephrocalcinosis.

- **Traversal:** NODE vitamin_d_calcitriol: 'normalising mineral ion homeostasis with a rescue diet prevents rachitic growth plate changes in VDR-null mice, showing rickets is secondary to hypophosphataemia'; NODE x_linked_hypophosphatemia (PHEX->FGF23->low Pi + impaired 1-alpha-hydroxylation)
- **structural_confidence:** 0.803
- **Note:** Atlas says the plate reads mineral-ion supply, not VDR tone. Calcitriol alone raises supply -> rickets improves.

**P27** · CORRECTLY_OUTSIDE · `10.1016/j.jbc.2026.111459` · 2026-04-16

> P4HA3, though peaking in the developing skeleton at E12.5, is DISPENSABLE for prolyl-4-hydroxylation of type I collagen in vivo — isoform redundancy not isoform specificity.

- **Traversal:** 'prolyl' -> iron_deficiency_growth only; 'hydroxyproline' -> 0 nodes. No collagen prolyl-4-hydroxylase node
- **structural_confidence:** n/a
- **Note:** Correct 'no coverage'. A negative result on an uncovered isoenzyme.

**P28** · **CORRECT_PREDICTION** · `10.1016/s2213-8587(26)00013-6` · 2026-04-24

> Burosumab given below 12 months of age in XLH is safe and improves phosphate homeostasis and rickets, extending the effective treatment window earlier than the licensed >=1 year.

- **Traversal:** NODE x_linked_hypophosphatemia + NODE fgf23_hormone + NODE phosphate_homeostasis (burosumab named inside all three); liang2025 in-node: 'short stature in XLH is already present in PRE-PUBERTAL children'
- **structural_confidence:** 0.747
- **Note:** Deficit present pre-pubertally + FGF23 blockade corrects the deficit => earlier blockade is better. Directionally derivable.

**P29** · CORRECTLY_OUTSIDE · `10.3389/fped.2026.1845607` · 2026-07-02

> In XLH on conventional therapy, LATER age at diagnosis predicts worse final height Z-score independently of other factors — diagnostic delay is itself a determinant of adult stature.

- **Traversal:** GAP g_l9organism_006 (quantitative_gap): 'What is the absolute rate constant k of human catch-up growth... and does it scale with the DURATION of the preceding growth suppression?'
- **structural_confidence:** n/a
- **Note:** The atlas registered exactly this as an open quantitative gap. The paper is a partial answer to a declared unknown.

### L6

**P30** · **CORRECT_PREDICTION** · `10.37796/2211-8039.1696` · 2026-03-01

> Restricting physical activity (COVID lockdown) lowers linear growth velocity in children, with a detectable effect in boys and not in girls.

- **Traversal:** e00879 sport_specific_loading_human-activates(+)->growth_velocity_longitudinal (usable, human, 47 children, jumping exercise 4.20 vs 2.48 cm); NODE disuse_growth_effect
- **structural_confidence:** 0.714
- **Note:** Usable signed human edge, correct direction. The male-only significance is unanticipated.

**P31** · **CORRECT_PREDICTION** · `10.3389/fspor.2026.1746084` · 2026-07-14

> Sport-specific hip loading concentrates compressive stress in identifiable subregions of the proximal femoral physis, giving a mechanical route from adolescent athletic loading to cam deformity.

- **Traversal:** NODE finite_element_model_physis (already cites koller2026 'foot progression angle alters hip contact forces and femoral growth plate mechanics in silico'); NODE hueter_volkmann_law (17.1%/0.1 MPa); NODE physeal_stress_in_vivo
- **structural_confidence:** 0.243
- **Note:** CHEAP HIT: the held-out paper is the next instalment of a programme the atlas already indexes. Counted, but flagged - this is bibliographic adjacency, not prediction.

**P32** · **CORRECT_PREDICTION** · `10.1186/s12938-026-01598-3` · 2026-07-15

> A single mechanobiological growth rule — octahedral shear stress accelerates and hydrostatic compressive stress retards longitudinal growth — reproduces juvenile femoral morphogenesis across epiphyseal, apophyseal and appositional growth simultaneously.

- **Traversal:** NODE computational_model_growth_plate (koller2025 personalised multi-scale femoral growth prediction); NODE hueter_volkmann_law (octahedral-shear/hydrostatic rule is its quantitative form)
- **structural_confidence:** n/a
- **Note:** Same caveat as P31 - same modelling programme already in the bibliography.

### L7

**P33** · **CORRECT_PREDICTION** · `10.1097/md.0000000000047998` · 2026-03-01

> Post-menarcheal height gain in girls with early/precocious puberty is small and bounded, and GnRH-agonist treatment before menarche raises predicted adult height relative to untreated girls.

- **Traversal:** NODE menarche_growth_remaining (mean 8.0 cm, SD 4.9, range 0.2-31.1); e00739 gnrh_analog_leuprolide-activates(+)->adult_height_attainment (usable); e00740 ->inhibits(-)->bone_age
- **structural_confidence:** 0.226
- **Note:** Both clauses predicted. Node sc is 0.226 - a thinly-connected region carrying an A-grade claim.

**P34** · **CORRECT_PREDICTION** · `10.1007/s40618-026-02957-6` · 2026-06-24

> In premature pubarche, final height is predicted by height relative to genetic potential and by skeletal maturation (BA/CA) at presentation, rather than by androgen concentrations.

- **Traversal:** NODE remaining_growth_prediction + NODE bone_age ('the variable on which every remaining-growth prediction is built') + NODE mid_parental_target_height + NODE adrenarche
- **structural_confidence:** 0.645
- **Note:** 'Height relative to genetic potential + skeletal maturation predict final height' is the atlas's core prediction machinery, applied to a cohort it never saw.

**P35** · **CORRECT_PREDICTION** · `10.3390/children13070861` · 2026-06-29

> In Laron syndrome (IGF-1 deficiency), menarche occurs at a bone age closer to normal than its chronological age, so skeletal maturation rather than chronological age indexes pubertal maturation when growth is abnormal.

- **Traversal:** NODE bone_age ('bone age is not chronological age with noise: it is systematically displaced by sex, adiposity and estrogen exposure'; morishima1995 BA 14 y at CA 24 y in aromatase deficiency); NODE laron_syndrome
- **structural_confidence:** 0.827
- **Note:** The atlas holds the extreme-case precedent (aromatase deficiency, ERalpha loss) that BA dissociates from CA in endocrine disease. Laron is the same class.

**P36** · **SILENTLY_ABSENT** · `10.13107/jocr.2026.v16.i07.7622` · 2026-07-01

> The canonical skeletal-maturity sequence can invert: distal phalangeal physeal closure can precede thumb adductor sesamoid ossification in GH deficiency, so bone-age landmark ordering is not invariant across endocrine states.

- **Traversal:** NODES fusion_timing_order(L7, 'a reproducible ascending order... most pairwise relationships invariant'), greulich_pyle_method(L7), gh_deficiency(L11), bone_age(L7). NO edge from any endocrine state to landmark ORDER
- **structural_confidence:** 0.645
- **Note:** Atlas asserts order invariance without an endocrine-state qualifier and holds no edge that could condition it. A GHD-driven inversion is unrepresentable, and the atlas does not flag it as unknown.

### L8

**P37** · **SILENTLY_ABSENT** · `10.1016/j.ajhg.2026.02.015` · 2026-03-19

> Skeletal PROPORTION (sitting-height ratio) has its own genetic architecture: 565 loci across ~550,000 people, overlapping height loci but with fine-mapped signals that are frequently distinct from height signals.

- **Traversal:** NODES height_gwas(L8, sc 0.319), sitting_height_ratio(L9, sc 0.269), body_proportion_development(L9), limb_segment_proportion(L9). sitting_height_ratio has exactly TWO edges, both correlates_with, neither to any L8 node
- **structural_confidence:** 0.269
- **Note:** The atlas has a saturated height-GWAS node AND a proportion phenotype node and never connects them - despite already holding shox_haploinsufficiency as a worked genetic->limb-segment example. Purest L8/L9 seam failure in the run.

**P39** · **SILENTLY_ABSENT** · `10.1038/s41586-026-10358-1` · 2026-04-15

> Polygenic height in West Eurasia has been under strong DIRECTIONAL selection over the last ten millennia, with ~1 SD shifts in trait-predicting allele combinations — human stature genetics is not at neutral equilibrium.

- **Traversal:** NODES height_gwas(L8), height_polygenic_score(L8), population_height_variation(L10), secular_trend_height(L10), migration_studies_height(L10). No node or edge represents natural selection on stature
- **structural_confidence:** 0.319
- **Note:** Evolution is absent as a mechanism class. The graph can say height varies between populations and over time, and cannot say why in allele-frequency terms.

**P40** · **CORRECT_PREDICTION** · `10.1016/j.ajhg.2026.05.013` · 2026-06-22

> Adults shorter than their polygenic score predicts are enriched for predicted-loss-of-function variants in ACAN and IGF1, and adults taller than predicted for damaging missense in FBN1 — monogenic growth-plate genes surface as residual from the polygenic model.

- **Traversal:** NODE rare_variant_height: '83 variants overlap genes mutated in monogenic growth disorders, so the rare-coding tier is partly the same gene set as the Mendelian tier at lower allelic effect'; NODE common_vs_rare_pathway_divergence; NODES acan_gene, igf1_gene, marfan_syndrome(FBN1->tall)
- **structural_confidence:** 0.380
- **Note:** Best L8 hit: the atlas's rare/Mendelian-tier-overlap claim predicts precisely which genes surface in PGS-misaligned individuals, including the FBN1 sign (taller-than-expected).

**P41** · **SILENTLY_ABSENT** · `10.1016/j.ajcnut.2026.101425` · 2026-07-01

> Residual height (observed minus genetically predicted from ~9,863 variants) carries independent associations with later-life disease incidence and mortality — the non-genetic component of attained stature is itself a health signal.

- **Traversal:** NODES height_polygenic_score(L8), adult_height_attainment(L7), stunting(L10, already carries victora2008 'shorter adult height, less schooling and lower income'), socioeconomic_gradient_height(L10)
- **structural_confidence:** 0.380
- **Note:** Weakest member of this bucket - the residual-height-to-disease question sits at the edge of scope. Recorded as silent because the atlas DOES carry height->downstream-outcome content in stunting and never generalises it.

**P42** · **WRONG_PREDICTION** · `10.1186/s13059-026-04140-9` · 2026-07-02

> Rare variants (LD-independent, from WGS in ~349,000 people) account for ~0.37 of the heritability of standing height — a substantially larger rare variant share than for BMI or blood pressure.

- **Traversal:** NODE rare_variant_height + NODE missing_heritability_height both state (wainschtein2026): '~68% common, ~20% rare' - the atlas returns ~20% as the rare-variant share of height heritability. Paper: 0.37 for standing height
- **structural_confidence:** 0.380
- **Note:** Same direction, ~2x magnitude disagreement. Denominators differ (pedigree h2 across 34 traits vs LD-independent rare-variant h2 for one trait) - which is exactly the methodological spread QUERY.md type-7 requires be REPORTED. The atlas states a single number and would have answered 20%.

### L9

**P43** · **CORRECT_PREDICTION** · `10.3390/children13050641` · 2026-05-03

> In SGA children without catch-up, EARLIER rhGH initiation yields greater height gain and a smaller adult-height deficit versus target height, and pubertal growth contributes little to final adult height.

- **Traversal:** e00726 recombinant_human_gh-activates(+)->growth_velocity_longitudinal; NODE recombinant_human_gh ('its skeletal effect requires open epiphyses'); NODES small_for_gestational_age, sga_catch_up, growth_cessation
- **structural_confidence:** 0.882
- **Note:** 'Requires open epiphyses' + finite remaining growth => earlier start, larger gain. Weakly but correctly derivable.

**P44** · **CORRECT_PREDICTION** · `10.1183/13993003.01678-2025` · 2026-07-02

> Ivacaftor (a CFTR modulator, not a growth drug) accelerates height growth and raises final height in cystic fibrosis — correcting the primary systemic disease recovers linear growth.

- **Traversal:** NODE catch_up_growth: 'directly observed in humans after treatment of hypothyroidism, glucocorticoid excess, coeliac disease and malnutrition'; NODE inflammation_growth_suppression (sc 0.969); NODE celiac_disease_growth
- **structural_confidence:** n/a
- **Note:** The atlas states a general rule - correcting the primary systemic disease recovers linear growth - and CFTR modulation is a new instance of it. No CF node needed for the prediction to hold.

**P45** · **CORRECT_PREDICTION** · `10.1007/s12325-026-03719-9` · 2026-07-28

> Vosoritide raises height SDS in Chinese children with achondroplasia in routine care (-4.7 to -4.3 at 12 months) and improves body proportion (sitting height/height ratio).

- **Traversal:** e00214 vosoritide-activates(+)->npr2_receptor; e00810 vosoritide-inhibits(-)->fgfr3_mapk_branch; NODE vosoritide (+1.57 cm/yr phase 3)
- **structural_confidence:** 0.888
- **Note:** Height-SDS gain predicted. The body-proportion clause (sitting height/height) is NOT derivable - no edge from vosoritide to sitting_height_ratio.

**P46** · **CORRECT_PREDICTION** · `10.1038/s41598-026-61162-w` · 2026-08-03

> Prednisone but NOT vamorolone suppresses serum bone/cartilage turnover markers (ALP, osteocalcin, P1NP, CTX1) in DMD boys — the growth-failure arm of glucocorticoid action is dissociable from the anti-inflammatory arm.

- **Traversal:** NODE glucocorticoid_sparing_strategy ('whether the anti-inflammatory transrepression arm can be separated from the transactivation arm that suppresses growth and bone'; clemens2026 vamorolone vs prednisone); e01140 glucocorticoid_cortisol-inhibits(-)->ihh_protein; e00455 ->inhibits(-)->growth_velocity_longitudinal
- **structural_confidence:** 0.226
- **Note:** The atlas frames the exact dissociation the paper demonstrates biochemically.

### L10

**P47** · CORRECTLY_OUTSIDE · `10.3389/fped.2026.1769902` · 2026-03-03

> Central precocious puberty incidence in girls rose during the COVID-19 pandemic in Japan, replicating the international pandemic signal in a population with low obesity prevalence.

- **Traversal:** adversarial.yaml a02: 'How does SARS-CoV-2 infection affect childhood growth? plausible growth question, ZERO atlas coverage'
- **structural_confidence:** n/a
- **Note:** Declared boundary, verbatim. Note the atlas holds central_precocious_puberty and endocrine_disrupting_chemicals but explicitly disclaims the pandemic axis.

**P48** · **CORRECT_PREDICTION** · `10.1371/journal.pone.0351677` · 2026-06-12

> Height in Macao children rose ~2.1 cm (boys) and ~2.4 cm (girls) between 2005 and 2020 while BMI rose faster than height — the secular height trend continues but is decoupling from the weight trend.

- **Traversal:** NODE secular_trend_height (ncd2016: 18.6M adults, 200 countries, up to +2.0 cm/decade sustained)
- **structural_confidence:** 0.675
- **Note:** Direction and order of magnitude correct (+2.1/+2.4 cm over 15 y). The BMI-decoupling clause is out of scope per adversarial a12.

**P49** · **CORRECT_PREDICTION** · `10.1002/ajhb.70309` · 2026-07-01

> Adult male height in Poland rose across 1965-2023 AND a socioeconomic gradient in height persisted throughout — secular gain does not abolish the SES stratification of attained stature.

- **Traversal:** NODE secular_trend_height + NODE socioeconomic_gradient_height ('in the Netherlands in 2009 - the world's tallest population, at its plateau - height was STILL correlated with parental education')
- **structural_confidence:** 0.714
- **Note:** Both clauses predicted, including the counterintuitive one: secular gain does not abolish the SES gradient.

### L11

**P50** · **CORRECT_PREDICTION** · `10.1210/clinem/dgaf533` · 2026-02-01

> Exome sequencing of SGA children with persistent short stature yields a monogenic/CNV diagnosis in ~18%, half of them copy-number variants — failure of catch-up growth is frequently a genetic skeletal or syndromic diagnosis rather than idiopathic.

- **Traversal:** NODE idiopathic_short_stature: 'not a disease but the residual category... its progressive dissolution is one of the strongest arguments that the layer works... repeatedly re-partitioned by sequencing'; NODE de_novo_variant_growth; NODE small_for_gestational_age
- **structural_confidence:** 0.214
- **Note:** A structural prediction about diagnostic yield, confirmed at ~18%. Node sc 0.214 - the lowest of any node carrying a hit.

**P51** · **CORRECT_PREDICTION** · `10.1038/s41431-026-02124-8` · 2026-05-02

> Mesomelic dysplasia Savarirayan-type is caused by ID4 misexpression through TAD disruption and limb-enhancer adoption — a non-coding structural mechanism, not a coding lesion.

- **Traversal:** NODE zrs_enhancer: 'kept in this layer as the atlas's worked example that a skeletal patterning decision can be made by a DISTANT NON-CODING element whose disruption produces a purely limb-restricted phenotype'
- **structural_confidence:** n/a
- **Note:** Mechanism class (long-range enhancer misregulation -> limb-restricted dysplasia) is explicitly held as the atlas's exemplar. ID4/6p22.3 is a new instance.

**P52** · CORRECTLY_OUTSIDE · `10.1002/ajmg.a.70243` · 2026-07-06

> Biallelic loss-of-function in MIMS1 (FAM210A) causes a new spondyloepimetaphyseal dysplasia with short stature, tracheal stenosis and ectodermal features.

- **Traversal:** 'mims1'/'fam210' -> 0 nodes; NODE spondyloepiphyseal_dysplasia exists as the phenotype class
- **structural_confidence:** 0.795
- **Note:** Novel-gene discovery is not anticipatable from a graph. Correct 'no coverage'.

**P53** · **SILENTLY_ABSENT** · `10.1038/s41431-026-02176-w` · 2026-07-07

> C-terminal frameshift variants in the last exon of FGFR1, producing a 164-aa elongation tail, cause fully penetrant multiple epiphyseal dysplasia with mild short stature — an FGFR1 gain-of-tail mechanism distinct from classical FGFR3 dysplasias.

- **Traversal:** NODES multiple_epiphyseal_dysplasia(L11, gene list COMP/COL9A2/COL9A3/SLC26A2/MATN3/CANT1 - all matrix), fgfr1_receptor(L3). NO edge between them; e00136 fgfr1_receptor-correlates_with(unknown)->fgfr3_receptor is fgfr1's ONLY disease-adjacent edge and it is unusable
- **structural_confidence:** 0.795
- **Note:** The atlas frames MED as 'the mild end of the same matrix-proteostasis continuum' - a receptor-tyrosine-kinase cause is not merely unlinked, it is off-frame. Both nodes present, zero connection.

**P54** · **CORRECT_PREDICTION** · `10.3389/fendo.2026.1830126` · 2026-07-07

> In Turner syndrome, karyotype class (45,X monosomy vs mosaic vs structural X abnormality) associates with clinical phenotype and with GH response, and the height SDS gain from GH is front-loaded into the first year.

- **Traversal:** NODE turner_syndrome (berry2025: 928,605-person biobank separating X vs Y dosage, +3.1 cm per Y over inactive X); e01014 shox_gene-required_for(+)->turner_syndrome
- **structural_confidence:** 0.721
- **Note:** Karyotype-dosage->phenotype gradient is quantified in-node. The front-loaded first-year GH gain is NOT in the graph (no time-course on e00726).

**P55** · **SILENTLY_ABSENT** · `10.1016/j.gim.2026.102666` · 2026-07-23

> Vosoritide started before age 3 in achondroplasia improves foramen magnum growth relative to untreated ACH reference curves — a CNP-pathway agonist acts on a synchondrosis-derived, non-long-bone skeletal site.

- **Traversal:** NODES vosoritide(L12), npr2_receptor(L3), cranial_base_synchondrosis(L9, 'bidirectional growth plates... the principal contributor to postnatal cranial base lengthening'), achondroplasia(L11). npr2_receptor has 24 edges, NONE to any non-long-bone growth site
- **structural_confidence:** 0.269
- **Note:** The CNP axis in this graph terminates at growth_velocity_longitudinal. Foramen magnum stenosis is a synchondrosis phenotype and the synchondrosis node is present, unconnected to any signalling layer (its only 2 edges are correlates_with/precedes, both unusable).

### L12

**P56** · **SILENTLY_ABSENT** · `10.1210/jendso/bvag008` · 2026-02-20

> Vosoritide increases spinal canal width and blunts the natural increase in thoracolumbar kyphosis angle in achondroplasia — the CNP agonist changes vertebral/spinal morphology, not just long-bone length.

- **Traversal:** NODES vosoritide(L12), vertebral_growth_plate(L1), scoliosis_vertebral_growth(L6), site_specific_growth_rate(L1). vertebral_growth_plate has 5 inbound edges - from mechanics and proportion only, none from any signalling or pharmacology node
- **structural_confidence:** 0.888
- **Note:** Same defect as P55 at a second site. The atlas effectively has ONE growth plate for pharmacological purposes.

**P57** · **CORRECT_PREDICTION** · `10.1016/j.aed.2026.04.004` · 2026-04-18

> Adding an aromatase inhibitor to GH during puberty in ACAN-related short stature (which has advanced bone age and early fusion) yields adult height well above pretreatment prediction — oestrogen blockade buys physeal time in an aggrecan-deficient plate.

- **Traversal:** e00737 aromatase_inhibitor_anastrozole-activates(+)->adult_height_attainment (usable); e00735 letrozole-inhibits(-)->bone_age; e00228 acan_related_short_stature-precedes(+)->growth_cessation; NODE acan_related_short_stature ('bone age ADVANCED by a median 1.3 y... growth stops early')
- **structural_confidence:** 0.849
- **Note:** Clean composite: a plate that fuses early + an agent that delays fusion => height gain. Atlas correctly carries the cautionary magnitude too (zegarra2024: 3-year gain only +1.3 cm), which the case report's +14 cm-vs-PAH does not respect.

**P58** · CORRECTLY_OUTSIDE · `10.1210/jendso/bvag123` · 2026-05-30

> Exogenous testosterone in constitutional delay transiently suppresses LH, FSH and INSL3, whereas letrozole does not — the two CDGP treatments differ in their gonadotropin-axis footprint despite both advancing puberty.

- **Traversal:** 'insl3' -> 0 nodes; the proposition has no stature endpoint
- **structural_confidence:** n/a
- **Note:** Gonadal-axis pharmacodynamics without a growth readout is outside 'human longitudinal skeletal growth'.

**P59** · **CORRECT_PREDICTION** · `10.1159/000553101` · 2026-06-25

> Pooled across REAL 3/4/6, once-weekly somapacitan matches daily GH on height velocity at 52 and 156 weeks, including across puberty onset — weekly GH exposure profile does not cost growth.

- **Traversal:** NODE transcon_growth_hormone (briGHt 10.66 vs 9.75 cm/yr weekly vs daily; shen2026 16 RCTs/2435 children); NODE gh_pulse_pattern_hypothesis; nct02413138 negative control in-node
- **structural_confidence:** 0.767
- **Note:** Weekly-equals-daily predicted and confirmed at 52 AND 156 weeks.

**P60** · **SILENTLY_ABSENT** · `10.1007/s40618-026-02986-1` · 2026-07-29

> Long-acting GH (somatrogon) raises IGF-I SDS while leaving adrenal (ACTH, cortisol) and thyroid (TSH, FT4, FT3) axes stable — the weekly formulation does not unmask other pituitary deficiencies.

- **Traversal:** NODES recombinant_human_gh(L12), transcon_growth_hormone(L12), thyroid_hormone_t3(L4), glucocorticoid_cortisol(L4), dio2_deiodinase(L4). NO edge from any GH intervention to any non-GH endocrine axis
- **structural_confidence:** 0.882
- **Note:** rhGH's 5 outbound edges are all within the GH/IGF axis. The graph cannot express an off-axis endocrine consequence of a growth drug, though every endpoint is a well-built L4 node.

### L13

**P61** · **SILENTLY_ABSENT** · `10.1080/03014460.2026.2627918` · 2026-03-26

> Adding a fourth "post-growth" random effect to SITAR improves fit for BOTH height and weight (height residual SD 0.67 vs 0.74 cm) — the standard three-parameter SITAR under-describes post-pubertal height velocity.

- **Traversal:** NODES sitar_model(L9, sc 0.226, 'three random effects... residual SD 0.79 cm'), peak_height_velocity(L7), menarche_growth_remaining(L7, post-menarcheal growth SD 4.9 cm on a mean of 8.0, range 0.2-31.1 cm)
- **structural_confidence:** 0.226
- **Note:** The atlas holds enormous measured between-individual variance in POST-pubertal growth (menarche_growth_remaining) and, in a different layer, a growth model with no post-pubertal random effect - and never joins them. sitar_model's single edge is correlates_with, unusable.

**P62** · **CORRECT_PREDICTION** · `10.1016/j.cdnut.2026.107714` · 2026-05-13

> WHO and CDC growth references classify the SAME children's height status discordantly, so measured stunting prevalence is reference-dependent, not a property of the population.

- **Traversal:** NODE who_growth_standard ('PRESCRIPTIVE rather than descriptive') vs NODE cdc_growth_reference ('a DESCRIPTIVE reference'); de2011 cited in BOTH: 'WHO and US growth velocity references differ, most at the lower percentiles'
- **structural_confidence:** 0.226
- **Note:** The atlas states the design difference and the empirical divergence. Reference-dependence of stunting prevalence follows directly.

**P63** · **CORRECT_PREDICTION** · `10.1136/bmjph-2025-004567` · 2026-06-23

> Linear growth faltering at 24-30 months (stunting, or short for genetic potential) flags children who fail neurodevelopmental screening — height is an indicator of a non-skeletal outcome.

- **Traversal:** NODE stunting (victora2008: 'undernutrition indices were strongly associated with shorter adult height, LESS SCHOOLING and lower income'); NODE who_growth_standard; NODE mid_parental_target_height (short-for-genetic-potential)
- **structural_confidence:** 0.780
- **Note:** Height-as-indicator-of-non-skeletal-outcome is already an atlas claim.

**P64** · **SILENTLY_ABSENT** · `10.1007/s00256-026-05297-x` · 2026-07-11

> Combining hand-wrist AND knee radiographs in a dual-input deep model gives bone-age MAE of 3.77 months in LATE adolescence (13-19 y), the range where hand-only bone age saturates.

- **Traversal:** NODE automated_bone_age_ai(L13/L7, hand-wrist only: 'reconstructs the borders of fifteen HAND-WRIST bones'); NODE bone_age_measurement_error holds tewattanarat2026: 'the largest method disagreement ABOVE 180 MONTHS of age'; NODES sanders_staging, risser_sign, mri_physeal_closure_staging (non-hand sites)
- **structural_confidence:** 0.226
- **Note:** The atlas holds the premise (hand bone age degrades after 15 y) AND holds four non-hand maturity indicators, and never infers that a second skeletal site is required in late adolescence. automated_bone_age_ai has exactly one edge and it is unusable.


---

## 7. What this run generated for the next sweep

Logged, not applied. See `query/falsification_corrections.md` for the full defect register
and the reasoning behind applying zero graph edits.

1. **Cross-layer seam audit** — 14 of 16 silent absences are cross-layer. The build has no
   pass that asks, for each node, which node in another layer it changes.
2. **L12 is terminal** — no growth intervention has an edge to any consequence outside the
   axis it targets.
3. **Site-specific plates are unwired** — 8 named plate/synchondrosis nodes receive no
   signalling or pharmacology edge.
4. **L8 nodes are unwired to their phenotypes** — `structural_confidence` 0.27–0.38 in a
   layer graded A throughout.
5. **`coverage.md` is stale** — 612/764 stated vs 614/1181 actual; L8 "3 nodes" vs 39; and
   its layer warnings do not track predictive performance.
6. **The rare-variant height fraction should be a spread, not a point estimate** (P42).
7. **Non-ingestion checks must be re-run at scoring time** against `graph.json.refs`, not
   only at sweep time against the bibliography (§1.1).

---

## 8. The honest summary

The atlas predicts findings it has never seen **about half the time overall, and between
0% and 100% depending on where you ask** — and the variation is not random. It is
mechanistic exactly where it has signed within-layer edges (mineralisation, whole-organism
growth, the signalling core) and it is a well-organised bibliography exactly where it has
graded nodes with no outbound edges (genetics, endocrine, pharmacology).

The 16 silent absences are not 16 unrelated misses. They are one defect counted 16 times:
**the layers were built and the seams were not.** That is a fixable defect, and it is more
useful to know than the headline number.

---

## 9. Retrospective re-score against the PRE-PHASE-3 graph

FINAL-01 item B. The Phase 6/8 delta reported in `falsification_corrections.md` is zero
and near-tautological — nothing structural changed between the baseline commit and now.
The informative test is the one never run: **did Phase 3, the largest single block of
work in the project, improve predictive power or only coverage?**

### Method

The graph at `4d9927c` — the commit immediately before `193b79b atlas(L*): phase 3
dispatch` — is the pre-Phase-3 state. **Neither graph was modified.**

| | pre-Phase-3 (`4d9927c`) | at baseline (`6c916e3`) |
|---|---:|---:|
| node files | 612 (34 stubs) | 614 (0 stubs) |
| edges | **764** | **1,181** |

The re-score is mechanical rather than re-judged, and that is deliberate: re-reading 63
papers against a second graph invites the second reading to be kinder. §6 records, for
every item, the specific nodes and edges its verdict rested on. Each of those object ids
was checked for existence at `4d9927c`. An item is re-scored as still CORRECT only if the
objects that produced its verdict were present then.

**Direction of the bound, stated:** an item whose recorded objects are missing might
still have been answerable by a route the record does not name, so this method can
*understate* the old score. It cannot overstate it. In the event, nothing was
understated — see below.

### Result: 32 / 50 = 64.0%. Identical. Zero delta.

Nine of the 32 CORRECT items used at least one object created during or after Phase 3:

| item | missing pre-Phase-3 | did the verdict depend on it? |
|---|---|---|
| P04 | `e01046` | No — verdict rests on NODE `bone_collar_formation` |
| P07 | `e01072` | No — NODE `chondrocyte_to_osteoblast_transdifferentiation` plus `e00321` (present) |
| P19 | `e00983` | No — `e00207` (present, the A-grade human edge the note names) |
| P22 | `e01113` | No — NODEs `pappa2_deficiency`, `pappa2_protease` |
| P30 | `e00879` | Partly — the *derived* form is lost, NODE `disuse_growth_effect` still carries the direction |
| P40 | `common_vs_rare_pathway_divergence` (node) | No — the prediction is the rare/Mendelian overlap claim on NODE `rare_variant_height` |
| P45 | `e00810` | No — `e00214` (present) plus NODE `vosoritide` |
| P46 | `e01140` | No — NODE `glucocorticoid_sparing_strategy` frames the exact dissociation |
| P54 | `e01014` | No — NODE `turner_syndrome` carries the quantified karyotype-dosage gradient |

One further check: the only correction landing between `4d9927c` and the baseline that
could have flipped a verdict is the Phase 2d CNP-effector break (CORR-003). No held-out
proposition touches PKG-II, cGKI or the cGMP effector step. The one item that turns on a
correction — **P25**, the strongest hit in the run — turns on **CORR-001**, which landed
at `bc6af59`, *before* the pre-Phase-3 snapshot. It scored CORRECT then too.

### What that means, and it is not a comfortable result

**Phase 3 added 417 edges — a 55% increase — inverted the cross-layer/intra-layer ratio
from 1.3:1 to 0.65:1, and populated every empty seam. The predictive score did not move
by a single item.**

The reason is visible in the composition of the 32 correct predictions:

| how the verdict was reached | items |
|---|---:|
| **node read only — no traversal at all** | **18** |
| node read plus edge traversal | 13 |
| **edge traversal alone** | **1** |

**Fifty-six per cent of this atlas's correct predictions come from what a node *says*.
Exactly one of thirty-two came from what the graph could *derive*.**

That reframes the earlier structural result. The cross-layer inversion was real and it
was worth doing — it is what makes context-filtered traversal and the fragility analysis
possible at all, and §3 of this report shows the *remaining* failures are cross-layer.
But on the evidence of this test, **the edges are not yet where the predictive power
lives.** The atlas predicts because its nodes are carefully written, not because its
graph reasons.

Two readings are available and this test does not separate them:

1. **The held-out set is biased toward node-reads.** A proposition extracted from a
   paper abstract is usually a single mechanistic claim, and single claims are what
   nodes hold. A question requiring a two-step inference would exercise the edges — and
   the benchmark's Type 2/3 questions do — but held-out *papers* mostly do not pose
   those.
2. **The graph genuinely cannot derive much yet.** 191 weakly-connected components in
   the answerable subgraph (`audit/fragility.md`) is consistent with this.

The discriminating test is stated rather than run: score a held-out set of
**multi-step** propositions — findings that connect two facts the atlas holds
separately — and see whether the edge-derived hit rate rises. That is the measurement
that would tell you whether Phase 3 bought predictive power that this test could not see.

Raw per-item data: `query/falsification_rescore_prephase3.json`.
