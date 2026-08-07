#!/usr/bin/env python3
import os, yaml
D = "/home/user/growth-plate/atlas/nodes/L2_stem_and_progenitor_biology"
LV = "2026-08-05"

def w(n):
    n.setdefault("layer", "L2"); n.setdefault("stub", False); n.setdefault("last_verified", LV)
    p = os.path.join(D, n["id"] + ".yaml")
    with open(p, "w") as f:
        yaml.safe_dump(n, f, sort_keys=False, default_flow_style=False, width=100, allow_unicode=True)
    print("wrote", p)

R = {
 "zhou2014a": dict(ref_id="zhou2014a", pmid="25474590", doi="10.1371/journal.pgen.1004820", first_author="Zhou X", year=2014, type="primary"),
 "yang2014": dict(ref_id="yang2014", pmid="25092332", doi="10.1073/pnas.1302703111", first_author="Yang L", year=2014, type="primary_abstract_only"),
 "shu2021": dict(ref_id="shu2021", pmid="34499868", doi="10.1016/j.stem.2021.08.010", first_author="Shu HS", year=2021, type="primary_abstract_only"),
 "mizuhashi2018": dict(ref_id="mizuhashi2018", pmid="30401834", doi="10.1038/s41586-018-0662-5", first_author="Mizuhashi K", year=2018, type="primary"),
 "mizuhashi2019": dict(ref_id="mizuhashi2019", pmid="30888720", doi="10.1002/jbmr.3719", first_author="Mizuhashi K", year=2019, type="primary_abstract_only"),
 "newton2019": dict(ref_id="newton2019", pmid="30814736", doi="10.1038/s41586-019-0989-6", first_author="Newton PT", year=2019, type="primary_abstract_only"),
 "schrier2006": dict(ref_id="schrier2006", pmid="16614378", doi="10.1677/joe.1.06489", first_author="Schrier L", year=2006, type="primary_abstract_only"),
 "nilsson2005": dict(ref_id="nilsson2005", pmid="16002553", doi="10.1677/joe.1.06016", first_author="Nilsson O", year=2005, type="primary_abstract_only"),
 "nilsson2004": dict(ref_id="nilsson2004", pmid="15380808", doi="10.1016/j.tem.2004.08.004", first_author="Nilsson O", year=2004, type="review"),
 "gafni2001": dict(ref_id="gafni2001", pmid="11641457", doi="10.1203/00006450-200111000-00014", first_author="Gafni RI", year=2001, type="primary_abstract_only"),
 "marino2008": dict(ref_id="marino2008", pmid="18174286", doi="10.1210/en.2007-0993", first_author="Marino R", year=2008, type="primary_abstract_only"),
 "baron1994": dict(ref_id="baron1994", pmid="7925098", doi="10.1210/endo.135.4.7925098", first_author="Baron J", year=1994, type="primary_abstract_only"),
 "tanner1963": dict(ref_id="tanner1963", pmid="14079891", doi="10.1038/199845a0", first_author="Tanner JM", year=1963, type="review"),
 "lui2011": dict(ref_id="lui2011", pmid="21865751", doi="10.1159/000328117", first_author="Lui JC", year=2011, type="review"),
 "emons2011": dict(ref_id="emons2011", pmid="21540578", doi="10.1159/000327788", first_author="Emons J", year=2011, type="review"),
 "wit2002": dict(ref_id="wit2002", pmid="12510974", first_author="Wit JM", year=2002, type="review"),
 "chu2025": dict(ref_id="chu2025", pmid="41289405", doi="10.1073/pnas.2512316122", first_author="Chu NTL", year=2025, type="primary"),
 "chu2026": dict(ref_id="chu2026", pmid="41984930", doi="10.1126/scitranslmed.adw3590", first_author="Chu NTL", year=2026, type="primary_abstract_only"),
 "hallett2021": dict(ref_id="hallett2021", pmid="34309509", doi="10.7554/elife.64513", first_author="Hallett SA", year=2021, type="primary"),
 "muruganandan2022": dict(ref_id="muruganandan2022", pmid="35523895", doi="10.1038/s41467-022-30247-1", first_author="Muruganandan S", year=2022, type="primary"),
 "ambrosi2021": dict(ref_id="ambrosi2021", pmid="34381212", doi="10.1038/s41586-021-03795-7", first_author="Ambrosi TH", year=2021, type="primary_abstract_only"),
 "carlone2021": dict(ref_id="carlone2021", pmid="33438789", doi="10.1002/stem.3318", first_author="Carlone DL", year=2021, type="primary"),
 "horike2026": dict(ref_id="horike2026", pmid="41748604", doi="10.1038/s41467-026-69507-9", first_author="Horike N", year=2026, type="primary"),
 "trompet2024": dict(ref_id="trompet2024", pmid="38516888", doi="10.1172/jci.insight.165226", first_author="Trompet D", year=2024, type="primary"),
 "chan2018": dict(ref_id="chan2018", pmid="30241615", doi="10.1016/j.cell.2018.07.029", first_author="Chan CKF", year=2018, type="primary"),
 "avijgan2025": dict(ref_id="avijgan2025", doi="10.1101/2025.03.12.642613", first_author="Avijgan M", year=2025, type="preprint"),
}
def ref(k, f):
    d = dict(R[k]); d["one_line_finding"] = f; return d

