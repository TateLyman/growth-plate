import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad")
from nodes_lib import *
n=[]

n.append(dict(
 id="growth_plate", name="Growth plate (physis)",
 aliases=["physis","epiphyseal plate","epiphyseal cartilage plate"],
 type="tissue_structure",
 summary=(
  "The growth plate is a disc of hyaline cartilage between epiphysis and metaphysis that is avascular, aneural "
  "and alymphatic and contains only chondrocytes and the matrix they make. Its functional unit is a vertical "
  "column of chondrocytes; the life history of one cell is laid out in space along that column, from slowly "
  "dividing resting-zone cells through rapidly cycling flattened proliferative cells to terminally enlarged "
  "hypertrophic cells that are removed at the vascular invasion front. Cartilage neoformation at the epiphyseal "
  "face is balanced against destruction at the metaphyseal face, so a plate in steady state maintains constant "
  "height while translating the epiphysis away from the diaphysis. In rat proximal tibia the balance is exact "
  "enough that the calculated cell production rate matches the loss rate at the chondro-osseous junction. Height "
  "and internal proportions are not fixed: in human rib the proliferative and hypertrophic zone heights and the "
  "primary spongiosa all fall with age, most steeply in the first postnatal year, while matrix volume fraction "
  "and septal thickness rise. Radiographic morphometry in mouse and human agrees that total plate width, and in "
  "mouse also total height and resting-zone height, correlate with tibial growth rate, whereas hypertrophic zone "
  "height on its own does not."),
 quantitative=[
  Q("growth plate variable most strongly correlated with tibial length and growth rate","total growth plate width","qualitative rank","mouse proximal tibia histomorphometry and human tibia radiographs","multiple","wilson2021","linear model; hypertrophic zone height and plate area did not correlate in mouse"),
  Q("chondrocytes lost per column at the vascular front","8","cells/day","rat proximal tibia in steady-state growth (one cell every 3 h)","rat","hunziker1987","not reported"),
  Q("age at which growth plate zone heights change most steeply","0-1","years postnatal","human rib growth plate, proliferative and hypertrophic zones and primary spongiosa","human","byers2000","direction of change reported; absolute heights not available from abstract"),
 ],
 localization=["human: all long bones, vertebral bodies, ribs (byers2000, dimeglio2020)",
               "mouse/rat: standard model tissue"],
 human_evidence="direct",
 human_evidence_note="Human growth plate architecture and its age-dependence have been measured histomorphometrically in rib (byers2000) and in a distal tibia undergoing physiological epiphysiodesis (white2008), and radiographically for plate height and width (wilson2021).",
 species_basis=["human","rat","mouse","porcine","rabbit"],
 translation_risk="moderate",
 translation_risk_reason="The zonal plan is conserved across mammals, but the kinetics are not: human proliferative cycle times, plate heights and cell counts per column differ substantially from rodent, and mice do not undergo epiphyseal fusion.",
 confidence="B",
 key_refs=[
  R("hunziker1987",3543020,"Hunziker EB",1987,"primary","Quantified chondrocyte performance and cellular turnover in rat proximal tibial growth plate by stereology plus fluorochrome labelling."),
  R("byers2000",11033444,"Byers S",2000,"primary","Human rib growth plate zone heights and primary spongiosa fall with age, most steeply in the first year, while matrix volume fraction and septal thickness rise."),
  R("wilson2021",31997656,"Wilson K",2021,"primary","Total growth plate width correlates most strongly with tibial length and growth rate in both mouse and human; hypertrophic zone height does not correlate in mouse."),
  R("ostria2026",41520458,"Ostria CB",2026,"review","Current synthesis of growth plate zonal architecture, plasticity and endocrine control."),
 ],
 open_questions=["g_l1arch_001","g_l1arch_014"],
))

