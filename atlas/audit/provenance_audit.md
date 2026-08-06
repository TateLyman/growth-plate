# Transitive method audit

**2026-08-06.** `CORR-009` and `CORR-010` are the same defect twice: a load-bearing number
whose grade lives not in the paper the atlas cites but in the *method paper that paper cites*.
`hunziker1989`'s terminal cell height carried three rounds of reasoning and a proposed
compound class before anyone opened `cruzorive1986`, forty pages long and named in its second
sentence. `rubin2021` was then accepted from its abstract on the other side of the same
dispute.

The atlas had no way to see that class of defect. It has `has_full_text` per reference. It
has nothing that says *the method behind this number was checked*.

## The scale of it

| | |
|---|---|
| quantitative rows | **1,618** |
| rows carrying stake (contradiction, flow model, A/B node, or compound screen) | **1,428** |
| distinct sources | 452 |
| references with `has_full_text` | **1,006** |
| references marked `full_text_read` | **19** |

## What the tool is

`atlas/tools/provenance_audit.py` is a **triage ranker**, not a detector. It scores each row
by *stake* (what rests on it) × *suspicion* (derivation language in its own text, no
dispersion reported, source never read, sole-sourced) and emits a reading list.

**A high score is a reading assignment, not a finding.** Nothing in that file could have
produced CORR-009 — every claim there came from reading a paper. The score is deliberately
not thresholded into pass/fail so no verdict can be read off it. Verdicts are hand-written in
`query/provenance_audit/verdicts.yaml` after reading the source, and each names its evidence.

## Verdicts from the first pass

**PROV-001 — the flow model's halt factor is a calculated budget, and was not labelled one.**
`wilsman1996`'s 9 / 32 / 59 partition — the number the whole field quotes — is computed, and
the paper states its assumptions plainly: *steady-state kinetics over 24 hours*, and *the
growth plate modeled as a two-compartment system*, with proliferative zones *"modeled as
circular cylinders of diameter 1"*. The atlas rows said only "not reported".

The part that matters: **the three shares sum to 100 % by construction**, and matrix volume
per cell is the *complement* of the cell volume fraction, `(1 − Vv) · V_total / N`, not a
measurement. They are not independent estimates and cannot carry independent uncertainties.
`flow_model.py` halts at exactly this factor, so nothing has propagated them — the risk was
latent, not realised. **Flag added to 11 rows across 4 nodes. No value changed.**

**PROV-002 — CORR-009 propagates to `hunziker1987`, and nothing said so.** Same laboratory,
same estimator family; `hunziker1989` states that some of its 35-day estimators had already
appeared there. So the **4-fold cell HEIGHT increase** is a shape-model output carrying the
CORR-009 biases. The **10-fold VOLUME increase from the same source is unaffected** — that
estimator is unbiased irrespective of shape and orientation. Flagged, with the limit stated:
this is *inferred* from `hunziker1989` and `cruzorive1986`, because `hunziker1987`'s own
Methods have never been read — the PDF supplied on 2026-08-06 was a Literature Abstracts
listing page from a different journal.

**PROV-003 — a flag in the atlas contradicted its own note.** `hunziker1987` carried
`has_full_text: true` beside a note recording that the full text had been *"Requested and NOT
obtained"*. Corrected. The general lesson is bigger than the entry: **`has_full_text` means a
file was obtained, never that the method was checked** — which is the exact distinction both
corrections turned on.

**PROV-004 — no defect, and worth recording.** `kember1976`'s 24-cell column count, 20-day
derived cycle time and 38 µm/day rate ranked 1st, 3rd and 11th on heuristics alone. On
reading, all three already declare precisely what they are — the 24 count is annotated *"NOT
a direct count … a RABBIT-derived fraction applied to it, and the paper says so"*. CORR-008
did that work. Recorded because a triage tool whose top hits are all defects is a tool tuned
to its own answer.

## What this does not do

It has read the top of a 1,428-row list. The rest is unadjudicated, and the ranking is a
heuristic over text, so it will miss any row whose derivation is invisible in its own prose —
which is precisely the `hunziker1989` case, where the row read like a measurement because the
paper's abstract does too. **The only reliable detector is reading the method paper**, and
the honest output of this audit is a queue, not a clean bill.

The structural fix the atlas still lacks: a per-row field recording whether the value is a
*measurement*, a *model output*, or *derived from another row in the same paper* — and a
pointer to the method source. `PROVENANCE FLAG` in free text is a stopgap.
