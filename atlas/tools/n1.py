import sys; sys.path.insert(0,"/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad")
from nodes_lib import *

n=[]

n.append(dict(
 id="elongation_budget",
 name="Partition of elongation among proliferation, matrix synthesis, and hypertrophy",
 aliases=["elongation budget","chondrocytic kinetic partition","growth partition"],
 type="process",
 summary=(
  "Longitudinal elongation of a growth plate is the sum of three separable contributions: the axial "
  "displacement produced by chondrocyte division, the axial displacement produced by interstitial matrix "
  "synthesis, and the axial displacement produced by the volume and shape change of chondrocytes during "
  "hypertrophy. The only study that has closed this budget quantitatively is Wilsman et al. 1996, which used "
  "oxytetracycline labelling for elongation rate and bromodeoxyuridine plus unbiased stereology for cell "
  "kinetics in four growth plates of 28-day-old Long-Evans rats: in the fast proximal tibia the split is 9% "
  "division, 32% matrix synthesis, 59% hypertrophic enlargement, and in the slow proximal radius the "
  "hypertrophic share falls to 44% while matrix synthesis rises to 49%. In the same study the calculated "
  "number of chondrocytes produced per day matched the number lost at the chondro-osseous junction, which is "
  "the internal consistency check that makes the partition credible. Hunziker and Schenk reached a compatible "
  "conclusion in rat by a different route: net matrix production per cell is nearly invariant across growth "
  "rates and ages, so acceleration is achieved by modulating final chondrocyte height rather than by making "
  "more matrix. The partition is therefore not a constant of the tissue but a site- and rate-dependent "
  "quantity: slower plates lean more on matrix and less on hypertrophy. No equivalent measurement exists for "
  "any human growth plate, and the human proliferative cell cycle appears to be one to two orders of "
  "magnitude slower than the rat's, so the rat partition cannot be assumed to transfer."),
 quantitative=[
  Q("contribution of cell division to elongation","9","% of elongation","proximal tibia, 28-day-old male Long-Evans rat","rat","wilsman1996","not reported; derived from stereology + oxytetracycline labelling"),
  Q("contribution of matrix synthesis to elongation","32","% of elongation","proximal tibia, 28-day-old Long-Evans rat","rat","wilsman1996","not reported"),
  Q("contribution of hypertrophic cell enlargement to elongation","59","% of elongation","proximal tibia (fastest of four plates), 28-day-old Long-Evans rat","rat","wilsman1996","not reported"),
  Q("contribution of hypertrophic cell enlargement to elongation","44","% of elongation","proximal radius (slowest of four plates), 28-day-old Long-Evans rat","rat","wilsman1996","not reported"),
  Q("contribution of matrix synthesis to elongation","49","% of elongation","proximal radius, 28-day-old Long-Evans rat","rat","wilsman1996","not reported"),
  Q("new chondrocytes produced per day per growth plate","16400","cells/day","proximal tibia, 28-day-old Long-Evans rat","rat","wilsman1996","not reported"),
  Q("new chondrocytes produced per day per growth plate","3700","cells/day","proximal radius, 28-day-old Long-Evans rat","rat","wilsman1996","not reported"),
  Q("range of elongation rates across the four plates compared","50-400","um/24 h","proximal tibia, distal radius, distal tibia, proximal radius; 28-day-old rat","rat","wilsman1996a","approximate range as stated by authors"),
  Q("chondrocytes lost per column at the chondro-osseous junction","8","cells/day (one every 3 h)","proximal tibia, rat in steady-state growth","rat","hunziker1987","not reported"),
 ],
 localization=["rat proximal tibia PZ+HZ: measured by stereology (wilsman1996)",
               "human: unmeasured"],
 human_evidence="absent",
 human_evidence_note="No human study partitions elongation among division, matrix synthesis and hypertrophy; a targeted PubMed search returned four records, none of which does so (see search log g_l1arch_001).",
 species_basis=["rat","pig","mouse"],
 translation_risk="high",
 translation_risk_reason="The canonical 9/32/59 partition is from four growth plates in 28-day-old rats elongating at 50-400 um/day. Human plates elongate at roughly 40 um/day with a proliferative cycle inferred to be ~20 days rather than ~31 h, and the rat data themselves show the partition shifts substantially (hypertrophy 59% to 44%) across a 8-fold range of growth rate within one animal.",
 confidence="C",
 key_refs=[
  R("wilsman1996",8982136,"Wilsman NJ",1996,"primary","Closed the elongation budget in rat: 9% division, 32% matrix, 59% hypertrophy in proximal tibia; hypertrophy falls to 44% and matrix rises to 49% in the slow proximal radius."),
  R("hunziker1989",2607442,"Hunziker EB",1989,"primary","Growth acceleration in rat is achieved almost entirely by increased final cell height; net matrix production per cell and longitudinal proliferation rate are unchanged."),
  R("hunziker1987",3543020,"Hunziker EB",1987,"primary","Rat proximal tibia: 4-fold height, 10-fold volume and 3-fold per-cell matrix increase from proliferative to late hypertrophic stage; one cell lost per column every 3 h."),
  R("breur1991",2010838,"Breur GJ",1991,"primary","Final hypertrophic chondrocyte volume varies linearly with elongation rate (r=0.98 rat, r=0.83 pig) with a species-specific slope."),
  R("cooper2013",23485973,"Cooper KL",2013,"primary","Hypertrophic volume increase occurs in three phases; the duration of the IGF-dependent third phase is what differs most between fast and slow plates."),
 ],
 open_questions=["g_l1arch_001","g_l1arch_009","g_l1arch_010"],
 contradicts=["barreto1994"],
))

