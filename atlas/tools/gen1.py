#!/usr/bin/env python3
import os, yaml
D = "/home/user/growth-plate/atlas/nodes/L2_stem_and_progenitor_biology"
LV = "2026-08-05"

def w(n):
    n.setdefault("layer", "L2")
    n.setdefault("stub", False)
    n.setdefault("last_verified", LV)
    p = os.path.join(D, n["id"] + ".yaml")
    with open(p, "w") as f:
        yaml.safe_dump(n, f, sort_keys=False, default_flow_style=False, width=100,
                       allow_unicode=True)
    print("wrote", p)

R = {
 "mizuhashi2018": dict(ref_id="mizuhashi2018", pmid="30401834", doi="10.1038/s41586-018-0662-5",
   first_author="Mizuhashi K", year=2018, type="primary"),
 "newton2019": dict(ref_id="newton2019", pmid="30814736", doi="10.1038/s41586-019-0989-6",
   first_author="Newton PT", year=2019, type="primary_abstract_only"),
 "hallett2021": dict(ref_id="hallett2021", pmid="34309509", doi="10.7554/elife.64513",
   first_author="Hallett SA", year=2021, type="primary"),
 "muruganandan2022": dict(ref_id="muruganandan2022", pmid="35523895", doi="10.1038/s41467-022-30247-1",
   first_author="Muruganandan S", year=2022, type="primary"),
 "kodama2025": dict(ref_id="kodama2025", pmid="40025030", doi="10.1038/s41413-025-00407-2",
   first_author="Kodama J", year=2025, type="primary"),
 "chu2026": dict(ref_id="chu2026", pmid="41984930", doi="10.1126/scitranslmed.adw3590",
   first_author="Chu NTL", year=2026, type="primary_abstract_only"),
 "chu2025": dict(ref_id="chu2025", pmid="41289405", doi="10.1073/pnas.2512316122",
   first_author="Chu NTL", year=2025, type="primary"),
 "avijgan2025": dict(ref_id="avijgan2025", doi="10.1101/2025.03.12.642613",
   first_author="Avijgan M", year=2025, type="preprint"),
 "avijgan2026": dict(ref_id="avijgan2026", pmid="41795828", doi="10.1093/stmcls/sxag010",
   first_author="Avijgan M", year=2026, type="systematic_review"),
 "trompet2024": dict(ref_id="trompet2024", pmid="38516888", doi="10.1172/jci.insight.165226",
   first_author="Trompet D", year=2024, type="primary"),
 "bian2024": dict(ref_id="bian2024", pmid="39236220", doi="10.1093/jbmr/zjae144",
   first_author="Bian F", year=2024, type="primary"),
 "horike2026": dict(ref_id="horike2026", pmid="41748604", doi="10.1038/s41467-026-69507-9",
   first_author="Horike N", year=2026, type="primary"),
 "snippert2010": dict(ref_id="snippert2010", pmid="20887898", doi="10.1016/j.cell.2010.09.016",
   first_author="Snippert HJ", year=2010, type="primary_abstract_only"),
 "rinkevich2011": dict(ref_id="rinkevich2011", pmid="21866153", doi="10.1038/nature10346",
   first_author="Rinkevich Y", year=2011, type="primary_abstract_only"),
 "qu2025": dict(ref_id="qu2025", pmid="41253754", doi="10.1038/s41467-025-65029-y",
   first_author="Qu X", year=2025, type="primary"),
 "carlone2021": dict(ref_id="carlone2021", pmid="33438789", doi="10.1002/stem.3318",
   first_author="Carlone DL", year=2021, type="primary"),
 "mizuhashi2019": dict(ref_id="mizuhashi2019", pmid="30888720", doi="10.1002/jbmr.3719",
   first_author="Mizuhashi K", year=2019, type="primary_abstract_only"),
}
def ref(k, finding):
    d = dict(R[k]); d["one_line_finding"] = finding; return d

