# Round 202 — the h_term axis exists, and it saturates

## What this round was trying to answer, and why this question

Not chosen by interest. Chosen by enumerating every open gap against the four stack agents and asking
which answer would **change what we do**.

Round 198 fixed the objective function: `adult height = reserve × terminal cell height`. That makes
**h_term the only axis on which a gain is free** — a taller terminal cell adds length without spending
a division. Two of four stack agents were assigned terms that CORR-189 says were never verified. And
the atlas's own gap said the axis might not exist at all:

> `g_l1_raise_terminal_cell_volume`: "no evidence the parameter can be pushed upward at all rather
> than only downward, and every manipulation on record LOWERS it"

**If that held, the free axis was imaginary** and the programme reduced to preserving reserve plus the
unsolved second-signal problem from round 201.

## It does not hold

`weber2025` (Nat Commun, mouse and jerboa tail vertebrae), Npr3-null against wild-type siblings, P7:

| measurement | result |
|---|---|
| **max hypertrophic cell height, in the axis of elongation** | **+~20 %** |
| hypertrophic **zone** height at TV6 | ~2.0× |
| proliferative zone height | significant in only 1 of 4 cartilages |

The cell is measured **axially and separately from the zone** — the measurement CORR-189 demands and
the one the atlas could not find for any CNP-axis agent. **First intervention in the file to raise
terminal cell height rather than lower it.**

But the decomposition cuts against the enthusiasm: zone 2.0× ÷ cell 1.2× ⇒ **~1.67× more cells per
column**. Two thirds of the effect is extra cells, one third is bigger cells. NPR3 loss is mostly a
cells-per-column agent.

**And the decisive half is unmeasured.** Extra hypertrophic cells from extra divisions *spend* reserve;
from delayed clearance they do not. The Npr3 arm carries **no calcein and no EdU** — both methods are
in the paper, used only on the mouse/jerboa comparison — and Npr3 mice are independently catalogued
with *delayed endochondral ossification*, which points at clearance. New gap opened.

## The exchange rate — the number that justifies the whole axis

Author-stated in `weber2025` with citations:

> one doubling of a flattened proliferative chondrocyte adds **8–9 µm** to the axis of elongation;
> that same cell then adds **up to 40–50 µm** through hypertrophic enlargement

**≈ 4.4–6.3×.** The division is the cheap part of the transaction and the expensive part of the budget
— it costs one unit of an exhaustible reserve and returns about a fifth of what the hypertrophy of the
same cell returns for nothing.

## `hunziker1994` re-read as a dose-response — the uncomfortable one

Held since round 172, always read as four treatments. Read as a **dose ladder in pool consumption**:

| group | GR µm/d | h_term µm | pool consumption /col/d | amplification |
|---|---|---|---|---|
| saline | 31 | 19.5 | 1 | 1.59 |
| IGF-I | 92 | 27.3 | 3 | 1.12 |
| GH | 163 | 26.5 | 6 | 1.03 |
| normal | 284 | 29.8 | 10 | 0.95 |

| step | h_term gain | pool cost |
|---|---|---|
| saline → IGF-I | **+40.0 %** | 3.00× |
| IGF-I → GH | −2.9 % | 2.00× |
| GH → normal | +12.5 % | 1.67× |

**h_term saturates. Pool consumption does not.** The first tripling of consumption buys 40 % of the
available terminal cell height; the next 3.3-fold buys 9 %.

Under `adult height = reserve × h_term`, **a saturating benefit against a linear cost has an interior
optimum.** The somatotropic dose that maximises adult height is the **lowest one that saturates
h_term**, not the highest tolerated one. That is the opposite of how the axis is dosed and the opposite
of what this stack assumed.

**Not claimed:** that IGF-I beats GH. 27.3 vs 26.5 µm at n=6 is noise, and the doses were never matched
for equipotency. If both agents sit on one curve, the only surviving claim is the saturation shape —
which is still the actionable one.

## The stack consequence

Three results put **three agents on one term**: `cooper2013` assigns h_term to IGF-1 (Igf1-deficient
mice — same *number* of hypertrophic chondrocytes, each 30 % shorter axially, and IGF1 loss abolishes
the between-bone height difference); `hunziker1994` gives GH 1.36×; `weber2025` gives the CNP/NPR3 axis
1.20×.

If the term saturates, **two h_term agents are sub-additive by construction** and the second is paid
for at full reserve cost. The stack contains GH *and* vosoritide on the assumption they stack. **No
terminal cell height measurement exists under vosoritide in any species** — the CNP evidence the atlas
leans on (`agoston2007`) reports a hypertrophic *zone* height, which CORR-189 forbids reading as a cell
claim. This is now the most decision-relevant unmeasured quantity in the stack.

## A third independent line against rate agents

`weber2025` measured 2-hour EdU proliferation index across growth cartilages differing **more than
twofold** in calcein-measured daily elongation, in two species: **the S-phase fraction is not
significantly different.** Faster bones are not built by faster division.

## The spine question, which matters for this case specifically

| source | finding |
|---|---|
| `weber2025` (mouse) | Npr3 loss **disproportionately** elongates proximal and mid-tail **vertebrae** |
| `lauffer2022` (human) | biallelic NPR3 loss → 205.1 cm at 14.7 y, **normal sitting-height ratio and arm span** — proportionate |
| `moffatt2025` (human) | tall stature **with scoliosis** — a spine phenotype |

**No segment-resolved human growth measurement exists under any CNP-axis agent.** The atlas should stop
assuming spine and limb respond alike. Recorded in the node's `contradicts`.

## Ledger for this round

**Closed / advanced**
- h_term *can* be raised — `g_l1_raise_terminal_cell_volume` premise overturned, gap text updated in place
- the exchange rate is quantified (~5× per cell, and only the cheap half is deducted from reserve)
- the NPR3 route's term assignment now exists (mostly cells/column, minority h_term)
- differential elongation is not achieved by a higher S-phase fraction (2 species, >2× contrast)
- human NPR3 LOF gain is proportionate, so the route is not spine-selective

**Opened**
- `g_l1_are_the_hterm_agents_in_the_stack_additive_or_saturating` — the top unmeasured quantity
- `g_l1_do_the_extra_hypertrophic_cells_under_npr3_loss_cost_divisions`

**Still open and now more urgent**
- `g_l1arch_009` — no human hypertrophic cross-sectional area exists, so no human h_term volume can be computed
- `g_l2_what_is_the_second_signal_that_converts_an_alerted_pool_into_columns` (round 201) — but the
  exchange rate says the pool route buys length at the *least* efficient point in the transaction, so
  h_term should be worked in parallel, not after

## Files

| file | what it is |
|---|---|
| `hterm_ledger_output.txt` | `atlas/tools/hterm_axis_ledger.py` — exchange rate, Npr3 decomposition, the dose-response re-read |
| `jerboa_tail_npr3.xml` / `.txt` | `weber2025` full text, Europe PMC `PMC12514186` (CC-BY) |
