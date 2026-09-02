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
 "mizuhashi2018": dict(ref_id="mizuhashi2018", pmid="30401834", doi="10.1038/s41586-018-0662-5", first_author="Mizuhashi K", year=2018, type="primary"),
 "chan2015": dict(ref_id="chan2015", pmid="25594184", doi="10.1016/j.cell.2014.12.002", first_author="Chan CK", year=2015, type="primary"),
 "chan2018": dict(ref_id="chan2018", pmid="30241615", doi="10.1016/j.cell.2018.07.029", first_author="Chan CKF", year=2018, type="primary"),
 "chan2013": dict(ref_id="chan2013", pmid="23858471", doi="10.1073/pnas.1310212110", first_author="Chan CK", year=2013, type="primary_abstract_only"),
 "chan2009": dict(ref_id="chan2009", pmid="19078959", doi="10.1038/nature07547", first_author="Chan CK", year=2009, type="primary_abstract_only"),
 "debnath2018": dict(ref_id="debnath2018", pmid="30250253", doi="10.1038/s41586-018-0554-8", first_author="Debnath S", year=2018, type="primary"),
 "worthley2015": dict(ref_id="worthley2015", pmid="25594183", doi="10.1016/j.cell.2014.11.042", first_author="Worthley DL", year=2015, type="primary"),
 "zhou2014": dict(ref_id="zhou2014", pmid="24953181", doi="10.1016/j.stem.2014.06.008", first_author="Zhou BO", year=2014, type="primary_abstract_only"),
 "omatsu2010": dict(ref_id="omatsu2010", pmid="20850355", doi="10.1016/j.immuni.2010.08.017", first_author="Omatsu Y", year=2010, type="primary_abstract_only"),
 "sacchetti2007": dict(ref_id="sacchetti2007", pmid="17956733", doi="10.1016/j.cell.2007.08.025", first_author="Sacchetti B", year=2007, type="primary_abstract_only"),
 "bianco2015": dict(ref_id="bianco2015", pmid="25758217", doi="10.1242/dev.102210", first_author="Bianco P", year=2015, type="review"),
 "ambrosi2021": dict(ref_id="ambrosi2021", pmid="34381212", doi="10.1038/s41586-021-03795-7", first_author="Ambrosi TH", year=2021, type="primary_abstract_only"),
 "ambrosi2025": dict(ref_id="ambrosi2025", pmid="40118065", doi="10.1016/j.stem.2025.02.013", first_author="Ambrosi TH", year=2025, type="primary_abstract_only"),
 "shu2021": dict(ref_id="shu2021", pmid="34499868", doi="10.1016/j.stem.2021.08.010", first_author="Shu HS", year=2021, type="primary_abstract_only"),
 "kusumbe2014": dict(ref_id="kusumbe2014", pmid="24646994", doi="10.1038/nature13145", first_author="Kusumbe AP", year=2014, type="primary_abstract_only"),
 "carlone2021": dict(ref_id="carlone2021", pmid="33438789", doi="10.1002/stem.3318", first_author="Carlone DL", year=2021, type="primary"),
 "qu2025": dict(ref_id="qu2025", pmid="41253754", doi="10.1038/s41467-025-65029-y", first_author="Qu X", year=2025, type="primary"),
 "mizuhashi2019": dict(ref_id="mizuhashi2019", pmid="30888720", doi="10.1002/jbmr.3719", first_author="Mizuhashi K", year=2019, type="primary_abstract_only"),
 "chu2026": dict(ref_id="chu2026", pmid="41984930", doi="10.1126/scitranslmed.adw3590", first_author="Chu NTL", year=2026, type="primary_abstract_only"),
}
def ref(k, f):
    d = dict(R[k]); d["one_line_finding"] = f; return d

MOUSE_PANEL = "CD45- Ter119- Tie2- AlphaV(CD51)+ Thy(CD90)- 6C3- CD105- CD200+"
HUMAN_PANEL = "CD45- CD235a- TIE2- CD31- PDPN+ CD146- CD73+ CD164+"

