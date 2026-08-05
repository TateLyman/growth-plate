# L2 — Stem and progenitor biology

**35 nodes (0 stubs) · 190 edges touching the layer · 28 gaps · 42 distinct refs · 62 quantitative rows**
Confidence: A 0 · B 3 · C 20 · D 10 · E 1 · **X 1**.
`human_evidence` direct 5 / indirect 9 / **absent 21**. `translation_risk` **high on 24 of 35**.

**Zero nodes in this layer have replicated human evidence** (`human_evidence: direct` plus
≥2 independent human primaries). That is not a sampling failure. The defining technique —
inducible Cre-lox clonal lineage tracing — cannot be performed in humans, and everything
that follows is downstream of that fact.

---

## 1. The settled core

**Postnatal chondrocyte columns are monoclonal, in mice.** Confetti labelling gives
monochromatic columns; a single P6 PTHrP-creER pulse generates short (<10-cell) columns
peaking at P18, then long columns, with labelled column number plateauing at ~6 months and
columns still present at 12 months (`mizuhashi2018`, node `monoclonal_column_formation`).
Grade C.

**Resting-zone cells cycle at one fifth the rate of proliferative cells.** 6.1% (SD 2.3) vs
30.5% (SD 3.2) EdU⁺ at P9, ratio 0.20, n = 3 (`mizuhashi2018`, `resting_zone_niche`). An
independent H2B-EGFP dilution measurement gives 2.03-fold signal loss per division
(n = 4 mice, p < 0.0001) and confirms the resting zone as the slow compartment
(`hallett2021`).

**Only ~2–3% of resting-zone cells are long-term self-renewing, and two unrelated assays
agree.** Serial passaging: 16.3% of P12-pulsed colonies formed secondary colonies and
12.5% of those (2/16) passaged ≥9 generations, giving the authors' 2–3% estimate. Label
retention: the durably label-retaining fraction plateaus at **2.6% (SE 0.9)** after
doxycycline chase, decaying with half-life 0.99–1.18 weeks from a starting 86.5% (SE 1.3)
(`hallett2021`). Two methods, two laboratories, same order of magnitude — the strongest
quantitative result in L2.

**Multipotency is acquired late and is not tri-potent.** PTHrP-lineage descendants become
Col1a1(2.3kb)-GFP⁺ osteoblasts and Cxcl12-GFP⁺ stroma, but **0 of 443 scored cells** became
adipocytes under rosiglitazone plus high-fat diet (`mizuhashi2018`). Grem1⁺ cells likewise:
**0 of 19 clones** adipogenic (`worthley2015`). Whatever these cells are, they are not
classical MSCs.

**Hypertrophic chondrocytes become osteoblasts and, in young mice, are the dominant
source.** Col10a1-lineage: **63%** of trabecular and **62%** of endosteal osteocalcin⁺
osteoblasts at 1 month; **60%/68%** of Col1a1(2.3kb)-GFP⁺ osteoblasts at 3 weeks
(`zhou2014a`, `yang2014`). Dual Cre/Dre fate mapping puts the end of that dominance at
adolescence, after which LepR⁺ stroma takes over (`shu2021`). Grade C, and it overturns the
older view that hypertrophic chondrocytes simply die.

---

## 2. The live disagreements

**Five schemes claim the apex skeletal stem cell and they are mutually incompatible on four
axes at once** (C-L2-01, gap `g_l2stem_004`):

| Scheme | Definition | The incompatibility |
|---|---|---|
| mSSC (`chan2015`) | CD45⁻Ter119⁻Tie2⁻CD51⁺CD90⁻6C3⁻CD105⁻CD200⁺; 8 subpopulations resolved | **Identical panel** to `debnath2018`'s periosteal PSC — so the panel does not specify anatomical compartment |
| hSSC (`chan2018`) | PDPN⁺CD146⁻CD73⁺CD164⁺ | **No shared antigen with the mouse panel**; discovery specimen is *one* 17-week fetal femur, scored on 76 mouse orthologues |
| PTHrP⁺ / FoxA2⁺ resting chondrocytes | reporter lineage | FoxA2⁺ and PTHrP⁺ overlap at **0.017%** at P18, against a 0.014% double-negative background — i.e. background (`muruganandan2022`) |
| Grem1⁺ OCR (`worthley2015`) | reporter lineage | 40% CD105⁺, non-adipogenic; conflicts with LepR⁺ |
| LepR⁺ stroma (`zhou2014`) | reporter lineage | 0.3% of marrow, 94% of all marrow CFU-F — a different compartment entirely, dominant only post-adolescence |

