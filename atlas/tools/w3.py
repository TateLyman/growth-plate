import yaml, os
D='atlas/nodes/L6_mechanobiology'
def w(n):
    n.setdefault('layer','L6'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    yaml.safe_dump(n,open(os.path.join(D,n['id']+'.yaml'),'w'),sort_keys=False,width=100,allow_unicode=True)
    print('wrote',n['id'])

w(dict(id='strain_frequency_dependence', name='Strain frequency dependence', type='process',
summary=("Frequency has been varied over a narrow band (0.1-1.0 Hz) in in vivo growth plate loading and it changes both growth and tissue "
 "response. In rat caudal vertebrae held at 0.2 MPa mean, sinusoidal loading at 0.1 Hz (+/-0.2 MPa) and at 1.0 Hz (+/-0.06 MPa) each "
 "reduced growth rate below sham without measurable histomorphometric change, whereas 1.0 Hz combined with +/-0.14 MPa produced repeated "
 "inflammation and loss of plate integrity - so frequency and amplitude are not independent. At the cell level frequency acts through "
 "viscoelasticity: in stress-controlled explant compression, higher-frequency dynamic loading produced significantly lower hypertrophic "
 "chondrocyte volumetric strain than lower-frequency loading (p=0.002), because each cycle is too short for full creep. Distraction "
 "osteogenesis provides the only frequency dose-response with a clinical endpoint: at a fixed 1.0 mm/day, increasing the number of "
 "increments from 1 to 4 to 60 per day monotonically improved regenerate quality in the canine tibia. No physiological frequency spectrum "
 "of human physeal loading (gait at ~1-2 Hz, running higher) has been mapped onto a growth response."),
quantitative=[
 dict(parameter='dynamic loading frequencies tested in vivo on rat caudal vertebrae', value='0.1 and 1.0', unit='Hz', conditions='mean 0.2 MPa, 15 days, amplitudes +/-0.2, +/-0.06 and +/-0.14 MPa', species='rat', source_ref='mnard2014', uncertainty='n=3-4 per group'),
 dict(parameter='hypertrophic chondrocyte volumetric strain, high vs low frequency dynamic compression', value='lower at high frequency', unit='p=0.002', conditions='stress-controlled compression of rat proximal tibial growth plate explants', species='rat', source_ref='zimmermann2017', uncertainty='effect size not reported as a ratio'),
 dict(parameter='distraction frequency giving best regenerate at fixed 1.0 mm/day', value='60', unit='increments/day', conditions='canine tibia, compared with 1/day and 4/day', species='multiple', source_ref='ilizarov1989', uncertainty='histomorphological grading, no numeric effect size reported'),
],
human_evidence='indirect', human_evidence_note='The only human-facing frequency evidence is distraction rhythm in limb lengthening, where higher increment frequency at fixed rate is preferred; physiological gait-frequency effects on the physis are unmeasured.',
species_basis=['rat','multiple'], translation_risk='high',
translation_risk_reason='Frequencies tested (0.1-1.0 Hz) barely overlap human locomotor loading, and the canine distraction data concern regenerate bone, not a native physis.',
confidence='D',
key_refs=[
 dict(ref_id='mnard2014', pmid='24902946', first_author='Menard AL', year=2014, type='primary', one_line_finding='Frequency and amplitude interact; each alone reduced growth without histological change, together they destroyed the plate'),
 dict(ref_id='zimmermann2017', pmid='28365062', first_author='Zimmermann EA', year=2017, type='primary', one_line_finding='Higher-frequency dynamic compression gave lower hypertrophic cell volumetric strain'),
 dict(ref_id='ilizarov1989', pmid='2912628', first_author='Ilizarov GA', year=1989, type='primary', one_line_finding='At fixed 1.0 mm/day, greater distraction frequency (up to 60 steps/day) gave better osteogenesis'),
],
open_questions=['g_l6mech_005','g_l6mech_006']))

w(dict(id='strain_rate_dependence', name='Strain rate dependence', type='process',
summary=("Growth plate cartilage is strongly viscoelastic and poroelastic, so its mechanical response depends on how fast strain is applied, "
 "not only on how much. This is the mechanistic root of the static/dynamic distinction: under stress control, a slowly or indefinitely "
 "applied load allows fluid exudation and continued creep, and hypertrophic chondrocytes accumulate lateral and volumetric strain over "
 "time, whereas a rapidly cycling load of the same mean magnitude truncates creep and leaves cells with the same axial but lower lateral "
 "and volumetric deformation. Digital image correlation in porcine explants likewise shows qualitatively different internal strain fields "
 "under static versus dynamic modulation rather than a simple scaling. Because the tissue's apparent modulus rises with loading rate, the "
 "stress transmitted to chondrocytes during a fast heel strike is not predictable from the quasi-static modulus, which is one reason "
 "in vivo human physeal stress cannot be inferred from joint contact force alone. No experiment has yet varied strain rate as the sole "
 "independent variable in an in vivo growth plate and measured growth rate."),
quantitative=[
 dict(parameter='axial hypertrophic cell strain, static vs dynamic at matched mean stress', value='not different', unit='qualitative', conditions='stress-controlled compression, pre-pubertal rat proximal tibial explants', species='rat', source_ref='zimmermann2017', uncertainty='lateral p<0.001 and volumetric p<=0.015 both higher under static'),
],
human_evidence='absent', human_evidence_note='No human physeal strain-rate measurement exists.',
species_basis=['rat','porcine'], translation_risk='high',
translation_risk_reason='Inference rests on explant rheology in two species; the in vivo human loading rate spectrum is unknown.',
confidence='D',
key_refs=[
 dict(ref_id='zimmermann2017', pmid='28365062', first_author='Zimmermann EA', year=2017, type='primary', one_line_finding='Time-dependent creep under static stress control is what raises lateral and volumetric chondrocyte strain'),
 dict(ref_id='kaviani2016', pmid='26452368', first_author='Kaviani R', year=2016, type='primary', one_line_finding='Internal strain fields in growth plate cartilage differ qualitatively between static and dynamic modulation'),
],
open_questions=['g_l6mech_002','g_l6mech_006']))

w(dict(id='loading_effect_plate_height', name='Loading effect on growth plate height and zonal structure', type='phenotype',
summary=("Sustained compression thins the growth plate and the thinning is zonally specific. In rat caudal vertebrae under 0.2 MPa for two weeks, "
 "static loading significantly reduced total plate thickness, the number of proliferative chondrocytes per column and hypertrophic chondrocyte "
 "height, whereas dynamic loading at the same mean stress produced the same growth-rate reduction with none of these histological changes. "
 "Under four weeks of ~60% body weight compression, hypertrophic zone height fell to 87% of control, mean hypertrophic cell height to 85%, and "
 "the increment in cell height along the growth direction to 78%; distraction changed none of these significantly, which is why compression "
 "and tension are not mirror images. Across species, altered plate height correlates with altered growth rate but explains it only partly: "
 "proliferative cell number per unit width and maximum hypertrophic cell height together account for the growth change with correlation "
 "coefficients of 0.38 and 0.56. Plate thinning is reversible - height returned to sham within 10 days of unloading. Plate thickness is also "
 "the single most influential parameter in finite-element models of how the plate adapts its shape to the local mechanical environment."),
quantitative=[
 dict(parameter='hypertrophic zone height under sustained compression', value='87', unit='% of control', conditions='rat tail vertebra, 4 weeks at ~60% body weight', species='rat', source_ref='stokes2002', uncertainty='significantly less than control'),
 dict(parameter='mean hypertrophic chondrocyte height under sustained compression', value='85', unit='% of control', conditions='same', species='rat', source_ref='stokes2002', uncertainty='significant; r2=0.23 vs growth rate, p=0.06'),
 dict(parameter='increment in chondrocyte height along the growth direction under compression', value='78', unit='% of control', conditions='same', species='rat', source_ref='stokes2002', uncertainty='significant'),
 dict(parameter='correlation of proliferative cell number per unit width with growth rate', value='0.38', unit='r', conditions='pooled rat, rabbit, calf, loaded and control', species='multiple', source_ref='stokes2007', uncertainty='overall correlation coefficient'),
 dict(parameter='correlation of maximum hypertrophic cell height with growth rate', value='0.56', unit='r', conditions='same', species='multiple', source_ref='stokes2007', uncertainty='overall correlation coefficient'),
 dict(parameter='recovery of growth plate height after unloading', value='complete by 10', unit='days', conditions='after 15 days of 0.2 MPa static or dynamic compression, rat caudal vertebra', species='rat', source_ref='mnard2015', uncertainty='no significant difference from sham'),
],
human_evidence='absent', human_evidence_note='Human growth plate height under known load has not been measured; paediatric MRI physeal thickness studies do not control applied stress.',
species_basis=['rat','rabbit','bovine'], translation_risk='high',
translation_risk_reason='Histomorphometry requires sacrifice, so all zonal data are animal; human physeal thickness data are cross-sectional imaging without a load variable.',
confidence='C',
key_refs=[
 dict(ref_id='stokes2002', pmid='12377917', first_author='Stokes IA', year=2002, type='primary', one_line_finding='Compression reduced hypertrophic zone height to 87% and cell height to 85% of control while distraction changed neither'),
 dict(ref_id='valteau2011', pmid='21784187', first_author='Valteau B', year=2011, type='primary', one_line_finding='Only static loading reduced plate thickness, proliferative cells per column and hypertrophic cell height'),
 dict(ref_id='stokes2007', pmid='17532281', first_author='Stokes IA', year=2007, type='primary', one_line_finding='Proliferative cell number and hypertrophic cell height correlate with growth rate at r=0.38 and 0.56'),
 dict(ref_id='mnard2015', pmid='26416149', first_author='Menard AL', year=2015, type='primary', one_line_finding='Plate height recovered fully within 10 days of load removal'),
 dict(ref_id='rodrguez2025', pmid='40475877', first_author='Rodriguez DQ', year=2025, type='primary', one_line_finding='In FE models of endochondral growth, plate thickness is the most influential parameter for mechanically driven shape change'),
],
open_questions=['g_l6mech_002']))
