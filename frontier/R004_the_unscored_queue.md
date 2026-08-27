# F-R004 — the 667 unscored zeros, opened and ranked

F-R003 established that R436's blind-spot triage scored **199 of 866** concepts and used three filters
this file's own corrections forbid, and that the unscored remainder is concentrated in the **mechanism**
domains: mechanics 32/32, cell biology 70/72, vascular-neural-immune-microbiome 86/91, pharmacology
99/105, comparative 46/52.

This is that remainder, opened. Every row below is **tier ZERO** in
`atlas/data/round436/zero_triage.json` — never mentioned in a node, a gap, a reference or `CLAUDE.md` —
**and never scored**. Quotations are verbatim from the atlas's own enumeration notes. Full rows and
PMIDs live in `atlas/concepts/enumerations/{03,09,10,12}_*.md`.

Ranked by the file's own criteria: does it name a **length endpoint**, does it act on a term the stack
does not already occupy (Step 0 / CORR-297), and is it obtainable.

---

## ⭐⭐⭐ TIER A — the one that reframes the problem

### A1 · The secondary ossification centre may be the *price* of fusion, not a bystander

Three ZERO rows, from three independent domain agents, that nobody put side by side:

> **"Teleost fish — permanently cartilaginous epiphyses.** Teleosts keep **entirely cartilaginous
> epiphyses for life, providing a virtually unlimited chondro-progenitor pool. The SOC — an adaptation
> to land — is formed AT THE EXPENSE of those chondroprogenitors."**

> **"Indeterminate growth as the ancestral vertebrate condition.** Comparative analysis argues
> indeterminate growth is **ancestral** and permanent arrest **derived**; arrest evolved by
> mechanistically **DISTINCT routes in closely related taxa**, and different organs in one animal."

> **"Squamate reptiles (164 species µCT survey).** Complete growth-plate-cartilage **resorption** is
> the predominant finding across Gekkota, Scincoidea, Lacertoidea."
> — plus **"Senescence-vs-land-colonisation hypothesis."**

**Why this is the top item.** This file's central model is a division budget with an oestrogen rate
multiplier, and its deepest unexplained fact is `nilsson2005`: rabbit resting-zone chondrocytes from
old and young donors undergo **the same number of population doublings in culture** — *"the
proliferative limit is not carried by the cell. It is imposed by the plate."* `THE_CLOCK.md` §1 has
called that imposed limit *"a target in a way an intrinsic one is not"* since Phase 1, and has never
named what imposes it.

**The teleost row names a candidate: the SOC.** A vertebrate that never builds a secondary ossification
centre keeps a cartilaginous epiphysis and grows for life. A vertebrate that builds one converts that
epiphysis into bone and sandwiches its growth plate between two osseous plates — and the row asserts
the SOC is built **out of the progenitors that would otherwise have sustained growth.** That converts
fusion from *a clock running out* into **a structural trade-off with an anatomical location**, and it
predicts `nilsson2005` exactly: freed from the plate, the cell has capacity left, because the capacity
was never the cell's limit.

**It also collides with the file's own best local result.** `trompet2024` — the cleanest local-depot
demonstration in the atlas — put a SAG bead **into the rat femoral SOC** and got femur +2.75/+2.64/
**+3.63%** at 1/2/6 months, effect growing, with resting-zone PTHrP⁺ cells 65.5 → 139.8/mm² and
proliferation and terminal cell height **unchanged** — pure **N**. **The one place an intervention has
worked is the structure this hypothesis says is doing the damage, and nobody has asked why.**

**The cheapest step needs no animal.** The atlas already holds `secondary_ossification_center` (L0) and
`xie2020`'s comparative microCT **across bats, jerboa, whales and the fossil record**. The question —
*does SOC size or timing predict the residual progenitor pool and the age at arrest, across species?* —
is a re-read of data that exists. The decisive step after it is a **timing** experiment: delay SOC
formation in a normal growing mouse and measure final bone length. ⚠ Against it: the mouse never fuses,
so the model that is easiest to run is the one least able to answer it — the file's oldest species
problem, at a new place.

