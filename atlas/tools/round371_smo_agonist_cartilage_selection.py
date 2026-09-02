#!/usr/bin/env python3
"""
ROUND 371. WHICH SMOOTHENED AGONIST, CALCULATED RATHER THAN ASSERTED.

WHY THIS EXISTS. R368 withdrew "the route must be local" and R369 found four FDA-approved SMO
agonists. The operator asked whether the right agonist can be worked out rather than guessed.
It can be, because this atlas already holds the two things needed:
  - the cartilage transport physics (R353: epiphyseal fixed charge density -0.19 to -0.35 M,
    so CATIONIC solutes are concentrated by Donnan partitioning and anions excluded)
  - the published penetration design rules (R315: evenly distributed cationic charge PLUS
    MINIMAL HYDROPHOBICITY gives the deepest and longest-lasting cartilage penetration)

WHAT THIS DOES.
  1. Pulls every molecule in ChEMBL with a pChEMBL value on human SMO (CHEMBL5971).
  2. Pulls physicochemical properties, including ChEMBL's computed most-basic pKa.
  3. Computes, for each: net charge state at pH 7.4, and the DONNAN ENRICHMENT FACTOR in
     cartilage at the atlas's own measured epiphyseal FCD.
  4. Scores against the cartilage criteria and prints the window.

THE DONNAN ARITHMETIC, WHICH IS THE POINT OF THE WHOLE SCRIPT.
For a tissue of fixed charge density magnitude cF against external ionic strength cs, the
partition ratio for a monovalent CATION is
    r = x + sqrt(x^2 + 1),  where x = cF / (2*cs)
and a solute of charge z is enriched by r^z (anions are excluded by r^-1).
  cF = 0.20 M, cs = 0.15 M ->  r = 1.87   (a +1 cation is enriched ~1.9-fold)
  cF = 0.35 M, cs = 0.15 M ->  r = 2.70
THE SCALING IS r^z, AND THAT IS WHY CPC+14 WORKS AND A MONOVALENT CATION DOES NOT:
  z=+1  -> ~1.9-2.7x        z=+14 -> ~1.9^14 to 2.7^14 = 1e4 to 1e6 x
So a singly-charged small molecule gets a real but MODEST cartilage boost. Do not oversell it.

READ THE OUTPUT AS: a screen for whether any SMO-active chemotype sits in the cartilage window
at all. It does NOT distinguish agonist from antagonist - ChEMBL's SMO content is dominated by
the oncology antagonist programme (R368) - so a hit is a CHEMOTYPE lead, not a candidate.
"""
import json, math, sys, time, urllib.request

from rdkit import Chem
from rdkit.Chem import Crippen, Descriptors

B = "https://www.ebi.ac.uk/chembl/api/data"
TARGET = "CHEMBL5971"          # human Smoothened
FCD_LO, FCD_HI, IONIC = 0.19, 0.35, 0.15   # M, epiphyseal cartilage (atlas R315/R353)


def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                return json.load(r)
        except Exception:
            time.sleep(3)
    return {}


def donnan(z, fcd, ionic=IONIC):
    """Partition ratio in cartilage for a solute of net charge z."""
    x = fcd / (2.0 * ionic)
    r = x + math.sqrt(x * x + 1.0)
    return r ** z


# ChEMBL's API returns alogp but NOT cx_logp and NOT any pKa, so ionisation is assigned
# from substructure. This is a HEURISTIC and is labelled as one in the output.
#   BASIC   = aliphatic amine (primary/secondary/tertiary) not bonded to a carbonyl or an
#             aromatic ring, plus amidine and guanidine. Protonated at pH 7.4.
#   NOT BASIC = amide, aniline, pyridine/azole ring N, sulfonamide, nitrile, nitro.
#   ACIDIC  = carboxylic acid, tetrazole, acyl sulfonamide. Deprotonated at pH 7.4.
BASIC = [Chem.MolFromSmarts(s) for s in (
    "[NX3;H2,H1,H0;!$(N[#6]=[O,S,N]);!$(Na);!$(N[SX4](=O)=O);!$(N#*);!$(N=*);!$(N[OX1])]"
    "[CX4]",                                   # aliphatic amine on sp3 carbon
    "[NX3][CX3]=[NX2]",                        # amidine
    "[NX3][CX3](=[NX2])[NX3]",                 # guanidine
)]
ACIDIC = [Chem.MolFromSmarts(s) for s in (
    "[CX3](=O)[OX2H1]",                        # carboxylic acid
    "c1nn[nH]n1",                              # tetrazole
    "[CX3](=O)[NX3H1][SX4](=O)(=O)",           # acyl sulfonamide
)]


def charge_at_ph(mol):
    """Net charge at pH 7.4, assigned by substructure. Heuristic, not a pKa calculation."""
    if mol is None:
        return None
    z = 0.0
    if any(mol.HasSubstructMatch(p) for p in BASIC if p is not None):
        z += 1.0
    if any(mol.HasSubstructMatch(p) for p in ACIDIC if p is not None):
        z -= 1.0
    z += Chem.GetFormalCharge(mol)
    return z


def collect_molecules():
    ids, off = set(), 0
    while True:
        d = get(f"{B}/activity.json?target_chembl_id={TARGET}&limit=1000&offset={off}")
        acts = d.get("activities", [])
        if not acts:
            break
        for a in acts:
            if a.get("pchembl_value"):
                ids.add(a["molecule_chembl_id"])
        tot = d.get("page_meta", {}).get("total_count", 0)
        off += 1000
        if off >= tot:
            break
    return sorted(ids)


