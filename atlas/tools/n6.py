import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad")
from nodes_lib import *
n=[]

n.append(dict(
 id="groove_of_ranvier", name="Groove of Ranvier",
 aliases=["ossification groove of Ranvier","perichondrial ossification groove","GOR"],
 type="tissue_structure",
 summary=(
  "The groove of Ranvier is a circumferential wedge of densely cellular tissue at the periphery of the growth "
  "plate, continuous with the perichondrium, that supplies cells for latitudinal enlargement of the plate. "
  "Shapiro, Holtrop and Glimcher's rabbit study established its cellular organisation and the direction of cell "
  "flow from perichondrium into the plate margin. It is present and morphologically identifiable in developing "
  "human bones, described in calcaneus and talus, and in human polydactylous digits it harbours CD90+/CD105+ "
  "mesenchymal progenitor cells and, unlike the immature sprouting vessels inside the ossification centre, "
  "mature vessels stabilised by alpha-SMA-positive smooth muscle. Its clinical importance is negative: "
  "disorganisation of the groove causes congenital hyperostosis in piglets, and injury to it is implicated in "
  "angular deformity and in osteochondroma formation. What is missing is quantitative: no lineage tracing has "
  "shown groove-derived cells entering columnar clones, and no study has apportioned plate diameter increase "
  "between the groove and interstitial growth in any species, let alone in humans."),
 quantitative=[
  Q("progenitor markers in the human groove of Ranvier","CD90+ / CD105+","marker phenotype","human polydactylous digit growth plates, immunohistochemistry and confocal microscopy","human","walzer2014","descriptive; cell counts not reported"),
  Q("vessel maturity in the human groove of Ranvier","alpha-SMA+ smooth muscle coverage present","qualitative","human polydactylous digits; contrasts with uncovered CD34+ sprouts inside ossification centres","human","walzer2014","descriptive"),
 ],
 localization=["rabbit GOR: cellular organisation established (shapiro1977)",
               "human GOR: present in calcaneus and talus (cheng1995) and in digits with CD90+/CD105+ progenitors (walzer2014)"],
 human_evidence="direct",
 human_evidence_note="The groove of Ranvier has been identified and characterised in human tissue, both morphologically in developing calcaneus and talus (cheng1995) and immunophenotypically in polydactylous digits (walzer2014).",
 species_basis=["rabbit","human","porcine"],
 translation_risk="moderate",
 translation_risk_reason="The structure is confirmed in humans, but its function - supplying cells for latitudinal growth - rests on rabbit morphology and has never been tested by lineage tracing in any species.",
 confidence="C",
 key_refs=[
  R("shapiro1977",71299,"Shapiro F",1977,"primary","Established the cellular organisation of the perichondrial ossification groove of Ranvier in rabbit and its role in latitudinal growth."),
  R("cheng1995",7697157,"Cheng X",1995,"primary","Described the perichondral ossification groove of Ranvier in the developing human calcaneus and talus."),
  R("walzer2014",25164565,"Walzer SM",2014,"primary","The groove of Ranvier in human digits harbours CD90+/CD105+ mesenchymal progenitors and mature alpha-SMA-covered vessels."),
  R("langenskild1998",9531398,"Langenskiöld A",1998,"review","Reviews the role of the groove of Ranvier in normal and pathological bone growth, including deformity after injury."),
 ],
 open_questions=["g_l1arch_013"],
))

