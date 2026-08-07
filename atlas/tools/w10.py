import yaml, os
D='atlas/nodes/L6_mechanobiology'
def w(n):
    n.setdefault('layer','L6'); n.setdefault('stub',False); n.setdefault('last_verified','2026-08-05')
    yaml.safe_dump(n,open(os.path.join(D,n['id']+'.yaml'),'w'),sort_keys=False,width=100,allow_unicode=True)
    print('wrote',n['id'])

w(dict(id='diurnal_stature_variation', name='Diurnal stature variation', type='phenotype',
aliases=['circadian variation in stature','spinal shrinkage','diurnal height loss'],
summary=("Human stature falls measurably over a waking day and recovers overnight, and the effect is large enough to corrupt growth monitoring. In eight "
 "young adults measured to 1 mm precision, mean circadian variation was 19.3 mm, 1.1% of stature; 54% of the loss occurred within the first hour after "
 "rising and about 70% was regained during the first half of the night. The loss is load-dependent: static shoulder loads from 2.5 to 40 kg increased "
 "the rate of shrinkage nonlinearly, and repetitive lifting produced more shrinkage than the equivalent static load, so the disc creeps faster under "
 "cyclic than sustained loading - the opposite ordering to what static compression does to the growth plate. In children the effect is smaller but not "
 "negligible: 12-14 year old boys lost 2.0 mm from 09:30 to 14:00 and 4.6 mm from 10:00 to 17:00 with sitting height falling 2.0 and 2.8 mm, against a "
 "measurement standard error of 1.8 mm, and children with idiopathic scoliosis lost a mean 7 mm standing (0.43%) and 7 mm sitting (0.79%) between early "
 "morning and evening. The mechanism is intervertebral disc fluid exudation and unloading of the spinal curves, not physeal growth; the practical "
 "consequence is that a single unrecorded measurement time can hide or fabricate a centimetre of apparent annual growth."),
quantitative=[
 dict(parameter='mean circadian variation in adult stature', value='19.3', unit='mm', conditions='eight young adults, measurement precision 1 mm', species='human', source_ref='tyrrell1985', uncertainty='1.1% of stature; 54% of the loss in the first hour after rising'),
 dict(parameter='fraction of diurnal loss regained in the first half of the night', value='70', unit='%', conditions='same subjects', species='human', source_ref='tyrrell1985', uncertainty='approximate figure reported'),
 dict(parameter='stature loss 09:30 to 14:00 in 12-14 year old boys', value='2.0', unit='mm', conditions='n=19, stretching-upward technique', species='human', source_ref='whitehouse1974', uncertainty='measurement SE 1.8 mm'),
 dict(parameter='stature loss 10:00 to 17:00 in 12-14 year old boys', value='4.6', unit='mm', conditions='n=11 different boys', species='human', source_ref='whitehouse1974', uncertainty='sitting height fell 2.8 mm over the same interval'),
 dict(parameter='standing height loss over the day, children with idiopathic scoliosis', value='7', unit='mm', conditions='n=98, Cobb 10-52 deg, 07:00-08:00 vs 19:00-20:00', species='human', source_ref='czaprowski2019', uncertainty='SD 7 mm; 0.43% of initial standing height; p<0.001'),
 dict(parameter='sitting height loss over the day, children with idiopathic scoliosis', value='7', unit='mm', conditions='same cohort', species='human', source_ref='czaprowski2019', uncertainty='SD 7 mm; 0.79% of initial sitting height'),
],
localization=['human intervertebral discs and spinal curvature: the source of the variation','human physis: not involved'],
human_evidence='direct',
human_evidence_note='Directly measured in adults and children with stadiometry accurate to 1-2 mm, replicated across several independent groups since 1974.',
species_basis=['human'], translation_risk='not_applicable',
translation_risk_reason='Human measurement.',
confidence='A',
key_refs=[
 dict(ref_id='tyrrell1985', pmid='4002039', first_author='Tyrrell AR', year=1985, type='primary', one_line_finding='Mean circadian stature variation 19.3 mm (1.1%), load-dependent, with repetitive lifting shrinking more than equivalent static load'),
 dict(ref_id='whitehouse1974', pmid='16431557', first_author='Whitehouse RH', year=1974, type='primary', one_line_finding='12-14 year old boys lost 2.0 mm by early afternoon and 4.6 mm by late afternoon, against a 1.8 mm measurement SE'),
 dict(ref_id='czaprowski2019', pmid='30689550', first_author='Czaprowski D', year=2019, type='primary', one_line_finding='Children with idiopathic scoliosis lost 0.7 cm standing and sitting height between morning and evening'),
 dict(ref_id='reilly1984', pmid='6600017', first_author='Reilly T', year=1984, type='primary', one_line_finding='Established the precision stadiometry method for circadian stature measurement'),
 dict(ref_id='voss1997', pmid='9389235', first_author='Voss LD', year=1997, type='primary', one_line_finding='Diurnal loss persists despite the stretch technique, so it cannot be corrected by measurement posture alone'),
 dict(ref_id='meijer2024', pmid='39568059', first_author='Meijer KM', year=2024, type='primary', one_line_finding='Diurnal spine-length variation is large enough to matter for paediatric radiotherapy field planning'),
],
open_questions=['g_l6mech_014']))

