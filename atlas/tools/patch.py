import yaml, os
D = '/home/user/growth-plate/atlas/nodes/L3_signaling_networks'

def load(i):
    with open(os.path.join(D, i + '.yaml')) as f:
        return yaml.safe_load(f)

def save(n):
    with open(os.path.join(D, n['id'] + '.yaml'), 'w') as f:
        yaml.safe_dump(n, f, sort_keys=False, default_flow_style=False, width=112, allow_unicode=True)
    print('patched', n['id'])

# ---- bmp_signaling_growth_plate: add Garrison 2017 zonal gradient ----
n = load('bmp_signaling_growth_plate')
n['summary'] = n['summary'].replace(
 "Human evidence is genetic and indirect:",
 "Zonally, laser-capture microdissection of postnatal mouse proximal tibia followed by direct mRNA counting "
 "shows Bmp2 and Bmp6 expression rising to a maximum in the hypertrophic zone, yet phospho-SMAD1/5/8 "
 "immunostaining is HIGHER in the proliferative and prehypertrophic zones than in the hypertrophic zone - "
 "ligand abundance and pathway activity run in opposite directions across the plate, apparently because the "
 "inhibitory SMAD7 is concentrated in the hypertrophic zone (Garrison 2017, mouse). "
 "Human evidence is genetic and indirect:")
n['localization'] = [
 "mouse PZ/PHZ: pSmad1/5/8 immunostaining highest here, above the hypertrophic zone (garrison2017)",
 "mouse HZ: Bmp2 and Bmp6 mRNA highest, but pSmad1/5/8 lower and Smad7 high (garrison2017)",
 "mouse PERI: confirmed - Bmp2/Bmp4/Bmp7 expressed in perichondrium (bandyopadhyay2006)",
 "human growth plate: unconfirmed - no zonal pSMAD1/5/8 immunostaining series published"]
n['key_refs'].insert(2, dict(ref_id='garrison2017', pmid='28467498', first_author='Garrison P', year=2017,
  type='primary', one_line_finding='Zonal LCM plus IHC in mouse tibia: Bmp2/Bmp6 mRNA peaks in HZ but pSmad1/5/8 activity peaks in PZ/PHZ, with Smad7 high in HZ.'))
save(n)

# ---- smad1_5_8 ----
n = load('smad1_5_8')
n['summary'] = n['summary'].replace(
 "No zonal pSMAD1/5/8 immunostaining series has been published on human growth plate tissue, so the human activity gradient across RZ-PZ-PHZ-HZ is unmeasured.",
 "In mouse the zonal activity profile has been measured: pSMAD1/5/8 immunostaining is highest in the "
 "proliferative and prehypertrophic zones and lower in the hypertrophic zone despite Bmp2/Bmp6 mRNA being "
 "highest there, an inversion attributed to hypertrophic-zone SMAD7 (Garrison 2017). No equivalent series "
 "has been published on human growth plate tissue, so the human activity gradient across RZ-PZ-PHZ-HZ is unmeasured.")
n['localization'] = [
 "mouse PZ/PHZ: pSmad1/5/8 highest by immunohistochemistry (garrison2017)",
 "mouse HZ: pSmad1/5/8 lower despite high ligand mRNA; Smad7 high (garrison2017)",
 "human growth plate: unconfirmed - no published zonal pSMAD1/5/8 staining"]
n['key_refs'].insert(0, dict(ref_id='garrison2017', pmid='28467498', first_author='Garrison P', year=2017,
  type='primary', one_line_finding='pSmad1/5/8 activity peaks in mouse PZ/PHZ, not in the hypertrophic zone where BMP ligand mRNA is highest.'))
n['confidence'] = 'C'
save(n)

# ---- tsc1_tsc2: replace with the real experiment ----
n = load('tsc1_tsc2')
n['summary'] = (
 "TSC1-TSC2 is the GTPase-activating complex that holds RHEB in its GDP-bound state and therefore keeps "
 "mTORC1 off; growth-factor signalling through AKT and ERK inactivates it. Chondrocyte-restricted Tsc1 "
 "deletion in mouse - the constitutive mTORC1-on experiment - gives a zone-specific result: the cranial "
 "base synchondroses EXPAND, and the expansion is entirely in the resting zone and is due to increased cell "
 "number and cell size with no change in proliferation rate. Critically, the same study shows that in "
 "wild-type mice mTORC1 activity is INHIBITED in resting and proliferating zone chondrocytes, and that "
 "Tsc1 deletion switches it on there; the resulting resting-zone cells acquire prehypertrophic characteristics "
 "(large size, high PTH1R and IHH), and rapamycin rescues the phenotype (Hsieh 2021, mouse). This makes "
 "TSC1-TSC2 the enforcer of the low-mTORC1 state that defines the resting zone, and identifies mTORC1 "
 "activation as one of the events that converts a resting chondrocyte into a prehypertrophic one. The "
 "converse loss-of-mTORC1 experiments (Raptor/mTor deletion) reduce chondrocyte size and matrix output "
 "(Chen and Long 2014). Human TSC1/TSC2 loss of function causes tuberous sclerosis complex with sclerotic "
 "bone lesions but no characteristic stature phenotype, and no human growth plate has been assayed for "
 "mTORC1 activity by zone.")
