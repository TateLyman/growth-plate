import yaml, glob

def node(nid):
    return [x for x in glob.glob('/home/user/growth-plate/atlas/nodes/**/*.yaml', recursive=True)
            if x.endswith(f'/{nid}.yaml')][0]

def add(nid, rows):
    p = node(nid)
    d = yaml.safe_load(open(p))
    d.setdefault('quantitative', []).extend(rows)
    d['last_verified'] = '2026-08-06'
    krefs = {r['ref_id'] for r in d.get('key_refs', [])}
    yaml.safe_dump(d, open(p, 'w'), sort_keys=False, width=112, allow_unicode=True,
                   default_flow_style=False)
    print(f'  {nid}: +{len(rows)} rows, now {len(d["quantitative"])}')

add('collagen_crosslinking', [
 {'parameter': 'pyridinoline cross-link concentration through the growth plate',
  'value': 'peak 0.55 in the proliferative zone falling to 0.03 at the collagen X boundary',
  'unit': 'residues per collagen molecule',
  'conditions': ('chick proximal tibiotarsus, sequential transverse sections, reverse-phase HPLC with '
    'hydroxyproline in the same hydrolysate as the collagen denominator; zones assigned by ALP '
    'histochemistry and collagen X immunostaining on the same sections. Articular cartilage sits at '
    '0.30-0.37 and peaks at 0.55 in the proliferative zone (section 9); ALP first appears at section 11 '
    '(0.21), collagen X at section 14 (0.03)'),
  'species': 'chick', 'source_ref': 'farquharson1996',
  'uncertainty': ('THE MEASUREMENT THIS ATLAS TWICE SAID DID NOT EXIST. Values read from Fig. 1A; the '
    'paper states the comparison as approximately 10-fold between sections without collagen X (N9-N11) '
    'and those with it (N14-N16), and the peak-to-trough span in the figure is about 18-fold. The '
    'minimum falls exactly at the onset of collagen X, i.e. at hypertrophic entry. DEOXYPYRIDINOLINE '
    'RUNS THE OTHER WAY: absent from articular cartilage and the upper plate, first detected in the '
    'ALP-positive prehypertrophic zone, and the principal cross-link in the most differentiated '
    'sections. So this is not a simple loss of cross-linking but a collapse and partial recovery with a '
    'SWITCH OF CROSS-LINK TYPE - total pyridinium cross-links fall from ~0.55 to ~0.03 and recover only '
    'to ~0.12. THE AUTHORS DRAW A DIFFERENT CONCLUSION FROM THE SAME DATA: they read the fall as an '
    'adaptation permitting vascular invasion and osteoclastic resorption, via increased collagenase '
    'activity and collagen turnover, not as a softening that permits the cell to expand. Both readings '
    'fit; nothing here distinguishes them.')},
 {'parameter': 'cross-link concentration where hypertrophic differentiation FAILS',
  'value': 'rises progressively through the lesion to about 0.45',
  'unit': 'residues per collagen molecule, total pyridinium',
  'conditions': ('chick tibial dyschondroplasia, a lesion in which chondrocytes arrest in the '
    'prehypertrophic state and unmineralised avascular cartilage accumulates; same sectioning and HPLC '
    'as the normal plate above'),
  'species': 'chick', 'source_ref': 'farquharson1996',
  'uncertainty': ('The sign is the informative part: where hypertrophy and resorption FAIL, cross-links '
    'are HIGH and rise with depth, against the collapse seen in the normal plate. orth1994 reports the '
    'same direction independently and across four different means of inducing the lesion. This is '
    'correlative in both papers - no one has manipulated cross-linking and measured hypertrophy.')},
 {'parameter': 'hydroxylysylpyridinoline in dyschondroplastic versus normal growth plate cartilage',
  'value': 'over 10-fold greater in the lesion',
  'unit': 'moles per mole collagen',
  'conditions': ('broiler chicks; tibial dyschondroplasia induced four separate ways - genetic '
    'predisposition, copper-deficient diet, thiram, and dietary homocysteine. ALL methods raised '
    'collagen and HP concentration in the lesion over normal growth plate cartilage'),
  'species': 'chick', 'source_ref': 'orth1994',
  'uncertainty': ('THE FOUR-CAUSE DESIGN IS WHAT MAKES THIS INTERPRETABLE: because genetic, copper, '
    'thiram and homocysteine induction all raise cross-links, the elevation is a property of the '
    'LESION, not of any one causative agent. The authors read the heavily cross-linked matrix as '
    'inhibiting collagenolysis and vascular penetration.')},
 {'parameter': 'effect of dietary homocysteine on cross-linking in NON-lesional cartilage',
  'value': 'none. sternal 0.355 vs 0.409; articular 0.603 vs 0.573',
  'unit': 'moles HP per mole collagen (homocysteine-fed vs control)',
  'conditions': ('broiler chicks fed a high-homocystine diet and developing tibial dyschondroplasia, '
    'against corn/soybean controls, n=5 per group; sternal and articular cartilage assayed rather than '
    'the lesion. Collagen concentration also unchanged (sternal 266 vs 273, articular 417 vs 439 ug/mg '
    'dry weight)'),
  'species': 'chick', 'source_ref': 'orth1994',
  'uncertainty': ('THIS ROW WITHDRAWS CORR-011 PART 2. That correction, written from the abstract '
    'alone, took orth1994 to show that homocysteine RAISES cartilage cross-linking and therefore that '
    'the homocystinuria step of g_l1arch_018 ran backwards. Experiment 3 of the same paper shows the '
    'opposite: in homocysteine-fed birds the non-lesional cartilage is normal in both HP and collagen. '
    'The paper says so plainly - the cartilage "appeared normal, having similar HP concentrations". So '
    'homocysteine does NOT systemically raise cartilage cross-linking, and the objection is void. What '
    'orth1994 actually shows is that dyschondroplastic lesions of any cause are hyper-cross-linked.')},
])

