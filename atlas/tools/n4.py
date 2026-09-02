import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad")
from nodes_lib import *
n=[]

n.append(dict(
 id="chondrocyte_column_formation", name="Chondrocyte column formation",
 aliases=["columnarisation","column morphogenesis"],
 type="process",
 summary=(
  "A proliferative chondrocyte divides with its cleavage plane perpendicular to the long bone axis, so the two "
  "daughters initially sit side by side across the growth direction. To build a column the doublet must rotate "
  "roughly 90 degrees before separating. Live imaging established that this is a rotation on a dynamic "
  "cell-cell and cell-matrix adhesion surface, not the convergent-extension intercalation originally inferred "
  "from static 2D sections; beta1 integrin, N-cadherin and alpha-parvin are each required. 3D clonal analysis "
  "has since shown that the rotation is far less reliable than the textbook picture implies. In E18.5 mouse "
  "growth plates only 17.6% (distal femur) and 19.4% (proximal tibia) of neighbouring clonal cell pairs sit at "
  "the 60-90 degree elevation angle that indicates a completed rotation; most embryonic clones are ellipsoidal "
  "clusters oriented orthogonal to the growth axis. Postnatally rotation improves but is still imperfect: within "
  "P40 columns 39.5% (distal femur) and 36.4% (proximal tibia) of divisions show complete rotation and fewer "
  "than 10% are near-perfect (80-90 degrees). A column therefore tolerates about 60% incomplete rotations before "
  "the structure buckles sideways into a cluster. This reframes columns as a postnatal, elongation-favouring "
  "configuration rather than a prerequisite for growth."),
 quantitative=[
  Q("proportion of clonal doublets with completed rotation (60-90 degrees)","17.6","% of doublets","E18.5 mouse distal femur, Col2a1-CreER:R26R-Confetti pulsed E14.5, 3D imaging","mouse","rubin2024","n = 1044 doublets, 3 biologically independent samples, 9 independent experiments"),
  Q("proportion of clonal doublets with completed rotation (60-90 degrees)","19.4","% of doublets","E18.5 mouse proximal tibia","mouse","rubin2024","n = 805 doublets, 3 biologically independent samples"),
  Q("proportion of complete rotations within postnatal columns","39.5","% of divisions","P40 mouse distal femur","mouse","rubin2024","n = 737 columns"),
  Q("proportion of complete rotations within postnatal columns","36.4","% of divisions","P40 mouse proximal tibia","mouse","rubin2024","n = 512 columns"),
  Q("proportion of near-perfect rotations (80-90 degrees) within postnatal columns","9.6","% of divisions","P40 mouse distal femur","mouse","rubin2024","n = 737 columns"),
  Q("proportion of near-perfect rotations (80-90 degrees) within postnatal columns","8.2","% of divisions","P40 mouse proximal tibia","mouse","rubin2024","n = 512 columns"),
  Q("proportion of complete rotations within postnatal clusters","15.5","% of divisions","P40 mouse distal femur clusters","mouse","rubin2024","n = 1129 clusters"),
  Q("tolerance of a column for incomplete rotations","60","% of divisions","P40 mouse; above this fraction the clone expands orthogonally and becomes a cluster","mouse","rubin2024","author-stated threshold based on elevation-angle analysis"),
  Q("clone long-axis to short-axis ratio, embryonic","0.201","PC3/PC1 ratio (mean)","E18.5 mouse distal femur clones, principal component analysis","mouse","rubin2024","SD 0.109"),
  Q("clone long-axis to short-axis ratio, embryonic","0.226","PC3/PC1 ratio (mean)","E18.5 mouse proximal tibia clones","mouse","rubin2024","SD 0.119"),
 ],
 localization=["mouse PZ: 3D clonal analysis (rubin2024); live-imaged rotation (romereim2014)",
               "human PZ: column cell counts measured (kember1976) but rotation never observed"],
 human_evidence="indirect",
 human_evidence_note="Human proliferative columns are described histologically and counted (24 cells per column in distal femur), but the rotation mechanism has never been observed in human tissue.",
 species_basis=["mouse","human"],
 translation_risk="high",
 translation_risk_reason="All mechanistic and quantitative data are from mouse live imaging and lineage tracing. Human plates have longer columns and much slower cycling, so the geometry of stacking may differ.",
 confidence="C",
 key_refs=[
  R("rubin2024",39269144,"Rubin S",2024,"primary","3D Confetti clonal analysis shows fewer than 20% of embryonic doublets are correctly stacked and that a column tolerates ~60% incomplete rotations."),
  R("romereim2014",24764078,"Romereim SM",2014,"primary","Post-mitotic doublets rotate on a dynamic adhesion surface rather than intercalating by convergent extension."),
  R("aszodi2003",14522949,"Aszodi A",2003,"primary","Beta1 integrin is required for chondrocyte rotation, G1 progression and cytokinesis."),
  R("greer2024",38294852,"Greer SE",2024,"primary","N-cadherin and beta1 integrin act coordinately to set growth plate column architecture."),
  R("yuan2023",37607905,"Yuan J",2023,"primary","alpha-parvin is required for chondrocyte column formation and long bone development."),
 ],
 open_questions=["g_l1arch_004"],
 contradicts=["chondrocyte_rotation"],
))

