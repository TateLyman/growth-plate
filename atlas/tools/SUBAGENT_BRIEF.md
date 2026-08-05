# Subagent briefing — literature sweep standard

Read this in full before your first search. It is the contract. Your output is
judged against it, not against how much text you produced.

Working dir is the repo root: `/home/user/growth-plate`. All paths below are relative to it.

---

## 0. The one rule that matters

**Never invent a citation, author, year, PMID, DOI, EC50, or effect size.**

You are structurally prevented from doing so if you use the tooling: `addref.py`
fetches metadata from the live Europe PMC/NCBI record and *refuses* an identifier that
does not resolve. Use it for every reference. Do not hand-write bibliography entries.

If you are unsure whether a number is right: record it with `value_unverified: true`
and add the source to `atlas/sources/access_queue.md`. **A missing number is a gap; a
wrong number is a defect that poisons everything downstream.**

Mouse data must never be stated as human fact. Every node carries `species_basis` and
`translation_risk`. This domain is ~90% murine and mice do not undergo epiphyseal
fusion — species tagging is the difference between an atlas and a folk tale.

---

## 1. How to search

Network is confirmed live. Prefer these over WebSearch for primary literature:

```bash
# Europe PMC — best general search. resultType=core gives abstract, OA status, MeSH.
curl -s --get "https://www.ebi.ac.uk/europepmc/webservices/rest/search" \
  --data-urlencode 'query=(growth plate OR physis) AND "resting zone" AND stem' \
  --data-urlencode 'format=json' --data-urlencode 'pageSize=25' \
  --data-urlencode 'resultType=core' | python3 -m json.tool | head -100

# Restrict to primary research, exclude reviews:
#   query=... AND (PUB_TYPE:"Journal Article" NOT PUB_TYPE:"Review")
# Open-access full text only:  AND OPEN_ACCESS:y   /  in EPMC: AND IN_EPMC:y
# Date filter:                 AND (FIRST_PDATE:[2015-01-01 TO 2026-12-31])

# Full text of an OA paper (methods + figure legends — read these, not just abstracts):
curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1234567/fullTextXML" | head -400

# PubMed ESearch when you need MeSH precision
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=30&term=..."

# ClinicalTrials.gov v2 (L12)
curl -s --get "https://clinicaltrials.gov/api/v2/studies" \
  --data-urlencode 'query.term=vosoritide' --data-urlencode 'pageSize=10'
```

WebFetch is available for regulatory documents (FDA/EMA), dataset portals (GEO), and
anything not indexed. Do not attempt to bypass paywalls — escalate instead (§5).

**Read figures and methods, not just abstracts.** If you only saw the abstract, the
ref type must be `primary_abstract_only`. That is an honest failure mode; pretending
otherwise is not.

**Reviews are an index, not a source.** Use them to *find* primaries and to establish
"what the field believes", then cite the primary. If a claim is repeated everywhere but
you cannot reach a primary, that is a **grade X** claim — a high-value finding. Log it
in `atlas/audit/contradictions.md` §2.

**Find the disagreement.** Do not stop at the first plausible answer. Where two credible
primaries conflict, that conflict is the interesting part: log it in
`audit/contradictions.md` §1 and, if unresolved, open a `contradiction` gap.

---

## 2. Adding references

```bash
python3 atlas/tools/addref.py --pmid 30356214 --tier T1 --type primary \
    --finding "PTHrP+ RZ chondrocytes form columnar clones after SOC formation" \
    --bib <YOUR_SHARD>.yaml
```

- `--bib <YOUR_SHARD>.yaml` is **mandatory** — you have your own bibliography shard so
  parallel agents cannot clobber each other. Use the shard name given in your task.
- `--tier` T1..T6, `--type` from the vocabulary (`primary`, `primary_abstract_only`,
  `regulatory`, `trial_registry`, `patent`, `dataset`, `systematic_review`,
  `meta_analysis`, `review`, `preprint`, ...). See `atlas/schema/vocab.yaml`.
- Non-indexed sources (FDA reviews, GEO accessions) use `--manual` with `--ref-id`,
  `--title`, `--url`/`--accession`; they are auto-flagged `verify_by_hand: true`.
- The script prints the assigned `ref_id`. Use exactly that string in your nodes.

---

## 3. Writing nodes