# ---------------------------------------------------------------- skeletal_stem_cell
w(dict(
 id="skeletal_stem_cell",
 name="Skeletal stem cell (SSC)",
 aliases=["SSC", "bone-cartilage-stroma stem cell"],
 type="cell_type",
 summary=(
  "'Skeletal stem cell' names an operational result, not a single cell: a cell that "
  "self-renews and generates bone, cartilage and hematopoiesis-supportive stroma in a "
  "transplantation or lineage-tracing assay. At least five mutually incompatible definitions "
  "are in current use - the FACS-defined mouse mSSC hierarchy, PTHrP+/FoxA2+ resting-zone "
  "chondrocytes, Grem1+ osteochondroreticular cells, LepR+ perisinusoidal stroma, and "
  "CTSK-lineage periosteal stem cells - and they disagree on anatomy, markers, adipogenic "
  "potential and developmental window. The disagreements are not semantic. Whether the SSC "
  "makes marrow adipocytes separates the CD146+ adventitial-reticular-cell definition (yes) "
  "from the mSSC/Grem1 definitions (no). Whether the growth plate SSC lies in the resting zone "
  "(mouse tracing) or in the pre-hypertrophic/hypertrophic zone (human FACS/scRNA homology "
  "mapping) is a straight contradiction in anatomy. Dual-recombinase fate mapping showed that "
  "even the dominant osteoblast source changes with age, from chondrocytes before adolescence "
  "to LepR+ stroma after - so 'the' skeletal stem cell is time-dependent as well as "
  "site-dependent. Human work rests on xenotransplantation of prospectively sorted cells, never "
  "on in-situ tracing."),
 quantitative=[],
 localization=[
  "mouse growth plate: mSSC phenotype enriched (chan2015)",
  "mouse metaphysis: Grem1+ OCR cells concentrated, not perisinusoidal (worthley2015)",
  "mouse perisinusoidal marrow: LepR+ stroma (zhou2014)",
  "mouse periosteum: CTSK-lineage PSC (debnath2018)",
  "human fetal pre-hypertrophic/hypertrophic zone: hSSC enriched (chan2018)",
 ],
 human_evidence="indirect",
 human_evidence_note=(
  "Human SSCs are defined by prospective sorting followed by renal-capsule xenotransplantation "
  "in immunodeficient mice; their behaviour in situ in a human skeleton is inferred, not observed."),
 species_basis=["mouse", "human"],
 translation_risk="high",
 translation_risk_reason=(
  "The mouse and human panels share no marker, and mouse assays are in-situ genetic while human "
  "assays are ectopic transplantation - two different questions given the same name."),
 confidence="D",
 key_refs=[
  ref("chan2015", f"Defines mSSC as {MOUSE_PANEL} at the apex of an eight-population hierarchy"),
  ref("chan2018", f"Defines hSSC as {HUMAN_PANEL}, sorted from human fetal growth plate"),
  ref("bianco2015", "Argues the bona fide SSC is the CD146+ marrow adventitial reticular cell, which does make adipocytes"),
  ref("shu2021", "Osteoblast source switches from chondrocytes to LepR+ stroma at adolescence, so no single SSC accounts for postnatal bone"),
 ],
 open_questions=["g_l2stem_004", "g_l2stem_009"],
 contradicts=["mouse_skeletal_stem_cell_hierarchy", "human_skeletal_stem_cell",
              "lepr_positive_stromal_cell", "gremlin1_lineage_cell", "periosteal_stem_cell"],
))

# ---------------------------------------------------------------- mouse hierarchy
w(dict(
 id="mouse_skeletal_stem_cell_hierarchy",
 name="Mouse skeletal stem cell (mSSC) hierarchy",
 aliases=["Chan-Longaker mSSC scheme", "AlphaV+ skeletal hierarchy"],
 type="hypothesis",
 summary=(
  f"Dissociated mouse femoral growth plate was fractionated on CD45, Ter119, Tie2 and AlphaV "
  f"(CD51), and the CD45-Ter119-Tie2-AlphaV+ compartment further split on CD105, Thy (CD90), "
  f"6C3 and CD200 into eight subpopulations. The apex population, {MOUSE_PANEL}, generates all "
  "seven other subpopulations in a linear sequence both in vitro (25-day culture then "
  "re-fractionation) and in vivo (renal capsule transplantation, explanted at one month), and "
  "single sorted cells regenerate the full set including on secondary single-cell replating - "
  "the formal self-renewal plus multipotency test. Its immediate descendants are pre-BCSP "
  "(CD105-CD200-) and BCSP (CD105+). The hierarchy explicitly excludes fat, muscle and "
  "fibroblast output, which is where it collides with the CD146+/MSC literature. Two structural "
  "caveats: transplanted single mSSCs engraft poorly without 5,000 carrier cells, so "
  "'multipotency' is measured in a supported niche; and the same CD200+CD105-Thy-6C3- "
  "immunophenotype is carried by the CTSK-lineage periosteal stem cell, meaning the surface "
  "panel alone does not specify anatomical identity."),
 quantitative=[
  dict(parameter="Subpopulations resolved within the CD45-Ter119-Tie2-AlphaV+ compartment",
       value="8", unit="populations", conditions="mouse long bone, rib and sternum, FACS",
       species="mouse", source_ref="chan2015", uncertainty="not applicable"),
  dict(parameter="Carrier cells co-transplanted with a single mSSC for renal capsule engraftment",
       value="5000", unit="unsorted RFP+ cells", conditions="mouse renal capsule, 2-week explant",
       species="mouse", source_ref="chan2015", uncertainty="not reported"),
  dict(parameter="mSSCs co-expressing BMP2 and BMPR1a", value="28", unit="% of mSSCs",
       conditions="single-cell RNA sequencing, mouse", species="mouse", source_ref="chan2015",
       uncertainty="not reported"),
 ],
 localization=[
  "mouse growth plate: confirmed, high frequency of AlphaV+ cells (chan2015)",
  "mouse fracture callus: confirmed expansion (chan2015)",
  "mouse periosteum: the same CD200+CD105- phenotype is present but Ctsk-lineage (debnath2018)",
 ],
 human_evidence="absent",
 human_evidence_note=(
  "The mouse marker panel does not transfer: the human SSC was defined with an entirely "
  "different set of antigens (PDPN, CD146, CD73, CD164)."),
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason=(
  "6C3 and Thy1.1/1.2 have no directly usable human equivalents in this assay, and CD105 and "
  "CD200 do not partition human skeletal progenitors the same way; the human scheme had to be "
  "built de novo from transcriptional homology."),
 confidence="C",
 key_refs=[
  ref("chan2015", f"Defines the mSSC as {MOUSE_PANEL} and demonstrates single-cell self-renewal and multilineage output"),
  ref("chan2013", "Defines the downstream BCSP as a clonal, lineage-restricted skeletal progenitor"),
  ref("chan2009", "Earlier CD105+Thy1- fetal progenitor that forms ectopic bone and an HSC niche"),
  ref("ambrosi2021", "Aged mSSCs lose osteochondral potential and generate an inflammatory niche"),
 ],
 open_questions=["g_l2stem_004", "g_l2stem_009"],
 contradicts=["human_skeletal_stem_cell", "periosteal_stem_cell", "marrow_stromal_cell"],
))