# ------------------------------------------------------- transdifferentiation
w(dict(
 id="chondrocyte_to_osteoblast_transdifferentiation",
 name="Chondrocyte-to-osteoblast transdifferentiation",
 aliases=["chondrocyte-derived osteoblast", "cartilage-to-bone lineage continuum"],
 type="process",
 summary=(
  "A century-old question was settled in mice in 2014 by two independent groups using different "
  "drivers. With Col10a1-Cre (constitutive, hypertrophic-chondrocyte-specific) and Agc1-CreERT2 "
  "(tamoxifen-inducible, chondrocyte-specific), neither of which labels perichondrium, "
  "periosteum or any osteoblast-lineage cell at induction, labelled descendants appear as "
  "osteocalcin-positive, 2.3kb-Col1a1-GFP-positive osteoblasts on trabecular surfaces and "
  "endosteum and as embedded osteocytes. The magnitude is large: about 63% of trabecular "
  "osteocalcin+ cells and 62% of endosteal osteocalcin+ cells were chondrocyte-derived in "
  "one-month-old mice, and about 60% of trabecular and 68% of endosteal Col1-GFP+ osteoblasts "
  "in three-week-old mice. Independent work using inducible recombination showed the same cells "
  "survive the cartilage-to-bone transition and persist into adulthood. Dual-recombinase fate "
  "mapping later added the temporal boundary: chondrocytes are the main osteoblast source only "
  "before adolescence, after which LepR+ marrow stroma takes over, starting in the diaphysis. "
  "The residual controversy is quantitative and technical rather than existential - the authors "
  "themselves flag that 60% could be an overestimate if Col10a1-Cre had any ectopic activity, "
  "and Cre-driver specificity is the standing objection. No human measurement of this fraction "
  "exists."),
 quantitative=[
  dict(parameter="Trabecular osteocalcin+ osteoblasts derived from hypertrophic chondrocytes",
       value="63", unit="% of Ocn+ cells", conditions="1-month-old Col10a1-Cre;Osx-flox mouse femur, double IF",
       species="mouse", source_ref="zhou2014a", uncertainty="approximate value; n=4 mice, per-sample sums over trabecular images"),
  dict(parameter="Endosteal osteocalcin+ osteoblasts derived from hypertrophic chondrocytes",
       value="62", unit="% of Ocn+ cells", conditions="1-month-old mouse femur endosteum",
       species="mouse", source_ref="zhou2014a", uncertainty="approximate value; n=3 mice"),
  dict(parameter="Trabecular Col1a1(2.3kb)-GFP+ osteoblasts that are chondrocyte-derived",
       value="60", unit="% of EGFP+ cells", conditions="3-week-old Col10a1-Cre;2.3col1-GFP;ROSA-tdTomato mouse",
       species="mouse", source_ref="zhou2014a", uncertainty="approximate value"),
  dict(parameter="Endosteal Col1a1(2.3kb)-GFP+ osteoblasts that are chondrocyte-derived",
       value="68", unit="% of EGFP+ cells", conditions="3-week-old triple transgenic mouse femur",
       species="mouse", source_ref="zhou2014a", uncertainty="approximate value"),
  dict(parameter="Developmental window in which chondrocytes are the dominant osteoblast source",
       value="birth to adolescence", unit="developmental stage",
       conditions="dual Cre/Dre recombinase fate mapping, mouse", species="mouse",
       source_ref="shu2021", uncertainty="transition spreads diaphysis to metaphysis"),
 ],
 localization=[
  "mouse primary spongiosa, trabeculae and endosteum: confirmed by two independent Cre systems (zhou2014a, yang2014)",
  "mouse fracture callus: confirmed (zhou2014a)",
  "human: unconfirmed - no lineage-resolving method available",
 ],
 human_evidence="absent",
 human_evidence_note=(
  "The fraction of human osteoblasts derived from hypertrophic chondrocytes has never been "
  "measured; the process is inferred in humans purely by analogy with mouse."),
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason=(
  "The measurement requires irreversible genetic labelling of a transient cell state. Humans "
  "also differ in the relevant window - human growth plates fuse, mouse plates do not - so even "
  "the developmental boundary reported by dual-recombinase tracing has no direct human analogue."),
 confidence="C",
 key_refs=[
  ref("zhou2014a", "~60-63% of trabecular and endosteal osteoblasts in 3-4 week mice derive from Col10a1+ hypertrophic chondrocytes"),
  ref("yang2014", "Independent inducible tracing shows hypertrophic chondrocytes survive the transition and become osteoblasts and osteocytes persisting into adulthood"),
  ref("shu2021", "Chondrocyte-derived osteoblasts dominate only before adolescence; LepR+ stroma takes over afterwards"),
  ref("mizuhashi2018", "PTHrP+ resting chondrocyte descendants become Col1a1-GFP+ osteoblasts and Cxcl12-GFP+ stroma, linking the resting zone to this output"),
 ],
 open_questions=["g_l2stem_002"],
))

