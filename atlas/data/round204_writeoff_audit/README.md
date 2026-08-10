# Round 204 — vosoritide decomposed in a primate, and the write-off site audit

## 1. The vosoritide term assignment exists, and round 203 was wrong that it didn't

`wendt2015` (user-supplied) was held here as a **ref_id with no finding and no note**. Its Table 3
carries four of the five Hunziker quantities **in the same animals, in cynomolgus monkeys, at 6 months**.

| parameter | vehicle | 2.25 nmol/kg/d | 8.25 nmol/kg/d | high/veh | P |
|---|---|---|---|---|---|
| longitudinal growth rate (µm/day) | 26 ± 7 | 26 ± 5 | 40 ± 9 | **1.54×** | <0.05 |
| growth plate thickness (µm) | 555 ± 61 | 594 ± 64 | 682 ± 48 | 1.23× | <0.05 |
| proliferating zone thickness (µm) | 125 ± 10 | 139 ± 89 | 196 ± 14 | 1.57× | <0.001 |
| **proliferating cells/column** | **13 ± 2** | 11 ± 2 | **11 ± 1.6** | **0.85×** | **N.S.** |
| hypertrophic zone thickness (µm) | 72 ± 26 | 89 ± 23 | 128 ± 56 | 1.78× | <0.05 |
| **hypertrophic cell "volume" (µm²)** | 232 ± 30 | 258 ± 56 | 286 ± 34 | 1.23× | **N.S.** |

**Cells per column FALLS, at both doses.** Vosoritide does not buy length by adding divisions.

**The cell-size column is labelled "volume" and its unit is µm² — a projected AREA.** CORR-190 bars
reading it as a length, and `cooper2013` shows why it matters: jerboa hypertrophic cells are 2.9× the
*volume* of mouse but only 1.58× the *height*.

Closing the identity `GR = A × D × h_term`:

```
growth rate         1.54×   (the only significant term)
cells per column    0.85×   (N.S.)
implied cell height 1.11×   (N.S., √area, isotropy assumed — and cooper2013 says isotropy is false)
RESIDUAL            1.64×   → sits on POOL CONSUMPTION
```

**The primate data reads: vosoritide buys its growth by spending the reserve faster.** That is the
unfavourable assignment and it puts vosoritide in the growth-hormone category, not the free-axis
category the stack assumed.

**Direction, not verdict.** n = 4; the authors write the study *"was not powered for significance"*;
both decomposition terms are N.S.; the cell measure is an area; cells/column is a *standing count* in
the proliferative zone, not the amplification term; and pool consumption is a **residual**, so it
absorbs every error in the other terms.

**Cheap fix, no new animals:** wendt2015 embedded left tibias in MMA and cut five 7-µm sections per
animal with calcein/oxytetracycline double labelling. Re-measuring terminal cell height *axially* on
those sections converts the area into the term the decomposition needs.

## 2. The write-off site audit (CORR-199)

CORR-195's rule — no agent scored against one site — applied **backwards**. 1,436 refs scanned; 22
carry a negative length statement; **8 measured through a single skeletal region**; all 8 resolved by hand.

**One genuine hit: `wang2018` / tadalafil**, titled *"...on **long bone development** in young rats."*
It is one of two legs under "stacking inside the cGMP node is dead." The other leg, `hakata2024`, used
**naso-anal length** — axial, therefore sound. **Verdict not reversed** (hakata2024 carries it, and has
the better design) but downgraded from *two independent negatives* to *one whole-body + one single-site*.

Everything else cleared: `trompet2024`'s systemic null is a **timing** artefact the atlas already
recorded (length read 2 days after a 7-day exposure); `koh2022` also measured cranial base and
synchondrosis lengths; `loqman2013`/`bush2010` are single-bone by design; `brjesson2012` is a positive
finding.

**No compound was written off for want of spine data.**

## 3. What the audit found instead — and it's better than what it looked for

`bush2010` was sitting in the null bucket while being a **positive** result: NKCC1 inhibition cut
metatarsal elongation ~35 % with **hypertrophic zone height 204 → 151 µm and cell NUMBER unchanged
(193 vs 192, p = 0.937)**. Cell number explicitly held constant ⇒ CORR-189 *and* CORR-197 satisfied ⇒
the zone change **is** a cell-size change. With `abubakar2022` (NHE1/AE2), **ion transport is a named,
isolated control point on the free axis** — downward only, so far.

## 4. CORR-198 — two over-strong negatives withdrawn

- Round 203's *"no cell-level measurement exists on the CNP axis"* — false (wendt2015). The narrow
  version survives: no **axial height**.
- Round 202's *"weber2025 is the first intervention to raise terminal cell height"* — false.
  `trompet2024` measured it in both arms: **null systemic**, **elevated by intra-articular bead**.

**The h_term axis has at least four agents with a cell-level signal**: hedgehog by local bead
(`trompet2024`), NPR3 loss (`weber2025`, +20 % axial), resveratrol (`karimian2013`, "increased number
and size of hypertrophic chondrocytes"), ion transport downward (`bush2010`, `abubakar2022`). Note the
**route split** — systemic SAG moved nothing, the local bead did.

## Files

| file | what it is |
|---|---|
| `vosoritide_decomposition_output.txt` | `atlas/tools/vosoritide_term_decomposition.py` |
| `audit_output.txt` | `atlas/tools/writeoff_site_audit.py` — the 22 negatives bucketed by site |
| `wendt2015.pdf` / `.txt` / `wendt2015_table3.png` | source and the 500 dpi Table 3 render |
| `trompet2024.txt` | full text, PMC11063944 — the both-arms cell-size check |
