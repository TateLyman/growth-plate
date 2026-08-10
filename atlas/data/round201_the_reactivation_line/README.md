# Round 201 — the reserve is alerted, not activated

## The question chosen

Round 200 ended at an unrun experiment: the human plate is still **there** when growth stops
(`herrmann2002`, open epiphyses at 27), but whether the **cells** retain divisional capacity had
never been tested in any species.

It had been tested. Twice, in human tissue, by two groups this atlas already holds.

## What resolved

**The ceiling is imposed, and it reverses.** `avijgan2026`, 17 days of intact human growth plate in
serum-free organ culture:

| zone | poly(A) per nucleus, uncultured → cultured | change |
|---|---|---|
| **resting** | 26.25 → **46.53** | **+77.3 %** |
| proliferative | 62.71 → 69.26 | +10.5 % |
| hypertrophic | 81.21 → 69.52 | **−14.4 %** |

Zone-specific, with the hypertrophic zone moving the *other* way. Not a global culture artefact,
and not producible by proliferative-zone exhaustion.

**Waking the pool is the easy half and buys nothing alone.** `chu2026`, same tissue, 2 months:
cartilage survives with intact histology, **bone does not expand**, and the root progenitor identity
is destroyed by the culture — CYTL1 from **175 to 4** reads per positive cell, IGF1 absent. The two
papers describe one event from two sides.

The mouse already produced that phenotype under a defined lesion. `newton2019` Tsc1 → pool up,
recruitment *explicitly unchanged*, resting zone disordered, no ColX, no Ihh. `trompet2024` SAG →
resting Pthrp⁺ 65.5 → 139.8 /mm², proliferation unchanged. **Three systems, one phenotype: the pool
wakes and does not make columns.** `rodgers2014` names that state — **G(Alert)**.

## The test that keeps this from being a story

Four muscle mechanisms were screened against **human growth plate tissue directly**, using
`avijgan2026`'s own deposited spatial data (14 sections, 8 donors, the authors' pseudobulk-by-area
approach). Pipeline validated on their markers: ZNF550 **85.7×**, UCMA 22.0×, CHRDL2 16.2×, SFRP5
7.0×, COL10A1 correctly hypertrophic at 20 946 CPM.

**The mTORC1 arm fails. The thyroid arm holds.**

| gene | RZ | PZ | HZ | paired sign test |
|---|---|---|---|---|
| **DIO2** | 32.04 | **0.00** | **0.00** | 6↑ 0↓ **p = 0.031** |
| **NOTCH2** | 75.56 | 22.17 | 38.91 | 7↑ 0↓ **p = 0.016** |
| HEY1 | 44.90 | 8.98 | 17.62 | 7↑ 1↓ p = 0.070 |
| THRA | 141.46 | 92.96 | 64.87 | 9↑ 2↓ p = 0.065 |
| MTOR | 85.17 | 39.43 | 155.97 | 6↑ 3↓ ns |
| MET | 1.89 | 0.00 | 0.00 | 1 of 14 sections |

`de2026a`'s entire **D2 → T3 → Notch** quiescence axis is compartment-matched to the human reserve.
The depth objection runs the wrong way for a critic: the **proliferative** zone carries more total
UMI (513 009) than the resting zone (433 659), so a resting-zone-only transcript is not a sequencing
artefact.

Why it matters: `de2026a` shows D2 loss **raises proliferation and destroys self-renewal, exhausting
the pool** — round 198's reserve model in another tissue. If it transfers, raising local T3 inside
the plate *spends* the reserve. That is the opposite of the intuitive direction, and growth hormone
already perturbs thyroid economy.

## Two things withdrawn

**CORR-193** — no re-entry fraction can be read from Fig 2f. Axes run to +150 % and −100 %, so the
quantity is normalised; and the analogues had unequal exposure (EdU 0.7 d, IdU 5 d, CldU 8 d).
Exposure-corrected, the RZ rate *falls* 10.6 → 6.9 %/day while the **PZ collapses 25-fold**. The
apparent overtaking is PZ shutdown, not RZ recruitment. The conclusion survives on Fig 2g instead.