# ------------------------------------------------------- hypertrophic chondrocyte survival
w(dict(
 id="hypertrophic_chondrocyte_survival",
 name="Hypertrophic chondrocyte survival at the chondro-osseous junction",
 type="process",
 summary=(
  "The classical model has terminal hypertrophic chondrocytes dying, with osteoblasts arriving "
  "from the perichondrium with the invading vasculature. Inducible lineage tracing overturned "
  "the exclusivity of that model: a substantial fraction of hypertrophic chondrocytes survive "
  "the cartilage-to-bone transition, downregulate the chondrocyte programme and become "
  "osteogenic cells that persist into adulthood. The two fates therefore coexist and their "
  "relative weights are the interesting quantity - roughly 60% of young mouse trabecular "
  "osteoblasts are chondrocyte-derived, so survival is not a rare escape event. Cells at the "
  "growth plate periphery behave differently again: borderline chondrocytes, aligned "
  "perpendicular to the columns adjacent to the perichondrium, behave as transient mesenchymal "
  "precursors rather than long-term stem cells. The mechanism licensing survival is not settled; "
  "candidate regulators reported in the mouse include Wnt/beta-catenin and mechanotransductive "
  "signalling, and none has been tested in human tissue."),
 quantitative=[
  dict(parameter="Lower bound on hypertrophic chondrocyte survival, inferred from osteoblast output",
       value="60", unit="% of young trabecular osteoblasts are chondrocyte-derived",
       conditions="3-4 week mouse femur", species="mouse", source_ref="zhou2014a",
       uncertainty="approximate; not a direct survival measurement"),
 ],
 localization=[
  "mouse chondro-osseous junction and primary spongiosa: confirmed (yang2014, zhou2014a)",
  "mouse growth plate periphery (borderline chondrocytes): transient precursor behaviour (mizuhashi2019)",
  "human: unconfirmed",
 ],
 human_evidence="absent",
 human_evidence_note="No human study has traced the fate of individual hypertrophic chondrocytes.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="Depends on inducible genetic labelling; human hypertrophic chondrocyte fate is inferred entirely by analogy.",
 confidence="C",
 key_refs=[
  ref("yang2014", "Hypertrophic chondrocytes survive the cartilage-to-bone transition and become osteoblasts and osteocytes"),
  ref("zhou2014a", "Quantifies the resulting osteoblast contribution at ~60%"),
  ref("mizuhashi2019", "Borderline chondrocytes at the plate periphery are transient mesenchymal precursors, not stem cells"),
 ],
 open_questions=["g_l2stem_002"],
))

# ------------------------------------------------------- apoptosis
w(dict(
 id="chondrocyte_apoptosis_hz",
 name="Hypertrophic zone chondrocyte apoptosis",
 type="process",
 summary=(
  "Apoptosis of terminal hypertrophic chondrocytes is the textbook mechanism by which cartilage "
  "is vacated for vascular invasion and bone deposition, and it remains a real fate. What has "
  "changed is its exclusivity: since inducible lineage tracing showed that a large fraction of "
  "hypertrophic chondrocytes survive and become osteoblasts, apoptosis can no longer be treated "
  "as the default fate of all hypertrophic cells. The two fates now have to be partitioned, and "
  "that partition has not been measured directly in any species - the surviving fraction is "
  "inferred from downstream osteoblast labelling (about 60% of young mouse trabecular "
  "osteoblasts) rather than counted at the junction. This is a genuine quantitative hole rather "
  "than a settled number, and it is flagged as gap g_l2stem_002 in its human form. For this "
  "layer the relevant consequence is that hypertrophic chondrocyte death is not a mechanism of "
  "stem cell loss: the resting zone is upstream and is depleted by differentiation, not by "
  "apoptosis at the far end of the plate."),
 quantitative=[],
 localization=[
  "mouse terminal hypertrophic zone and zone of provisional calcification: classical site",
  "human hypertrophic zone: histologically described; fate partition unmeasured",
 ],
 human_evidence="absent",
 human_evidence_note="No human data partition hypertrophic chondrocyte fate between apoptosis and survival.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="The competing fate (survival/transdifferentiation) is measurable only by genetic tracing, so the human balance between death and survival is unknown.",
 confidence="D",
 key_refs=[
  ref("yang2014", "Demonstrates that death is not the obligate fate of terminal hypertrophic chondrocytes"),
  ref("zhou2014a", "Quantifies the surviving lineage's osteoblast output, bounding the non-apoptotic fraction"),
 ],
 open_questions=["g_l2stem_002"],
))