# ------------------------------------------------------------------ 1
w(dict(
 id="resting_zone_niche",
 name="Resting zone as a stem cell niche",
 aliases=["reserve zone niche", "RZ niche", "epiphyseal stem cell niche"],
 type="tissue_structure",
 summary=(
  "The resting (reserve) zone is the epiphyseal-most stratum of the growth plate, "
  "containing small round chondrocytes in an abundant matrix that divide rarely and sit "
  "immediately below the secondary ossification centre. In mouse it functions as a niche "
  "rather than a passive reserve: it holds at least three partially overlapping slow-cycling "
  "populations (PTHrP/Pthlh+, FoxA2+, and label-retaining Col2a1-lineage cells) that seed the "
  "proliferative columns below. Its niche signals are defined negatively as much as "
  "positively - resting chondrocytes sit in a Wnt-inhibitory microenvironment (enriched for "
  "secreted Wnt inhibitors; forced beta-catenin activation drives them out of the zone), and "
  "their fate is instructed in reverse by Indian hedgehog from the hypertrophic zone, since "
  "both Smoothened agonism and antagonism reduce the number of columns formed from labelled "
  "resting cells. Loss of niche integrity is phenotypically visible: partial diphtheria-toxin "
  "ablation of PTHrP+ resting cells in mouse shrinks the proliferative zone and expands the "
  "hypertrophic and resting zones, and Adgrg6 loss shortens the resting zone and produces "
  "intra-plate cell clusters. In humans the resting zone has been mapped only "
  "transcriptionally and histologically; no human cell has ever been shown to behave as a "
  "resting-zone stem cell, because clonal lineage tracing cannot be performed in people."),
 quantitative=[
  dict(parameter="EdU+ fraction, PTHrP-mCherry+ resting chondrocytes at P9", value="6.1",
       unit="% of mCherry+ cells", conditions="postnatal day 9 mouse distal femur, 2 h EdU pulse",
       species="mouse", source_ref="mizuhashi2018", uncertainty="SD 2.3, n=3 mice"),
  dict(parameter="EdU+ fraction, proliferative zone chondrocytes at P9", value="30.5",
       unit="% of PZ chondrocytes", conditions="postnatal day 9 mouse distal femur, same assay",
       species="mouse", source_ref="mizuhashi2018", uncertainty="SD 3.2, n=3 mice"),
  dict(parameter="H2B-EGFP label-retaining fraction of Col2a1-lineage chondrocytes, plateau",
       value="2.6", unit="% of Col2a1-creER lineage cells",
       conditions="doxycycline chase from P21, mouse distal femur, flow cytometry",
       species="mouse", source_ref="hallett2021", uncertainty="SE 0.9; decay half-life 0.99-1.18 weeks"),
  dict(parameter="H2B-EGFP signal loss per chondrocyte division", value="2.03",
       unit="fold", conditions="P35 mouse, paired EdU- RZ cell vs EdU+ PZ daughter, 24 cell pairs",
       species="mouse", source_ref="hallett2021", uncertainty="n=4 mice, p<0.0001"),
 ],
 localization=[
  "mouse RZ: confirmed, PTHrP-mCherry knock-in reporter and PTHrP-creER lineage (mizuhashi2018)",
  "mouse RZ: confirmed, H2B-EGFP label-retaining cells concentrated at the top of the plate (hallett2021)",
  "human RZ: transcriptionally defined only, spatial transcriptomics of adolescent biopsies (avijgan2025, chu2026)",
  "rabbit RZ: FoxA2+ cells present at the cartilage/SOC interface (muruganandan2022)",
 ],
 human_evidence="indirect",
 human_evidence_note=(
  "Human resting zone cells have been profiled by single-cell and spatial transcriptomics in "
  "adolescent surgical specimens and show quiescence-associated features, but no functional "
  "stem-cell assay has been performed in human tissue in situ."),
 species_basis=["mouse", "rabbit", "human"],
 translation_risk="high",
 translation_risk_reason=(
  "Every functional claim about the niche (clonality, self-renewal, ablation, Hedgehog and Wnt "
  "manipulation) rests on mouse genetics. Mice never fuse their growth plates, so the terminal "
  "behaviour of the human niche has no murine counterpart."),
 confidence="C",
 key_refs=[
  ref("mizuhashi2018", "PTHrP+ resting chondrocytes are slow-cycling, clonogenic and generate columns; partial ablation distorts zone heights"),
  ref("hallett2021", "Label-retaining resting chondrocytes occupy a Wnt-inhibitory microenvironment and exit on beta-catenin activation"),
  ref("muruganandan2022", "FoxA2+ cells at the top of the resting zone are a second, longer-lived stem population"),
  ref("bian2024", "ADGRG6 is required to maintain slow-cycling resting zone cells and normal zone architecture"),
  ref("avijgan2025", "Human adolescent resting zone contains transcriptionally quiescent sub-populations (CHRDL2+, SFRP5+)"),
 ],
 open_questions=["g_l2stem_001", "g_l2stem_003", "g_l2stem_005"],
 contradicts=["soc_formation_triggers_stemness"],
))

