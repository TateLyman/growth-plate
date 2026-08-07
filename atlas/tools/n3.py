import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad")
from nodes_lib import *
n=[]

n.append(dict(
 id="resting_chondrocyte", name="Resting (reserve) zone chondrocyte", aliases=["reserve chondrocyte","RZ chondrocyte"],
 type="cell_type",
 summary=(
  "Resting chondrocytes are small, rounded cells lying singly or in pairs in abundant matrix at the epiphyseal "
  "end of the plate. In mouse they include a PTHrP-expressing subpopulation with formal skeletal stem cell "
  "properties: these cells self-renew and generate the columnar clones of the proliferative zone, but they "
  "acquire that behaviour only after the secondary ossification centre forms, which means the stem compartment "
  "is a postnatal acquisition rather than a property of the embryonic plate. The label 'resting' overstates "
  "their quiescence. A systematic review of the primary data finds that reported labelling indices and even the "
  "operational definition of quiescence differ widely between studies, so the zone contains cycling cells at "
  "rates that are not agreed. A separate mouse population at the plate periphery, the borderline chondrocytes, "
  "leaves the cartilage altogether and becomes marrow stroma and osteoblasts. In human tissue none of this has "
  "been demonstrated: the human resting zone is described morphologically, and the only human proliferation data "
  "come from an in vitro thymidine labelling study in which two of four specimens produced no labelled cells "
  "anywhere in the plate."),
 quantitative=[
  Q("human specimens yielding no labelled cells after in vitro tritiated thymidine exposure","2 of 4","specimens","human growth plates, in vitro labelling","human","thurston1985","author-reported; possible technical failure discussed by the authors"),
 ],
 localization=["mouse RZ: PTHrP+ skeletal stem cells confirmed by lineage tracing (mizuhashi2018)",
               "human RZ: morphology described, stem identity unconfirmed"],
 human_evidence="absent",
 human_evidence_note="No human study demonstrates stem or progenitor behaviour of resting zone chondrocytes; the human evidence is descriptive histology only.",
 species_basis=["mouse","human"],
 translation_risk="high",
 translation_risk_reason="Stem identity rests on inducible Cre lineage tracing in mouse, and it is conditional on secondary ossification centre formation - a developmental milestone whose human timing relative to plate maturation has not been mapped onto this biology.",
 confidence="C",
 key_refs=[
  R("mizuhashi2018",30401834,"Mizuhashi K",2018,"primary","PTHrP+ resting zone chondrocytes are skeletal stem cells forming columnar clones after secondary ossification centre formation."),
  R("avijgan2026",41795828,"Avijgan M",2026,"systematic_review","Reported labelling indices and definitions of quiescence in the resting zone vary widely across the primary literature."),
  R("thurston1985",3864550,"Thurston MN",1985,"primary_abstract_only","In vitro thymidine labelling of human growth plates gave no labelled cells in two of four subjects."),
 ],
 open_questions=["g_l1arch_012"],
 pending_source="thurston1985",
))

