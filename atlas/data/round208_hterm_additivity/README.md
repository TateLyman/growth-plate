# Round 208 — restoration is not elevation, and the two arms may be complementary

## The additivity question, worked — and it failed on its premise

**CORR-203.** Round 205 said the h_term range across every agent is "1.0–1.4×", quoting `hunziker1994`'s
1.36× (GH) alongside `weber2025`'s 1.20× (NPR3 loss). **Different kinds of number.**

| baseline | ratio | |
|---|---|---|
| RESTORATION — hypophysectomised → GH | 1.36× | **does not reach** the intact control |
| RESTORATION — hypophysectomised → intact | 1.53× | the ceiling of restoration |
| **ELEVATION** — NPR3 loss vs wild-type littermate | **1.20×** | above a *normal* baseline |
| **ELEVATION** — hedgehog bead vs contralateral limb, 1 mo | **1.18–1.25×** | above a *normal* baseline |
| same, femur at 2 mo | 0.93× | does not persist |

GH brings a hypophysectomised rat to **26.5 µm** against an intact control's **29.8 µm**. **There is no
evidence anywhere that GH raises h_term above a normal baseline** — graded X. Headroom above normal is
about **21 %**, not 40 %.

**So the gap's premise fails**: it asked whether GH and a CNP agent share an h_term ceiling; GH has
nothing to add. The live version is the **hedgehog vs natriuretic** arms — and an enumerated search
found **no study in any species has given two growth-plate agents together and measured terminal
hypertrophic cell height.** Hard negative.

## The comparison the atlas had the pieces for and never made

`tyra300_2025` was in the bibliography with its headline recorded but **not its numbers**. Read properly:

**Wild-type C57BL/6J, oral daily 4→8 wk:** naso-anal **+7.3 %**, femur **+8.2 %**, tibia **+6.4 %** at
14 mg/kg; femur +5.0 %, tibia +3.9 % at 12 mg/kg; significant at 8 and 10 mg/kg too. **"No difference in
body weight among the treatment groups"** — clears the CORR-191 confound that spoils most length results
in this file. Also: **lumbar vertebrae length ↑**, skull and **foramen magnum** improved, hypertrophic
chondrocytes **larger**, and the plate **more organised**.

Against rounds 205/207 for the CNP axis:

| | FGFR3-selective inhibition | CNP axis |
|---|---|---|
| normal animal | **elevates** (+8.2 % femur, no wt confound) | dose ceiling = growth plate **dysplasia** at 0.08–0.2× human exposure |
| lumbar vertebrae | **increased** | **no change** (primate), only non-sig segment (TD mouse) |
| skull / foramen magnum | **improved** | **no change** |
| plate architecture | **more organised** | **dysplasia** at ceiling |

**If that holds the two arms are complementary by site, not redundant** — the most consequential thing
this stack could learn. New gap `g_l12_are_fgfr3_inhibition_and_the_cnp_axis_complementary_by_site` with
a four-arm wild-type experiment specified.

**The caveat that must travel with it: TYRA-300 is not erdafitinib.** TYRA-300 is FGFR3-**selective**,
designed for paediatric growth; erdafitinib is pan-FGFR at oncology dosing — which is where this atlas's
physeal and laryngeal cartilage findings come from. **The atlas has been carrying the FGFR arm under the
wrong molecule.**

## The question ledger

`atlas/tools/open_question_ledger.py` → `question_ledger.txt`. **14 questions opened since round 199**,
each with status, what would close it, and who can get it. **8 of 14 need no new animal and no new
patient.**

## Files
`baseline_audit.txt`, `question_ledger.txt`, `tyra300.txt`, `ctcmnp.txt`.