# ------------------------------------------------------- SOC hypothesis
w(dict(
 id="soc_formation_triggers_stemness",
 name="Hypothesis: secondary ossification centre formation triggers resting-zone stem cell acquisition",
 aliases=["SOC-niche hypothesis"],
 type="hypothesis",
 summary=(
  "The claim is that resting-zone chondrocytes are not stem cells from the outset but acquire "
  "self-renewal when the secondary ossification centre forms, which in mouse is roughly the "
  "second postnatal week. The evidence is entirely temporal coincidence in two mouse studies. "
  "First, PTHrP-mCherry+ resting chondrocytes appear at P3 and expand sharply between P6 and "
  "P9, and PTHrP-creER colony-forming cells acquire robust in vitro self-renewal between a P9 "
  "pulse (17/518, 3.3% secondary colonies, none passageable) and a P12 pulse (16/98, 16.3% "
  "secondary colonies, 2/16 passageable nine times) - the authors describe this as occurring "
  "'when the secondary ossification centre actively develops'. Second, multicolour clonal "
  "tracing found that fetal and neonatal growth depletes chondroprogenitors whereas later "
  "growth produces large stable monoclonal columns with symmetric division and stem cell marker "
  "expression, 'coinciding with the formation of the secondary ossification centre'. Neither "
  "study manipulated the SOC. A targeted Europe PMC search for any experiment that ablates, "
  "blocks, prevents or delays SOC formation and then assays resting-zone stemness returned zero "
  "records (see search log for g_l2stem_003). The hypothesis is therefore correlational in one "
  "species. It is load-bearing for fusion models in L7 and should be cited as a hypothesis, not "
  "a mechanism."),
 quantitative=[
  dict(parameter="Secondary colony formation from PTHrP-creER cells pulsed at P9 (pre-SOC)",
       value="3.3", unit="% (17/518 clones)", conditions="mouse ex vivo colony assay",
       species="mouse", source_ref="mizuhashi2018", uncertainty="none survived further passage"),
  dict(parameter="Secondary colony formation from PTHrP-creER cells pulsed at P12 (SOC developing)",
       value="16.3", unit="% (16/98 clones)", conditions="mouse ex vivo colony assay",
       species="mouse", source_ref="mizuhashi2018", uncertainty="2/16 passaged >=9 generations"),
  dict(parameter="Causal experiments manipulating SOC formation and assaying RZ stemness",
       value="0", unit="studies retrieved", conditions="Europe PMC, 2026-08-05, query in search log g_l2stem_003",
       species="not_applicable", source_ref="mizuhashi2018", uncertainty="null result of a literature search, not a measurement",
       value_unverified=True),
 ],
 localization=["mouse RZ/SOC interface: temporal association only"],
 human_evidence="absent",
 human_evidence_note=(
  "Human SOC timing is well described radiographically and varies by bone (distal femur around "
  "term, others through childhood), but no human study has related SOC appearance to any "
  "property of resting zone cells."),
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason=(
  "Two mouse studies with coincident timing; humans form SOCs at bone-specific times over years, "
  "which would predict staggered, bone-by-bone acquisition of resting-zone stemness - a "
  "prediction nobody has tested."),
 confidence="D",
 key_refs=[
  ref("mizuhashi2018", "In vitro self-renewability of PTHrP+ colony-forming cells rises between P9 and P12, described as coinciding with active SOC development"),
  ref("newton2019", "Clonal switch from progenitor depletion to stable monoclonal columns is reported as coinciding with SOC formation"),
  ref("muruganandan2022", "FoxA2+ long-term stem cells sit precisely at the cartilage/SOC interface, consistent with but not demonstrating an SOC-derived niche"),
 ],
 open_questions=["g_l2stem_003", "g_l2stem_011"],
 contradicts=["finite_proliferative_capacity_model"],
))

# ------------------------------------------------------- RZ depletion causes fusion
w(dict(
 id="rz_depletion_causes_fusion",
 name="Hypothesis: resting zone stem cell depletion causes epiphyseal fusion",
 type="hypothesis",
 summary=(
  "Two readings of the same correlation compete. In the causal reading, resting zone progenitors "
  "have a finite proliferative capacity; when it is exhausted, chondrocyte production stops and "
  "the plate is resorbed and bridged by bone. In the consequence reading, fusion is an "
  "independently triggered event - in humans, an oestrogen-driven one - that terminates the "
  "plate while proliferative capacity may still remain, so the observed depletion at fusion is "
  "an endpoint, not a cause. Supporting the causal reading: in rabbit, resting-zone chondrocyte "
  "proliferation rate and cell number per unit area both fall with age, and growth-inhibiting "
  "treatments that slow resting-cell proliferation slow senescence. Against it: growth plate "
  "senescence in rodents proceeds to near-cessation without fusion at all, so depletion is "
  "clearly not sufficient for fusion in every mammal; and oestrogen accelerates senescence while "
  "simultaneously slowing resting-zone proliferation, which is the opposite of what a pure "
  "proliferation-consumption model predicts. What discriminates: measure resting-zone cell "
  "number and proliferative capacity in human or rabbit plates at matched chronological age with "
  "and without oestrogen exposure. If depletion causes fusion, plates that fuse early under "
  "oestrogen must be more depleted at the moment of fusion; if fusion is imposed, they will fuse "
  "while less depleted than age-matched controls."),
 quantitative=[],
 localization=["rabbit RZ: age-related numerical depletion measured (schrier2006)",
               "human RZ: unmeasured across the fusion transition"],
 human_evidence="absent",
 human_evidence_note=(
  "No study has quantified human resting zone cell number or proliferative capacity across the "
  "fusion transition; human evidence about fusion timing is radiographic and endocrine."),
 species_basis=["rabbit", "rat", "mouse"],
 translation_risk="high",
 translation_risk_reason=(
  "Rodents do not fuse, so the species in which senescence is best measured cannot exhibit the "
  "outcome being explained; rabbits fuse but have not been examined with modern clonal tools."),
 confidence="E",
 key_refs=[
  ref("schrier2006", "Rabbit resting zone chondrocytes decline in proliferation rate and number with age; glucocorticoid slows both"),
  ref("nilsson2004", "States the depletion-then-fusion sequence as the field's working model"),
  ref("emons2011", "Emphasises that rodents senesce without fusing, separating the two events"),
  ref("newton2019", "Clonal tracing showing postnatal acquisition of self-renewal, which weakens a simple monotonic depletion account"),
 ],
 open_questions=["g_l2stem_006", "g_l2stem_005"],
 contradicts=["finite_proliferative_capacity_model"],
))