n.append(dict(
 id="chondrocyte_rotation", name="Post-mitotic chondrocyte rotation",
 aliases=["division plane rotation","daughter cell rotation"],
 type="process",
 summary=(
  "After a proliferative chondrocyte divides, the daughter pair remains attached and rotates so that the axis "
  "joining the two nuclei swings from transverse toward parallel with the growth direction. Live imaging of "
  "explanted growth plates showed this directly and ruled out the earlier convergent-extension model in which "
  "cells were thought to intercalate between neighbours; the sister cells never intercalate, they rotate and "
  "then separate. The rotation depends on integrin-based adhesion to the pericellular matrix and on N-cadherin "
  "mediated cell-cell adhesion: chondrocyte-specific beta1 integrin deletion abolishes rotation and "
  "simultaneously delays G1 progression and impairs cytokinesis, and alpha-parvin, a component of the "
  "integrin-linked kinase complex, is likewise required. Quantitatively, rotation is a graded and often "
  "incomplete process rather than a switch: measured as the elevation angle between neighbouring clonal nuclei, "
  "only about a third to two fifths of postnatal divisions complete it and fewer than one in ten reach 80-90 "
  "degrees. Because incomplete rotations accumulate within a clone, the cumulative fraction determines whether "
  "the clone remains a column or expands laterally into a cluster."),
 quantitative=[
  Q("elevation angle defining a completed rotation","60-90","degrees","operational threshold validated against orthogonal viewing angles in 3D clonal imaging","mouse","rubin2024","threshold set by the authors from two orthogonal views"),
  Q("proportion of divisions completing rotation, postnatal columns","36.4-39.5","% of divisions","P40 mouse proximal tibia and distal femur","mouse","rubin2024","n = 512 and 737 columns"),
  Q("proportion of divisions completing rotation, embryonic clones","17.6-19.4","% of doublets","E18.5 mouse distal femur and proximal tibia","mouse","rubin2024","n = 1044 and 805 doublets"),
  Q("Pearson correlation between nuclear and whole-cell elevation angle","0.79","Pearson r","validation that nuclei can be used as a proxy for cells","mouse","rubin2024","n = 1278 clones"),
 ],
 localization=["mouse PZ: live-imaged and quantified in 3D (romereim2014, rubin2024)",
               "human PZ: not observed"],
 human_evidence="absent",
 human_evidence_note="Rotation has never been observed in human growth plate tissue; it requires live imaging of explants and all published observations are murine.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="Entirely mouse live-imaging and genetics; no human system exists in which the manoeuvre could currently be observed.",
 confidence="C",
 key_refs=[
  R("romereim2014",24764078,"Romereim SM",2014,"primary","Live imaging shows post-mitotic rotation on a dynamic adhesion surface, not intercalation."),
  R("aszodi2003",14522949,"Aszodi A",2003,"primary","Beta1 integrin deletion abolishes rotation and delays G1 progression and cytokinesis."),
  R("rubin2024",39269144,"Rubin S",2024,"primary","Quantifies rotation completeness by elevation angle and shows most divisions do not complete it."),
  R("greer2024",38294852,"Greer SE",2024,"primary","N-cadherin and beta1 integrin coordinately regulate column architecture."),
 ],
 open_questions=["g_l1arch_004"],
))