# ------------------------------------------------------------------ 2
w(dict(
 id="pthrp_positive_resting_chondrocyte",
 name="PTHrP+ (Pthlh+) resting zone chondrocyte",
 aliases=["PTHrP+ RZ chondrocyte", "epiphyseal skeletal stem cell", "epSSC"],
 type="cell_type",
 summary=(
  "PTHrP-expressing chondrocytes appear in the centre of the mouse growth plate around P3, "
  "expand sharply between P6 and P9, and occupy a discrete resting zone; they are markedly "
  "less proliferative than the cells below (6.1% vs 30.5% EdU+ at P9). Lineage tracing with a "
  "PTHrP-creER BAC line pulsed at P6 shows the labelled cells stay in the resting zone for "
  "about a week, then generate short (<10-cell) and subsequently long (>10-cell) columns, and "
  "continue to generate new columns for at least one year; Confetti labelling shows each "
  "column is monochromatic, i.e. clonal. Descendants leave the plate and become Col1a1(2.3kb)-GFP+ "
  "osteoblasts and Cxcl12-GFP+ marrow stromal cells, but not adipocytes in vivo (0/443 cells "
  "scored under rosiglitazone plus high-fat diet), so multipotency is acquired only after the "
  "post-mitotic hypertrophic step. Immunophenotypically these cells are heterogeneous: 49.2% "
  "of PTHrP-mCherry+ CD45-Ter119-CD31-CD51+CD90- growth plate cells carry the CD105-CD200+ "
  "mSSC phenotype, 23.4% pre-BCSP and 27.4% BCSP. Only a small minority behave as long-term "
  "stem cells - 16.3% of P12-pulsed colonies formed secondary colonies and 12.5% of those "
  "could be passaged nine times, i.e. roughly 2-3% of PTHrP+ colony-forming cells. No "
  "equivalent cell has been identified in human growth plate; the human resting zone contains "
  "a PTHLH-negative stem-like population, which is a direct challenge to translating this "
  "marker."),
 quantitative=[
  dict(parameter="EdU+ fraction of PTHrP-creER-labelled resting chondrocytes", value="7.7",
       unit="% of tdTomato+ cells", conditions="pulsed P6, analysed with serial EdU, mouse",
       species="mouse", source_ref="mizuhashi2018", uncertainty="SD 2.0, n=3 mice; PZ comparison 61.1 +/- 11.5%"),
  dict(parameter="PTHrP-mCherry+ cells with mSSC (CD105-CD200+) phenotype", value="49.2",
       unit="% of CD45-Ter119-CD31-CD51+CD90- mCherry+ cells",
       conditions="P9 mouse growth plate, flow cytometry", species="mouse",
       source_ref="mizuhashi2018", uncertainty="SD 8.4"),
  dict(parameter="PTHrP-creER colonies forming secondary colonies (P9 pulse)", value="3.3",
       unit="% (17/518 clones)", conditions="ex vivo colony assay, mouse", species="mouse",
       source_ref="mizuhashi2018", uncertainty="none survived a further passage"),
  dict(parameter="PTHrP-creER colonies forming secondary colonies (P12 pulse)", value="16.3",
       unit="% (16/98 clones)", conditions="ex vivo colony assay during active SOC development",
       species="mouse", source_ref="mizuhashi2018", uncertainty="2/16 (12.5%) passaged >=9 generations"),
  dict(parameter="Long-term self-renewing fraction of PTHrP+ colony-forming cells", value="2-3",
       unit="%", conditions="authors' summary estimate from serial passaging", species="mouse",
       source_ref="mizuhashi2018", uncertainty="derived figure, not a measured CI"),
  dict(parameter="PTHrP+ colonies reaching passage 5", value="1.4",
       unit="% (2/143 colonies)", conditions="side-by-side comparison against FoxA2+ colonies, P18 mouse",
       species="mouse", source_ref="muruganandan2022", uncertainty="n=3 experiments"),
  dict(parameter="In vivo adipocyte output of PTHrP-creER lineage", value="0",
       unit="LipidTOX+ cells / 443 scored", conditions="high-fat diet plus rosiglitazone, mouse",
       species="mouse", source_ref="mizuhashi2018", uncertainty="not reported"),
 ],
 localization=[
  "mouse RZ: confirmed by PTHrP-mCherry knock-in and PTHrP-creER lineage tracing (mizuhashi2018)",
  "mouse perichondrium (fetal): confirmed, PTHrP-mCherry+ cells are perichondrial before birth (mizuhashi2018)",
  "human RZ: unconfirmed - human resting-zone 'root' stem cells do not express PTHLH (chu2026)",
 ],
 human_evidence="absent",
 human_evidence_note=(
  "No human PTHrP+ resting chondrocyte has been shown to have stem-cell behaviour; the one "
  "human growth plate single-cell/spatial study to address it reports that the candidate human "
  "root stem cell population is PTHLH-negative."),
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason=(
  "Identity rests entirely on tamoxifen-inducible Cre lineage tracing, which cannot be done in "
  "humans, and the marker itself appears not to identify the analogous human population."),
 confidence="C",
 key_refs=[
  ref("mizuhashi2018", "PTHrP+ resting chondrocytes are clonal, long-lived column-forming skeletal stem cells with ~2-3% long-term self-renewal"),
  ref("muruganandan2022", "PTHrP+ colonies are markedly shorter-lived than FoxA2+ colonies (1.4% vs 9% reaching late passage)"),
  ref("trompet2024", "Hedgehog activation expands PTHrP+ epiphyseal stem cell clones and increases bone length in mice"),
  ref("chu2026", "The stem-like 'root' population of the human pubertal resting zone does not express PTHLH"),
 ],
 open_questions=["g_l2stem_001", "g_l2stem_003", "g_l2stem_010"],
 contradicts=["foxa2_resting_chondrocyte", "prrx1_root_stem_cell"],
))

