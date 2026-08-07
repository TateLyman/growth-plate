import yaml, os
D='atlas/nodes/L6_mechanobiology'
def w(n):
    n.setdefault('layer','L6'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    yaml.safe_dump(n,open(os.path.join(D,n['id']+'.yaml'),'w'),sort_keys=False,width=100,allow_unicode=True)
    print('wrote',n['id'])

w(dict(id='physeal_bar_formation', name='Physeal bar formation', type='phenotype',
aliases=['bony bridge','physeal bridge','partial growth arrest'],
summary=("A physeal bar is a bridge of bone spanning the growth plate that tethers one region while the rest continues to grow, producing angular "
 "deformity, or that arrests growth entirely if extensive. It is the pathological limit case of mechanical tethering: the bar imposes an internal, "
 "self-generated tension band. Human incidence after physeal fracture is uncertain and probably higher than textbooks state - a prospective cohort of "
 "332 children found growth arrest in 30.1% overall, against up to 5.5% in the prior literature, with 86% after distal femoral physeal fractures, "
 "older age and initial displacement associated with arrest; the authors caution that diagnostic criteria for arrest vary and the true figure may be "
 "lower. Physeal fractures themselves account for 18-30% of all paediatric fractures. Mechanistically, a reproducible mouse distal femoral drill-hole "
 "model shows bone tissue accumulating in the defect over 42 days and identifies the cellular source: Pdgfra- and Pdgfrb-lineage cells, absent from the "
 "plate before injury, migrate into the defect and contribute to the bar. This makes the bar a repair response by perivascular/mesenchymal populations "
 "rather than transdifferentiation of resident chondrocytes."),
quantitative=[
 dict(parameter='growth arrest incidence after paediatric physeal fracture', value='30.1', unit='%', conditions='prospective cohort, 332 children, >=6 months follow-up or arrest within 6 months', species='human', source_ref='hooper2024', uncertainty='authors note diagnostic-criterion variation; prior literature reports up to 5.5%'),
 dict(parameter='growth arrest incidence after distal femoral physeal fracture', value='86', unit='%', conditions='same cohort', species='human', source_ref='hooper2024', uncertainty='highest of all sites; small subgroup'),
 dict(parameter='mean age, growth arrest vs no arrest', value='12.8 vs 9.4', unit='years', conditions='same cohort', species='human', source_ref='hooper2024', uncertainty='displacement 59.0% vs 47.8%, angulation 47.0% vs 38.8%'),
 dict(parameter='physeal fractures as a share of all paediatric fractures', value='18-30', unit='%', conditions='literature range quoted in the same study', species='human', source_ref='hooper2024', uncertainty='range across sources'),
 dict(parameter='time course of bony bar accumulation after drill-hole injury', value='42', unit='days of progressive bone formation', conditions='mouse distal femoral drill-hole model, micro-CT and histology, 5-point grading', species='mouse', source_ref='li2026', uncertainty='progressive increase; endpoint value not extracted'),
],
localization=['human distal femoral physis: highest arrest rate (hooper2024)','mouse distal femoral physis: Pdgfra and Pdgfrb lineage cells within the bar (li2026)'],
human_evidence='direct',
human_evidence_note='Human incidence and risk factors are measured prospectively; the cellular mechanism is mouse only.',
species_basis=['human','mouse'], translation_risk='moderate',
translation_risk_reason='Incidence data are human; the Pdgfra/Pdgfrb lineage attribution rests on mouse reporter lines with no human counterpart.',
confidence='B',
key_refs=[
 dict(ref_id='hooper2024', pmid='38792486', first_author='Hooper N', year=2024, type='primary', one_line_finding='Growth arrest occurred in 30.1% of 332 prospectively followed physeal fractures and 86% of distal femoral fractures'),
 dict(ref_id='li2026', pmid='41883142', first_author='Li Z', year=2026, type='primary', one_line_finding='Pdgfra and Pdgfrb lineage cells, absent from the uninjured plate, migrate in and build the bony bar in a mouse drill-hole model'),
],
open_questions=['g_l6mech_012']))

w(dict(id='blount_disease', name='Blount disease (tibia vara)', type='phenotype',
summary=("Blount disease is progressive varus of the proximal tibia caused by growth suppression of the posteromedial proximal tibial physis, and it is "
 "the standard human illustration of the Hueter-Volkmann law running away with itself: varus alignment shifts load medially, medial compression "
 "suppresses medial growth, and the resulting deformity increases the medial load - a mechanical positive feedback identical in form to the scoliosis "
 "vicious cycle. Its epidemiology fits the mechanical account: obesity is the dominant risk factor and early walking is a recognised association, both "
 "of which raise medial compartment compressive stress in a child whose physis is still soft. Treatment is itself a mechanical experiment in the "
 "opposite direction - lateral tension band plating or transphyseal screw hemiepiphysiodesis restores growth symmetry - but Blount is the setting in "
 "which guided growth performs worst, with lower correction rates and more failures than idiopathic genu varum, and late-onset disease in heavy "
 "adolescents frequently requires osteotomy instead. That failure is informative: it implies the compressive stress in a heavy varus knee exceeds the "
 "range in which the physis remains modulable, or that the medial physis is already partly bridged. No study has measured the medial physeal stress in "
 "a child with Blount disease."),
quantitative=[],
localization=['human posteromedial proximal tibial physis: the site of suppressed growth'],
human_evidence='direct',
human_evidence_note='Human clinical entity with radiographic natural history and surgical outcome data; the mechanical cause is inferred from risk factors and response to unloading, never measured.',
species_basis=['human'], translation_risk='not_applicable',
translation_risk_reason='Human phenotype.',
confidence='B',
key_refs=[
 dict(ref_id='coskun2026', pmid='41178588', first_author='Coskun E', year=2026, type='primary', one_line_finding='Guided growth outcomes in juvenile and adolescent Blount disease, showing lower success than in idiopathic deformity'),
 dict(ref_id='tolk2026', pmid='41696355', first_author='Tolk JJ', year=2026, type='primary', one_line_finding='Non-idiopathic aetiologies including varus deformity correct more slowly and less completely than idiopathic ones'),
 dict(ref_id='stokes2006', pmid='16705695', first_author='Stokes IA', year=2006, type='primary', one_line_finding='Supplies the stress-growth coefficient on which the mechanical account of tibia vara depends'),
],
open_questions=['g_l6mech_003','g_l6mech_012']))

w(dict(id='scoliosis_vertebral_growth', name='Scoliosis and vertebral growth modulation', type='phenotype',
summary=("Adolescent idiopathic scoliosis is the largest natural human experiment in physeal mechanobiology, through the 'vicious cycle' hypothesis: a "
 "pre-existing lateral curve makes muscular and gravitational loading asymmetric across vertebral endplate physes, asymmetric loading modulates "
 "vertebral growth by Hueter-Volkmann, the vertebra wedges, and the curve worsens. The hypothesis has been tested quantitatively rather than merely "
 "asserted - a frontal-plane mathematical simulation using the measured animal stress-growth sensitivity reproduced observed rates of curve "
 "progression, giving quantitative data consistent with the cycle. The animal counterpart is direct: sustained compression and distraction across rat "
 "and calf tail vertebrae produce wedging and altered growth exactly as required. Two caveats sit on the human side. Vertebral wedging in the animal "
 "model arises from both asymmetric growth and remodelling, not growth alone. And clinical growth modulation shows the relation is not a simple "
 "monotone function of applied load: in kyphotic swine, high tether tension gave 53% growth modulation versus -1% for low tension at 2 weeks, but by "
 "2-4 weeks the two were indistinguishable (14% vs 10%), so the tension benefit is transient and modulation becomes load-independent. Human vertebral "
 "body tethering works, but no human study has measured the stress across a vertebral endplate physis."),
quantitative=[
 dict(parameter='growth modulation, high vs low tether tension at 2 weeks', value='53 vs -1', unit='%', conditions='single-level posterior vertebral body tethering, kyphotic swine model', species='porcine', source_ref='halanski2026', uncertainty='SD 43 and 15; p=0.03 vs low tension, p=0.01 vs non-operative control'),
 dict(parameter='growth modulation, high vs low tether tension at 2-4 weeks', value='14 vs 10', unit='%', conditions='same animals', species='porcine', source_ref='halanski2026', uncertainty='SD 11 and 10; p=0.6'),
 dict(parameter='growth-rate sensitivity used to simulate curve progression', value='15.0', unit='% per 0.1 MPa (vertebral plates)', conditions='animal-derived coefficient applied to a human frontal-plane model', species='multiple', source_ref='stokes2006', uncertainty='the human application is an extrapolation'),
],
localization=['human vertebral endplate physes: the presumed site, never directly instrumented','rat and calf caudal vertebral physes: measured (stokes2006)','porcine thoracic vertebrae: measured (halanski2026)'],
human_evidence='indirect',
human_evidence_note='Human evidence is the observed correlation between curve magnitude, remaining growth and progression, plus the success of tethering; the mechanical step is modelled from animal coefficients.',
species_basis=['human','rat','bovine','porcine'], translation_risk='moderate',
translation_risk_reason='The phenomenon is human and the treatment works in humans, but the quantitative mechanism is imported wholesale from quadruped tail vertebrae.',
confidence='B',
key_refs=[
 dict(ref_id='stokes2006a', pmid='17049077', first_author='Stokes IA', year=2006, type='review', one_line_finding='A frontal-plane simulation using the measured stress-growth coefficient reproduces observed scoliosis progression rates'),
 dict(ref_id='halanski2026', pmid='40836185', first_author='Halanski MA', year=2026, type='primary', one_line_finding='Tether tension effects on vertebral growth modulation are large early and vanish by 4 weeks, i.e. biphasic and transient'),
 dict(ref_id='aronsson2011', pmid='21173627', first_author='Aronsson DD', year=2011, type='review', one_line_finding='Reviews non-fusion growth modulation for adolescent scoliosis as a Hueter-Volkmann application'),
 dict(ref_id='chen2025a', pmid='40714837', first_author='Chen F', year=2025, type='primary', one_line_finding='Compression-driven PIEZO1-GPX4 ferroptosis in vertebral growth plate chondrocytes accelerates scoliosis in mice and is druggable'),
 dict(ref_id='stokes2006', pmid='16705695', first_author='Stokes IA', year=2006, type='primary', one_line_finding='Supplies the vertebral stress-growth sensitivity of 15%/0.1 MPa used in the simulation'),
],
open_questions=['g_l6mech_003','g_l6mech_001']))