n.append(dict(
 id="clonal_column", name="Clonal chondrocyte column",
 aliases=["chondrocyte column","cell column","clone"],
 type="tissue_structure",
 summary=(
  "The clonal column is the functional unit of the growth plate: a vertical stack of chondrocytes all descended "
  "from one progenitor, in which the life history of a single cell is displayed in space. Postnatally, after "
  "the secondary ossification centre forms, columns become monoclonal and originate from PTHrP-expressing "
  "resting-zone cells; embryonic columns are multiclonal. Column length in the proliferative zone is a "
  "measurable and species-distinctive quantity: 24 cells per column in the human distal femur. Because a "
  "steady-state column loses one cell at its base for every cell added at its top, column length together with "
  "the loss rate fixes the transit time; in the rat proximal tibia a column loses 8 cells per day. Computer "
  "simulation of stem-cell plus amplification-division parameters reproduces rabbit column structure, showing "
  "that observed column architecture is compatible with a simple hierarchical proliferation model. 3D imaging "
  "has complicated the classical picture by showing that postnatal columns are composites of ordered and "
  "disordered stacks and that they coexist with peripheral clusters, so 'column' names a statistical tendency "
  "rather than a crystalline structure."),
 quantitative=[
  Q("cells per column, proliferative zone","24","cells","human distal femur","human","kember1976","single-study value"),
  Q("cells lost per column per day","8","cells/day","rat proximal tibia in steady-state growth","rat","hunziker1987","one cell every 3 h"),
  Q("clonality of postnatal columns","monoclonal","qualitative","mouse, after secondary ossification centre formation, PTHrP+ resting zone origin","mouse","mizuhashi2018","lineage tracing"),
  Q("number of columns analysed in 3D at P40","737 (distal femur), 512 (proximal tibia)","columns","mouse, 3D Confetti clonal analysis","mouse","rubin2024","sample sizes as reported"),
 ],
 localization=["human PZ: column length counted (kember1976)",
               "mouse: clonality and 3D structure (mizuhashi2018, rubin2024)",
               "rabbit: simulated and observed column structure (mosssalentijn1991)"],
 human_evidence="direct",
 human_evidence_note="Human proliferative column length has been counted directly on histological sections of distal femur (kember1976).",
 species_basis=["human","mouse","rat","rabbit"],
 translation_risk="moderate",
 translation_risk_reason="Column length is measured in humans, but clonality, origin and 3D order are established only in mouse.",
 confidence="B",
 key_refs=[
  R("kember1976",1018028,"Kember NF",1976,"primary","24 cells per proliferative column in the human distal femur."),
  R("mizuhashi2018",30401834,"Mizuhashi K",2018,"primary","Postnatal columns are monoclonal and derive from PTHrP+ resting zone cells after secondary ossification centre formation."),
  R("rubin2024",39269144,"Rubin S",2024,"primary","Postnatal columns are composites of ordered and disordered stacks coexisting with peripheral clusters."),
  R("mosssalentijn1991",2050577,"Moss-Salentijn L",1991,"primary","Simulation of stem-cell and amplification-division parameters reproduces rabbit growth plate column structure."),
  R("hunziker1987",3543020,"Hunziker EB",1987,"primary","A steady-state rat column loses 8 chondrocytes per day at its base."),
 ],
 open_questions=["g_l1arch_004"],
))