# ------------------------------------------------------------------ 3
w(dict(
 id="foxa2_resting_chondrocyte",
 name="FoxA2+ resting zone chondrocyte",
 aliases=["FoxA2+ long-term skeletal stem cell"],
 type="cell_type",
 summary=(
  "FoxA2+ cells sit at the very top of the mouse resting zone, at the cartilage/secondary "
  "ossification centre interface (75% within the cartilage, 25% inside the SOC domain at "
  "P13-P17). They are a small population - about 98 cells per section by immunohistochemistry "
  "at P14 - and are essentially non-overlapping with PTHrP+ cells at the time of labelling "
  "(0.017% double-positive by flow cytometry, indistinguishable from the 0.014% background). "
  "By P40 a FoxA2 pulse gives rise to PTHrP+ cells (0.1% double-positive), placing FoxA2+ "
  "cells upstream. In colony assays FoxA2+ cells are more clonogenic and much longer-lived "
  "than PTHrP+ cells: 9% (10/112) of FoxA2+ colonies reached passage 9 or beyond, versus 1.4% "
  "(2/143) of PTHrP+ colonies reaching passage 5. FoxA2+ cells are required for growth plate "
  "regeneration after injury. FoxA2+ cells at this site are also present in rabbit, the only "
  "non-murine mammalian confirmation of any resting-zone stem cell marker, but no functional "
  "tracing has been done outside mouse."),
 quantitative=[
  dict(parameter="FoxA2+/PTHrP+ double-positive cells at P18", value="0.017",
       unit="% of sorted growth plate cells", conditions="FoxA2-creER;ZsGreen;PTHrP-mCherry mouse, tamoxifen P13-P17",
       species="mouse", source_ref="muruganandan2022", uncertainty="SD 0.004; double-negative background 0.014%"),
  dict(parameter="FoxA2+/PTHrP+ double-positive cells at P40 after P13-P17 pulse", value="0.1",
       unit="% of sorted cells", conditions="same mice, 3-week chase", species="mouse",
       source_ref="muruganandan2022", uncertainty="not reported"),
  dict(parameter="FoxA2+ colonies reaching passage 9 or beyond", value="8.9",
       unit="% (10/112 colonies)", conditions="ex vivo colony assay, P18 mouse", species="mouse",
       source_ref="muruganandan2022", uncertainty="n=3 experiments"),
  dict(parameter="FoxA2+ cells per growth plate section at P14", value="97.67",
       unit="cells", conditions="immunohistochemistry, mouse tibia", species="mouse",
       source_ref="muruganandan2022", uncertainty="SD 9"),
  dict(parameter="FoxA2+ cells located within growth plate cartilage (rest inside SOC)", value="75",
       unit="%", conditions="5-DTAF bone-matrix counterstain, P13-P17 pulse, mouse", species="mouse",
       source_ref="muruganandan2022", uncertainty="not reported"),
 ],
 localization=[
  "mouse RZ (uppermost, adjacent SOC): confirmed by FoxA2-creER lineage and IHC (muruganandan2022)",
  "rabbit RZ: FoxA2 immunoreactivity present at the same anatomical position (muruganandan2022)",
  "human RZ: unconfirmed",
 ],
 human_evidence="absent",
 human_evidence_note="FoxA2 has not been examined as a stem-cell marker in human growth plate tissue.",
 species_basis=["mouse", "rabbit"],
 translation_risk="high",
 translation_risk_reason=(
  "All functional evidence is from inducible Cre tracing in mouse; the rabbit data are "
  "immunostaining only and carry no clonal information."),
 confidence="D",
 key_refs=[
  ref("muruganandan2022", "FoxA2+ cells are a distinct, more clonogenic and longer-lived resting zone stem population upstream of PTHrP+ cells"),
  ref("mizuhashi2018", "Provides the PTHrP+ population against which FoxA2+ longevity is benchmarked"),
 ],
 open_questions=["g_l2stem_001", "g_l2stem_004", "g_l2stem_010"],
 contradicts=["pthrp_positive_resting_chondrocyte"],
))

# ------------------------------------------------------------------ 4
w(dict(
 id="apoe_resting_zone_marker",
 name="ApoE as a pan-resting-zone chondrocyte marker",
 aliases=["Apolipoprotein E resting zone marker"],
 type="protein",
 summary=(
  "Every previously proposed resting-zone stem cell marker (PTHrP/Pthlh, FoxA2, Axin2, CD73) "
  "labels only a subset of resting chondrocytes, which leaves the zone itself defined by the "
  "ambiguous histological criterion of 'small round cells without columns'. Apolipoprotein E "
  "was identified as a marker expressed by essentially all chondrocytes of the mouse resting "
  "zone and not by proliferative or hypertrophic chondrocytes, so it provides a molecular "
  "definition of the compartment rather than of a stem cell within it. This matters "
  "operationally: comparisons of 'resting zone height' or 'resting cell number' across "
  "laboratories, including the senescence-depletion literature, currently rest on morphology "
  "rather than on a marker, and ApoE offers a way to standardise them. ApoE is a marker of "
  "compartment identity, not of stemness - its expression does not by itself imply "
  "self-renewal. Human validation has not been reported."),
 quantitative=[],
 localization=[
  "mouse RZ: confirmed, ApoE labels essentially all resting chondrocytes (kodama2025)",
  "mouse PZ/HZ: negative (kodama2025)",
  "human RZ: unconfirmed",
 ],
 human_evidence="absent",
 human_evidence_note="No study has tested ApoE as a resting zone marker in human growth plate tissue.",
 species_basis=["mouse"],
 translation_risk="moderate",
 translation_risk_reason=(
  "A zonal expression marker is more likely to translate than a functional stem-cell claim, but "
  "human zonal expression has not been checked and human and mouse growth plate zonal "
  "transcriptomes differ."),
 confidence="D",
 key_refs=[
  ref("kodama2025", "ApoE marks essentially all mouse resting zone chondrocytes, giving the zone a molecular rather than histological definition"),
  ref("avijgan2025", "Independent spatial transcriptomic zonal marker discovery in human growth plate, against which ApoE could be tested"),
 ],
 open_questions=["g_l2stem_001"],
))

