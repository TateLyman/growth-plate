import yaml
E=[]
def e(s,t,rel,sign,ctx,tier,refs,conf,magnitude=None,notes=None,gap=None):
    E.append({k:v for k,v in dict(
        edge_id="e%05d"%(len(E)+1), source=s, target=t, relation=rel, sign=sign,
        magnitude=magnitude, context=ctx, evidence_tier=tier, refs=refs, confidence=conf,
        gap_id=gap, notes=notes).items() if v is not None})

# --- zonal sequence ---
e("resting_chondrocyte","proliferative_chondrocyte","differentiates_into","+",
  "mouse growth plate, postnatal, after secondary ossification centre formation","T1",["mizuhashi2018"],"C",
  notes="PTHrP+ resting zone cells generate monoclonal columns only after SOC formation.")
e("proliferative_chondrocyte","prehypertrophic_chondrocyte","differentiates_into","+",
  "mouse and rat proliferative-to-prehypertrophic transition, postnatal","T1",["cooper2013","breur1994"],"C",
  magnitude="cell volume ~600 fl at entry (mouse)")
e("prehypertrophic_chondrocyte","hypertrophic_chondrocyte","differentiates_into","+",
  "mouse proximal tibia, postnatal","T1",["cooper2013"],"C",
  magnitude="phase 1: 600 to 2000 fl at constant dry mass density 0.183 pg/fl")
e("resting_zone","proliferative_zone","precedes","+",
  "mammalian growth plate, epiphyseal to metaphyseal axis","T1",["mizuhashi2018","avijgan2026"],"B")
e("proliferative_zone","prehypertrophic_zone","precedes","+",
  "mammalian growth plate zonal sequence","T1",["breur1994"],"C")
e("prehypertrophic_zone","hypertrophic_zone","precedes","+",
  "mammalian growth plate zonal sequence","T1",["cooper2013","hunziker1987"],"C")
e("hypertrophic_zone","zone_provisional_calcification","precedes","+",
  "metaphyseal face of the growth plate; human specimens mapped by ToF-SIMS","T1",["zoehrer2025"],"B")
e("zone_provisional_calcification","chondro_osseous_junction","precedes","+",
  "human and rodent metaphyseal face","T1",["zoehrer2025","farnum1989"],"B")
e("chondro_osseous_junction","primary_spongiosa","precedes","+",
  "human rib birth to adolescence; rodent metaphysis","T1",["byers2000","farnum1989"],"B")

# --- elongation budget ---
e("chondrocyte_hypertrophy","elongation_budget","required_for","+",
  "rat proximal tibia, 28 days","T1",["wilsman1996"],"C",
  magnitude="59% of elongation (proximal tibia), 44% (proximal radius)")
e("chondrocyte_proliferation_rate","elongation_budget","required_for","+",
  "rat proximal tibia, 28 days","T1",["wilsman1996"],"C",
  magnitude="9% of elongation directly; sets the number of cells available to hypertrophy")
e("hypertrophic_volume_increase","growth_velocity_longitudinal","correlates_with","+",
  "four growth plates, 21- and 35-day-old rats and Yucatan pigs","T1",["breur1991"],"C",
  magnitude="Pearson r = 0.98 (rat), r = 0.83 (pig); species-specific regression slope")
e("elongation_budget","growth_velocity_longitudinal","required_for","+",
  "rat, four growth plates","T1",["wilsman1996","hunziker1989"],"C")
e("hypertrophic_phase_duration","hypertrophic_volume_increase","required_for","unknown",
  "rat proximal tibia 21-80 days; mouse proximal tibia","T1",["hunziker1989","cooper2013"],"C",
  magnitude="~2 days (rat) / ~24 h column turnover (mouse), invariant across growth rates",
  notes="A fixed transit window forces fast plates to enlarge cells faster rather than for longer.")

# --- column architecture ---
e("chondrocyte_rotation","chondrocyte_column_formation","required_for","+",
  "mouse growth plate, embryonic and postnatal","T1",["romereim2014","rubin2024","aszodi2003"],"C",
  magnitude="columns tolerate up to ~60% incomplete rotations before becoming clusters")
e("chondrocyte_column_formation","clonal_column","required_for","+",
  "mouse postnatal growth plate","T1",["rubin2024","mizuhashi2018"],"C")
e("chondrocyte_rotation","chondrocyte_cluster","inhibits","-",
  "mouse E18.5 and P40 growth plate","T1",["rubin2024"],"C",
  magnitude="clusters show 15.5-17.3% complete rotations vs 36.4-39.5% in columns")
e("chondrocyte_cluster","appositional_growth","correlates_with","+",
  "mouse, eight growth plates, E17.5 to P40, micro-CT","T1",["rubin2024"],"D",
  magnitude="expansion:elongation ratio 0.16-0.18 embryonic (cluster-dominated) to 0-0.04 at P40 (column-dominated)",
  notes="Correlative only; no experiment has dissociated cluster abundance from developmental stage.")
e("clonal_column","column_density","correlates_with","+",
  "human rib across age; rat plates of differing rate","T1",["byers2000","wilsman1996"],"B")

# --- vascular / catabolic ---
e("septoclast","cartilage_septum_resorption","required_for","+",
  "mouse chondro-osseous border, 3 weeks","T1",["sivaraj2022","lee1995"],"C",
  magnitude="FABP5+ septoclasts significantly outnumber osteoclasts at the interface (n=6 mice)")
e("metaphyseal_vasculature","septoclast","required_for","+",
  "mouse metaphysis; endothelial Dll4-Notch dependence","T1",["sivaraj2022"],"C")
e("cartilage_septum_resorption","chondro_osseous_junction","required_for","+",
  "rat and swine chondro-osseous junction","T1",["farnum1989","hunziker1987"],"C",
  magnitude="one chondrocyte and its transverse septum removed per column every 3 h (rat)")