One YAML file per entity at `atlas/nodes/<LAYER_DIR>/<node_id>.yaml`.
Schema: `atlas/schema/node.schema.yaml`. Vocabulary: `atlas/schema/vocab.yaml`.

Many of your nodes **already exist as stubs** (`stub: true`). Overwrite them in place,
keeping the `id`. Do not create a second file for the same concept under a new name —
check first: `ls atlas/nodes/*/ | grep -i <term>`.

Required on a researched node: `id, name, type, layer, summary, human_evidence,
human_evidence_note, species_basis, translation_risk, translation_risk_reason,
confidence, key_refs, last_verified`. Set `stub: false`.

The `summary` is 3–8 sentences, mechanistic, **no hedging and no filler**. Every clause
should be independently checkable. Bad: "CNP is important for growth and plays a key
role." Good: names the receptor, the zone, the species, the number, and what is *not* known.

`quantitative:` is where the atlas earns its keep. Any number you find goes here with
`parameter, value, unit, conditions, species, source_ref, uncertainty`. Include sample
sizes and CIs; prefer effect sizes over p-values.

Confidence: **A** replicated human direct/interventional · **B** strong animal mechanism
+ human genetic/correlative support · **C** animal only, replicated · **D** single study /
in vitro only / conflicting · **E** flagged inference · **X** untraceable to primary data.

---

## 4. Writing edges and gaps (your own shards — never the canonical files)

- edges → `atlas/edges/shards/<YOUR_SHARD>.edges.yaml`, key `edges:`
- gaps → `atlas/gaps/shards/<YOUR_SHARD>.gaps.yaml`, key `gaps:`
- search logs → `atlas/gaps/shards/<YOUR_SHARD>.search.yaml`, key `searches:`

Number your edges `e00001`... locally; the merge tool renumbers globally.
Schemas: `atlas/schema/edge.schema.yaml`, and for gaps see below.

A `hypothesized_link` edge **must** carry `confidence: speculative` **and** a real
`gap_id`. The validator rejects it otherwise.

### The gap quota is a hard exit criterion

**≥8 gaps for your domain, ≥3 of which are `search_established` or `quantitative_gap`.**

A `search_established` gap is **inadmissible** without a matching `search_log` entry —
the validator enforces this. The log must let a reader re-run your exact query and
reproduce the null:

```yaml
searches:
  - gap_id: g_l1_007
    database: Europe PMC
    exact_query_string: '(growth plate) AND (PDE3A OR PDE9A) AND (human) AND zonal'
    filters: 'resultType=core, no date limit'
    date_run: '2026-08-05'
    hit_count: 3
    screened_count: 3
    reason_none_qualified: >-
      All three are rodent; none reports zonal localization in human tissue.
```

Gap fields: `gap_id, question, type, layer, why_it_matters, what_is_known,
what_is_missing, nearest_evidence, discriminating_experiment, tractability (1-5),
search_log_ref`. Types: `known_unknown, search_established, contradiction, species_gap,
method_blocked, scale_gap, quantitative_gap`.

`question` must be a precise, answerable research question. `discriminating_experiment`
must name the model system, the readout, and the expected result under each competing
hypothesis. "More research is needed" is banned.

Gap ids: prefix with your layer and shard, e.g. `g_l1arch_001`, to avoid collisions.

---

## 5. Paywalls — escalate, do not stall

Append a row to `atlas/sources/access_queue.md`: priority (**P1** blocks a subsystem /
**P2** refines a number / **P3** nice-to-have), full citation, DOI, and the **specific
thing** you need ("Figure 3B: PDE3A zonal IHC in human distal femur" — not "the paper").
Then mark the node `pending_source: <ref_id>`, **drop its confidence one grade**, and
keep going. Never block.

---

## 6. Before you finish — self-check

```bash
python3 atlas/tools/validate.py 2>&1 | tail -30
```

Zero errors attributable to your files. Then confirm: every node non-stub with
`key_refs` resolving to your shard · gap quota met with search logs present · every
number has a unit, a species and a source · no mouse claim written as human fact.

## 7. What to return

Return **file paths and a ≤10-line summary. Never raw content dumps.** Include:
node count, edge count, gap count (and how many are search_established/quantitative),
ref count, the single most surprising finding, and anything you had to leave blocked.