n.append(dict(
 id="column_density", name="Column density and cartilage septal number",
 aliases=["columns per unit area","septal number"],
 type="phenotype",
 summary=(
  "Column density - the number of chondrocyte columns per unit cross-sectional area of the plate, measured "
  "histologically as cartilage septal number - determines how many parallel elongation units the plate runs. It "
  "changes systematically with age in humans and it does so differently by zone: in human rib, cartilage septal "
  "number falls with age in the proliferative zone but shows no significant change in the hypertrophic zone, "
  "while septal thickness rises in both. That dissociation means the plate becomes coarser (fewer, thicker "
  "units) at the proliferative level while preserving the number of units actually delivering cartilage to the "
  "metaphysis. Because total plate width, not zone height, is the growth plate parameter that correlates most "
  "strongly with tibial length and growth rate in both mouse and human, the total number of columns a plate can "
  "run is plausibly the dominant scaling variable; but no study has counted columns per unit area in a human "
  "plate and related it to a measured growth rate. Column number is also the quantity that recovers or fails to "
  "recover after physeal injury, which is why it matters clinically."),
 quantitative=[
  Q("direction of cartilage septae number change with age, proliferative zone","decreasing","qualitative","human rib growth plate, birth to adolescence","human","byers2000","absolute counts not available from abstract"),
  Q("change in cartilage septae number with age, hypertrophic zone","no significant change","qualitative","human rib growth plate, birth to adolescence","human","byers2000","explicitly contrasted with the proliferative zone"),
  Q("growth plate parameter most strongly correlated with tibial length and growth rate","total growth plate width","qualitative","mouse histomorphometry and human radiographs","multiple","wilson2021","linear correlation reported"),
  Q("new chondrocytes produced per day per plate","16400 (proximal tibia) vs 3700 (proximal radius)","cells/day","28-day-old rat; a 4.4-fold difference in total output between plates of one animal","rat","wilsman1996","not reported"),
 ],
 localization=["human rib: septal number quantified by zone (byers2000)",
               "rat: total daily chondrocyte output per plate (wilsman1996)"],
 human_evidence="direct",
 human_evidence_note="Cartilage septal number, the histological proxy for column density, has been quantified by zone across age in human rib growth plates (byers2000).",
 species_basis=["human","rat","mouse"],
 translation_risk="low",
 translation_risk_reason="The primary evidence is human histomorphometry; the supporting kinetic comparison is rodent and labelled as such.",
 confidence="B",
 key_refs=[
  R("byers2000",11033444,"Byers S",2000,"primary","Cartilage septal number falls with age in the human proliferative zone but not in the hypertrophic zone."),
  R("wilson2021",31997656,"Wilson K",2021,"primary","Total growth plate width correlates most strongly with tibial length and growth rate in mouse and human."),
  R("wilsman1996",8982136,"Wilsman NJ",1996,"primary","Total daily chondrocyte output differs 4.4-fold between the proximal tibia and proximal radius of a single rat."),
 ],
))

n.append(dict(
 id="chondrocyte_proliferation_rate", name="Chondrocyte proliferation rate",
 aliases=["chondrocyte production rate","cell production per column"],
 type="process",
 summary=(
  "Chondrocyte production rate is the number of new cells a plate generates per unit time, and in steady state "
  "it equals the number removed at the chondro-osseous junction. It is measured in vivo by pulse or repeated "
  "pulse labelling with bromodeoxyuridine combined with unbiased stereology. In 28-day-old rats the whole-plate "
  "output differs 4.4-fold between plates of the same animal: about 16,400 new chondrocytes per day in the "
  "proximal tibia against about 3,700 in the proximal radius. Per column the rat proximal tibia produces and "
  "loses 8 cells per day. Crucially, production rate is not the main lever on elongation: in the same rat "
  "proximal tibia cell division accounts for only 9% of elongation directly, and Hunziker and Schenk found that "
  "the physiological acceleration of growth between 21 and 35 days is achieved without any increase in "
  "longitudinal proliferation rate at all. Proliferation does become limiting in the other direction: growth "
  "deceleration toward maturity involves simultaneous falls in cell height, cell volume and proliferation rate. "
  "Human production rates have never been measured; the only human proliferation datum is an in vitro labelling "
  "index that failed to label any cells in half the specimens."),
 quantitative=[
  Q("new chondrocytes produced per day, whole plate","16400","cells/day","proximal tibia, 28-day-old Long-Evans rat","rat","wilsman1996","not reported"),
  Q("new chondrocytes produced per day, whole plate","3700","cells/day","proximal radius, 28-day-old Long-Evans rat","rat","wilsman1996","not reported"),
  Q("chondrocytes produced and lost per column per day","8","cells/day","rat proximal tibia, steady state","rat","hunziker1987","one every 3 h"),
  Q("change in longitudinal proliferation rate during physiological growth acceleration","unchanged","qualitative","rat proximal tibia, 21 to 35 days","rat","hunziker1989","explicitly reported as unchanged while cell height increased"),
  Q("direct contribution of proliferation to elongation","9","% of elongation","proximal tibia, 28-day-old rat","rat","wilsman1996","not reported"),
 ],
 localization=["rat: measured in vivo (wilsman1996, farnum1993)",
               "human: not measured (thurston1985 in vitro only)"],
 human_evidence="absent",
 human_evidence_note="No in vivo human proliferation rate exists; the single human attempt used in vitro tritiated thymidine and produced no labelled cells in two of four subjects (thurston1985).",
 species_basis=["rat","porcine","human"],
 translation_risk="high",
 translation_risk_reason="All rate data are rodent and obtained with labelling methods that cannot be applied to healthy children.",
 confidence="C",
 key_refs=[
  R("wilsman1996",8982136,"Wilsman NJ",1996,"primary","Daily chondrocyte production of 16,400 (proximal tibia) versus 3,700 (proximal radius) in one 28-day-old rat, matching the loss rate at the junction."),
  R("hunziker1989",2607442,"Hunziker EB",1989,"primary","Growth acceleration occurs without any increase in longitudinal proliferation rate."),
  R("farnum1993",8443686,"Farnum CE",1993,"primary","Established BrdU pulse and repeated-pulse labelling for growth plate proliferative kinetics."),
  R("farnum2003",12508079,"Farnum CE",2003,"primary","Catch-up growth after fasting in rats is achieved by increases in chondrocyte production and hypertrophic volume."),
 ],
 open_questions=["g_l1arch_012","g_l1arch_001"],
))

