#!/usr/bin/env python3
"""
R401 - THE VENDOR-LEVEL SWEEP. "NO MOLECULE EXISTS" HAS MEANT "NO MEDICINE IS SOLD."

CORR-347 established that Open Targets "known drugs" lists only CLINICAL and APPROVED
agents, so every tool compound is invisible to it, and that ChEMBL must be queried for
chemical matter instead. R401 applies the same correction ONE LEVEL FURTHER OUT:
ChEMBL indexes SMALL MOLECULES with bioactivity records. It does not index the
catalogue of RECOMBINANT PROTEINS AND FC-FUSIONS that biology suppliers sell.

For a file whose two best target classes are SECRETED PROTEINS (R287's layer) and
whose repeated conclusion is "the direction is to SUPPLY this protein" or "the wanted
form is the CLUSTERED ligand", that omission is exactly where the answers would hide.

Every row below was checked against live vendor catalogue listings on 2026-08-14.
These are RESEARCH-GRADE REAGENTS. None is a medicine, none has an impurity or tox
package, and none has been given to a human. What they change is that several
experiments this file has repeatedly called "does not exist" are purchase orders.
"""

SWEEP = [
    # symbol, what the atlas SAID, what is actually on sale, why it matters
    ("JAG1-Fc",
     "R400 named a multivalent Notch agonist as the wanted form and treated it as a construct to be built",
     "SOLD - Recombinant Human Jagged-1 Fc Chimera (R&D 1277-JG and N-terminal 10111-JG), "
     "Mouse (10969-JG), plus an Abcam 'Active' listing. Vendor bioactivity is measured "
     "IMMOBILISED, ED50 0.3-1.8 ug/mL",
     "⭐ THIS IS THE EXACT REAGENT lin2011 USED (Jagged1/Fc) TO EXPAND THE EPIPHYSIS STEM "
     "CELL ZONE. Fc-dimeric = the CLUSTERED form CORR-355 says is the agonist. Human and "
     "mouse, catalogue, today."),

    ("DLL1-Fc",
     "never asked",
     "SOLD - Human (R&D 10184-DL), Mouse (5026-DL), Rat (3970-DL). ED50 0.1-0.5 ug/mL",
     "⭐ DLL1 is THE PLATE'S OWN Notch ligand - 3.05x cartilage-enriched, 24.9 CPM in the "
     "purity-corrected human growth plate (R399/R400). The physiological ligand, in the "
     "agonist format, in three species including the two used for growth-plate work."),

    ("SCUBE3",
     "R287 listed 'recombinant SCUBE3 -> measure a bone' as one of FOUR cheap experiments "
     "that DO NOT EXIST; R312 recorded 'no recombinant product'",
     "SOLD - Recombinant Human SCUBE3, CF (R&D 7730-SC), CHO-derived Ala21-Lys993, >95% "
     "pure, endotoxin <0.10 EU/ug",
     "⭐⭐ AND THE VENDOR VALIDATES IT ON CHONDROGENIC CELLS - bioactivity is adhesion of "
     "ATDC5 mouse chondrogenic cells, ED50 0.25-1.25 ug/mL. SCUBE3 pLoF is -7.18 cm, loss "
     "SHORTENS, so the direction is to SUPPLY - and it is the one target in the layer "
     "where supplying is the move. The atlas said this product did not exist."),

    ("SMOC-1",
     "R356 already recorded it as a catalogue reagent",
     "SOLD - recombinant human and mouse, >95% purity",
     "already known; listed for completeness. SMOC1 pLoF -1.63 cm, monotone with variant "
     "severity, and biallelic loss is short - the direction is to supply."),

    ("SAG",
     "R372 established it is purchasable at >=98% HPLC with CoA, incl. the dihydrochloride",
     "SOLD - Tocris 4366 (free base) and 6390 (dihydrochloride), Sigma, Abcam, Santa Cruz "
     "and others",
     "already known. The blocker was never availability - it is that no pharmaceutical-"
     "grade material and no human exposure exist."),

    # --- and the ones that are genuinely NOT sold, confirmed by the same sweep ---
    ("anti-HHIP, function-blocking",
     "R314/R376: no function-blocking anti-HHIP exists in any species",
     "NOT SOLD - CONFIRMED. Vendors list HHIP antibodies for WB, IHC, ELISA, IP and flow "
     "(incl. clone 5D11) but none is offered as neutralising or function-blocking",
     "the gap is real and unchanged. HHIP remains the best-validated target in the file "
     "with no usable agent."),

    ("anti-STC2, neutralising",
     "R341/R342: no anti-STC2 therapeutic antibody exists in any species",
     "NOT SOLD - detection antibodies only",
     "STC2 +1.37 cm at P=4.5e-34 across 3,927 carriers, secreted, direction is to BLOCK, "
     "and the PAPP-A interface is solved at 3.1 A. Still no binder."),

    ("anti-CHAD / CHAD-alpha2beta1 blocker",
     "R313/CORR-335: the published peptides MIMIC CHAD; the antagonist does not exist",
     "NOT SOLD",
     "direction is to BLOCK (+2.63 cm on loss); the motif is known to 8 residues."),

    ("NRK inhibitor",
     "R313/R324: no human NRK ChEMBL target record, Pharos Tdark, 0 ligands",
     "NOT SOLD",
     "and R324 showed the phenotype is KINASE-INDEPENDENT, so an ATP-competitive "
     "inhibitor would be the wrong modality anyway."),
]

