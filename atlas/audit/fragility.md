# Fragility — where would this map break?

`python3 atlas/tools/fragility.py --json query/fragility.json`

Convergence analysis asks *where does causal information concentrate*. This asks *where
would this map break*, and it is the question that decides where verification effort
belongs. A node with 40 inbound edges is important. A node with two inbound edges that
is the sole route between two subsystems is **fragile**. They are not the same property
and the atlas had never measured the second one.

The analysis exists because CORR-004 found a **withdrawn** paper carrying what the atlas
itself called *"the only demonstrated molecular entry point from the environment layer
into a local signalling node"* — and it was found by accident, during a retraction
check, rather than by looking.

---

## 0. The positive control, and the premise it corrects

The control was: **e01055 must appear in the bridge set**, or the implementation is
wrong. Run against the pre-correction graph (`9c80db7`, the commit before CORR-004):

| graph | e01055 a bridge? |
|---|---|
| **structural** — all 1,181 edges | **No** |
| **answerable** — the 777 `traversal_usable` edges | **Yes** |

Both answers are correct, and the difference between them is the finding.

**The L10–L3 seam was never topologically unique.** Eight edges connect L10 and L3, and
`klotho_beta_cofactor` had a second inbound edge (`e01057`) throughout. Removing e01055
disconnected nothing structural.

**What was unique was its position in the graph that can carry an answer.** Before
CORR-004, e01055 was `activates` / grade C / `traversal_usable: true`, and e01057 was
`hypothesized_link` / speculative / unusable. So in the *answerable* graph e01055 was
the sole inbound edge to that node, and its loss orphaned the node completely.

So the premise "a single withdrawn reference was carrying the only L10→L3 seam, and its
removal disconnected a layer pair" is **half right, and the correction matters**: the
seam was not unique in the graph, it was unique in the subgraph that answers questions.
A fragility analysis run only on the full edge set would have missed it entirely. Both
graphs are therefore computed and reported, always.

## 1. What was measured

| | structural (1,181 edges) | answerable (777 edges) |
|---|---:|---:|
| weakly-connected components | 32 | **191** |
| bridge / sole-seam edges | 205 | 184 |
| articulation nodes | 104 | 109 |
| layer pairs connected | 51 | 45 |
| — sole-edge seams | 6 | 7 |
| — single-source seams | 3 | 4 |

**The answerable graph is in 191 pieces.** That is the number to sit with. Restricting to
edges that can carry a directional answer shatters a graph that looks like 32 components
into 191, because `precedes`, `binds`, `correlates_with` and every `hypothesized_link` —
403 edges — are correctly excluded from traversal. Much of what looks connected is
connected by relations that cannot propagate a perturbation.

`pairs_destroyed` below is the number of ordered reachable (s,t) pairs lost when the edge
is removed. For a true bridge it is exact: |ancestors(u)+u| × |descendants(v)+v|.

## 2. The top 20 by reachable pairs destroyed — **verified by hand**

Every reference was re-resolved against the live Europe PMC record, checked for
retraction and correction notices, and its abstract read against what the edge asserts.
**Verification is abstract-level unless stated**; a claim buried in a methods section
behind a paywall cannot be checked this way and is marked as such.

**6 of 24 objects checked carry a citation defect — 25%. Two of them were graded A.**

