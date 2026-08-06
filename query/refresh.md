# Refresh protocol — the atlas decays

An atlas built at one moment is a snapshot of a moving literature. This file specifies when
a claim stops being current, which open questions would force a re-sweep if answered, and
what events should trigger one.

---

## 1. `last_verified` decay

Every node carries `last_verified`. The rule:

| Grade | Re-check before citing as current |
|---|---|
| **A / B** | older than **12 months** |
| C / D | older than 24 months |
| **X** | every re-sweep — an X-grade claim exists precisely because the primary could not be traced, and a newly published primary would resolve it |
| E | on any change to the adjacent node it was inferred from |

Check with:

```bash
python3 - <<'EOF'
import json, datetime
g = json.load(open('query/graph.json'))
cut = (datetime.date.today() - datetime.timedelta(days=365)).isoformat()
stale = [n for n in g['nodes'].values()
         if not n['stub'] and n.get('confidence') in ('A','B')
         and str(n.get('last_verified','')) < cut]
print(f"A/B nodes needing re-verification: {len(stale)}")
for n in stale[:20]: print(' ', n['id'], n['last_verified'])
EOF
```

Re-verification is not re-reading the node. It is re-running `verify_refs.py` on its
references, checking for retractions, and searching for a primary published since
`last_verified` that would change the grade.

---

## 2. Watch list — gaps whose closure forces a re-sweep

These are ranked by **blast radius**, not by tractability. Closing any one invalidates or
reframes a large block of reasoning at once, so each needs a targeted re-sweep rather than a
node edit.

| Gap | If answered | Re-sweep required |
|---|---|---|
| **Growth-plate tissue drug concentration** (`g_l12b_002`, `g_mr002_h2`) | A single measured plate concentration would reframe **most of L12 at once** — every dose-selection rationale currently rests on plasma as an unvalidated surrogate. It also discriminates H2 from H1/H3 for the CNP exposure question. | **L12 entire, plus the CNP nodes in L3** |
| **Human growth-plate spatial transcriptomics** (`g_l13data_001`) | Would close ~10 zonal gaps simultaneously — human zonal PDE map, zonal receptor expression, the oxygen-responsive gradient. These are currently recorded as separate unknowns but are **one missing measurement counted several times**. | **L1, L3, L13 zonal claims** |
| **SOC-triggers-stemness causality** (`g_l2stem_003`) | The tools already exist (axitinib at P18, Prx-Cre:GnasR201H); only a readout is missing. A positive or negative result changes whether L2's central hypothesis is mechanism or coincidence. | **L2 entire, L0→L2 edges, L7 fusion models** |
| **Height GWAS variance partition** (`g_l8gwas_001`) | Would tell us what fraction of stature variance actually acts through the growth plate — the premise of a plate-centred atlas. A low fraction would mean L3–L7 explain a minority of height variance. | **Atlas-wide centre of gravity** |
| **Human physeal stress-growth coefficient** (`g_l6mech_*`) | Every clinical application of Hueter-Volkmann currently multiplies an unmeasured human stress by a quadruped coefficient. | **L6 entire, plus L11 Blount/scoliosis** |
| **Infigratinib potency vs G380R** (`g_mr002_allele`) | All FGFR3-inhibitor potency data are on kinase-domain alleles; achondroplasia is transmembrane. | **L12 FGFR3 nodes, L11 FGFR3 allelic series** |
| **CNP-analogue final adult height** (`g_l12pharm_001`) | Converts a surrogate endpoint into a real one, or shows the surrogate fails. Extension trials are running, so this **will** resolve. | **L12 entire, `docs/surrogate_validity.md`** |

---

## 3. Trigger conditions for an unscheduled re-sweep

Any of these should start a targeted re-sweep without waiting for the decay clock:

1. **A retraction or expression of concern on a load-bearing reference.**
   Run `python3 atlas/tools/verify_refs.py` — it flags retraction-related publication types.
   Then trace the blast radius per `audit/corrections.md` and classify the reference as
   `observation_stands` / `interpretation_superseded` / `both_invalid`. **Never discard a
   measurement solely because its published explanation failed** — that is the standing
   policy from the ANKH correction.

2. **A phase 3 readout in any L12 programme.** Especially navepegritide's pivotal trial and
   any final-height data. These convert D-grade surrogate reasoning into A-grade outcome data.

3. **A new human genetic model** — a novel monogenic stature locus, or a large-scale rare
   variant analysis. L8 is designed as the confidence-upgrade engine; new human dosage
   evidence is exactly what upgrades a mechanistic node from C to B.

4. **A new growth-plate atlas dataset.** Re-run the GEO census
   (`atlas/tools/` recipes in `dataset_inventory.csv`) and check `could_close_gap` against
   the current gap register. A new human zone-resolved dataset is the single highest-value
   event for this atlas.

