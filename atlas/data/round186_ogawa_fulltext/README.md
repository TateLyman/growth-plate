# ROUND 186 — `ogawa2002` READ IN FULL

PDF supplied by the user. `ogawa2002_ft.txt` is the extracted text; `DECOMPOSITION.txt` and
`DOSE_SCHEDULE_TRADEOFF.txt` are verbatim tool output.

## The paper is better than its abstract

Tables 1 and 2 report **longitudinal growth rate by double tetracycline label** and **cell
production rate** (CPR = LGR / degenerative cell height — the Kember–Sissons construction). So
terminal cell height is recoverable by inversion.

| cohort | arm | LGR µm/d | CPR /d | **h_term µm** |
|---|---|---|---|---|
| young 6 wk | control | 207.0 ± 11.4 | 10.4 ± 1.1 | 19.90 |
| young 6 wk | **PTH** | 235.0 ± 18.8\* | 12.0 ± 1.0\* | **19.58** |
| adult 15 wk | control | 74.2 ± 4.5 | 3.5 ± 0.3 | 21.20 |
| adult 15 wk | **PTH** | 81.7 ± 8.4 ns | 3.8 ± 0.4 ns | **21.50** |

**h_term is flat at both ages.** Young: LGR 1.135 = CPR 1.154 × h_term 0.984. Adult: 1.101 = 1.086 ×
1.014. **85–90% of the effect is cell production, none is terminal cell height** — the opposite
signature to GH (round 183), which took 1.36× from h_term.

Cross-check: `hunziker1994` measured 19.5–29.8 µm by stereology in the same bone and species.

## Three corrections to this atlas

1. **The age gate was overstated (round 185).** Adult +10.1% vs young +13.5%, Cohen d = 1.11,
   **41% power at n=6**, n=14 needed. An underpowered positive, not a null. And the 15-wk plate
   (74 µm/d, 36% of young) is the closer analogue to bone age 16.
2. **The molecule was TERIPARATIDE** — synthetic hPTH(1-34), Asahi Chemical. Round 184's
   abaloparatide preference pointed away from the only supporting experiment.
3. **The authors state CORR-189 themselves, in 2002**: plate thickness and cell number "do not
   directly reflect the LGR"; LGR and CPR "may be more sensitive indices".

## The molecular question

- `hashmi2026` — PTHrP(67-139), carrying the NLS + C-terminus, independently **maintains chondrocytes
  in an immature state**; deleting it shortens all three zones and causes premature differentiation.
  **No 1-34 drug touches this arm.**
- `schipani1997` — but a **constitutively active PTH1R with no ligand at all rescues the growth plate
  of a complete PTHrP null.** The commitment-delay function is receptor-borne.

→ Teriparatide/abaloparatide are partial mimics with a ceiling below full-length PTHrP, but they hit
the arm that carries the term being targeted.

## The new problem

**Schedule and dose constraints pull apart.** Daily abaloparatide: 6.9× short on dose, 20× too
frequent. Weekly teriparatide: 2.9× too frequent, 68× short on dose. Nothing existing satisfies both;
the regimen that would is ~11.6 mg every 3 weeks, which nobody has given.

## Still open

CPR = amplification × pool-consumption rate. No resting-zone kinetics here. **The central question is
exactly as unanswered as before** — and it is the question that turned GH from an apparent
amplification agent into a pool-spending one.
