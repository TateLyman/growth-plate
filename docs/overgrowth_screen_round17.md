# Round 17 — the human tall-stature gene space, screened backwards, and what it does not contain

Every previous screen started inside the graph: pick a node, walk signed edges into an
elongation outcome, emit a compound. That search is bounded by what the graph contains, which
is bounded by what has been studied in mice.

This one starts outside. **Human overgrowth syndromes and tall-stature associations are a
catalogue of perturbations already known to make a human taller** — lifetime, whole-organism,
right species, integrating growth velocity *and* growth duration by construction, already run
at population scale. The short-stature side is mined exhaustively because dwarfisms present in
clinic. The tall side is comparatively unmined, because being tall is rarely a complaint.

## Method

50 overgrowth / tall-stature disease terms resolved against Open Targets → **1,596 distinct
associated genes**. Filtered to genes present in **≥3 of 4 human growth-plate donors** and
carrying an association score at or above the harvest's own **90th percentile (0.118)** —
median is 0.058, so the bottom nine-tenths is the tier where a gene was mentioned near a
disease name once. That leaves 141 genes to ask about drugs. **45 clear all three necessary
conditions**: associated with human overgrowth, present in a human growth plate, and having a
drug that exists.

Direction is left **UNRESOLVED** on every row, on purpose. An association says a gene is
implicated in tall stature; it does not say whether loss or gain of function causes it, and
therefore does not say whether you want an agonist or an antagonist. FGFR3 carries both at
once.

## Result

| mechanism of tallness | n | usable? |
|---|---|---|
| PI3K/AKT/mTOR segmental overgrowth | 14 | no — cancer predisposition, and the drugs are GOF inhibitors, running the wrong way |
| Marfanoid connective tissue | 14 | no — tall by **dolichostenomelia**, a structural fibrillin/collagen defect; the drugs are aortic-root protection |
| GH/IGF endocrine | 4 | no — every listed drug is an **acromegaly** drug, built to reduce growth |
| chromatin / syndromic overgrowth | 3 | no — tall with intellectual disability and tumour risk |
| insulin secretion | 2 | no — ABCC8 loss of function gives fetal **macrosomia** via hyperinsulinism, not postnatal linear growth |
| imprinted locus, vascular, matrix, noise | 4 | no |
| **growth-plate kinetic** | **3** | FGFR3, NPR2, LEPR |
| **fusion timing** | **1** | ESR1 |

## What that means

**The screen found no new pharmacologically approachable growth-plate target.** The four that
survive classification are exactly the ones this project already had:

- **NPR2** — drugs returned: vosoritide, carperitide. The CNP axis, already the most advanced
  programme in the field.
- **FGFR3** — infigratinib. Loss of function gives CATSHL tall stature; already the second
  programme.
- **ESR1** — 51 approved drugs. The duration lever, and the reason aromatase inhibitors are
  already discussed here.
- **LEPR** — already standing at grade C from the round-1 compound screen, with no human
  stature association strong enough to promote it.

This is a negative result, and it is worth as much as a positive one. It says:

> **The human tall-stature gene space, filtered to genes that are actually in a growth plate
> and actually have a drug, is exhausted.** Everything in it is either already being drugged,
> or is tall through a mechanism nobody would induce — a cancer pathway, a collagen defect, a
> chromatin syndrome, or fetal hyperinsulinism.

Two-thirds of the list — the PI3K/mTOR and Marfanoid blocks, 28 of 45 — are tall for reasons
that have nothing to do with growth-plate kinetics at all. That is the single clearest thing
the screen shows, and it is invisible without hand classification, which is why
`mechanism_class` was deliberately left for a person rather than a keyword rule.

## Where that points

If human genetics has no unused lever, the unused lever is not a gene. Round 16 and
`g_l1arch_018` point at the alternative: the chondrocyte enlarges **isotropically**, so its
size cannot explain why the gain appears as *length* rather than width. Something outside the
cell converts it — the tissue's mechanical **anisotropy**, ~10× along the growth axis at
birth, collapsing to ~1 exactly as growth slows. That is not a gene, it is a material
property, and no therapeutic programme in this field addresses it.

The screen's negative result is what makes that axis worth the attention.

## Defects found in my own tooling on the way

Recorded because the first run produced a clean, confident, wrong answer.

1. **"0 with a known drug" across all 141 genes** — not a result. `Target.knownDrugs` had been
   removed from the API, every call returned HTTP 400, and a bare `except Exception: pass`
   turned each 400 into an empty list. A silent zero is indistinguishable from a real negative.
   There is now a **positive control** (CYP19A1 must return anastrozole) that halts the run,
   and `fetch_drugs` returns `None` on failure — never `[]`.
2. **Results written only at the end** — a timeout destroyed 50 minutes of live API calls. Now
   checkpointed and resumable.
3. **The expensive query ran before the free filters** — 1,596 genes at ~20 s each is eight
   hours to rank noise.
4. **A patch inserted a warning block mid-loop**, silently making the row-builder the body of
   an `if` that was never true, so the writer got an empty list and truncated the previous
   output to zero bytes. There is now a `if not rows: HALT` guard rather than an overwrite.
