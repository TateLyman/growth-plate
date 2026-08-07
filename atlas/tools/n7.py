import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad")
from nodes_lib import *
n=[]

n.append(dict(
 id="distal_femur_plate", name="Distal femoral growth plate",
 aliases=["distal femoral physis"],
 type="tissue_structure",
 summary=(
  "The distal femoral physis is the fastest human growth plate and the single largest contributor to standing "
  "height among individual plates. It supplies about 70% of femoral length overall, and its share rises with "
  "age: from 60% at age 7 to 90% at age 14 in girls, and from 55% at 7 to 90% at 16 in boys. In absolute terms "
  "it adds about 1.3 cm per year from age 7 until the final two years of growth, when the rate halves. "
  "Independent data from the Harpenden Growth Study give a mean distal femoral growth rate of 1.4 cm per year "
  "between ages 5 and 8, which is roughly 38 um per day - an order of magnitude slower than the rat proximal "
  "tibia. Its histology is the source of the only human column-length measurement: 24 cells per proliferative "
  "column, from which a mean proliferative cycle time of about 20 days was derived. Because of its speed and "
  "its accessibility it is also the plate on which most human epiphysiodesis and guided-growth surgery is "
  "performed, and the site of the intercondylar transphyseal complexes through which metaphyseal osteosarcoma "
  "reaches the epiphysis."),
 quantitative=[
  Q("share of femoral longitudinal growth","70","% of femoral length","human, overall across ages 7 to skeletal maturity","human","pritchett1992","n = 244 children (123 boys, 121 girls)"),
  Q("share of femoral growth, girls","60 (age 7) to 90 (age 14)","% of femoral length","human girls","human","pritchett1992","n = 121 girls"),
  Q("share of femoral growth, boys","55 (age 7) to 90 (age 16)","% of femoral length","human boys","human","pritchett1992","n = 123 boys"),
  Q("absolute contribution to femoral growth","1.3","cm/year","human, age 7 to skeletal maturity; halves in the final two years","human","pritchett1992","n = 244"),
  Q("mean growth rate","1.4","cm/year","human, ages 5-8 years, serial radiographs (Harpenden Growth Study)","human","kember1976","mean; dispersion not reported"),
  Q("mean growth rate expressed per day","38","um/day","human, ages 5-8; arithmetic conversion of 1.4 cm/year","human","kember1976","derived"),
  Q("cells per proliferative column","24","cells","human distal femur histology","human","kember1976","single-study value"),
  Q("derived mean proliferative cell cycle time","20","days","human distal femur; derived from column count and growth rate","human","kember1976","derived quantity, not measured"),
 ],
 localization=["human distal femur: growth rate, column length and transphyseal anatomy all measured in human tissue"],
 human_evidence="direct",
 human_evidence_note="All key parameters for this plate - growth rate, share of segment growth, column cell count and transphyseal anatomy - come from human specimens and human radiographic cohorts.",
 species_basis=["human","mouse"],
 translation_risk="not_applicable",
 translation_risk_reason="This node is defined by human anatomy and human measurements.",
 confidence="A",
 key_refs=[
  R("pritchett1992",1735225,"Pritchett JW",1992,"primary","Distal femur supplies ~70% of femoral growth and ~1.3 cm/yr from age 7, with age- and sex-dependent shifts from 55-60% to 90%."),
  R("kember1976",1018028,"Kember NF",1976,"primary","Distal femoral growth of 1.4 cm/yr at ages 5-8 with 24 cells per proliferative column and a derived 20-day cycle time."),
  R("shao2022",35199961,"Shao XH",2022,"primary","Intercondylar transphyseal complexes cross the human distal femoral physis and permit transphyseal tumour extension."),
  R("rubin2024",39269144,"Rubin S",2024,"primary","3D clonal architecture of the mouse distal femoral plate, including expansion-to-elongation ratios."),
 ],
 open_questions=["g_l1arch_001","g_l1arch_009"],
))