n.append(dict(
 id="chondrocyte_hypertrophy", name="Chondrocyte hypertrophy",
 aliases=["terminal differentiation","hypertrophic differentiation"],
 type="process",
 summary=(
  "Chondrocyte hypertrophy is the post-mitotic programme in which a flattened proliferative chondrocyte becomes "
  "a large, axially elongated cell, and it is the single largest contributor to longitudinal growth. Mechanically "
  "the enlargement is anisotropic: the cell increases its height in the growth direction far more than its "
  "lateral diameter, because the surrounding longitudinal matrix channels constrain it. Hunziker and Schenk "
  "showed in rat that this shape modulation, not volume as such, is what changes when growth accelerates - "
  "between 21 and 35 days the final cell height rises and lateral diameter falls while final cell volume is "
  "slightly reduced. The volume increase itself has three biophysically distinct phases, of which the middle "
  "one is fluid uptake that dilutes dry mass by about 60%, so a large hypertrophic chondrocyte is a diluted "
  "cell, not simply a bigger one. The whole programme is time-boxed: about two days in rat regardless of growth "
  "rate, and roughly 24 h in mouse. Hypertrophic cells are metabolically active throughout, with 2-5 fold "
  "expansion of secretory organelles, and remain alive to the chondro-osseous junction."),
 quantitative=[
  Q("change in final cell height during growth acceleration","increased","qualitative","rat proximal tibia, 21 to 35 days; lateral diameter decreased, final volume slightly reduced","rat","hunziker1989","direction reported; magnitudes not in abstract"),
  Q("duration of the hypertrophic phase","2","days","rat proximal tibia, constant across 21, 35 and 80 days","rat","hunziker1989","approximate"),
  Q("fraction of elongation contributed by hypertrophy","59","% of elongation","proximal tibia, 28-day-old rat","rat","wilsman1996","falls to 44% in the slow proximal radius"),
  Q("dry mass dilution during the swelling phase","60","% reduction in density","mouse hypertrophic chondrocytes, tomographic phase microscopy","mouse","cooper2013","approximate"),
  Q("expansion of rough endoplasmic reticulum, Golgi and mitochondria","2-5","fold","rat proximal tibia, proliferative to late hypertrophic","rat","hunziker1987","range across compartments"),
 ],
 localization=["rat HZ: shape and organelle stereology (hunziker1987, hunziker1989)",
               "mouse HZ: volume and dry mass trajectory (cooper2013)",
               "human HZ: cell heights only (thurston1985)"],
 human_evidence="indirect",
 human_evidence_note="Human hypertrophic cell heights have been reported (thurston1985, abstract only); the mechanics of enlargement have not been studied in human tissue.",
 species_basis=["rat","mouse","porcine"],
 translation_risk="high",
 translation_risk_reason="The three-phase mechanism, the volume set points and the time-boxing are all rodent; no human measurement exists to anchor them.",
 confidence="C",
 key_refs=[
  R("hunziker1989",2607442,"Hunziker EB",1989,"primary","Growth acceleration is achieved by cell-shape modulation - greater final height, smaller lateral diameter - not by increased volume or proliferation."),
  R("cooper2013",23485973,"Cooper KL",2013,"primary","Enlargement occurs in three phases, the middle one diluting dry mass by ~60%."),
  R("hunziker1987",3543020,"Hunziker EB",1987,"primary","Hypertrophic cells expand secretory organelles 2-5 fold, indicating high biosynthetic activity."),
  R("wilsman1996",8982136,"Wilsman NJ",1996,"primary","Hypertrophy contributes 59% of elongation in the fast rat proximal tibia and 44% in the slow proximal radius."),
 ],
 open_questions=["g_l1arch_008","g_l1arch_009"],
))

