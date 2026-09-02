# Round 21 — Wilsman 1996, and the outreach package

**Date:** 2026-08-06 · **Branch:** `claude/growth-system-atlas-yl5esl`

---

## 1. Wilsman already ran the experiment I nominated — in rat

Last round I called for continuous labelling to plateau, because the plateau *is* the growth
fraction. `wilsman1996` did it in 1996: BrdU by implanted osmotic pump, rats culled at 12, 24,
48, 72 h, four growth plates.

**Rat growth fraction: 0.99 (proximal tibia), 0.99 (distal radius), 0.98 (distal tibia), 0.89
(proximal radius).** The rodent plate has essentially **no idle proliferative pool** — and the
one plate below 0.99 is the slowest-growing, the direction a recruitment model predicts.

That makes the human deficit a real species difference rather than a methodological one, and it
validates the protocol I nominated for human tissue.

### A derived tension, graded E

The identity is `labelling index = S / T_turn`, where `T_turn` is the mean inter-division time
over *all* proliferative-zone cells. **The growth fraction cancels.** It checks out in rat:
`T_turn` = 30.9/0.99 = 31.2 h with S = 3.4–6.1 h predicts a labelling index of 11–20%, matching
the 9–15% reported in rodents.

Applied to human — labelling index 3.4–4.4%, `T_turn` = 480 h — it gives **S ≈ 16–21 h**, three
to six times the rat's. But if human S phase were rat-like at ~5 h, the same identity forces
`T_turn` ≈ 114 h, about 5 days, not 20 — outside Kember's own ±50% band.

So at least one of three things is true, and the atlas does not choose:
1. human S phase really is long;
2. the 20-day turnover time is a ~4× overestimate;
3. the 3.4–4.4% labelling index is an overestimate — plausible, since it comes from *in vitro*
   labelling of **amputation specimens**, tissue that may be reactive.

**And a structural point that survives whichever resolves.** Because the growth fraction cancels,
**no single-pulse labelling index can ever determine it** — and every human proliferative
measurement ever made is a single-pulse index. Only cumulative labelling separates them. The
nominated experiment is not replaced by this derivation; it is *proved necessary* by it.

The arithmetic does bound the human growth fraction from below: since S ≤ cycle time, GF ≥ the
labelling index (~4%); and an S phase occupying no more than a third of the cycle puts it above
~15%.

## 2. The 59% figure was quoted flat, and it is not a constant

I had `9% division / 32% matrix / 59% enlargement` second-hand through Roach. From the primary:
that is the **fastest** plate. In the slowest (proximal radius) it is **7% / 49% / 44%** — as
elongation slows, the contribution shifts from cell enlargement toward matrix synthesis.

"Chondrocyte enlargement supplies ~60% of elongation" is true of one rat growth plate, not of rat
growth plates. What *does* generalise within the study: **division is the smallest term
everywhere, 7–9%.**

Also from the primary, and counterintuitive: proliferative-zone cell **density varies inversely**
with elongation rate (196,370 → 345,070 cells/mm³). Faster plates have fewer, larger cells.

## 3. CORR-015 — I asked you for the wrong paper

I requested "Thurston 1985, PMID 3840788 or 4066480." Both are **mouse** papers. The atlas's
`thurston1985` is a *third* 1985 Thurston paper — *In vitro thymidine labelling in human and
porcine growth plates*, **PMID 3864550** — which was **already held and already read on
2026-08-05**, with the correct PMID and DOI sitting in the bibliography.

I generated a want-list item from a fresh literature search instead of from the atlas's own
record. The atlas was right; the request was wrong. New rule: resolve any request against the
bibliography entry for that `ref_id` before asking a person for it.

**Salvage:** the supplied paper earns its place anyway. **Type I `cn` mice are dwarfed with
reduced hypertrophic cell height *alone*** — proliferation-zone cell number hardly reduced,
mitotic rate normal. That is the counterweight to C-L1-09: human development doesn't vary
`h_term` and birds don't track it, but *breaking* it is sufficient to dwarf an animal.
Invariance under physiology is not irrelevance under perturbation.

## 4. Outreach — drafted, not sent

Three documents in `outreach/`. **Nothing has been sent.** One Gmail draft created, sitting
unsent in the account.

- **`01_karolinska_newton_chagin.md`** — to Newton, cc Chagin / Sävendahl / Mirzazadeh (the
  corresponding addresses printed in the two 2026 papers). Two asks: the cumulative-labelling
  readout for the human growth fraction, and sacubitril in the Chu explant. Includes the design
  note neither paper states — GH failed in some donors, so donor variance can hide the positive
  control. **Also a Gmail draft.**
- **`02_vivli_kigs_data_request.md`** — the full KIGS proposal: question, prespecified
  falsification condition, variable list, publication plan, and an explicit
  confounding-by-indication section with four mitigations and a commitment to report *"not
  answerable in these data"* if they fail. Complete except the two fields I cannot supply.
- **`03_collaborator_ask_for_kigs.md`** — a short email to find the named PI the Vivli form
  requires.

**Verify before submitting:** the Vivli/CSDR routing is from the sponsors' public data-sharing
policies; I have not confirmed KIGS currently appears in Vivli's study catalogue. Check the
catalogue first, and use the "data not listed" enquiry route if absent.

## 5. Atlas state

628 nodes · 1,220 edges · 305 gaps · 1,096 refs · **0 validator errors**

`wilsman1996` marked read; `thurston1985cn` added. Growth-fraction node rebuilt with the rat
measurement, the derived S phase (E), and the cancellation argument. `CORR-015` recorded.