add('zonal_stiffness_gradient', [
 {'parameter': 'tangent modulus by zone, tension along the growth axis',
  'value': 'resting 27.0; proliferating 14.9; hypertrophic 15.1; whole plate 17.7',
  'unit': 'MPa',
  'conditions': ('rabbit distal radius and ulna, 20 animals aged 8 weeks, epiphysis-growth '
    'plate-metaphysis complex loaded to failure with four dye markers tracked by video dimension '
    'analyser so strain could be resolved per zone'),
  'species': 'rabbit', 'source_ref': 'fujii2000',
  'uncertainty': ('mean +/- SE. The RESTING zone is roughly 80% stiffer than the two zones below it, '
    'and it fails at less than half the strain (0.043 against 0.081 and 0.096) with under half the '
    'energy absorption (32.9 against 66.2 and 88.5 kJ/m3). So the compliant, extensible part of the '
    'plate is the proliferative-plus-hypertrophic region - the part that has to accommodate cell '
    'expansion.')},
 {'parameter': 'collagen fibre orientation by zone',
  'value': 'proliferative and hypertrophic fibres aligned parallel to the long axis; resting random',
  'unit': 'ellipse long/short axis ratio, direction relative to the bone axis',
  'conditions': 'same rabbit specimens; fibre architecture scored microscopically per zone',
  'species': 'rabbit', 'source_ref': 'fujii2000',
  'uncertainty': ('p<0.01 for longitudinal alignment in proliferative and hypertrophic zones; the mean '
    'direction did not differ significantly between zones but the CONCENTRATION of directions did. '
    'AWKWARD FOR ANY SIMPLE FIBRE-ALIGNMENT ACCOUNT OF STIFFNESS: the resting zone is the least aligned '
    'and the STIFFEST in axial tension, which is the opposite of what aligned load-bearing fibres would '
    'predict. Whatever sets the zonal modulus here, it is not fibre alignment alone.')},
 {'parameter': 'total collagen by zone',
  'value': 'radius 250.6, 294.5, 399.6, 332.7, 207.2; ulna 234.2, 273.8, 345.6, 267.5, 207.2',
  'unit': 'ug hydroxyproline per mg dry tissue, zones I-V epiphyseal to metaphyseal',
  'conditions': 'rabbit distal radius and ulna, same animals as the mechanical testing',
  'species': 'rabbit', 'source_ref': 'fujii2000',
  'uncertainty': ('Collagen peaks in the middle of the plate (zone III) and falls by roughly half at '
    'the metaphyseal end in both bones. Note the collagen peak does not coincide with the stiffness '
    'peak, which is at the epiphyseal end.')},
 {'parameter': 'ultimate tensile stress, radius versus ulna in the same animals',
  'value': '1.05 vs 1.03',
  'unit': 'MPa',
  'conditions': ('rabbit distal radial and ulnar growth plates, 20 animals, both plates from each '
    'animal; cross-sectional areas 29.7 and 27.9 mm2'),
  'species': 'rabbit', 'source_ref': 'fujii2000',
  'uncertainty': ('NOT SIGNIFICANTLY DIFFERENT, p>0.1. THIS IS A NULL RESULT AGAINST g_l1arch_018 AND '
    'IS THE CLOSEST EXISTING TEST OF ITS BETWEEN-PLATE PREDICTION: two plates of different growth rate, '
    'same animals, same age - and no difference in axial tensile strength. It is not a direct '
    'refutation, because the quantity predicted to differ is the transverse-to-axial modulus RATIO and '
    'what was compared here is axial ultimate stress alone, with the modulus pooled across both bones. '
    'But nothing in this dataset supports the prediction either.')},
 {'parameter': 'change in physeal tensile properties with age',
  'value': '25% thinner, 34% stronger, 65% greater failure strain in the older animals',
  'unit': '% change, 5-month calves to 12-18-month heifers',
  'conditions': ('bovine proximal tibia, 21 specimens from 12-18-month and 19 from 5-month animals, '
    'four matched anatomic sites, tension at 0.004 mm/s'),
  'species': 'bovine', 'source_ref': 'williams2001',
  'uncertainty': ('The plate gets axially STRONGER as the animal ages and growth slows. Consistent in '
    'direction with wosu2012, where the transverse-to-axial modulus ratio collapses over development, '
    'but NOT the same measurement - wosu2012 measured transverse tension and out-of-plane compression, '
    'this is axial tension - and the two should not be pooled.')},
 {'parameter': 'human physeal tensile strength against bovine',
  'value': 'about twice as thick and about half as strong, with similar ultimate strain',
  'unit': 'relative to bovine proximal tibia',
  'conditions': ('8 samples from the femoral capital growth plate of two cerebral palsy patients, '
    'tested identically to the bovine specimens'),
  'species': 'human', 'source_ref': 'williams2001',
  'uncertainty': ('A RARE HUMAN PHYSEAL MECHANICAL MEASUREMENT and the only one this atlas holds. Two '
    'patients, both with cerebral palsy, so the specimens come from limbs with abnormal loading history '
    'and probably abnormal growth; capital femoral physis, not a long-bone metaphyseal plate. Directional '
    'only - no absolute value is quoted here because the sample cannot support one.')},
])

