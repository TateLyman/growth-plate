import yaml, os
D='atlas/nodes/L6_mechanobiology'
def w(n):
    n.setdefault('layer','L6'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    yaml.safe_dump(n,open(os.path.join(D,n['id']+'.yaml'),'w'),sort_keys=False,width=100,allow_unicode=True)
    print('wrote',n['id'])

w(dict(id='mechanical_modulation_growth', name='Mechanical modulation of longitudinal growth', type='process',
summary=("Mechanical modulation is the change in endochondral growth rate produced by an externally imposed stress across a physis, "
 "over and above the growth the plate would have produced unloaded. Its measured magnitude in animals is large: 8 days of sustained "
 "loading changes growth rate by up to 53%, and the response is approximately linear in stress at 17.1% per 0.1 MPa. Two cell-level "
 "levers carry the effect - the number of proliferative chondrocytes generated per column and the final height reached by hypertrophic "
 "chondrocytes - and both are altered in the same direction as growth. Modulation is reversible: after 15 days of 0.2 MPa compression "
 "on rat caudal vertebrae, both growth rate and plate height returned to sham values within 10 days of unloading. Duration matters "
 "independently of magnitude, since halving the daily loading time from 24 h to 12 h roughly halves the growth suppression, and the "
 "response saturates or reverses with time under a fixed displacement, as posterior vertebral tethering in kyphotic swine shows a "
 "53% growth-modulation advantage of high over low tether tension at 2 weeks that has vanished by 4 weeks. In humans the process is "
 "only observed through its surgical exploitation, never measured against a known applied stress."),
quantitative=[
 dict(parameter='maximum growth rate change achieved by sustained loading', value='53', unit='%', conditions='8 days, compression or distraction, rat/rabbit/calf', species='multiple', source_ref='stokes2007', uncertainty='not reported'),
 dict(parameter='time to full recovery of growth rate and plate height after unloading', value='10', unit='days', conditions='after 15 days of 0.2 MPa static or dynamic compression, rat caudal vertebra', species='rat', source_ref='mnard2015', uncertainty='n=48 rats across 8 subgroups; no residual difference vs sham at 4 weeks'),
 dict(parameter='growth modulation, high vs low tether tension at 2 weeks', value='53 vs -1', unit='% growth modulation', conditions='single-level posterior vertebral body tethering, kyphotic swine', species='porcine', source_ref='halanski2026', uncertainty='SD 43 and 15 respectively, p=0.03'),
 dict(parameter='growth modulation, high vs low tether tension at 2-4 weeks', value='14 vs 10', unit='%', conditions='same animals, second interval', species='porcine', source_ref='halanski2026', uncertainty='SD 11 and 10, p=0.6'),
],
human_evidence='indirect', human_evidence_note='Guided growth, epiphysiodesis and vertebral tethering demonstrate that human physes are mechanically modulable, but the applied stress is never measured, so the human dose-response is unknown.',
species_basis=['rat','rabbit','bovine','porcine'], translation_risk='high',
translation_risk_reason='All dose-response data are from quadruped tail vertebrae and proximal tibiae under externally applied apparatus over days to weeks.',
confidence='C',
key_refs=[
 dict(ref_id='stokes2007', pmid='17532281', first_author='Stokes IA', year=2007, type='primary', one_line_finding='Growth changes of up to 53% track proliferative cell number and hypertrophic cell height'),
 dict(ref_id='mnard2015', pmid='26416149', first_author='Menard AL', year=2015, type='primary', one_line_finding='Growth rate and plate height fully recovered 10 days after removal of static or dynamic compression'),
 dict(ref_id='halanski2026', pmid='40836185', first_author='Halanski MA', year=2026, type='primary', one_line_finding='Tether tension effects on vertebral growth modulation are biphasic and transient'),
 dict(ref_id='stokes2006', pmid='16705695', first_author='Stokes IA', year=2006, type='primary', one_line_finding='Established the linear stress-growth relation used to define the modulation coefficient'),
],
open_questions=['g_l6mech_001','g_l6mech_005'], ))

w(dict(id='static_vs_dynamic_loading', name='Static versus dynamic loading of the growth plate', type='process',
summary=("The clinically important claim is that dynamic loading is growth-preserving where static compression is suppressive. The evidence "
 "supports a weaker and more specific statement. Duty cycle matters: cutting sustained 0.1 MPa compression from 24 h/day to 12 h/day "
 "raised rat vertebral growth from 82% to 90-93% of control and tibial growth from 70% to 84-86%, with no difference between day and "
 "night loading. But oscillation about a non-zero mean does not spare growth: sinusoidal 0.2 MPa +/- 30% at 0.1 Hz reduced rat caudal "
 "vertebral growth by exactly the same 19% as sustained 0.2 MPa, while sparing plate histology - only the static group lost plate "
 "thickness, proliferative cells per column and hypertrophic cell height. In swine explants at matched compressive strain (10% static "
 "vs 7-13% at 0.1 Hz for 48 h) the static group lost aggrecan, collagen II and collagen X while the dynamic group maintained the "
 "proliferative:hypertrophic ratio and matrix synthesis but lost columnar alignment. The mechanical explanation is viscoelastic: under "
 "stress control, static compression permits continued time-dependent creep, so hypertrophic chondrocytes accumulate significantly "
 "greater lateral and volumetric strain than under dynamic loading at the same mean stress and the same axial strain, and higher "
 "frequency reduces volumetric strain further. So mean stress sets growth rate; the waveform sets tissue damage."),
quantitative=[
 dict(parameter='rat vertebral growth, 24 h/day vs 12 h/day compression', value='82 vs 90-93', unit='% of within-animal control', conditions='nominally 0.1 MPa, 8 days, day-loading 93% and night-loading 90%', species='rat', source_ref='stokes2005', uncertainty='n=5 per group; sham 100%'),
 dict(parameter='rat proximal tibial growth, 24 h/day vs 12 h/day compression', value='70 vs 84-86', unit='% of within-animal control', conditions='nominally 0.1 MPa, 8 days', species='rat', source_ref='stokes2005', uncertainty='n=5 per group; sham 89%'),
 dict(parameter='growth rate reduction, static vs dynamic at equal mean stress', value='19 vs 19', unit='% below sham', conditions='0.2 MPa sustained vs 0.2 MPa +/-30% at 0.1 Hz, 2 weeks, rat caudal vertebra Cd7', species='rat', source_ref='valteau2011', uncertainty='both p<0.001 vs sham; static-dynamic difference not significant'),
 dict(parameter='growth plate thickness and proliferative cells per column, static vs dynamic', value='significant reduction under static only', unit='qualitative (p<0.01 static vs dynamic)', conditions='same experiment', species='rat', source_ref='valteau2011', uncertainty='hypertrophic cell height difference p=0.014'),
 dict(parameter='applied strain in matched static vs dynamic explant compression', value='10 static vs 7-13 dynamic', unit='% compressive strain', conditions='swine ulnar growth plate explants, 48 h, 0.1 Hz', species='porcine', source_ref='sergerie2011', uncertainty='matched mean strain by design'),
 dict(parameter='hypertrophic chondrocyte lateral and volumetric strain, static vs dynamic', value='higher under static', unit='p<0.001 lateral, p<=0.015 volumetric', conditions='stress-controlled compression of pre-pubertal rat proximal tibial explants; axial strain equal', species='rat', source_ref='zimmermann2017', uncertainty='high-frequency dynamic lower volumetric strain than low-frequency, p=0.002'),
],
human_evidence='absent', human_evidence_note='No human study compares static with dynamic physeal loading; the tension-band plate is the closest analogue and it is modelled, not measured.',
species_basis=['rat','porcine'], translation_risk='high',
translation_risk_reason='All comparisons are rodent tail vertebrae or swine explants; loading waveforms used are far simpler than human gait.',
confidence='C',
key_refs=[
 dict(ref_id='stokes2005', pmid='15607892', first_author='Stokes IA', year=2005, type='primary', one_line_finding='Halving daily loading duration roughly halved growth suppression at both vertebral and tibial sites'),
 dict(ref_id='valteau2011', pmid='21784187', first_author='Valteau B', year=2011, type='primary', one_line_finding='Static and dynamic loading at equal mean stress reduced growth equally (19%) but only static damaged plate histomorphometry'),
 dict(ref_id='sergerie2011', pmid='21337387', first_author='Sergerie K', year=2011, type='primary', one_line_finding='At matched strain, static compression destroyed matrix protein expression while dynamic preserved it but disordered columns'),
 dict(ref_id='zimmermann2017', pmid='28365062', first_author='Zimmermann EA', year=2017, type='primary', one_line_finding='Static stress-controlled loading produces greater lateral and volumetric hypertrophic cell strain than dynamic at equal mean stress'),
 dict(ref_id='mnard2014', pmid='24902946', first_author='Menard AL', year=2014, type='primary', one_line_finding='Dynamic compression reduced growth rate without histomorphometric change unless both magnitude and frequency were raised together'),
 dict(ref_id='kaviani2015', pmid='26019113', first_author='Kaviani R', year=2015, type='primary', one_line_finding='Static compression reduced growth plate chondrocyte viability more than dynamic at comparable loading'),
],
open_questions=['g_l6mech_004','g_l6mech_005'], contradicts=['wolff_law']))

w(dict(id='strain_magnitude_dependence', name='Strain magnitude dependence of growth modulation', type='process',
summary=("Within the range tested experimentally the growth response is linear in applied stress rather than threshold-like: across rat, "
 "rabbit and calf plates the percentage growth change was proportional to stress with a slope of 17.1% per 0.1 MPa and no evidence of a "
 "dead band around zero. The range actually probed is narrow, roughly 0.02-0.2 MPa in compression and a comparable magnitude in distraction, "
 "so linearity outside it is an assumption. In explant work strain rather than stress is the controlled variable and the magnitudes used are "
 "an order of magnitude larger than physiological: 10% static compressive strain for 48 h in swine ulnar plates suppressed every "
 "histomorphological parameter measured and abolished aggrecan and collagen II/X expression, and compressive modulation reduces chondrocyte "
 "viability in a magnitude-dependent way. Magnitude also interacts non-additively with frequency: raising either alone reduced growth without "
 "histological change in rat caudal vertebrae, but raising both together (1.0 Hz at 0.2 +/- 0.14 MPa) caused repeated inflammation and "
 "destroyed the tissue. There is no measured strain-magnitude dose-response curve for any human physis."),
quantitative=[
 dict(parameter='slope of growth change vs applied stress', value='17.1', unit='% per 0.1 MPa', conditions='pooled across 3 species, 2 sites, 8 days sustained loading', species='multiple', source_ref='stokes2006', uncertainty='range 9.2-23.9 across individual plates'),
 dict(parameter='stress range over which linearity was demonstrated', value='approximately -0.2 to +0.1', unit='MPa (negative = compression)', conditions='external loading apparatus, rat/rabbit/calf', species='multiple', source_ref='stokes2006', uncertainty='read from the reported loading protocol; extrapolation outside this range untested'),
 dict(parameter='static compressive strain used in explant suppression experiments', value='10', unit='%', conditions='4-week-old swine ulnar growth plate explants, 48 h unconfined compression', species='porcine', source_ref='sergerie2011', uncertainty='single magnitude tested'),
 dict(parameter='dynamic loading amplitude that destroyed plate integrity when combined with 1.0 Hz', value='0.2 +/- 0.14', unit='MPa', conditions='rat caudal vertebrae, 15 days', species='rat', source_ref='mnard2014', uncertainty='n=3; repeated inflammation prevented analysis'),
],
human_evidence='absent', human_evidence_note='No human physeal strain-magnitude dose-response exists; human physeal strain in vivo has not been measured.',
species_basis=['rat','rabbit','bovine','porcine'], translation_risk='high',
translation_risk_reason='Linearity is asserted over a narrow, non-physiological stress window in quadrupeds; explant strains used are far above in vivo values.',
confidence='C',
key_refs=[
 dict(ref_id='stokes2006', pmid='16705695', first_author='Stokes IA', year=2006, type='primary', one_line_finding='Growth change was apparently linear in stress with a 17.1%/0.1 MPa slope'),
 dict(ref_id='sergerie2011', pmid='21337387', first_author='Sergerie K', year=2011, type='primary', one_line_finding='10% static compressive strain for 48 h abolished aggrecan and collagen II/X expression in swine explants'),
 dict(ref_id='mnard2014', pmid='24902946', first_author='Menard AL', year=2014, type='primary', one_line_finding='Magnitude and frequency interact: raising both together destroyed the plate'),
 dict(ref_id='kaviani2015', pmid='26019113', first_author='Kaviani R', year=2015, type='primary', one_line_finding='Chondrocyte viability falls with compressive modulation magnitude'),
],
open_questions=['g_l6mech_002','g_l6mech_006']))
