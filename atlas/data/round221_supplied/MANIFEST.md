# Round 221 — three supplied documents, and the first refutes the round committed hours earlier

User-supplied 2026-08-10, against the ask list at the end of round 220. All three were on it.

| file | source | ref_id | what it settled |
|---|---|---|---|
| `breinholt2019.txt` | Breinholt VM et al., *J Pharmacol Exp Ther* 2019, JPET #258251, doi 10.1124/jpet.119.258251 — 57 pp | `breinholt2019` | **ASK #4, and it refutes round 220.** The primate head-to-head exists: 26-week juvenile cynomolgus, n=4/group, TransCon CNP 100 µg CNP/kg/**week** vs a daily CNP-39 molecule with **the same amino acid sequence as vosoritide** at 20 µg CNP/kg/**day**. Tail **+9 vs +3 %**, tibia +6 vs +3, body +5 vs +3, proliferative zone width **+37 vs +16 %**, epiphyseal plate thickness **+16 % significant vs +7 % n.s.**, hypertrophic zone equal (38 vs 39). The daily arm got **140 µg/kg/wk vs 100** — the weekly prodrug won on 71 % of the peptide. Plus the cleanest schedule test possible: same molecule, same daily dose (CNP-38 203 µg/kg/d, 5 wk, n=9 FVB), **bolus vs continuous osmotic-pump infusion — continuity wins.** PK: CNP-39 t½ 20 min / exposure ≤2 h; released CNP-38 apparent t½ 90 h / ≥7 d at ~100-fold lower Cmax. CNP-39 and free CNP-38 lowered BP and/or raised HR; TransCon did not. |
| `surf301_loriot_pk_pd_poster.txt` + `surf301_fgf19_klb_boxplots.png` + `surf301_col9a1_ctdna.png` | SURF301 PK/PD poster, Loriot Y et al. (TYRA-300) | `surf301_pb060_2024` | **ASK #3.** The figure, rendered at 200 dpi and read against its printed axis. FGF19 C1D15 log₂FC **+0.15 / +0.95 / +1.80 / +1.40** at 40/60/90/120 mg = 1.11× / 1.93× / **3.48×** / 2.64×. KLB **−0.30** / +0.45 / +0.85 / +0.85 = **0.81×** / 1.37× / 1.80× / 1.80× — the co-receptor **falls at 40 mg** before rising. COL9A1 C2D1 log₂FC +0.25 / +0.15 / +0.90 / **+1.05** = up to 2.07×, **rising**. Also states exposures "above the IC90 for FGFR3 inhibition that are below the IC50 for FGFR1/2/4". **ASK #5 (the FGFR4 PD analysis) is still open** — the poster says it is ongoing. |
| `cinque2016_cell_cycle_editorial.txt` | Cinque L, Forrester A, Settembre C, *Cell Cycle* 2016;15(7):871–872, doi 10.1080/15384101.2016.1151724 | `cinque2016_editorial` | **ASK #1, partially.** The authors' own summary of `cinque2015`. States FGF18 acts "mainly through FGFR4, and **to a lesser extent through FGFR3**" — upgrading the FGFR3 contribution from in-vitro-only. Describes the Tat-beclin-1 result three times and **every description is restoration language**; no wild-type elevation is claimed anywhere. Points to `wang2015_ach_autophagy` (PMID 26491898): **defective autophagy in an achondroplasia mouse growth plate**, i.e. FGFR3 overactivity suppresses the arm. |

## Reading discipline for the rendered figure

The box-plot medians above are **read from a 200-dpi render against the printed axis, good to about
±0.15 log₂ units**, and are **not sponsor-stated values**. The rule comes from round 213, where text-layer
extraction of a figure nearly put a misread potency into the atlas: reading a figure means rendering it
**and** stating how precisely it was read. The two crops are archived so the reading can be checked.

## Still on the ask list after this bundle

1. `cinque2015` **Extended Data Fig. 9g–i** — the Tat-beclin-1 magnitudes and whether a wild-type arm exists.
2. `weinstein1998` full text (Development 125:3615) — the user judges it unlikely to carry the skeletal
   detail; the search continues elsewhere.
3. The SURF301 **FGFR4 PD analysis**, stated on the poster as ongoing.
4. Any **cell-level decomposition for navepegritide** — still the decisive missing measurement, and now
   more urgent, because the drug that wins the head-to-head is the one whose term assignment is unknown.
