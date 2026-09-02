import yaml, os
D='atlas/nodes/L6_mechanobiology'
def w(n):
    n.setdefault('layer','L6'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    yaml.safe_dump(n,open(os.path.join(D,n['id']+'.yaml'),'w'),sort_keys=False,width=100,allow_unicode=True)
    print('wrote',n['id'])

w(dict(id='physeal_stress_in_vivo', name='In vivo physeal stress', type='process',
aliases=['growth plate stress in vivo','physeal loading magnitude'],
summary=("Every quantitative claim in this layer is expressed per MPa of applied stress, and the value of that stress in a living human has never been "
 "measured. The animal stress-growth experiments impose known stress with an external apparatus, over a range of roughly 0.02-0.2 MPa, chosen for "
 "instrument convenience rather than because it matches physiological loading. The only human-facing numbers come from modelling: personalised finite "
 "element models of four human distal femoral epiphyses driven by instrumented gait analysis show that stress across the physis is markedly "
 "heterogeneous and geometry-dependent, that a tension-band plate imposes local static stress and abolishes cyclic loading at its insertion, and that "
 "tensile stress rises on the opposite side - but the authors are explicit that their models are not fully participant-specific in geometry and "
 "loading, so absolute values should not be quoted as measurements. Related FE work shows growth plate shape itself adapts to the local mechanical "
 "environment, so the geometry that determines stress is not a fixed input. Direct measurement is method-blocked: an implanted pressure transducer "
 "across a healthy child's physis is not ethically available, and the alternatives (MRI-based strain mapping, dual-fluoroscopy kinematics driving "
 "subject-specific models validated against cadaveric measurement) have not been applied to a paediatric physis. This is the single largest missing "
 "number in the layer, because without it the animal sensitivity coefficient cannot be converted into a human prediction."),
quantitative=[
 dict(parameter='applied stress range in the animal stress-growth experiments', value='approximately 0.02-0.2', unit='MPa', conditions='external loading apparatus, rat/rabbit/calf caudal vertebrae and proximal tibiae', species='multiple', source_ref='stokes2006', uncertainty='inferred from the reported protocol; chosen for apparatus, not physiology'),
 dict(parameter='in vivo human physeal stress during gait', value='not measured', unit='MPa', conditions='no direct measurement located in any age group', species='human', source_ref='hucke2023', uncertainty='FE model output only, explicitly stated by the authors as not fully participant-specific'),
],
localization=['human distal femoral physis: modelled only (hucke2023)','animal physes under external apparatus: applied stress known by design'],
human_evidence='absent',
human_evidence_note='No in vivo human physeal stress measurement exists; the only human values are finite-element estimates whose authors caution against treating them as measurements.',
species_basis=['human','multiple'], translation_risk='high',
translation_risk_reason='The entire clinical use of the Hueter-Volkmann coefficient depends on assuming that human physeal stress falls in the range the animal experiments probed, an assumption that has never been checked.',
confidence='D',
key_refs=[
 dict(ref_id='hucke2023', pmid='37415789', first_author='Hucke L', year=2023, type='primary', one_line_finding='Personalised FE models of human distal femoral epiphyses show heterogeneous, geometry-dependent physeal stress and implant-induced static loading'),
 dict(ref_id='stokes2006', pmid='16705695', first_author='Stokes IA', year=2006, type='primary', one_line_finding='Defines the applied-stress range over which the growth sensitivity coefficient was established'),
 dict(ref_id='rodrguez2025', pmid='40475877', first_author='Rodriguez DQ', year=2025, type='primary', one_line_finding='Growth plate geometry, which determines stress distribution, itself adapts to the mechanical environment'),
],
open_questions=['g_l6mech_003','g_l6mech_001']))