# ------------------------------------------------------- clonal exhaustion
w(dict(
 id="clonal_exhaustion",
 name="Clonal exhaustion of growth plate progenitors",
 type="process",
 summary=(
  "Clonal exhaustion is the loss of individual founder clones from the growth plate over time, "
  "as distinct from a fall in per-cell proliferation. It is directly visible in mouse lineage "
  "tracing: after a single P6 PTHrP-creER pulse the number of labelled columns falls "
  "progressively until about six months of chase and then plateaus, meaning most labelled "
  "founders stop contributing while a minority persist for at least a year. In vitro the same "
  "asymmetry appears as a small tail of long-lived clones - 12.5% of secondary colonies from a "
  "P12 pulse could be passaged nine times, giving roughly 2-3% of PTHrP+ colony-forming cells "
  "with long-term self-renewal, and 9% of FoxA2+ colonies versus 1.4% of PTHrP+ colonies "
  "reaching late passage. Clonal exhaustion therefore behaves like neutral drift with a "
  "surviving minority rather than synchronous failure of a whole compartment. Interventions "
  "that consume the pool accelerate it: growth hormone reduces the slow-cycling label-retaining "
  "population by pushing cells into transit-amplifying differentiation."),
 quantitative=[
  dict(parameter="Time at which labelled column number plateaus after a single P6 pulse",
       value="6", unit="months of chase", conditions="PTHrP-creER;tdTomato mouse", species="mouse",
       source_ref="mizuhashi2018", uncertainty="columns still present at 12 months"),
  dict(parameter="Long-term self-renewing fraction among PTHrP+ colony-forming cells", value="2-3",
       unit="%", conditions="serial passaging of P12-pulse colonies, mouse", species="mouse",
       source_ref="mizuhashi2018", uncertainty="authors' derived estimate"),
  dict(parameter="FoxA2+ colonies surviving to passage 9+ vs PTHrP+ colonies to passage 5",
       value="8.9 vs 1.4", unit="% of colonies", conditions="P18 mouse, parallel assays",
       species="mouse", source_ref="muruganandan2022", uncertainty="10/112 and 2/143 respectively"),
 ],
 localization=["mouse RZ and columns: confirmed by lineage tracing (mizuhashi2018)",
               "human: unmeasurable with current methods"],
 human_evidence="absent",
 human_evidence_note="Clone-level dynamics cannot be observed in human growth plate.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="Clone counting requires genetic labelling; in humans neither the founder number nor the clone lifetime is accessible.",
 confidence="C",
 key_refs=[
  ref("mizuhashi2018", "Labelled column number declines to a plateau, with a small long-lived founder minority"),
  ref("newton2019", "Fetal/neonatal growth depletes progenitors while later growth sustains stable clones"),
  ref("chu2025", "Growth hormone accelerates consumption of the slow-cycling stem pool"),
  ref("muruganandan2022", "Quantifies differing clonal longevity between two resting zone populations"),
 ],
 open_questions=["g_l2stem_010", "g_l2stem_005"],
))

# ------------------------------------------------------- finite proliferative capacity
w(dict(
 id="finite_proliferative_capacity_model",
 name="Finite proliferative capacity model of growth plate lifespan",
 aliases=["proliferative exhaustion model", "Baron-Nilsson senescence model"],
 type="hypothesis",
 summary=(
  "The model states that resting-zone stem-like cells possess a fixed, cell-division-denominated "
  "quantity of proliferative capacity; growth slows as it is spent, and the decline depends on "
  "cumulative divisions rather than chronological age. Its strongest support is that growth "
  "plate senescence is intrinsic and dissociable from age: local glucocorticoid delivered to a "
  "single rabbit growth plate produces catch-up growth confined to that plate, so the "
  "information is stored locally; dexamethasone-suppressed rabbits and propylthiouracil-treated "
  "hypothyroid rats resume growth with plates that are structurally and functionally less "
  "senescent than age-matched controls; and rabbit resting-zone cells decline in both "
  "proliferation rate and number with age. The model's own authors falsified its simplest "
  "molecular version: the number of population doublings of rabbit resting-zone chondrocytes in "
  "culture did not depend on donor age, so the in vivo limit is not a Hayflick limit carried by "
  "the cells. They proposed instead a progressive loss of DNA methylation that tracks slow "
  "in vivo resting-zone proliferation and not rapid proliferative-zone or in vitro division. "
  "The unresolved tension is with clonal tracing showing that mouse progenitors acquire "
  "self-renewal postnatally rather than only spending down a fixed budget."),
 quantitative=[
  dict(parameter="Dependence of rabbit RZ chondrocyte population doublings in vitro on donor age",
       value="none detected", unit="population doublings vs age", conditions="rabbit RZ chondrocytes in culture",
       species="rabbit", source_ref="nilsson2005", uncertainty="reported as no dependence; effect size not given"),
  dict(parameter="Direction of DNA methylation change with growth plate senescence", value="decrease",
       unit="global DNA methylation", conditions="rabbit resting zone chondrocytes in vivo, across age",
       species="rabbit", source_ref="nilsson2005", uncertainty="no change across RZ-to-HZ transition or in vitro"),
 ],
 localization=["rabbit RZ: measured (schrier2006, nilsson2005)",
               "rat growth plate: measured (marino2008)",
               "human growth plate: inferred only"],
 human_evidence="indirect",
 human_evidence_note=(
  "Human support is clinical and inferential - catch-up growth after treatment of hypothyroidism, "
  "Cushing syndrome or coeliac disease is consistent with conserved proliferative capacity - but "
  "no human growth plate proliferative capacity has been measured."),
 species_basis=["rabbit", "rat", "human"],
 translation_risk="moderate",
 translation_risk_reason=(
  "The core phenomenon (local, intrinsic, division-dependent senescence) is replicated across "
  "rabbit and rat and matches human clinical catch-up growth, but the human growth plate has "
  "never been assayed and the proposed molecular carrier (DNA methylation loss) is unverified in "
  "humans."),
 confidence="C",
 key_refs=[
  ref("baron1994", "Local glucocorticoid produces local catch-up growth, establishing that senescence information is intrinsic to the plate"),
  ref("gafni2001", "Catch-up growth after dexamethasone is accompanied by a less senescent rabbit growth plate"),
  ref("schrier2006", "Resting zone chondrocytes are numerically and functionally depleted with age in rabbit"),
  ref("nilsson2005", "Refutes the in vitro Hayflick version of the model and proposes DNA methylation loss instead"),
  ref("nilsson2004", "Canonical statement of the model and its link to fusion"),
 ],
 open_questions=["g_l2stem_005", "g_l2stem_008", "g_l2stem_006"],
 contradicts=["soc_formation_triggers_stemness", "replicative_senescence_chondrocyte"],
))