n.append(dict(
 id="perichondrial_ring_lacroix", name="Perichondrial ring of LaCroix",
 aliases=["ring of LaCroix","perichondrial ring","bone bark"],
 type="tissue_structure",
 summary=(
  "The perichondrial ring of LaCroix is the thin collar of dense fibrous tissue and bone that encircles the "
  "growth plate at its periphery, continuous with the metaphyseal periosteum below and with the groove of "
  "Ranvier above. Functionally it is the mechanical restraint on the plate: it resists the shear and tensile "
  "forces that would otherwise displace the epiphysis on the metaphysis, which is why it is described together "
  "with the groove as a single peripheral apparatus in Shapiro's rabbit study and why its structural integrity "
  "is what surgical approaches to the physis attempt to preserve. It is the anatomical explanation for the "
  "clinical observation that physeal separation occurs more readily in young children, in whom the ring is "
  "relatively thin. Because it is a mechanical rather than a metabolic structure, there are almost no "
  "quantitative data on it: no measurements of its stiffness, thickness or load share have been reported in "
  "human tissue, and it is described in the human literature only qualitatively alongside the groove."),
 quantitative=[
  Q("published measurements of ring stiffness or load share in human tissue","0","studies","literature to 2026-08-05","human","shapiro1977","null result; the ring is described only qualitatively"),
 ],
 localization=["rabbit: described with the groove of Ranvier as a peripheral apparatus (shapiro1977)",
               "human: described qualitatively in developmental series (cheng1995)"],
 human_evidence="indirect",
 human_evidence_note="Human evidence is descriptive morphology in developmental series and the clinical pattern of physeal separation injuries; no human mechanical measurement exists.",
 species_basis=["rabbit","human"],
 translation_risk="moderate",
 translation_risk_reason="The structure exists in humans and its clinical relevance is established, but its mechanical function is asserted from rabbit morphology and clinical inference rather than measured.",
 confidence="D",
 key_refs=[
  R("shapiro1977",71299,"Shapiro F",1977,"primary","Described the perichondrial ossification groove and its associated ring as a single peripheral apparatus of the growth plate in rabbit."),
  R("cheng1995",7697157,"Cheng X",1995,"primary","Documented perichondral ossification at the plate periphery in developing human calcaneus and talus."),
  R("langenskild1998",9531398,"Langenskiöld A",1998,"review","Reviews peripheral physeal structures and the consequences of their injury."),
 ],
 open_questions=["g_l1arch_013"],
))

n.append(dict(
 id="cartilage_canal", name="Cartilage canal",
 aliases=["epiphyseal cartilage canal","canals of Wegner"],
 type="tissue_structure",
 summary=(
  "Cartilage canals are vascularised connective-tissue channels that invade the epiphyseal cartilage before the "
  "secondary ossification centre appears. They carry arterioles, venules, capillaries and mesenchymal cells into "
  "an otherwise avascular tissue, form a discrete network within the epiphysis, and determine where the "
  "secondary centre will form: in mouse, cartilage canals establish the marrow space that the secondary centre "
  "subsequently occupies, and they influence the fate of the resting chondrocytes they pass. Their mesenchymal "
  "cells express bone-relevant proteins and can become osteocytes, so the canals are not merely a plumbing "
  "system but a delivery route for osteogenic precursors. In human epiphyses, the vessels that build the "
  "ossification centres arise by sprouting from the bone collar or by intussusception rather than from "
  "circulating CD133+ endothelial progenitors, and vascular invasion of the joint anlage is delayed relative to "
  "the surrounding tissue. Canals are also the point of vulnerability in osteochondrosis of large animals, where "
  "failure of canal blood supply causes focal ischaemic chondronecrosis."),
 quantitative=[
  Q("temporal relation of cartilage canals to the secondary ossification centre","canals precede the centre","qualitative","mammalian long bone epiphysis","mouse","blumer2008","descriptive review of primary work"),
  Q("mechanism of new vessel formation in human ossification centres","sprouting from bone collar or intussusception, not endothelial progenitor recruitment","qualitative","human polydactylous digit growth plates, CD34/CD31/CD133/VEGFR-2 immunostaining","human","walzer2014","descriptive"),
 ],
 localization=["mouse femoral epiphysis: canals determine secondary centre site (blumer2007)",
               "human epiphysis: vessel origin characterised (walzer2014)"],
 human_evidence="direct",
 human_evidence_note="The origin and phenotype of epiphyseal vessels have been characterised directly in human polydactylous digit specimens (walzer2014).",
 species_basis=["mouse","human","porcine","ovine"],
 translation_risk="moderate",
 translation_risk_reason="Canal function in determining secondary centre position is mouse work; the human data establish vessel origin but not canal fate.",
 confidence="C",
 key_refs=[
  R("blumer2007",17626280,"Blumer MJ",2007,"primary","Cartilage canals determine the site of the secondary ossification centre and influence the fate of resting chondrocytes in mouse femoral epiphysis."),
  R("blumer2008",18602255,"Blumer MJ",2008,"review","Reviews cartilage canal structure and formation and the transformation of canal mesenchymal cells into osteocytes."),
  R("walzer2014",25164565,"Walzer SM",2014,"primary","Human ossification centre vessels arise by sprouting from the bone collar or intussusception, not from CD133+ progenitors."),
 ],
))

