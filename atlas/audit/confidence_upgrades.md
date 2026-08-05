# Confidence grade changes

Every change to a node's confidence grade is recorded here with its justification.
Grades are claims about evidence strength, so changing one silently would defeat the
purpose of having them.

---

## 2026-08-05 — Baseline A/B-tier audit and re-grade (DOWNGRADES)

Run before any synthesis was built on the grades, per the density diagnostics.
Tool: `atlas/tools/grade_audit.py` (criteria encoded there, not applied by hand).

**Criteria tested**
- **A** = "replicated in humans with direct measurement or interventional data"
  → operationalised as ≥2 primary-type refs **and** `human_evidence: direct` **and**
  `human` in `species_basis`.
- **B** = "strong animal mechanism + consistent human correlative/genetic support"
  → requires `human_evidence` ≠ `absent` and ≥2 refs.

**Result: A-tier inflation 28.2% (35/124), B-tier 18.2% (16/88). 51 nodes downgraded.**

| | before | after |
|---|---:|---:|
| A | 124 | **89** |
| B | 88 | **106** |
| C | 134 | **150** |
| D | 52 | **53** |
| E | 11 | 11 |
| X | 1 | 1 |

### The finding that matters more than the rate

**Zero A-grade nodes failed on human-evidence or species grounds.** Every single
failure was citation *thinness* — fewer than two primary sources. Not one A-grade node
was passing animal data off as human fact, and not one lacked `human` in its
`species_basis`.

That distinction is the whole point of running the audit. An inflation rate driven by
species laundering would mean the atlas's core epistemic discipline had failed and the
content needed re-reading. An inflation rate driven by citation count means the grades
were *directionally honest* but over-claimed on replication — the content is sound and
the fix is to add a second independent primary, not to re-examine the biology.

### Method correction made during the audit

The first implementation downgraded any single-reference A node to **D**. That produced
an obviously wrong result: `height_gwas` — a meta-analysis of **5.4 million** individuals,
the strongest human evidence in the atlas — was scored "D: single study, in vitro only,
or conflicting reports". The rule was wrong, not the node.

Two fixes, applied before any grade was written:
1. **Downgrade by one grade, not to a floor.** A node failing only on citation count is
   under-evidenced, not unreliable.
2. **Meta-analyses and systematic reviews count as internally replicated.** A pooled
   analysis of many cohorts satisfies the spirit of A's "replicated" requirement even as
   a lone reference, provided the human-evidence criteria are met.

`height_gwas` accordingly sits at **B**, and is a prime candidate for re-upgrade once a
second independent primary is attached.

### Disposition

These 51 downgrades are **not final**. L8 is designed as the confidence-upgrade engine:
each monogenic locus is a human dosage experiment attached to a mechanistic node, and
attaching it supplies exactly the second human primary these nodes lack. Upgrades earned
that way are logged below with the evidence that justified them.

---

## Upgrade admissibility — replication is PROPOSITIONAL, not topical

An upgrade is admissible only if the second reference **independently tests the same
proposition by a different route**. Topical adjacency is not replication. A paper on
*ACAN* dosage does not replicate a claim about aggrecan turnover kinetics merely
because both concern aggrecan; two papers agreeing that a molecule "matters" replicate
nothing.

**Every upgrade must record all of these fields. An entry missing any of them is not an
upgrade, it is citation-stacking, and is rejected.**

```yaml
- node_id:
  proposition_tested:     # ONE falsifiable sentence. If you cannot state it in one
                          # sentence, the node is making several claims and needs
                          # claim_grades (see below), not an upgrade.
  ref_1:
    ref_id:
    what_it_shows:        # what THIS paper demonstrates about THAT proposition
  ref_2:
    ref_id:
    what_it_shows:
  independence_basis:     # different method | different cohort | different direction
                          # of perturbation (gain- vs loss-of-function) | different
                          # species with human confirmation. State which.
  grade_before:
  grade_after:
```

**Rejected attempts are logged too.** The rejection rate is itself a measurement: it
quantifies how thin genuinely replicated human evidence is in this field, which is a
finding this atlas is positioned to make and most reviews are not.

### Upgrades — accepted

_(none yet — populated during the L8 completion sweep)_

| date | node | proposition | ref_1 | ref_2 | independence basis | from → to |
|---|---|---|---|---|---|---|

### Upgrades — REJECTED (citation-stacking attempts)

| date | node | proposition | why rejected |
|---|---|---|---|