# ---------------------------------------------------------------- human SSC
w(dict(
 id="human_skeletal_stem_cell",
 name="Human skeletal stem cell (hSSC)",
 aliases=["hSSC", "PDPN+CD146-CD73+CD164+ cell"],
 type="cell_type",
 summary=(
  f"The human SSC is defined as {HUMAN_PANEL}. It was found by Smart-seq2 single-cell "
  "sequencing of seven microdissected regions of a 17-week human fetal femur, scoring each cell "
  "for expression of human orthologues of 76 mSSC/mBCSP-specific genes; the cells scoring "
  "highest were in the second half of the pre-hypertrophic zone and the first half of the "
  "hypertrophic zone - not the resting zone. Sorted hSSCs form ossicles with a marrow cavity "
  "under the renal capsule of NSG mice, self-renew through serial colony formation to tertiary "
  "CFU and through serial transplantation, and generate bone, cartilage and stroma but not fat. "
  "Downstream are a human BCSP, human osteoprogenitors and three chondroprogenitor subsets "
  "distinguished by CD73 and CD164. CD146+ cells, the classic marrow 'MSC', gave smaller and "
  "fewer colonies. hSSCs are present in fetal and adult bone, can be induced from BMP2-treated "
  "adipose stroma and iPSCs, and expand locally after fracture. Across ten skeletal sites the "
  "hSSC pool is compositionally different site by site and shifts toward a fibroblastic state "
  "with age. The translation risk runs in the awkward direction: the human panel and the mouse "
  "panel share no antigen, and the human cell was localised to a different growth plate zone "
  "than the mouse resting-zone stem cell."),
 quantitative=[
  dict(parameter="mSSC/mBCSP-specific genes used to build the human orthologue score", value="76",
       unit="genes", conditions="Gene Expression Commons-derived gene set", species="human",
       source_ref="chan2018", uncertainty="not applicable"),
  dict(parameter="Gestational age of the fetal femur used for hSSC discovery", value="17",
       unit="weeks", conditions="human fetal femur, seven microdissected regions", species="human",
       source_ref="chan2018", uncertainty="single specimen for the discovery scRNA-seq"),
  dict(parameter="hSSCs transplanted for the in vivo serial self-renewal assay", value=">1.5e6",
       unit="DiD-labelled cells", conditions="NSG renal capsule, 2-week primary explant",
       species="human", source_ref="chan2018", uncertainty="not reported"),
  dict(parameter="Distinct human skeletal sites profiled for hSSC composition", value="10",
       unit="anatomical sites", conditions="prospective isolation plus scRNA-seq", species="human",
       source_ref="ambrosi2025", uncertainty="not reported"),
 ],
 localization=[
  "human fetal growth plate pre-hypertrophic (p-H2) and hypertrophic (H1) zones: confirmed by FACS and scRNA-seq (chan2018)",
  "human diaphysis: depleted (chan2018)",
  "human resting zone: unconfirmed - not reported as an hSSC site (chan2018)",
  "human adult bone and fracture site: confirmed, expands after injury (chan2018)",
 ],
 human_evidence="direct",
 human_evidence_note=(
  "Cells were prospectively isolated from human fetal and adult bone and assayed functionally, "
  "but every functional readout required xenotransplantation into immunodeficient mice or "
  "ex vivo culture; no in-situ human assay exists."),
 species_basis=["human", "mouse"],
 translation_risk="high",
 translation_risk_reason=(
  "The reverse translation problem: the hSSC was derived from mouse gene signatures yet shares "
  "no surface marker with the mSSC, was localised to a different growth plate zone than the "
  "mouse resting-zone stem cell, and its behaviour is measured in a mouse kidney rather than in "
  "a human growth plate."),
 confidence="C",
 key_refs=[
  ref("chan2018", f"Defines hSSC as {HUMAN_PANEL}, enriched in the human fetal pre-hypertrophic/hypertrophic zone, self-renewing on serial transplantation"),
  ref("ambrosi2025", "hSSC subtype composition varies across ten skeletal sites and shifts fibroblastic with age"),
  ref("sacchetti2007", "The competing human definition: CD146+ subendothelial stromal cells self-renew and transfer the hematopoietic microenvironment"),
  ref("chu2026", "Human resting zone stem-like cells identified independently, with a different molecular identity"),
 ],
 open_questions=["g_l2stem_004", "g_l2stem_009", "g_l2stem_001"],
 contradicts=["mouse_skeletal_stem_cell_hierarchy", "pthrp_positive_resting_chondrocyte", "marrow_stromal_cell"],
))

