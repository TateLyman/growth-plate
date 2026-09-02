# Round 19 — the five requested sources, read in full

**Date:** 2026-08-06 · **Branch:** `claude/growth-system-atlas-yl5esl`

All five Tier-1 want-list items from `docs/acquisition_sweep_round18.md` were supplied and
read. Four were the atlas's oldest missing primaries; the fifth is three months old. Below
is what each one changed, including the two places where it changed something I had
previously asserted.

---

## 1. Byers 2000 + Kember 1976 — the age interval the atlas could not see

New node: `atlas/nodes/L1_growth_plate_architecture/human_growth_plate_age_trajectory.yaml`
(grade **B**, human evidence **direct**, 8 quantitative rows).

Between them these cover **58 human individuals from 11 days to 14 years** at two skeletal
sites — the interval that Round 18 identified as a hole in the public record.

**What collapses.** Human rib proliferative zone height falls 1.1 mm (11 days) → 0.671 mm
(1 year) → 0.372 mm (13.5 y), r=−0.62, p<0.001. Hypertrophic zone 0.37 → 0.104 → 0.095 mm,
r=−0.68, p<0.001.

**The shape matters more than the endpoints: 72% of the entire hypertrophic-zone fall
happens in the first year of life, and between age 1 and 13.5 the zone changes by 9%** —
while growth velocity falls several-fold and then spikes at puberty. Hypertrophic zone
height therefore cannot be what sets human growth velocity after infancy.

**What does not change.** Human terminal hypertrophic cell height is **29–38 µm from birth
to 13 years with no age dependence, 33 ± 5 µm at ages 5–8** (distal femur, measured in the
direction of growth, five groups of ten cells per specimen, 13% processing shrinkage
measured and corrected). Rib lacunar diameter likewise shows no significant change with age
in either zone. The cells keep both their height and their width while the zones containing
them collapse — so the collapse is in **cell number per column and in the matrix between
columns**, not in cell size.

**What carries the variation.** At ages 5–8 the distal femoral plate elongates 1.4 cm/yr =
38 µm/day; at 33 µm per terminal cell that is 1.2 new cells per column per day; with ~24
proliferative cells per column, **mean cell cycle time = 20 days.** The rat figure is 2
days. Kember & Sissons state the conclusion the atlas should have been carrying for fifty
years: *it is unwise to extrapolate this tissue from mouse to man.*

And: **the number of cells in the proliferation zone does not increase during the adolescent
spurt**, so the spurt must come from faster cycling. With terminal cell height fixed and
column cell number only falling, **cycle time is the only free variable left in the human
growth plate.**

### Two nodes were wrong in a way this fixes

- `cell_cycle_time_pz` **cited `kember1976` and contained no human number** — every
  quantitative row was rat, in hours. It now carries 20 days (≈480 h against 30.9 h in fast
  rat proximal tibia, a ~15-fold difference in the same parameter). `human_evidence`
  indirect → **direct**.
- `hypertrophic_volume_increase` recorded `human_evidence: absent` while the human
  measurement had existed since 1976. Now **direct**, and the human evidence is a *null*.

Grade held at **C** on both. A derivation with a rabbit-imported assumption in 12 subjects
does not raise a grade, and neither does a null. What changes is reach, not confidence.

---

## 2. Roach 2003 — and a contradiction it creates

`rat_growth_cessation_without_fusion` previously held only the four old-plate morphologies,
taken from the abstract. The full text supplies the mechanism, and it collides with §1.

In rat, plate height is maximal at 2–4 weeks when the lower hypertrophic zone holds cells up
to 40 µm; the fall is **mostly loss of that zone**; in 62–80-week rats *all* plate cells are
the size of young proliferative cells — the capacity for volume increase is gone. Meanwhile
**proliferative zone height and PCNA index hold to at least 12 weeks.** The authors:
absence of the volume increase is the main factor associated with deceleration and
eventually cessation.

> **New contradiction C-L1-09.** The variable that shuts growth down in the rat is the one
> the human holds constant.

I have not resolved it and have recorded three open readings — a real species difference; a
power/site artefact (12 subjects, 1–2 per age; rib for the transverse measure); or a
between-species regression being misread as a within-individual law. Wilsman's much-quoted
"59% of elongation from chondrocyte enlargement" is 4-week rat proximal tibia, and is
recorded as second-hand because I have not read that primary.

**The therapeutic reading runs both ways and I am not choosing.** An invariant parameter may
be invariant because it is tightly defended — or because nothing in normal human physiology
varies it, in which case it is an unused degree of freedom with no homeostat to fight. That
second reading is what a CNP analogue exploits, and vosoritide works.

---

## 3. Avijgan 2026 — the resting zone, measured in human tissue

8 biopsies, ages 12 y 2 m to 14 y 6 m, Tanner 2–4, distal femur, epiphysiodesis for
idiopathic tall stature. Visium + Visium HD, electron microscopy, RNAscope, and sequential
thymidine-analogue labelling of intact biopsies.

