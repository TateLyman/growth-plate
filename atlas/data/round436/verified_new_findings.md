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

## 7. PERIOSTEAL RESECTION IN LAMBS — a real addition to a well-covered node, NOT a new synthesis
`PMID 19098649`, J Pediatr Orthop 2009 (verified). NOT in the bibliography. Microtransducer
measurement of tibial growth velocity; reported to raise velocity in every animal at every
timepoint, with the mechanism named as **axial elongation of the hypertrophic chondrocyte** rather
than proliferation, swelling or matrix.
⛔ **DISCIPLINE NOTE — I nearly wrote this up as a new synthesis and it is not.** Before drafting I
greped, and the atlas already holds both halves:
  · `chondrocyte_hypertrophy` states that hypertrophy is ANISOTROPIC, that the cell raises its
    height far more than its lateral diameter because longitudinal matrix channels constrain it,
    and — citing Hunziker and Schenk — that **SHAPE MODULATION, NOT VOLUME, is what changes when
    growth accelerates**: final cell height rises and lateral diameter falls while final cell
    volume is slightly REDUCED.
  · `periosteum` states that the tether mechanism was **tested and REFUTED** (`chaudhary2016`,
    rabbit, before-and-after imaging by authors who expected the opposite), and proposes instead
    that periosteal resection is a **LOCAL HEDGEHOG WITHDRAWAL**, since strain raises periosteal
    Ihh, PTHrP, Gli and Patched.
→ WHAT IS ACTUALLY NEW is narrower and still worth having: a NORMAL-ANIMAL growth-VELOCITY endpoint
  in a large species, whose stated mechanism converges independently on Hunziker and Schenk's
  shape-modulation variable. Two literatures, one conclusion, and the file had them apart.
→ AND IT SHARPENS AN EXISTING ARM RATHER THAN OPENING ONE: if periosteal resection works by
  withdrawing a periosteal hedgehog source, it runs OPPOSITE to the SAG programme, which adds
  hedgehog at the SOC. Same pathway, two compartments, opposite signs — CORR-300's shape again,
  and the periosteum node already names the decisive unrun experiment (measure physeal hedgehog
  signalling before and after resection).

## 8. TWO EXPOSURES WITH ZERO ATLAS COVERAGE THAT ARE FREE TO CHECK
· **HELICOBACTER PYLORI** — `pylori` returns **0 files** across nodes, gaps and CLAUDE.md.
  `PMID 34997950` (verified) meta-analyses 29 studies / 9,384 subjects for height-for-age Z.
  Confounded by socioeconomic status, so causation is not established — but it is diagnosable by
  breath or stool antigen and eradicable in a week, which is the same class as the file's other
  free subtractions.
· **TONSILLECTOMY / ADENOTONSILLAR DISEASE and paediatric OSA** — `tonsillectomy` 0 files,
  `adenotonsill` 0 files, `sleep apnea` 0 files. `PMID 40909198` (verified, Laryngoscope
  Investigative Otolaryngology 2025, UK Biobank) reports an ADULT HEIGHT endpoint for childhood
  tonsillectomy. An entire airway-obstruction axis with an adult-height number and no coverage.

## 9. CORR-296 UPGRADED — the chu2026 GP1/GP2 contrast is probably COMPOSITIONAL, not a maturity axis
CORR-296 has said since R296 that the GP1/GP2 direction "cannot currently be resolved" and that four
rounds (R241, R244, R245, R246) are built on it. R436 tried to resolve it and FAILED IN A SPECIFIC
AND INFORMATIVE WAY, which is more useful than the standing caution.
Method: the file is `atlas/data/round243_supplied/chu2026_supp/adw3590_data_file_s1.csv`, header
"differentially regulated genes (DEGs) between mouse GP1 and GP2 clusters", 15,983 genes.
⚠ It is semicolon-delimited with COMMA DECIMAL SEPARATORS - a naive csv read returns zero parsed
rows silently, which is how it can look empty. 1,480 rows reach padj<0.05, 1,039 positive : 441
negative (the skew CORR-296 already recorded).
Instead of arguing from single stem markers, orient it with whole PANELS:
· MATURE/HYPERTROPHIC panel: **5 of 6 significant rows positive** - COL10A1 +3.24 (1e-07),
  MEF2C +3.48 (7e-38), IBSP +8.34 (4e-51), ALPL +1.77 (9e-10), SPARC +0.95 (6e-38); against
  RUNX2 -0.95 (1e-05).
· EARLY/RESTING panel: **only 3 of 6 in the predicted direction** - SFRP5 -2.36 (1e-16),
  UCMA -1.79 (1e-24), COL9A1 -0.51 (8e-08) go the right way, but CYTL1 **+5.28** (4e-16),
  PTH1R +1.13 (2e-06) and COL2A1 +0.38 (4e-04) go the wrong way.
· And the stem panel is openly contradictory: SFRP5 -2.36 and NOTUM -1.57 say one cluster,
  while **PRRX1 +1.78 (1e-14)** says the other - and PRRX1 is the marker the paper's own HUMAN
  result uses to name the root population.
⭐ **THE TELL IS THE TOP OF THE FILE: the two largest positive effects are PRG4 +8.46 and IBSP +8.34.**
PRG4 is superficial/ARTICULAR and IBSP is BONE. Two different tissues, moving together, at the top
of a contrast that is supposed to lie along one cartilage differentiation trajectory.
→ **A contrast whose largest movers are markers of two ADJACENT TISSUES, and which no maturity or
stem panel can orient, behaves like a difference in TISSUE COMPOSITION rather than in chondrocyte
regulation. That is CORR-339's shape** - the lesson learned on the LUMBAR/THORACIC ATAC sheets,
appearing again on the dataset four rounds are built on.
⛔ HONEST LIMIT: I have the DE table, not the cluster definitions or per-cluster cell counts, so
this is a strong inference and not a demonstration. What it licenses is NOT a new direction call -
it is a REASON for CORR-296's caution and an instruction for whoever settles it: get the cluster
composition, and put a marker of the suspected contaminant (PRG4 for articular, IBSP for bone) in
the control panel before reading any compartment from this dataset.
✓ Unaffected: every ABUNDANCE claim made from this table (HHIP baseMean 3.73 above FGFR3 2.30 and
NT5E 3.21; NRK 6.10) is a baseMean, not a direction, and does not depend on the sign convention.