5. **Any published growth-plate tissue concentration for any compound.** This converts
   `g_l12b_002` from an unasked question into an answered one and reframes L12.

---

## 4. Re-sweep procedure

1. `git pull`, then `python3 atlas/tools/validate.py` — establish a clean baseline.
2. Run the targeted sweep against the affected layer using `atlas/tools/SUBAGENT_BRIEF.md`.
3. Merge shards, run `fix_citations.py`, re-run `grade_audit.py` — new references may
   **upgrade** grades, and every upgrade must be logged in `audit/confidence_upgrades.md`
   under the propositional-replication rule (a second reference counts only if it tests the
   **same proposition** by an independent route).
4. If a mechanism changed, open a `CORR-00N` entry in `audit/corrections.md` and trace the
   blast radius across nodes, edges, gaps **and quantitative rows** — prose is not the only
   place a dead mechanism hides.
5. Recompile: `python3 atlas/tools/compile_query.py`.
6. Re-run the benchmark. A correction that lets the superseded version resurface is a
   protocol failure, not a content failure.

---

## 5. What does not decay

The **gaps and their search logs** are timestamped evidence of a null at a moment. They do
not become wrong — they become *dated*. A search log from 2026-08-05 remains a true record
that the query returned nothing on that date, which is why the exact query string is stored.
Re-running it is cheap; re-deriving the gap is not.


---

## 6. Cadence — activated 2026-08-06 (FINAL-01 item J)

The protocol existed and was not running. It runs now, on this schedule:

| axis | tool | cadence | why that interval |
|---|---|---|---|
| **source standing** — retractions, withdrawals, expressions of concern, errata | `atlas/tools/standing.py` | **quarterly**, and before any release | The measured event rate is ~3.4 % of the bibliography carrying a post-publication notice. A retraction is the one defect that gets *worse* with time and is invisible to every other gate. |
| reference resolution / metadata drift | `atlas/tools/verify_refs.py` | **twice yearly**, and before any release | Slower-moving: metadata drift is rare and non-silent. |
| `last_verified` decay on A/B nodes | the §1 snippet | **quarterly**, acting on nodes >12 months | See §1. |
| X-grade claims | every re-sweep | unchanged | An X exists because the primary could not be traced; a new primary resolves it. |
| watch list | §2 | on any trigger in §3 | unchanged |
| **chokepoints** | `atlas/tools/fragility.py` | **on any merge that adds or removes edges** | A new bridge edge is a new single point of failure and should not appear silently. |

Each cycle writes `query/refresh_cycle_NNN.json` so the decay rate itself becomes a
measured quantity rather than an assumption.

## 7. Cycle 001 — 2026-08-06, and it measured the wrong axis first

**`last_verified` decay is not measurable on a build this young.** 341 A/B nodes, maximum
`last_verified` age **1 day**, **0 stale**. Every node was verified during the build, so
the 12-month rule has nothing to act on and will not for a year. Recording a "0 stale, all
clear" would be true and worthless.

**What had actually decayed was source standing, and it was decaying the whole time.**

| | count | of 1,009 indexed refs |
|---|---:|---:|
| **FATAL** — retraction / withdrawal | **1** | 0.1 % |
| SERIOUS — expression of concern | 0 | 0 % |
| **CHECK** — published correction or erratum | **33** | **3.3 %** |
| OK | 973 | 96.4 % |
| no identifier (accessions, labels, registries — **uncheckable**, not clean) | 44 | — |

**3.4 % of this bibliography carries a post-publication notice, and the atlas had looked
at none of them before today.** The one FATAL is `wu2013` (CORR-004). The 33 CHECK
entries are new: 21 of them supply quantitative rows, and none of their notice bodies is
retrievable through the open API — they are escalated in
`atlas/sources/access_queue.md` and flagged `has_published_correction: true` with
`correction_checked: false` in the bibliography.

Worst cases by dependency: `bethlehem2022` (13 quant rows), `smith1994` (8, and it is the
ESR1-null case on which the whole L7 estrogen argument rests), `ogawa2025` (7),
`karlberg1995` (6), `wilson2021` (5 — and the corrigendum is on the growth-plate
morphometric parameters the atlas quotes), `savarirayan2020` (5 — the vosoritide phase 3).

### The lesson for the cadence

The first cycle measured a decay rate of **zero** on the axis the protocol was written
around, and **3.4 %** on an axis it did not have. `last_verified` tracks *when the atlas
last looked*. It does not track *whether the world moved*. Those are different clocks and
only the second one was running.

**X-grade nodes re-checked this cycle** (`mecasermin_rinfabate`,
`telomere_attrition_chondrocyte`): both still X; their references are standing; no primary
published since `last_verified` resolves either.

Raw: `query/refresh_cycle_001.json`, `atlas/sources/standing_report.yaml`.