w(dict(id='gravity_posture_spinal_loading', name='Gravity, posture and spinal loading', type='process',
summary=("Gravity acting through posture is the largest sustained mechanical variable acting on the growing human axial skeleton, and it can be titrated "
 "without surgery. Upright posture compresses the intervertebral discs and vertebral endplate physes; recumbency releases them, producing the overnight "
 "recovery of ~70% of the day's stature loss; and true weightlessness releases them completely, producing a stature gain of up to 3% that fully reverses "
 "on return to Earth. Added axial load scales the effect: static shoulder loads of 2.5-40 kg increased the shrinkage rate nonlinearly, and repetitive "
 "lifting exceeded equivalent static loading. This makes posture and gravity the natural experiment that most closely mirrors the animal compression "
 "studies - except that everything that has actually been measured in humans concerns the disc, not the physis. The vertebral endplate physis sits in "
 "series with the disc and must experience some fraction of the same load, but the partition between disc deformation and physeal stress has never been "
 "measured in a living human, which is precisely why the human vertebral stress-growth relation is unquantified. Finite element models of the growth "
 "plate show that plate morphology itself adapts to the local mechanical environment, so the geometry through which gravity acts is not fixed."),
quantitative=[
 dict(parameter='stature recovered in the first half of the night (recumbency)', value='70', unit='% of daily loss', conditions='eight young adults', species='human', source_ref='tyrrell1985', uncertainty='approximate'),
 dict(parameter='static shoulder load range over which shrinkage rate rises nonlinearly', value='2.5-40', unit='kg', conditions='young adults, precision stadiometry', species='human', source_ref='tyrrell1985', uncertainty='relation described as nonlinear; no fitted coefficient reported'),
 dict(parameter='stature gain under weightlessness', value='up to 3', unit='%', conditions='nine ISS crew, early flight phase', species='human', source_ref='young2023', uncertainty='reverses postflight'),
],
localization=['human intervertebral disc: directly measured','human vertebral endplate physis: load share never measured'],
human_evidence='direct',
human_evidence_note='Postural and gravitational effects on stature are directly measured in humans; the share of that load borne by the physis is not.',
species_basis=['human'], translation_risk='not_applicable',
translation_risk_reason='Human measurement, though the physeal component is inferred.',
confidence='B',
key_refs=[
 dict(ref_id='tyrrell1985', pmid='4002039', first_author='Tyrrell AR', year=1985, type='primary', one_line_finding='Quantified load- and posture-dependence of spinal shrinkage and recovery in humans'),
 dict(ref_id='young2023', pmid='34674563', first_author='Young KS', year=2023, type='primary', one_line_finding='Weightlessness raises stature up to 3% reversibly, the zero-gravity end point of the posture-load axis'),
 dict(ref_id='rodrguez2025', pmid='40475877', first_author='Rodriguez DQ', year=2025, type='primary', one_line_finding='Growth plate morphology itself adapts to the local mechanical environment in coupled remodelling/ossification models'),
 dict(ref_id='hucke2023', pmid='37415789', first_author='Hucke L', year=2023, type='primary', one_line_finding='Demonstrates the only route currently available to human physeal stress values - personalised finite element modelling from gait'),
],
open_questions=['g_l6mech_003','g_l6mech_014']))