# ------------------------------------------------------- growth plate senescence
w(dict(
 id="growth_plate_senescence",
 name="Growth plate senescence",
 aliases=["programmed growth plate senescence", "growth plate maturation"],
 type="process",
 summary=(
  "Growth plate senescence is the coordinated, age-related decline in plate function: falling "
  "chondrocyte proliferation rate, decreasing plate height, fewer resting zone cells per unit "
  "area, reduced hypertrophic cell size and altered matrix - not cellular senescence in the "
  "p16/SASP sense. It is intrinsic and local rather than systemic, demonstrated by local "
  "catch-up growth after local glucocorticoid in rabbit, and it is division-dependent rather "
  "than time-dependent, demonstrated by the conservation of growth potential during "
  "growth-inhibited periods in rabbit and rat. It is molecularly accompanied by progressive loss "
  "of global DNA methylation in resting zone chondrocytes, an effect specific to slow in vivo "
  "resting-zone proliferation. Ageing also acts on the progenitor compartment more broadly: aged "
  "mouse skeletal stem cells lose bone and cartilage potential and produce an inflammatory, "
  "pro-resorptive stroma. The species boundary is critical: rodent plates senesce nearly to "
  "cessation without fusing, so senescence and fusion are separable processes, and human growth "
  "plate senescence has been characterised histologically but never functionally."),
 quantitative=[],
 localization=["rabbit and rat growth plate: measured across age (schrier2006, marino2008)",
               "human growth plate: histological description only"],
 human_evidence="indirect",
 human_evidence_note=(
  "Human evidence is the clinical growth-velocity curve and its response to removing "
  "growth-inhibiting conditions; there are no direct human measurements of plate proliferative "
  "kinetics across age."),
 species_basis=["rabbit", "rat", "mouse", "human"],
 translation_risk="moderate",
 translation_risk_reason=(
  "The phenomenon is cross-species and matches human growth curves, but its endpoint differs: "
  "rodents never fuse, so the terminal phase of human senescence has no faithful model."),
 confidence="B",
 key_refs=[
  ref("schrier2006", "Quantifies age-related decline in rabbit resting zone proliferation and cell number"),
  ref("nilsson2005", "Links senescence to progressive loss of DNA methylation in resting zone chondrocytes"),
  ref("marino2008", "Shows senescence is delayed by a growth-inhibiting condition in rat"),
  ref("ambrosi2021", "Skeletal stem cell ageing produces an inflammatory degenerative niche in mice"),
  ref("emons2011", "Reviews maturation and fusion and stresses the rodent/human species difference"),
 ],
 open_questions=["g_l2stem_005", "g_l2stem_006", "g_l2stem_008"],
))