n.append(dict(
 id="resting_zone", name="Resting (reserve) zone",
 aliases=["reserve zone","germinal zone","RZ"],
 type="tissue_structure",
 summary=(
  "The resting zone is the epiphyseal-most stratum of the growth plate, containing small, rounded, sparsely "
  "distributed chondrocytes in abundant matrix and singly or in pairs rather than in columns. It is the source "
  "of the columnar clones: PTHrP-expressing resting-zone chondrocytes in mouse behave as skeletal stem cells "
  "that acquire self-renewal and generate columnar clones only after the secondary ossification centre has "
  "formed, which places the appearance of a true stem compartment after, not before, the establishment of the "
  "plate. The zone is not uniformly quiescent: a systematic review of the primary literature finds reported "
  "labelling indices and the operational definition of quiescence vary widely between studies, so 'resting' is a "
  "morphological label rather than an established kinetic state. Resting-zone height is one of the "
  "histomorphometric parameters that correlates linearly with tibial length and growth rate in mouse. The zone "
  "is also the most hypoxic and nutritionally remote part of the plate, since it is furthest from the "
  "metaphyseal vasculature and depends on epiphyseal supply."),
 quantitative=[
  Q("resting zone height correlation with tibial growth rate","high linear correlation","qualitative","mouse proximal tibia, neonate to young adult, histomorphometry","mouse","wilson2021","linear model reported; coefficient not extractable from abstract"),
 ],
 localization=["mouse RZ: PTHrP+ skeletal stem cells confirmed by lineage tracing (mizuhashi2018)",
               "human RZ: architecture described histologically, kinetics unmeasured (kember1976, thurston1985)"],
 human_evidence="indirect",
 human_evidence_note="Human resting zone morphology is described in histological series but no human study establishes its stem-cell function or labelling index reliably.",
 species_basis=["mouse","rat","human"],
 translation_risk="high",
 translation_risk_reason="The stem-cell identity of resting-zone chondrocytes rests entirely on mouse lineage tracing, which cannot be done in humans; and the secondary-ossification-centre dependence of that identity means timing relative to human skeletal development is unestablished.",
 confidence="C",
 key_refs=[
  R("mizuhashi2018",30401834,"Mizuhashi K",2018,"primary","PTHrP+ resting zone chondrocytes are skeletal stem cells that form columnar clones only after secondary ossification centre formation in mouse."),
  R("avijgan2026",41795828,"Avijgan M",2026,"systematic_review","Systematic review finds the resting zone is not uniformly quiescent and that reported labelling indices and definitions of quiescence vary widely."),
  R("wilson2021",31997656,"Wilson K",2021,"primary","Resting zone height is among the growth plate parameters that correlate linearly with tibial length and growth rate in mouse."),
 ],
 open_questions=["g_l1arch_002","g_l1arch_012"],
))

n.append(dict(
 id="proliferative_zone", name="Proliferative zone",
 aliases=["PZ","columnar zone","zone of flattened cells"],
 type="tissue_structure",
 summary=(
  "The proliferative zone contains flattened, discoid chondrocytes stacked into longitudinal columns, each "
  "column a clone descended from a resting-zone progenitor. It is where the cell cycle is run and where column "
  "architecture is generated by post-mitotic rotation of daughter pairs. Column length in this zone is a species "
  "constant of sorts: Kember and Sissons counted 24 cells per proliferative column in the human distal femur, "
  "against a rodent plate that is structurally different and cycles roughly ten times faster. Rat proliferative "
  "cycle time varies from 30.9 h to 76.3 h between plates in the same animal, with the variation almost entirely "
  "in G1. In human rib the proliferative zone height falls with age, most steeply in the first year, while "
  "cartilage septal thickness rises and septal number falls, meaning the zone becomes shorter and coarser as "
  "growth decelerates. The proliferative zone contributes only a small direct share of elongation - about 9% by "
  "cell division in the fast rat proximal tibia - but it sets the number of cells that will later hypertrophy, "
  "which is where most of the elongation is generated."),
 quantitative=[
  Q("cells per proliferative column","24","cells","human distal femur, cell counts on histological sections","human","kember1976","not reported; single-study value"),
  Q("total cell cycle time","30.9-76.3","h","four growth plates, 28-day-old rat, in vivo BrdU","rat","wilsman1996a","range across plates; differences significant at p<0.05 except proximal tibia vs distal radius"),
  Q("direct contribution of cell division to elongation","9","% of elongation","proximal tibia, 28-day-old rat","rat","wilsman1996","not reported"),
  Q("direction of proliferative zone height change with age","decreasing","qualitative","human rib, birth to adolescence, greatest change in first year","human","byers2000","absolute heights not available from abstract"),
  Q("direction of cartilage septae number change with age, proliferative zone","decreasing","qualitative","human rib, birth to adolescence","human","byers2000","not reported"),
 ],
 localization=["human PZ: cell counts and zone heights measured (kember1976, byers2000)",
               "rat PZ: full cell-cycle decomposition (wilsman1996a)"],
 human_evidence="direct",
 human_evidence_note="Human proliferative zone cell counts per column, zone height and septal architecture have been measured directly in femur and rib specimens (kember1976, byers2000).",
 species_basis=["human","rat","porcine"],
 translation_risk="moderate",
 translation_risk_reason="Human column cell counts and zone heights are measured, but the kinetics behind them are only derived; the rodent cell-cycle decomposition cannot be assumed to apply.",
 confidence="B",
 key_refs=[
  R("kember1976",1018028,"Kember NF",1976,"primary","24 cells per proliferative column in human distal femur, with a derived cycle time of ~20 days."),
  R("wilsman1996a",8764865,"Wilsman NJ",1996,"primary","Rat PZ cycle time 30.9-76.3 h across four plates, with the variation concentrated in G1."),
  R("byers2000",11033444,"Byers S",2000,"primary","Human rib proliferative zone height falls with age while septal thickness rises and septal number falls."),
  R("wilsman1996",8982136,"Wilsman NJ",1996,"primary","Cell division contributes 9% of elongation in the fast rat proximal tibia."),
 ],
 open_questions=["g_l1arch_002","g_l1arch_012"],
))

