import yaml, os
D='atlas/nodes/L6_mechanobiology'
def w(n):
    n.setdefault('layer','L6'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    with open(os.path.join(D,n['id']+'.yaml'),'w') as f:
        yaml.safe_dump(n,f,sort_keys=False,width=100,allow_unicode=True,default_flow_style=False)
    print('wrote',n['id'])

w(dict(
id='hueter_volkmann_law', name='Hueter-Volkmann law', type='hypothesis',
aliases=['Hueter-Volkmann principle','stress-growth law','growth modulation by sustained stress'],
summary=(
 "Stated qualitatively in the 1860s-1870s, the law asserts that sustained compression across a physis slows "
 "longitudinal growth and sustained tension accelerates it. Its quantitative form comes from one experimental "
 "programme (Stokes, Aronsson and colleagues), which applied calibrated external loading apparatus across "
 "caudal vertebral and proximal tibial growth plates in rats, rabbits and calves for 8 days and measured growth "
 "as the separation of fluorochrome labels given 24 and 48 h before euthanasia. Over roughly -0.2 to +0.1 MPa the "
 "stress-growth relation was apparently linear, with a growth-rate sensitivity of 17.1% per 0.1 MPa averaged "
 "across all plates (range 9.2-23.9% per 0.1 MPa), 15.0%/0.1 MPa for vertebrae and 18.6%/0.1 MPa for proximal "
 "tibia, despite baseline growth rates spanning 30 um/day (rat vertebra) to 366 um/day (rabbit proximal tibia). "
 "Cellularly the modulation is not a single mechanism: about half the growth change under sustained compression "
 "is accounted for by reduced hypertrophic chondrocyte enlargement and the remainder by fewer proliferative-zone "
 "chondrocytes per column, and in multiple regression the hypertrophic enlargement term carries the larger "
 "coefficient (1.39 vs 0.72). The response is asymmetric: compression suppresses more than an equal tension "
 "accelerates (52% vs 113% of control at ~60% body weight in rat tail vertebrae over 4 weeks). No equivalent "
 "sensitivity coefficient has ever been measured in a human physis; every human application - guided growth, "
 "vertebral body tethering, the scoliosis vicious cycle - extrapolates the animal coefficient."),
quantitative=[
 dict(parameter='growth-rate sensitivity to sustained stress, all plates pooled', value='17.1', unit='% growth change per 0.1 MPa',
      conditions='8 days sustained external loading, compression and distraction, fluorochrome-label growth measurement',
      species='multiple', source_ref='stokes2006', uncertainty='range across plates 9.2-23.9%/0.1 MPa; linear fit, CI not reported'),
 dict(parameter='growth-rate sensitivity, caudal vertebral growth plates', value='15.0', unit='% per 0.1 MPa',
      conditions='rat and calf caudal vertebrae, 8 days', species='multiple', source_ref='stokes2006', uncertainty='not reported separately'),
 dict(parameter='growth-rate sensitivity, proximal tibial growth plates', value='18.6', unit='% per 0.1 MPa',
      conditions='rat, rabbit and calf proximal tibia, 8 days', species='multiple', source_ref='stokes2006', uncertainty='not reported separately'),
 dict(parameter='baseline (unloaded) longitudinal growth rate range across the species/sites studied', value='30-366', unit='um/day',
      conditions='rat caudal vertebra lowest, rabbit proximal tibia highest', species='multiple', source_ref='stokes2006', uncertainty='site means'),
 dict(parameter='growth of compressed rat tail vertebra', value='52', unit='% of contralateral/adjacent control',
      conditions='4 weeks sustained compression at nominally 60% body weight', species='rat', source_ref='stokes2002', uncertainty='p=0.002 vs control'),
 dict(parameter='growth of distracted rat tail vertebra', value='113', unit='% of control',
      conditions='4 weeks sustained distraction at nominally 60% body weight', species='rat', source_ref='stokes2002', uncertainty='not significantly different from control'),
 dict(parameter='hypertrophic chondrocyte height under sustained compression', value='85', unit='% of control',
      conditions='rat tail vertebra, 4 weeks', species='rat', source_ref='stokes2002', uncertainty='significant; zone height 87%, increment in cell height 78%'),
 dict(parameter='multiple regression coefficient, final hypertrophic cell height -> growth rate', value='1.39', unit='dimensionless (normalised)',
      conditions='pooled rat, rabbit, calf loaded and control plates', species='multiple', source_ref='stokes2007', uncertainty='overall r=0.56 for this variable'),
 dict(parameter='multiple regression coefficient, proliferative cell number per unit width -> growth rate', value='0.72', unit='dimensionless (normalised)',
      conditions='pooled rat, rabbit, calf loaded and control plates', species='multiple', source_ref='stokes2007', uncertainty='overall r=0.38 for this variable'),
 dict(parameter='maximum growth-rate change achieved across the loading range tested', value='53', unit='%',
      conditions='sustained compression or distraction, 8 days', species='multiple', source_ref='stokes2007', uncertainty='not reported'),
],
localization=['rat caudal vertebral physis: measured (stokes2006)','rat proximal tibial physis: measured (stokes2006)',
 'rabbit proximal tibial physis: measured (stokes2006)','calf caudal vertebral and proximal tibial physis: measured (stokes2006)',
 'human physis: no direct stress-growth measurement located'],
human_evidence='indirect',
human_evidence_note=('Human evidence is entirely inferential: guided growth, epiphysiodesis, vertebral body tethering and '
 'the progression of Blount disease and scoliosis behave as the law predicts, but no human study has applied a known '
 'stress across a physis and measured the resulting growth rate, so no human sensitivity coefficient exists.'),
species_basis=['rat','rabbit','bovine'],
translation_risk='high',
translation_risk_reason=('The coefficient is extrapolated to humans from three quadrupedal species at two skeletal sites over '
 '8-28 day loading windows; human physes differ in thickness, baseline growth rate, loading history and duration of exposure, '
 'and the human in vivo physeal stress is itself unmeasured.'),
confidence='C',
key_refs=[
 dict(ref_id='stokes2006', pmid='16705695', doi='10.1002/jor.20189', first_author='Stokes IA', year=2006, type='primary',
      one_line_finding='Growth-rate sensitivity to sustained stress is 17.1%/0.1 MPa on average (9.2-23.9%) and similar across rat, rabbit and calf at two sites'),
 dict(ref_id='stokes2002', pmid='12377917', doi='10.2106/00004623-200210000-00016', first_author='Stokes IA', year=2002, type='primary',
      one_line_finding='Sustained compression cut rat tail vertebral growth to 52% of control and distraction raised it to 113%, with hypertrophic cell height at 85% of control'),
 dict(ref_id='stokes2007', pmid='17532281', doi='10.1016/j.bone.2007.04.180', first_author='Stokes IA', year=2007, type='primary',
      one_line_finding='Modulated growth is explained by both proliferative cell number and hypertrophic cell enlargement, the latter with the larger regression coefficient'),
 dict(ref_id='villemure2009', pmid='19540500', first_author='Villemure I', year=2009, type='review',
      one_line_finding='Consolidates growth plate mechanics and the stress-growth literature into a single survey'),
 dict(ref_id='roelen2026', pmid='42299327', first_author='Roelen MCR', year=2026, type='review',
      one_line_finding='Contemporary surgical practice explicitly grounds guided growth in the Hueter-Volkmann observation'),
],
open_questions=['g_l6mech_001','g_l6mech_002','g_l6mech_003'],
contradicts=[],
))

w(dict(
id='wolff_law', name="Wolff's law (as applied to the physis)", type='hypothesis',
aliases=["Wolff's law","mechanostat","Frost chondral modeling theory"],
summary=(
 "Wolff's law is a statement about bone: trabecular architecture and cortical mass adapt to the direction and magnitude "
 "of habitual loading. Frost's mechanostat recast it as a set-point controller in which modelling is switched on above "
 "roughly 1000-1500 microstrain of peak strain and remodelling removes bone below a lower threshold, so bone responds to "
 "peak intermittent strain rather than to mean stress. Frost's chondral modeling theory extended the same logic to cartilage "
 "and explicitly predicted the opposite dependence to Hueter-Volkmann: intermittent, dynamic loading drives cartilage growth, "
 "while static compression is the suppressive stimulus. The two laws are therefore not variants of each other and are "
 "distinguished experimentally by the loading waveform, not the tissue. Where Hueter-Volkmann is measured with mean stress "
 "held constant for days, Frost's prediction concerns the peak-to-trough excursion and the number of loading cycles; the "
 "static/dynamic experiments in the growth plate are the direct test, and they partly support Frost (dynamic loading preserves "
 "growth plate histology at stresses that static loading damages) while partly contradicting him (at matched mean stress, "
 "dynamic loading in rat caudal vertebrae suppressed growth just as much as static). Frost's writings are narrative theory, "
 "not primary data; the numerical thresholds he quotes are for bone strain, and no equivalent threshold has been measured "
 "for physeal cartilage in any species."),
quantitative=[
 dict(parameter='bone modelling threshold (mechanostat), peak strain', value='1000-1500', unit='microstrain',
      conditions="Frost's synthesis for cortical bone; not a growth plate measurement", species='multiple',
      source_ref='frost2004', uncertainty='theoretical range asserted in a narrative review; primary derivation not reproduced', value_unverified=True),
],
localization=['bone cortex and trabeculae: the domain of the original law','growth plate cartilage: extension by analogy only (frost1979, frost2001)'],
human_evidence='indirect',
human_evidence_note=('Human evidence for the bone form of the law is abundant (loading asymmetry in racquet-sport athletes, disuse '
 'osteopenia); for the cartilage/physis form there is no human strain-threshold measurement at all.'),
species_basis=['human','multiple'],
translation_risk='moderate',
translation_risk_reason=('The bone statement generalises well across species; the cartilage extension is a theoretical proposal by '
 'one author and its numerical thresholds have never been measured in physeal cartilage.'),
confidence='D',
key_refs=[
 dict(ref_id='frost1979', pmid='92358', first_author='Frost HM', year=1979, type='review',
      one_line_finding='Proposed the chondral modeling theory: intermittent rather than static loading governs cartilage growth and modelling'),
 dict(ref_id='frost2001', pmid='11393568', first_author='Frost HM', year=2001, type='review',
      one_line_finding='Applies the Utah paradigm to longitudinal growth, treating the physis as a load-bearing organ tuned to peak intermittent strain'),
 dict(ref_id='frost2004', pmid='15038485', first_author='Frost HM', year=2004, type='review',
      one_line_finding="Restates Wolff's law as the mechanostat with strain-defined modelling and remodelling thresholds in bone"),
 dict(ref_id='valteau2011', pmid='21784187', doi='10.1016/j.bone.2011.07.008', first_author='Valteau B', year=2011, type='primary',
      one_line_finding='At matched mean stress, dynamic loading suppressed rat caudal vertebral growth as much as static loading, contradicting a pure Frost prediction'),
 dict(ref_id='sergerie2011', pmid='21337387', doi='10.1002/jor.21282', first_author='Sergerie K', year=2011, type='primary',
      one_line_finding='Dynamic compression preserved matrix synthesis and zonal proportions in swine growth plate explants where static compression destroyed them'),
],
open_questions=['g_l6mech_004'],
contradicts=['hueter_volkmann_law'],
))
