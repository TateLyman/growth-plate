#!/usr/bin/env python3
"""
THE OPEN-QUESTION LEDGER - every question this programme has opened since round
199, what would close it, and who can get it.

WHY THIS TOOL EXISTS
--------------------
The user has asked repeatedly to keep track of every question opened. Gaps have
been going into the shard files round by round without a consolidated view, and
at 393 gaps the file cannot be read as a to-do list. This prints the ones THIS
PROGRAMME opened, ranked by whether answering them changes what we do.

RANKING RULE. A question scores on three things and nothing else:
  DECIDES   does the answer change an agent's place in the stack?
  GETTABLE  can it be answered from existing data, or does it need new work?
  SIZE      how much height is at stake if the answer goes the good way?
"""

# id, round opened, one-line question, status, what would close it, who can get it
LEDGER = [
    ("g_l1_are_the_hterm_agents_in_the_stack_additive_or_saturating", 202,
     "Do the h_term agents share one ceiling?",
     "REFRAMED round 208 - the question was wrong",
     "A combination arm with terminal cell height measured. AN ENUMERATED SEARCH THIS "
     "ROUND FOUND NONE IN EXISTENCE. But round 208 showed GH has no demonstrated h_term "
     "effect above a NORMAL baseline at all, so there is nothing for a second agent to "
     "add to. The live version is whether the hedgehog and natriuretic arms share a "
     "ceiling - never given together.",
     "NEW ANIMAL WORK. Nobody has this."),

    ("g_l12_does_a_cnp_agent_change_terminal_cell_height_or_matrix", 203,
     "Does a CNP agent move cells, cell height, or matrix?",
     "OPEN - partially answered",
     "wendt2015 gave cells/column (DOWN) and a projected AREA (up, n.s.) in primate. "
     "Still missing an AXIAL cell height under any CNP agonist. The cheap version needs "
     "no animals - re-measure on the existing hirota2018 or nakao2015 histology.",
     "SECTIONS EXIST at the original labs. Not obtainable by us."),

    ("g_l12_why_does_the_cnp_axis_lengthen_limb_but_not_spine_in_primates", 205,
     "Why is the CNP axis appendicular-biased?",
     "UPGRADED to a three-species pattern, mechanism still open",
     "NPR2 expression in vertebral against appendicular growth cartilage in the same "
     "individuals. Round 208 adds the contrast that matters - FGFR3 inhibition DOES grow "
     "lumbar vertebrae, so the bias is CNP-specific rather than a property of the axial "
     "plate.",
     "PARTLY GETTABLE - avijgan2026 and chu2026 deposited human data may carry vertebral "
     "tissue; worth a re-analysis attempt."),

    ("g_l12_does_growth_plate_cartilage_deconjugate_polyphenol_glucuronides", 206,
     "Does cartilage carry the enzyme that activates polyphenol glucuronides?",
     "DOWNGRADED round 207 - enzyme localised to marrow",
     "A fluorogenic MUG assay on microdissected growth plate zones. One afternoon of work "
     "on archived sections.",
     "NEW BENCH WORK, but trivial. Any lab with rat growth plate sections."),

    ("g_l12_does_an_intra_articular_nanoparticle_reach_the_growth_plate", 206,
     "Can a nanoparticle reach the growth plate?",
     "LARGELY ANSWERED and the answer is yes, by a better route",
     "ye2026 already did it - chondrocyte-membrane-coated collagen-II-targeting particles "
     "delivered a hedgehog agonist SYSTEMICALLY to growth plate cartilage and raised body "
     "length. The residual is quantitative - delivery is reported only as normalised DiR "
     "fluorescence, with no absolute concentration, no AUC, no half-life.",
     "PUBLISHED. The residual needs the authors' raw data."),

    ("g_l12_can_resveratrol_or_a_bioavailable_analogue_reach_the_plate_in_humans", 205,
     "Can resveratrol reach the plate?",
     "OPEN - the barrier moved but did not disappear",
     "Resveratrol parent, glucuronide AND sulfate measured in microdissected growth plate "
     "after an oral dose. Round 206 made the glucuronide the interesting species rather "
     "than a loss term; round 207 put the activating enzyme in marrow.",
     "NEW WORK. A sweep found no such measurement in any species."),

    ("g_l12_does_fgfr_inhibition_change_chondrocyte_lysosomal_enzyme_handling", 207,
     "Does erdafitinib change chondrocyte lysosomal enzyme handling?",
     "OPEN - direction undetermined",
     "MUG assay on cell lysate against conditioned medium under an FGFR inhibitor. Same "
     "assay as the polyphenol question, so one experiment serves both.",
     "NEW BENCH WORK, trivial."),

    ("g_l9_per_site_remaining_growth_at_late_bone_age", 203,
     "How many centimetres remain AT EACH SITE at bone age 16?",
     "OPEN - and it blocks all arithmetic",
     "Re-analyse any existing paediatric EOS or scanogram cohort for FEMUR and TIBIA "
     "lengths against Sanders stage. The images already exist; the studies simply reported "
     "the spine.",
     "RETROSPECTIVE, essentially free, but needs a clinical cohort."),

    ("g_l2_what_is_the_second_signal_that_converts_an_alerted_pool_into_columns", 201,
     "What converts an expanded pool into columns?",
     "OPEN - still the binding constraint on the reserve route",
     "Pool expander plus each candidate second signal, reading the Hunziker five. The "
     "decisive readout is pool CONSUMPTION rate, not zone height.",
     "NEW ANIMAL WORK."),

    ("g_l2_is_the_growth_plate_reserve_held_in_g0_or_in_galert", 201,
     "Is the reserve in G0 or already alerted?",
     "OPEN",
     "Phospho-S6 and phospho-4E-BP1 immunostaining on archived human growth plate "
     "sections, staged by zone. No new tissue needed.",
     "SECTIONS EXIST at Karolinska."),

    ("g_l4_does_dio2_set_resting_zone_quiescence_in_the_growth_plate", 201,
     "Does the D2-T3-Notch axis guard the human reserve?",
     "OPEN - compartment established, function not",
     "D2 and NOTCH2 protein immunostaining by zone on human sections already held, then a "
     "cartilage-conditional Dio2 deletion with a FINAL BONE LENGTH endpoint.",
     "STEP ONE NEEDS EXISTING SECTIONS; step two is new animal work."),

    ("g_l1_do_the_extra_hypertrophic_cells_under_npr3_loss_cost_divisions", 202,
     "Do NPR3-loss extra hypertrophic cells cost divisions?",
     "OPEN",
     "Calcein plus EdU in Npr3-null against wild-type siblings - both methods the same "
     "authors already run in the same paper on other animals.",
     "NEW ANIMAL WORK, but a small addition to an existing model."),

    ("g_l6_does_unilateral_paediatric_fracture_raise_growth_in_the_uninjured_limb", 201,
     "Is post-fracture overgrowth systemic or regional?",
     "OPEN - and structurally invisible",
     "Absolute limb lengths and sitting height after unilateral fracture, against "
     "normative data rather than the other leg. THE UPPER LIMB IS THE CLEAN DISCRIMINATOR "
     "because no vascular account reaches the humerus from a tibial fracture.",
     "RETROSPECTIVE, free, needs a trauma cohort."),

    ("g_l12_does_npr3_occupancy_preserve_the_vascular_gi_arm", 209,
     "Does an OCCUPYING NPR-C ligand preserve the Gi arm an antagonist would block?",
     "CLOSED round 211 - and the answer is NO",
     "ANSWERED. smith2022, human NPR-C in HeLa - osteocrin at 100 nM is SILENT on "
     "forskolin-stimulated cAMP and REVERSES the fall produced by the agonist cANF(4-23), "
     "exactly as M372049 does; in rat aorta and mouse mesenteric artery it BLOCKS "
     "cANF(4-23)-induced vasorelaxation. Osteocrin is a Gi-silent occupier. The general "
     "form survives - cANF(4-23) IS an occupying ligand that engages Gi - but osteocrin "
     "is not that molecule. CORR-204.",
     "ALREADY IN THE BIBLIOGRAPHY SINCE 2026-08-08, UNREAD. CORR-205."),

    ("g_l12_does_npr_c_couple_to_gi_in_growth_plate_chondrocytes", 211,
     "Does NPR-C couple to Gi in a CHONDROCYTE, and would engaging it spend the reserve?",
     "OPEN - and it is now the decisive question for this arm",
     "Forskolin-stimulated cAMP in primary growth plate chondrocytes under cANF(4-23) "
     "across a dose range, pertussis toxin as the Gi control, osteocrin as the silent "
     "comparator. Then a bone length under cANF(4-23), which has decades of in vivo rodent "
     "use and has never been given to a growing animal.",
     "NEW BENCH WORK, one plate. The in vivo half needs animals but the compound is old."),

    ("g_l12_what_happens_to_the_aortic_root_under_chronic_osteocrin", 211,
     "Does an occupier dilate the aorta the way a null does?",
     "OPEN - the only surviving vascular objection",
     "Serial aortic root imaging under a dosed occupier. Three cardioprotection groups "
     "already have banked tissue from osteocrin animals and measured the myocardium "
     "instead of the vessel - THE CHEAP VERSION IS TO ASK THEM.",
     "PARTLY RETROSPECTIVE - the tissue may exist at Hannover, Iowa and Boston."),

    ("g_l12_does_hnpr3_delta_c_separate_the_height_from_the_aorta", 211,
     "Does a Gi-dead but clearance-competent NPR3 mouse separate the two phenotypes?",
     "OPEN - one animal answers both halves",
     "Knock devotta2023's HNPR3-deltaC deletion into the mouse Npr3 locus; phenotype "
     "against wild-type and null littermates on segment-resolved lengths and serial aortic "
     "root imaging. Three genotypes, two readouts, and the compound spec falls out.",
     "NEW ANIMAL WORK, but the construct and both phenotyping protocols are published."),

    ("g_l12_is_osteocrin_silent_at_all_concentrations_or_a_partial_agonist", 211,
     "Is osteocrin silent across its whole dose range, or only at 100 nM?",
     "OPEN - and CORR-204 rests on the single point",
     "A full concentration-response, 1 nM to 10 uM, on the same assay. Same plate as the "
     "chondrocyte coupling question.",
     "NEW BENCH WORK, trivial."),

    ("g_l1_raise_terminal_cell_volume", "pre-199",
     "Can terminal cell height be raised in a healthy plate?",
     "PREMISE OVERTURNED round 202, quantified round 208",
     "Answered in part - two agents elevate a NORMAL baseline by about 20 per cent "
     "(weber2025 NPR3 loss, trompet2024 hedgehog). Round 205 showed the hedgehog "
     "elevation does not survive to two months. What is still missing is a DOSE-RESPONSE "
     "and any agent sustaining it.",
     "NEW ANIMAL WORK."),
]