| # | edge | pairs | conf | verdict |
|---|---|---:|---|---|
| 1 | `e00268` mek1_erk_chondrocyte → noonan_syndrome | 17,136 | B | **SUPPORTED INDIRECTLY.** `jirova2026` is a genotyped clinical cohort establishing that the causal variants are RAS-MAPK genes; it does not measure MEK/ERK flux. The edge's own context already says MAPK flux "has been measured in patient-derived non-cartilage cells only, never in human growth plate". Left at B with the limitation standing. |
| 2 | `e00788` noonan_syndrome → mek1_erk_chondrocyte | 17,136 | B | **DEFECT — contradicts its own source.** Asserted *"birth length is usually normal and growth failure is postnatal"*. `jirova2026`, the paper it cites, reports birth length **−1.23 SDS [−1.74; −0.57]** in that cohort. Corrected to the measured value. This is the only case in the set where the edge contradicted its paper rather than merely overreaching. |
| 3 | `e00538` aggrecan_acan → fixed_charge_density | 326 | C | STANDS. `lesperance1992` reports calf articular FCD −0.28 ± 0.03 M by sodium NMR; the −0.19 to −0.35 M range is consistent with the per-specimen figures. |
| 4 | `e00485` calcium_homeostasis → parathyroid_hormone | 228 | **A** | **DEFECT — wrong paper entirely.** Asserted *"CASR-mediated suppression of PTH secretion within minutes of a rise in ionised calcium"*, cited to `sabbagh2005` = *"Hypophosphatemia leads to rickets by impairing caspase-mediated apoptosis of hypertrophic chondrocytes"*. Nothing about CaSR, PTH, or secretion kinetics. Re-sourced to `garrett1995` (human parathyroid calcium receptor cloning and functional expression) and `brown1993`; the unsupported "within minutes" clause **deleted rather than re-sourced**; grade **A → B**. |
| 5 | `e00685` intrauterine_growth_restriction → igf1_systemic | 224 | B | **PARTIAL — evidence targets the wrong endpoint.** The edge's target is systemic IGF-1; the cited magnitude is a 7.1-fold relative risk of *short final stature* (`karlberg1995`, n=3,650). Correct paper, real number, but it evidences a stature outcome and not IGF-1 suppression. Recorded; `karlberg1995` also carries an erratum (Pediatr Res 1996;39(1):175) whose content is not retrievable through the API. |
| 6 | `e00073` chondrocyte_to_osteoblast_transdifferentiation → cxcl12_abundant_reticular_cell | 193 | C | STANDS at abstract level. `mizuhashi2018` does the PTHrP-creER lineage tracing into marrow stroma; the specific "3-month plateau" is not in the abstract. |
| 7 | `e00539` fixed_charge_density → cartilage_osmotic_swelling | 164 | B | STANDS. `zimmerman2021` abstract gives "approximately 1/3 those predicted by ideal Donnan law", 18 bovine + 6 human samples — an exact match to the assertion. |
| 8 | `e00259` thyroid_hormone_t3 → congenital_hypothyroidism | 153 | **A** | **DEFECT — assertion absent from both sources.** Asserted *"untreated congenital hypothyroidism arrests terminal hypertrophy and gives epiphyseal dysgenesis"*. `karimian2024` is a menarche/final-height comparison; `kochar2025` is a treatment-timing anthropometry study. Neither reports histology. Epiphyseal dysgenesis is a real classical finding — it just is not in these papers. Assertion rewritten to what they support; grade **A → B**. `karimian2024` carries an erratum, flagged for hand-check. |
| 9 | `e00419` ghsr_receptor → gh_secretion_pulsatility | 118 | B | **STANDS — exact.** `hornsby2025`: "meal-feeding tripled GH secretion, with burst height augmented and 2 additional bursts of GH per day", ghrelin/GHS-R dependent. |
| 10 | `e00469` estrogen_gh_axis_amplification → gh_secretion_pulsatility | 118 | A | STANDS. `roelfsema2018` design matches exactly — 74 men 57–77, degarelix clamp, anastrozole, E2 add-back, 10-minute overnight sampling. The 60–70% figure is not in the abstract. |
| 11 | `e00683` psychosocial_dwarfism → gh_secretion_pulsatility | 118 | D | STANDS **with its limitation already recorded on the edge**: "the 1967 defining case series was read at title level only, hormone values unverified". No abstract exists for either 1967 paper. |
| 12 | `e00416` ghrh_hormone → growth_hormone | 117 | A | STANDS. `aguiaroliveira2021`: homozygous inactivating GHRHR mutation, severe isolated GHD, proportionate short stature, Itabaianinha kindred. |
| 13 | `e00417` somatostatin_hormone → growth_hormone | 117 | B | **DEFECT — wording overstates the result.** Said octreotide "abolished" GH-stimulated tibial growth. `zapf2002` reports tibial epiphyseal width **−14%** and growth rate **−24%**. Replaced with the measured percentages. |
| 14 | `e00733` octreotide_somatostatin_analog → growth_hormone | 117 | D | STANDS. `burren2023` records somatostatin analogues giving "minimal therapeutic benefit" in X-LAG, consistent with the edge's honest "not quantified in paediatric growth cohorts". |
| 15 | `e00105` furin_cnp_processing → cnp_protein | 115 | C | STANDS. `wu2003`: furin inhibitor blocks proCNP processing; furin-deficient LoVo cells show no conversion. *Note:* the edge's zonal tag is inferred from endpoint localisation on a paper done in HEK293 and SW1353 cells — see §4. |
| 16 | `e00494` hsd11b2_enzyme → glucocorticoid_cortisol | 115 | E | **DEFECT — wrong paper.** Cited `baron1992` = *"Dexamethasone acts locally to inhibit longitudinal bone growth in rabbits"*, which is not about HSD11B2. Re-pointed to the one piece of evidence that bears on the local question: the P8-01 non-detection of HSD11B2 in human growth plate. Grade E unchanged — it was already correct. |
| 17 | `e00657` calcium_intake_growth → calcium_homeostasis | 115 | **A** | **DEFECT — an A-grade signed edge resting on a null.** `hoppe2009` is a 2×2 factorial RCT in 57 boys showing milk minerals had **no** independent effect on IGF-1 or insulin. The sign `+` is not in dispute as physiology, but the reference supports a null on the somatotropic route and nothing measures the positive claim. Magnitude rewritten as the null it is; grade **A → C**. |
| 18 | `e00689` dutch_hunger_winter → intrauterine_growth_restriction | 113 | A | **PARTIAL, already disclosed.** The magnitude (−1.4 cm adult height, 95% CI −2.4 to −0.3, 40 years later) comes from `abera2026`, the **Ethiopian** famine cohort, on an edge whose source node is the Dutch Hunger Winter. The context string says so. Left as is; the transfer is stated, not hidden. |
| 19 | `e00395` ift88_protein → primary_cilium_chondrocyte | 113 | C | STANDS. `haycraft2007` generates the conditional `Ift88` allele and disrupts cilia in limb mesenchyme. |
| 20 | `e01040` de_novo_variant_growth → fgfr3_gene | 113 | B | **STANDS — exact.** `moura2024`: "9 of these variants resulted in a higher activation of the receptor's downstream signaling". |