**And the human cell is in the wrong zone.** C-L2-03: the hSSC was localised to the second
half of the prehypertrophic and first half of the hypertrophic zone of that single fetal
femur — *not* the resting zone where every mouse result points. `chu2026` compounds it: the
most stem-like population of the human pubertal resting zone is **PTHLH-negative**, sits in
a WNT/TGF-β-low microenvironment, and maps to Prrx1⁺ mouse cells (C-L2-05). If both hold,
the murine resting-zone paradigm may not describe human tissue at all. `chu2026` full text
was inaccessible; the claim rests on its abstract and is queued P1. Note also that
`avijgan2025`, cited by five nodes for human resting-zone sub-populations, is **T6 —
an unrefereed preprint**. The human end of this layer is one fetal specimen, one
abstract-only 2026 paper and one preprint.

**Is capacity spent or acquired?** C-L2-04. `nilsson2004`/`schrier2006` hold that resting-zone
progenitors have a finite budget monotonically spent, producing senescence. `newton2019`
holds that chondroprogenitors are *depleted* fetally and then *acquire* self-renewal
postnatally. The two literatures have never been run in one system (rabbit/rat population
kinetics vs mouse clone counting). Worse, the finite-capacity model's own originators
falsified its Hayflick reading: rabbit resting-zone population doublings in vitro are
**independent of donor age** (`nilsson2005`). What does change with senescence is **global
DNA methylation, which decreases**, with no change across the resting-to-hypertrophic
transition — a result pointing at an epigenetic clock rather than a division counter.

**The mechanism audit removed the phrase this layer was built on.** `growth_plate_senescence`
was SCOPED in Phase 2d: `marino2008`'s catch-up was **incomplete** (p < 0.001 residual
deficit in body mass, tail and tibia length), and gonadal suppression by leuprolide was
partial (uterine mass ≈0.16 g vs ≈0.1 g ovariectomised, ≈0.5 g intact), leaving oestrogen —
the single most important alternative driver — present and unequal between arms. The node
now reads "**partial** conservation of growth potential". `catch_up_growth` was also SCOPED:
`marino2008` observed catch-up in heart, liver and kidney too, and the anti-central-sensor
argument rests on `baron1994`, which could not be read (P1 in the access queue).

**Telomere attrition is grade X.** The most commonly invoked molecular clock for the
finite-capacity model. No primary measurement of telomere length or telomerase activity in
*human* growth plate chondrocytes as a function of age could be traced; the search returns
osteoarthritic articular cartilage, skeletal-ageing reviews and rodent work. Nearest datum
is murine and indirect (`carlone2021`: mTert-GFP marks a transitional progenitor peaking
during adolescent growth rather than persisting). Logged `x001`, search `g_l2stem_007`.

---

## 3. The load-bearing assumption

**That the mouse PTHrP⁺ resting chondrocyte is the functional equivalent of whatever cell
performs the same job in the human growth plate.**

Every downstream use of this layer runs through it: L7's inheritance of "resting-zone
depletion causes fusion", L12's occasional framing of growth drugs as acting on a progenitor
pool, and the entire interpretive value of the 2–3% self-renewing fraction as a human number.

Its evidence is: shared marker overlap in mouse (49.2% of PTHrP-mCherry⁺ cells carry the
mSSC CD105⁻CD200⁺ phenotype, SD 8.4; 27.4% carry the BCSP phenotype, SD 16.5 —
`mizuhashi2018`), and nothing human. Against it: the hSSC is in the wrong zone (C-L2-03),
the human root cell is reported PTHLH-negative (C-L2-05), and the mouse and human marker
panels share **no antigen** (C-L2-02). Gap `g_l12l7_002` states the question directly and it
is unanswered.