n.append(dict(
 id="proximal_tibia_plate", name="Proximal tibial growth plate",
 aliases=["proximal tibial physis"],
 type="tissue_structure",
 summary=(
  "The proximal tibial physis is the second fastest human plate and the workhorse of experimental growth "
  "biology, because in rodents it is the fastest plate and is easy to access. In humans it supplies about 57% "
  "of tibial length overall, rising from 50% at age 7 to 80% at 14 in girls and to 80% at 16 in boys. In the rat "
  "it is the reference plate for essentially every quantitative statement in this layer: elongating at the top "
  "of the 50-400 um/24 h range, with a proliferative cycle time of 30.9 h, an elongation partition of 9% "
  "division / 32% matrix / 59% hypertrophy, production of about 16,400 new chondrocytes per day, and loss of "
  "one cell per column every 3 h. In the mouse it is where the three-phase hypertrophic enlargement trajectory "
  "was defined, reaching a final chondrocyte volume of about 14,000 fl. The gap between this richly "
  "characterised rodent plate and the human plate of the same name is the central translational problem of the "
  "layer: the human proximal tibia has none of these parameters measured."),
 quantitative=[
  Q("share of tibial longitudinal growth","57","% of tibial length","human, overall across ages 7 to skeletal maturity","human","pritchett1992","n = 244 children; range 50-80% by age and sex"),
  Q("proliferative zone cell cycle time","30.9","h","28-day-old rat","rat","wilsman1996a","fastest of the four plates studied"),
  Q("elongation partition","9 / 32 / 59","% division / matrix / hypertrophy","28-day-old rat","rat","wilsman1996","not reported"),
  Q("new chondrocytes produced per day","16400","cells/day","28-day-old rat","rat","wilsman1996","not reported"),
  Q("chondrocyte loss rate per column","8","cells/day","rat, steady-state growth","rat","hunziker1987","one every 3 h"),
  Q("final hypertrophic chondrocyte volume","14000","fl","postnatal mouse","mouse","cooper2013","approximate"),
  Q("duration of the hypertrophic phase","2","days","rat, constant across 21, 35 and 80 days","rat","hunziker1989","approximate"),
 ],
 localization=["human proximal tibia: share of tibial growth measured (pritchett1992)",
               "rat proximal tibia: reference plate for kinetics (wilsman1996, hunziker1987)",
               "mouse proximal tibia: reference plate for hypertrophic volume (cooper2013)"],
 human_evidence="direct",
 human_evidence_note="The human proximal tibial contribution to tibial length is measured radiographically in 244 children (pritchett1992); all cellular parameters attributed to this plate are rodent.",
 species_basis=["human","rat","mouse","ovine"],
 translation_risk="high",
 translation_risk_reason="Almost everything quantitative known about the proximal tibial plate is rat or mouse; the human plate of the same name has only a share-of-segment-growth figure.",
 confidence="B",
 key_refs=[
  R("pritchett1992",1735225,"Pritchett JW",1992,"primary","Proximal tibia supplies ~57% of tibial growth in 244 children, rising from 50% at age 7 to 80% at maturity."),
  R("wilsman1996",8982136,"Wilsman NJ",1996,"primary","Rat proximal tibial elongation partition of 9/32/59 and daily production of 16,400 chondrocytes."),
  R("wilsman1996a",8764865,"Wilsman NJ",1996,"primary","Rat proximal tibial proliferative cycle time of 30.9 h, the fastest of four plates."),
  R("cooper2013",23485973,"Cooper KL",2013,"primary","Mouse proximal tibial chondrocytes reach ~14,000 fl through all three phases of enlargement."),
  R("noonan2004",15502578,"Noonan KJ",2004,"primary","Lamb proximal tibial elongation measured continuously by implanted microtransducer."),
 ],
 open_questions=["g_l1arch_001","g_l1arch_009"],
))