n.append(dict(
 id="transphyseal_canal", name="Transphyseal canal",
 aliases=["transphyseal vessel","physeal bridging channel","intercondylar transphyseal complex"],
 type="tissue_structure",
 summary=(
  "Transphyseal canals are channels that cross the growth plate from metaphysis to epiphysis, breaching what is "
  "otherwise treated as an avascular barrier. In the human distal femur a distinct anatomical entity, the "
  "intercondylar transphyseal complex, has been described and characterised: cartilage and vascular channels "
  "that traverse the physis in the intercondylar region and provide a route by which metaphyseal osteosarcoma "
  "extends into the epiphysis. This matters because the physis has traditionally been taught as a tumour and "
  "infection barrier, and the existence of a constant transphyseal route reframes both oncological staging and "
  "the pathogenesis of transphyseal haematogenous osteomyelitis in children. In young children before the "
  "secondary ossification centre matures, transphyseal vessels are also the route by which the epiphysis "
  "receives blood, which is the anatomical basis for epiphyseal osteonecrosis after septic arthritis or "
  "vascular injury. The human quantitative anatomy - number, diameter and age-dependence of these channels - is "
  "essentially unmapped outside the single distal femoral study."),
 quantitative=[
  Q("anatomical site of the described human transphyseal complex","intercondylar region of the distal femur","anatomical location","human, pathological and radiological study","human","shao2022","descriptive; complex number and dimensions not summarised in the abstract"),
 ],
 localization=["human distal femur: intercondylar transphyseal complexes described (shao2022)",
               "human digit: vessel architecture around the plate characterised (walzer2014)"],
 human_evidence="direct",
 human_evidence_note="Transphyseal complexes have been described and characterised directly in human distal femoral specimens with radiological and clinical correlation (shao2022).",
 species_basis=["human"],
 translation_risk="not_applicable",
 translation_risk_reason="The primary evidence for this node is human anatomical and pathological material.",
 confidence="C",
 key_refs=[
  R("shao2022",35199961,"Shao XH",2022,"primary","Described intercondylar transphyseal complexes in the human distal femur and their role in transphyseal extension of paediatric osteosarcoma."),
  R("walzer2014",25164565,"Walzer SM",2014,"primary","Characterised the vascular architecture around the human growth plate and its ossification centres."),
 ],
))

n.append(dict(
 id="epiphyseal_vasculature", name="Epiphyseal vasculature",
 aliases=["epiphyseal blood supply","secondary ossification centre vasculature"],
 type="tissue_structure",
 summary=(
  "The epiphyseal side of the growth plate is supplied by vessels that reach the secondary ossification centre "
  "through cartilage canals and then via the epiphyseal arterial network. These vessels feed the resting and "
  "upper proliferative zones by diffusion across the epiphyseal face, since the plate itself contains no "
  "vessels. In human epiphyses the new vessels of the ossification centres are immature: they are formed by "
  "CD34-positive endothelial sprouts that do not yet co-express the mature marker CD31 and carry no abluminal "
  "alpha-SMA-positive smooth muscle coverage, in contrast to the mature, smooth-muscle-invested vessels of the "
  "periosteum and the groove of Ranvier in the same specimens. Vessel formation proceeds by sprouting from the "
  "bone collar or by intussusception rather than by recruitment of circulating CD133+ endothelial progenitors, "
  "and vascular invasion of the joint anlage is delayed relative to surrounding joint tissue. Interruption of "
  "this supply is the mechanism of epiphyseal osteonecrosis and, in the horse and pig, of osteochondrosis."),
 quantitative=[
  Q("endothelial phenotype of new ossification-centre vessels","CD34+ / CD31-negative","marker phenotype","human polydactylous digit growth plates","human","walzer2014","descriptive; no vessel counts reported"),
  Q("smooth muscle coverage of ossification-centre vessels","absent (no abluminal alpha-SMA+ cells)","qualitative","human polydactylous digits; present in periosteum and groove of Ranvier in the same specimens","human","walzer2014","descriptive"),
 ],
 localization=["human epiphysis: vessel phenotype characterised (walzer2014)",
               "mouse epiphysis: cartilage canal-dependent vascularisation (blumer2007)"],
 human_evidence="direct",
 human_evidence_note="Human epiphyseal and ossification-centre vessel phenotypes have been characterised directly by immunohistochemistry and confocal microscopy in polydactylous digit specimens (walzer2014).",
 species_basis=["human","mouse"],
 translation_risk="low",
 translation_risk_reason="The core evidence is from human tissue; only the canal-to-centre developmental sequence is murine.",
 confidence="B",
 key_refs=[
  R("walzer2014",25164565,"Walzer SM",2014,"primary","Human ossification centre vessels are immature CD34+/CD31-negative sprouts without smooth muscle coverage, formed by sprouting or intussusception."),
  R("blumer2007",17626280,"Blumer MJ",2007,"primary","Cartilage canals establish the epiphyseal marrow space that the secondary ossification centre occupies."),
  R("blumer2008",18602255,"Blumer MJ",2008,"review","Reviews cartilage canal vascular anatomy in the developing epiphysis."),
 ],
))