# ---------------------------------------------------------------- BCSP
w(dict(
 id="bone_cartilage_stromal_progenitor",
 name="Bone, cartilage and stromal progenitor (BCSP)",
 aliases=["BCSP", "pre-BCSP", "CD105+ skeletal progenitor"],
 type="cell_type",
 summary=(
  "The BCSP is the multipotent but non-self-renewing tier immediately below the mSSC: "
  "CD45-Ter119-Tie2-AlphaV+Thy-6C3-CD105+, with the CD105-CD200- pre-BCSP as an intermediate. "
  "Clonally it produces chondrocytes, osteogenic cells and at least three stromal subsets, but "
  "it does not regenerate the mSSC, which is the operational difference between a progenitor "
  "and a stem cell in this scheme. The earlier CD45-Tie2-AlphaV+CD105+Thy1- fetal population "
  "recruits host vasculature and builds an ectopic ossicle containing a functional long-term "
  "HSC niche when placed under the kidney capsule, which is the origin of the claim that "
  "endochondral ossification is required to construct a marrow niche. In the growth plate, "
  "27.4% of PTHrP-mCherry+ resting chondrocytes carry the BCSP phenotype and 53.4% of BCSPs are "
  "PTHrP-mCherry+, so the immunophenotypic tiers and the anatomical zones cut across each other "
  "rather than nesting cleanly."),
 quantitative=[
  dict(parameter="PTHrP-mCherry+ growth plate cells with BCSP (CD105+) phenotype", value="27.4",
       unit="%", conditions="P9 mouse, CD45-Ter119-CD31-CD51+CD90- gate", species="mouse",
       source_ref="mizuhashi2018", uncertainty="SD 16.5"),
  dict(parameter="BCSPs that are PTHrP-mCherry+", value="53.4", unit="%",
       conditions="P9 mouse growth plate", species="mouse", source_ref="mizuhashi2018",
       uncertainty="SD 16.9"),
  dict(parameter="pre-BCSP fraction of PTHrP-mCherry+ cells", value="23.4", unit="%",
       conditions="P9 mouse growth plate, CD105-CD200- gate", species="mouse",
       source_ref="mizuhashi2018", uncertainty="SD 8.4"),
 ],
 localization=[
  "mouse growth plate and metaphysis: confirmed by FACS (chan2013, mizuhashi2018)",
  "human fetal bone: hBCSP defined as PDPN+CD146-CD73+CD164- (chan2018)",
 ],
 human_evidence="indirect",
 human_evidence_note=(
  "A human BCSP-equivalent tier was defined by surface phenotype and renal-capsule "
  "transplantation, not by in-situ observation."),
 species_basis=["mouse", "human"],
 translation_risk="high",
 translation_risk_reason="Mouse and human BCSP tiers are defined by non-overlapping marker sets and both are assayed ectopically.",
 confidence="C",
 key_refs=[
  ref("chan2013", "Defines the BCSP as a clonal, lineage-restricted bone/cartilage/stroma progenitor"),
  ref("chan2009", "CD105+Thy1- fetal skeletal progenitors build ectopic bone with a functional HSC niche"),
  ref("mizuhashi2018", "Quantifies the overlap between PTHrP+ resting chondrocytes and the mSSC/pre-BCSP/BCSP tiers"),
 ],
 open_questions=["g_l2stem_004"],
))