n.append(dict(
 id="proximal_humerus_plate", name="Proximal humeral growth plate",
 aliases=["proximal humeral physis"],
 type="tissue_structure",
 summary=(
  "The proximal humeral physis is the dominant plate of the upper limb, supplying about 80% of humeral length "
  "overall. Its dominance increases through childhood: less than 75% before age 2, about 85% at age 8, and a "
  "constant 90% after age 11. The humerus as a whole grows about 1.2 cm per year in girls and 1.3 cm per year "
  "in boys from age 7 to skeletal maturity, so the proximal plate is contributing roughly 1.0-1.2 cm per year "
  "at its peak share. The humerus stays a nearly constant fraction of standing height across this period - 18% "
  "at age 7 rising to 19-20% at maturity - which means upper limb growth is proportionally coupled to stature "
  "rather than running an independent programme. Clinically the proximal humeral dominance is why proximal "
  "humeral fractures in children remodel so extensively and why distal humeral physeal injuries cause "
  "disproportionately little shortening. No histological or kinetic data exist for this human plate."),
 quantitative=[
  Q("share of humeral longitudinal growth","80","% of humeral length","human, overall","human","pritchett1991","n = 200 subjects"),
  Q("share of humeral growth before age 2","less than 75","% of humeral length","human","human","pritchett1991","n = 200"),
  Q("share of humeral growth at age 8","85","% of humeral length","human","human","pritchett1991","n = 200"),
  Q("share of humeral growth after age 11","90","% of humeral length","human; constant thereafter","human","pritchett1991","n = 200"),
  Q("humeral growth rate, girls","1.2","cm/year","human, age 7 to skeletal maturity","human","pritchett1988","n = 121 girls"),
  Q("humeral growth rate, boys","1.3","cm/year","human, age 7 to skeletal maturity","human","pritchett1988","n = 123 boys"),
  Q("humerus as a fraction of standing height","18 (age 7) to 19-20 (maturity)","% of standing height","human, girls and boys","human","pritchett1988","n = 244"),
 ],
 localization=["human proximal humerus: radiographic growth data only; no histology"],
 human_evidence="direct",
 human_evidence_note="Contribution and growth rate come from two human radiographic cohorts (n = 200 and n = 244) followed to skeletal maturity.",
 species_basis=["human","mouse"],
 translation_risk="not_applicable",
 translation_risk_reason="The node's evidence is human radiographic measurement.",
 confidence="A",
 key_refs=[
  R("pritchett1991",2060215,"Pritchett JW",1991,"primary","Proximal humerus supplies ~80% of humeral growth, rising from <75% before age 2 to 90% after age 11."),
  R("pritchett1988",3356718,"Pritchett JW",1988,"primary","Humerus grows ~1.2 cm/yr in girls and ~1.3 cm/yr in boys from age 7 to maturity and stays a near-constant 18-20% of standing height."),
  R("rubin2024",39269144,"Rubin S",2024,"primary","Included the proximal humeral plate in the mouse micro-CT analysis of elongation versus expansion."),
 ],
 open_questions=["g_l1arch_010"],
))

