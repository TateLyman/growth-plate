# round 213 — SURF301, ENA 2024 (`surf301_ena2024`)

User-supplied 23-slide conference presentation, 2026-08-10. Tran B et al., Abstract 500 LBA,
EORTC-NCI-AACR 36th Symposium. Phase I/II SURF301, NCT05544552, TYRA Biosciences.

## Files

| file | what it is |
|---|---|
| `surf301_ena2024_text.txt` | full text layer, all 23 slides |
| `pg04.png` | erdafitinib adverse reactions ≥15 %, grouped FGFR2 / FGFR1 / other (n=135) |
| `pg05.png` | **erdafitinib dose-modification table — the slide that overturns round 212 (CORR-206)** |
| `pg06.png` | Ba/F3 cellular IC50 panel, five FGFR inhibitors, identical conditions (CORR-207) |
| `pg12.png` | **steady-state PK with protein-binding-adjusted target-coverage lines, and the printed AUC table** |
| `pg13.png` | UM-UC-14 xenograft against individual human steady-state AUCs, murine 18 mg/kg anchor |
| `pg18.png` | TYRA-300 TRAEs at 90 mg QD by receptor axis (n=15) |

## Why the PNGs are here and the text layer is not enough

The text layer of `pg06` exposes only two numbers from that figure, **459** and **142**. Dividing them
by the printed 63× and 19× selectivities produces a *self-consistent* TYRA-300 FGFR3 IC50 of ~7.3 nmol/L.
Rendering the page shows those are **infigratinib's and pemigatinib's FGFR4 values sitting past an axis
break**, and the true value is **~1.75 nmol/L** — a fourfold error that agreed with itself. The derived
protein binding, and therefore the entire free-concentration comparison in round 213, depends on getting
that right. See CORR-207.

`pg12`'s four horizontal reference lines carry no printed values — they are read by pixel against the
log-decade ticks. Those reads are the **only** estimated inputs to
`atlas/tools/fgfr3_free_coverage_ledger.py`, and each is cross-checked against an independently printed
IC50 from `pg06`; three isoforms agree on a 93–109× offset and the unused fourth line then falls out at a
physically sensible Hill slope.

## The numbers this document put into the atlas

- **Printed** steady-state C1D15 AUC: 40 mg 2,270 (n=10) · 60 mg 4,360 (n=8) · 90 mg 10,300 (n=13) ·
  120 mg 23,578 (n=3) ng·h/mL. Exposure rises **faster than dose**.
- **Derived** TYRA-300 plasma protein binding ≈ 99 %.
- **Derived** free FGFR3 coverage: erdafitinib 7 mg = 4.01× IC50 (the 19.06 cm/yr case), 9 mg = 5.16×
  (label maximum); TYRA-300 90 mg = 4.33×, 120 mg = 9.91×.
- **Printed** erdafitinib dose modification: interruption 72 %, reduction 69 %, discontinuation 14 %,
  with hyperphosphataemia contributing only 7 % / 4.4 %.
- **Printed** MTD not reached; optimal dose not determined.
