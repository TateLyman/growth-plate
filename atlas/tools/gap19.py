import yaml

g = {
 'gap_id': 'g_l1arch_019',
 'question': ("Is the fibrillin/TGF-beta axis a GROWTH PLATE mechanism for long bone overgrowth rather "
   "than a connective-tissue one - and if so, is it the largest untapped lever on human height?"),
 'type': 'known_unknown', 'layer': 'L1',
 'why_it_matters': ("This atlas dismissed the entire class on 2026-08-06 and the dismissal was wrong. "
   "Round 17's screen of every human tall-stature gene classified 14 of its 45 hits - FBN1, TGFBR1/2, "
   "TGFB2/3, SKI, the fibrillar collagens, AGTR1 - as 'connective tissue: tall by dolichostenomelia, a "
   "structural defect, not a growth plate that runs faster or longer', and set them aside. That was an "
   "assumption stated as a classification. It is the single largest block in the screen, it contains "
   "the only approved drug in the whole list that acts on the axis (losartan, an AT1 blocker used in "
   "Marfan to reduce TGF-beta signalling), and the direction is known - which is more than can be said "
   "for anything else the screen returned. If the overgrowth is physeal, this is a mapped, drugged, "
   "human-validated pathway to long bone length that nobody has read as such."),
 'what_is_known': ("THE EVIDENCE THAT BROKE THE CLASSIFICATION CAME FROM HOMOCYSTINURIA, WHICH SHARES "
   "THE AXIS BY A DIFFERENT ROUTE. (i) The overgrowth is postnatal and therefore physeal: an Irish "
   "cohort of 48 pyridoxine-nonresponsive patients has NORMAL BIRTH WEIGHT and reaches about +1 SD "
   "above the population in height and weight with no BMI difference, and within the disease the "
   "late-diagnosed are 7.97 cm taller at 18 years than the newborn-screened (P=0.0204), the divergence "
   "complete before age 10 (purcell2017). Length accrued after birth is length accrued at the growth "
   "plate. (ii) The animal counterpart localises it: chicks fed 0.6% homocysteine for 8 weeks grow "
   "faster with SIGNIFICANTLY LONGER TIBIAE (P<0.01) and radiographic ACCELERATED EPIPHYSEAL "
   "OSSIFICATION, described by the authors as epiphyseal growth plate lesions; the bones are stronger "
   "only in proportion to their extra length and cortical thickness, so nothing about the material "
   "changed (mass2003). (iii) The molecular target is FIBRILLIN-1, the Marfan protein: "
   "homocysteinylation but not cysteinylation disrupts fibrillin-1 multimerisation and greatly reduces "
   "microfibril network deposition by human fibroblasts, and the authors note that Marfan and "
   "homocystinuria share long bone overgrowth, scoliosis and ectopia lentis from unrelated origins "
   "(hubmacher2010). (iv) It is NOT the collagen cross-link route of g_l1arch_018: homocysteine leaves "
   "cross-links in non-lesional cartilage unchanged (orth1994, Experiment 3)."),
 'what_is_missing': ("THE PHYSEAL STEP ITSELF, IN THE FIBRILLIN AXIS PROPER. Everything above reaches "
   "the growth plate through homocystinuria; nobody has shown that FBN1 or TGF-beta perturbation "
   "lengthens bone BY ACTING ON THE PHYSIS rather than on periosteum, bone modelling or soft tissue. "
   "Specifically absent: (1) growth plate histomorphometry in a Marfan model or patient - zone heights, "
   "proliferative cell number per column, terminal cell size - against controls; (2) any measurement of "
   "growth VELOCITY, as opposed to attained length, in a fibrillin-deficient animal; (3) whether "
   "losartan or any TGF-beta-lowering agent changes long bone length in a growing animal, which would "
   "establish the direction pharmacologically and is almost certainly recoverable from existing Marfan "
   "mouse work that measured aorta and not limbs; (4) whether the fibrillin effect is on velocity or on "
   "DURATION - purcell2017 finds no difference in growth rate after age 10, which hints the effect is "
   "prepubertal velocity rather than delayed fusion, but the study was not designed to separate them. "
   "AND THE OBVIOUS PROBLEM WITH THE WHOLE CLASS: this axis is the aortic aneurysm axis. Marfan, "
   "Loeys-Dietz and homocystinuria all buy their height alongside aortic root dilatation, ectopia "
   "lentis, scoliosis and osteoporosis, and losartan exists to push the axis the OTHER way. Any lever "
   "found here runs toward a disease, not away from one, and that has to be said plainly rather than "
   "discovered later."),
 'nearest_evidence': ['purcell2017', 'mass2003', 'hubmacher2010', 'orth1994', 'mudd1985'],
 'nearest_evidence_note': ("purcell2017 (the quantified human height, postnatal timing and within-"
   "disease dose-response); mass2003 (longer tibiae and accelerated epiphyseal ossification in chick); "
   "hubmacher2010 (fibrillin-1 as the molecular target, in vitro); orth1994 (excludes the collagen "
   "cross-link route); mudd1985 (the 629-patient natural history that reports no stature data at all, "
   "which is why this took so long to see)."),
 'discriminating_experiment': ("THE CHEAPEST DECISIVE STEP IS A LITERATURE ONE AND SHOULD BE DONE "
   "FIRST: Marfan mouse models have been characterised extensively for aortic and skeletal phenotype, "
   "and several report long bone length. Extract limb length and, where available, growth plate "
   "histology from the existing Fbn1 hypomorph and Fbn1 C1039G literature and ask whether the "
   "overgrowth tracks physeal zone heights. If it does, the classification of round 17 inverts and 14 "
   "of the 45 screen hits become live. THEN THE EXPERIMENT: give a growing wild-type animal a "
   "TGF-beta-lowering agent already used in Marfan - losartan is the obvious one, it is approved, and "
   "its skeletal effect in a normal growing animal appears never to have been the endpoint of any study "
   "- and measure long bone length and growth plate histomorphometry against controls. The prediction "
   "that makes it worth running is DIRECTIONAL AND UNCOMFORTABLE: if the fibrillin/TGF-beta axis drives "
   "physeal elongation, losartan should SHORTEN bones in a normal growing animal, which would be both a "
   "confirmation of the mechanism and a safety signal for every child on losartan for Marfan. That "
   "second consequence is the reason to look at the existing paediatric Marfan trial data for height "
   "before running anything new."),
 'tractability': 1,
}

