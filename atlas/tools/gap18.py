import yaml

KNOWN = (
 "READ IN FULL 2026-08-06, five primaries. THE CHEMISTRY SIDE IS NOW MEASURED, NOT ASSUMED. "
 "farquharson1996 quantified pyridinium cross-links by HPLC through sequential transverse sections of "
 "the chick growth plate against ALP and collagen X on the same sections: pyridinoline peaks at 0.55 "
 "residues per collagen molecule in the proliferative zone and collapses to 0.03 exactly at the collagen "
 "X boundary, an 18-fold span, with total pyridinium cross-links recovering only to about 0.12 in the "
 "terminal sections as deoxypyridinoline - absent above - becomes the principal cross-link. So the "
 "network is least cross-linked precisely where the cell begins to expand, which is the direction this "
 "gap predicts. THE SIGN IS CORROBORATED FROM THE FAILURE SIDE: where hypertrophy and resorption FAIL, "
 "in tibial dyschondroplasia, cross-links are HIGH and rise with depth through the lesion "
 "(farquharson1996), and orth1994 finds the same across four unrelated means of inducing that lesion. "
 "THE AXIAL ARCHITECTURE IS REAL AND ROBUST: collagen fibres are significantly aligned with the bone "
 "axis in the proliferative and hypertrophic zones and randomly in the resting zone (fujii2000, p<0.01), "
 "and hypertrophic columns and transphyseal septa run nearly parallel to the diaphyseal axis even where "
 "the plate surface is inclined as much as 60 degrees, which cohen1992 identifies as one of the dominant "
 "microstructural determinants of tensile behaviour. AND THE COMPLIANT PART OF THE PLATE IS THE RIGHT "
 "PART: in rabbit the resting zone is about 80% stiffer in axial tension than the proliferative and "
 "hypertrophic zones (27.0 against 14.9 and 15.1 MPa) and fails at less than half the strain, so the "
 "extensible region is the one that has to accommodate cell expansion (fujii2000).")

MISSING = (
 "THREE THINGS, AND THE FIRST TWO ARE NARROWER THAN THIS GAP PREVIOUSLY CLAIMED - see CORR-012. "
 "(1) CROSS-LINK DENSITY PAIRED WITH MECHANICS IN THE SAME SPECIMENS. Not composition-with-mechanics, "
 "which cohen1992 already did - it regresses ultimate stress and both tangent moduli on collagen content "
 "across anatomical regions of the bovine distal femur and finds more collagen where the plate is "
 "stiffest. The unpaired quantity is specifically CROSS-LINK density, and farquharson1996 shows why the "
 "distinction is not pedantic: through the chick plate collagen concentration varies about 5-fold while "
 "pyridinoline varies about 18-fold, in a different pattern. Pyridinoline HPLC on zone-dissected plate "
 "against mechanical testing of the adjacent block would close it. "
 "(2) THE BETWEEN-PLATE PREDICTION, WHICH NOW HAS ITS FIRST NULL. fujii2000 tested rabbit distal radius "
 "AND ulna from the same 20 animals - two plates of different growth rate, same age - and found ultimate "
 "tensile stress indistinguishable, 1.05 against 1.03 MPa, p>0.1. That is the closest existing test of "
 "this gap's between-plate prediction and it does not support it. It is not a refutation: the predicted "
 "quantity is the TRANSVERSE-to-axial modulus RATIO and what was compared was axial ultimate stress "
 "alone, with modulus pooled across both bones. But the burden has shifted, and any future claim here "
 "has to explain this null. "
 "(3) WHETHER THE HUMAN STEP IS PHYSEAL AT ALL. mudd1985, the 629-patient natural history of CBS "
 "deficiency, is still unread and is the only route to whether homocystinuric tall stature involves the "
 "growth plate or is purely structural dolichostenomelia. NOTE that the objection raised against this "
 "step in CORR-011 has been WITHDRAWN in CORR-012: orth1994 Experiment 3 shows homocysteine-fed birds "
 "have normal HP and normal collagen in non-lesional sternal and articular cartilage, so homocysteine "
 "does not systemically raise cartilage cross-linking. The step is unverified, not contradicted. "
 "ONE OBSERVATION THAT FITS NOTHING YET: in rabbit the resting zone is the LEAST aligned and the "
 "STIFFEST in axial tension, which is the opposite of what load-bearing aligned fibres predict "
 "(fujii2000). Whatever sets zonal modulus in the physis, fibre alignment alone does not explain it, and "
 "that weakens the mechanistic step from 'fibres are axial' to 'the tissue is axially compliant'.")

