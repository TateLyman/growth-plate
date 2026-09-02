# ROUND 184 — THE YIELD CANDIDATE

**Intermittent PTH1R agonism. Abaloparatide over teriparatide.**

## Why it wins

| | evidence |
|---|---|
| exact mechanistic match | amplification = commitment delay; PTHrP→PTH1R *is* the commitment-delay signal; abaloparatide is a PTHrP(1-34) analogue |
| **wild-type positive** | `ogawa2002` — normal, normally-loaded 6-wk rats: growth plate thickness, chondrocyte number **and longitudinal growth rate** all up vs untreated controls |
| Jansen objection dissolves | `reyes2023` — humanized H223R-PTH1R plate has **expanded** proliferative/prehypertrophic zones; short because those cells **apoptose** instead of hypertrophying |
| schedule is the drug | `liu2012` — continuous PTH suppresses chondrocyte differentiation (COL10A1↓); intermittent enhances it (RUNX2, ALP, COL10A1↑) |
| ligand choice | `zhai2022` — teriparatide long-acting, abaloparatide short-acting at PTH1R. Qualified by `sato2021` (no difference in early pathway engagement) |

Everything else the programme found was a rescue (`xie2012`, `horike2026`), a pool addition
(`trompet2024`), or never measured for length.

## What is NOT established

`ogawa2002` reports a **zone height**, an unspecified "chondrocyte number", and a growth rate. Only
the last is a flux. **No terminal hypertrophic cell height and no resting-zone cycle time has ever
been measured under a PTH1R agonist**, so the growth-rate gain cannot be partitioned. Under CORR-189
this is a candidate with a positive endpoint and an unverified term.

Round 183 is the precedent: GH looked like an amplification agent to two separate nodes until the
flux quantities were computed and it came out at **0.77**.

## The two hard limits

- **Age gate.** `ogawa2002`'s effect was present at 6 weeks and **absent at 15 weeks**. The subject
  is at bone age 16. No dose escalation fixes an age gate.
- **Dose gap.** See `DOSE_GAP.txt` — HED ≈ 12.9 µg/kg/day ≈ 774 µg/day for 60 kg, about **10× the
  approved abaloparatide dose** and 39× teriparatide. `ogawa2002` ran a single dose, so the minimum
  effective dose is unknown.

The 94 paediatric patients in `tantivit2026` with growth "within normal ranges" are on **replacement**
dosing 13–26× below this HED. That is a safety anchor, not an efficacy null.

Written to the atlas as `the_yield_candidate_intermittent_pth1r_agonism`, edges `e01333`–`e01337`,
gap `g_l12_does_intermittent_pth1r_agonism_raise_amplification_in_a_wild_type_plate`.
