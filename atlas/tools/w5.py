import yaml, os
D='atlas/nodes/L6_mechanobiology'
def w(n):
    n.setdefault('layer','L6'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    yaml.safe_dump(n,open(os.path.join(D,n['id']+'.yaml'),'w'),sort_keys=False,width=100,allow_unicode=True)
    print('wrote',n['id'])

w(dict(id='integrin_beta1_chondrocyte', name='Integrin beta-1 (ITGB1) in growth plate chondrocytes', type='protein',
aliases=['ITGB1','beta1 integrin','CD29'],
summary=("Integrin beta-1 is the growth plate's principal cell-matrix adhesion receptor and, unusually for this layer, its growth-plate function "
 "has been tested directly rather than borrowed from articular cartilage. Live time-lapse confocal imaging of mouse cranial base explants with "
 "conditional Itgb1 deletion shows that column formation fails: the 90-degree rotation by which a daughter chondrocyte aligns with the long axis "
 "of the bone is integrin beta-1-driven. Conditional deletion of the cell-cell adhesion molecule Cdh2 (N-cadherin) also disrupts column formation, "
 "but the compound mutant resolves the hierarchy - defective rotation in the N-cadherin mutant is rescued by heterozygous loss of Itgb1, so "
 "N-cadherin acts as a negative regulator of integrin beta-1 rather than as a parallel driver. Because a column is the structural unit of "
 "longitudinal growth, this places integrin beta-1 upstream of growth plate architecture itself. Integrin beta-1 is also a load-transducing "
 "receptor: mechanical loading of chondrocytes activates beta-1 integrins and FGFR, and the two target distinct, non-overlapping mechano-response "
 "gene sets. The integrin's ligand environment is itself mechanically tuned, since the chondron pericellular matrix through which load reaches the "
 "cell surface is built and remodelled in a mechanoresponsive way. No human growth plate integrin beta-1 perturbation data exist."),
quantitative=[],
localization=['mouse cranial base and long bone growth plate chondrocytes: confirmed by conditional deletion (greer2024)','human growth plate: not tested'],
human_evidence='absent',
human_evidence_note='All functional data are mouse conditional knockouts and cell culture; no human physeal integrin beta-1 study located.',
species_basis=['mouse','in_vitro_animal_cell'], translation_risk='high',
translation_risk_reason='Conditional deletion in mouse cartilage cannot be replicated in humans and the column-rotation assay has no human counterpart.',
confidence='C',
key_refs=[
 dict(ref_id='greer2024', pmid='38294852', first_author='Greer SE', year=2024, type='primary', one_line_finding='Integrin beta-1, not N-cadherin, drives the chondrocyte rotation that builds growth plate columns; N-cadherin negatively regulates it'),
 dict(ref_id='dietmar2025', pmid='40379111', first_author='Dietmar HF', year=2025, type='primary', one_line_finding='Load-activated beta-1 integrins and FGFR target distinct chondrocyte mechano-response gene sets'),
 dict(ref_id='lee2025', pmid='40315311', first_author='Lee D', year=2025, type='primary', one_line_finding='The chondron pericellular matrix that transmits load to the chondrocyte surface is itself mechanoresponsive during development'),
],
open_questions=['g_l6mech_008']))

w(dict(id='focal_adhesion_kinase', name='Focal adhesion kinase (FAK/PTK2)', type='protein', aliases=['FAK','PTK2'],
summary=("FAK is the obligatory kinase downstream of integrin engagement and is therefore the assumed transducer converting growth plate matrix strain "
 "into intracellular signalling. The assumption is not backed by a growth-plate experiment. The direct skeletal mechanotransduction evidence for FAK "
 "is in osteocytes, where mechanosensitive FAK together with phosphodiesterase 8A sets intracellular cAMP in response to load. In cartilage, cyclic "
 "tensile stress restores chondrocyte homeostasis through an integrin-FAK-RhoA/ROCK2 axis, but that work is in articular chondrocytes, and "
 "integrin-beta1/FAK/Akt signalling supports chondrogenic activity in human chondrocyte culture rather than in a physis. No conditional Ptk2 deletion "
 "in a chondrocyte Cre line with a longitudinal growth readout has been located, and there is no zonal FAK localisation in human or animal growth "
 "plate. FAK is included here as a mechanistically necessary but experimentally unvalidated node, and its confidence reflects that: the inference "
 "runs from integrin beta-1's demonstrated growth plate role, not from FAK data."),
quantitative=[],
localization=['osteocytes: functional mechanotransduction evidence','articular chondrocytes: functional evidence via integrin-FAK-RhoA/ROCK2','growth plate, any species: no zonal localisation located'],
human_evidence='absent', human_evidence_note='No human growth plate FAK data; human evidence is limited to cultured chondrocytes.',
species_basis=['mouse','in_vitro_human_cell'], translation_risk='unknown',
translation_risk_reason='The node is an inference from integrin biology; without a growth plate experiment in any species the translation question cannot yet be posed properly.',
confidence='E',
key_refs=[
 dict(ref_id='dietmar2025', pmid='40379111', first_author='Dietmar HF', year=2025, type='primary', one_line_finding='Establishes that beta-1 integrin engagement is a genuine load-transduction route in chondrocytes, the premise on which the FAK inference rests'),
 dict(ref_id='greer2024', pmid='38294852', first_author='Greer SE', year=2024, type='primary', one_line_finding='Demonstrates the growth plate function of the integrin beta-1 receptor upstream of FAK'),
],
open_questions=['g_l6mech_008']))

w(dict(id='yap_taz_chondrocyte', name='YAP/TAZ in growth plate chondrocytes', type='protein', aliases=['YAP1','WWTR1','TAZ','Hippo effectors'],
summary=("YAP and TAZ are the canonical stiffness- and tension-responsive transcriptional co-activators, shuttling to the nucleus when cytoskeletal "
 "tension is high. In skeletal tissue their best-documented in vivo mechanoregulatory role is not in the chondrocyte: YAP and TAZ in osteoblast "
 "precursors couple precursor mobilisation to angiogenesis and mechanoregulation during murine bone development. Within the endochondral lineage, "
 "Yap/Taz orchestrate chondrocyte differentiation fate in fibrocartilage, and substrate stiffness modulates hypertrophic chondrocyte reversion in "
 "culture, but neither establishes a load-dependent YAP/TAZ function in a growth plate. The one mechanically explicit endochondral result is from "
 "distraction osteogenesis, where cyclic distraction-compression promotes bone regeneration through a Piezo1-YAP-beta-catenin axis - a regenerate, "
 "not a physis. There is no chondrocyte-specific Yap1/Wwtr1 deletion with a physeal loading challenge and a growth-rate readout, and no human "
 "growth plate YAP/TAZ localisation. This node is therefore held at low confidence deliberately: the pathway is highly plausible and widely "
 "asserted for the growth plate, and the specific experiment has not been done."),
quantitative=[],
localization=['mouse osteoblast precursors: functional mechanoregulatory evidence','mouse fibrocartilage chondrocytes: differentiation-fate evidence','growth plate zones, any species: no load-dependent localisation located','human growth plate: no data located'],
human_evidence='absent', human_evidence_note='No human growth plate YAP/TAZ data located.',
species_basis=['mouse','in_vitro_animal_cell'], translation_risk='unknown',
translation_risk_reason='The growth plate role is extrapolated from osteoblast, fibrocartilage and regenerate biology; the enabling experiment has not been performed in any species.',
confidence='E',
key_refs=[
 dict(ref_id='chen2025a', pmid='40714837', first_author='Chen F', year=2025, type='primary', one_line_finding='Provides the closest growth plate mechanotransduction cascade (PIEZO1-GPX4) into which YAP/TAZ is usually inserted without direct evidence'),
 dict(ref_id='lee2025', pmid='40315311', first_author='Lee D', year=2025, type='primary', one_line_finding='Shows the pericellular matrix stiffness environment through which YAP/TAZ would be expected to act in the growth plate'),
],
open_questions=['g_l6mech_008','g_l6mech_009']))

w(dict(id='cytoskeletal_tension_chondrocyte', name='Chondrocyte cytoskeletal tension', type='process',
summary=("Cytoskeletal tension is the proximate variable that most mechanotransduction models assume the chondrocyte actually reads. In the growth plate "
 "there is one hard structural result: the actin- and adhesion-dependent 90-degree rotation of daughter chondrocytes that builds a column is driven "
 "by integrin beta-1 and antagonised by N-cadherin, so cytoskeletal force generation is directly responsible for growth plate architecture rather "
 "than merely reporting on it. The complementary measurement is deformation rather than force: hypertrophic chondrocytes in stress-controlled explant "
 "compression accumulate lateral and volumetric strain under static but not dynamic loading at the same mean stress and the same axial strain, "
 "showing that the cell's mechanical state is set by the viscoelastic history of the matrix, not by instantaneous load. The chondron pericellular "
 "matrix that mediates this is itself built mechanoresponsively. Beyond this, the F-actin/RhoA/ROCK evidence in cartilage comes from articular "
 "chondrocytes and dedifferentiation studies, and no measurement of actual cytoskeletal tension (traction force, FRET tension sensor) has been made "
 "in a growth plate chondrocyte in any species."),
quantitative=[
 dict(parameter='lateral and volumetric hypertrophic chondrocyte strain, static vs dynamic compression', value='higher under static', unit='p<0.001 lateral, p<=0.015 volumetric', conditions='stress-controlled compression, pre-pubertal rat proximal tibial growth plate explants, axial strain equal between conditions', species='rat', source_ref='zimmermann2017', uncertainty='confocal cell tracking; absolute strains not reported here'),
],
localization=['mouse growth plate proliferative zone: adhesion-dependent rotation confirmed (greer2024)','rat hypertrophic zone: cell strain measured (zimmermann2017)','human growth plate: no data'],
human_evidence='absent', human_evidence_note='No human growth plate cytoskeletal or cell-strain measurement located.',
species_basis=['mouse','rat'], translation_risk='high',
translation_risk_reason='Explant and conditional-knockout data only; no human tissue is available for live cell-mechanics measurement.',
confidence='D',
key_refs=[
 dict(ref_id='greer2024', pmid='38294852', first_author='Greer SE', year=2024, type='primary', one_line_finding='Adhesion-driven chondrocyte rotation, an actively force-generating process, builds growth plate columns'),
 dict(ref_id='zimmermann2017', pmid='28365062', first_author='Zimmermann EA', year=2017, type='primary', one_line_finding='Hypertrophic chondrocyte lateral and volumetric strain depends on loading waveform, not mean stress'),
 dict(ref_id='lee2025', pmid='40315311', first_author='Lee D', year=2025, type='primary', one_line_finding='The chondron pericellular matrix transmitting load to the chondrocyte is mechanoresponsively assembled'),
],
open_questions=['g_l6mech_008']))

w(dict(id='primary_cilium_mechanosensing', name='Primary cilium mechanosensing in the growth plate', type='process',
summary=("The primary cilium is the one mechanosensory organelle with a clean, loading-controlled growth plate experiment. Cartilage-specific inducible "
 "deletion of Ift88 (AggrecanCreERT2;Ift88fl/fl) in juvenile and adolescent mice reduced ciliation and disrupted chondrocyte differentiation, "
 "cartilage resorption and mineralisation - but only in the peripheral tibial regions beneath the load-bearing compartments of the knee, which "
 "accumulated enlarged hypertrophic populations. Hedgehog signalling was preserved, so the defect is not the usual ciliary Hh phenotype; instead "
 "hypertrophic VEGF expression fell, with downstream loss of vascular recruitment, osteoclastic activity and cartilage-to-bone replacement. Two "
 "controls make the mechanical interpretation strong: raising physiological loading in control mice reproduced the impaired peripheral ossification, "
 "and limb immobilisation abolished the Ift88-null phenotype. Separately, PIEZO1 colocalises with the cilium in mouse growth plate chondrocytes and "
 "chloral hydrate cilia disruption (cilia-positive cells 97.2% to 16.6%) or IFT88 knockdown reversed compression-induced cartilage degeneration, "
 "placing the cilium downstream of or in a feedback loop with PIEZO1. All of this is mouse; no human physeal cilium mechanics data exist."),
quantitative=[
 dict(parameter='cilia-positive growth plate chondrocytes before vs after chloral hydrate', value='97.2 -> 16.6', unit='%', conditions='primary mouse growth plate chondrocytes, in vitro', species='mouse', source_ref='chen2025', uncertainty='p<0.001'),
 dict(parameter='disc/plate degeneration score under caudal compression, wild type vs IFT88-cKO', value='12 vs 8', unit='score (baseline 2)', conditions='8-week-old C57BL/6J mice, 10 kPa caudal compression, 8 weeks', species='mouse', source_ref='chen2025', uncertainty='MRI at 4 weeks; n not extracted'),
],
localization=['mouse growth plate chondrocytes, peripheral load-bearing tibial regions: functional evidence (coveney2022)','mouse growth plate chondrocyte cilium, PIEZO1 colocalised: confirmed (chen2025)','human growth plate: no data'],
human_evidence='absent', human_evidence_note='No human growth plate ciliary mechanosensing data; human ciliopathies affect the skeleton but through Hedgehog patterning rather than a demonstrated load pathway.',
species_basis=['mouse'], translation_risk='high',
translation_risk_reason='Requires inducible cartilage-specific gene deletion plus controlled limb loading and immobilisation, none of which is possible in humans.',
confidence='C',
key_refs=[
 dict(ref_id='coveney2022', pmid='35038201', first_author='Coveney CR', year=2022, type='primary', one_line_finding='Ciliary IFT88 protects load-bearing regions of the adolescent growth plate from disruptive physiological force; immobilisation abolishes the phenotype'),
 dict(ref_id='chen2025', pmid='41194970', first_author='Chen F', year=2025, type='primary', one_line_finding='PIEZO1 colocalises with the primary cilium in growth plate chondrocytes and cilia disruption blocks compression-induced degeneration'),
],
open_questions=['g_l6mech_008']))
