# The paediatric RCT height screen

See `frontier/R001_paediatric_rct_height_screen.md` for the result. This directory is the code and
the output tables.

## Run order

```bash
python3 ctg_harvest.py   # ~5 min. Writes ctg_raw/studies.json (841 studies, ~90 MB).
                         # ClinicalTrials.gov v2 API, no key needed.
python3 screen3.py       # THE RESULT: randomised + placebo-controlled contrasts,
                         #   base rates by unit and stratum, z and two-sided p.
                         #   Writes results_randomised_placebo_controlled.csv
python3 screen2.py       # All-pairs mode incl. active-comparator trials.
                         #   Recovers the atlas positive control (losartan 0.935 vs atenolol 0.822).
                         #   Writes results_all_contrasts.csv
python3 screen.py        # First pass, kept for provenance. screen2/screen3 reuse its
                         #   regex definitions by exec'ing the header of this file.
```

`ctg_raw/` is not committed (large, and fully reproducible from `ctg_harvest.py`). The two result
CSVs are committed so the tables in F-R001 can be checked without re-running the harvest.

## Committed outputs

| file | rows | what |
|---|---:|---|
| `results_randomised_placebo_controlled.csv` | 153 | The base-rate set. Randomised allocation, paediatric, drug intervention, height-change outcome, named placebo/control arm, both arms n ≥ 10. Carries `growthdrug` / `growthdx` / `restore` labels, `diff`, `se`, `z`, `p`. |
| `results_all_contrasts.csv` | 529 | Wider set, includes active-comparator trials (`mode` column). Unanalysed — see F-R002 §C4. |

## What the columns mean

`diff` = arm minus reference, in the outcome's own unit (`u` ∈ cm, cm/yr, Z).
`se` honours the posted `dispersionType`: `√(SE₁²+SE₂²)` for standard errors,
`√(SD₁²/n₁+SD₂²/n₂)` for standard deviations. LS means from one model are correlated, so where the
posted dispersion is a standard error this SE is **conservative** if that correlation is positive.
These are screening statistics, not the trial's own inference.

`growthdrug` — the arm is a known growth agent (somatropin, vosoritide, infigratinib, GnRH analogue,
sex steroid, …). `growthdx` — the indication is a growth disorder. `restore` — the indication is a
deficit state, so any positive effect is restoration and CORR-203 governs. **Nothing is dropped on
these labels; they are strata.**

## Positive controls

Both are run in-band and both must pass before any result is read.

1. **External.** `screen2.py` must reproduce NCT00429364 as losartan 0.935 vs atenolol 0.822 cm/yr —
   the value already hand-read into the atlas. It does.
2. **Internal.** `screen3.py` must recover the known true positives: growth drugs and growth
   diagnoses come back **35/37 positive in cm (median +0.99)** and **11/11 in height-Z**.
