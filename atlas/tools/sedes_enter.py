import yaml, glob

p = [x for x in glob.glob('/home/user/growth-plate/atlas/nodes/**/*.yaml', recursive=True)
     if x.endswith('/perichondrial_tgfb_restraint.yaml')][0]
d = yaml.safe_load(open(p))

# replace the abstract-derived rows with full-text rows
d['quantitative'] = [r for r in d['quantitative']
                     if not r['parameter'].startswith(('tissue responsible', 'effect of restoring'))]

d['quantitative'] = [
 {'parameter': 'limb bone overgrowth from fibrillin-1 loss in limb mesenchyme',
  'value': 'about 7',
  'unit': '% greater length than wild-type littermates',
  'conditions': ('Fbn1 inactivated in early limb mesenchyme with Prx1-Cre; tibia, humerus and ulna at 3 '
    'months (n=5-6 per genotype) and femur at 1, 2 and 3 months (n=4-10 per genotype). Bones were '
    'UNREMARKABLE AT BIRTH and became gradually longer between 1 and 3 months'),
  'species': 'mouse', 'source_ref': 'sedes2022',
  'uncertainty': ('IN VIVO LIMB LENGTH, which the abstract does not mention and which this atlas '
    'previously recorded as missing. Normal at birth with divergence over the postnatal growth period '
    'means the effect is on growth itself rather than on patterning. The authors anchor it to humans by '
    'citing an early report that Marfan adolescents average an ~8% increase in height over the general '
    'population - a CITATION, not a measurement in this paper, and not verified here.')},
 {'parameter': 'which tissue carries the overgrowth, by conditional deletion',
  'value': 'Scx lineage YES; osteoblast NO; CHONDROCYTE NO',
  'unit': 'femur length at 3 months, significant or not',
  'conditions': ('femur length in wild-type (n=20), Fbn1-Osx-/- (osteoblast, n=9), Fbn1-Col2-/- '
    '(chondrocyte, n=6) and Fbn1-Scx+/- (scleraxis lineage, n=9) mice. Tibia, humerus and ulna were '
    'also longer in Fbn1-Scx+/- (n=10 WT vs 6 mutant)'),
  'species': 'mouse', 'source_ref': 'sedes2022',
  'uncertainty': ('THE NEGATIVE CONTROL IS THE POINT AND IT IS DECISIVE FOR THIS WHOLE FIELD: deleting '
    'fibrillin-1 from the CHONDROCYTES THEMSELVES - the growth plate - produces NO overgrowth, while '
    'deleting it from the scleraxis lineage does. The control of long bone length here is EXTRINSIC to '
    'the plate. Any account that looks only inside the growth plate cannot explain the most conspicuous '
    'skeletal phenotype in Marfan syndrome. Caveat: Col2 n=6 is small for a negative, and Scx+/- is a '
    'heterozygote while Osx and Col2 are homozygous nulls, so the comparison is not dose-matched.')},
 {'parameter': 'growth plate phenotype from perichondrial fibrillin-1 loss',
  'value': ('proliferative zone length UNCHANGED; hypertrophic zone significantly EXPANDED; '
            'proliferation and hypertrophic transit both increased'),
  'unit': 'zone length and EdU labelling',
  'conditions': ('Fbn1-Scx-/- versus wild-type tibia at P4 and P10 (n=14-17 and 13-15 per genotype); '
    'no PZ difference at either timepoint; HZ expanded between P4 and P10 with a matching expansion of '
    'the type X collagen expressing zone; EdU gave MORE proliferating PZ cells at 3 h (n=5-6) and MORE '
    'EdU-positive HZ cells at 72 h (n=5). Longer HZ also seen in P4 ribs (n=10-12) and in metatarsal '
    'rudiments cultured 14 days (n=19-40)'),
  'species': 'mouse', 'source_ref': 'sedes2022',
  'uncertainty': ('A DUAL-TERM EFFECT, WHICH IS RARE IN THIS LITERATURE. Proliferation rises AND the '
    'hypertrophic compartment expands, while proliferative zone LENGTH stays fixed. In the flow model '
    'those are separate multiplicative terms, so an intervention that moves both is worth more than one '
    'that moves either. THE AMBIGUITY THAT REMAINS IS THE SAME ONE hunziker1989 AND wilsman1996 TURN '
    'ON: an expanded hypertrophic zone with more EdU-positive cells at 72 h is consistent with faster '
    'transit AND with slower clearance at the chondro-osseous junction, and this paper does not '
    'separate them.')},
 {'parameter': 'TGF-beta1 add-back that normalises mutant elongation',
  'value': '2',
  'unit': 'ng/ml recombinant mouse TGF-beta1',
  'conditions': ('newborn metatarsal rudiments in alphaMEM with BSA, ascorbate, beta-glycerophosphate, '
    'medium changed daily, length by ImageJ over a 14-day culture; total TGF-beta1 in conditioned '
    'medium by ELISA. Mutant metatarsals grew longer and released less TGF-beta1 than wild-type'),
  'species': 'mouse', 'source_ref': 'sedes2022',
  'uncertainty': ('THE CAUSAL STEP: a correlation between low TGF-beta and long bones could run either '
    'way; an add-back that normalises growth cannot. One concentration, no dose-response reported, '
    'organ culture rather than a living animal, and metatarsals rather than a weight-bearing long bone.')},
 {'parameter': 'where fibrillin-1 and the latent TGF-beta binding proteins sit',
  'value': 'exclusively in the OUTER layer of the perichondrium; LTBP-3 and LTBP-4 reduced, LTBP-1 not',
  'unit': 'immunohistochemical signal intensity',
  'conditions': 'immunohistochemistry of fibrillin-1 with LTBP-1, -3 and -4 in mouse perichondrium',
  'species': 'mouse', 'source_ref': 'sedes2022',
  'uncertainty': ('The selectivity for LTBP-3 and -4 over LTBP-1 matches what the same group found in '
    'the fibrillin-1-deficient aorta, so the sequestration defect is a property of the fibrillin-LTBP '
    'interaction rather than of this tissue.')},
 {'parameter': 'transcriptional consequence in the fibrillin-1-deficient perichondrium',
  'value': '1114 genes down, 529 up; TGF-beta signalling predicted DOWN and KDM5A predicted UP',
  'unit': 'differentially expressed genes',
  'conditions': ('RNA-seq of perichondral tissue isolated by laser capture microdissection from P4 '
    'Fbn1-Scx-/- and wild-type mice; Reactome enrichment dominated by ECM assembly including elastic '
    'and collagen fibre formation; qPCR confirmed significant decreases in Tgfb1 and its targets Col1a1 '
    'and SerpinF1'),
  'species': 'mouse', 'source_ref': 'sedes2022',
  'uncertainty': ('KDM5A, A HISTONE DEMETHYLASE, CAME OUT AS THE JOINT TOP DYSREGULATED PATHWAY AND THE '
    'AUTHORS EXPLICITLY DID NOT PURSUE IT - "KDM5A contribution to bone lengthening was not further '
    'explored in this study". That is a named, unexplored lead on long bone length sitting in the '
    'paper that solved the mechanism, and it is druggable as a class.')},
 {'parameter': 'prior organ-culture result the mechanism explains',
  'value': 'perichondrium removal lengthens bones; recombinant TGF-beta shortens them',
  'unit': 'qualitative, embryonic bone rudiment culture',
  'conditions': ('cited by sedes2022 as established prior work, with the perichondrium shown to mediate '
    'the inhibitory effect of exogenous TGF-beta on BOTH proliferation and terminal differentiation of '
    'growth plate chondrocytes'),
  'species': 'mouse', 'source_ref': 'sedes2022',
  'uncertainty': ('SECONDARY CITATION, not measured in sedes2022 - recorded because it means the '
    'direction was known in organ culture long before the fibrillin mechanism was found, and because '
    'the double action on proliferation and differentiation is what makes this a two-term lever.')},
] + d['quantitative']

d['confidence'] = 'B'
d['confidence_note'] = (
 "RAISED C to B on 2026-08-06 after reading sedes2022 in full rather than from its abstract. The "
 "abstract describes organ culture; the paper reports IN VIVO limb length across four conditional "
 "deletions with a chondrocyte-specific NEGATIVE control, a growth plate phenotype at two postnatal "
 "timepoints with EdU, laser-capture RNA-seq of the responsible tissue, and a TGF-beta1 add-back "
 "rescue. B rather than A because it is one laboratory, one species, and no measurement of the axis "
 "exists in a human growth plate.")
d['last_verified'] = '2026-08-06'
yaml.safe_dump(d, open(p, 'w'), sort_keys=False, width=112, allow_unicode=True,
               default_flow_style=False)
print('perichondrial_tgfb_restraint:', len(d['quantitative']), 'rows, confidence', d['confidence'])