n.append(dict(
 id="prehypertrophic_zone", name="Prehypertrophic zone",
 aliases=["PHZ","zone of maturation","transitional zone"],
 type="tissue_structure",
 summary=(
  "The prehypertrophic zone is the narrow stratum where chondrocytes have left the cell cycle but have not yet "
  "begun the large volume increase of terminal hypertrophy. It is defined by position and by marker expression "
  "(Indian hedgehog and PTH1R in rodents) rather than by an unambiguous morphological boundary, which is why "
  "stereological studies define strata by unbiased position rather than by eye. In quantitative terms this zone "
  "is where phase 1 of chondrocyte enlargement occurs: a roughly three-fold volume increase from about 600 fl to "
  "2000 fl at constant dry mass density in mouse, that is, true hypertrophy with proportionate macromolecular "
  "synthesis, before the swelling phase begins. Because the transition out of this zone is the committed step "
  "toward the volume increase that generates most elongation, its timing is the point at which local signals "
  "(IGF, Ihh/PTHrP, CNP, FGFR3) are integrated into growth rate. Reserve of caution: essentially all "
  "prehypertrophic zone marker work is murine, and the zone is not separately quantified in any human "
  "histomorphometric series."),
 quantitative=[
  Q("volume increase during phase 1 of enlargement","600 to 2000","fl","mouse proximal tibia; ~3-fold at constant dry mass density 0.183 pg/fl","mouse","cooper2013","approximate values as stated"),
 ],
 localization=["mouse PHZ: defined by Ihh/PTH1R expression and by unbiased stratum position",
               "human PHZ: not separately quantified in published histomorphometry"],
 human_evidence="absent",
 human_evidence_note="No human histomorphometric series reports the prehypertrophic zone as a separate compartment; human studies report proliferative and hypertrophic zones only (byers2000).",
 species_basis=["mouse","rat"],
 translation_risk="high",
 translation_risk_reason="The zone is defined by rodent marker expression and by stereological convention; there is no validated human definition, so any human claim about it is an inference.",
 confidence="C",
 key_refs=[
  R("cooper2013",23485973,"Cooper KL",2013,"primary","Phase 1 of chondrocyte enlargement is a ~3-fold volume increase at constant dry mass density, preceding the swelling phase."),
  R("breur1994",7943757,"Breur GJ",1994,"primary","Stereological analysis in unbiasedly defined narrow strata localises where chondrocyte volume and shape change begin in rat proximal tibia."),
  R("ostria2026",41520458,"Ostria CB",2026,"review","Places the prehypertrophic compartment within current zonal and endocrine models of the growth plate."),
 ],
 open_questions=["g_l1arch_008"],
))