n.append(dict(
 id="metaphyseal_vasculature", name="Metaphyseal vasculature",
 aliases=["metaphyseal capillary loops","vascular invasion front"],
 type="tissue_structure",
 summary=(
  "The metaphyseal vasculature terminates in blind capillary loops that abut the last transverse septum of each "
  "chondrocyte column and advance as that septum is removed. Scanning electron microscopy of vascular casts "
  "shows the invading capillary ends are morphologically varied rather than uniform, and serial-section analysis "
  "shows the endothelium penetrates the non-calcified pericellular and territorial matrix specifically, not the "
  "mineralised longitudinal septa. The advancing tips are physically associated with FABP5+ septoclasts, which in "
  "mouse require endothelial Dll4 for their specification, making the vessel the organiser of its own path "
  "through cartilage. In the metaphysis proper the vessels are type H capillaries, a CD31-high/endomucin-high "
  "subtype that is enriched near the growth plate, surrounds osteoprogenitors and declines with age. Because "
  "vascular invasion sets the rate at which the plate is consumed, anything that blocks metaphyseal angiogenesis "
  "thickens the hypertrophic zone without increasing elongation."),
 quantitative=[
  Q("morphology of capillary ends at the invasion front","variable, not uniform","qualitative","rat femur, scanning electron microscopy of vascular casts","rat","yamamoto2022","descriptive"),
  Q("matrix compartment penetrated by invading endothelium","non-calcified pericellular and territorial matrix","qualitative","distal hypertrophic zone, Yucatan swine, serial light-microscopic sections","porcine","farnum1989","descriptive"),
  Q("abundance of septoclasts relative to osteoclasts at the chondro-osseous interface","significantly greater","qualitative","3-week-old mouse femur","mouse","sivaraj2022","n = 6 animals"),
 ],
 localization=["rat metaphysis: capillary cast morphology (yamamoto2022)",
               "mouse metaphysis: type H vessels and septoclast association (kusumbe2014, sivaraj2022)",
               "human metaphysis: RANK+ chondro/osteoclasts quantified by zone (walzer2014)"],
 human_evidence="indirect",
 human_evidence_note="Human metaphyseal vessels and RANK+ resorptive cells have been quantified by zone in polydactylous digit specimens (walzer2014), but the invasion-front cell biology is entirely rodent.",
 species_basis=["rat","mouse","porcine","human"],
 translation_risk="high",
 translation_risk_reason="Type H vessel identity and septoclast coupling are murine constructs; no human study has demonstrated either at the growth plate.",
 confidence="C",
 key_refs=[
  R("kusumbe2014",24646994,"Kusumbe AP",2014,"primary","Type H capillaries are enriched in the metaphysis near the growth plate, couple angiogenesis to osteogenesis and decline with age in mouse."),
  R("sivaraj2022",35091558,"Sivaraj KK",2022,"primary","Septoclasts associate with distal endothelial buds and require endothelial Dll4 for specification."),
  R("farnum1989",2760737,"Farnum CE",1989,"primary","Endothelial penetration at the junction is into non-calcified pericellular and territorial matrix."),
  R("yamamoto2022",35537657,"Yamamoto T",2022,"primary","Scanning electron microscopy of vascular casts shows morphological variety among capillary ends invading the rat epiphyseal plate."),
 ],
 open_questions=["g_l1arch_003"],
))