### The four single-source layer seams, also verified

These are the CORR-004 class by construction: a whole layer-pair connection resting on
one reference.

| seam | edge | ref | verdict |
|---|---|---|---|
| **L0–L6** | `e00601` secondary_ossification_center → physeal_stress_in_vivo | `xie2020` | STANDS. "Mathematical modeling revealed that SOC reduces mechanical stress within the growth plate." |
| **L1–L8** | `e00997` col10a1_gene → hypertrophic_chondrocyte | `yang2025` | STANDS. Abstract confirms the p.W651fsX666 mutation disrupts trimerisation of normal collagen X. |
| **L3–L9** | `e00409` ift80_protein → articular_cartilage | `yuan2015` | STANDS at abstract level. Direction consistent: deletion thickens articular cartilage, so IFT80 inhibits it. |
| **L7–L8** | `e01010` esr1_gene → epiphyseal_fusion | `smith1994` | **STANDS — exact.** "A 28-year-old man… incomplete epiphyseal closure… despite otherwise normal pubertal development." `smith1994` carries an erratum (NEJM 1995;332(2):131) not retrievable through the API — flagged. |

**No retracted or withdrawn source was found among the 24.** Three carry errata whose
content the API does not expose (`karlberg1995`, `karimian2024`, `smith1994`); all three
are recorded as hand-check items rather than assumed harmless.

## 3. What the failures have in common

Six defects, and they are not six kinds of mistake. They are **two**:

**(a) The citation names a real paper that does not contain the claim** — `e00485`,
`e00259`, `e00494`. In every case the paper is *topically adjacent*: hypophosphatemia
and rickets standing in for calcium and PTH; congenital hypothyroidism growth outcomes
standing in for congenital hypothyroidism histology; local dexamethasone action standing
in for the enzyme that inactivates cortisol. **This is the same failure mode as the
propositional-replication rule's Pattern A** — topical adjacency mistaken for evidential
support — appearing on edges rather than on grades, where nothing was checking for it.