# ---------------------------------------------------------------- LepR
w(dict(
 id="lepr_positive_stromal_cell",
 name="LepR+ bone marrow stromal cell",
 aliases=["LepR+ MSC", "leptin receptor-expressing stromal cell"],
 type="cell_type",
 summary=(
  "LepR marks roughly 0.3% of mouse bone marrow cells; about 10% of these are CFU-F and they "
  "account for 94% of all marrow CFU-F, making LepR the highest-purity prospective marker for "
  "marrow stroma. LepR+ cells are Scf-GFP+, Cxcl12-DsRed-high and Nestin-GFP-low, and form "
  "bone, cartilage and adipocytes in culture and on transplantation. Their in vivo behaviour is "
  "strongly age-restricted: they contribute little or nothing to developing bone or to growth "
  "plate cartilage, and become the main source of osteoblasts only in adult mice - after "
  "adolescence, according to dual-recombinase fate mapping, where the dominant osteoblast "
  "source switches from chondrocytes to LepR+ stroma and the switch begins in the diaphysis and "
  "spreads to the metaphysis. This is why LepR+ cells cannot be the growth plate stem cell: "
  "they occupy the wrong compartment at the wrong time. Their adipogenic competence also puts "
  "them on the opposite side of the fat-or-no-fat disagreement from the mSSC and Grem1+ "
  "schemes."),
 quantitative=[
  dict(parameter="LepR+ cells in mouse bone marrow", value="0.3", unit="% of bone marrow cells",
       conditions="adult mouse, flow cytometry", species="mouse", source_ref="zhou2014",
       uncertainty="approximate value as reported"),
  dict(parameter="CFU-F frequency within LepR+ cells", value="10", unit="%",
       conditions="adult mouse marrow", species="mouse", source_ref="zhou2014",
       uncertainty="approximate value as reported"),
  dict(parameter="Share of total marrow CFU-F that is LepR+", value="94", unit="%",
       conditions="adult mouse marrow", species="mouse", source_ref="zhou2014",
       uncertainty="approximate value as reported"),
  dict(parameter="Age at which LepR+ cells become the dominant osteoblast source", value="post-adolescent",
       unit="developmental stage", conditions="dual Cre/Dre recombinase fate mapping, mouse",
       species="mouse", source_ref="shu2021", uncertainty="transition begins in diaphysis, spreads to metaphysis"),
 ],
 localization=[
  "mouse perisinusoidal marrow: confirmed by LepR-cre lineage (zhou2014)",
  "mouse growth plate cartilage: absent - LepR+ cells do not contribute to developing chondrocytes (worthley2015 citing zhou2014)",
 ],
 human_evidence="absent",
 human_evidence_note="LepR lineage tracing is impossible in humans; no human LepR+ stromal population has been functionally traced.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="Defined entirely by mouse Cre lineage tracing; the human marrow stromal equivalent is usually assigned to CD146+ cells by a different assay.",
 confidence="C",
 key_refs=[
  ref("zhou2014", "LepR marks 0.3% of marrow cells containing 94% of CFU-F and is the main source of adult bone"),
  ref("shu2021", "Osteoblast origin switches from chondrocytes to LepR+ stroma at adolescence"),
  ref("worthley2015", "Reports that LepR+ perisinusoidal cells never contribute to normal developing chondrocytes"),
 ],
 open_questions=["g_l2stem_004"],
 contradicts=["gremlin1_lineage_cell", "mouse_skeletal_stem_cell_hierarchy"],
))