print("=" * 100)
print("R401  VENDOR-LEVEL AVAILABILITY SWEEP  (catalogue listings checked 2026-08-14)")
print("=" * 100)
sold = [r for r in SWEEP if r[2].startswith("SOLD")]
not_sold = [r for r in SWEEP if r[2].startswith("NOT")]
for label, group in (("ON SALE", sold), ("CONFIRMED NOT ON SALE", not_sold)):
    print("\n" + "#" * 100)
    print("##", label)
    print("#" * 100)
    for sym, said, avail, why in group:
        print(f"\n  {sym}")
        print(f"    atlas said : {said}")
        print(f"    actually   : {avail}")
        print(f"    why it matters: {why}")

print("""

""" + "=" * 100 + """
WHAT THIS DOES AND DOES NOT MEAN
""" + "=" * 100 + """
⛔ EVERY ITEM ON THE 'ON SALE' LIST IS A RESEARCH-GRADE REAGENT. None is a medicine.
   None carries an impurity, endotoxin-release or toxicology package adequate for
   administration to a person, and none has ever been given to a human. Nothing here
   changes the standing position that this file's leads are not obtainable as
   treatments.

⭐ WHAT IT DOES CHANGE IS THE COST OF THE DECIDING EXPERIMENTS. Three questions that
   have blocked this axis for many rounds are now purchase orders rather than
   programmes:
     1. Does a CLUSTERED Notch agonist expand the resting zone in a NORMAL GROWING
        animal, and does the bone get longer? JAG1-Fc and DLL1-Fc, human and mouse,
        catalogue.
     2. Is the soluble monomeric JAG1 peptide an agonist or an antagonist IN
        CHONDROCYTES? Both forms are purchasable; the readout is HES1; CORR-355
        predicts the peptide INHIBITS and the Fc-fusion ACTIVATES. One week in a dish.
     3. Does supplying SCUBE3 lengthen a bone? The protein is sold and the vendor
        already validates it on chondrogenic cells.

⭐ THE GENERALISABLE CORRECTION: this file has written 'no molecule exists' about
   secreted proteins whose recombinant forms are catalogue items. The phrase must be
   split three ways, as CORR-347 split it two ways:
     · no APPROVED MEDICINE          (true of almost everything here)
     · no CHEMICAL MATTER            (query ChEMBL - CORR-347)
     · no PURCHASABLE PROTEIN        (query the vendor catalogues - THIS ROUND)
   The third was never run, and it is exactly where a secreted-protein atlas would
   hide its answers.
""")