# ------------------------------------------------------------------ 5
w(dict(
 id="label_retaining_chondrocyte",
 name="Label-retaining resting chondrocyte (LRC)",
 aliases=["slow-cycling growth plate chondrocyte", "H2B-GFP label-retaining chondrocyte"],
 type="cell_type",
 summary=(
  "Label retention is the assay that turns 'resting' from a histological adjective into a "
  "measured cell-cycle property. A chondrocyte-specific Tet-Off H2B-EGFP system (Col2a1-tTA) "
  "combined with Col2a1-creER lineage marking allows slow-cycling cells to be identified by "
  "retained histone-bound GFP: signal halves with each division (measured fold change 2.03 per "
  "division), so cells at the top decile of brightness after a doxycycline chase are the least "
  "divided. The label-retaining fraction of Col2a1-lineage chondrocytes decays with a half-life "
  "of roughly one week (0.99-1.18 weeks) from 86.5% to a plateau of 2.6%, meaning that the "
  "durably slow-cycling compartment of the mouse growth plate is a few percent of chondrocytes. "
  "Transcriptomically, these LRCs are enriched for both secreted Wnt inhibitors and Wnt "
  "activators, and activating beta-catenin in them drives them out of the resting zone - the "
  "clearest positive definition of a niche signal for this compartment. Growth hormone reduces "
  "this label-retaining pool by pushing the cells into transit-amplifying differentiation, "
  "which links a therapeutic hormone directly to stem cell consumption. A 2026 PRISMA "
  "systematic review found that despite decades of the word 'quiescent', functional and "
  "molecular assays of quiescence in this compartment are sparse and inconsistently defined."),
 quantitative=[
  dict(parameter="Label-retaining fraction of Col2a1-lineage chondrocytes, initial", value="86.5",
       unit="%", conditions="P21 mouse, before doxycycline chase, flow cytometry",
       species="mouse", source_ref="hallett2021", uncertainty="SE 1.3"),
  dict(parameter="Label-retaining fraction, plateau after chase", value="2.6", unit="%",
       conditions="doxycycline chase from P21, mouse distal femur", species="mouse",
       source_ref="hallett2021", uncertainty="SE 0.9"),
  dict(parameter="Decay half-life of the label-retaining population", value="0.99-1.18",
       unit="weeks", conditions="non-linear decay fit, mouse", species="mouse",
       source_ref="hallett2021", uncertainty="range of fitted values"),
  dict(parameter="Growth plate chondrocytes as fraction of dissociated Col2a1-creER lineage cells",
       value="99.1", unit="%", conditions="microdissected epiphysis after collagenase, P49 mouse",
       species="mouse", source_ref="hallett2021", uncertainty="SD 1.4, n=4 mice"),
 ],
 localization=[
  "mouse RZ: confirmed, brightest H2B-EGFP cells localise to the top of the growth plate (hallett2021)",
  "human RZ: indirect - a subset of human resting chondrocytes shows nuclear-retained mRNA and heterochromatin consistent with G0 (avijgan2025)",
 ],
 human_evidence="indirect",
 human_evidence_note=(
  "Human resting chondrocytes show quiescence-associated features (predominantly nuclear mRNA, "
  "abundant heterochromatin, ability to exit G0 ex vivo) in spatial transcriptomic biopsies, but "
  "label retention itself requires transgenic pulse-chase and has never been done in humans."),
 species_basis=["mouse", "human"],
 translation_risk="high",
 translation_risk_reason=(
  "The quantitative kinetics come from a transgenic Tet-Off system with no human counterpart; "
  "human evidence is descriptive and cross-sectional."),
 confidence="C",
 key_refs=[
  ref("hallett2021", "Defines label-retaining resting chondrocytes quantitatively and places them in a Wnt-inhibitory niche"),
  ref("chu2025", "Growth hormone depletes the label-retaining growth plate stem cell pool by driving differentiation"),
  ref("avijgan2026", "Systematic review showing quiescence in resting zone chondrocytes is asserted far more often than it is measured"),
  ref("avijgan2025", "Human resting zone sub-populations show molecular hallmarks of functional quiescence"),
 ],
 open_questions=["g_l2stem_005", "g_l2stem_010"],
))