n.append(dict(
 id="type_h_vessel", name="Type H vessel",
 aliases=["type H capillary","CD31-hi endomucin-hi capillary"],
 type="cell_type",
 summary=(
  "Type H vessels are a capillary subtype in bone defined by high expression of CD31 (Pecam1) and endomucin, "
  "distinguished from the more abundant sinusoidal type L vessels. They are concentrated in the metaphysis "
  "immediately beneath the growth plate and in the endosteum, are surrounded by Runx2+ and osterix+ "
  "osteoprogenitors, and their abundance falls sharply with age in parallel with declining bone formation. "
  "Their functional claim is that they couple angiogenesis to osteogenesis: manipulating endothelial Notch or "
  "HIF signalling changes type H vessel abundance and changes bone mass in the same direction. For growth plate "
  "architecture their relevance is positional - they define the vascular compartment that meets the "
  "chondro-osseous junction and that hosts the septoclasts and osteoprogenitors which convert the cartilage "
  "template into primary spongiosa. The entire type H concept is murine; no human study has demonstrated a "
  "type H compartment at the human growth plate, and the human vessels characterised at the human "
  "chondro-osseous region were phenotyped with a different marker panel."),
 quantitative=[
  Q("anatomical distribution","metaphysis adjacent to the growth plate and endosteum","qualitative","mouse long bone, CD31/endomucin immunostaining","mouse","kusumbe2014","descriptive"),
  Q("change with age","declining abundance","qualitative","mouse, juvenile to aged","mouse","kusumbe2014","direction reported"),
  Q("human studies demonstrating type H vessels at the growth plate","0","studies","literature to 2026-08-05","human","kusumbe2014","null result"),
 ],
 localization=["mouse metaphysis and endosteum: defined (kusumbe2014)",
               "human growth plate: not demonstrated"],
 human_evidence="absent",
 human_evidence_note="No study demonstrates a CD31-high/endomucin-high type H vessel compartment at the human growth plate; human physeal vessels have been phenotyped with CD34/CD31/alpha-SMA panels instead (walzer2014).",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="A marker-defined vascular subtype established entirely in mouse, with an age-related decline that maps onto a species that does not undergo epiphyseal fusion.",
 confidence="C",
 key_refs=[
  R("kusumbe2014",24646994,"Kusumbe AP",2014,"primary","Defined type H capillaries as a CD31-high/endomucin-high subtype enriched near the growth plate that couples angiogenesis to osteogenesis and declines with age."),
  R("walzer2014",25164565,"Walzer SM",2014,"primary","Characterised human growth plate vessels with CD34/CD31/alpha-SMA rather than type H markers, finding immature uncovered sprouts in ossification centres."),
 ],
))

n.append(dict(
 id="oxygen_gradient_growth_plate", name="Oxygen gradient across the growth plate",
 aliases=["physeal hypoxia","growth plate pO2 gradient"],
 type="process",
 summary=(
  "The growth plate is avascular, so oxygen must diffuse in from the epiphyseal and metaphyseal margins, "
  "producing a gradient with the lowest tension in the interior. The gradient was mapped by direct electrode "
  "measurement across the epiphyseal plate, metaphysis and diaphysis in rat and rabbit by Brighton and "
  "Heppenstall; that 1971 study remains the source of nearly every statement about physeal hypoxia and its "
  "numeric values are not recoverable from any indexed abstract. Genetic evidence confirms the interior is "
  "genuinely hypoxic: deleting HIF-1alpha in chondrocytes causes massive death in the centre of the plate while "
  "sparing the margins, and VEGFA is required for chondrocyte survival. A striking adaptation was described in "
  "2023: growth plate chondrocytes assemble cytoplasmic membraneless haemoglobin bodies whose oxygen "
  "dissociation curve is strongly left-shifted, with P50 of 27.6-27.9 mmHg compared with 58.2 mmHg for red cells "
  "from the same mice, allowing them to bind and store oxygen at tensions at which erythrocyte haemoglobin has "
  "already released it. No oxygen tension has ever been measured in a human growth plate, which matters because "
  "human plates are thicker and diffusion distances therefore longer."),
 quantitative=[
  Q("P50 of chondrocyte haemoglobin bodies (Hedy)","27.58-27.85","mmHg","mouse growth plate chondrocytes, oxygen dissociation curve by Clark electrode and dual-wavelength spectrophotometry at 37 C","mouse","zhang2023","two independently reported values, 27.58 and 27.85 mmHg"),
  Q("P50 of red blood cells from the same mice","58.2","mmHg","comparison sample, same conditions","mouse","zhang2023","as reported"),
  Q("oxygen concentration at which Hba or Hbb knockout cartilage shows increased chondrocyte death","1","% O2","E14.5 mouse humeral cartilage growth plates cultured 6 days","mouse","zhang2023","n = 3 biological replicates"),
  Q("measured oxygen tension in human growth plate zones","not measured","mmHg","literature to 2026-08-05; PubMed search returned 4 records, none reporting a human tissue measurement","human","brighton1971","null result; see search log g_l1arch_007"),
 ],
 localization=["rat and rabbit: electrode measurement by zone (brighton1971)",
               "mouse: HIF-1alpha requirement in the plate interior (schipani2001); chondrocyte haemoglobin bodies (zhang2023)",
               "human: never measured"],
 human_evidence="absent",
 human_evidence_note="No measurement of oxygen tension in human growth plate tissue exists; a targeted PubMed search returned four records, none of which measures tissue oxygen in human physis (search log g_l1arch_007).",
 species_basis=["rat","rabbit","mouse"],
 translation_risk="high",
 translation_risk_reason="Absolute oxygen tensions are rodent and unrecoverable in value, and human plates have longer diffusion distances, so the human gradient could differ substantially. Human physeal explants are routinely cultured at 21% oxygen without knowing the in vivo baseline.",
 confidence="C",
 key_refs=[
  R("brighton1971",5580029,"Brighton CT",1971,"primary","Measured oxygen tension by zone across the epiphyseal plate, metaphysis and diaphysis in rat and rabbit; the source of the physeal hypoxia concept."),
  R("schipani2001",11691837,"Schipani E",2001,"primary","HIF-1alpha is essential for survival of chondrocytes in the hypoxic interior of the growth plate in mouse."),
  R("zhang2023",37794190,"Zhang F",2023,"primary","Growth plate chondrocytes form membraneless haemoglobin bodies with P50 left-shifted to 27.6-27.9 mmHg versus 58.2 mmHg for red cells."),
  R("zelzer2004",15073147,"Zelzer E",2004,"primary","VEGFA is necessary for chondrocyte survival during bone development."),
 ],
 open_questions=["g_l1arch_007"],
 pending_source="brighton1971",
))