def rule(c="="):
    print(c * 92)


def main():
    rule()
    print("OPEN-QUESTION LEDGER - everything this programme opened, rounds 199 to 211")
    rule()
    print(f"\n    {len(LEDGER)} questions tracked\n")

    for gid, rnd, q, status, close, who in LEDGER:
        print("-" * 92)
        print(f"  {q}")
        print(f"    id       {gid}")
        print(f"    opened   round {rnd}")
        print(f"    status   {status}")
        print(f"    closes   {close}")
        print(f"    access   {who}")

    print("\n" + "=" * 92)
    print("WHAT CAN BE ANSWERED WITHOUT NEW ANIMALS OR NEW PATIENTS")
    rule("-")
    cheap = [l for l in LEDGER if "EXIST" in l[5].upper() or "RETROSPECTIVE" in l[5].upper()
             or "trivial" in l[5]]
    for gid, rnd, q, status, close, who in cheap:
        print(f"    - {q}")
        print(f"        {who}")
    print(f"\n    {len(cheap)} of {len(LEDGER)} need no new animal and no new patient.")

    print("\n" + "=" * 92)
    print("THE TWO THAT WOULD CHANGE THE STACK TODAY IF ANSWERED")
    rule("-")
    print("    1. PER-SITE REMAINING GROWTH AT BONE AGE 16. Without it no agent can be")
    print("       converted into predicted centimetres, and every site-specific animal")
    print("       result is being weighted by guesswork. The images exist in paediatric")
    print("       orthopaedic cohorts; the studies simply reported the spine.")
    print("    2. THE CNP AXIAL MECHANISM. Round 208 sharpened it into a contrast - FGFR3")
    print("       inhibition grows lumbar vertebrae and improves the foramen magnum, the")
    print("       CNP axis does neither in primates. If that holds, the two arms are")
    print("       COMPLEMENTARY BY SITE rather than redundant, which is the single most")
    print("       consequential thing the stack could learn.")
    rule()


if __name__ == "__main__":
    main()