# ------------------------------------------------------------------ 6
w(dict(
 id="prrx1_root_stem_cell",
 name="Prrx1+ 'root' resting zone stem cell",
 aliases=["root stem cell", "PTHLH-negative resting zone stem cell"],
 type="cell_type",
 summary=(
  "Single-cell and spatial profiling of early pubertal human growth plates obtained from "
  "growth-restricting surgery identified two stem-like populations in the human resting zone "
  "that differ in proliferative activity and molecular identity. The upper population, termed "
  "root stem cells, expresses several skeletal stem cell markers but is PTHLH-negative and "
  "occupies a microenvironment low in WNT and TGF-beta ligands - the same negative-signalling "
  "logic reported for the mouse label-retaining niche. A transcriptionally matched population "
  "was found in unsorted mouse growth plates and marked with Prrx1; clonal lineage tracing of "
  "Prrx1+ cells in mouse generated extensive chondrocyte clones and stromal and osteoblastic "
  "progeny, satisfying the mouse definition of a stem cell. This is the first candidate human "
  "growth plate stem cell population, and it directly complicates the PTHrP-centred model: the "
  "human cell with the most stem-like profile does not express the mouse marker. Human explant "
  "culture showed that growth hormone acts directly on the plate, activating JAK/STAT, TGF-beta "
  "and ERK and inhibiting AKT, and stimulating proliferation of both cartilage stem cells and "
  "proliferative-zone chondrocytes. The full-text figures were not accessible, so no clonal "
  "kinetic numbers are recorded here."),
 quantitative=[],
 localization=[
  "human RZ (upper): confirmed by single-cell plus spatial transcriptomics of pubertal biopsies (chu2026)",
  "mouse RZ: confirmed, Prrx1-marked equivalent population traced clonally (chu2026)",
 ],
 human_evidence="direct",
 human_evidence_note=(
  "The population was identified in human tissue, and human growth plate explants responded "
  "directly to growth hormone; however the stem-cell property itself was demonstrated only by "
  "lineage tracing in the mouse counterpart."),
 species_basis=["human", "mouse"],
 translation_risk="moderate",
 translation_risk_reason=(
  "The population was defined in human tissue, which removes the usual species leap for "
  "identity, but 'stemness' was still established by mouse lineage tracing of a "
  "transcriptionally matched cell, and transcriptional matching is not proof of functional "
  "equivalence."),
 confidence="D",
 key_refs=[
  ref("chu2026", "Two stem-like populations in the human pubertal resting zone; the PTHLH-negative root population maps to Prrx1+ mouse cells that trace clonally"),
  ref("avijgan2025", "Independent human spatial transcriptomics identifying CHRDL2+/SFRP5+ resting zone sub-populations"),
 ],
 open_questions=["g_l2stem_001", "g_l2stem_004"],
 contradicts=["pthrp_positive_resting_chondrocyte"],
 pending_source="chu2026",
))

# ------------------------------------------------------------------ 7
w(dict(
 id="human_resting_zone_chondrocyte",
 name="Human resting zone chondrocyte",
 type="cell_type",
 summary=(
  "What is actually known about human resting zone chondrocytes comes from two 2025-2026 "
  "studies on rare surgical specimens, because human growth plate tissue is otherwise "
  "inaccessible and lineage tracing is impossible. Spatially resolved transcriptomics of "
  "healthy adolescent biopsies produced zonal marker sets and showed that a subset of resting "
  "chondrocytes is functionally quiescent in vivo - predominantly nuclear mRNA, abundant "
  "heterochromatin, and the ability to exit G0 under defined ex vivo conditions - and resolved "
  "overlapping sub-populations in which CHRDL2+ and/or SFRP5+ cells are among the least "
  "quiescent. Independently, single-cell plus spatial analysis of early pubertal plates "
  "resolved two stem-like resting populations, one of which is PTHLH-negative. Disease genes "
  "map onto zones: NKX3-2, SGMS2 and WNK4 expression is restricted to specific human growth "
  "plate zones. None of this establishes self-renewal, clonal output, or lifespan of any human "
  "resting cell; those remain formally untested and, by current methods, untestable in vivo."),
 quantitative=[],
 localization=[
  "human RZ: confirmed by spatial transcriptomics of adolescent biopsies (avijgan2025)",
  "human RZ: confirmed by single-cell plus spatial transcriptomics of pubertal specimens (chu2026)",
 ],
 human_evidence="direct",
 human_evidence_note=(
  "Direct molecular and histological characterisation of human growth plate biopsies from "
  "healthy adolescents and from growth-restricting surgery; functional stem-cell assays absent."),
 species_basis=["human"],
 translation_risk="not_applicable",
 translation_risk_reason="The node is defined on human tissue.",
 confidence="D",
 key_refs=[
  ref("avijgan2025", "Spatial transcriptomics of adolescent human growth plates defines zonal markers and quiescent resting sub-populations"),
  ref("chu2026", "Two stem-like resting zone populations in human pubertal growth plate, one PTHLH-negative"),
  ref("avijgan2026", "Systematic review documenting how little of resting-zone quiescence has been measured rather than assumed"),
 ],
 open_questions=["g_l2stem_001", "g_l2stem_005", "g_l2stem_009"],
))