n.append(dict(
 id="nutrient_diffusion_growth_plate", name="Nutrient diffusion in the growth plate",
 aliases=["solute transport in physeal cartilage","metabolite gradients"],
 type="process",
 summary=(
  "Because the growth plate contains no vessels, every solute a chondrocyte needs must diffuse from the "
  "epiphyseal or metaphyseal margins through a dense, negatively charged proteoglycan matrix, and every waste "
  "product must leave the same way. The consequence is that the interior of the plate is simultaneously the "
  "most hypoxic and the most nutritionally remote compartment, and that plate height is bounded by diffusion. "
  "This is one plausible reason why growth plate height falls as animals mature and why bulk plate height is a "
  "poor predictor of growth rate. The direct evidence for a nutrient gradient is much weaker than for the oxygen "
  "gradient: the only zonal transport measurements in the growth plate literature are the oxygen electrode "
  "profiles of Brighton and Heppenstall, and the strongest indirect evidence is that mouse chondrocytes have "
  "evolved an intracellular oxygen store (haemoglobin bodies) precisely because delivery is marginal. Glucose, "
  "lactate and amino acid gradients across the plate have not been measured in any species, and no human "
  "measurement of any kind exists. Treating this node as established biology would be an error; it is a "
  "well-motivated inference from tissue architecture."),
 quantitative=[
  Q("published measurements of glucose or lactate gradients across the growth plate","0","studies","any species, literature to 2026-08-05","not_applicable","brighton1971","null result; the only zonal transport data are oxygen electrode profiles"),
  Q("evidence of marginal oxygen delivery requiring intracellular storage","haemoglobin bodies with left-shifted P50 (27.6-27.9 mmHg)","mmHg","mouse growth plate chondrocytes","mouse","zhang2023","two reported values"),
 ],
 localization=["rat and rabbit: oxygen profile measured (brighton1971)",
               "human: no transport measurement of any solute"],
 human_evidence="absent",
 human_evidence_note="No study measures solute transport or metabolite gradients in human growth plate cartilage.",
 species_basis=["rat","rabbit","mouse"],
 translation_risk="high",
 translation_risk_reason="Diffusion limits scale with the square of plate thickness, and human plates are thicker than rodent ones, so rodent inferences about how far solutes reach are not transferable.",
 confidence="E",
 key_refs=[
  R("brighton1971",5580029,"Brighton CT",1971,"primary","The only zonal measurement of a diffusible solute (oxygen) across the epiphyseal plate, in rat and rabbit."),
  R("zhang2023",37794190,"Zhang F",2023,"primary","Chondrocyte haemoglobin bodies with left-shifted P50 imply that oxygen delivery to the plate interior is marginal."),
  R("schipani2001",11691837,"Schipani E",2001,"primary","Deletion of HIF-1alpha kills chondrocytes specifically in the plate interior, consistent with a diffusion-limited centre."),
 ],
 open_questions=["g_l1arch_007"],
 pending_source="brighton1971",
))

for x in n: print(write(x))