e("metaphyseal_vasculature","primary_spongiosa","required_for","+",
  "mouse metaphysis; type H capillary compartment","T1",["kusumbe2014"],"C")
e("type_h_vessel","metaphyseal_vasculature","required_for","+",
  "mouse metaphysis and endosteum, juvenile to aged","T1",["kusumbe2014"],"C")
e("cartilage_canal","epiphyseal_vasculature","precedes","+",
  "mouse femoral epiphysis before secondary ossification centre formation; human digits","T1",["blumer2007","walzer2014"],"C")
e("epiphyseal_vasculature","resting_zone","required_for","+",
  "human and mouse epiphysis; the plate is avascular and supplied by diffusion from its margins","T1",
  ["walzer2014","blumer2008"],"C")
e("oxygen_gradient_growth_plate","resting_chondrocyte","correlates_with","-",
  "mouse growth plate interior; rat and rabbit electrode profiles","T1",["schipani2001","brighton1971","zhang2023"],"C",
  notes="Interior of the plate is the most hypoxic compartment; HIF-1alpha loss kills central chondrocytes.")
e("nutrient_diffusion_growth_plate","growth_plate_height","correlates_with","-",
  "inference from avascularity and diffusion distance; no direct measurement in any species","T5",
  ["brighton1971","zhang2023"],"E",
  notes="Flagged inference: diffusion limitation is a plausible but unmeasured constraint on plate height.")
e("transphyseal_canal","growth_plate","correlates_with","unknown",
  "human distal femur, intercondylar region","T1",["shao2022"],"C",
  notes="Transphyseal channels breach the physis as a tumour and infection barrier.")

# --- peripheral ---
e("groove_of_ranvier","appositional_growth","required_for","+",
  "rabbit growth plate periphery; human digits and hindfoot","T1",["shapiro1977","cheng1995","walzer2014"],"C")
e("groove_of_ranvier","perichondrial_ring_lacroix","precedes","+",
  "rabbit and human plate periphery; the groove is continuous with the ring","T1",["shapiro1977"],"D")
e("borderline_zone","primary_spongiosa","differentiates_into","+",
  "mouse growth plate periphery, inducible lineage tracing","T1",["mizuhashi2019"],"D",
  notes="Borderline chondrocytes become marrow stromal cells and osteoblasts beneath the plate.")

# --- sites ---
e("site_specific_growth_rate","distal_femur_plate","correlates_with","+",
  "human, ages 7 to skeletal maturity, n=244","T1",["pritchett1992"],"A",
  magnitude="~70% of femoral length; ~1.3 cm/yr")
e("site_specific_growth_rate","proximal_tibia_plate","correlates_with","+",
  "human, ages 7 to skeletal maturity, n=244","T1",["pritchett1992"],"A",
  magnitude="~57% of tibial length")
e("site_specific_growth_rate","proximal_humerus_plate","correlates_with","+",
  "human, n=200 subjects","T1",["pritchett1991"],"A", magnitude="~80% of humeral length")
e("site_specific_growth_rate","distal_radius_plate","correlates_with","+",
  "human, n=200 subjects","T1",["pritchett1991"],"A", magnitude="~80% of radial length; distal ulna ~85%")
e("site_specific_growth_rate","vertebral_growth_plate","correlates_with","unknown",
  "human spine, more than 130 growth plates; per-plate rates unpublished","T5",["dimeglio2020"],"D")
e("site_specific_growth_rate","metacarpal_plate","correlates_with","+",
  "mouse and jerboa metatarsal; single-plate architecture","T1",["cooper2013","reno2025"],"C",
  magnitude="jerboa metatarsal hypertrophic volume ~23,000 fl vs ~8,000 fl in mouse")
e("cell_cycle_time_pz","site_specific_growth_rate","correlates_with","-",
  "four growth plates, 28-day-old rat","T1",["wilsman1996a"],"C",
  magnitude="30.9 h (fast proximal tibia) to 76.3 h (slow proximal radius), variation concentrated in G1")

# --- temporal pattern ---
e("saltation_stasis_growth","growth_velocity_longitudinal","hypothesized_link","biphasic",
  "human infants (anthropometry) versus rabbit and lamb (direct physeal measurement)","T1",
  ["lampl1992","klein1994","noonan2004","mcbrien2011"],"speculative",
  notes="Whether tissue-level elongation truly alternates between zero and high velocity is unresolved; the only established discontinuity is diurnal load gating.",
  gap="g_l1arch_005")
e("growth_plate_height","growth_velocity_longitudinal","correlates_with","unknown",
  "rat 21-80 days; mouse proximal tibia neonate to young adult","T1",["hunziker1989","wilson2021"],"C",
  notes="Total plate height and width correlate with growth rate in mouse, but hypertrophic zone height alone does not, and bulk height is explicitly a poor estimator in rat.")
e("appositional_growth","bone_modeling_drift","precedes","+",
  "mouse micro-CT of chondro-osseous junction width; general vertebrate bone modelling","T5",
  ["rubin2024","rauch2005"],"C")
e("bone_modeling_drift","metaphyseal_funnelization","required_for","+",
  "mammalian metaphysis; osteoclast-dependent surface resorption","T5",["rauch2005"],"C")
e("growth_plate","growth_velocity_longitudinal","required_for","+",
  "human and all mammals; the plate is the sole source of longitudinal growth","T1",
  ["pritchett1992","kember1976"],"A")

with open("atlas/edges/shards/l1arch.edges.yaml","w") as f:
    yaml.safe_dump({"edges":E},f,sort_keys=False,default_flow_style=False,width=110,allow_unicode=True)
print(len(E),"edges")
