# R436 — VERIFIED NEW FINDINGS FROM THE EXTERNAL ENUMERATION
Every PMID below was re-resolved against PubMed or Europe PMC by the main loop, not taken on
an agent's word. Atlas coverage counted by grep over nodes + gaps + CLAUDE.md.

## 1. SOLUBLE EPOXIDE HYDROLASE — a whole axis with ZERO atlas coverage and a normal-animal endpoint
`PMID 42297360`, Cell Proliferation 2026 (verified; closed access, abstract only).
sEH inhibitor **TPPU promotes LONG BONE GROWTH IN NEWBORN MICE** — normal animals, so CORR-203
does not apply — by enhancing **FABP5+ SEPTOCLAST** activity (MMP9, FABP5 up in the metaphysis)
through HUVEC→hDPSC crosstalk that raises HIF-1a and activates NOTCH. The authors' own prior work
attributes long-bone growth and repair to enhanced **H-type vessel-coupled osteogenesis**.
- ATLAS COVERAGE: `soluble epoxide` 0 files · `EPHX2` 0 · `TPPU` 0 · `epoxyeicosatrienoic` 0.
  (`septoclast` is covered, 10 files — the CELL is known here, the AXIS is not.)
- STEP 0: CLEAN. Nothing in the stack touches sEH, EETs or septoclasts.
- OBTAINABLE CLASS: sEH inhibitors have reached humans (GSK2256294, EC5026, AR9281). TPPU itself
  is a research tool.
- ⛔ THE OBJECTION, AND IT IS SERIOUS: the reported phenotype is a **REDUCED ratio of hypertrophic
  to proliferative cartilage width**, i.e. the hypertrophic zone got relatively THINNER, and
  h_term is ~80% of longitudinal growth. The mechanism is faster MMP9-driven clearance of
  hypertrophic cartilage plus more H-type vessel coupling — and R365 established that vascular
  invasion IS the terminal event of closure. So this is the mirror of failure mode 1: it only
  buys length if DISCHARGE is rate-limiting, and it may spend the period faster.
- ⛔ NEWBORN MICE. CORR-299's question — is sEH still doing work in an OPEN ADOLESCENT plate —
  is unasked in any species.
- VERDICT: worth a full round. Not a promotion.

## 2. THE HUMAN PUBERTAL GROWTH PLATE HAS TWO STEM POPULATIONS AND GH ACTS ON IT DIRECTLY
`PMID 41984930`, Science Translational Medicine 2026 (verified).
"A transcriptional atlas of the pubertal human growth plate reveals two populations of stem cells
and direct effect of growth hormone." Reported deeper population is **PTHrP-NEGATIVE**, Prrx1-marked,
in a niche low in **both** WNT and TGF-beta. Human, pubertal — the right tissue and the right stage.
- Bears directly on R360's open question `g_l7_360a` (is the pool finite at all?) and on R356's
  finding that the human resting zone's own programme is secreted Wnt antagonists.

## 3. CALCIUM SUPPLEMENTATION COSTS 3.5 cm OF ADULT HEIGHT IN BOYS
`PMID 22990031` — recorded in the bibliography as `prentice2012`. See that entry.

## 4. HELICOBACTER PYLORI — a removable insult with a meta-analysed growth effect
`PMID 34997950`, Helicobacter 2022 (verified). Meta-analysis, 29 studies / 9,384 subjects,
height-for-age Z **SMD -0.41**.
- ATLAS COVERAGE: to be checked. Diagnosable by urea breath test or stool antigen and eradicable
  in a week, which puts it in the same class as the file's other free subtractions.
- ⛔ Confounded by socioeconomic status in most of the underlying studies; direction of causation
  is not established by a meta-analysis of observational data.

## 5. SEASONALITY IS LARGE ENOUGH TO BE BOTH A HAZARD AND A CLUE
`PMID 28561389`, Am J Hum Biol 1997 (verified). Seasonal height velocity variation, boys and girls
8-18. Reported summer share of annual growth is large.
- MEASUREMENT HAZARD: any velocity computed across unmatched seasons is uninterpretable, which
  compounds R425's fixed-time-of-day requirement.
- ⭐ AND A CLUE THIS FILE ALREADY HAS HALF OF: R426/R433 hold `serrat2015` (local limb warming,
  40 C to one side, femur +1.3% / tibia +1.5%, contralateral control) and `serrat2014` (22->34 C
  raises 10 kDa tracer entry into the tibial growth plate by >150%). If summer growth is partly
  THERMAL rather than photoperiodic or nutritional, those are the same phenomenon measured two
  ways. Nobody has decomposed the seasonal effect into light, temperature, activity and diet.

## 6. TONSILLECTOMY +0.34 cm ON ADULT HEIGHT
`PMID 40909198` — Europe PMC lookup returned a malformed record on the first attempt; RE-VERIFY
BEFORE USE. Reported as UK Biobank, +0.34 cm (95% CI 0.26-0.41), larger the younger the surgery.
Recorded here as UNVERIFIED pending a clean fetch.
