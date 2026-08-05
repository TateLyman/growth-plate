# Retracted, corrected, or seriously disputed sources

Any paper that is load-bearing for a node gets a retraction/critique check before its
claim is graded above D. Findings are logged here with the node ids affected.

**Checked mechanically over all 1,049 references on 2026-08-05** by
`atlas/tools/verify_refs.py`, which re-resolves every entry against the live Europe PMC
/ NCBI record and flags retraction-related publication types.

Result: **1,005 resolved OK · 0 metadata mismatches · 0 unresolved · 44 manual
(non-indexed, `verify_by_hand`) · 1 retraction-related.**

| Ref | Status | Evidence | Nodes affected | Action taken |
|-----|--------|----------|----------------|--------------|
| `wu2013` — Wu S *et al.* 2013, *J Biol Chem*, PMID 23940039 | **WITHDRAWN** | Europe PMC pubtype `Retracted Publication`; `Retraction in: J Biol Chem 2020;295(37):13137`, notice PMID **32917830**, title begins "Withdrawal:". No reason text is retrievable and none is asserted here. | `klotho_beta_cofactor`; edges `e01055`, `e01056`, `e01057`; gaps `g_l0l9_001`, `g_l0l9_009`, `g_para_007` | **CORR-004.** Disposition `both_invalid`. Claim *"FGF21 mediates undernutrition-induced growth-plate GH insensitivity"* **C → X**. Claim *"KLB is expressed in growth plate chondrocytes"* **C → D** (its replication was `wu2013`). Quantitative row voided and tombstoned. Edge `e01055` reclassified `activates`/C → `hypothesized_link`/speculative, reopening the L10→L3 seam. Reference retained and flagged rather than deleted. |

## Checked and clean

- **`wu2012`** (Wu S *et al.* 2012, *J Biol Chem*, PMID 22696219) — same laboratory,
  same subject, cited on the same node. Queried separately: publication types clean,
  `commentCorrectionList` null. **Not retracted.** Recorded because "same group as a
  retracted paper" is a suspicion, not a finding, and the atlas does not act on
  suspicions.

## Disputed but not retracted

Substantive scientific disputes are tracked in `atlas/audit/contradictions.md`, not
here. This file is for the publication record — retractions, withdrawals, expressions
of concern, and errata that change a number the atlas quotes.

## What this check cannot see

`verify_refs.py` reads the publication-type field of the indexed record. It will not
detect:

- a retraction that the indexer has not yet propagated;
- an **expression of concern** filed as a comment rather than a pubtype;
- a **correction/erratum** that silently changes a figure the atlas quotes, unless the
  erratum is itself indexed against the record;
- anything at all about the 44 non-indexed manual sources (GEO accessions, FDA labels,
  trial-registry entries), which have no publication record to carry a retraction flag.

Re-run `python3 atlas/tools/verify_refs.py` before any release. It takes about ten
minutes over the full bibliography and it is the only thing standing between this atlas
and a claim whose source stopped existing after it was cited.
