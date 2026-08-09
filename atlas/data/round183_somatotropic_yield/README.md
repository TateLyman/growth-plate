# ROUND 183 — THE SOMATOTROPIC AXIS IS NOT A YIELD AXIS

`hunziker1994ft.txt` is the extracted full text of Hunziker, Wagner & Zapf, *J Clin Invest*
93:1078–1086 (1994), PMID 8132747. Every input to the computation is an **author-stated** number
from Table II or a figure legend — none is digitised from a plot.

`OUTPUT.txt` is the verbatim output of `atlas/tools/hunziker1994_amplification.py`.

## The identity

    P = GR / h_term                    Kember–Sissons cell production per column per day
    D = N_rest / T_stem                resting cells leaving per column per day
    A = P / D                          AMPLIFICATION, hypertrophic cells per progenitor consumed

    GR = A × D × h_term                exact, zero residual

## Result

| | saline | IGF-I | GH | normal |
|---|---|---|---|---|
| growth rate (µm/d) | 31 | 92 | 163 | 284 |
| terminal cell height (µm) | 19.5 | 27.3 | 26.5 | 29.8 |
| resting cycle time (d) | 50 | 15 | 8 | 6 |
| resting cells/column | 2.5 | 2 | 2 | 2.5 |
| **amplification** | **31.8** | **25.3** | **24.6** | **22.9** |

GH: 5.26× = 5.00× pool consumption × 1.36× h_term × **0.77× amplification** (pool term = 97% of the
log effect). IGF-I: 2.67 × 1.40 × **0.79** (90%). Normal vs hypox: 8.33 × 1.53 × **0.72** (96%).

## Three internal validations

1. `GR / h_term` reproduces Hunziker's own independent stereological turnover count in every group
   (1.59/3.37/6.15/9.53 against a stated 1/3/6/10).
2. `log2(A)` = 4.99/4.66/4.62/4.52 — four to five doublings — in columns the same paper reports as
   holding 14–18 proliferative cells.
3. Forcing the resting count identical across groups gives a GH ratio of **0.62**, and the GH
   resting cycle time would have to be understated by ~30% before amplification reaches parity.

Written to the atlas as `the_somatotropic_axis_is_not_a_yield_axis`, edges `e01328`–`e01332`, gap
`g_l2_does_fgfr3_inhibition_raise_cells_per_column_or_only_zone_height`, and **CORR-189**.
