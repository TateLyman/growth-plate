import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad")
from nodes_lib import *
n=[]

n.append(dict(
 id="growth_velocity_longitudinal", name="Longitudinal growth velocity at the physis",
 aliases=["elongation rate","physeal growth rate","bone elongation velocity"],
 type="phenotype",
 summary=(
  "Longitudinal growth velocity is the axial displacement produced per unit time by a single growth plate, and "
  "it spans nearly an order of magnitude between plates of the same animal at the same moment. In 28-day-old "
  "rats the four plates studied by Wilsman and colleagues ran at approximately 50 to 400 um per 24 h. Human "
  "plates are far slower: the distal femur, the fastest human physis, averaged 1.4 cm per year between ages 5 "
  "and 8 in the Harpenden Growth Study series, which is about 38 um per day, and contributes roughly 1.3 cm per "
  "year from age 7 until the final two years of growth when it halves. Velocity is measured in animals by "
  "fluorochrome (oxytetracycline or calcein) double labelling, or continuously by implanted microtransducers; in "
  "humans only by serial radiography over months, or externally by knemometry. The rate is not steady on short "
  "timescales: implanted microtransducers in lambs show at least 90% of elongation occurs during recumbency and "
  "almost none during standing or locomotion, so velocity is mechanically gated on a diurnal cycle even where "
  "the multi-day average is smooth."),
 quantitative=[
  Q("range of elongation rates across four growth plates of one animal","50-400","um/24 h","28-day-old Long-Evans rat: proximal tibia, distal radius, distal tibia, proximal radius","rat","wilsman1996a","approximate range as stated"),
  Q("mean distal femoral growth rate","1.4","cm/year","human, ages 5-8 years, serial radiographs from the Harpenden Growth Study","human","kember1976","mean value; dispersion not reported"),
  Q("mean distal femoral growth rate expressed per day","38","um/day","human, ages 5-8 years; arithmetic conversion of 1.4 cm/year","human","kember1976","derived from the reported annual rate"),
  Q("distal femoral contribution to femoral growth after age 7","1.3","cm/year","human, ages 7 to skeletal maturity, halving in the final two years","human","pritchett1992","n = 244 children (123 boys, 121 girls), 6-monthly teleroentgenograms"),
  Q("fraction of lamb tibial elongation occurring during recumbency","90","% or more","implanted microtransducer, sampling every 167 s for 21-25 days","ovine","noonan2004","authors state at least 90%"),
 ],
 localization=["human distal femur: radiographic growth rate (kember1976, pritchett1992)",
               "rat: fluorochrome-labelled elongation across four plates (wilsman1996a)",
               "lamb: continuous microtransducer measurement (noonan2004)"],
 human_evidence="direct",
 human_evidence_note="Human physeal growth rates have been measured directly by serial radiography with roentgenstereophotogrammetric analysis in a cohort of 244 children followed 6-monthly to maturity (pritchett1992) and from the Harpenden Growth Study (kember1976).",
 species_basis=["human","rat","ovine"],
 translation_risk="low",
 translation_risk_reason="The human velocities are measured in humans; only the sub-daily temporal structure is animal-derived and is flagged as such.",
 confidence="A",
 key_refs=[
  R("pritchett1992",1735225,"Pritchett JW",1992,"primary","Distal femur contributes ~70% of femoral growth and ~1.3 cm/yr after age 7 in 244 children followed to maturity."),
  R("kember1976",1018028,"Kember NF",1976,"primary","Distal femoral growth averaged 1.4 cm/yr at ages 5-8 in the Harpenden Growth Study series."),
  R("wilsman1996a",8764865,"Wilsman NJ",1996,"primary","Four rat growth plates spanning approximately 50-400 um per 24 h were compared at one time point."),
  R("noonan2004",15502578,"Noonan KJ",2004,"primary","At least 90% of lamb tibial elongation occurs during recumbency."),
 ],
 open_questions=["g_l1arch_006","g_l1arch_005"],
))