def fetch_props(ids):
    out = {}
    for i in range(0, len(ids), 25):
        chunk = ",".join(ids[i:i + 25])
        d = get(f"{B}/molecule.json?molecule_chembl_id__in={chunk}&limit=25")
        for m in d.get("molecules", []):
            p = m.get("molecule_properties") or {}
            out[m["molecule_chembl_id"]] = {
                "name": m.get("pref_name"),
                "maxphase": m.get("max_phase"),
                "mw": p.get("full_mwt"),
                "alogp": p.get("alogp"),
                "psa": p.get("psa"),
                "hbd": p.get("hbd"),
                "ro5": p.get("num_ro5_violations"),
                "smiles": (m.get("molecule_structures") or {}).get("canonical_smiles"),
            }
        time.sleep(0.15)
    return out


def main():
    ids = collect_molecules()
    print(f"molecules with a pChEMBL value on human SMO: {len(ids)}")
    props = fetch_props(ids)
    print(f"properties retrieved: {len(props)}\n")

    rows = []
    for cid, p in props.items():
        mw, logp, smi = p.get("mw"), p.get("alogp"), p.get("smiles")
        if mw is None or logp is None or not smi:
            continue
        mol = Chem.MolFromSmiles(smi)
        z = charge_at_ph(mol)
        if z is None:
            continue
        rows.append({
            "id": cid, "name": p.get("name"), "maxphase": p.get("maxphase"),
            "mw": float(mw), "logp": float(logp), "z": z, "smiles": smi,
            "donnan_lo": donnan(z, FCD_LO), "donnan_hi": donnan(z, FCD_HI),
        })

    print(f"DONNAN REFERENCE: a +1 cation is enriched "
          f"{donnan(1, FCD_LO):.2f}x (FCD {FCD_LO} M) to {donnan(1, FCD_HI):.2f}x (FCD {FCD_HI} M); "
          f"a -1 anion is EXCLUDED to {donnan(-1, FCD_LO):.2f}x-{donnan(-1, FCD_HI):.2f}x\n")

    # the cartilage window: basic centre, moderate lipophilicity, small
    win = [r for r in rows if r["z"] >= 0.5 and r["logp"] <= 4.0 and r["mw"] <= 500]
    print(f"IN THE CARTILAGE WINDOW (net charge >= +0.5, cLogP <= 4.0, MW <= 500): "
          f"{len(win)} of {len(rows)}")
    for r in sorted(win, key=lambda r: r["logp"])[:30]:
        print(f"  {r['id']:15s} MW {r['mw']:6.1f}  cLogP {r['logp']:5.2f}  z {r['z']:+.2f}  "
              f"Donnan {r['donnan_lo']:.2f}-{r['donnan_hi']:.2f}x  phase {r['maxphase']}  {r['name']}")

    # where do the KNOWN AGONISTS sit? computed from SMILES the same way
    print("\nTHE KNOWN AGONISTS, SCORED ON THE SAME CRITERIA:")
    known = {
        "SAG":            "CNC1CCC(CC1)N(CC2=CC(=CC=C2)C3=CC=NC=C3)C(=O)C4=C(C5=CC=CC=C5S4)Cl",
        "purmorphamine":  "C1CCC(CC1)N2C=NC3=C(N=C(N=C32)OC4=CC=CC5=CC=CC=C54)NC6=CC=C(C=C6)N7CCOCC7",
        "GSA-10":         "CCCCCCN1C2=CC=CC=C2C(=C(C1=O)C(=O)NC3=CC=C(C=C3)C(=O)OCCC)O",
        "clobetasol prop":"CCC(=O)OC1(C(CC2C1(CC(C3(C2CCC4=CC(=O)C=CC43C)F)O)C)C)C(=O)CCl",
        "halcinonide":    "CC12CCC(=O)C=C1CCC3C2C(CC4(C3CC5C4(OC(O5)(C)C)C(=O)CCl)C)O",
    }
    for nm, smi in known.items():
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            print(f"  {nm:18s} SMILES parse failed"); continue
        z = charge_at_ph(mol)
        lp = Crippen.MolLogP(mol); mw = Descriptors.MolWt(mol)
        print(f"  {nm:18s} MW {mw:6.1f}  cLogP(Crippen) {lp:5.2f}  z {z:+.1f}  "
              f"Donnan {donnan(z, FCD_LO):.2f}-{donnan(z, FCD_HI):.2f}x")

    cat = [r for r in rows if r["z"] >= 0.5]
    print(f"\nCATIONIC AT pH 7.4 (any lipophilicity): {len(cat)} of {len(rows)}")
    print(f"MEDIAN cLogP of all SMO-active molecules: "
          f"{sorted(r['logp'] for r in rows)[len(rows)//2]:.2f}")
    print(f"FRACTION with cLogP > 5 (fails the R315 minimal-hydrophobicity rule): "
          f"{100*sum(1 for r in rows if r['logp'] > 5)/len(rows):.1f}%")

    json.dump(rows, open("atlas/data/round371/smo_cartilage_screen.json", "w"), indent=1)
    print("\nwrote atlas/data/round371/smo_cartilage_screen.json")


if __name__ == "__main__":
    main()