n.append(dict(
 id="proliferative_chondrocyte", name="Proliferative zone chondrocyte", aliases=["flattened chondrocyte","columnar chondrocyte"],
 type="cell_type",
 summary=(
  "Proliferative chondrocytes are flattened discs whose short axis lies along the growth direction, stacked in "
  "clonal columns. They divide with their division plane perpendicular to the long bone axis and then rotate as "
  "a doublet so that the daughters end up stacked, a manoeuvre that requires beta1 integrin and N-cadherin "
  "mediated adhesion. In rat their cycle is long and its length is set by G1: total cycle time ranges from 30.9 h "
  "in the fast proximal tibia to 76.3 h in the slow proximal radius, while S, G2 and M are essentially fixed at "
  "3.4-6.1 h, 3.0 h and 0.5-0.6 h respectively. Beta1 integrin deletion delays G1/S progression as well as "
  "blocking rotation, which links adhesion directly to cycle control. Human proliferative chondrocytes have "
  "never had their cycle measured; the only human number is a derived mean cycle time of roughly 20 days for the "
  "distal femur. In quantitative terms, the direct contribution of these divisions to elongation is small (9% in "
  "the fast rat proximal tibia); their function is to set the number of cells that will subsequently hypertrophy."),
 quantitative=[
  Q("total cell cycle time","30.9","h","proximal tibia, 28-day-old rat","rat","wilsman1996a","not reported"),
  Q("total cell cycle time","76.3","h","proximal radius, 28-day-old rat","rat","wilsman1996a","significantly different from all other plates, p<0.05"),
  Q("S phase duration","3.4-6.1","h","four rat growth plates, 28-day-old","rat","wilsman1996a","range across plates"),
  Q("G2 phase duration","3.0","h","four rat growth plates, 28-day-old","rat","wilsman1996a","not reported"),
  Q("M phase duration","0.5-0.6","h","four rat growth plates, 28-day-old","rat","wilsman1996a","range across plates"),
  Q("cell volume at the start of hypertrophic enlargement","600","fl","mouse proximal tibia, dissociated live cells","mouse","cooper2013","approximate"),
 ],
 localization=["rat PZ: in vivo BrdU kinetics (wilsman1996a)",
               "mouse PZ: rotation and adhesion mechanism (aszodi2003, romereim2014, greer2024)",
               "human PZ: kinetics not measured"],
 human_evidence="indirect",
 human_evidence_note="Human proliferative chondrocytes have been counted per column and their cycle time derived arithmetically (kember1976), but no direct human kinetic measurement exists.",
 species_basis=["rat","mouse","human"],
 translation_risk="high",
 translation_risk_reason="Cell-cycle structure is rodent-only and the derived human cycle time differs from the rat by more than an order of magnitude.",
 confidence="C",
 key_refs=[
  R("wilsman1996a",8764865,"Wilsman NJ",1996,"primary","Rat PZ cycle time 30.9-76.3 h with the variation concentrated in G1; S, G2 and M durations reported."),
  R("aszodi2003",14522949,"Aszodi A",2003,"primary","Beta1 integrin is required both for post-mitotic rotation into columns and for normal G1 progression and cytokinesis."),
  R("kember1976",1018028,"Kember NF",1976,"primary","24 cells per proliferative column in human distal femur with a derived ~20-day cycle time."),
  R("cooper2013",23485973,"Cooper KL",2013,"primary","Chondrocytes enter hypertrophy at roughly 600 fl in mouse proximal tibia."),
 ],
 open_questions=["g_l1arch_002","g_l1arch_012"],
))

n.append(dict(
 id="prehypertrophic_chondrocyte", name="Prehypertrophic chondrocyte", aliases=["maturing chondrocyte","PHZ chondrocyte"],
 type="cell_type",
 summary=(
  "Prehypertrophic chondrocytes are post-mitotic cells that have committed to terminal differentiation but have "
  "not yet begun the swelling phase of enlargement. Quantitatively they occupy phase 1 of the enlargement "
  "trajectory: in mouse they roughly triple their volume from about 600 fl to about 2000 fl while holding dry "
  "mass density at the normal 0.183 pg/fl, so this is genuine biosynthetic hypertrophy with proportionate "
  "increase in macromolecular content, not fluid uptake. The transition out of this state is the growth-rate "
  "determining decision, because whether a cell goes on to complete phase 2 swelling and the IGF-dependent phase "
  "3 determines its final volume and therefore its contribution to elongation. Structurally, unbiased "
  "stereological stratification is required to place the boundary, because the morphological transition is "
  "gradual; the marker-based definition (Indian hedgehog, PTH1R) that is used routinely is murine and has no "
  "validated human counterpart."),
 quantitative=[
  Q("volume range occupied by phase 1 of enlargement","600-2000","fl","mouse proximal tibia; dry mass density held at 0.183 pg/fl","mouse","cooper2013","approximate"),
  Q("fold volume increase during phase 1","3","fold","mouse proximal tibia","mouse","cooper2013","approximate"),
 ],
 localization=["mouse PHZ: defined by marker expression and volume trajectory","human PHZ: not separately defined"],
 human_evidence="absent",
 human_evidence_note="No human study defines or quantifies a prehypertrophic chondrocyte compartment separately from the proliferative and hypertrophic zones.",
 species_basis=["mouse","rat"],
 translation_risk="high",
 translation_risk_reason="Both the marker definition and the volume trajectory are murine; the compartment has no operational human definition.",
 confidence="C",
 key_refs=[
  R("cooper2013",23485973,"Cooper KL",2013,"primary","Phase 1 of enlargement is a 3-fold volume increase at constant dry mass density, preceding the swelling phase."),
  R("breur1994",7943757,"Breur GJ",1994,"primary","Defines by stereology where in the rat proximal tibial plate chondrocyte volume and shape change begins."),
 ],
 open_questions=["g_l1arch_008"],
))