**(b) The claim is stronger than the number behind it** — `e00788` (birth length "usually
normal" against a measured −1.23 SDS), `e00417` ("abolished" against −14%), `e00657` (a
signed positive edge whose evidence is a null).

**Two of the six were graded A**, the atlas's highest grade, and the grade was doing no
work: `verify_refs.py` confirmed the references exist and resolve, `validate.py`
confirmed the ref_ids are real, the pmid cross-check confirmed they point at the right
papers — and every one of those gates passed on a citation that does not support its
claim. **Existence, resolution and identity are all mechanically checkable. Support is
not.** That gap is the standing limitation of this atlas's verification stack, and it is
why §2 was done by reading rather than by running something.

## 4. A systematic risk the verification exposed

`e00485`'s context string read *"human parathyroid chief cell; zones resolved in source:
hypertrophic zone"*. A parathyroid chief cell is not in a growth plate zone. The tag came
from the MR-004 context-fill campaign inferring zone from the endpoint nodes'
`localization` records — sound for two cartilage nodes, nonsense for an endocrine one.

Quantified across the graph (`context_filter.py --coverage-report`):

| zone annotation provenance | edges | share |
|---|---:|---:|
| resolved in the cited source | 60 | 5.1% |
| definitional — an endpoint node **is** a zone | 316 | 26.8% |
| **inferred from endpoint localization records** | **261** | **22.1%** |
| → strong (source-resolved + definitional) | 376 | 31.8% |
| explicitly `unknown` | 544 | 46.1% |

**Only 5% of zone annotations come from a paper that measured the zone.** The 22% inferred
tier is where an incoherent tag can hide, and it is now reported separately everywhere
rather than folded into a single 53.9% figure.

## 5. Articulation nodes — the top of the list is not a surprise, and that is the point

`growth_hormone`, `gh_secretion_pulsatility`, `calcium_homeostasis`,
`parathyroid_hormone`, `cnp_protein`, `igf1_systemic`, `thyroid_hormone_t3`,
`primary_cilium_chondrocyte`, `stunting`, `fgfr3_gene`. These are the hubs one would
name from memory, and their fragility is mostly an artefact of the atlas modelling each
axis as a chain through a single canonical node.

The informative entries are the ones with **few references**:
`igf2_hormone` (1 key_ref), `ghsr_receptor` (1), `calcium_homeostasis` (1). A node that
severs the graph and rests on one paper is where the next `verify_refs` surprise will
come from.

## 6. What was done with this

- **6 edges corrected**, each with a `FRAGILITY-VERIFY` note on the edge recording what
  was asserted, what the paper says, and what changed. Two A-grades dropped to B, one to
  C. No grade was raised.
- **Two references added** (`garrett1995`, `brown1993`) to replace a citation that did
  not support its claim. Neither was hand-written; both came from `addref.py`.
- **`query/fragility.json`** is compiled alongside the other query artifacts.
- **The query layer now reports chokepoints.** Any answer whose path crosses a bridge
  edge or a single-source seam says so — see `QUERY.md` §8.2. A user should be told when
  an answer rests on one edge and one paper.

## 7. What this analysis cannot do

- It measures **graph** fragility, not **evidential** fragility. An edge with 40
  citations and an edge with one look identical here unless they also happen to be
  bridges; `n_refs` is reported but not ranked on.
- Verification in §2 is **abstract-level** for the 20 edges whose full text is not open
  access, which is most of them. A claim supported in a methods section cannot be
  confirmed or refuted this way, and "STANDS" means "nothing in the abstract contradicts
  it", not "I have seen the number".
- The `pairs_destroyed` metric assumes a true bridge splits the graph cleanly. For the
  handful of non-splitting candidates it is summed directly, which is exact but slower;
  both paths are in the tool.
- It says nothing about **which** claims matter to a user. A chokepoint carrying 269
  quantitative rows into a corner nobody queries is less urgent than one carrying five
  into the middle of the fusion question, and the tool has no way to know the difference.