n.append(dict(
 id="distal_radius_plate", name="Distal radial growth plate",
 aliases=["distal radial physis"],
 type="tissue_structure",
 summary=(
  "The distal radial physis supplies about 80% of radial length overall, rising to 85% by age 5 and 90% by age "
  "8; the neighbouring distal ulnar physis is even more dominant at about 85% overall, 90% by age 5 and 95% "
  "after age 8. In absolute terms the radius grows about 0.9 cm per year in girls and 1.0 cm per year in boys "
  "from age 7 to skeletal maturity, and the ulna about 1.0 and 1.1 cm per year respectively. This distal "
  "dominance is the anatomical reason distal radial physeal arrest after fracture or pinning produces "
  "clinically significant deformity while proximal radial injury rarely does. In the rat the distal radius is "
  "one of the four plates in the canonical differential-growth series, with a proliferative cycle time of 34.0 "
  "h - not significantly different from the fast proximal tibia - which shows that cycle time and elongation "
  "rate are not in one-to-one correspondence across plates."),
 quantitative=[
  Q("share of radial longitudinal growth","80","% of radial length","human, overall; 85% at age 5 and 90% by age 8","human","pritchett1991","n = 200 subjects"),
  Q("share of ulnar longitudinal growth, distal ulnar physis","85","% of ulnar length","human, overall; 90% by age 5 and 95% after age 8","human","pritchett1991","n = 200"),
  Q("radial growth rate, girls","0.9","cm/year","human, age 7 to skeletal maturity","human","pritchett1988","n = 121 girls"),
  Q("radial growth rate, boys","1.0","cm/year","human, age 7 to skeletal maturity","human","pritchett1988","n = 123 boys"),
  Q("ulnar growth rate, girls and boys","1.0 and 1.1","cm/year","human, age 7 to skeletal maturity","human","pritchett1988","n = 244"),
  Q("radius as a fraction of standing height","13-14 (girls), 14-15 (boys)","% of standing height","human, age 7 to skeletal maturity","human","pritchett1988","n = 244"),
  Q("proliferative zone cell cycle time","34.0","h","28-day-old rat distal radius; not significantly different from proximal tibia despite a much lower elongation rate","rat","wilsman1996a","p > 0.05 versus proximal tibia"),
 ],
 localization=["human distal radius and ulna: radiographic growth data (pritchett1991, pritchett1988)",
               "rat distal radius: cell cycle and kinetic parameters (wilsman1996a, wilsman1996)"],
 human_evidence="direct",
 human_evidence_note="Human contributions and growth rates come from radiographic cohorts of 200 and 244 children followed to maturity.",
 species_basis=["human","rat"],
 translation_risk="low",
 translation_risk_reason="The human growth data are direct; only the cell-kinetic comparison is rodent and is labelled as such.",
 confidence="A",
 key_refs=[
  R("pritchett1991",2060215,"Pritchett JW",1991,"primary","Distal radius supplies ~80% and distal ulna ~85% of their segment's growth, with distal dominance increasing through childhood."),
  R("pritchett1988",3356718,"Pritchett JW",1988,"primary","Radius grows ~0.9-1.0 cm/yr and ulna ~1.0-1.1 cm/yr from age 7 to maturity."),
  R("wilsman1996a",8764865,"Wilsman NJ",1996,"primary","Rat distal radial proliferative cycle time of 34.0 h, not significantly different from the much faster proximal tibia."),
  R("wilsman1996",8982136,"Wilsman NJ",1996,"primary","Distal radius is one of the four plates in the rat differential-growth kinetic series."),
 ],
 open_questions=["g_l1arch_010"],
))

n.append(dict(
 id="metacarpal_plate", name="Metacarpal and metatarsal growth plate",
 aliases=["metacarpal physis","metatarsal physis","pseudoepiphysis"],
 type="tissue_structure",
 summary=(
  "Metacarpals and metatarsals are architecturally unusual: unlike other long bones they carry a functional "
  "growth plate at one end only, with the opposite end forming a pseudoepiphysis or none at all. The PTHrP/Ihh "
  "feedback loop has been shown to explain this asymmetric architecture, and the same logic applies to the "
  "pisiform. This makes these bones a natural experiment for the question of what determines where a growth "
  "plate forms and how many a bone gets. Metatarsals are also the element in which the mechanism of "
  "evolutionary limb elongation has been localised most precisely: in the jerboa, whose metatarsals are about "
  "2.5 times longer in relative proportion than the mouse's, hypertrophic chondrocytes reach about 23,000 fl "
  "against about 8000 fl in mouse, and individual hypertrophic cell height is 58% greater, achieved by "
  "extending the IGF-dependent third phase of enlargement that the mouse metatarsal truncates. Human metacarpal "
  "physeal growth rates have not been reported in the sources reviewed here; metacarpophalangeal pattern "
  "profiles are used clinically to characterise short stature but describe final proportions, not growth plate "
  "kinetics."),
 quantitative=[
  Q("number of functional growth plates per metatarsal or metacarpal","1","growth plate per bone","mammals; opposite end forms a pseudoepiphysis or none","mouse","reno2025","architectural feature explained by the PTHrP/Ihh loop"),
  Q("final hypertrophic chondrocyte volume, distal metatarsal","8000","fl","mouse; phases 1 and 2 complete, phase 3 truncated","mouse","cooper2013","approximate"),
  Q("final hypertrophic chondrocyte volume, distal metatarsal","23000","fl","jerboa; phase 3 extended; ~40-fold increase from initial volume","multiple","cooper2013","approximate; jerboa not in the controlled species vocabulary"),
  Q("hypertrophic cell height, jerboa versus mouse metatarsal","58","% greater","homologous distal metatarsal plates","multiple","cooper2013","not reported"),
  Q("relative metatarsal proportion, jerboa versus mouse","2.5","fold","hindlimb metatarsals","multiple","cooper2013","as stated"),
 ],
 localization=["mouse and jerboa metatarsal: volume trajectories measured (cooper2013)",
               "mouse metatarsal and pisiform: single-plate architecture explained (reno2025)",
               "human metacarpal: growth plate kinetics not reported"],
 human_evidence="absent",
 human_evidence_note="No human metacarpal or metatarsal physeal growth rate or histomorphometric measurement was found in this sweep; human hand data are limited to metacarpophalangeal pattern profiles of final bone proportions.",
 species_basis=["mouse","multiple"],
 translation_risk="high",
 translation_risk_reason="All quantitative data are rodent and jerboa, and the jerboa comparison is an evolutionary rather than a physiological model.",
 confidence="C",
 key_refs=[
  R("reno2025",40088130,"Reno PL",2025,"primary","The PTHrP/Ihh feedback loop explains why mammalian metatarsals and the pisiform carry a growth plate at one end only."),
  R("cooper2013",23485973,"Cooper KL",2013,"primary","Jerboa metatarsal hypertrophic chondrocytes reach ~23,000 fl by extending the third phase of enlargement, versus ~8000 fl in mouse."),
 ],
 open_questions=["g_l1arch_010","g_l1arch_009"],
))