# ---------------------------------------------------------------- Grem1
w(dict(
 id="gremlin1_lineage_cell",
 name="Grem1+ osteochondroreticular (OCR) stem cell",
 aliases=["OCR stem cell", "Gremlin1 lineage cell"],
 type="cell_type",
 summary=(
  "Grem1-creER labels a population concentrated in the metaphysis immediately adjacent to the "
  "growth plate and trabecular bone, not in the perisinusoidal space. Traced Grem1+ cells "
  "generate columns of chondrocytes by P5, osteoblasts and reticular marrow stroma, self-renew, "
  "and are required for bone development, remodelling and fracture repair - but they do not "
  "make adipocytes (0 of 19 single clones by oil red O; polyclonal cultures also failed). About "
  "40% of Grem1+ cells are CD105+, versus under 2% of Grem1-negative CD45-CD31-Ter119- cells, "
  "and only 5.9% co-express Acta2-RFP. They are explicitly non-overlapping with Nestin-GFP "
  "perisinusoidal MSCs. Two conflicts follow. First, Grem1+ OCR cells and LepR+ stroma disagree "
  "on adipogenic output and on anatomical position for the same claimed role. Second, PTHrP+ "
  "resting chondrocytes do not express Grem1, so the metaphyseal OCR cell and the resting-zone "
  "stem cell are different cells even though both are said to supply growth plate chondrocytes."),
 quantitative=[
  dict(parameter="Grem1+ single clones producing adipocytes", value="0", unit="of 19 clones",
       conditions="oil red O staining, mouse", species="mouse", source_ref="worthley2015",
       uncertainty="polyclonal cultures also negative"),
  dict(parameter="Grem1+ cells that are CD105+", value="40", unit="%",
       conditions="CD45-Ter119-CD31- mouse marrow", species="mouse", source_ref="worthley2015",
       uncertainty="Grem1-negative comparison <2%"),
  dict(parameter="Grem1+ cells co-expressing Acta2-RFP", value="5.9", unit="% (mean)",
       conditions="adult mouse", species="mouse", source_ref="worthley2015", uncertainty="not reported"),
 ],
 localization=[
  "mouse metaphysis adjacent to growth plate and trabecular bone: confirmed (worthley2015)",
  "mouse perisinusoidal space: absent (worthley2015)",
  "mouse resting zone PTHrP+ cells: negative for Grem1 (mizuhashi2018)",
  "mouse periosteum: a subset of CTSK-lineage cells expresses Gremlin1 (debnath2018)",
 ],
 human_evidence="absent",
 human_evidence_note="No human GREM1+ skeletal stem cell has been identified or assayed.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="Entirely dependent on an inducible mouse Cre driver; GREM1 expression in human bone has not been mapped to a functional progenitor.",
 confidence="C",
 key_refs=[
  ref("worthley2015", "Grem1+ metaphyseal OCR stem cells make bone, cartilage and reticular stroma but not fat"),
  ref("mizuhashi2018", "PTHrP+ resting chondrocytes do not express Grem1, separating the two candidate growth plate stem cells"),
  ref("debnath2018", "A subset of periosteal CTSK-lineage cells also expresses Gremlin1, blurring compartment assignment"),
 ],
 open_questions=["g_l2stem_004"],
 contradicts=["lepr_positive_stromal_cell", "pthrp_positive_resting_chondrocyte"],
))

# ---------------------------------------------------------------- CAR
w(dict(
 id="cxcl12_abundant_reticular_cell",
 name="CXCL12-abundant reticular (CAR) cell",
 aliases=["CAR cell", "adipo-osteogenic progenitor"],
 type="cell_type",
 summary=(
  "CAR cells are reticular marrow stromal cells producing high CXCL12 and SCF. Short-term "
  "in vivo ablation of CAR cells does not destroy the candidate niches (bone-lining osteoblasts, "
  "endothelium) but severely impairs the adipogenic and osteogenic differentiation potential of "
  "marrow cells and cuts CXCL12 and SCF production, reducing HSC number and cell size and "
  "driving HSCs into quiescence, with a marked loss of cycling lymphoid and erythroid "
  "progenitors. They are therefore an adipo-osteogenic progenitor and a hematopoietic niche "
  "cell simultaneously. Their relevance to this layer is that they are a documented terminal "
  "destination of growth plate output: PTHrP-creER-labelled resting chondrocyte descendants "
  "leave the plate and become Cxcl12-GFP+ stromal cells beneath the labelled columns, with the "
  "number of double-positive cells rising for the first three months of chase and then "
  "plateauing. CAR cells overlap heavily with LepR+ stroma (LepR+ cells are Cxcl12-DsRed-high), "
  "which is one reason the marrow stromal nomenclature is unresolved."),
 quantitative=[
  dict(parameter="Time to plateau of chondrocyte-derived Cxcl12-GFP+ stromal cells",
       value="3", unit="months of chase", conditions="PTHrP-creER pulsed at P6, mouse",
       species="mouse", source_ref="mizuhashi2018", uncertainty="osteoblast-derived counts fell after the same point"),
 ],
 localization=[
  "mouse marrow reticular network: confirmed (omatsu2010)",
  "mouse primary spongiosa beneath labelled columns: confirmed as chondrocyte-derived (mizuhashi2018)",
 ],
 human_evidence="absent",
 human_evidence_note="CAR cell identity and ablation experiments are murine; no equivalent human population has been functionally defined.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="Depends on conditional ablation in transgenic mice, and human marrow stroma is classified by different markers (CD146, CD271).",
 confidence="C",
 key_refs=[
  ref("omatsu2010", "CAR cells are adipo-osteogenic progenitors whose ablation impairs marrow differentiation potential and HSC maintenance"),
  ref("mizuhashi2018", "Growth plate resting chondrocyte descendants become Cxcl12-GFP+ marrow stromal cells"),
  ref("zhou2014", "LepR+ stromal cells are Cxcl12-DsRed-high, indicating substantial overlap with CAR cells"),
 ],
 open_questions=["g_l2stem_004"],
))