---

## ⭐⭐ TIER B — length endpoints in normal animals, already run, never scored

Each of these is what `WHAT_THIS_ATLAS_NEEDS.md` asks for 51 times — *put a caliper on a mouse* — and
each already has one.

| # | ZERO concept | the atlas's own note | why it matters here |
|---|---|---|---|
| **B1** | ⭐ **Chronic exercise raises solute delivery and limb length** | *"All runners had significantly **longer limbs** regardless of housing temperature"* · agent: **exercise (free)** | A positive **length** endpoint in a normal animal, attributed to **transport**, not to mechanotransduction. R448 computed that impact loading at 1–20 Hz **cannot** ventilate the plate and that the ventilating timescale is **diurnal/postural**; R456 ran the physical-modality sweep to a null. **This row is the surviving positive and it is filed under solute delivery, which is the axis R450/R452 opened and R448 made rate-limiting.** |
| **B2** | **Limb temperature raises solute delivery** | *"Warm vs cool hindlimb immersion, core held constant"* · agent: **local heating (device)** | **Local limb warming is one of only THREE items on R436's own list of positive length endpoints in a normal animal that are available to a person today.** This is its mechanism, and it was never connected to it. |
| **B3** | ⭐ **Endothelial proteolytic activity + non-resorbing osteoclasts** | *"Directly mediates bone **ELONGATION** — named in the title"* · agent: MMP inhibitors (**wrong direction**) | Elongation = production minus clearance. This file models production exhaustively and has never priced the **clearance** front as a controllable rate. |
| **B4** | **Sciatic denervation and longitudinal bone growth** | rat: metatarsals **3–5% shorter** on the denervated side from week 1 | A **neural** input to elongation with a length endpoint. `skeletal innervation` returns **0 files** here; `NGF` returns **0 word-boundary hits in any node**; TrkA and tanezumab are enumeration-only. |
| **B5** | **Circumferential periosteal sleeve resection lengthens a limb** | *"Consistent gain for discrepancies ~3.5 cm; femur responds ~1 y, tibia >2 y"* | The atlas closed periosteal release with *"real but age-cutoff ~9.6 y."* This row is a **different operation** with a **different magnitude** and it was never read against that closure. |
| **B6** | **Arteriovenous malformation → limb overgrowth (Klippel-Trénaunay)** + ⭐ **pO₂ of the epiphyseal plate distal to an arteriovenous fistula** | *"The one experiment that manipulates limb perfusion and measures plate pO₂"* · agent: **alpelisib (PIK3CA)** | A **human** perfusion→overgrowth phenotype paired with the **only** experiment that manipulates limb perfusion and reads plate oxygen. R450 opened the perfusion term and R475 found a plate tolerates five hours of complete ischaemia; **the gain direction was never worked.** |

---

## ⭐ TIER C — mechanism the atlas has no node for