# ------------------------------------------------------- replicative senescence
w(dict(
 id="replicative_senescence_chondrocyte",
 name="Replicative (Hayflick) senescence of growth plate chondrocytes",
 type="process",
 summary=(
  "The intuitive molecular explanation for a finite proliferative capacity is classical "
  "replicative senescence - a cell-autonomous division counter of the Hayflick type. The "
  "decisive test was done and it failed: rabbit resting zone chondrocytes harvested from young "
  "and old animals achieved the same number of population doublings in culture, so the in vivo "
  "limit is not carried by the cells as a fixed replicative reserve that survives explantation. "
  "The same study found that global DNA methylation declined with in vivo growth plate "
  "senescence but not during rapid proliferation in vitro or across the resting-to-hypertrophic "
  "transition, which argues for an epigenetic timer coupled specifically to slow in vivo "
  "resting-zone division rather than for telomere-driven crisis. This node is therefore a "
  "negative result that is frequently re-asserted as positive in secondary literature; treat "
  "'growth plate chondrocytes undergo replicative senescence' as unsupported in its "
  "cell-autonomous form."),
 quantitative=[
  dict(parameter="Population doublings of cultured rabbit RZ chondrocytes vs donor age",
       value="no dependence", unit="population doublings", conditions="rabbit resting zone chondrocytes in vitro",
       species="rabbit", source_ref="nilsson2005", uncertainty="reported as independent of donor age; no effect size given"),
 ],
 localization=["rabbit RZ chondrocytes in vitro: tested and negative (nilsson2005)",
               "human chondrocytes: untested in growth plate"],
 human_evidence="absent",
 human_evidence_note="No human growth plate chondrocyte replicative-capacity measurement exists.",
 species_basis=["rabbit"],
 translation_risk="high",
 translation_risk_reason=(
  "Rabbit in vitro behaviour, and rodent telomere biology differs markedly from human, so "
  "neither a positive nor a negative rodent result settles the human case."),
 confidence="D",
 key_refs=[
  ref("nilsson2005", "Population doublings of rabbit RZ chondrocytes in culture are independent of donor age, arguing against cell-autonomous replicative senescence"),
  ref("nilsson2004", "Contextualises the finite-capacity model that this negative result constrains"),
 ],
 open_questions=["g_l2stem_007", "g_l2stem_008"],
 contradicts=["finite_proliferative_capacity_model"],
))

# ------------------------------------------------------- telomere attrition
w(dict(
 id="telomere_attrition_chondrocyte",
 name="Telomere attrition in growth plate chondrocytes",
 type="process",
 summary=(
  "Telomere shortening is the most commonly invoked molecular clock for a finite proliferative "
  "capacity, and it is routinely asserted for the growth plate in review literature. A targeted "
  "Europe PMC search for measurements of telomere length or telomerase activity in human growth "
  "plate or resting-zone chondrocytes as a function of age returned no qualifying primary study "
  "(see search log for g_l2stem_007): the hits are osteoarthritis cartilage, general skeletal "
  "ageing reviews, and rodent work. The nearest positive datum is murine and indirect - "
  "mTert-GFP marks a transitional skeletal progenitor population whose expression peaks during "
  "adolescent bone growth rather than persisting - and the nearest negative datum is that "
  "rabbit resting-zone chondrocyte replicative capacity in vitro does not decline with donor "
  "age, which is hard to reconcile with progressive telomere-driven exhaustion in vivo. Treat "
  "telomere attrition in the growth plate as an untraceable claim in its human form."),
 quantitative=[],
 localization=["human growth plate: no measurement located",
               "mouse growth plate, metaphyseal stroma, marrow: mTert-GFP+ cells present (carlone2021)"],
 human_evidence="absent",
 human_evidence_note="No primary measurement of telomere length or telomerase activity in human growth plate chondrocytes was found.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason=(
  "Laboratory mice have long telomeres and broader somatic telomerase expression than humans, so "
  "murine telomere data are among the least transferable in skeletal biology."),
 confidence="X",
 key_refs=[
  ref("carlone2021", "mTert expression in mouse long bone peaks during adolescent growth and marks a transitional progenitor, not a permanent stem pool"),
  ref("nilsson2005", "Age-independent in vitro replicative capacity of rabbit RZ chondrocytes constrains any telomere-clock account"),
 ],
 open_questions=["g_l2stem_007"],
))

# ------------------------------------------------------- delayed senescence hypothesis
w(dict(
 id="delayed_senescence_hypothesis",
 name="Delayed-senescence explanation of catch-up growth",
 type="hypothesis",
 summary=(
  "The hypothesis: growth-inhibiting conditions suppress resting-zone chondrocyte proliferation, "
  "which conserves the plate's limited proliferative capacity; when the condition resolves the "
  "plate is less senescent than expected for chronological age and therefore grows faster than "
  "age-matched controls. Three separate perturbations support it. Local intra-plate "
  "glucocorticoid in rabbit produces catch-up confined to the treated plate, excluding a "
  "systemic explanation for that experiment. Systemic dexamethasone in rabbits is followed by "
  "catch-up growth with structurally and functionally less senescent plates. Propylthiouracil-"
  "induced hypothyroidism in newborn rats delays the normal progression of plate senescence and "
  "is followed by catch-up. Mechanistically it is supported by the observation that "
  "glucocorticoid slows resting-zone chondrocyte proliferation and slows their numerical "
  "depletion. Limits: it does not explain catch-up that is not preceded by proliferation "
  "suppression, and it cannot be complete, since local catch-up is measurable but so is a "
  "systemic component in some clinical settings."),
 quantitative=[],
 localization=["rabbit growth plate: measured (baron1994, gafni2001, schrier2006)",
               "rat growth plate: measured (marino2008)"],
 human_evidence="indirect",
 human_evidence_note=(
  "Human catch-up growth after treatment of hypothyroidism, glucocorticoid excess or coeliac "
  "disease is consistent with the model, but no human growth plate has been examined for delayed "
  "senescence."),
 species_basis=["rabbit", "rat"],
 translation_risk="moderate",
 translation_risk_reason=(
  "Replicated across two species with two different growth-inhibiting mechanisms and matching "
  "human clinical phenomenology, but the histological readout has never been obtained in humans."),
 confidence="B",
 key_refs=[
  ref("baron1994", "Local glucocorticoid to one growth plate yields local catch-up, excluding a purely central mechanism"),
  ref("gafni2001", "Catch-up after dexamethasone accompanied by delayed growth plate senescence in rabbit"),
  ref("marino2008", "Hypothyroidism delays rat growth plate senescence and is followed by catch-up growth"),
  ref("schrier2006", "Glucocorticoid slows resting zone proliferation and numerical depletion, the proposed conserving mechanism"),
 ],
 open_questions=["g_l2stem_005", "g_l2stem_008"],
 contradicts=["neuroendocrine_catchup_hypothesis"],
))