n.append(dict(
 id="hypertrophic_zone", name="Hypertrophic zone",
 aliases=["HZ","zone of hypertrophy","zone of cell enlargement"],
 type="tissue_structure",
 summary=(
  "The hypertrophic zone is where most longitudinal elongation is generated, by chondrocytes increasing their "
  "volume roughly ten-fold and their axial height roughly four-fold within laterally confining matrix channels. "
  "In rat proximal tibia the enlargement is accompanied by two- to five-fold increases in rough endoplasmic "
  "reticulum surface area, Golgi membrane and mitochondrial volume, so these are metabolically active cells "
  "rather than dying ones, a point confirmed by time-lapse imaging of living terminal hypertrophic chondrocytes "
  "in situ. The zone turns over fast and on a fixed schedule: the hypertrophic phase lasts approximately two "
  "days in rat regardless of whether the animal is growing quickly or slowly, and in mouse the entire "
  "hypertrophic column is replaced in about 24 h, with roughly 12 h spent enlarging and 12 h at terminal size. "
  "Counterintuitively, hypertrophic zone height by itself is a poor predictor of growth rate: in mouse "
  "histomorphometry it does not correlate with tibial growth rate, whereas total plate width, total height and "
  "resting-zone height do. Height of the zone is a product of cell height and cell number, and those two can "
  "trade off."),
 quantitative=[
  Q("duration of the hypertrophic phase","2","days","rat proximal tibia; constant across 21-, 35- and 80-day-old animals with widely different growth rates","rat","hunziker1989","approximate, as stated"),
  Q("increase in rough endoplasmic reticulum surface area, Golgi membranes and mitochondrial volume","2-5","fold","proliferative to late hypertrophic chondrocyte, rat proximal tibia","rat","hunziker1987","range across organelle compartments"),
  Q("time for the whole hypertrophic column to turn over","24","h","mouse; ~12 h enlarging plus ~12 h at terminal size","mouse","cooper2013","approximate"),
  Q("correlation of hypertrophic zone height with tibial growth rate","no significant linear correlation","qualitative","mouse proximal tibia, neonate to young adult","mouse","wilson2021","explicitly contrasted with total height, resting zone height and plate width, which did correlate"),
  Q("direction of hypertrophic zone height change with age","decreasing","qualitative","human rib, birth to adolescence","human","byers2000","absolute values not available from abstract"),
  Q("cartilage septae number in hypertrophic zone across age","no significant change","qualitative","human rib, birth to adolescence, in contrast to the proliferative zone","human","byers2000","not reported"),
 ],
 localization=["rat HZ: stereology and ultrastructural morphometry (hunziker1987)",
               "human HZ: zone height and septal architecture measured in rib (byers2000)"],
 human_evidence="direct",
 human_evidence_note="Human hypertrophic zone height and cartilage septal architecture have been measured across age in rib specimens (byers2000) and hypertrophic cell heights reported in an in vitro human labelling study (thurston1985).",
 species_basis=["rat","mouse","human","porcine"],
 translation_risk="moderate",
 translation_risk_reason="Zone-level architecture is measured in humans, but the cell-level volume kinetics that make the zone the engine of elongation are rodent-only.",
 confidence="B",
 key_refs=[
  R("hunziker1987",3543020,"Hunziker EB",1987,"primary","Late hypertrophic rat chondrocytes show 4-fold height, 10-fold volume and 2-5 fold organelle increases."),
  R("hunziker1989",2607442,"Hunziker EB",1989,"primary","The duration of the hypertrophic phase is fixed at approximately 2 days across widely different rat growth rates."),
  R("farnum1990",2201757,"Farnum CE",1990,"primary","Time-lapse DIC imaging shows terminal hypertrophic chondrocytes are living, viable cells up to the chondro-osseous junction."),
  R("wilson2021",31997656,"Wilson K",2021,"primary","Hypertrophic zone height alone does not correlate with tibial growth rate in mouse, unlike total height and plate width."),
  R("byers2000",11033444,"Byers S",2000,"primary","Human rib hypertrophic zone height decreases with age while septal number is unchanged."),
 ],
 open_questions=["g_l1arch_008","g_l1arch_009"],
))

