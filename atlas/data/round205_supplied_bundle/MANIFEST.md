# Round 205 — manifest of everything supplied, and where each went

Recorded here because supplied material has been lost between rounds before.

| supplied file | what it is | ref_id | status |
|---|---|---|---|
| `combined_ultra_compact_8up.pdf` (39 pp, 8-up) | **FDA Multi-Discipline Review NDA 214938 (VOXZOGO/vosoritide), Reference ID 4890910** + **karimian2013** (PLoS ONE, doi 10.1371/journal.pone.0067859) | `fda_voxzogo_multidiscipline_review_2021` (NEW, manual), `karimian2013` (existing, now read in full) | **READ, both annotated** → text at `combined_8up.txt` |
| `jci.insight.165226.sd.pdf` (11 pp) | **trompet2024 supplementary figures** — Suppl Fig 5F/6B are the terminal hypertrophic chondrocyte heights I asked for | `trompet2024` | **READ** → `trompet2024_supplement.pdf` |
| `jci.insight.165226.sdval.xlsx` | **trompet2024 author-deposited per-animal source data**, 10 sheets | `trompet2024` | **READ, analysed** → `trompet2024_source_data.xlsx`, tool output in `trompet_thc_output.txt` |
| `Abubakar 2019 Anim Models Exp Med` (10 pp) | Postnatal ex vivo rat model for longitudinal bone growth — the platform behind the NHE1/AE2 ion-transport thread | `abubakar2019` (NEW, PMID 31016285) | **REGISTERED, annotated, not yet read in full for its own quantitative content** |
| `pnas002480231.pdf` (5 pp) | PNAS 1989, Uitterlinden et al., *"Two-dimensional DNA fingerprinting of human individuals"* | — | **NOT RELEVANT** to growth-plate biology. Recorded so it is not re-requested. Almost certainly an accidental inclusion; say if it was deliberate and I will look again |

## What each one settled

- **trompet2024 source data** → CORR-200: the h_term gain is **transient** (peaks 1 month, gone by 2), and the whole observed h_term range across every agent in the atlas is **1.0–1.4×**
- **FDA review, bone age** → vosoritide does **not** advance bone age at the label dose (randomised, 1.02 vs 1.14 y/52 wk; −0.05 y at 104 wk)
- **FDA review, Table 55** → CORR-201: **no significant effect on L1–L4 vertebrae or skull** in normal primates, against +7 % tibia and +6 % humerus; plus a sex split and a **fourfold within-plate regional range**
- **FDA review, Table 37** → CORR-202: the dose ceiling is **growth plate dysplasia in normal animals at 0.08–0.2× the human exposure**
- **karimian2013** → the only compound in the file measured on **all four terms separately**, all favourable, multi-site, with a final-length endpoint

## Files here

`combined_8up.txt`, `trompet_thc_output.txt`, `MANIFEST.md`, plus the three copied source files above.
Tools: `atlas/tools/trompet_thc_height_timecourse.py`.