n.append(dict(
 id="hypertrophic_chondrocyte", name="Hypertrophic chondrocyte", aliases=["terminal hypertrophic chondrocyte","enlarged chondrocyte"],
 type="cell_type",
 summary=(
  "The hypertrophic chondrocyte is the cell whose volume increase produces most of the elongation of a long "
  "bone. In mouse proximal tibia it reaches about 14,000 fl from a starting volume of about 600 fl, a roughly "
  "23-fold increase, achieved by three sequential mechanisms: proportionate biosynthetic growth, then a swelling "
  "phase that dilutes dry mass density from 0.183 to about 0.07 pg/fl, then renewed proportionate growth at that "
  "low density. In rat the same process is described stereologically as a 4-fold height and 10-fold volume "
  "increase accompanied by 2-5 fold increases in rough endoplasmic reticulum, Golgi and mitochondrial "
  "compartments, so these are not degenerate cells; time-lapse imaging confirms they remain alive up to the "
  "chondro-osseous junction, passing through a discrete condensation stage immediately before removal. Final "
  "volume correlates linearly with elongation rate across four plates and two ages in rat (r=0.98) and pig "
  "(r=0.83), with a species-specific slope, and the relationship fails altogether in birds. No human hypertrophic "
  "chondrocyte volume has been reported with unbiased stereology."),
 quantitative=[
  Q("final volume, fast plate","14000","fl","mouse proximal tibia","mouse","cooper2013","approximate"),
  Q("total fold volume increase","23","fold","mouse proximal tibia, ~600 fl to ~14,000 fl","mouse","cooper2013","derived from the reported start and end volumes"),
  Q("dry mass density, small prehypertrophic cells","0.183","pg/fl","mouse; equals the normal healthy-cell value of 0.182 pg/fl","mouse","cooper2013","not reported"),
  Q("dry mass density, largest hypertrophic cells","0.07","pg/fl","mouse proximal tibia","mouse","cooper2013","approximate; ~60% dilution"),
  Q("mean cell height increase, proliferative to late hypertrophic","4","fold","rat proximal tibia, stereology","rat","hunziker1987","not reported"),
  Q("mean cell volume increase, proliferative to late hypertrophic","10","fold","rat proximal tibia, stereology","rat","hunziker1987","not reported"),
  Q("correlation of final volume with elongation rate","0.98","Pearson r","rat, four plates, 21 and 35 days","rat","breur1991","as reported"),
  Q("correlation of final volume with elongation rate","0.83","Pearson r","Yucatan pig, four plates, 21 and 35 days","porcine","breur1991","as reported"),
 ],
 localization=["mouse HZ: single-cell volume and density measured (cooper2013)",
               "rat HZ: stereology and ultrastructure (hunziker1987)",
               "swine HZ: terminal condensation stage described (farnum1989a)",
               "human HZ: cell heights reported but not volumes (thurston1985)"],
 human_evidence="indirect",
 human_evidence_note="Human hypertrophic cell heights were measured in an in vitro labelling study (thurston1985, abstract only); no human volume measurement exists.",
 species_basis=["mouse","rat","porcine","chicken"],
 translation_risk="high",
 translation_risk_reason="The volume-versus-growth-rate relationship that makes this cell the central lever has a species-specific slope between rat and pig and does not hold in birds, so human values cannot be predicted from rodent data.",
 confidence="C",
 key_refs=[
  R("cooper2013",23485973,"Cooper KL",2013,"primary","Mouse hypertrophic chondrocytes reach ~14,000 fl via three phases including dry-mass-diluting swelling."),
  R("hunziker1987",3543020,"Hunziker EB",1987,"primary","4-fold height, 10-fold volume and 2-5 fold organelle increases in rat hypertrophic chondrocytes."),
  R("breur1991",2010838,"Breur GJ",1991,"primary","Final hypertrophic volume correlates linearly with elongation rate in rat and pig with different slopes."),
  R("farnum1990",2201757,"Farnum CE",1990,"primary","Terminal hypertrophic chondrocytes are viable living cells at the chondro-osseous junction."),
  R("barreto1994",8146454,"Barreto C",1994,"primary","The mammalian volume/growth-rate relationship does not hold in ducklings and chicks."),
 ],
 open_questions=["g_l1arch_009","g_l1arch_008"],
 contradicts=["barreto1994"],
))