n.append(dict(
 id="zone_provisional_calcification", name="Zone of provisional calcification",
 aliases=["ZPC","calcified cartilage zone","zone of preparatory calcification"],
 type="tissue_structure",
 summary=(
  "The zone of provisional calcification is the thin stratum at the metaphyseal face of the plate in which the "
  "longitudinal cartilage septa mineralise while the transverse septa remain unmineralised, producing the "
  "scaffold on which the primary spongiosa is built. Time-of-flight secondary ion mass spectrometry of human "
  "polydactyly growth plates shows the transition is compositionally abrupt rather than graded: across the "
  "calcified cartilage interface there is a sharp decline in organic matrix ion fragments and a concurrent rise "
  "in mineral fragments, with a highly significant peak in the calcium to organic-nitrogen ratio. Correlations "
  "between organic and phosphate markers across the interface are consistent with progressive, ordered "
  "mineralisation rather than a single nucleation event. Radiographically this zone is the dense white line at "
  "the metaphyseal border of the physis and is the landmark used clinically to assess physeal integrity and, "
  "when it is disrupted, to diagnose rickets and scurvy. The mineral chemistry and matrix vesicle biology of "
  "this zone belong to the matrix and mineralisation layer; here it is treated as the architectural boundary "
  "that determines where vascular invasion can occur."),
 quantitative=[
  Q("statistical significance of the calcium-to-organic ratio peak at the calcified cartilage interface","p < 0.0001","p-value","human polydactyly growth plate specimens, ToF-SIMS large-area imaging, Dunn's multiple comparisons","human","zoehrer2025","n = 3 specimens"),
  Q("number of human specimens analysed by ToF-SIMS","3","specimens","human polydactyly digits","human","zoehrer2025","n = 3"),
 ],
 localization=["human ZPC: compositional transition mapped by ToF-SIMS (zoehrer2025)",
               "rat/rabbit ZPC: oxygen tension and structure described (brighton1971)"],
 human_evidence="direct",
 human_evidence_note="The organic-to-mineral transition across the human zone of provisional calcification has been mapped directly by ToF-SIMS in three polydactyly specimens (zoehrer2025).",
 species_basis=["human","rat","rabbit"],
 translation_risk="low",
 translation_risk_reason="The key compositional evidence in this node is from human tissue; the mineralisation mechanism itself is cross-species conserved.",
 confidence="B",
 key_refs=[
  R("zoehrer2025",41253283,"Zoehrer R",2025,"primary","ToF-SIMS mapping of three human polydactyly growth plates shows a sharp organic-to-mineral transition at the calcified cartilage interface, with a highly significant Ca/organic ratio peak."),
  R("byers2000",11033444,"Byers S",2000,"primary","Human rib: cartilage septal thickness increases and the transition to bone trabeculae is quantified across age."),
  R("brighton1971",5580029,"Brighton CT",1971,"primary","Measured oxygen tension by zone across the epiphyseal plate, metaphysis and diaphysis in rat and rabbit."),
 ],
 open_questions=["g_l1arch_007"],
))