# ---------------------------------------------------------------- PSC
w(dict(
 id="periosteal_stem_cell",
 name="Periosteal stem cell (PSC)",
 aliases=["CTSK-lineage periosteal stem cell", "PSC"],
 type="cell_type",
 summary=(
  "Cathepsin K-cre unexpectedly labels periosteal rather than osteoclastic mesenchyme from "
  "E14.5 onward, and within the CTSK-lineage mesenchymal cells three populations separate on "
  "flow cytometry, all THY- 6C3- CD49f-dim CD51-dim: PSC (CD200+ CD105-), periosteal "
  "progenitor 1 (CD200- CD105-) and periosteal progenitor 2 (CD105+, CD200 variable). PSCs show "
  "clonal multipotency and self-renewal and sit at the apex of this hierarchy; they mediate "
  "intramembranous bone formation, which is the functional distinction from the endosteal "
  "compartment. The uncomfortable observation for the field is that the PSC immunophenotype "
  "(CD200+CD105-Thy-6C3-) is the same as the mSSC immunophenotype - the two are separated by "
  "anatomy and by Ctsk lineage history, not by surface markers. Subsets of CTSK-lineage cells "
  "also express Gremlin1 and Nestin, so three published 'distinct' stem cell schemes intersect "
  "within the periosteum."),
 quantitative=[
  dict(parameter="Earliest embryonic day of periosteal CTSK-mGFP labelling", value="E14.5",
       unit="embryonic day", conditions="Ctsk-cre;mTmG mouse", species="mouse",
       source_ref="debnath2018", uncertainty="not reported"),
  dict(parameter="Populations resolved within CTSK-lineage periosteal mesenchyme", value="3",
       unit="populations", conditions="THY- 6C3- CD49f-dim CD51-dim gate, mouse", species="mouse",
       source_ref="debnath2018", uncertainty="not applicable"),
 ],
 localization=[
  "mouse periosteum of long bones and calvarium: confirmed (debnath2018)",
  "mouse endosteum: separate compartment, physically divided by the cortex (debnath2018)",
  "human periosteum: candidate LRP1+CD13+ population reported separately; not verified here",
 ],
 human_evidence="absent",
 human_evidence_note="The CTSK-lineage definition requires Cre lineage tracing and has no human counterpart in this evidence base.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="Lineage-defined mouse population; in humans CTSK is best known as an osteoclast protease, so the lineage inference does not transfer by expression alone.",
 confidence="C",
 key_refs=[
  ref("debnath2018", "Identifies the CD200+CD105- CTSK-lineage periosteal stem cell and its two-progenitor hierarchy"),
  ref("chan2015", "Defines the mSSC with an overlapping surface phenotype, showing markers alone do not specify compartment"),
 ],
 open_questions=["g_l2stem_004"],
 contradicts=["mouse_skeletal_stem_cell_hierarchy"],
))

# ---------------------------------------------------------------- marrow stromal cell
w(dict(
 id="marrow_stromal_cell",
 name="Bone marrow stromal cell (skeletal 'MSC')",
 aliases=["BMSC", "mesenchymal stem cell", "CD146+ adventitial reticular cell"],
 type="cell_type",
 summary=(
  "This node exists to hold the older, competing definition of the skeletal stem cell. Human "
  "MCAM/CD146-expressing subendothelial cells in marrow stroma, transplanted heterotopically, "
  "self-renew, reconstitute identical subendothelial cells in a miniature bone organ and "
  "transfer the hematopoietic microenvironment - the assay that originally defined a human "
  "skeletal stem cell. In this framework the SSC is a specific perivascular adventitial "
  "reticular cell that also makes marrow adipocytes. That last property is the point of "
  "collision: the mSSC, Grem1+ OCR and hSSC schemes all explicitly exclude adipogenesis, and "
  "the hSSC paper reports that CD146+ cells give smaller and fewer colonies than "
  "PDPN+CD146-CD73+CD164+ cells, while the CD146 school argues that FACS-defined 'MSC' "
  "populations from different tissues are not equivalent and that in vitro phenotype is not "
  "evidence of stemness. The disagreement is unresolved and is logged in "
  "audit/contradictions.md."),
 quantitative=[],
 localization=[
  "human marrow sinusoidal wall (subendothelial/adventitial reticular): confirmed (sacchetti2007)",
  "mouse perisinusoidal marrow: LepR+/Cxcl12-high equivalent (zhou2014)",
 ],
 human_evidence="direct",
 human_evidence_note=(
  "Human CD146+ marrow stromal cells were prospectively isolated and shown to self-renew and "
  "organise a hematopoietic microenvironment, though again only after heterotopic "
  "transplantation into mice."),
 species_basis=["human", "mouse"],
 translation_risk="moderate",
 translation_risk_reason=(
  "The defining experiments were done on human cells, but the readout is ectopic ossicle "
  "formation in a mouse, which does not test the cell's role in a human growth plate."),
 confidence="C",
 key_refs=[
  ref("sacchetti2007", "Human CD146+ subendothelial marrow stromal cells self-renew and transfer the hematopoietic microenvironment"),
  ref("bianco2015", "Sets out the adventitial-reticular-cell definition of the skeletal stem cell against FACS-hierarchy definitions"),
  ref("chan2018", "Reports CD146+ cells as inferior colony formers relative to the proposed hSSC"),
 ],
 open_questions=["g_l2stem_004"],
 contradicts=["human_skeletal_stem_cell", "mouse_skeletal_stem_cell_hierarchy"],
))