The atlas's own defensive move is worth naming: **"SOC formation triggers resting-zone
stemness" has no causal evidence.** Both anchor papers report only temporal coincidence
(3.3% secondary-colony formation from a P9 pre-SOC pulse vs 16.3% from a P12 pulse during
SOC development). A Europe PMC search for any SOC ablation, blockade or delay experiment
with a resting-zone stemness readout returned **0 studies** (`g_l2stem_003`, logged). It is
held as `hypothesized_link` edges with `confidence: speculative` and a linked gap, which the
validator enforces, so L7 cannot silently inherit it as mechanism.

---

## 4. What would change everything

A clonal phylogeny of the human growth plate built from somatic mutations. This needs no
genetic labelling and is therefore not blocked by the method that blocks everything else
here. Whole-genome sequencing of laser-microdissected human columns and resting-zone cells
would return, in one experiment: whether human columns are monoclonal; how many divisions
separate a resting cell from a terminal hypertrophic cell; whether a small long-lived
population exists and at what frequency; and — by cross-referencing PTHLH expression in the
same tissue — whether the human root cell is PTHrP⁺ or PTHrP⁻.

Any of four outcomes rewrites the layer. Polyclonal human columns would invalidate the
clonal-column framework transferred from mouse. A long-lived fraction far above 2–3% would
mean the in vitro figure is a culture artefact (`g_l2stem_010`). A PTHLH-negative root would
confirm `chu2026` and orphan the field's flagship marker. Division counts incompatible with a
finite budget would close C-L2-04 against the senescence model that L7 depends on.

---

## 5. Numbers

| Parameter | Value | Unit | Species | Spread / n | Source | Flag |
|---|---|---|---|---|---|---|
| RZ vs PZ EdU incorporation | 6.1 vs 30.5 (ratio 0.20) | % EdU⁺ | mouse, P9 distal femur | SD 2.3 / 3.2, n = 3 | `mizuhashi2018` | single source |
| Label-retaining fraction, plateau | **2.6** | % of Col2a1 lineage | mouse | SE 0.9; from 86.5% (SE 1.3) | `hallett2021` | single source |
| Label-retention decay half-life | 0.99–1.18 | weeks | mouse | fitted range | `hallett2021` | single source |
| H2B-EGFP loss per division | 2.03 | fold | mouse, P35 | n = 4, p < 0.0001 | `hallett2021` | single source |
| Long-term self-renewing fraction | **2–3** | % of CFU | mouse | derived by authors; 2/16 clones passaged ≥9 | `mizuhashi2018` | derived |
| Secondary colony formation, P9 vs P12 pulse | 3.3 (17/518) vs 16.3 (16/98) | % of clones | mouse | none of the P9 clones survived further passage | `mizuhashi2018` | single source |
| PTHrP⁺ vs FoxA2⁺ colonies at passage 5 / 9 | 1.4 (2/143) vs 8.9 (10/112) | % of colonies | mouse, P18 | n = 3 experiments | `muruganandan2022` | single source |
| FoxA2⁺/PTHrP⁺ double positives | 0.017 | % of sorted cells | mouse, P18 | SD 0.004; background 0.014 | `muruganandan2022` | single source |
| Adipocyte output in vivo | **0 / 443** | LipidTOX⁺ cells | mouse | rosiglitazone + high-fat diet | `mizuhashi2018` | single source |
| Grem1⁺ clones making adipocytes | **0 / 19** | clones | mouse | polyclonal cultures also negative | `worthley2015` | single source |
| Chondrocyte-derived osteoblasts | 62–63 (Ocn⁺) / 60–68 (Col1a1-GFP⁺) | % | mouse, 1 month / 3 weeks | n = 3–4 mice | `zhou2014a` | single source |
| **Human** equivalent of the above | **not measured** | % | human | — | — | gap `g_l2stem_002` |
| PTHrP⁺ cells with mSSC phenotype | 49.2 | % | mouse, P9 | SD 8.4 | `mizuhashi2018` | single source |
| LepR⁺ share of marrow CFU-F | 94 | % | mouse | 0.3% of marrow cells | `zhou2014` | single source |
| hSSC discovery specimen | **1** | 17-week fetal femur | human | 76 orthologue gene score | `chan2018` | **n = 1** |
| Rabbit RZ doublings vs donor age | no dependence | — | rabbit | effect size not given | `nilsson2005` | single source |
| DNA methylation with senescence | decrease | global 5mC | rabbit | no change across RZ→HZ | `nilsson2005` | single source |
| Causal SOC-ablation stemness experiments | **0** | studies | any | full search screened | — | null, `g_l2stem_003` |
| Human telomere/telomerase in physis | **0** | studies | human | — | — | **grade X** (`x001`) |