n.append(dict(
 id="borderline_zone", name="Borderline zone (peripheral borderline chondrocytes)",
 aliases=["borderline chondrocytes","peripheral transition zone"],
 type="tissue_structure",
 summary=(
  "At the outer margin of the growth plate, immediately adjacent to the perichondrium and the groove of "
  "Ranvier, sits a population of chondrocytes that are aligned perpendicular to the columnar chondrocytes rather "
  "than parallel to the growth axis. Inducible lineage tracing in mouse shows these borderline chondrocytes are "
  "not simply mis-oriented columnar cells: they behave as transient mesenchymal precursors, leaving the "
  "cartilage and contributing to marrow stromal cells and osteoblasts in the metaphysis. This is a route from "
  "cartilage to bone lineage that is distinct from the transdifferentiation of terminal hypertrophic "
  "chondrocytes at the chondro-osseous junction. Independently, 3D clonal analysis in mouse finds that "
  "postnatal growth plates retain small, disorganised, orthogonally oriented clusters specifically at the outer "
  "edges while the interior is columnar, which is architecturally consistent with a distinct peripheral "
  "compartment that supports lateral rather than longitudinal growth. Nothing equivalent has been shown in "
  "human tissue; the borderline compartment is defined entirely by mouse genetics."),
 quantitative=[
  Q("orientation of borderline chondrocytes relative to columnar chondrocytes","perpendicular","qualitative","mouse growth plate periphery adjacent to perichondrium","mouse","mizuhashi2019","descriptive"),
  Q("location of residual disorganised clusters in the postnatal growth plate","outer edges","qualitative","P40 mouse distal femur and proximal tibia, 3D Confetti clonal analysis","mouse","rubin2024","n = 1129 (distal femur) and 1154 (proximal tibia) clusters"),
 ],
 localization=["mouse BZ: lineage traced (mizuhashi2019)","human BZ: not described"],
 human_evidence="absent",
 human_evidence_note="No study identifies a borderline chondrocyte population in human growth plate tissue; the compartment is defined by mouse inducible lineage tracing.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="Defined solely by mouse Cre-based lineage tracing, a method with no human equivalent, and not yet corroborated by any human histological or single-cell description.",
 confidence="D",
 key_refs=[
  R("mizuhashi2019",30888720,"Mizuhashi K",2019,"primary","Peripheral borderline chondrocytes, oriented perpendicular to columns, act as transient mesenchymal precursors giving rise to marrow stromal cells and osteoblasts in mouse."),
  R("rubin2024",39269144,"Rubin S",2024,"primary","Postnatal mouse growth plates retain small disorganised clusters specifically at the outer edges while the interior is columnar."),
 ],
 open_questions=["g_l1arch_013"],
))

n.append(dict(
 id="chondro_osseous_junction", name="Chondro-osseous junction",
 aliases=["COJ","chondro-osseous border","vascular invasion front","metaphyseal front"],
 type="tissue_structure",
 summary=(
  "The chondro-osseous junction is the interface at which the terminal hypertrophic chondrocyte is removed, the "
  "transverse septum is breached and a metaphyseal capillary bud enters the emptied lacuna. Serial-section "
  "analysis in swine and rat established the time sequence: metaphyseal endothelial cells penetrate the "
  "non-calcified pericellular and territorial matrix rather than the mineralised longitudinal septa, so the "
  "invasion is targeted rather than indiscriminate. Terminal hypertrophic chondrocytes are alive up to this "
  "point; time-lapse differential interference contrast imaging of living explants shows them viable at the "
  "junction, and they pass through a defined condensation stage immediately before removal. The rate of removal "
  "is the mirror image of the production rate at the top of the plate: in the rat proximal tibia in steady "
  "state, one chondrocyte per column is eliminated every 3 h, that is 8 cells per column per day, and across the "
  "whole plate the calculated production and loss rates match. The junction is therefore the point at which "
  "elongation rate is read out, and the point at which anything that blocks resorption or angiogenesis will "
  "cause the plate to thicken."),
 quantitative=[
  Q("chondrocyte elimination rate at the vascular front","1 per 3","cells per hour per column","rat proximal tibia, steady-state growth","rat","hunziker1987","equivalently 8 cells per column per day"),
  Q("agreement between calculated cell production and cell loss","approximately equal","qualitative","four growth plates, 28-day-old rat; internal consistency check on the kinetic model","rat","wilsman1996","stated as approximate equality"),
  Q("matrix compartment penetrated by invading endothelial cells","non-calcified pericellular and territorial matrix","qualitative","distal hypertrophic zone, swine and rat, serial light-microscopic sections","porcine","farnum1989","descriptive"),
 ],
 localization=["swine and rat COJ: serial-section timing (farnum1989, farnum1989a)",
               "mouse COJ: septoclast and capillary bud biology (sivaraj2022)",
               "human COJ: mineral transition mapped (zoehrer2025); cellular kinetics unmeasured"],
 human_evidence="indirect",
 human_evidence_note="The human chondro-osseous junction has been characterised compositionally (zoehrer2025) and immunohistochemically for vessels and RANK+ cells (walzer2014), but no human study measures cell turnover rate at the junction.",
 species_basis=["rat","porcine","mouse","human"],
 translation_risk="moderate",
 translation_risk_reason="The architecture of the junction is conserved and partly documented in human tissue, but every turnover rate and every resorptive cell identity comes from rodents.",
 confidence="C",
 key_refs=[
  R("farnum1989",2760737,"Farnum CE",1989,"primary","Serial-section analysis establishes the time sequence of terminal chondrocyte death and endothelial penetration of non-calcified matrix at the chondro-osseous junction."),
  R("farnum1989a",2589219,"Farnum CE",1989,"primary","Terminal hypertrophic chondrocytes undergo a distinct condensation stage at the chondro-osseous junction in Yucatan swine."),
  R("hunziker1987",3543020,"Hunziker EB",1987,"primary","Vascular invasion eliminates one chondrocyte per column every 3 h in rat proximal tibia."),
  R("sivaraj2022",35091558,"Sivaraj KK",2022,"primary","FABP5+ mesenchyme-derived septoclasts, not osteoclasts, mediate matrix degradation and chondrocyte phagocytosis at the chondro-osseous border in mouse."),
 ],
 open_questions=["g_l1arch_003"],
))

