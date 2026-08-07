# Round 35 — the optimal stack, safety set aside, and what is actually missing

## Two things I had wrong, both found this round

**1. The pool arm is not empty — the atlas already held the answer.** `qu2025`,
`progenitor_reservoir_outside_the_plate`, grade C, human evidence direct:

> Fetal/neonatal reserve-zone progenitors do **not** self-renew; at ~3 postnatal weeks they begin to,
> and long columns appear. The long-lived progenitors descend from **Gli1+ cells dormant through fetal
> life**. When cartilage is damaged (mosaic p21 arrest), the **Gli1+ population expands inside the
> cartilage, biased to the resting zone, enriches the cycling fraction, and restores normal growth** —
> and the reparative cells come from **Pdgfra+ cells outside the cartilage entirely.**

**The system is not closed.** There is a reservoir, it sits in the surrounding stroma, and **damage
recruits it.** I have been saying "nothing enlarges the pool" for several rounds while the atlas held
this at direct human evidence.

**2. The FGFR3-selective compound I said was missing exists.** `TYRA-300` increased nasoanal, tibial and
femoral length **in wild-type mice** — not only in FGFR3-mutant models. That is the demonstration that
FGFR3 inhibition grows a *normal* growth plate. It raised both proliferation and differentiation, and
**increased lumbar vertebral length and improved intervertebral disc shape.**

## The optimal stack, safety set aside

| arm | term | agent | status |
|---|---|---|---|
| **1** | **h_term** | CNP analogue at max exposure — navepegritide weekly > daily vosoritide | approved |
| **2** | **amplification** | **FGFR3-*selective*** inhibitor (TYRA-300 class), not pan-FGFR | preclinical; erdafitinib is the potent pan- fallback |
| **3** | **pool** | recruitment of the Gli1+/Pdgfra+ external reservoir | **no pharmacological recruiter exists** |
| **4** | **duration** | aromatase inhibition to hold the pubertal clock | approved; *required* if arm 3 is run as cycling |

### Growth hormone is deliberately excluded, and this is the least obvious call

GH is additive on **velocity** — 8.69 vs 5.95 cm/yr added to navepegritide. But:

- GH raises IGF-1, and `oichi2023` shows IGF-1 restores resting-zone phospho-Akt and **drives pooled
  progenitors out of the pool, decreasing their number**
- `chu2025` independently shows GH **depleting the slow-cycling pool** while raising elongation rate
- That is exactly the mechanism that makes the KIGS dose–response saturate: 43 % more GH bought
  first-year velocity and **nothing** at near-adult height

**GH spends the budget to buy rate. It belongs in a velocity-optimal stack, not a final-height-optimal
one, and it is actively antagonistic to arm 3.** If final height isn't the objective, put it back.

### Why FGFR3-selective rather than erdafitinib

Erdafitinib is genuinely the more potent molecule (FGFR3 3.0 nM vs infigratinib 10.0) and produced
19.06 cm/yr in a child. But it **inhibits FGFR1 harder than FGFR3**, FGFR1 blockade raises phosphate via
FGF23, and this atlas holds that **normal phosphate is required for caspase-9 apoptosis of terminal
hypertrophic chondrocytes** — the exact cell arm 1 is trying to enlarge. A selective FGFR3 inhibitor
removes that conflict. If a pan-FGFR agent is used anyway, **a phosphate binder is a rational and
untested adjunct.**

## The toxicity mechanism is now observed, not inferred

`erdaseries2025`: erdafitinib produced growth acceleration **independent of sex steroids and of IGF1
levels**, accompanied by **a distinct widening of the growth plate**. Combined with `williams2001`
(stress = 3.2 − 2.8 × thickness, R² 0.55) and `erdachild2024` (kyphoscoliosis, cord compression), three
independent observations close the loop: **drug → plate widens → plate weakens → deformity.**

It also complicates the IGF-I/AKT story from `erdachild2024` — here acceleration was explicitly
IGF1-independent. Circulating IGF1 ≠ local signalling, so the two aren't strictly in conflict, but the
atlas should not carry the IGF-I account as settled.

## What is missing — ranked

1. **A pharmacological recruiter of the Gli1+/Pdgfra+ reservoir.** `qu2025` triggers it with genetic p21
   arrest, which is not a therapy. This is now the highest-value missing compound in the atlas, because
   it is the only arm that *adds to* the budget rather than spending it better. Note the clinical
   correlate nobody has exploited: fractures near growth plates cause overgrowth in children.
2. **A cartilage-restricted CNP** to break the hypotension ceiling on arm 1 (`hirai2026` is the proof of
   concept). Test the *headroom* first — if plate CNP signalling is already saturated at tolerated doses,
   targeting buys nothing.
3. **The FGFR dose–response middle.** Infigratinib 0.25 mg/kg → +1.74 cm/yr; erdafitinib oncology dose →
   +19. An 11-fold range in one class with the entire middle unexplored — oncology doses down,
   achondroplasia doses timidly up, nothing titrated for growth in a normal plate.
4. **Whether any of these drugs reach cartilage.** The growth plate is avascular. Small molecules
   (FGFR inhibitors) should penetrate better than peptides (CNP) — nobody has measured growth-plate
   concentrations of either.

## Documents still wanted

- **PMID 42370681** — infigratinib Phase 3, for **bone age**. Still the single highest-value item.
- **PMID 41449965** — *Postmarketing Cases of Erdafitinib-Associated Skeletal Growth Toxicity Events in
  Pediatric patients.* A regulatory case series = the closest thing to a dose–response across children.
  Paywalled.

Validator: 643 nodes, 1247 edges, 320 gaps, 1146 refs — 0 errors, 0 warnings.
