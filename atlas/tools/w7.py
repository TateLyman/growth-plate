import yaml, os
D='atlas/nodes/L6_mechanobiology'
def w(n):
    n.setdefault('layer','L6'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    yaml.safe_dump(n,open(os.path.join(D,n['id']+'.yaml'),'w'),sort_keys=False,width=100,allow_unicode=True)
    print('wrote',n['id'])

w(dict(id='distraction_osteogenesis', name='Distraction osteogenesis', type='intervention',
aliases=['Ilizarov method','callotasis','limb lengthening','tension-stress effect'],
summary=("Distraction osteogenesis is the deliberate creation of a de novo growth zone: a bone is osteotomised, allowed a latency period, then the "
 "fragments are separated slowly, and new bone forms in the gap. Ilizarov's canine experiments established that the resulting tissue is not a "
 "growth plate but a distinct structure - new bone forms in parallel columns extending in both directions from a central fibrous growth zone, with "
 "features of both physeal and intramembranous ossification and belonging to neither. Three variables were shown to determine success: stability of "
 "external fixation, preservation of periosteum, bone marrow and medullary blood supply at osteotomy, and the rate and rhythm of distraction. The "
 "same experiments showed the tension vector, not the bone's mechanical axis, sets the direction of new bone: canine tibiae widened by lateral "
 "distraction formed bone parallel to the applied tension even when perpendicular to the mechanical axis. Distraction osteogenesis is therefore the "
 "cleanest demonstration in any species that sustained tensile strain is an instructive, direction-setting stimulus for skeletal tissue formation - "
 "the tension arm of Hueter-Volkmann operating outside a physis. It is routine human surgery, so its efficacy in humans is not in doubt; what is "
 "absent is any human measurement of the strain or stress in the regenerate."),
quantitative=[],
localization=['canine tibial diaphysis (experimental): confirmed (ilizarov1989, ilizarov1989a)','human long bones: routine clinical practice'],
human_evidence='direct',
human_evidence_note='Distraction osteogenesis is performed in humans daily with radiographically measured regenerate formation; only the mechanical dose at tissue level is unmeasured.',
species_basis=['multiple','human'], translation_risk='low',
translation_risk_reason='The canine-derived rate and rhythm parameters were adopted into human practice and have held for four decades.',
confidence='A',
key_refs=[
 dict(ref_id='ilizarov1989', pmid='2912628', first_author='Ilizarov GA', year=1989, type='primary', one_line_finding='Defined the rate and rhythm dose-response and showed the regenerate is a physis-like but distinct structure with a central growth zone'),
 dict(ref_id='ilizarov1989a', pmid='2910611', first_author='Ilizarov GA', year=1989, type='primary', one_line_finding='Fixation stability and soft-tissue/marrow preservation determine osteogenesis; new bone aligns with the tension vector, not the mechanical axis'),
],
open_questions=['g_l6mech_011']))

w(dict(id='distraction_rate_dose_response', name='Distraction rate and rhythm dose-response', type='process',
summary=("The canonical prescription - 1 mm per day in four increments - traces to a single primary source, Ilizarov's canine tibial series, and the "
 "primary source supports it. Three rates were compared at fixed frequency: 0.5 mm/day often caused premature consolidation of the lengthening bone, "
 "2.0 mm/day often caused undesirable changes in the elongating soft tissues (fascia, muscle, vessels, nerve, skin), and 1.0 mm/day gave the best "
 "result. Frequency was varied independently at 1, 4 and 60 steps per day and the finding was monotonic: the greater the frequency, the better the "
 "outcome, so 4 steps/day is a practical compromise rather than an optimum - continuous distraction would be predicted to be better still. The "
 "reported endpoints are histomorphological and biochemical grading of the regenerate and of the elongating soft tissues, not a numeric growth rate, "
 "so no sensitivity coefficient (mm of regenerate per mm/day of distraction) exists. The upper and lower failure modes are mechanistically distinct - "
 "premature consolidation below the optimum is a bone problem, soft-tissue injury above it is a nerve/muscle/vessel problem - which means the "
 "therapeutic window is set by two different tissues and should be expected to differ by segment, age and species. Human practice inherited the 1 mm/day "
 "figure without an equivalent human dose-finding study."),
quantitative=[
 dict(parameter='distraction rate causing premature consolidation', value='0.5', unit='mm/day', conditions='canine tibia, open osteotomy and closed osteoclasis, Ilizarov circular fixator', species='multiple', source_ref='ilizarov1989', uncertainty='"often" - frequency not quantified in the report'),
 dict(parameter='optimal distraction rate', value='1.0', unit='mm/day', conditions='same', species='multiple', source_ref='ilizarov1989', uncertainty='best of three rates tested; no confidence interval'),
 dict(parameter='distraction rate causing soft-tissue injury', value='2.0', unit='mm/day', conditions='same; changes in fascia, skeletal and smooth muscle, vessels, nerves, skin', species='multiple', source_ref='ilizarov1989', uncertainty='"often" - frequency not quantified'),
 dict(parameter='distraction frequencies tested at fixed 1.0 mm/day', value='1, 4 and 60', unit='increments/day', conditions='canine tibia', species='multiple', source_ref='ilizarov1989', uncertainty='outcome improved monotonically with frequency; the clinical standard of 4/day is a compromise, not the measured optimum'),
],
human_evidence='indirect',
human_evidence_note='Human limb lengthening uses ~1 mm/day in 3-4 increments by inheritance from the canine data; no human study has randomised rate or rhythm against a regenerate-quality endpoint.',
species_basis=['multiple'], translation_risk='moderate',
translation_risk_reason='A single canine series with qualitative endpoints underwrites a universal human prescription; segment, age and pathology are known in clinical practice to shift the tolerable rate, but that shift has not been quantified.',
confidence='C',
key_refs=[
 dict(ref_id='ilizarov1989', pmid='2912628', first_author='Ilizarov GA', year=1989, type='primary', one_line_finding='0.5 mm/day premature consolidation, 2.0 mm/day soft-tissue damage, 1.0 mm/day optimal; higher frequency always better'),
 dict(ref_id='ilizarov1989a', pmid='2910611', first_author='Ilizarov GA', year=1989, type='primary', one_line_finding='Establishes the fixation-stability and tissue-preservation conditions under which the rate/rhythm optimum holds'),
],
open_questions=['g_l6mech_011']))

w(dict(id='guided_growth_tension_band', name='Guided growth (tension band plating)', type='intervention',
aliases=['hemiepiphysiodesis','eight-Plate','tension-band plate','growth modulation'],
summary=("Guided growth is the therapeutic application of Hueter-Volkmann: a two-hole plate with divergent screws is placed extraperiosteally across one "
 "side of a physis, tethering that side while the other continues to grow, so the bone angulates. It is the largest human dataset on mechanically "
 "modulated physeal growth. In 654 growth modulations in 313 children the mean correction rate was 0.67 +/- 0.55 degrees/month for the distal femur "
 "(mLDFA) and 0.43 +/- 0.38 degrees/month for the proximal tibia (mMPTA); a neutral mechanical axis was achieved in 68.7% overall, 78.2% in idiopathic "
 "and 66.3% in non-idiopathic aetiologies, and older age at surgery and varus deformity predicted slower correction. The very wide standard deviations "
 "- roughly 80-90% of the mean - are the important number: the human response to a nominally identical mechanical intervention is far more variable "
 "than the tight animal stress-growth relation would predict. The mechanical dose is unknown: the only estimate comes from personalised finite element "
 "models of four human distal femoral epiphyses under gait loads, which show the implant locally imposes static stress and removes cyclic loading at "
 "the insertion site while raising tensile stress on the contralateral side, so the plate acts through both arms of the static/dynamic distinction, "
 "not by compression alone. Correction is not always permanent; rebound after implant removal is recognised."),
quantitative=[
 dict(parameter='correction rate, distal femur (mLDFA)', value='0.67', unit='degrees/month', conditions='654 growth modulations in 313 children, tension band plates, 2009-2021', species='human', source_ref='tolk2026', uncertainty='SD 0.55'),
 dict(parameter='correction rate, proximal tibia (mMPTA)', value='0.43', unit='degrees/month', conditions='same cohort', species='human', source_ref='tolk2026', uncertainty='SD 0.38'),
 dict(parameter='proportion achieving neutral mechanical axis', value='68.7', unit='%', conditions='same cohort', species='human', source_ref='tolk2026', uncertainty='idiopathic 78.2% vs non-idiopathic 66.3%, p=0.02'),
 dict(parameter='site distribution of modulations', value='55.4 distal femur / 44.6 proximal tibia', unit='%', conditions='same cohort', species='human', source_ref='tolk2026', uncertainty='42.2% of children had both'),
],
localization=['human distal femoral and proximal tibial physes: direct clinical measurement (tolk2026)'],
human_evidence='direct',
human_evidence_note='Thousands of human physes have been mechanically modulated with radiographically measured angular outcomes; only the applied stress is unmeasured.',
species_basis=['human'], translation_risk='not_applicable',
translation_risk_reason='Human clinical intervention.',
confidence='A',
key_refs=[
 dict(ref_id='tolk2026', pmid='41696355', first_author='Tolk JJ', year=2026, type='primary', one_line_finding='Mean correction 0.67 deg/month (femur) and 0.43 deg/month (tibia) with 68.7% reaching a neutral axis, varying strongly by aetiology'),
 dict(ref_id='hucke2023', pmid='37415789', first_author='Hucke L', year=2023, type='primary', one_line_finding='Personalised FE models show the plate imposes local static stress and removes cyclic loading at insertion while raising contralateral tension'),
 dict(ref_id='roelen2026', pmid='42299327', first_author='Roelen MCR', year=2026, type='review', one_line_finding='Current-concepts review grounding guided growth explicitly in the Hueter-Volkmann observation'),
 dict(ref_id='coskun2026', pmid='41178588', first_author='Coskun E', year=2026, type='primary', one_line_finding='Guided growth outcomes in juvenile and adolescent Blount disease, a high-load failure setting'),
],
open_questions=['g_l6mech_003','g_l6mech_012']))

w(dict(id='epiphysiodesis', name='Epiphysiodesis', type='intervention',
aliases=['physeal arrest','Phemister procedure','PETS','percutaneous epiphysiodesis'],
summary=("Epiphysiodesis is the deliberate, permanent destruction or mechanical bridging of a physis to stop growth at that site, used to equalise leg "
 "lengths or to limit final height. As an experiment it is the mechanical converse of guided growth: instead of modulating growth by asymmetric "
 "compression, it abolishes it by continuity of bone across the plate. Its outcomes establish two facts relevant to this layer. First, surgically "
 "induced physeal arrest in humans is permanent - 28 to 40 year follow-up after epiphysiodesis for leg length discrepancy shows the correction is "
 "maintained into middle age, with no evidence of late intra-articular knee deformity after temporary epiphysiodesis. Second, the effect is "
 "quantitatively predictable enough to be planned: remaining growth prediction methods are accurate enough to time the operation, which means human "
 "physeal output is forecastable from age and skeletal maturity even though it is not forecastable from load. Bilateral epiphysiodesis is also used "
 "deliberately to reduce final height in extremely tall adolescents, which is the only human procedure that directly trades measured growth for a "
 "mechanical intervention on the physis."),
quantitative=[],
localization=['human distal femoral, proximal tibial and distal radial/ulnar physes: routine clinical targets'],
human_evidence='direct',
human_evidence_note='Long-term human follow-up series with radiographic and clinical endpoints.',
species_basis=['human'], translation_risk='not_applicable',
translation_risk_reason='Human clinical intervention.',
confidence='A',
key_refs=[
 dict(ref_id='laufer2025', pmid='41400744', first_author='Laufer A', year=2025, type='primary', one_line_finding='28-40 year follow-up shows permanent epiphysiodesis for leg length discrepancy maintains correction into middle age'),
 dict(ref_id='aeppli2025', pmid='38402874', first_author='Aeppli TRJ', year=2025, type='primary', one_line_finding='Bilateral epiphysiodesis safely reduces final height in extremely tall adolescents'),
],
open_questions=['g_l6mech_012']))