Human resting zone chondrocytes are **functionally quiescent in vivo**, on four independent
readouts: lowest mRNA content of any zone (in every one of 17 sections), predominantly
*nuclear* mRNA, abundant heterochromatin, and failure to incorporate EdU overnight while
incorporating IdU and CldU on subsequent days — reversible arrest, the behaviour of satellite,
haematopoietic and neural stem cells released from their niche. **CHRDL2+ and/or SFRP5+
subsets are the *least* quiescent**, giving a hierarchy rather than a uniform compartment.

`resting_chondrocyte` **absent → direct**; `resting_zone` **indirect → direct**. The atlas
previously stated in terms that *"in human tissue none of this has been demonstrated."* It
now has been.

Data/code: `github.com/anarl/spatial_bone_growth`. No sequencing accession is given; original
images are on request.

This also converts gap `g_l1arch_human_cycle_time_measured` from hard to tractable — the
sequential-analogue protocol on intact human biopsies is exactly the technique a human cycle
time needs, applied to the proliferative zone instead of the resting zone, in the pubertal
window no other method reaches.

---

## 4. KIGS — the largest human dataset bearing on depletion

New node: `atlas/nodes/L12_pharmacology_as_mechanistic_probe/gh_dose_versus_final_height.yaml`
(grade **C**; the two derived comparisons graded **D** individually).

The supplement is the safety-and-demographics supplement, not participant data — but
Supplemental Table 11 carries the height-SDS trajectory by diagnosis and region, and the
regions were dosed differently.

**Idiopathic GHD, prepubertal at start:**

| | Europe | USA |
|---|---|---|
| median dose | 0.21 mg/kg/wk | **0.30 mg/kg/wk** (+43%) |
| baseline height SDS | −3.01 | −2.99 |
| baseline age | 7.51 y | 7.4 y |
| **Δ height SDS, year 1** | +0.69 | **+0.75** |
| **Δ height SDS, near-adult height** | **+1.97** | **+1.96** |

**The higher dose buys more in the first year and nothing at the end.**

And across all six diagnosis × region cells, **the first year delivers 35–41% of the entire
lifetime height-SDS gain** (IGHD Japan 62% is the outlier), with the remaining decade of
daily injections delivering the rest.

Both patterns are what a depletable resource spent at an adjustable rate looks like. **Both
are equally consistent with catch-up growth toward a genetic target involving no depletion
at all**, and aggregates cannot separate them. The confound that most limits the dose
comparison is in the numbers themselves: **2,642 of 8,597 European children reach near-adult
height (31%) against 213 of 2,239 American ones (9.5%)** — the two endpoint medians describe
differently selected survivors, and that alone could produce the null.

Japan's IGHD row proves the general point: cumulative gain at puberty onset (0.41) is
*lower* than at year 1 (0.53), which cannot happen within a person. These are different
subsets at every row.

New gap `g_l12_kigs_depletion_test` states the falsifiable version: depletion predicts
cumulative GH exposure is associated with **earlier** attainment of near-adult height at no
greater final height. It needs individual participant data via Vivli or CSDR — a named
researcher and an institutional affiliation, which remains the barrier.

---

## 5. Atlas state

626 nodes · 1,216 edges · 302 gaps · 1,092 refs · **0 validator errors**
Confidence: A 156 · B 188 · C 187 · D 80 · E 13 · X 2

New: `human_growth_plate_age_trajectory` (B), `gh_dose_versus_final_height` (C).
Upgraded to human-direct: `cell_cycle_time_pz`, `hypertrophic_volume_increase`,
`resting_chondrocyte`, `resting_zone`.
New refs: `roach2003`, `avijgan2026br`, `maghnie2022`. Marked read: `kember1976`,
`avijgan2025`.
New contradiction **C-L1-09**; **C-L1-07** status updated — the `kember1976` side is now
verified against the primary and confirms the atlas's record exactly.

### Provenance note

`byers2000` was already flagged `full_text_read: 2026-08-06` before I had the PDF. Its
recorded one-line finding is accurate to the full text, so nothing downstream is wrong — but
the sampling structure that most limits it (**36 of 46 cases under one year; one individual
per age thereafter**) was not recorded and could only have come from the full text. The flag
was ahead of the reading. That is the same defect class the provenance audit was built for,
found again in my own bookkeeping, and it is now recorded in the ref's note.

---

## Still wanted

1. **Chu et al. 2026**, *Sci Transl Med*, PMID 41984930 — the paper behind GSE288028, whose
   data this atlas has used since Phase 5 and whose text it has never read.
2. **KIGS / NCGS individual participant data** via Vivli or CSDR — the only thing that
   settles §4.
3. **Thurston 1985** (the 20.5 µm side of C-L1-07) — the one side of that contradiction
   still unread in full.
4. **Wilsman et al. 1996**, the source of the 9% / 32% / 59% decomposition now quoted
   second-hand in C-L1-09.
5. **Kember cell-kinetics series** — PMIDs 8219479, 2267417, 3502931.