n['localization'] = [
 "mouse RZ and PZ: mTORC1 activity normally low, i.e. TSC1-TSC2 active (hsieh2021)",
 "mouse synchondrosis RZ: Tsc1 deletion activates mTORC1 and expands the zone (hsieh2021)",
 "human growth plate: zonal mTORC1 activity unmeasured"]
n['confidence'] = 'C'
n['species_basis'] = ['mouse', 'human']
n['translation_risk_reason'] = ("The decisive experiment is in mouse cranial base synchondroses, not a long-bone "
 "physis, and human TSC patients have no described growth plate phenotype.")
n['key_refs'] = [
 dict(ref_id='hsieh2021', pmid='34365025', first_author='Hsieh YL', year=2021, type='primary',
      one_line_finding='mTORC1 is normally inhibited in resting/proliferating chondrocytes; chondrocyte Tsc1 deletion activates it, expands the resting zone and confers prehypertrophic features, rescued by rapamycin.'),
 dict(ref_id='chen2014', pmid='24948603', first_author='Chen J', year=2014, type='primary',
      one_line_finding='Loss of mTORC1 output in cartilage reduces chondrocyte size and matrix, the phenotype TSC1 loss inverts.'),
 dict(ref_id='zhang2024', pmid='38253890', first_author='Zhang Y', year=2024, type='primary',
      one_line_finding='Rheb1, the direct target of TSC1-TSC2 GAP activity, is required for limb growth via growth plate chondrogenesis.'),
]
save(n)

# ---- mtorc1_chondrocyte: add zonal data ----
n = load('mtorc1_chondrocyte')
n['summary'] = n['summary'].replace(
 "No study has measured phospho-S6 or phospho-4E-BP1 zonally in human growth plate tissue, so the assumption that human hypertrophic chondrocytes are the high-mTORC1 compartment is untested.",
 "Zonally, mouse data show mTORC1 activity is LOW in resting and proliferating chondrocytes and that "
 "forcing it on there (chondrocyte Tsc1 deletion) expands the resting zone and gives its cells "
 "prehypertrophic character, reversibly with rapamycin (Hsieh 2021). No study has measured phospho-S6 or "
 "phospho-4E-BP1 zonally in HUMAN growth plate tissue, so the assumption that human hypertrophic "
 "chondrocytes are the high-mTORC1 compartment is untested.")
n['localization'] = [
 "mouse RZ/PZ: mTORC1 activity low in wild type (hsieh2021)",
 "mouse limb cartilage: mTORC1 activity confirmed during development (chen2014)",
 "human growth plate, zonal phospho-S6/phospho-4E-BP1: unmeasured"]
n['key_refs'].insert(1, dict(ref_id='hsieh2021', pmid='34365025', first_author='Hsieh YL', year=2021,
  type='primary', one_line_finding='mTORC1 activity is normally suppressed in resting and proliferating zone chondrocytes; de-repressing it expands the resting zone.'))
save(n)

# ---- autophagy_chondrocyte: add Srinivas 2009 ----
n = load('autophagy_chondrocyte')
n['summary'] = n['summary'].replace(
 "mTORC1 is the canonical autophagy suppressor but the mTORC1-autophagy link has not been tested genetically in growth plate chondrocytes.",
 "Autophagy is not constitutive across the plate: immunohistochemistry localises the autophagic phenotype "
 "to the postmitotic maturing zone, making it a transient stage of the maturation programme rather than a "
 "background housekeeping state, and pharmacological/siRNA work places its induction under mTOR and AMPK "
 "control in a HIF-1-dependent manner (Srinivas 2009, mouse and chondrocytic cells). The genetic test of "
 "the mTORC1-autophagy link in growth plate chondrocytes in vivo has still not been done.")
n['localization'] = [
 "mouse maturing/postmitotic zone: autophagic phenotype localised by immunohistochemistry (srinivas2009)",
 "human growth plate (cultured tissue slices): autophagy inhibition causes chondrocyte death (vuppalapati2015)",
 "mouse growth plate: Atg5/Atg7 required for chondrocyte survival (vuppalapati2015)"]
n['key_refs'].insert(1, dict(ref_id='srinivas2009', pmid='18703865', first_author='Srinivas V', year=2009,
  type='primary', one_line_finding='Autophagy is a transient stage confined to the postmitotic maturing zone and is regulated by mTOR and AMPK in a HIF-1-dependent way.'))
save(n)

# ---- hypoxic_gradient_signaling: add Schipani 2015 ----
n = load('hypoxic_gradient_signaling')
n['key_refs'].insert(2, dict(ref_id='schipani2015', pmid='26331009', first_author='Schipani E', year=2015,
  type='review', one_line_finding='Review by the group that defined growth plate hypoxia, stating the gradient claim and enumerating what remains unanswered.'))
save(n)