n.append(dict(
 id="vertebral_growth_plate", name="Vertebral growth plate",
 aliases=["vertebral endplate physis","ring apophysis","vertebral body growth plate"],
 type="tissue_structure",
 summary=(
  "Each vertebral body grows in height from cartilaginous growth plates at its superior and inferior surfaces, "
  "and the human vertebral column carries more than 130 such plates. Collectively they generate the trunk "
  "component of standing height, and their behaviour is not linear with age: three distinct postnatal phases "
  "are recognised, birth to 5 years, 5 to 10 years, and 10 years to skeletal maturity, with acceleration and "
  "deceleration rather than a constant rate. The consequence for pathology is that the same asymmetric load "
  "produces very different deformity depending on when it acts, which is the basis of the relationship between "
  "remaining growth and progression risk in idiopathic scoliosis, and of growth-modulation surgery such as "
  "vertebral body tethering. What is missing is resolution: the field measures segment lengths radiographically "
  "rather than per-plate growth rates, so the contribution of an individual vertebral physis, and how it "
  "compares between superior and inferior endplates or between thoracic and lumbar levels, is unquantified in "
  "humans. No vertebral growth plate histomorphometry comparable to the appendicular literature exists."),
 quantitative=[
  Q("number of growth plates in the human vertebral column","more than 130","growth plates","human spine","human","dimeglio2020","as stated by the author"),
  Q("number of distinct postnatal phases of spinal growth","3","phases","human: birth to 5 y, 5 to 10 y, 10 y to skeletal maturity","human","dimeglio2020","as stated"),
  Q("per-plate vertebral growth rate","not reported","mm/year","human, any level","human","dimeglio2020","null result; only segment-level rates are published"),
 ],
 localization=["human spine: plate count and phase structure described (dimeglio2020)",
               "human vertebral physis: no histomorphometry located in this sweep"],
 human_evidence="direct",
 human_evidence_note="Human spinal growth phases and the number of vertebral growth plates are described from human radiographic series (dimeglio2020), but per-plate rates are not published.",
 species_basis=["human","porcine"],
 translation_risk="low",
 translation_risk_reason="The descriptive human data are human; the risk is not species but resolution, since growth-modulation models are porcine and human data are segment-level.",
 confidence="C",
 key_refs=[
  R("dimeglio2020",32055613,"Dimeglio A",2020,"review","The human vertebral column carries more than 130 growth plates and spinal growth proceeds in three non-linear postnatal phases."),
  R("byers2000",11033444,"Byers S",2000,"primary","Provides the nearest human axial-skeleton growth plate histomorphometry, in rib rather than vertebra."),
 ],
 open_questions=["g_l1arch_011"],
))

for x in n: print(write(x))