# ------------------------------------------------------------------ 8
w(dict(
 id="chondroprogenitor_quiescence",
 name="Chondroprogenitor quiescence",
 type="process",
 summary=(
  "Resting zone chondrocytes have been called quiescent since the 1930s, but the term has been "
  "carried on morphology. Where quiescence has been measured, it is real but shallow: 6.1% of "
  "PTHrP+ resting chondrocytes are EdU+ over a short pulse versus 30.5% of proliferative "
  "chondrocytes, and the durably label-retaining fraction plateaus at 2.6% of Col2a1-lineage "
  "cells with a decay half-life near one week - so most 'resting' cells are cycling slowly, "
  "not arrested. Quiescence is actively imposed rather than passive: resting chondrocytes are "
  "held in a Wnt-inhibitory environment and forcing beta-catenin activity expels them from the "
  "zone; ADGRG6/GPR126 signalling through IHH is required to maintain the slow-cycling state; "
  "and growth hormone shrinks the slow-cycling pool by driving differentiation. A 2026 PRISMA "
  "systematic review of every study using 'quiescen*' for resting chondrocytes concluded that, "
  "relative to well-characterised quiescent stem cells elsewhere, molecular and functional "
  "characterisation here is thin and definitions are inconsistent - so 'quiescent resting "
  "zone' should be treated as a partially validated claim, not an established fact."),
 quantitative=[
  dict(parameter="Resting-to-proliferative EdU incorporation ratio at P9", value="0.20",
       unit="ratio (6.1% / 30.5%)", conditions="mouse distal femur, PTHrP-mCherry reporter",
       species="mouse", source_ref="mizuhashi2018", uncertainty="derived from means; SDs 2.3 and 3.2, n=3"),
  dict(parameter="Durably label-retaining chondrocyte fraction", value="2.6", unit="%",
       conditions="Tet-Off H2B-EGFP chase, mouse", species="mouse", source_ref="hallett2021",
       uncertainty="SE 0.9"),
 ],
 localization=[
  "mouse RZ: confirmed by EdU pulse and H2B-EGFP label retention (mizuhashi2018, hallett2021)",
  "human RZ: indirect, nuclear-retained mRNA and heterochromatin in a subset (avijgan2025)",
 ],
 human_evidence="indirect",
 human_evidence_note=(
  "Human quiescence evidence is transcriptomic and ultrastructural in fixed biopsies; no "
  "proliferation kinetics have been measured in living human growth plate."),
 species_basis=["mouse", "human"],
 translation_risk="high",
 translation_risk_reason=(
  "Cycling rates are measured with nucleoside pulses and transgenic pulse-chase in mice; human "
  "growth plate proliferation indices are cross-sectional immunostaining at best."),
 confidence="C",
 key_refs=[
  ref("avijgan2026", "Systematic review: quiescence of resting chondrocytes is under-measured and inconsistently defined"),
  ref("hallett2021", "Quantifies the slow-cycling fraction and shows Wnt inhibition maintains it"),
  ref("bian2024", "ADGRG6 loss depletes slow-cycling resting zone cells and disorganises the plate"),
  ref("chu2025", "Growth hormone reduces the slow-cycling label-retaining pool"),
 ],
 open_questions=["g_l2stem_005"],
))

# ------------------------------------------------------------------ 9
w(dict(
 id="monoclonal_column_formation",
 name="Monoclonal column formation in the growth plate",
 aliases=["clonal column", "chondrocyte column clonality"],
 type="process",
 summary=(
  "A chondrocyte column is the unit of longitudinal growth, and whether a column is a clone is "
  "the operational test of resting-zone stemness. In mouse, PTHrP-creER;Confetti labelling "
  "gives columns each marked by a single colour, and PTHrP-creER-labelled cells first make "
  "short columns (<10 cells, peaking at P18) then long columns (>10 cells, appearing at P18 "
  "and increasing to P36), with the number of labelled columns falling until about 6 months of "
  "chase and then plateauing. Multicolour clonal tracing independently showed a switch: during "
  "fetal and neonatal growth, progenitors are consumed and columns are polyclonal or transient, "
  "whereas later in life large stable monoclonal columns appear, with progenitors adopting "
  "symmetric division and expressing stem cell markers. Dlx5-creER-labelled proliferative and "
  "hypertrophic chondrocytes make only short columns that disappear, confirming that column "
  "founders live above the proliferative zone. Hedgehog and mTORC1 signalling set the size of "
  "the self-renewing pool. No human column has ever been shown to be clonal."),
 quantitative=[
  dict(parameter="Short columns (<10 cells) from PTHrP-creER P6 pulse, peak", value="P18",
       unit="postnatal day of peak", conditions="mouse distal femur", species="mouse",
       source_ref="mizuhashi2018", uncertainty="qualitative peak from time course"),
  dict(parameter="Duration over which labelled resting cells keep generating columns",
       value=">=12", unit="months", conditions="single tamoxifen pulse at P6, mouse",
       species="mouse", source_ref="mizuhashi2018", uncertainty="column number plateaus after ~6 months"),
 ],
 localization=[
  "mouse PZ columns: confirmed clonal by Confetti (mizuhashi2018) and by multicolour clonal tracing (newton2019)",
  "human PZ columns: unconfirmed - clonality cannot be assayed",
 ],
 human_evidence="absent",
 human_evidence_note="Column clonality in humans has never been measured; no method exists to do so in vivo.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason=(
  "Clonality is defined by multicolour Cre reporters. Human columns are morphologically similar "
  "but their clonal structure is unknown, and the mouse clonal switch is tied to a postnatal "
  "window that has no verified human equivalent."),
 confidence="C",
 key_refs=[
  ref("mizuhashi2018", "Confetti labelling shows single-colour columns arising from individual PTHrP+ resting chondrocytes"),
  ref("newton2019", "Clonal tracing reveals a switch from progenitor depletion to large stable monoclonal columns after SOC formation"),
  ref("snippert2010", "Origin of the multicolour Confetti clonal-tracing logic used to call columns clonal"),
 ],
 open_questions=["g_l2stem_003", "g_l2stem_010", "g_l2stem_011"],
))

