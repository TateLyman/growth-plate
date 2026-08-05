# Design decisions

Recorded so that later passes (especially Phase 3 integration and Phase 5 redteam)
do not "fix" things that are deliberate.

## D1 — Gene nodes and protein nodes are separate on purpose

`graph.py --duplicates` flags pairs like `npr2_gene`/`npr2_receptor`,
`fgfr3_gene`/`fgfr3_receptor`, `ihh_gene`/`ihh_protein`, `acan_gene`/`aggrecan_acan`,
`stat5b_gene`/`stat5b_tf`, `ghr_gene`/`gh_receptor`, `col2a1_gene`/`collagen_type_ii`,
`pth1r_gene`/`pth1r_receptor`, `igf1r_gene`/`igf1_receptor`.

**These are not duplicates and must not be merged.** They answer different questions
and carry different evidence:

- the **gene** node (L8) is about *human genetic variation* — allelic series, dosage
  effects, dominant-negative versus haploinsufficiency, population frequency. Its
  evidence is human by construction.
- the **protein** node (L3/L4/L5) is about *molecular mechanism* — binding, zonal
  localization, signal transduction, kinetics. Its evidence is usually murine or
  in vitro, and it carries a translation_risk grade the gene node does not need.

Merging them would silently launder mouse mechanism into human genetic fact, which
is the exact failure mode this atlas exists to prevent. The correct link is an
**edge**, not a merge.

Phase 3 should connect each pair explicitly rather than collapsing them.

## D2 — Genuine duplicates that DO need merging

`graph.py --duplicates` also flags collisions that are real and should be resolved
when the layers are researched:

- `pappa2_protease` / `pappa_protease` — matched on the substring "papp" only. These
  are **different enzymes** (PAPP-A vs PAPP-A2) and both must be kept; the flag is a
  false positive of the matcher, not a duplicate.
- `parathyroid_hormone` / `teriparatide` — flagged on "pth". Not duplicates: one is
  the endogenous hormone (L4), the other a therapeutic analogue (L12). Keep both.
- `collagen_type_ii/ix/x/xi` and `igfbp1..6` — flagged on shared tokens. Distinct
  entities. Keep all.

As of this writing **every** flagged collision is a false positive of substring
matching. That is worth stating explicitly so a later pass does not assume the
detector found real problems and start merging.

## D3 — Stub nodes are exempt from full schema, but not from vocabulary

A stub carries only `id/name/type/layer/aliases/human_evidence/last_verified` and
`stub: true`. The validator still enforces controlled vocabulary on them, so a typo
in a node type or layer fails immediately rather than at research time.

## D4 — The bibliography is machine-populated and is never hand-edited

`addref.py` writes every entry from the live Europe PMC/NCBI record. This is the
anti-fabrication guarantee, and it means the `first_author`/`year`/`title` fields in
`bibliography.yaml` are *evidence*, not annotation. `verify_refs.py` re-checks them
and reports `FABRICATION_RISK` on any drift between stored and resolved metadata.

Non-indexed sources (regulatory dossiers, GEO accessions, patents) are added with
`--manual` and are auto-flagged `verify_by_hand: true` so they remain visible as the
weaker link they are.

## D5 — Parallel sweeps write shards, never canonical files

Concurrent subagents writing `bibliography.yaml` directly would lose entries to
last-writer-wins. Each sweep owns `sources/shards/<topic>.yaml`,
`gaps/shards/<topic>.gaps.yaml`, `gaps/shards/<topic>.search.yaml`,
`edges/shards/<topic>.edges.yaml`. `merge_shards.py` folds them in, de-duplicating
refs on pmid→doi→ref_id, renaming colliding ids, renumbering edge ids globally, and
rewriting those ids across all node/edge/gap files so no citation dangles.

Consequence to expect: **between a sweep finishing and the merge running,
`validate.py` legitimately reports "key_ref not in bibliography.yaml"**. That is the
system working, not a defect.

## D6 — A gap is a claim, and claims need evidence

`search_established` gaps are rejected by the validator without a matching
`search_log` entry giving database, exact query string, date, hit count and the
reason nothing qualified. This is because "nothing is known about X" is the single
easiest thing to fabricate in a project like this, and the hardest for a reader to
falsify.

Worked example of why this matters: an early L8 search was expected to establish
that no human growth-plate functional genomics existed. It returned Richard 2025
(*Cell*) and Darbellay 2024. The gap was rewritten from "no human data" (false) to
"enrichment demonstrated, variance partition not measured" (true). Without the
search-log requirement, the false version would have been recorded as a finding.