for p in ('/home/user/growth-plate/atlas/gaps/shards/l1arch.gaps.yaml',
          '/home/user/growth-plate/atlas/gaps/gaps.yaml'):
    d = yaml.safe_load(open(p))
    if not any(x.get('gap_id') == 'g_l1arch_019' for x in d['gaps']):
        d['gaps'].append(g)
    yaml.safe_dump(d, open(p, 'w'), sort_keys=False, width=110, allow_unicode=True,
                   default_flow_style=False)
    print('added g_l1arch_019 to', p)

# strip the homocystinuria step out of gap 018 - it was never that mechanism
for p in ('/home/user/growth-plate/atlas/gaps/shards/l1arch.gaps.yaml',
          '/home/user/growth-plate/atlas/gaps/gaps.yaml'):
    d = yaml.safe_load(open(p))
    for x in d['gaps']:
        if x.get('gap_id') == 'g_l1arch_018':
            x['what_is_missing'] = x['what_is_missing'].split(
                "(3) WHETHER THE HUMAN STEP IS PHYSEAL AT ALL.")[0] + (
              "(3) THE HUMAN STEP HAS BEEN REMOVED FROM THIS GAP ENTIRELY, 2026-08-06. It rested on "
              "homocystinuria, and homocystinuria turns out to act on FIBRILLIN-1 rather than on "
              "collagen cross-linking (hubmacher2010), while leaving cartilage cross-links unchanged "
              "(orth1994). Its overgrowth is real, postnatal and quantified (purcell2017, mass2003) but "
              "it belongs to the fibrillin/TGF-beta axis and is now tracked in g_l1arch_019. THIS GAP "
              "THEREFORE HAS NO HUMAN STEP AT ALL and rests entirely on animal mechanics: a "
              "zone-resolved cross-link collapse in chicken, an axial architecture in rabbit and "
              "cattle, an anisotropy collapse in pig and cattle, and an isotropic-enlargement "
              "re-analysis in mouse. That is a weaker gap than it was this morning, and it should be "
              "carried on the animal evidence honestly rather than on a human anchor that was never "
              "attached to it.")
    yaml.safe_dump(d, open(p, 'w'), sort_keys=False, width=110, allow_unicode=True,
                   default_flow_style=False)
print('gap 018 human step removed')