# ------------------------------------------------------- neuroendocrine hypothesis
w(dict(
 id="neuroendocrine_catchup_hypothesis",
 name="Neuroendocrine ('sizostat') explanation of catch-up growth",
 type="hypothesis",
 summary=(
  "The older explanation, proposed in 1963, is that the central nervous system compares actual "
  "body size with an age-appropriate set point and adjusts growth rate through a circulating "
  "factor; after a period of growth restriction the deficit is sensed and growth accelerates. "
  "The set point has never been identified experimentally. The decisive evidence against it "
  "being the whole story is that catch-up growth occurs locally: glucocorticoid administered to "
  "a single rabbit growth plate is followed by catch-up restricted to that plate, which a "
  "circulating signal cannot explain. The hypothesis is not dead, only demoted - the local "
  "experiment shows a growth-plate-intrinsic mechanism is sufficient for local catch-up, not "
  "that systemic modulation is absent, and clinical catch-up after nutritional or endocrine "
  "rescue involves unambiguous systemic changes in GH/IGF-1 signalling. On the evidence "
  "reviewed here, the intrinsic delayed-senescence mechanism is supported by direct "
  "experimental data and the neuroendocrine set point is supported by none; the honest position "
  "is that catch-up is at least partly intrinsic and possibly additionally modulated centrally."),
 quantitative=[],
 localization=["not_applicable SYS: systemic hypothesis"],
 human_evidence="indirect",
 human_evidence_note=(
  "Human catch-up growth is well documented clinically, but no human study has demonstrated a "
  "size-sensing set point or its circulating mediator."),
 species_basis=["rabbit", "human"],
 translation_risk="unknown",
 translation_risk_reason=(
  "The mechanism itself is unidentified in any species, so there is no defined entity whose "
  "human relevance could be assessed."),
 confidence="D",
 key_refs=[
  ref("tanner1963", "Original proposal of a central size set-point regulating mammalian growth"),
  ref("baron1994", "Local catch-up growth after local glucocorticoid shows a circulating set-point signal is not required"),
  ref("wit2002", "Reviews definitions and competing models of catch-up growth"),
 ],
 open_questions=["g_l2stem_006"],
 contradicts=["delayed_senescence_hypothesis"],
))

# ------------------------------------------------------- catch-up growth
w(dict(
 id="catch_up_growth",
 name="Catch-up growth",
 type="phenotype",
 summary=(
  "Catch-up growth is a height velocity above the normal range for age sustained for at least a "
  "year following a period of growth inhibition, best expressed as a change in height standard "
  "deviation score rather than as velocity because it must be separated from the pubertal "
  "spurt. It is directly observed in humans after treatment of hypothyroidism, glucocorticoid "
  "excess, coeliac disease and malnutrition, and it may be complete or incomplete. Its "
  "mechanistic significance for this layer is that it is the strongest functional evidence that "
  "the growth plate carries a stored, spendable growth potential: rabbit experiments show that "
  "catch-up can be produced within a single growth plate by local glucocorticoid, and that the "
  "catching-up plate is histologically and functionally less senescent than an age-matched "
  "control. Catch-up growth is therefore evidence FOR the finite-capacity/senescence model - "
  "specifically for its division-dependence rather than for a Hayflick mechanism - and evidence "
  "AGAINST catch-up requiring a central size sensor."),
 quantitative=[
  dict(parameter="Minimum duration of supranormal height velocity conventionally required",
       value="1", unit="year", conditions="clinical definition in children", species="human",
       source_ref="wit2002", uncertainty="convention, not a measurement"),
 ],
 localization=["human SYS: clinically observed", "rabbit growth plate: experimentally produced locally (baron1994)"],
 human_evidence="direct",
 human_evidence_note=(
  "Catch-up growth is a directly measured human clinical phenomenon with an accepted "
  "quantitative definition; only its mechanism is extrapolated from animals."),
 species_basis=["human", "rabbit", "rat"],
 translation_risk="low",
 translation_risk_reason=(
  "The phenotype itself is human-defined and human-measured; the translation risk attaches to "
  "the mechanistic explanation, not to the observation."),
 confidence="A",
 key_refs=[
  ref("wit2002", "Defines catch-up growth quantitatively in children and reviews competing mechanisms"),
  ref("baron1994", "Demonstrates catch-up growth confined to a single locally treated growth plate"),
  ref("gafni2001", "Links catch-up growth to a measurably less senescent growth plate in rabbit"),
  ref("lui2011", "Frames catch-up growth as delayed senescence from conserved replicative capacity"),
 ],
 open_questions=["g_l2stem_005", "g_l2stem_006"],
))