n.append(dict(
 id="hypertrophic_volume_increase",
 name="Hypertrophic chondrocyte volume increase",
 aliases=["chondrocyte enlargement","hypertrophic swelling","three-phase hypertrophy"],
 type="process",
 summary=(
  "Terminal chondrocyte enlargement is the largest single contributor to longitudinal elongation and the "
  "parameter that correlates best with growth rate across mammals. Quantitative phase microscopy of live "
  "dissociated mouse chondrocytes resolves the enlargement into three phases with distinct biophysics. Phase 1 "
  "is true hypertrophy: volume rises from about 600 fl to 2000 fl with dry mass density held at 0.183 pg/fl, "
  "the normal value for healthy cells. Phase 2 is swelling: volume rises from about 2000 fl to 8000 fl while dry "
  "mass production continues at a lower relative rate, so density falls to about 0.07 pg/fl, a roughly 60% "
  "dilution confirmed independently by tomographic phase microscopy. Phase 3 resumes proportional growth at the "
  "new low density, taking mouse proximal tibial cells from 8000 fl to about 14,000 fl. Which phases a plate "
  "executes determines its growth rate: the slow mouse proximal radius truncates phase 2 at about 5000 fl and "
  "omits phase 3 entirely, the jerboa metatarsal extends phase 3 to about 23,000 fl, and Igf1-deficient cells "
  "stop at about 7000 fl. Volume increase is fast and time-boxed: proximal tibial cell height more than triples "
  "within roughly 12 h and cells then sit at terminal size for roughly another 12 h before being removed at the "
  "chondro-osseous junction. Stereologically, the rat proximal tibia shows a 4-fold height and 10-fold volume "
  "increase from proliferative to late hypertrophic stage. None of this has been measured in human cells."),
 quantitative=[
  Q("chondrocyte volume at start of enlargement","600","fl","proximal tibia, postnatal mouse, dissociated live cells, diffraction phase microscopy","mouse","cooper2013","approximate value as stated"),
  Q("dry mass density, phase 1 (true hypertrophy)","0.183","pg/fl","mouse proximal tibia chondrocytes 600-2000 fl","mouse","cooper2013","reference healthy-cell density 0.182 pg/fl"),
  Q("volume at end of phase 1","2000","fl","mouse proximal tibia; ~3-fold increase from 600 fl at constant density","mouse","cooper2013","approximate"),
  Q("volume at end of phase 2 (swelling)","8000","fl","mouse proximal tibia; ~4-fold increase from 2000 fl","mouse","cooper2013","approximate"),
  Q("dry mass density at end of phase 2","0.07","pg/fl","mouse proximal tibia hypertrophic chondrocytes","mouse","cooper2013","approximate; ~60% fall confirmed by tomographic phase microscopy"),
  Q("fall in dry mass density in the largest cells","60","% reduction","mouse proximal tibia, regularized tomographic phase microscopy","mouse","cooper2013","approximate"),
  Q("final volume, fast plate","14000","fl","mouse proximal tibia, end of phase 3","mouse","cooper2013","approximate"),
  Q("final volume, slow plate","5000","fl","mouse proximal radius; phase 2 truncated, phase 3 absent; density ~0.10 pg/fl","mouse","cooper2013","approximate"),
  Q("final volume, mouse distal metatarsal","8000","fl","phases 1 and 2 complete, phase 3 truncated","mouse","cooper2013","approximate"),
  Q("final volume, jerboa distal metatarsal","23000","fl","phase 3 extended; ~40-fold increase from initial volume","multiple","cooper2013","approximate; jerboa (Jaculus jaculus), species term not in controlled vocabulary"),
  Q("hypertrophic cell height increase, jerboa vs mouse metatarsal","58","% taller","homologous distal metatarsal growth plates","multiple","cooper2013","not reported"),
  Q("final volume, Igf1-deficient","7000","fl","HoxB6-Cre conditional Igf1 deletion, mouse hindlimb; phase 3 absent","mouse","cooper2013","approximate"),
  Q("reduction in hypertrophic cell height, Igf1 null","30","% shorter","direction of elongation; Igf1-null mice are 35% smaller with unchanged hypertrophic cell number","mouse","cooper2013","not reported"),
  Q("time to triple cell height after leaving the proliferative pool","12","h","mouse proximal tibia, BrdU pulse-chase","mouse","cooper2013","approximate"),
  Q("dwell time at terminal size before chondro-osseous junction turnover","12","h","mouse proximal tibia","mouse","cooper2013","approximate"),
  Q("mean cell height increase, proliferative to late hypertrophic","4","fold","proximal tibia, rat, stereology on optimally fixed tissue","rat","hunziker1987","not reported"),
  Q("mean cell volume increase, proliferative to late hypertrophic","10","fold","proximal tibia, rat","rat","hunziker1987","not reported"),
  Q("mean matrix volume per cell increase","3","fold","proximal tibia, rat","rat","hunziker1987","not reported"),
  Q("correlation of final hypertrophic volume with elongation rate","0.98","Pearson r","four growth plates, 21- and 35-day-old hooded rats","rat","breur1991","r as reported"),
  Q("correlation of final hypertrophic volume with elongation rate","0.83","Pearson r","four growth plates, 21- and 35-day-old Yucatan pigs","porcine","breur1991","r as reported; regression slope differs from rat"),
 ],
 localization=["mouse HZ: measured on dissociated live cells (cooper2013)",
               "rat HZ: measured by stereology (hunziker1987)",
               "human HZ: unmeasured"],
 human_evidence="absent",
 human_evidence_note="No quantitative phase, interferometric or stereological measurement of human hypertrophic chondrocyte volume or dry mass density exists; a targeted PubMed search returned six records, none in human growth plate tissue (search log g_l1arch_008).",
 species_basis=["mouse","rat","porcine","multiple"],
 translation_risk="high",
 translation_risk_reason="Every number in this node is rodent (or jerboa). The mammalian volume-versus-growth-rate relationship already fails in birds (barreto1994) and has a species-specific slope between rat and pig (breur1991), so the mouse volume set points cannot be applied to human plates without measurement.",
 confidence="C",
 key_refs=[
  R("cooper2013",23485973,"Cooper KL",2013,"primary","Three phases of chondrocyte enlargement, including a dry-mass-diluting swelling phase; phase 3 duration is IGF-dependent and sets differential growth."),
  R("hunziker1987",3543020,"Hunziker EB",1987,"primary","4-fold height and 10-fold volume increase from proliferative to late hypertrophic chondrocyte in rat proximal tibia."),
  R("breur1991",2010838,"Breur GJ",1991,"primary","Linear relationship between final hypertrophic volume and elongation rate in rat and pig, with species-specific slope."),
  R("breur1994",7943757,"Breur GJ",1994,"primary","Serial-section and stereological reconstruction localises where in the plate the chondrocyte volume and shape change begins and ends."),
  R("barreto1994",8146454,"Barreto C",1994,"primary","In ducklings and chicks the mammalian hypertrophic-volume/growth-rate relationship does not hold, showing it is not a universal amniote rule."),
 ],
 open_questions=["g_l1arch_008","g_l1arch_009","g_l1arch_010"],
 contradicts=["barreto1994"],
))