---

## 6. Top gaps and their discriminating experiments

1. **`g_l2stem_001`** (method_blocked, tract 3) — which human resting-zone cell self-renews,
   and does it express PTHLH? Route around the block: clonal somatic-mutation phylogenies
   from microdissected human physeal tissue, which require no genetic labelling. Monoclonal
   columns with long shared branches → a durable root cell exists; star phylogenies → columns
   are seeded repeatedly from a large pool.
2. **`g_l2stem_003`** (search_established, tract 4) — does SOC formation *cause* stemness?
   Discriminator: delay SOC formation (VEGF blockade or epiphyseal *Hif1a* manipulation) at
   P8–P10 and score secondary-colony formation from PTHrP-creER cells at P12. Causal model
   predicts the P12 rate stays at the P9 value (3.3%); autonomous-clock model predicts it
   rises to 16.3% regardless.
3. **`g_l2stem_004`** (contradiction, tract 2) — are the five schemes distinct cells? The
   experiment nobody has run: all five panels and all five Cre drivers applied to *one* cohort
   at matched ages with *one* functional assay. Only `mizuhashi2018` has done any cross-scheme
   quantification at all.
4. **`g_l2stem_009`** (search_established) — does the hSSC panel label human resting-zone
   cells? Discriminator: PDPN/CD146/CD73/CD164 immunostaining with zone annotation on
   postnatal human physeal blocks. Resting-zone labelling reconciles mouse and human; renewed
   prehypertrophic-only labelling makes C-L2-03 a real biological species difference.
5. **`g_l2stem_011`** (species_gap, tract 2) — does the postnatal clonal switch occur in a
   species that actually **fuses**? Every demonstration is in one that does not. This is the
   hinge between L2 and L7 and it is currently unbolted.
6. **`g_l2stem_010`** (quantitative_gap, tract 4) — is 2–3% an in vivo number or a culture
   artefact? Discriminator: in vivo dilution kinetics at multiple chase lengths against
   serial-transplant frequency in the same animals.

---

## 7. Human-translation status

**21 of 35 nodes have `human_evidence: absent`; 24 of 35 carry high translation risk; 0 have
replicated human evidence.** In practical terms: of the 62 quantitative rows in this layer,
essentially every functional measurement — cycle fraction, label retention, self-renewal
frequency, adipogenic output, osteoblast contribution, colony kinetics — is mouse or rabbit.

The human contribution is three items and each is fragile. `chan2018`: **one** 17-week fetal
femur, scored by transferring 76 mouse orthologues, localising the stem cell to the wrong
zone relative to all mouse work. `chu2026`: abstract only, inaccessible full text, claiming
the human root cell is PTHLH-negative. `avijgan2025`: **T6, unrefereed preprint**, cited by
five nodes. `ambrosi2025` adds ten human anatomical sites but profiles composition rather
than testing self-renewal in the physis.

The correct reading of any L2 answer: **it is a statement about mice**, and the one place
where human data exist, they disagree with the mouse on both the zone and the marker. This
is the layer to distrust, and the atlas holds it at A 0 / B 3 precisely so that L7 and L12
cannot borrow from it at a grade it has not earned.