n.append(dict(
 id="saltation_stasis_growth", name="Saltation and stasis growth",
 aliases=["saltatory growth","episodic growth","mini growth spurts"],
 type="hypothesis",
 summary=(
  "The saltation-and-stasis model holds that linear growth is not continuous but occurs in discrete bursts "
  "separated by intervals of true zero growth. Lampl, Veldhuis and Johnson reported from serial infant "
  "measurements (n = 31 infants measured weekly, semi-weekly or daily over the first 21 months) that length "
  "accrues in 0.5-2.5 cm saltations separated by stasis intervals of 2-63 days, with 90-95% of days growth-free. "
  "The claim is contested on both statistical and biological grounds. Klein and colleagues measured rabbit "
  "proximal tibial elongation directly with about 15-fold better precision than human anthropometry and obtained "
  "a single Gaussian distribution of daily velocities rather than the bimodal distribution the model predicts, "
  "concluding growth is continuous; Heinrichs et al. published a further critique in Science. The saltation camp "
  "replied that frequency-distribution shape cannot exclude saltation, showing by Monte Carlo simulation that a "
  "genuinely pulsatile process can produce unimodal, left- or right-skewed distributions depending on sampling "
  "frequency, measurement error and study duration. A third position holds that short-term growth is chaotic "
  "rather than discretely saltatory, with mini growth spurts and no true stasis. Separately from the statistical "
  "dispute there is one unambiguous, directly measured discontinuity: in lambs with implanted microtransducers "
  "at least 90% of elongation occurs during recumbency, so growth is mechanically gated on a diurnal cycle. "
  "Canine proximal tibial growth measured with implanted tantalum markers has been reported as following the "
  "saltation-and-stasis model. The dispute has never been settled because no group has measured the same "
  "preparation with both camps' instruments."),
 quantitative=[
  Q("saltation amplitude","0.5-2.5","cm per event","human infants, first 21 months, serial length measurement","human","lampl1992","range across events; n = 31 infants (19 female, 12 male)"),
  Q("stasis interval duration","2-63","days","human infants, first 21 months","human","lampl1992","range across intervals"),
  Q("proportion of days without measurable growth","90-95","% of days","human infants, first 21 months","human","lampl1992","as stated by the authors"),
  Q("implied annualised velocity during a growth event","greater than 350","cm/year","recalculation of the saltation model by its critics","human","klein1994","critics' arithmetic, stated in the abstract"),
  Q("precision advantage of rabbit proximal tibial measurement over human anthropometry","15","fold","implanted marker measurement of daily growth rate","rabbit","klein1994","as stated"),
  Q("shape of the daily growth velocity distribution","single Gaussian","qualitative","rabbit proximal tibia, direct daily measurement","rabbit","klein1994","interpreted by the authors as evidence of continuous growth"),
  Q("fraction of elongation occurring during recumbency","90","% or more","lamb tibia, implanted microtransducer sampled every 167 s for 21-25 days","ovine","noonan2004","as stated"),
 ],
 localization=["human infants: external anthropometry (lampl1992)",
               "rabbit proximal tibia: direct implanted measurement (klein1994)",
               "lamb tibia: continuous microtransducer (noonan2004)",
               "dog proximal tibia: tantalum markers, monthly radiographs (mcbrien2011)"],
 human_evidence="direct",
 human_evidence_note="The human evidence is serial anthropometry in infants (lampl1992) and its statistical re-analysis; there is no direct human measurement of physeal elongation at daily resolution.",
 species_basis=["human","rabbit","ovine","rat"],
 translation_risk="moderate",
 translation_risk_reason="The pro-saltation evidence is human but indirect (surface anthropometry with a technical error exceeding the mean daily increment); the strongest anti-saltation evidence is direct but from rabbit. Neither camp has measured the human physis.",
 confidence="D",
 key_refs=[
  R("lampl1992",1439787,"Lampl M",1992,"primary","Infant length accrues in 0.5-2.5 cm saltations separated by 2-63 day stasis intervals, with 90-95% of days growth-free."),
  R("klein1994",8119172,"Klein KO",1994,"primary","Direct daily measurement of rabbit proximal tibial elongation gives a unimodal Gaussian velocity distribution, not the predicted bimodal one."),
  R("johnson1996",8940335,"Johnson ML",1996,"primary","Monte Carlo simulation shows frequency-distribution shape cannot exclude a saltatory process."),
  R("hermanussen1998",9661976,"Hermanussen M",1998,"primary","Rat short-term growth is a chaotic series of mini growth spurts rather than discrete saltation with true stasis."),
  R("noonan2004",15502578,"Noonan KJ",2004,"primary","At least 90% of lamb tibial elongation occurs during recumbency, establishing a real load-gated diurnal discontinuity."),
  R("mcbrien2011",21470252,"McBrien CS",2011,"primary","Canine proximal tibial growth measured with implanted tantalum markers is reported to follow a saltation-and-stasis model."),
  R("heinrichs1995",7716552,"Heinrichs C",1995,"primary","Science report on patterns of human growth published as part of the saltation controversy; full text not retrieved."),
  R("lampl2017",28217849,"Lampl M",2017,"review","Argues that saltation and stasis is the auxological signature of discretely timed hypertrophic expansion events at the growth plate."),
 ],
 open_questions=["g_l1arch_005","g_l1arch_006"],
 contradicts=["klein1994","lampl1992","mcbrien2011"],
 pending_source="heinrichs1995",
))