add('cartilage_septum_resorption', [
 {'parameter': 'orientation of hypertrophic cell columns relative to the bone axis',
  'value': 'nearly parallel to the diaphyseal axis regardless of the local plate surface angle',
  'unit': 'qualitative, with the plate surface inclined up to 60 degrees',
  'conditions': ('bovine distal femur, ~12-month animals, 12 femora; gross morphology by hypochlorite '
    'maceration plus histology, alongside 86 tensile tests'),
  'species': 'bovine', 'source_ref': 'cohen1992',
  'uncertainty': ('The columns and transphyseal septa stay axial even where the primary contour of the '
    'physis is inclined as much as 60 degrees to the diaphyseal axis, so the axial architecture is '
    'independent of the plate surface geometry. The authors identify column orientation as one of the '
    'dominant microstructural features governing tensile behaviour of the bone-plate-bone specimen.')},
 {'parameter': 'relationship between composition and tensile properties across anatomical regions',
  'value': 'greater collagen content in the regions that were stiffest and strongest',
  'unit': 'qualitative correlation',
  'conditions': ('bovine distal femoral physis, regions compared for ultimate stress and two tangent '
    'moduli against water content, sulfated GAG and hydroxyproline measured on adjacent tissue'),
  'species': 'bovine', 'source_ref': 'cohen1992',
  'uncertainty': ('PARTLY WITHDRAWS THE REVISED CLAIM IN g_l1arch_018 that no one has paired '
    'composition with mechanics in the same growth plate: cohen1992 does exactly that, by anatomical '
    'region, with least-squares regression of both material properties on collagen content. What is '
    'still unpaired is CROSS-LINK density specifically - collagen content and cross-link density are '
    'different quantities, and farquharson1996 shows they can move independently, since collagen '
    'concentration varies about 5-fold through the chick plate while pyridinoline varies about 18-fold '
    'and in a different pattern.')},
])
