import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad")
from nodes_lib import *
n=[]

n.append(dict(
 id="chondrocyte_cluster", name="Chondrocyte cluster (non-columnar clone)",
 aliases=["orthogonal clone","non-columnar clone","lateral clone"],
 type="tissue_structure",
 summary=(
  "A cluster is a clone of chondrocytes whose long axis lies at less than 60 degrees to the proximal-distal "
  "bone axis, that is, a clone that failed to convert its divisions into a longitudinal stack. Clusters are not "
  "an artefact or a pathological finding: in the E18.5 mouse growth plate they are the majority clone type, "
  "with only 17.6% (distal femur) and 19.4% (proximal tibia) of doublets stacked at 60-90 degrees, and they are "
  "elongated ellipsoids oriented orthogonal to the growth direction. Postnatally clusters persist but retreat to "
  "the outer edges of the plate while the interior becomes columnar. Their proposed function is bone widening "
  "rather than lengthening, and the evidence is correlative but quantitative: the expansion-to-elongation ratio "
  "measured by micro-CT falls from 0.16-0.18 embryonically, when clusters dominate, to 0-0.04 by P40, when "
  "columns dominate. Mechanistically a clone becomes a cluster when the cumulative fraction of incomplete "
  "division-plane rotations exceeds about 60%. This entity is a recent and mouse-only construct; whether human "
  "growth plates contain a comparable peripheral cluster compartment is unexamined."),
 quantitative=[
  Q("angular threshold separating clusters from columns","less than 60","degrees between clone long axis and proximal-distal bone axis","mouse, 3D principal component analysis of Confetti clones","mouse","rubin2024","author-defined threshold"),
  Q("proportion of embryonic clones that are clusters","majority (>80% of doublets not stacked)","% of doublets","E18.5 mouse distal femur and proximal tibia","mouse","rubin2024","n = 1044 and 805 doublets"),
  Q("number of clusters analysed at P40","1129 (distal femur), 1154 (proximal tibia)","clusters","mouse, 3D imaging","mouse","rubin2024","sample sizes as reported"),
  Q("complete rotations within postnatal clusters","15.5 (distal femur), 17.3 (proximal tibia)","% of divisions","P40 mouse; versus 36-40% within columns","mouse","rubin2024","n = 1129 and 1154 clusters"),
  Q("near-perfect rotations within postnatal clusters","1.9 (distal femur), 3.0 (proximal tibia)","% of divisions","P40 mouse","mouse","rubin2024","as reported"),
  Q("rotation-failure fraction above which a clone becomes a cluster","60","% of divisions","mouse","rubin2024_threshold_placeholder","rubin2024","author-stated tolerance threshold"),
 ],
 localization=["mouse embryonic growth plate: clusters dominate throughout (rubin2024)",
               "mouse postnatal growth plate: clusters restricted to outer edges (rubin2024)",
               "human: not examined"],
 human_evidence="absent",
 human_evidence_note="Clusters have been defined and quantified only in mouse by 3D multicolour clonal imaging; no human study has looked for them.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="Defined entirely by mouse Confetti lineage tracing and 3D morphometry, a method with no human counterpart, and reported in a single study.",
 confidence="D",
 key_refs=[
  R("rubin2024",39269144,"Rubin S",2024,"primary","Defined clusters as clones oriented below 60 degrees to the growth axis, showed they dominate the embryonic plate and retreat to the periphery postnatally, and correlated their abundance with bone expansion."),
  R("mizuhashi2019",30888720,"Mizuhashi K",2019,"primary","Independently identified a peripheral, perpendicularly oriented chondrocyte population with mesenchymal precursor behaviour."),
 ],
 open_questions=["g_l1arch_004","g_l1arch_013"],
))

n.append(dict(
 id="hypertrophic_phase_duration", name="Hypertrophic phase duration (transit time constraint)",
 aliases=["hypertrophic transit time","hypertrophic zone turnover time"],
 type="process",
 summary=(
  "The time a chondrocyte spends between leaving the cell cycle and being removed at the chondro-osseous "
  "junction is remarkably invariant, and this invariance is a strong constraint on how growth rate can be "
  "regulated. Hunziker and Schenk found the duration of hypertrophic activity to be approximately two days in "
  "rat proximal tibia and unchanged across 21-, 35- and 80-day-old animals whose growth rates differ several "
  "fold. In mouse the constraint is tighter: the whole hypertrophic column turns over in about 24 h, split into "
  "roughly 12 h during which cell height more than triples and roughly 12 h at terminal size before removal. "
  "The implication is that plates growing at different rates cannot simply take longer to enlarge their cells; "
  "they must enlarge them faster or reach a different final size within a fixed window, which is exactly what "
  "the three-phase model shows - fast plates run the IGF-dependent third phase, slow plates truncate it. This "
  "also means the hypertrophic zone height is the product of a fixed transit time and a variable cell height, "
  "which is why zone height alone is a poor predictor of growth rate. The constraint has never been tested in "
  "human tissue, where the proliferative cycle appears to be an order of magnitude slower."),
 quantitative=[
  Q("duration of the hypertrophic activity phase","2","days","rat proximal tibia; constant across 21-, 35- and 80-day-old animals","rat","hunziker1989","approximate; explicitly reported as constant across growth rates"),
  Q("turnover time of the whole hypertrophic column","24","h","mouse, BrdU pulse-chase","mouse","cooper2013","approximate"),
  Q("time to more than triple cell height after leaving the proliferative pool","12","h","mouse proximal tibia","mouse","cooper2013","approximate"),
  Q("dwell time at terminal size before removal","12","h","mouse proximal tibia","mouse","cooper2013","approximate"),
  Q("chondrocyte removal interval per column","3","h per cell","rat proximal tibia, steady state","rat","hunziker1987","equivalently 8 cells/day"),
 ],
 localization=["rat proximal tibia: phase duration measured (hunziker1989)",
               "mouse proximal tibia: transit time measured by pulse-chase (cooper2013)",
               "human: not measured"],
 human_evidence="absent",
 human_evidence_note="No human study measures the transit time of a chondrocyte through the hypertrophic zone.",
 species_basis=["rat","mouse"],
 translation_risk="high",
 translation_risk_reason="A fixed ~24 h to 2 day transit time is a rodent finding in tissues that elongate roughly ten times faster than human plates; whether the same constraint operates in a slow human plate is unknown and would change how growth rate must be regulated.",
 confidence="C",
 key_refs=[
  R("hunziker1989",2607442,"Hunziker EB",1989,"primary","The duration of the hypertrophic phase is approximately 2 days and constant across widely different rat growth rates."),
  R("cooper2013",23485973,"Cooper KL",2013,"primary","The mouse hypertrophic column turns over in about 24 h, with roughly 12 h enlarging and 12 h at terminal size."),
  R("hunziker1987",3543020,"Hunziker EB",1987,"primary","One chondrocyte is removed per column every 3 h in the rat proximal tibia."),
  R("farnum1989",2760737,"Farnum CE",1989,"primary","Serial-section analysis of the real-time duration of terminal events at the chondro-osseous junction."),
 ],
 open_questions=["g_l1arch_008","g_l1arch_001"],
))

for x in n: print(write(x))
