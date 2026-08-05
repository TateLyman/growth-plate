# QUERY.md — operating instructions for answering from this atlas

You are answering a question about human growth using the Human Growth System Atlas.
This file is the protocol. Follow it in order. It exists because the failure mode of
an atlas like this is not wrong answers — it is **fluent answers that silently blend
atlas content with training data**, which destroys the value of every grade, gap and
correction in the build.

---

## 0. The rule that everything else serves

**Never answer from memory when the atlas contains the entity.**

If you know something about NPR2 and the atlas has an `npr2_receptor` node, the node
wins — including when the node is *less* complete than your training data. The node is
graded, species-tagged and cited; your recollection is none of those things. If your
knowledge contradicts the node, that is a finding to report, not a correction to apply
silently: say so explicitly and flag it as a candidate contradiction.

---

## 1. Load order (do this before reading the question twice)

```bash
query/derived.json     # FIRST — alias table, cycles, convergence, reachability
query/graph.json       # nodes + edges + refs
query/parameters.json  # only for quantitative questions
query/gaps.json        # only for negative-space questions
query/contradictions.json  # contradiction ledger + node contradicts + contradiction gaps
query/coverage.md      # ALWAYS — §8 requires the layer warning BEFORE the answer
```

`derived.json` first because `alias_to_id` decides whether the atlas even *has* the
entity, and because reachability and cycles are precomputed — recomputing them by hand
is where traversal errors get introduced.

## 2. Resolve aliases BEFORE searching

Look the entity up in `derived.alias_to_id` (lowercase key). "GC-B", "NPR-B" and
"guanylyl cyclase B" all resolve to `npr2_receptor`. A grep for the user's exact
wording will miss the node and produce a false coverage gap — which is worse than a
miss, because it sends you to memory.

If the alias table has no entry, the atlas genuinely may not cover it → §7.

## 3. Identify the query type, then execute ITS operation

An answer produced by the wrong operation is wrong even when it sounds right.

| # | Type | Trigger | REQUIRED operation |
|---|---|---|---|
| 1 | **ENTITY** | "what is X" | Node read + `claim_grades` **if present**. Cheapest type — do not over-answer or traverse. |
| 2 | **MECHANISM** | "how does X become Y" | Path trace. Carry **units at every step**. Report where the chain breaks or needs an unmeasured conversion factor. The breaks are the answer. |
| 3 | **PERTURBATION** | "what if X is suppressed at age 11 in a female" | `derived.reachability[X]` with sign products. If context is requested, use **`atlas/tools/context_filter.py`** — NOT a hand-written filter. Three-state semantics are mandatory (see below). **Report annotation coverage with every context-filtered answer.** |
| 4 | **COMPARATIVE** | "does CNP or FGFR3 matter more" | The four-way ranking: velocity elasticity, final-height elasticity, GWAS enrichment, graph convergence. Report **all four and their disagreements**; never collapse to one. **STATUS: only graph convergence is currently computed.** Phase 3b has not run, so the two elasticity axes and the GWAS-enrichment axis do not exist in any artifact. Until they do, the correct answer to a comparative question is: report convergence, and state explicitly that three of the four axes are not yet computed — **do not substitute convergence for the ranking.** |
| 5 | **EVIDENCE** | "how do we know estrogen drives fusion" | `key_refs` + `confidence` + `human_evidence` + `translation_risk`. Distinguish established-in-humans from inferred. |
| 6 | **NEGATIVE** | "what don't we know about the resting zone" | `gaps.json` filtered by layer, **with search logs attached** so the user can see the gap is established, not assumed. |
| 7 | **CONTRADICTION** | "do sources agree on zonal stiffness" | **Check all three**: `contradictions.json` (`ledger_markdown`, `node_contradicts`, `gap_contradictions`) **then** `parameters.disputed` **then** the node's own `contradicts` field. `parameters.disputed` holds only 5 numeric keys — the flagship contradictions (zonal stiffness, CNP zonal partition, competing SSC schemes) are in the ledger, NOT there. Return **the spread and the methodological reason**, never a central estimate. |
| 8 | **DESIGN** | "what would settle this" | `discriminating_experiment` fields, ranked by `tractability`. |
| 9 | **SPECIES** | "does this hold in humans" | `translation_risk` + `human_evidence` + what the human data actually is. **Highest-value type in this domain. Never answer by silent extrapolation.** |