# ------------------------------------------------------------------ 10
w(dict(
 id="clonal_lineage_tracing",
 name="Clonal lineage tracing (genetic fate mapping)",
 type="method",
 summary=(
  "Nearly every claim in this layer is a claim about a tamoxifen-inducible Cre driver crossed "
  "to a reporter. The method's resolution is set by three parameters that are frequently "
  "unreported: labelling efficiency, driver specificity, and clonal density. In the growth "
  "plate literature these are sometimes quantified - FoxA2-creER labelled 8%, 23% or 38% of "
  "FoxA2+ cells depending on tamoxifen dose and reporter allele copy number, and PTHrP-creER "
  "preferentially marks an immature CD105-low subset of PTHrP-mCherry+ cells rather than all "
  "of them - which means a negative tracing result can be a labelling failure and a "
  "'population' can be an artefact of driver bias. Multicolour reporters (Confetti, Rainbow) "
  "convert fate mapping into clonal analysis by making neighbouring clones distinguishable. "
  "Dual-recombinase (Cre plus Dre) systems allow intersectional labelling and were needed to "
  "show that osteoblast origin switches from chondrocytes to LepR+ stroma at adolescence. The "
  "decisive limitation for this atlas is that none of this can be applied to humans: germline "
  "transgenesis and tamoxifen pulse-chase are not available, so human stem-cell identity in the "
  "growth plate is method-blocked rather than merely unstudied."),
 quantitative=[
  dict(parameter="FoxA2-creER labelling efficiency, two tamoxifen doses", value="8",
       unit="% of FoxA2+ cells", conditions="P14-P15 tamoxifen, one floxed reporter allele, mouse",
       species="mouse", source_ref="muruganandan2022", uncertainty="7.92 +/- 0.9 cells labelled of 97.67 +/- 9"),
  dict(parameter="FoxA2-creER labelling efficiency, five doses plus two reporter alleles",
       value="38", unit="% of FoxA2+ cells", conditions="P14-P18 tamoxifen, mouse", species="mouse",
       source_ref="muruganandan2022", uncertainty="36.9 +/- 2.3 cells labelled"),
 ],
 localization=["not_applicable SYS: methodological node"],
 human_evidence="absent",
 human_evidence_note=(
  "Genetic fate mapping requires engineered alleles and cannot be performed in humans; human "
  "clonal inference would require somatic mutation phylogenies from growth plate tissue, which "
  "has not been reported."),
 species_basis=["mouse"],
 translation_risk="not_applicable",
 translation_risk_reason="Methodological node; the translation problem is the method's inapplicability to humans, captured in gap g_l2stem_001.",
 confidence="C",
 key_refs=[
  ref("muruganandan2022", "Reports labelling efficiency explicitly across tamoxifen doses and reporter allele copy number"),
  ref("mizuhashi2018", "Shows PTHrP-creER marks a biased, immature subset of PTHrP-mCherry+ cells"),
  ref("rinkevich2011", "Rainbow multicolour clonal fate mapping establishing lineage restriction in skeletal repair"),
 ],
 open_questions=["g_l2stem_001", "g_l2stem_011"],
))

# ------------------------------------------------------------------ 11
w(dict(
 id="confetti_reporter",
 name="Confetti / Rainbow multicolour clonal reporters",
 aliases=["R26R-Confetti", "Brainbow-2.1", "Rainbow reporter"],
 type="method",
 summary=(
  "Confetti (Brainbow-2.1 knocked into Rosa26) stochastically recombines to one of four "
  "fluorophores (nuclear GFP, YFP, RFP, membrane CFP), so adjacent clones acquire different "
  "colours and a monochromatic structure can be read as clonal. It was introduced to show that "
  "intestinal crypts drift to clonality through neutral competition among symmetrically "
  "dividing Lgr5+ cells, and the same neutral-drift logic is what makes a single-coloured "
  "chondrocyte column interpretable. In the growth plate, PTHrP-creER;Confetti gave columns of "
  "one colour each, and Col2a1-creER;Confetti supported the same conclusion. The Rainbow "
  "reporter serves the same purpose in the Weissman-lab skeletal work. The critical caveats are "
  "that colour identity is only informative at low labelling density, that recombination "
  "frequencies of the four cassettes are unequal, and that a shared colour between neighbours "
  "is not proof of common ancestry - none of these are usually quantified in growth plate "
  "papers, which is why clonality claims here sit at confidence C rather than higher."),
 quantitative=[],
 localization=["not_applicable SYS: methodological node"],
 human_evidence="absent",
 human_evidence_note="Multicolour genetic reporters cannot be used in humans.",
 species_basis=["mouse"],
 translation_risk="not_applicable",
 translation_risk_reason="Methodological node with no human application.",
 confidence="C",
 key_refs=[
  ref("snippert2010", "Introduces the Confetti reporter and the neutral-drift framework for reading clonality from colour"),
  ref("mizuhashi2018", "Applies Confetti to the growth plate to show single-colour columns"),
  ref("rinkevich2011", "Rainbow reporter application to skeletal clonal analysis"),
 ],
 open_questions=["g_l2stem_010"],
))