n.append(dict(
 id="growth_plate_height", name="Growth plate height",
 aliases=["physeal thickness","plate height"],
 type="phenotype",
 summary=(
  "Growth plate height is the axial thickness of the cartilage disc and is the most commonly measured "
  "architectural variable, but it is a poor stand-alone proxy for growth rate. Hunziker and Schenk warned "
  "explicitly that bulk measures including growth plate height bear little relationship to linear growth rate "
  "and are useful only as indicators of total plate activity. Direct morphometry supports the caution: in mouse "
  "proximal tibia total plate height, resting zone height and combined proliferative-plus-prehypertrophic height "
  "correlate linearly with tibial length and growth rate, but hypertrophic zone height and plate area do not, "
  "and in both mouse and human it is total plate width that correlates most strongly. In humans, plate height "
  "falls with age: proliferative and hypertrophic zone heights and primary spongiosa height all decrease from "
  "birth to adolescence in rib, most steeply in the first postnatal year. Regional heterogeneity within one "
  "plate is substantial - histomorphometry of a human distal tibia undergoing physiological epiphysiodesis "
  "showed physeal height varying by region alongside focal bony bar formation, so a single height value for a "
  "human plate is an average over a structurally non-uniform sheet."),
 quantitative=[
  Q("plate variables correlating linearly with tibial length and growth rate","total height, resting zone height, combined proliferative+prehypertrophic height, plate width, proliferation activity","qualitative list","mouse proximal tibia, neonate to young adult","mouse","wilson2021","hypertrophic zone height and growth plate area did not correlate"),
  Q("direction of zone height change with age","decreasing","qualitative","human rib proliferative and hypertrophic zones, birth to adolescence","human","byers2000","greatest change in the first postnatal year"),
  Q("utility of growth plate height as an estimator of linear growth rate","limited","qualitative","rat proximal tibia across 21, 35 and 80 days","rat","hunziker1989","authors state bulk parameters bear little relationship to linear growth rate"),
  Q("regional variation of physeal height within one human plate","present","qualitative","single adolescent human distal tibia sampled anterior/central/posterior and medial/middle/lateral during physiological epiphysiodesis","human","white2008","n = 1 specimen"),
 ],
 localization=["human distal tibia: regional heights mapped (white2008)",
               "human rib: zone heights across age (byers2000)",
               "mouse proximal tibia: heights vs growth rate (wilson2021)"],
 human_evidence="direct",
 human_evidence_note="Human physeal heights have been measured histomorphometrically in rib across age (byers2000) and regionally in a distal tibia at the onset of closure (white2008), and radiographically in tibia (wilson2021).",
 species_basis=["human","mouse","rat"],
 translation_risk="low",
 translation_risk_reason="Human measurements exist directly; the main caution is that the human data are from few specimens and from rib and distal tibia rather than the fast knee plates.",
 confidence="B",
 key_refs=[
  R("wilson2021",31997656,"Wilson K",2021,"primary","Total height, resting zone height and plate width correlate with tibial growth rate in mouse; hypertrophic zone height and plate area do not."),
  R("byers2000",11033444,"Byers S",2000,"primary","Human rib proliferative and hypertrophic zone heights fall with age, most steeply in the first year."),
  R("hunziker1989",2607442,"Hunziker EB",1989,"primary","Bulk parameters including growth plate height are of limited value as estimators of linear growth rate."),
  R("white2008",19308560,"White JR",2008,"primary","Stereological mapping of regional physeal height in a human distal tibia during physiological epiphysiodesis."),
 ],
))

for x in n: print(write(x))