n.append(dict(
 id="septoclast", name="Septoclast", aliases=["cartilage-resorbing perivascular cell","FABP5+ chondro-osseous border cell"],
 type="cell_type",
 summary=(
  "The septoclast is a mononuclear, spindle-shaped, cathepsin B-rich cell sitting at the chondro-osseous "
  "junction in intimate contact with the distal buds of the invading metaphyseal capillaries, first defined in "
  "rat as the cell that resorbs the transverse cartilage septa. Lineage tracing in mouse shows septoclasts are "
  "mesenchymal, not haematopoietic: they are FABP5+, PDGFRalpha+ and PDGFRbeta+, NG2+ but CD146-negative, and "
  "they lack the CD68/vATPase profile of osteoclasts, which are also present at the junction but far less "
  "abundant there. Their specification requires the Notch ligand Dll4 supplied by endothelial cells, which "
  "makes them a directly angiogenesis-coupled catabolic cell. They disappear in adult and ageing bone in "
  "parallel with the cessation of growth, and re-emerge with growing vessels during fracture healing. Marker "
  "assignment is not fully settled: FABP4 is upregulated in septoclasts of FABP5-deficient mice, indicating "
  "redundancy, and their origin has been assigned variously to pericytes and to the perichondrium. Every "
  "primary observation is rodent or bovine; a full search of the septoclast literature returns no human tissue "
  "study whatsoever."),
 quantitative=[
  Q("abundance at the chondro-osseous interface relative to osteoclasts","significantly more abundant","qualitative","3-week-old wild-type mouse femur, FABP5 vs CD68/vATPase immunostaining","mouse","sivaraj2022","n = 6 animals"),
  Q("proportion of septoclasts expressing the Pdgfra-GFP reporter","reported as a percentage in Fig. 1c","% of FABP5+ cells","3-week-old mouse femur chondro-osseous border","mouse","sivaraj2022","n = 6; exact percentage read from figure, not stated in text",True),
  Q("primary studies of septoclasts in human tissue","0","studies","Europe PMC query 'septoclast*', 54 records screened, 2026-08-05","human","sivaraj2022","null result; see search log g_l1arch_003"),
 ],
 localization=["mouse chondro-osseous border: FABP5+/PDGFRa+/PDGFRb+/NG2+/CD146- (sivaraj2022)",
               "rat chondro-osseous junction: cathepsin B-rich (lee1995)",
               "human: not demonstrated"],
 human_evidence="absent",
 human_evidence_note="A complete screen of the 54-record septoclast literature found no primary study in human tissue; the closest human work at the chondro-osseous region (walzer2014) did not stain for septoclast markers.",
 species_basis=["mouse","rat","bovine"],
 translation_risk="high",
 translation_risk_reason="An entire cell type with a distinct lineage, marker set and druggable Notch dependency has been defined without a single human observation. If human cartilage septa are removed by osteoclasts instead, Dll4-directed reasoning does not transfer.",
 confidence="C",
 key_refs=[
  R("sivaraj2022",35091558,"Sivaraj KK",2022,"primary","FABP5+ septoclasts are mesenchyme-derived, Dll4-dependent, more abundant than osteoclasts at the chondro-osseous border, and disappear in adult bone."),
  R("lee1995",7730591,"Lee ER",1995,"primary","Original definition of the septoclast as a cathepsin B-rich, non-osteoclastic cell resorbing growth plate cartilage septa in rat."),
  R("bando2018",29464321,"Bando Y",2018,"primary","Traced the origin and development of septoclasts during endochondral ossification in mice."),
  R("bando2021",33398436,"Bando Y",2021,"primary","FABP4 is expressed and upregulated in septoclasts of FABP5-deficient mice, showing marker redundancy."),
  R("odgren2016",26818783,"Odgren PR",2016,"review","Distinguishes osteoclasts, chondroclasts and septoclasts as separate catabolic populations at the vascular invasion front."),
 ],
 open_questions=["g_l1arch_003"],
))