# ---------------------------------------------------------------- mTert
w(dict(
 id="mtert_skeletal_progenitor",
 name="mTert+ transitional skeletal progenitor",
 aliases=["telomerase-expressing skeletal progenitor"],
 type="cell_type",
 summary=(
  "Telomerase reverse transcriptase expression is a common, if imperfect, proxy for stem-cell "
  "identity in self-renewing tissues, and mTert-GFP reporter mice show that its expression in "
  "long bone is not constitutive but peaks at the time of adolescent bone growth. mTert-GFP+ "
  "cells sit in the metaphyseal stroma, the growth plate and the marrow, have enriched "
  "colony-forming capacity relative to unsorted cells, and contribute to multiple mesenchymal "
  "lineages - a distinct, transitional skeletal progenitor rather than a lifelong pool. The "
  "temporal restriction matters for the senescence models in this layer: it is consistent with a "
  "growth-associated, self-limiting progenitor compartment rather than a permanently "
  "telomerase-competent stem cell. Whether human growth plate chondrocytes express TERT at any "
  "age is not established (see gap g_l2stem_007)."),
 quantitative=[],
 localization=[
  "mouse metaphyseal stroma, growth plate and bone marrow: confirmed by mTert-GFP (carlone2021)",
  "human growth plate: unconfirmed",
 ],
 human_evidence="absent",
 human_evidence_note="No measurement of TERT expression or telomerase activity in human growth plate chondrocytes was found.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason=(
  "Mouse and human telomere biology differ substantially - laboratory mice have long telomeres "
  "and broader somatic telomerase expression - so a murine mTert reporter is a poor guide to "
  "human chondrocyte replicative limits."),
 confidence="D",
 key_refs=[
  ref("carlone2021", "mTert marks a transitional skeletal progenitor enriched during adolescent bone growth"),
 ],
 open_questions=["g_l2stem_007"],
))

# ---------------------------------------------------------------- vascular coupling
w(dict(
 id="stem_cell_niche_vascular_coupling",
 name="Vascular coupling of the skeletal stem cell niche",
 type="process",
 summary=(
  "Skeletal progenitor behaviour is set in part by a specific vessel type. Type H capillaries "
  "(CD31-high, endomucin-high) in the murine metaphysis are surrounded by osteoprogenitors, "
  "couple angiogenesis to osteogenesis, and decline with age in parallel with bone formation. "
  "This is the vascular arm of the argument that the secondary ossification centre creates the "
  "resting zone niche: the SOC is itself a vascular invasion event, and cartilage canals "
  "carrying vessels precede it. The strongest mechanistic link demonstrated so far is indirect - "
  "in the mSSC scheme, VEGF blockade during BMP2-induced ossicle formation shifts the output "
  "from bone with a marrow cavity to predominantly cartilage, showing that vascular signalling "
  "steers skeletal progenitor fate. What has not been shown is that manipulating the epiphyseal "
  "vasculature specifically changes resting-zone stem cell acquisition, which is the "
  "experiment that would test the SOC hypothesis (gap g_l2stem_003)."),
 quantitative=[],
 localization=[
  "mouse metaphysis: type H vessels confirmed (kusumbe2014)",
  "mouse epiphysis/SOC: vascular invasion precedes SOC formation; niche consequence unconfirmed",
 ],
 human_evidence="absent",
 human_evidence_note="Type H vessel biology and VEGF-blockade fate switching are murine; no human epiphyseal equivalent has been tested functionally.",
 species_basis=["mouse"],
 translation_risk="high",
 translation_risk_reason="Depends on mouse vascular subtype markers and pharmacological blockade in mice; human epiphyseal vascular anatomy differs in timing and canal structure.",
 confidence="C",
 key_refs=[
  ref("kusumbe2014", "Type H capillaries couple angiogenesis to osteogenesis and decline with age in mouse bone"),
  ref("chan2015", "VEGF inhibition during BMP2-induced ossicle formation shifts mSSC output from bone to cartilage"),
  ref("qu2025", "Gli1+ stromal cells are fetal precursors of long-lived cartilage progenitors, linking perichondrial/stromal compartments to the plate"),
 ],
 open_questions=["g_l2stem_003"],
))