**CORR-194** — `chu2026`'s resting-zone GH result is uninformative, not null. Point estimate
**2.80×** in the *same* direction as the significant PZ effect; P = 0.79 is Tukey-corrected across
four groups against ≈0.25 unadjusted; MDD at 80 % power is a **5.0× rise**. The study could not have
detected the effect it observed. And pSTAT5 rises **predominantly in the RZ** (P = 0.034).

## Questions this round opened, and where each landed

| question | status |
|---|---|
| does reversible arrest hold at bone age 16? | **bounded** — donors are 12y2m–14y6m, Tanner 2–4; the round-197 sampling ceiling makes this unobtainable in human tissue by this route |
| what fraction of RZ cells re-enters? | **inadmissible** — CORR-193; no such number exists in the literature |
| the authors' prolonged-G1 alternative | **answered indirectly** — under either reading the output is set by position in the body and rises when position is removed; the ceiling is imposed either way |
| the Wnt sign conflict with `hallett2021` | **resolved** — the two score different axes (label retention vs instantaneous RNA), and `avijgan2026`'s own mouse cross-check contains the reconciling population. Residual named in the node |
| does re-entry produce columns? | **answered, negative** — no bone in explant, root identity destroyed, and the mouse Tsc1 equivalent shows no recruitment |
| what releases quiescence on explanting? | **partially** — 3 of 5 candidate inputs bounded; `boaventura2026` (loss of 3D confinement) is the leading candidate; injury is the one input *added* rather than removed |

## New gaps

- `g_l2_is_the_growth_plate_reserve_held_in_g0_or_in_galert` — nobody has staged cartilage against G0/G(Alert); two logged sweeps, 28 and 74 hits, zero in growth plate
- `g_l2_what_is_the_second_signal_that_converts_an_alerted_pool_into_columns` — **now the binding constraint on the whole reserve route**
- `g_l4_does_dio2_set_resting_zone_quiescence_in_the_growth_plate`
- `g_l6_does_unilateral_paediatric_fracture_raise_growth_in_the_uninjured_limb` — `cho2025` shows 66 % of children overgrew the ipsilateral **unfractured** femur; the systemic reading predicts a contralateral and upper-limb effect that nobody can see, because everyone reports leg-length **discrepancy**

`g_l2_p16_cellular_senescence_in_the_growth_plate` was attempted and **not** answered: CDKN2A is on
the probe panel in all 14 sections and reads **zero in every spot**, including marrow and SOC. A
zero everywhere points to probe failure, not biology.

## Files

| file | what it is |
|---|---|
| `ledger_output.txt` | `atlas/tools/explant_reactivation_ledger.py` — the exposure correction, the MDD arithmetic, the release-input enumeration |
| `galert_candidates_output.txt` | `atlas/tools/human_rz_galert_candidates.py` — the human compartment screen |
| `avijgan_fig2f_page5_400dpi.png` | full page render |
| `avijgan_fig2f_600dpi.png` | the three-analogue row |
| `avijgan_fig2f_{EdU,IdU,CldU}_900dpi.png` | per-panel renders the per-donor values were calibrated from |
| `chu2026_fig5L_700dpi.png` | the GH EdU panel behind CORR-194 |

Source PDFs are at `acquire/papers/avijgan2026_boneres_human_rz_quiescent_published.pdf`,
`acquire/papers/avijgan2025_biorxiv_human_resting_zone.pdf` (the preprint carries the culture
protocol and the numeric medians the published legend omits) and
`acquire/papers/chu2026_scitranslmed_pubertal_human_gp.pdf`. The spatial data re-analysed here is
`acquire/spatial_bone_growth/visium_export/`, from github.com/anarl/spatial_bone_growth.