n.append(dict(
 id="site_specific_growth_rate", name="Site-specific growth rate (differential growth)",
 aliases=["differential growth","plate-specific elongation rate"],
 type="phenotype",
 summary=(
  "Every growth plate in an individual runs at its own velocity at the same moment, and it is this differential "
  "growth that produces limb proportions. In the human lower limb the distal femoral physis supplies about 70% "
  "of femoral length and the proximal tibial physis about 57% of tibial length, and these proportions themselves "
  "shift with age - the distal femoral share rises from 60% at age 7 to 90% at 14 in girls and from 55% at 7 to "
  "90% at 16 in boys. In the upper limb the proximal humeral physis supplies about 80% of humeral length, the "
  "distal radius about 80% and the distal ulna about 85%, with the distal-dominant proportion increasing through "
  "childhood. Mechanistically, differential growth is not explained by any single parameter. Wilsman and "
  "colleagues showed that eight independent chondrocytic variables are involved and that seven of them vary "
  "between plates of one 28-day-old rat; cell cycle time differs 2.5-fold with the variation almost entirely in "
  "G1; final hypertrophic cell volume correlates with rate at r=0.98; and the relative contribution of "
  "hypertrophy falls from 59% to 44% as plates get slower, with matrix synthesis taking up the difference. In "
  "mouse the site difference maps onto whether the IGF-dependent third phase of enlargement is executed or "
  "truncated. Differential growth is not present from the beginning: in rat it emerges postnatally."),
 quantitative=[
  Q("distal femoral share of femoral growth","70","% of femoral length","human, overall across ages 7 to maturity","human","pritchett1992","n = 244 children; range 55-90% depending on age and sex"),
  Q("proximal tibial share of tibial growth","57","% of tibial length","human, overall across ages 7 to maturity","human","pritchett1992","range 50-80% depending on age and sex"),
  Q("proximal humeral share of humeral growth","80","% of humeral length","human, overall; <75% before age 2, 85% at 8, 90% after 11","human","pritchett1991","n = 200 subjects"),
  Q("distal radial share of radial growth","80","% of radial length","human, overall; 85% at age 5, 90% by age 8","human","pritchett1991","n = 200"),
  Q("distal ulnar share of ulnar growth","85","% of ulnar length","human, overall; 90% by age 5, 95% after age 8","human","pritchett1991","n = 200"),
  Q("number of independent chondrocytic variables involved in differential growth","8","variables","28-day-old rat, four growth plates; seven of the eight vary between plates","rat","wilsman1996","authors' model, validated by the match between calculated cell production and loss"),
  Q("spread in proliferative cell cycle time between plates of one animal","2.5","fold (30.9 to 76.3 h)","28-day-old rat","rat","wilsman1996a","difference significant at p<0.05"),
  Q("age at which differential growth first appears","postnatal","qualitative","rat, four plates sampled at 24 time points from gestational day 17","rat","wilsman2008","onset described as postnatal, correlated with hypertrophic volume and cell production changes"),
 ],
 localization=["human: per-plate contributions measured radiographically (pritchett1992, pritchett1991)",
               "rat: mechanistic decomposition (wilsman1996, wilsman1996a, wilsman2008)",
               "mouse: phase-3 truncation as the site-specific switch (cooper2013)"],
 human_evidence="direct",
 human_evidence_note="Per-plate contributions to limb segment length have been measured directly in two human radiographic cohorts of 244 and 200 children followed to skeletal maturity (pritchett1992, pritchett1991).",
 species_basis=["human","rat","mouse"],
 translation_risk="moderate",
 translation_risk_reason="The human proportions are solid human data, but every mechanistic explanation of why plates differ is rodent, and the rodent explanation itself is a multi-variable model rather than a single lever.",
 confidence="B",
 key_refs=[
  R("pritchett1992",1735225,"Pritchett JW",1992,"primary","Distal femur supplies ~70% of femoral and proximal tibia ~57% of tibial growth in 244 children, with age- and sex-dependent shifts."),
  R("pritchett1991",2060215,"Pritchett JW",1991,"primary","Proximal humerus ~80%, distal radius ~80% and distal ulna ~85% of their segment's growth in 200 subjects."),
  R("wilsman1996",8982136,"Wilsman NJ",1996,"primary","Differential growth requires eight independent chondrocytic variables, seven of which vary between plates of one animal."),
  R("cooper2013",23485973,"Cooper KL",2013,"primary","Whether the IGF-dependent third phase of enlargement is executed or truncated distinguishes fast from slow plates in mouse."),
  R("wilsman2008",18404738,"Wilsman NJ",2008,"primary","Differential growth among rat growth plates emerges postnatally and tracks hypertrophic volume and cell production."),
 ],
 open_questions=["g_l1arch_010","g_l1arch_001"],
))