n.append(dict(
 id="primary_spongiosa", name="Primary spongiosa",
 aliases=["primary trabecular bone","primary spongy bone"],
 type="tissue_structure",
 summary=(
  "The primary spongiosa is the layer of newly formed trabeculae immediately below the chondro-osseous "
  "junction, each trabecula consisting of a mineralised longitudinal cartilage septum coated with woven bone. "
  "It is the direct structural product of the growth plate, so its dimensions track plate activity: in human "
  "rib the primary spongiosa height falls with age in parallel with the proliferative and hypertrophic zones, "
  "most steeply in the first postnatal year, while bone trabecular thickness increases and trabecular number "
  "decreases. Byers and colleagues make the point that the proliferative zone, hypertrophic zone and primary "
  "spongiosa should be treated as a single active growth region whose internal rearrangement, not just its "
  "height, changes with age; by contrast the secondary spongiosa in the same specimens showed stable bone "
  "mineral volume with trabecular consolidation. Because the primary spongiosa carries the cartilage core "
  "forward, its resorption rate determines how much of the plate's product survives into the metaphysis, which "
  "is where growth plate architecture couples to peak bone mass."),
 quantitative=[
  Q("direction of primary spongiosa height change with age","decreasing","qualitative","human rib, birth to adolescence, greatest change in first postnatal year","human","byers2000","absolute values not available from abstract"),
  Q("direction of bone trabecular thickness change with age, primary spongiosa","increasing","qualitative","human rib, birth to adolescence","human","byers2000","not reported"),
  Q("direction of bone trabecular number change with age, primary spongiosa","decreasing","qualitative","human rib, birth to adolescence","human","byers2000","not reported"),
  Q("bone mineral volume in secondary spongiosa across age","stable","qualitative","human rib, birth to adolescence, contrasted with primary spongiosa","human","byers2000","not reported"),
 ],
 localization=["human primary spongiosa: quantified across age in rib (byers2000)",
               "mouse metaphysis: type H vessel coupling (kusumbe2014)"],
 human_evidence="direct",
 human_evidence_note="Human primary and secondary spongiosa architecture has been quantified histomorphometrically from birth to adolescence in rib specimens (byers2000).",
 species_basis=["human","mouse","rat"],
 translation_risk="low",
 translation_risk_reason="The core structural evidence in this node is human histomorphometry; the vascular coupling mechanism is murine and is flagged as such.",
 confidence="B",
 key_refs=[
  R("byers2000",11033444,"Byers S",2000,"primary","Human rib primary spongiosa height falls with age while trabecular thickness rises and number falls; secondary spongiosa bone mineral volume is stable."),
  R("kusumbe2014",24646994,"Kusumbe AP",2014,"primary","Type H capillaries in the metaphysis couple angiogenesis to osteogenesis and are the vascular substrate on which the primary spongiosa forms in mouse."),
  R("rauch2005",16172510,"Rauch F",2005,"review","Frames longitudinal growth plate output against the modelling drift that reshapes the metaphysis."),
 ],
))

for x in n: print(write(x))
