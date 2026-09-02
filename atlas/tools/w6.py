import yaml, os
D='atlas/nodes/L6_mechanobiology'
def w(n):
    n.setdefault('layer','L6'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    yaml.safe_dump(n,open(os.path.join(D,n['id']+'.yaml'),'w'),sort_keys=False,width=100,allow_unicode=True)
    print('wrote',n['id'])

w(dict(id='gymnastics_stature_effect', name='Gymnastics and stature', type='phenotype',
summary=("Female artistic gymnasts are short, mature late and have a blunted pubertal spurt; whether training causes this is the longest-running "
 "controversy in human growth mechanobiology. The pro-causal case rests on prospective cohorts: 22 gymnasts training >18 h/wk had peak height "
 "velocity 5.48 cm/yr against 8.0 cm/yr in age-matched swimmers, a height SDS that fell significantly over 2.35 years while the swimmers' did not, "
 "selective stunting of leg length (sitting height/leg length ratio 1.054 vs 1.100), and falling predicted adult height - and, critically, no change "
 "in the chronological-age/bone-age ratio, which weakens the pure maturational-delay explanation. A dose gradient exists within gymnasts: advanced "
 "(20-27 h/wk) versus intermediate (7.5-22 h/wk) trainees had lower peripubertal sitting-height velocity (2.3 vs 3.1 cm/yr) and over 35% of pre- and "
 "peripubertal gymnasts had height velocity below 4.5 cm/yr. The selection case is equally concrete: gymnasts' growth curves are indistinguishable "
 "from short, late-maturing girls with short parents, the spurt is present and about one year late rather than absent, and adult height is normal "
 "in retired gymnasts. The FIG Scientific Commission review concluded that available data cannot establish causality because training volume is "
 "confounded with selection, energy availability and family size, and epidemiological criteria for causation are not met. Adjudication: the "
 "attenuation during training is real and dose-related; the claim that it removes adult height is not established, and no study has separated "
 "mechanical loading of the physis from energy deficit and hypothalamic suppression, which is the mechanistically decisive question for this layer."),
quantitative=[
 dict(parameter='peak height velocity, gymnasts vs swimmers', value='5.48 vs 8.0', unit='cm/yr', conditions='mean age 12.3 y, gymnasts ~22 h/wk vs swimmers ~8 h/wk, 2.35 y prospective', species='human', source_ref='theintz1993', uncertainty='SEM 0.32 and 0.50; p<0.05 for bone ages 11-13'),
 dict(parameter='sitting height / leg length ratio, gymnasts vs swimmers', value='1.054 vs 1.100', unit='ratio', conditions='same cohort', species='human', source_ref='theintz1993', uncertainty='SEM 0.005 both; p<0.001'),
 dict(parameter='height SDS trajectory in gymnasts over follow-up', value='-0.747', unit='correlation coefficient r vs time', conditions='same cohort; swimmers r=-0.165, p=0.1', species='human', source_ref='theintz1993', uncertainty='p<0.001'),
 dict(parameter='peak height velocity in competitive gymnasts (advanced and intermediate)', value='6.2-6.4', unit='cm/yr', conditions='137 gymnasts, 2 y prospective, Preece-Baines model; age at PHV 13-13.5 y', species='human', source_ref='daly2005', uncertainty='estimated from mixed-longitudinal data'),
 dict(parameter='peripubertal sitting height velocity, advanced vs intermediate training', value='2.3 vs 3.1', unit='cm/yr', conditions='20-27 h/wk vs 7.5-22 h/wk', species='human', source_ref='daly2005', uncertainty='p<0.05'),
 dict(parameter='gymnasts with growth faltering (height velocity <4.5 cm/yr)', value='>35', unit='% of pre- and peripubertal gymnasts', conditions='same cohort', species='human', source_ref='daly2005', uncertainty='proportion, no CI given'),
 dict(parameter='delay in age at peak height velocity vs non-athletic girls', value='approximately 1', unit='years', conditions='15 Belgian gymnasts ~15 h/wk followed 8.7-15.5 y', species='human', source_ref='thomis2005', uncertainty='spurts present in height, sitting height and leg length'),
],
human_evidence='direct',
human_evidence_note='All data are human prospective anthropometric cohorts; the dispute is about confounding and causal inference, not about whether the association exists.',
species_basis=['human'], translation_risk='not_applicable',
translation_risk_reason='Inherently human observational phenotype.',
confidence='D',
key_refs=[
 dict(ref_id='theintz1993', pmid='8117341', first_author='Theintz GE', year=1993, type='primary', one_line_finding='Gymnasts training >18 h/wk had PHV 5.48 vs 8.0 cm/yr in swimmers with falling height SDS and selective leg-length stunting'),
 dict(ref_id='daly2005', pmid='15947733', first_author='Daly RM', year=2005, type='primary', one_line_finding='Within-gymnast training-volume gradient: advanced trainees had lower peripubertal sitting-height velocity than intermediate trainees'),
 dict(ref_id='thomis2005', pmid='15689917', first_author='Thomis M', year=2005, type='primary', one_line_finding='Gymnasts do have adolescent spurts, about a year late and slightly blunted, matching short late-maturing girls with short parents'),
 dict(ref_id='malina2013', pmid='23743792', first_author='Malina RM', year=2013, type='systematic_review', one_line_finding='FIG commission review: causality between training and attained adult stature is not established; selection and maturation confound every design'),
 dict(ref_id='beunen2006', pmid='16540852', first_author='Beunen G', year=2006, type='review', one_line_finding='Reviews the blunted growth velocity claim and the catch-up argument'),
 dict(ref_id='bass2002', pmid='12145127', first_author='Bass S', year=2002, type='review', one_line_finding='States the case that intense training in elite female athletes reduces growth and delays maturation'),
],
open_questions=['g_l6mech_010'], contradicts=['sport_specific_loading_human']))

w(dict(id='sport_specific_loading_human', name='Sport-specific mechanical loading effects on the human skeleton', type='phenotype',
summary=("Sport gives the only human experiments in which a physis is loaded far outside the normal range for years, and the results split by site. "
 "Where loading is compressive, repetitive and applied through a small joint, local growth is suppressed: in gymnasts the wrist bears body weight, "
 "and imaging shows distal radial physeal stress injury with acquired positive ulnar variance, i.e. the radius is shortened relative to the ulna in "
 "the same limb - an internally controlled demonstration of load-suppressed physeal output in humans. Wrist pain and physeal injury are common enough "
 "in adolescent artistic gymnasts to have their own systematic review and meta-analysis. Where loading is impact-type, intermittent and axial, growth "
 "is preserved or promoted: a 24-week supervised jumping protocol (3 sessions/week, 50 min) in 47 prepubertal short-stature children gave 4.20 cm of "
 "height gain against 2.48 cm in controls (p=0.001) alongside a femoral neck BMD Z-score gain of 1.075. The two findings are consistent with the "
 "static-versus-dynamic distinction seen in animals rather than with a single monotonic load-growth relation. Neither the gymnast wrist nor the jumping "
 "trial measures the stress at the physis, so the human dose axis remains empty; the jumping trial is also small, single-centre and not blinded, and "
 "its mediation analysis (via femoral neck BMD, beta=-0.442) is fragile."),
quantitative=[
 dict(parameter='height gain over 24 weeks, jumping intervention vs control', value='4.20 vs 2.48', unit='cm', conditions='47 prepubertal short-stature children aged 8-11 y, 3 sessions/wk of 50 min progressive jumping', species='human', source_ref='wang2025', uncertainty='p=0.001; n=20 intervention, n=27 control; not randomised'),
 dict(parameter='femoral neck BMD Z-score change, jumping intervention', value='1.075', unit='Z-score units', conditions='same trial, DXA', species='human', source_ref='wang2025', uncertainty="p<0.001, Cohen's d 0.869; lumbar spine BMD unchanged"),
 dict(parameter='mediation of height gain by femoral neck BMD change', value='-0.442', unit='beta', conditions='same trial', species='human', source_ref='wang2025', uncertainty='95% CI -1.474 to -0.009; no direct effect detected'),
],
localization=['human distal radial physis in gymnasts: stress injury and positive ulnar variance (difiori2006)','human lower limb physes under impact loading: growth promotion inferred, not localised'],
human_evidence='direct',
human_evidence_note='Both the gymnast wrist series and the jumping trial are human, but neither measures physeal stress and neither is randomised with adult height as the endpoint.',
species_basis=['human'], translation_risk='not_applicable',
translation_risk_reason='Human observational and interventional data.',
confidence='C',
key_refs=[
 dict(ref_id='difiori2006', pmid='16493174', first_author='DiFiori JP', year=2006, type='review', one_line_finding='Repetitive weight-bearing wrist loading in gymnasts causes distal radial physeal injury and acquired positive ulnar variance'),
 dict(ref_id='dileo2026', pmid='41552624', first_author='DiLeo SDF', year=2026, type='systematic_review', one_line_finding='Quantifies the epidemiology and risk factors of wrist pain and injury in adolescent artistic gymnasts'),
 dict(ref_id='wang2025', pmid='41233903', first_author='Wang HM', year=2025, type='primary', one_line_finding='24 weeks of jumping exercise gave 4.20 cm height gain vs 2.48 cm in controls in prepubertal short-stature children'),
],
open_questions=['g_l6mech_010','g_l6mech_003']))