n.append(dict(
 id="appositional_growth", name="Appositional (circumferential) growth",
 aliases=["latitudinal growth","radial growth","periosteal apposition"],
 type="process",
 summary=(
  "Appositional growth widens a bone, in contrast to the longitudinal growth generated by the physis. Two "
  "distinct processes contribute: periosteal bone apposition on the outer cortex, which thickens the diaphysis, "
  "and latitudinal enlargement of the cartilaginous plate itself, to which the groove of Ranvier supplies cells "
  "at the plate margin. The two modes are quantitatively separable in mouse by micro-CT: measuring the "
  "equivalent radius of the chondro-osseous junction against its axial displacement gives an expansion-to- "
  "elongation ratio that falls from 0.18 (distal femur) and 0.16 (proximal tibia) at E17.5-E18.5 to 0 and 0.04 "
  "respectively by P32-P40. In other words, embryonic bones widen almost a fifth as fast as they lengthen, and "
  "postnatal bones essentially stop widening at the plate while continuing to elongate. The same study connects "
  "this to cellular architecture: embryonic clones are mostly orthogonally oriented clusters and postnatal ones "
  "are mostly columns, suggesting that whether the division plane rotation is completed determines whether a "
  "clone contributes to widening or to lengthening."),
 quantitative=[
  Q("expansion-to-elongation ratio","0.18","dimensionless ratio","mouse distal femur, E17.5-E18.5, micro-CT of registered bones","mouse","rubin2024","computed from equivalent radius change over elongation"),
  Q("expansion-to-elongation ratio","0.16","dimensionless ratio","mouse proximal tibia, E17.5-E18.5","mouse","rubin2024","as above"),
  Q("expansion-to-elongation ratio","0","dimensionless ratio","mouse distal femur, P32-P40","mouse","rubin2024","expansion negligible relative to elongation"),
  Q("expansion-to-elongation ratio","0.04","dimensionless ratio","mouse proximal tibia, P32-P40","mouse","rubin2024","non-monotonic decrease seen in proximal fibula and distal tibia"),
 ],
 localization=["mouse: quantified across eight growth plates and three time windows (rubin2024)",
               "rabbit: groove of Ranvier as the source of latitudinal cells (shapiro1977)",
               "human: not quantified separately from total bone width"],
 human_evidence="absent",
 human_evidence_note="No human study separates plate latitudinal enlargement from periosteal apposition quantitatively; human data exist only for total bone width.",
 species_basis=["mouse","rabbit"],
 translation_risk="high",
 translation_risk_reason="The expansion-to-elongation ratios are mouse micro-CT values and the cellular explanation is mouse clonal analysis; nothing equivalent has been measured in human bone.",
 confidence="C",
 key_refs=[
  R("rubin2024",39269144,"Rubin S",2024,"primary","Expansion-to-elongation ratio falls from 0.16-0.18 embryonically to 0-0.04 by P40, correlating with the shift from clusters to columns."),
  R("shapiro1977",71299,"Shapiro F",1977,"primary","The groove of Ranvier is the perichondrial source of cells for latitudinal growth of the plate in rabbit."),
  R("rauch2005",16172510,"Rauch F",2005,"review","Contrasts longitudinal growth plate output with periosteal appositional growth and its role in bone stability."),
 ],
 open_questions=["g_l1arch_013"],
))

