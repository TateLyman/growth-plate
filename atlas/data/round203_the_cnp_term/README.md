# Round 203 — the CNP axis is linear where the somatotropic axis saturates, and its term is still unmeasured

## What this round was answering

Round 202 left one question as the most decision-relevant unmeasured quantity in the stack: **does the
CNP axis raise terminal cell height — the free axis — and does it saturate the way the somatotropic axis
does?** This round answers the second and establishes that the first cannot currently be answered by
anyone.

It also fixes a framing error the user caught: rounds 199–202 had drifted from "spine and knee reserve"
to **"spine reserve"**. See `open_growth_sites_at_bone_age_16` (L9) and CORR-195.

## The saturation answer is the opposite of the somatotropic one

`jeong2026` — held in this bibliography **as a bare citation with no finding, never read** — functionally
characterised **245 NPR2 missense variants** from UK Biobank: 47 loss-of-function, 34 partial, **14
gain-of-function**.

| | |
|---|---|
| shape | **near-linear** activity score → standing height |
| fit | R² = 0.438, p = 5.8 × 10⁻¹⁰ |
| additivity | polygenic scores combine **additively** with the variant effect |
| direction | LoF enriched in the **shortest**, **GoF enriched in the tallest** |
| PheWAS | NPR2 activity associated **only** with height and height-associated traits |
| authors' own word | **"a dimmer switch"** |

Round 202: h_term **saturates** against somatotropic drive — 40 % of the gain in the first tripling of
pool consumption, 9 % in the next 3.3-fold. **The CNP axis shows no such ceiling.**

**The two arms of the stack should be dosed by opposite logic, and currently are not.**

## The site answer is favourable

`cnpmeta2026`, 4 RCTs, n = 326, low risk of bias: **upper-to-lower segment ratio unchanged, MD −0.02
(95 % CI −0.04 to +0.01), P = 0.17, I² = 0**, vosoritide and navepegritide separately both −0.02.
Against a register of *several* simultaneously open sites, an agent that grows the segments
proportionately is the right kind of agent.

Age gradient also runs the helpful way: **+1.63 cm/yr at age ≥5 vs +0.91 under 5, subgroup P = 0.01.**
Still stops far short of BA 16, and adult height is explicitly not yet known.

## The constitutive end, which the atlas had never read as a census

Six human strong-activation reports, held individually, never tallied:

| feature | count | reports |
|---|---|---|
| **digital overgrowth** | **4/6** | `lauffer2020`, `miura2012`, `miura2014`, `moffatt2025` |
| **scoliosis** | **3/6** | `miura2012`, `miura2014`, `moffatt2025` |
| aortic root dilatation | 1/6 | `boudin2018` (2 of 4 individuals, progressive) |

**Digital overgrowth is the most consistent non-height feature** — macrodactyly of great toes, elongated
proximal and middle phalanges, additional and pseudo-epiphyses of phalanges and metacarpals. **The
phalanges contribute nothing to stature.** At maximal activation a visible share of output goes to sites
with zero height value.

**Scoliosis is a yield term, not only a safety term.** `moffatt2025`: all three siblings, **one requiring
spinal fusion surgery** — which ends spinal growth outright — with lumbar BMD low for the height
achieved. A curve converts axial length into deviation.

**These three points are not in conflict — they are three points on one dose curve**, and the atlas had
been quoting whichever suited the paragraph. The population PheWAS samples the *mild* end by
construction and cannot exclude the constitutive phenotypes; the constitutive families are germline and
lifelong and do not bound a months-long exposure.

Ascertainment caveat stated in the node: these families are diagnosed partly *on* the digital features,
so 4/6 is inflated by design.

## The term is unmeasured — and that is a fact about the literature, not about our reading

Full texts obtained and exhaustively searched:

| paper | what it measures | cell dimension? |
|---|---|---|
| `hirota2018` (the wild-type CNP result) | growth plate **thickness**, 9 femoral + 5 tibial/calcaneal sites, plus HZ and non-HZ zone thickness | **none anywhere** |
| `nakao2015` (Nppc / Npr2 cKO) | **layer thickness** — HZ to 34.6 % and 23.0 % of control, non-HZ to 76.7 % and 71.1 % | **none anywhere** |
| `agoston2007` | hypertrophic **zone** expansion | none |

**No terminal cell height has been measured under any CNP-axis agent in any species.** `weber2025`'s
+20 % is **NPR3 loss** — the clearance arm, not NPR2 agonism, in a receptor the atlas separately records
as bifunctional.

## CORR-197 — and this makes it worse, not just incomplete

`nakao2015` reports that in **both** knockouts *"the extracellular spaces of the non-hypertrophic
chondrocyte layer were greatly decreased."*

CORR-189 said a zone height is cells/column × cell height. **It is cells/column × cell height PLUS
EXTRACELLULAR MATRIX — and the CNP axis moves the matrix term.** So the entire CNP zone-height
literature is consistent with a matrix effect, a cell-number effect, a cell-height effect, or any
mixture, and **cannot be decomposed even in principle** from what is published. TUNEL in the same paper
shows apoptosis almost unchanged, so clearance *is* excluded.

## Ledger

**Closed**
- does the CNP axis saturate in humans? **No** — near-linear, GoF end populated (`jeong2026`)
- does it grow one segment at others' expense? **No** — ULS ratio unchanged, I² = 0 (`cnpmeta2026`)
- does a terminal cell height exist under any CNP agent? **No** — established by exhaustive full-text search

**Opened**
- `g_l12_does_a_cnp_agent_change_terminal_cell_height_or_matrix` — with a cheap version needing **no new
  animals**: re-measure cell height and cells/column on the existing `hirota2018` or `nakao2015` histology

**Corrections**
- CORR-195 — the open-site register; no agent scored against one site ever again
- CORR-196 — round 202 was wrong that no segment-resolved human CNP data exists
- CORR-197 — a zone height has three terms, and the CNP axis moves the third

## Files

| file | what it is |
|---|---|
| `cnp_dose_census_output.txt` | `atlas/tools/cnp_axis_dose_census.py` — the three dose points and the phenotype tally |
| `hirota2018.xml` / `.txt` | full text, PMC6147488 — searched, no cell dimension |
| `nakao2015.xml` / `.txt` | full text, PMC5395013 — the matrix observation behind CORR-197 |
| `npr2_activity_scores.xml` / `.txt` | `jeong2026` full text, PMC12824620 |
