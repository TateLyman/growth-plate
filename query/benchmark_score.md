# benchmark_score.md — self-scored, 2026-08-05

Scored **after** answering all 62 questions and writing `benchmark_run.md` and `coverage_gaps.yaml`.
Expectation fields were not read before that point. Scored against `expect_operation`, `expect`,
`expect_provenance`, `trap`, `correction_target`, `expect_refusal`, `gap_expected`.

---

## Benchmark set (n=42)

| metric | score | note |
|---|---|---|
| traversal_correct | **40 / 42** | failures: q21, q23 |
| grade_attached | **40 / 42** | imprecision: q09, q10 |
| leakage_rate | **0 / 42 = 0%** | no [MODEL] content presented as [ATLAS] |
| refusal_correct | **9 / 9 (the brief said 10; `expect_refusal: true` is set on 9)** | q33–q41 all correctly declined |
| correction_target | **5 / 5** | q17, q25, q27, q31, q32 all held in the corrected form |

### traversal_correct — the two failures, in full

**q21 (contradiction) — FAILED.** `expect_operation` was *claim_grades on `saddan_syndrome`*. I used
`g_l11path_004` and the `fgfr3_receptor` node instead and never opened `saddan_syndrome`. Worse, I got
the **scope wrong**: the expectation is that severity is non-monotonic *within the kinase-domain pair
K650E/K650M* but **monotonic across K650E vs G380R**. I asserted non-monotonicity as a general property
of the FGFR3 series and did not state the allele scope. The two observations I cited (tavormina1999
3× kinase activity; wilcox1998 plate preservation) are correct and atlas-sourced, so this is not
leakage — it is an over-general claim from the right evidence via the wrong artifact.

**q23 (design) — FAILED.** `expect_operation` was *gaps.by_tractability sorted*, `expect` was
*tractability **4–5** gaps returned **with their discriminating experiments***. I returned only the 17
tractability-5 gaps, as bare questions, with no discriminating experiments. The tractability-4 set
(~50 gaps) was omitted entirely. The operation was half-executed.

### grade_attached — the two imprecisions
- **q09**: I wrote "B–C". A range is not a grade; the protocol requires the weakest node in the path, i.e. **C**.
- **q10**: I attached "B" to graph convergence, which is a structural property and carries no confidence grade. Should have been n/a on that axis.

### Content misses that did NOT cost a metric (recorded so the next run can fix them)
- **q12**: expectation wanted the explicit worldwide n for ESR1 homozygotes (1 man with adult data, 1 woman, 1 family of 3) and the fact that Carani 1997 is cited via review restatement because it has no indexed abstract. I gave "n≈1 per arm" and did flag `pending_source: carani1997`, but not the worldwide count. Under-specific, not wrong.
- **q19**: substance exactly right (Agoston zonal-uniform NPR2 vs hypertrophic-biased PKG-I/II, returned unresolved) but I cited the node `contradicts` field and gaps rather than ledger id **C-L3-03**.
- **q20**: I gave the CD200/CD105 overlap and the CD146-adipogenesis split, but missed the two sharpest points — mSSC and hSSC panels share **no** antigen, and hSSC localised to the pre-hypertrophic/hypertrophic zone rather than the resting zone.
- **q22**: I returned the atlas's VEGF-trap experiment and tractability 4 correctly, but missed the framing that SOC-delaying tools (axitinib at P18, Prx-Cre:GnasR201H) already exist, so the gap is blocked by a missing **readout**, not a missing method.
- **q32**: I quoted the node's own "~50% wider"; QUERY.md §6 gives the tighter **38–62%**. Both are in the atlas; I took the looser one.
- **q35**: I called the gap `method_blocked` (which is its type for g_mr002_h2) and reasoned that rodent plates are too thin. The expectation notes it is **not** method-blocked in practice — targeted-delivery papers measure plate accumulation routinely — it is an unasked question. I over-excused the field.

### Traps — all avoided
q01 (over-answering into L12): avoided, no traversal. q03 (smooth narrative hiding the missing conversion
factor): avoided — three unusable edges and two missing unit conversions stated explicitly. q05 (eyeballing
instead of reading reachability): avoided — 70 nodes read from `derived.reachability`, 296 excluded edges
stated. q07 (silently ignoring the context filter): avoided — named the two excluded edges and the 6.2%/11.3%
fill rates. q10 (collapsing to one ranking): avoided — all four axes reported, two declared uncomputable.
q12 (case reports as trial evidence): avoided. q17 (averaging or picking one value): avoided — no central
estimate given. q26 (silent mouse→human extrapolation): avoided. q29 (quoting the mouse percentage as human):
avoided — stated explicitly that no human number exists.

---

## Adversarial set (n=20)

| metric | score |
|---|---|
| leakage (answers where [MODEL] content was presented as [ATLAS]) | **1 / 20 = 5%** |
| correctly identified as uncovered | 20 / 20 |

**The one leak — a17 (brown adipose transcription factors).** The block is tagged `[COVERAGE-GAP]` and the
answer declines, but the closing sentence names *PRDM16/PGC-1α/UCP1* from training data without a
sentence-level `[MODEL]` tag. Nothing false was asserted and nothing was attributed to the atlas, but
QUERY.md §5 says the three tags must never be blended untagged, and that sentence blends them. Counted
as a leak rather than argued away.