n.append(dict(
 id="bone_modeling_drift", name="Bone modelling drift",
 aliases=["modelling drift","cortical drift"],
 type="process",
 summary=(
  "Modelling drift is the coordinated apposition on one surface and resorption on the opposite surface that "
  "moves a bone cross-section through space without changing its shape, and it is what allows the wide "
  "metaphysis produced by the growth plate to be reshaped into the narrow diaphysis as the plate moves away. "
  "Where longitudinal growth is a cartilage process, drift is entirely an osteoblast-osteoclast process on "
  "periosteal and endosteal surfaces, so the two can be dissociated pharmacologically and genetically: a drug "
  "that blocks osteoclasts will leave elongation intact while preventing funnelisation, producing the "
  "club-shaped metaphyses seen in osteopetrosis. Rauch frames longitudinal and appositional growth as "
  "complementary determinants of bone stability, with drift providing the mechanical adaptation that "
  "longitudinal growth alone cannot. This node is architectural context for the growth plate rather than a "
  "growth plate mechanism, and its own quantitative parameters (drift rates, surface-specific apposition) "
  "belong to bone remodelling rather than to physeal biology."),
 quantitative=[
  Q("expansion-to-elongation ratio at the chondro-osseous junction, postnatal","0-0.04","dimensionless ratio","mouse distal femur and proximal tibia P32-P40; sets the width the drift process must subsequently reshape","mouse","rubin2024","as reported"),
 ],
 localization=["human and rodent metaphysis and diaphysis: periosteal and endosteal surfaces"],
 human_evidence="indirect",
 human_evidence_note="Modelling drift in humans is inferred from bone histomorphometry and from the metaphyseal deformities of osteoclast-deficient disorders rather than from direct measurement at the physis.",
 species_basis=["human","rat","mouse"],
 translation_risk="low",
 translation_risk_reason="Surface-based modelling is a general vertebrate bone process well documented in human histomorphometry; the risk here is only that this node is contextual rather than physeal.",
 confidence="C",
 key_refs=[
  R("rauch2005",16172510,"Rauch F",2005,"review","Frames longitudinal and appositional growth and the modelling drift that reshapes the metaphysis as complementary determinants of bone stability."),
  R("rubin2024",39269144,"Rubin S",2024,"primary","Quantifies the width of new bone generated at the chondro-osseous junction relative to elongation across development."),
 ],
))

n.append(dict(
 id="metaphyseal_funnelization", name="Metaphyseal funnelisation",
 aliases=["funnelization","metaphyseal remodelling","metaphyseal cutback"],
 type="process",
 summary=(
  "Funnelisation is the narrowing of the flared metaphysis into the tubular diaphysis as the growth plate "
  "advances away from it. Because the plate deposits bone at its own full diameter, every increment of "
  "elongation leaves behind a segment that is too wide for the diaphysis; osteoclastic resorption on the outer "
  "metaphyseal cortex removes the excess. The rate at which funnelisation must operate is therefore set by the "
  "plate: it equals the product of the elongation rate and the difference between plate diameter and diaphyseal "
  "diameter. In mouse the width the process must handle is quantified by the expansion-to-elongation ratio, "
  "which falls to near zero postnatally, meaning that in older animals almost all the metaphyseal reshaping "
  "burden comes from the historical width laid down earlier rather than from continuing widening. Failure of "
  "funnelisation produces the Erlenmeyer-flask metaphysis of osteopetrosis and storage disorders, which is the "
  "clinical demonstration that this is an osteoclast-dependent process separable from the plate itself. No study "
  "has measured a funnelisation rate in human bone against a simultaneously measured physeal elongation rate."),
 quantitative=[
  Q("expansion-to-elongation ratio setting the funnelisation burden","0.16-0.18 (embryonic) falling to 0-0.04 (P32-P40)","dimensionless ratio","mouse distal femur and proximal tibia","mouse","rubin2024","as reported"),
 ],
 localization=["mouse metaphysis: expansion quantified (rubin2024)",
               "human metaphysis: failure phenotypes described clinically; rate not measured"],
 human_evidence="indirect",
 human_evidence_note="Human evidence is the radiographic phenotype of failed funnelisation in osteoclast disorders; no human study measures funnelisation rate against physeal elongation.",
 species_basis=["mouse","human"],
 translation_risk="moderate",
 translation_risk_reason="The process is unambiguous in humans from disease phenotypes, but every quantitative parameter available is murine.",
 confidence="C",
 key_refs=[
  R("rubin2024",39269144,"Rubin S",2024,"primary","Quantifies growth plate expansion relative to elongation across development, setting the geometric burden funnelisation must remove."),
  R("rauch2005",16172510,"Rauch F",2005,"review","Places metaphyseal reshaping within the balance of longitudinal and appositional growth."),
  R("kusumbe2014",24646994,"Kusumbe AP",2014,"primary","Type H vessels define the metaphyseal region in which osteogenesis and remodelling are coupled."),
 ],
))

for x in n: print(write(x))
