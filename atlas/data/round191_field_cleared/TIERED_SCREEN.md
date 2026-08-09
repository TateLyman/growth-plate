# ROUND 191 — TIERED SCREEN OF THE DECISION-RELEVANT SLICE

Auto-classification of the 275-record slice (131 after triage) by evidence type.

**Tier 1** = PTH1R agonist AND length endpoint AND in vivo — the only combination that can contain the result.
**Tier 2** = agonist + resting-zone/fusion mechanism. **Tier 3** = agonist in vivo, other endpoint.
**Tier 4** = growth biology, no agonist. **Tier 5** = background.

| tier | n | status |
|---|---|---|
| 1 | 5 | **ALL 5 READ** |
| 3 | 11 | all bone microarchitecture, no growth endpoint |
| 4 | 41 | growth biology without an agonist |
| 5 | 74 | background |

## Tier 1 (complete)

- [39883563] 2025 — Bone Health and Linear Growth in Children With Familial Hypoparathyroidism Treated With Human Parathyroid Hormone 1-34.
- [33434347] 2021 — Pleckstrin homology (PH) domain and Leucine Rich Repeat Phosphatase 1 (Phlpp1) Suppresses Parathyroid Hormone Receptor 1 (Pth1r) Expression and Signaling During Bone Growth.
- [32219165] 2020 — Regulation of body length and bone mass by Gpr126/Adgrg6.
- [26254742] 2015 — Quantification of skeletal growth, modeling, and remodeling by in vivo micro computed tomography.
- [11862529] 2002 — Human PTH (1-34) induces longitudinal bone growth in rats.

## Tier 3 (screened, none carry a growth endpoint)

- [42268882] 2026 — Nf2 orchestrates β-arrestin2-biased PTH1R signaling to couple bone mass with skeletal integrity.
- [34273687] 2021 — Activation, development, and attenuation of modeling- and remodeling-based bone formation in adult r
- [32483372] 2020 — PTH(1-34) treatment and/or mechanical loading have different osteogenic effects on the trabecular an
- [30354669] 2019 — Progenitor recruitment and adipogenic lipolysis contribute to the anabolic actions of parathyroid ho
- [29544022] 2018 — The Deletion of Hdac4 in Mouse Osteoblasts Influences Both Catabolic and Anabolic Effects in Bone.
- [24998454] 2014 — PTH1-34 alleviates radiotherapy-induced local bone loss by improving osteoblast and osteocyte surviv
- [21932346] 2012 — Proteoglycan 4: a dynamic regulator of skeletogenesis and parathyroid hormone skeletal anabolism.
- [22700192] 2012 — Mice lacking AMP-activated protein kinase α1 catalytic subunit have increased bone remodelling and m
- [21215827] 2011 — Low dose parathyroid hormone maintains normal bone formation in adult male rats during rapid weight 
- [21852324] 2011 — Mitogen-activated protein kinase phosphatase 1 regulates bone mass, osteoblast gene expression, and 
- [19262974] 2009 — Effects of PTH treatment on tibial bone of ovariectomized rats assessed by in vivo micro-CT.

## Orthogonal queries — closing the vocabulary gap

The slice required BOTH a growth-plate term AND a length term, so studies framed as "mandibular growth"
or "juvenile mouse femur" were invisible. Three orthogonal queries returned **509** records outside the
275. Screened for the same decisive combination: **4 hits**, two already known, **two new**:

- **[36576115] wang2023** — head-to-head abaloparatide vs teriparatide, 70 adolescent wild-type rats.
  Both raise condylar length; COL X down, SOX9/COL II up. **ABL judged more potent.**
- **[27653318] bartlow2017** — 189 healthy juvenile mice, PTH(1-34) 40 µg/kg 5×/wk × 8 wk.
  **No enduring body length difference.** Half the ogawa2002 dose, whole-animal endpoint.

## The finding that reframes the gap

**Four studies had a length measurement in a growing animal under a PTH1R agonist and none reported the
treatment comparison:**

| study | what it had | what it reported |
|---|---|---|
| `liao2026` | tibia length in every genotype table | drug tables: trabecular/cortical only |
| `altman2015` | young rat proximal tibia linear growth, 0.31 mm/d under intermittent PTH | as *method validation* |
| `bartlow2017` | total femur length (used to normalise VOIs) | body length nose-to-tail only |
| `ogawa2002` | LGR by double tetracycline label | **reported it** |

PTH1R agonists are studied by the bone-densitometry community — BV/TV, BMD, trabecular number,
strength. Length belongs to the growth community, which has never had reason to dose them.

**The gap is a discipline artifact, not a negative result.** And it means the decisive experiment is
cheap: a re-analysis of existing micro-CT, not a new animal study.
