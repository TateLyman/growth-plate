# Round 293 — the effect size that was locked in a figure

`haraguchi2025` (PMID 41509161, Acta Histochem Cytochem 58(6):187–198, CC BY-NC) reports
its femur-length result as *"a statistically significant increase in femur length in cKO
mice at both stages (Fig. 6b, d)"* and gives **no mean, no SD and no percentage anywhere
in the text**. Rounds 285 and 290 recorded the effect size as "figure-only" and moved on.

It is not unobtainable. The article is open access on J-STAGE; the PDF page carrying
Figure 6 was rendered at 420 dpi and read directly. The two PNGs here are those renders,
kept so the digitisation is auditable rather than asserted.

**Every number derived from them is a reading off a scatter plot and is marked
`value_unverified: true` in the graph.** Axis ranges are stated so a reader can check:
Fig 6b y-axis 1.3–1.7 cm, Fig 6d 1.4–1.8 cm, Fig 6i 0.0–0.8 mm².

Significance codes are the paper's own and are NON-STANDARD — its legend reads
`*p < 0.01; **p < 0.001; ***p < 0.0001`.

| panel | age | endpoint | control | mutant | delta | code |
|---|---|---|---|---|---|---|
| 6b | 10 wk male | femur length | ~1.49 cm (n=6) | ~1.53 cm (n=4) | **+0.04 cm, ~+2.7 %** | `*` p<0.01 |
| 6d | 53 wk male | femur length | ~1.55 cm (n=6) | ~1.62 cm (n=6) | **+0.07 cm, ~+4.5 %** | `***` p<0.0001 |
| 6i | 10 wk | growth plate area | ~0.44 mm² | ~0.62 mm² | **~+41 %** | `**` p<0.001 |
| 6i | 53 wk | growth plate area | ~0.29 mm² | ~0.44 mm² | **~+52 %** | `**` p<0.001 |
| 6b/d | both | body weight | — | — | **ns at both ages** | ns |

Two things the text never says and only the figure shows:

1. **Every skeletal panel is labelled MALE.** There is no female skeletal data in this paper.
2. **The 53-week cKO growth plate area (~0.44 mm²) equals the 10-week WILD-TYPE value
   (~0.44 mm²).** Wild-type plate area falls 0.44 → 0.29 mm² over that interval; the
   mutant's falls 0.62 → 0.44. The mutant reaches at 53 weeks the plate size a normal
   mouse has at 10.