n.append(dict(
 id="cell_cycle_time_pz",
 name="Proliferative zone chondrocyte cell cycle time",
 aliases=["PZ cycle time","chondrocyte cell cycle duration"],
 type="process",
 summary=(
  "Proliferative-zone chondrocytes are slow-cycling compared with most renewing tissues, and the cycle length "
  "is set almost entirely by G1. In 28-day-old rats measured in vivo by repeated bromodeoxyuridine pulses, total "
  "cycle time is 30.9 h in the fast proximal tibia, 34.0 h in the distal radius, 48.7 h in the distal tibia and "
  "76.3 h in the slow proximal radius; the proximal tibia and distal radius do not differ significantly but all "
  "other pairwise differences do. S phase is 3.4-6.1 h, G2 is 3.0 h and M is 0.5-0.6 h, so essentially the whole "
  "2.5-fold spread in cycle time is G1. This makes G1 length a locally controlled determinant of differential "
  "growth, in parallel with the hypertrophic volume set point. The human situation is very different and much "
  "worse characterised: Kember and Sissons derived a mean cycle time of about 20 days for the human distal "
  "femoral proliferative zone from a column length of 24 cells and a radiographic growth rate of 1.4 cm/yr, and "
  "explicitly warned against extrapolating rodent kinetics to humans. That figure is inferred, not measured; it "
  "assumes steady state and that every proliferative-zone cell cycles. Thurston and Kember's in vitro tritiated "
  "thymidine labelling of human plates found no labelled cells at all in two of four subjects."),
 quantitative=[
  Q("total cell cycle time, proliferative zone","30.9","h","proximal tibia, 28-day-old rat, repeated BrdU pulse labelling, regression of labelling index on inter-pulse interval","rat","wilsman1996a","not reported; differences among plates tested at p<0.05"),
  Q("total cell cycle time, proliferative zone","34.0","h","distal radius, 28-day-old rat","rat","wilsman1996a","not significantly different from proximal tibia"),
  Q("total cell cycle time, proliferative zone","48.7","h","distal tibia, 28-day-old rat","rat","wilsman1996a","significantly different from proximal tibia, p<0.05"),
  Q("total cell cycle time, proliferative zone","76.3","h","proximal radius, 28-day-old rat","rat","wilsman1996a","significantly different from all others, p<0.05"),
  Q("S phase duration","3.4-6.1","h","proliferative zone, four growth plates, 28-day-old rat","rat","wilsman1996a","range across four plates"),
  Q("G2 phase duration","3.0","h","proliferative zone, 28-day-old rat","rat","wilsman1996a","not reported"),
  Q("M phase duration","0.5-0.6","h","proliferative zone, 28-day-old rat","rat","wilsman1996a","range across four plates"),
  Q("mean cell cycle time, proliferative zone (derived, not measured)","20","days","human distal femur, derived from 24 cells per column and 1.4 cm/yr growth rate","human","kember1976","derived quantity; assumes steady state and 100% growth fraction"),
  Q("mean cell cycle time, proliferative zone","2","days","rodent, as quoted for comparison by the authors","rat","kember1976","author's comparison figure"),
 ],
 localization=["rat PZ: measured in vivo (wilsman1996a)",
               "human distal femur PZ: derived only (kember1976)",
               "human PZ: never measured directly"],
 human_evidence="indirect",
 human_evidence_note="The only human figure is a ~20-day cycle time derived arithmetically from column cell counts and radiographic growth rate (kember1976), supported by an in vitro labelling study in four subjects in which two yielded no labelled cells (thurston1985).",
 species_basis=["rat","human","porcine"],
 translation_risk="high",
 translation_risk_reason="The human and rat values differ by roughly 16-fold and the human value is derived rather than measured. Any inference about proliferation-targeting drug exposure windows, radiation sensitivity or chemotherapy effects on the physis depends on which figure is right.",
 confidence="C",
 key_refs=[
  R("wilsman1996a",8764865,"Wilsman NJ",1996,"primary","Total PZ cycle time in rat ranges from 30.9 h to 76.3 h across four plates, with nearly all the variation in G1."),
  R("kember1976",1018028,"Kember NF",1976,"primary","Human distal femur: 24 cells per proliferative column and a derived mean cycle time of ~20 days; explicit warning against rodent-to-human extrapolation."),
  R("thurston1985",3864550,"Thurston MN",1985,"primary_abstract_only","In vitro tritiated thymidine labelling of human and porcine growth plates; two of four human subjects gave no labelled cells, and pig kinetics lie between human and rodent."),
  R("farnum1993",8443686,"Farnum CE",1993,"primary","Established single- and repeated-pulse BrdU labelling as the method for measuring growth plate proliferative kinetics in vivo."),
 ],
 open_questions=["g_l1arch_002","g_l1arch_012"],
 pending_source="thurston1985",
))

for x in n: print(write(x))