### Grading fallback — `claim_grades` is absent on most nodes

**`claim_grades` is null on 468 of 578 researched nodes (81%).** It was populated only
where a summary demonstrably mixed claims of uneven support. So:

- `claim_grades` present → quote the per-claim grades; the node-level `confidence` is the
  weakest of them.
- `claim_grades` absent → **use the node-level `confidence`, and say the node is graded as a
  whole.** This is not a defect in the answer; it means nobody has yet found divergent
  support within that node. Do not invent per-claim grades.
- **Derived / structural answers** (cycle counts, convergence ranks, reachability sets, "how
  many nodes are X") carry **no confidence grade** — they are properties of the graph, not
  empirical claims. Report them as `[ATLAS-INFERRED]` with `CONFIDENCE: n/a (structural)`
  and state the artifact they came from. Attaching an evidence grade to a graph statistic
  is a category error.
- **Path answers** take the **weakest** grade on the path, and must name which node or edge
  set it.

### Traversal rule (types 2 and 3)

**Only traverse edges with `traversal_usable: true`.** 296 of 764 edges are excluded:
`precedes` (temporal, no sign), `binds` (no direction), `correlates_with` (direction
not inferable from relation type), `hypothesized_link` (speculative). Traversing an
unsigned edge produces a path with **no directional meaning** — the answer will look
computed and mean nothing.

`derived.reachability` is precomputed for **every non-stub node**. Therefore:

- key present, non-empty → that is the answer
- key present, **empty dict** → nothing is reachable through usable signed edges. This is a
  REAL finding: the node is a terminal or its outbound edges are all sign-exempt. Say so.
- key **absent** → the node is a stub, or does not exist. Check the alias table; do not read
  absence as "nothing reachable".

When a path is blocked because the only route runs through unusable edges, **say the graph
cannot answer it directionally.** That is a real result.

### Context filtering — THREE-STATE, never two

Edge context is free text. Zone is annotated on **11.8%** of edges, sex on **11.8%**,
stage on **22.4%**, species on 93.9%. A two-state filter (keep / drop) therefore drops
the overwhelming majority of edges for **missing annotation**, not for context mismatch,
and the residue looks exactly like a small, precise, context-specific answer.

Every context filter classifies each edge into three states:

| state | meaning | action |
|---|---|---|
| **MATCH** | context affirms the requested value | carry |
| **MISMATCH** | context affirms a **different** value on that axis | **exclude** |
| **UNANNOTATED** | the axis is not mentioned at all | **carry, and count** |

**Only MISMATCH excludes.** Collapsing UNANNOTATED into MISMATCH is the bug that shipped
a wrong answer in the first benchmark run (§ below).

Every context-filtered answer must report `annotation_coverage` = MATCH / (MATCH +
UNANNOTATED). **If coverage < 40%, the answer is returned as UNRELIABLE**, with the
figure, and must not be presented as sex- or zone-specific. It is the unfiltered set
minus the few edges that positively contradict the filter — which is a different object.

```bash
python3 atlas/tools/context_filter.py --node glucocorticoid_cortisol --sex female --age 11
python3 atlas/tools/context_filter.py --coverage-report
```

---

## 4. The answer contract

Every substantive answer carries, at minimum:

```
claim          — one sentence, the thing being asserted
confidence     — A/B/C/D/E/X, from the node or the WEAKEST node in the path
species_basis  — which organisms this rests on
path           — node and edge ids traversed (types 2,3) or node id (type 1,5)
refs           — ref_ids, resolvable in graph.refs
gaps_crossed   — any speculative/hypothesized edge or open gap in the path
provenance     — [ATLAS] / [ATLAS-INFERRED] / [MODEL]
```

Three rules that are not optional:

- An answer whose path crosses a `hypothesized_link` edge **says so in the body**, not
  in a footnote.
- An answer resting on a single-lab value (`parameters.single_source_parameters`)
  **says so**.
- An answer whose supporting nodes disagree **presents the disagreement** rather than
  picking a side.

---

## 5. Provenance tags — the load-bearing requirement

Three tags. Never blend them untagged.

| Tag | Meaning | Permitted for |
|---|---|---|
| **[ATLAS]** | Stated in a node or edge. Cite the ids. | Everything. |
| **[ATLAS-INFERRED]** | Derived by traversal or computation over the graph; not stated in any single node. | Everything, **provided it is labelled as derived**. Often the most valuable output — a sign product across four edges is a real prediction. |
| **[MODEL]** | From general knowledge, outside the atlas. | Framing, definitions, well-established background **only**. |

**[MODEL] is NEVER permitted for a mechanistic, quantitative, or species claim.**

If a substantive claim requires [MODEL] content, that is **by definition a coverage
gap**. Do not fill it and move on. Log it:

```yaml
# query/coverage_gaps.yaml
- question: "<the question as asked>"
  missing: "<the entity, edge or value the atlas lacks>"
  layer: "<where it belongs>"
  date: "YYYY-MM-DD"
```

This file is the input queue for the next sweep. **The query layer generates its own
improvement backlog** — a question the atlas cannot answer is data about the atlas.

---

## 6. Known corrections — do not let the superseded version resurface

Training data contains the old versions of these. The atlas contains the corrected
ones. If your recollection disagrees, the atlas is right and your recollection is the
pre-correction literature.

| Topic | Superseded (in training data) | Current (in atlas) |
|---|---|---|
| **ANKH** | ANKH transports pyrophosphate out of the cell | ANKH exports **ATP**; ENPP1 then makes PPi extracellularly. `Enpp1−/−` bone holds <2.5% of WT PPi despite intact *Ank*. See CORR-001. |
| **Zonal stiffness** | A single modulus value per zone | Spans **three orders of magnitude** by method (380 kPa → 416 MPa) and the gradient *direction* disagrees between species. Report the spread. |
| **CNP exposure** | Longer exposure ⇒ more growth (the long-acting prodrug premise) | Within-trial dose-response exists for navepegritide, but vosoritide exposure predicts urine cGMP and **not** growth. Three hypotheses compete (H1/H2/H3); none discriminated. |
| **Target height** | ±8.5 cm is a measured band | **Never measured.** Derived theoretically. Guideline ±1.64 SDS bands are 38–62% wider than the 2024 measured residual SD supports. |
| **Mouse fusion** | "Mice don't fuse" | Too loose. WT mice form ~495 transphyseal bony bridges per tibial plate — bridging happens and is genotype-tunable, it just never completes. |

---

## 7. When the atlas does not know

Say so. Then do exactly this:

1. Check `gaps.json` — if a gap covers it, **return the gap with its search log**.
   "This is a `search_established` gap; here is the exact query that returned nothing"
   is a far better answer than a hedge, and it is *checkable*.
2. If no gap covers it, log a coverage gap (§5) and say the atlas does not cover it.
3. Only then, if the user explicitly asks for your general knowledge, provide it
   under an unmistakable **[MODEL]** tag with a statement that it is unverified
   against the atlas.

"I don't know, and here is the systematic search proving nobody does" is the highest
form of answer this atlas can give. Do not trade it for a fluent paragraph.

---

## 8. Layer context — read before answering

Before answering in any layer, check its `human_evidence_fraction` in
`query/coverage.md`. A user asking a question in a layer that is 80% rodent-derived
should be told that **before** receiving the answer, not after.

### 8.1 Evidence quality is not the same warning as predictive reliability

Phase 7 measured, against 63 held-out post-cutoff papers, how often the graph
anticipates a finding it has never seen. The result overturns the obvious heuristic:

- **L8** — 97% direct human, 89% replicated, 0% translation risk — **20% hit rate**,
  the worst in the atlas.
- **L3** — 20% direct human, 56% high translation risk — **100% hit rate**.

So there are now **two independent warnings to give, and they do not coincide**:

1. **Evidence warning** — is this claim human? Read `human_evidence`, `species_basis`,
   `translation_risk` on the node.
2. **Structural warning** — can anything be *derived* here? Read the layer hit rate in
   `query/coverage.md` and `structural_confidence` on the answer.

A node graded A on impeccable human data can sit in a neighbourhood so weakly connected
that no derived answer from it is trustworthy. That is L8's situation exactly.

**The measured failure mode is cross-layer traversal.** 14 of the 16 findings the graph
should have anticipated and did not required an edge between layers. Any answer whose
chain crosses a layer boundary carries a higher risk of silent incompleteness than its
node grades suggest, and §5's `[ATLAS-INFERRED]` tag must be accompanied by that
statement.