EXPERIMENT = (
 "REORDERED 2026-08-06 now that the chemistry exists and the between-plate test has returned a null. "
 "(1) REPEAT fujii2000's TWO-PLATE DESIGN MEASURING THE RIGHT QUANTITY. Rabbit or rat radius and ulna, "
 "or the four plates of wilsman1996, one age, measuring the TRANSVERSE-to-axial modulus ratio by the "
 "cohen1998 or wosu2012 protocol rather than axial ultimate stress. If E1/E3 tracks elongation rate "
 "across plates at fixed age, the converter is real and fujii2000's null was a measurement of the wrong "
 "variable. If it does not, this gap closes negative and the anisotropy is a consequence of the "
 "architecture rather than a lever on it. THIS IS NOW THE FIRST EXPERIMENT, because it is the one the "
 "existing evidence has put in doubt. "
 "(2) PAIR PYRIDINOLINE HPLC WITH MECHANICS on adjacent blocks of the same plate, replicating "
 "farquharson1996's chemistry and cohen1992's mechanics in one specimen set. "
 "(3) PERTURB. beta-aminopropionitrile irreversibly inhibits lysyl oxidase; the prediction is lower "
 "transverse stiffness, higher E1/E3, and more elongation per unit of hypertrophic cell volume. The "
 "prediction remains falsifiable and uncomfortable - lathyrism is a disease of skeletal deformity and "
 "aortic dissection, and Lox-null mice die perinatally - and rucklidge1996 reports that BAPN changes the "
 "solubility of growth plate collagen X, so the perturbation demonstrably reaches this tissue.")

for p in ('/home/user/growth-plate/atlas/gaps/shards/l1arch.gaps.yaml',
          '/home/user/growth-plate/atlas/gaps/gaps.yaml'):
    d = yaml.safe_load(open(p))
    for g in d['gaps']:
        if g.get('gap_id') == 'g_l1arch_018':
            g['what_is_known'] = g['what_is_known'].split(' CORRECTED 2026-08-06, SEE CORR-011')[0] + " " + KNOWN
            g['what_is_missing'] = MISSING
            g['discriminating_experiment'] = EXPERIMENT
            g['nearest_evidence'] = ['farquharson1996', 'fujii2000', 'cohen1992', 'williams2001',
                                     'orth1994', 'wosu2012', 'cohen1998', 'rubin2021', 'mudd1985']
            g['nearest_evidence_note'] = (
              "farquharson1996 (the zone-resolved cross-link collapse, chicken, HPLC); orth1994 (the "
              "same sign from the failure side, and the experiment that withdrew CORR-011's objection); "
              "fujii2000 (zonal modulus, collagen content and fibre alignment in rabbit radius AND ulna "
              "from the same animals - and the null on the between-plate prediction); cohen1992 "
              "(composition regressed on mechanics by region, bovine, and the 60-degree column-orientation "
              "observation); williams2001 (physeal tensile properties by age and location, plus the only "
              "human physeal mechanical measurement in this atlas); wosu2012 and cohen1998 (the "
              "anisotropy and its developmental collapse); rubin2021 (isotropic enlargement and the "
              "short-axis-along-the-bone finding, via re-analysis by this atlas); mudd1985 (629-patient "
              "CBS natural history, still unread).")
            g['tractability'] = 2
    yaml.safe_dump(d, open(p, 'w'), sort_keys=False, width=110, allow_unicode=True,
                   default_flow_style=False)
    print('updated', p)
