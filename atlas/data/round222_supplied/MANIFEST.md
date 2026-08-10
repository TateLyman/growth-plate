# Round 222 — the inventors' own patent, and the published Breinholt tables

User-supplied 2026-08-10. Two of the three were on the ask list; the third (a second copy of the Breinholt
accepted manuscript) duplicated `atlas/data/round221_supplied/breinholt2019.txt`.

| file | source | ref_id | what it settled |
|---|---|---|---|
| `WO2017055370_ocr.txt` + `wo2017055370_figure17_no_wildtype_arm.png` | **WO 2017/055370 A1**, "Treatment of bone growth disorders", Fondazione Telethon; inventors **Settembre C, Cinque L, Bartolomeo R, Auricchio A, Trapani I, Toriello E**. PCT/EP2016/073149, filed 28 Sep 2016, published 6 Apr 2017, priority 62/233,687 of 28 Sep 2015 | `wo2017055370` | **ASK #1, closed.** Figure 17 f–h carries the panel absent from the Nature main text, with **exactly three keys and three bars**: Fgfr4 +/+ vehicle, Fgfr4 −/− vehicle, Fgfr4 −/− Tat-Beclin 1. **No wild-type treatment arm exists.** Collagen ~100 / 65 / 90 %; femur length P9 ~100 / 89 / 97 %; P15 ~100 / 93 / 98 % — restoration to just below the wild-type bar, never above. Also **Example 2**: FGFR3 G380R and R248C chondrocytes have **blocked autophagic flux** (leupeptin + bafilomycin fail to raise LC3-II vs FGFR3-WT; FACS agrees). And the patent **claims mTORC1 inhibitors while its own background cites the evidence they reduce longitudinal growth** — see CORR-223. Third claimed class, **BH3 mimetics**, has no bone data anywhere in it. |
| `breinholt2019_published_jpet.txt` | Breinholt VM et al., *J Pharmacol Exp Ther* **370:459–471**, September 2019 (typeset version of the accepted manuscript archived in round 221) | `breinholt2019` | **ASK #4, the magnitudes.** **Table 5** — FVB mice, 5 wk, CNP-38 **203 µg/kg/day, same dose both arms**: femur +5.5 → +7.1 %; tibia +4.0 → **+12.2 %**; **spine +11.3 → +25.0 %**, tibia and spine formally different from bolus (P<0.05). These are **wild-type** mice; the authors write that growth "even in a healthy animal with normal endogenous CNP levels" can be greatly accelerated by sustained exposure. **Table 6** — bone formation markers **dissociate from length**: daily CNP-39 gave BAP +51 % / PINP +144 % while delivering a third to a half the length of TransCon (BAP +14 % / PINP +53 %). |

## How the patent was read

The PDF is **image-only** (4 patent pages per sheet, no text layer). It was OCRed page-quadrant by
page-quadrant with tesseract for the text, and **Figure 17 was read from a 300-dpi render** of the quadrant
containing it. **Bar heights are approximate (±~2 percentage points); the arm count is not** — the legend
lists three keys and the panels show three bars. The render is archived so the reading can be checked.

## Corrections this bundle produced

- **CORR-222** — the atlas's "an hour a day is enough" model, taken from a *competitor's* patent figure in
  rat chondrosarcoma cells, predicted the clinical wash that CORR-221 showed the trials could not resolve.
  Table 5 refutes it at the level of bone length.
- **CORR-223** — a mechanism-defined drug class is not a shortlist. The clinically available members of the
  "autophagy activator" class are mTORC1 inhibitors, and `alvarezgarcia2007` (94 vs 182 µm/day, a **48 %
  reduction**, at the same 2 mg/kg/day IP dose used for Tat-Beclin 1) and `hymes2011` (lower growth velocity
  in children on sirolimus) show they reduce growth.

## Still on the ask list

1. **A cell-level decomposition for navepegritide** — still the decisive missing measurement; the TransCon
   primate toxicology package has the slides and needs no new animals.
2. The SURF301 **FGFR4 PD analysis**, stated on the poster as ongoing.
3. `weinstein1998` — the user judges it unlikely to carry the skeletal detail; the Fgfr3/Fgfr4 double-null
   bone phenotype is being pursued by other routes.