| # | ZERO concept | atlas note | comment |
|---|---|---|---|
| **C1** | **Ferroptosis of growth-plate chondrocytes** | *"iron/lipid-peroxidation death mode distinct from apoptosis"* · regulators **GPX4, PIEZO1, SLC7A11** | **Worked in F-R003.** Lands on R459's named open question. |
| **C2** | **Chondrocyte pentose-phosphate pathway → oxidative protein folding** | — | **Worked in F-R003.** Same paper as C1 (`PMID 39794539`, Nat Metab 2025). |
| **C3** | **Histone lactylation under intermittent hypoxia** | *"Metabolite→chromatin route by which a systemic condition (**sleep apnoea**) shortens long bones"* · regulators lactate, **LDHA, p300** | The growth plate is the most hypoxic and most glycolytic tissue in the body and therefore the highest-lactate one. **`THE_CLOCK.md`'s ageing hypothesis is epigenetic and is entirely about DNA methylation**; lactylation is a second, metabolite-driven epigenetic axis with a systemic entry point and a **length** direction. Nothing here touches it. |
| **C4** | **Physeal bar as "local fusion" — and it is nerve-driven** | *"The one form of plate closure with a newly identified causal upstream signal"* · regulators **PTN; gangliosides** | The duration lever is the biggest in the file and it has exactly **one** mechanism (oestrogen). This is a second, **local**, causally-signposted route to closure — read backwards, a fusion-delaying target that is not a steroid. Pairs with B4. |
| **C5** | **Mitochondrial transfer between cells via Cx43** | *"MSCs can donate mitochondria to chondrocytes through connexin-43 channels — an **entirely unexploited route**"* · GJA1 | Direct delivery of oxidative capacity into a hypoxic, NADPH-limited cell. If F-R003's redox model is right, this is its cell-therapy form. |
| **C6** | **A permissive mid-plate transport region + pressure-driven flow from both chondro-osseous junctions** | *"FRAP + intravital; flow arises from a **pressure difference** between bone vasculature and cartilage"* | Advective, not diffusive, and **pressure-driven** — which makes it modulable by anything that changes intraosseous pressure. Pairs with B1/B2/B6. |
| **C7** | **Molecular-weight ceiling on solute entry** | *"332 Da–10 kDa enter from all three routes; **≥40 kDa did NOT enter**"* | The hard number under R315's delivery wall. Any biologic proposal in this file should be read against it first. |

---

## TIER D — human, randomised or population-scale, and unscored

| # | concept | note |
|---|---|---|
| D1 | ⭐ **Microbiota-directed complementary food (MDCF-2)** | *"Improves **LINEAR growth** in 12–18-month-old Bangladeshi children with moderate acute malnutrition, followed for 2 years"* — a food product, human, randomised. ⛔ CORR-203: a deficit population. |
| D2 | ⭐ **Gut microbiota → IGF-1 → bone growth** | *"Colonisation induces IGF-1 and promotes bone formation and growth; antibiotics lower IGF-1; **SCFA supplementation restores it**"* |
| D3 | **Canakinumab → improved growth in autoinflammatory disease** | *"Height SDS **significantly increased** in FMF/MKD/TRAPS/DADA2 cohorts"* · **approved agent**. ⛔ CORR-203 again — an inflammatory brake being removed. |
| D4 | ⭐ **HIV on ART — appendicular vs axial trajectories separated** | VITALITY trial (Zimbabwe/Zambia): **leg length and sitting height reported separately.** The atlas's residual is trunk-dominant and it has almost no dataset that splits the two compartments. |
| D5 | **Adenotonsillectomy for paediatric OSA** / **CPAP raises pulsatile GH and IGF-1** | Pairs with C3 (intermittent hypoxia → lactylation). A systemic, treatable condition with a plausible **two-route** mechanism onto length. |

---

## What I am NOT claiming

These are **enumeration rows**, written by R436's external agents, most carrying a PMID and none
verified by me beyond the four I worked in F-R003. Several will die on the first read — that is what
a queue is for. The claim is narrower and it is about the file, not the biology:

> **R436 built the best coverage instrument in this project, scored 23% of what it found, filtered that
> 23% with three criteria its own corrections forbid, and recorded the result as "the blind spot does
> not hide an obvious missed compound."** It contains at least six length endpoints in normal animals,
> a named candidate for the death route R459 could not name, a second epigenetic axis, a second route
> to fusion, and a comparative argument that the thing imposing the limit is a structure this atlas
> already has a node for.

**Suggested disposition.** Re-run `zero_triage` with (a) symbols extracted from the enumeration
`REGULATORS:` field rather than from free text, (b) no cartilage-enrichment threshold — CORR-349/363,
(c) presence in **any** compartment that can act on the plate, not ≥20 CPM in the plate — CORR-342,
and (d) **both** directions — CORR-344. Score all 866. The four filters above are each already written
into this file's own correction ledger; none of them is new.