n.append(dict(
 id="cartilage_septum_resorption", name="Cartilage septum resorption",
 aliases=["septal resorption","transverse septum breakdown"],
 type="process",
 summary=(
  "Removal of cartilage at the metaphyseal face is selective, not wholesale. The transverse septa separating "
  "successive chondrocytes in a column are removed to open a channel for the capillary bud, while the "
  "mineralised longitudinal septa are preserved and become the cores of the primary spongiosa trabeculae. "
  "Serial-section analysis in swine shows that invading endothelial cells penetrate the non-calcified "
  "pericellular and territorial matrix compartments specifically, which explains the geometric selectivity. In "
  "rodents the executing cell is the septoclast, a cathepsin-B-rich, FABP5+ mesenchymal cell whose "
  "differentiation depends on endothelial Dll4 and whose transcriptional programme includes Ctsb and Mmp13; "
  "osteoclasts are present but sparse at this interface. The rate of septal removal must equal the rate of "
  "chondrocyte production for the plate to hold constant height, and in rat that means one cell per column every "
  "three hours. In human tissue, septal thickness has been measured across age - it increases from birth to "
  "adolescence in rib - but the resorbing cell has never been identified."),
 quantitative=[
  Q("direction of cartilage septal thickness change with age","increasing","qualitative","human rib growth plate, birth to adolescence","human","byers2000","absolute values not available from abstract"),
  Q("septal removal rate implied by steady state","1 per 3","cells per hour per column","rat proximal tibia","rat","hunziker1987","equivalently 8 per day"),
  Q("matrix compartment targeted by invading endothelium","non-calcified pericellular and territorial matrix","qualitative","distal hypertrophic zone, Yucatan swine","porcine","farnum1989","descriptive"),
 ],
 localization=["mouse: FABP5+ septoclast-mediated (sivaraj2022)",
               "rat: cathepsin B-rich septoclasts (lee1995)",
               "human: septal thickness measured, resorbing cell unidentified (byers2000)"],
 human_evidence="indirect",
 human_evidence_note="Human cartilage septal thickness and number have been quantified across age (byers2000), but no human study identifies the cell that resorbs the septa.",
 species_basis=["mouse","rat","porcine","human"],
 translation_risk="high",
 translation_risk_reason="The mechanism is entirely rodent; only the static septal geometry has been measured in humans.",
 confidence="C",
 key_refs=[
  R("sivaraj2022",35091558,"Sivaraj KK",2022,"primary","Septoclasts, not osteoclasts, mediate matrix degradation and chondrocyte phagocytosis at the chondro-osseous border."),
  R("farnum1989",2760737,"Farnum CE",1989,"primary","Endothelial penetration is into non-calcified pericellular and territorial matrix, explaining selective septal removal."),
  R("byers2000",11033444,"Byers S",2000,"primary","Human cartilage septal thickness increases and septal number falls in the proliferative zone across childhood."),
  R("lee1995",7730591,"Lee ER",1995,"primary","Cathepsin B-rich septoclast defined as the cell resorbing growth plate cartilage septa in rat."),
 ],
 open_questions=["g_l1arch_003"],
))

for x in n: print(write(x))
