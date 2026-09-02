# Round 161 — closing both arms to the maximum public data allows

Computed by this atlas 2026-08-09. Files: `sel_flagged.json` (253 actives with scaffold + alert flags),
`sel_activity.json`, `ppp_matrix.json` (full ChEMBL phosphatase selectivity matrix).

## THREAD B — the decisive negative

Enumerated **all 39 human Ser/Thr phosphatase targets in ChEMBL** and pulled every IC50/Ki/Kd.

| | count |
|---|---|
| molecules with any PPP-family value | **1,801** |
| with a **PP2A catalytic subunit** value | **16** |
| with a **PP4 catalytic subunit** value | **1** (fostriecin, 3.0 nM) |
| with **both PP2A and PP4** | **0** |
| with both PP2A and PP5 | 2 — calyculin A (12×, but PP1 0.14 nM), cantharidin (2.5×) |

**PP2A-versus-PP4 selectivity has never been measured for any compound.** Not a gap in a dataset — the
absence of a dataset. Since `theobald2013` attributes fostriecin's cellular phenotype to PP4C, the one
question that decides the arm cannot be asked with existing reagents.

**Four independent blockers on Thread B:** enzyme unidentified and resistant (SD-008) · no compound and
none cheaply makeable · no PP2A/PP4 counter-screen chemistry anywhere · prize bounded at **1.42×** tonic
in a stack that already has an FGFR inhibitor, against systemic pan-PPP liability with hepatic DLT.

→ **REMOVE as a compound arm. Retain as mechanism** (`wagner2021`, +4.3–8.8% femur on wild-type FGFR3).

## THREAD A — compound 1 confirmed best, by re-analysis the paper didn't publish

Re-ranked all 253 GC-B-selective actives on three axes:

| filter | result |
|---|---|
| distinct Murcko scaffolds | **208 of 253** — overwhelmingly singletons (HTS-noise signature) |
| PAINS A/B/C or BRENK flagged | **101 of 253 (40%)** |
| compounds scoring above compound 1 | 7 (up to 125.6% vs its 96.67%) — **all scaffold singletons**, Tanimoto 0.06–0.20 |
| best **clean AND scaffold-supported** alternative | **65.1%** |

One of the high-scoring singletons is **diazinon**, an organophosphate pesticide, at 74.4% — a fair
summary of what the singleton tail contains.

**Compound 1 (CID 647514) is the highest-activity compound in the entire selective set with real SAR
support** — its 5-arylfuran-2-thioamide amine scaffold has 4 members, the sister morpholine scaffold 3
more. Seven chemically coherent analogues, all active together. The authors chose correctly; this
reproduces their choice from raw data without using their reasoning.

### The liability the paper doesn't discuss

**Compound 1 is itself BRENK-flagged — for the thiocarbonyl.** And `ma2024` shows replacing the thioamide
with an amide causes **complete loss of activity**. The alert *is* the pharmacophore. It cannot be
designed out, and it is present in MCUF-42 too. Thioamides are a recognised metabolic-activation
liability and this would be chronic dosing.

### No intracellular activator exists

`robinson2011`: Gö6976 is a **competitive inhibitor** of GC-A/GC-B at the **catalytic GTP site** (Ki ~1 µM
in 1 mM ATP), and the paper states explicitly that neither staurosporine nor Gö6976 **activated** either
enzyme. Wrong site, wrong direction. With CORR-174, the intracellular allosteric site has a mapped residue
(Thr640/Ile624), a validated point-mutant positive control, and **no compound**.

## THE ANSWER — which compounds to add

**To the therapeutic stack: NONE, from either thread.** Compound 1 has no in vivo data, no PK, no
toxicology, an unremovable structural alert, and a sibling with 0.26% oral bioavailability. Thread B has
no compound at all.

**To the research programme: two, both purchasable.**
- `CID 647514` — compound 1, CAS **332862-27-8**, 14 vendors — potency benchmark, EC₅₀ 0.74 µM, Eₘₐₓ 112%
- `CID 3588620` — N-methylpiperazine analogue, 7 vendors — the charge probe

**Control point A** (vosoritide/navepegritide) remains the only arm with an actual drug — and Thread D
showed it is inaccessible for this case at any price.

**Honest summary of the CNP axis for this subject: one arm has a drug that cannot be obtained, one has a
probe that is not a drug, and one has neither.**