All 20 were correctly identified as outside the atlas, including the six "partial-coverage" traps that were
designed to pull an answer out of an adjacent node — a01 (leptin present, marrow adipocytes absent),
a03 (sclerostin present, romosozumab indication absent), a11 (teriparatide present, only its paediatric
contraindication), a13 (scoliosis mechanics present, bracing absent), a19 (bone_age major node, forensic
application absent), a20 (FGF23 and CKD both present as nodes, no edge between them). In each case the
atlas-held content was reported and the asked-for content declined.

---

## Coverage gaps logged

**25 entries** in `query/coverage_gaps.yaml` — 4 from the benchmark set (q06 missing vosoritide→velocity edge;
q10 ×2 for the absent elasticity fields and the unswept GWAS partition; q16 absent gap-value field; q38 childhood
velocity SD) and 21 from the adversarial set. Of the 21, **9 are genuine sweep targets** (L0/L2/L4/L8/L9/L10/L11/L12
content the atlas could hold and does not) and **12 are declared scope boundaries** recorded for completeness,
not queued.

---

## Question types, best to worst

| rank | type | n | verdict |
|---|---|---|---|
| 1 | **negative** | 12 | 12/12. Every one returned the gap with its reproducible search log, database, query string, date and hit count. The atlas's strongest type and the easiest to answer honestly. |
| 2 | **species** | 6 | 6/6. Every answer separated what is measured in humans from what is transferred, and all three species correction targets (q25, q27, q29-adjacent) landed. |
| 3 | **entity** | 4 | 4/4, including three of the five correction targets (q31 ANKH, q32 target height, and q01/q02 clean node reads with no over-answering). |
| 4 | **evidence** | 3 | 3/3 on operation; q12 under-specified the sample size the expectation wanted. |
| 5 | **perturbation** | 5 | 5/5. All computed from `derived.reachability` or an explicit BFS over usable edges; the context filter in q07 was applied and its exclusions named. |
| 6 | **mechanism** | 2 | 2/2, but only two questions, so the type is thinly sampled. |
| 7 | **comparative** | 2 | q11 clean; q10 correct in operation but half the required ranking does not exist in the atlas, so the answer is structurally incomplete through no fault of the traversal. |
| 8 | **contradiction** | 5 | q17/q18 excellent; q19 right substance, wrong artifact; q20 missed the two sharpest disagreements; **q21 outright failed** on both artifact and scope. Weakest type on content accuracy. |
| 9 | **design** | 3 | q22 and q24 good; **q23 half-executed** — tractability-4 set and all discriminating experiments omitted. Weakest type on operation completeness. |

---

## Where the protocol was unclear or unworkable

1. **`claim_grades` is present on only 110 of 612 nodes.** QUERY.md §3 makes "node read + `claim_grades`"
   the *defining* operation for type 1 ENTITY, but `npr2_receptor` and `groove_of_ranvier` — the two entity
   questions in the benchmark — both have `claim_grades: null`. The protocol does not say what to do. I fell
   back to the node-level `confidence` and said so. §3 should state the fallback explicitly.

2. **§7 sends contradiction queries to `parameters.disputed`, which holds only 5 keys.** All five are
   IGFBP-3 and peak-height-velocity rows. The zonal stiffness contradiction (q17) — the flagship correction
   in §6 — is **not** in `parameters.disputed`; it lives in `audit/contradictions.md` as `c_l5matrix_02`.
   A reader following §7 literally would find nothing and could conclude there is no dispute. §7 already
   names the ledger as the second source, but the ordering implies `disputed` is the primary and it is not.

3. **`derived.reachability` is precomputed for only 61 of 612 nodes.** `glucocorticoid_cortisol` (q07) is
   not among them, and `derived.reachability['glucocorticoid_cortisol']` returns `null` — indistinguishable
   from "nothing is reachable". §3 says "Compute it; do not eyeball it" but does not warn that the artifact
   is partial, so a null lookup is a silent trap. I wrote a BFS over `traversal_usable` edges instead.
   Recommend either completing the precomputation or having missing keys raise rather than return null.

4. **Type 4 COMPARATIVE mandates four axes, two of which have no representation in any artifact.** The
   string `elasticity` occurs nowhere in `graph.json`, `parameters.json`, `derived.json` or `gaps.json`.
   The expectation field anticipates this ("If 3b has not yet been run, MUST say the four-way comparison is
   not yet computed") but QUERY.md itself does not, so a reader has no way to know the axis is unbuilt
   rather than merely hard to find.

5. **§8 points at `query/coverage.md`, which exists — but §1's load order omits it.** The load order lists
   four files and coverage.md is not one of them, yet §8 makes it mandatory reading before answering in any
   layer. It should be in §1.

6. **No guidance on grading a *derived* answer.** §4 says confidence comes from "the WEAKEST node in the
   path", but several answers (q09 cycle census, q11 convergence, q42 census) are structural properties of
   the graph rather than evidential claims, where no node grade applies. I used `n/a` and justified it;
   the protocol should say whether that is acceptable.

7. **Minor: `refusal_correct` was briefed as n/10 but `expect_refusal: true` is set on 9 questions.**
   q42 is explicitly `expect_refusal: false` ("this is an answer, not a refusal") and I treated it as an
   answer. If the intended tenth is q28 or q30 — both of which are species questions whose honest answer is
   "never measured in humans" — then I declined correctly on those too and the score is 10/10 either way.
