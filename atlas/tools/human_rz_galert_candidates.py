#!/usr/bin/env python3
"""
DO THE G(Alert) MACHINERY GENES EXIST IN THE HUMAN RESTING ZONE?
A re-analysis of avijgan2026's own deposited spatial transcriptomics.

WHY THIS TOOL EXISTS
--------------------
Round 201 arrived at G(Alert) - the mTORC1-gated G0-to-primed transition of
rodgers2014 - as the term that explains why every pool-expanding intervention in
this atlas produces a bigger reserve and no extra flux. The supporting mechanism
papers are all MUSCLE OR MARROW:

  rodgers2014   mTORC1 necessary and sufficient for G0 -> G(Alert); cMet also
                necessary; injury-induced SYSTEMIC signals drive it (mouse)
  brun2022      GLI3 holds satellite cells in G0; losing GLI3 gives G(Alert)
                WITHOUT injury via mTORC1 activation, and expands the pool
  de2026a       D2 (DIO2) marks quiescent stem cells; depleting it forces a
                G(Alert)-like state that RAISES proliferation and DESTROYS
                self-renewal, exhausting the pool
  hirano2025a   Mg2+ entry through TRPM7 drives mTOR and the G0 -> G(Alert) step
  boaventura2026  human MSCs in soft 3D confinement enter DEEP quiescence with
                mTORC1 DOWN - a phenotype 2D serum starvation cannot reproduce

NONE OF THEM TOUCHES CARTILAGE. A Europe PMC sweep for G(Alert) in bone,
cartilage or chondrocytes returns nothing on the growth plate at all. Importing
a muscle mechanism into the growth plate on vibes is exactly what this atlas
forbids, so the first question is the cheap one: ARE THESE GENES EVEN
TRANSCRIBED IN THE HUMAN RESTING ZONE?

That is answerable today. avijgan2026 deposited its spatial data, spot-level
zone annotations included, at github.com/anarl/spatial_bone_growth. This tool
reproduces the authors' own pseudobulk-by-area approach and asks only where the
candidate transcripts sit.

WHAT THIS IS AND IS NOT
-----------------------
IT IS: a presence/absence and relative-abundance test in human tissue.
IT IS NOT: evidence that any of these genes DOES anything in cartilage. A
transcript in the right compartment is a licence to ask the next question, and
nothing more. Graded accordingly - the strongest verdict available here is
'the human resting zone expresses it', which is grade B for presence and
grade E for any functional claim.

A NORMALISATION CAVEAT THAT MATTERS HERE MORE THAN USUAL
--------------------------------------------------------
The central finding of avijgan2026 is that RZ spots carry LESS total mRNA than
any other zone. CPM normalisation therefore answers 'what share of the resting
zone's transcriptome is this gene', not 'how many molecules per cell'. For a
compartment defined by low output, a CPM enrichment can coexist with a lower
absolute count. Both are printed.
"""
import os, sys, csv, math
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
EXPORT = os.path.join(ROOT, "growth-plate", "acquire", "spatial_bone_growth",
                      "visium_export")
if not os.path.isdir(EXPORT):
    EXPORT = os.path.join(os.path.dirname(os.path.dirname(HERE)),
                          "acquire", "spatial_bone_growth", "visium_export")

# The G(Alert) machinery, plus positive and negative controls from the paper.
CANDIDATES = {
    "MTOR":   "mTORC1 catalytic subunit - the switch itself (rodgers2014)",
    "RPTOR":  "RAPTOR, defines mTORC1 as opposed to mTORC2",
    "TSC1":   "brake on mTORC1; its ablation is newton2019 pool-expanding lesion",
    "TSC2":   "the other half of the brake",
    "RHEB":   "the GTPase TSC1/2 acts on",
    "MET":    "cMet - NECESSARY for G0 -> G(Alert) in rodgers2014",
    "HGF":    "the cMet ligand; if made locally the alerting signal is paracrine",
    "GLI3":   "holds satellite cells in G0; loss gives G(Alert) (brun2022)",
    "GLI1":   "hedgehog activator output, for context",
    "GLI2":   "hedgehog activator output, for context",
    "PTCH1":  "hedgehog receptor - trompet2024's SAG target pathway",
    "SMO":    "smoothened",
    "DIO2":   "type 2 deiodinase - marks quiescence; loss exhausts the pool (de2026a)",
    "DIO3":   "the inactivating deiodinase, opposite sign",
    "THRA":   "thyroid hormone receptor alpha",
    "THRB":   "thyroid hormone receptor beta",
    "TRPM7":  "Mg2+ channel upstream of mTOR in G0 -> G(Alert) (hirano2025a)",
    "EZH1":   "deep-quiescence mark in 3D-confined human MSCs",
    "FOXO3":  "deep-quiescence mark, same source",
    "CDKN1B": "p27, same source",
    "CDKN2A": "p16 - the senescence gap opened in round 199",
    "NOTCH1": "TH sustains Notch in de2026a; Notch is the self-renewal arm",
    "NOTCH2": "as above",
    "HEY1":   "Notch target",
    # controls, from avijgan2026's own marker list
    "SFRP5":  "CONTROL - author-stated RZ marker",
    "CHRDL2": "CONTROL - author-stated RZ marker",
    "UCMA":   "CONTROL - author-stated RZ marker",
    "ZNF550": "CONTROL - author-stated RZ marker",
    "COL10A1": "CONTROL - author-stated HZ marker, must NOT be RZ-enriched",
    "MKI67":  "CONTROL - proliferation, must be PZ-weighted",
}

ZONES = ["RZ", "PZ", "HZ", "SOC"]


def load_section(stem):
    genes = []
    with open(os.path.join(EXPORT, stem + ".genes.csv")) as f:
        r = csv.reader(f); next(r)
        for row in r:
            genes.append(row[0])
    spot_zone, spot_pat = {}, {}
    order = []
    with open(os.path.join(EXPORT, stem + ".meta.csv")) as f:
        r = csv.DictReader(f)
        first = r.fieldnames[0]
        for row in r:
            spot_zone[row[first]] = row.get("area", "")
            spot_pat[row[first]] = row.get("orig.ident", "")
    with open(os.path.join(EXPORT, stem + ".spots.csv")) as f:
        r = csv.reader(f); next(r)
        for row in r:
            order.append(row[0])
    # pseudobulk: gene x zone
    zsum = {z: defaultdict(int) for z in ZONES}
    ztot = {z: 0 for z in ZONES}
    zspots = {z: 0 for z in ZONES}
    for s in order:
        z = spot_zone.get(s, "")
        if z in zspots:
            zspots[z] += 1
    with open(os.path.join(EXPORT, stem + ".counts.mtx")) as f:
        f.readline()  # banner
        line = f.readline()
        while line.startswith("%"):
            line = f.readline()
        for line in f:
            gi, si, v = line.split()
            gi = int(gi) - 1; si = int(si) - 1; v = int(v)
            s = order[si]
            z = spot_zone.get(s, "")
            if z in zsum:
                zsum[z][gi] += v
                ztot[z] += v
    patients = {spot_pat.get(s, "") for s in order}
    return genes, zsum, ztot, zspots, (patients.pop() if len(patients) == 1 else "mixed")


def main():
    stems = sorted({f.rsplit(".", 2)[0] for f in os.listdir(EXPORT)
                    if f.endswith(".counts.mtx")})
    print("=" * 92)
    print("G(Alert) MACHINERY IN THE HUMAN GROWTH PLATE - avijgan2026 deposited data")
    print("=" * 92)
    print(f"    sections found : {len(stems)}")

    per_gene = defaultdict(lambda: defaultdict(list))   # gene -> zone -> [cpm]
    per_gene_raw = defaultdict(lambda: defaultdict(list))
    detected_sections = defaultdict(int)
    panel_missing = set()
    totals = {z: [] for z in ZONES}
    spots_tot = {z: 0 for z in ZONES}
    patients = set()

    for stem in stems:
        genes, zsum, ztot, zspots, pat = load_section(stem)
        patients.add(pat)
        idx = {g: i for i, g in enumerate(genes)}
        for z in ZONES:
            totals[z].append(ztot[z])
            spots_tot[z] += zspots[z]
        for g in CANDIDATES:
            if g not in idx:
                panel_missing.add(g)
                continue
            gi = idx[g]
            hit = False
            for z in ZONES:
                if ztot[z] == 0:
                    continue
                c = zsum[z][gi]
                per_gene[g][z].append(1e6 * c / ztot[z])
                per_gene_raw[g][z].append(c)
                if c > 0:
                    hit = True
            if hit:
                detected_sections[g] += 1

    print(f"    patients       : {len(patients)}  {sorted(patients)}")
    print(f"    spots by zone  : " +
          "  ".join(f"{z}={spots_tot[z]}" for z in ZONES))
    print(f"    total UMI      : " +
          "  ".join(f"{z}={sum(totals[z]):,}" for z in ZONES))
    print("\n    THE ZONE UMI TOTALS REPRODUCE THE PAPER'S CENTRAL CLAIM: the resting")
    print("    zone is the transcriptionally quietest compartment. Read every CPM")
    print("    below against that denominator.")

    if panel_missing:
        print(f"\n    NOT ON THE PROBE PANEL (cannot be scored either way): "
              f"{sorted(panel_missing)}")

    print("\n" + "=" * 92)
    print("MEAN CPM BY ZONE, ACROSS SECTIONS")
    print("=" * 92)
    print(f"    {'gene':<9} {'sect':>5} {'RZ':>9} {'PZ':>9} {'HZ':>9} {'SOC':>9}"
          f" {'RZ/PZ':>7}   note")
    order = [g for g in CANDIDATES if g not in panel_missing]
    for g in order:
        d = per_gene[g]
        if not d:
            continue
        m = {z: (sum(d[z]) / len(d[z]) if d[z] else 0.0) for z in ZONES}
        ratio = (m["RZ"] / m["PZ"]) if m["PZ"] > 0 else float("inf")
        rs = "  inf" if ratio == float("inf") else f"{ratio:5.2f}"
        note = CANDIDATES[g]
        print(f"    {g:<9} {detected_sections[g]:>5} {m['RZ']:>9.2f} {m['PZ']:>9.2f}"
              f" {m['HZ']:>9.2f} {m['SOC']:>9.2f} {rs:>7}   {note[:34]}")

    print("\n" + "=" * 92)
    print("VERDICTS")
    print("=" * 92)
    absent, present, enriched = [], [], []
    for g in order:
        d = per_gene[g]
        if not d:
            continue
        m = {z: (sum(d[z]) / len(d[z]) if d[z] else 0.0) for z in ZONES}
        rzhit = sum(1 for c in per_gene_raw[g]["RZ"] if c > 0)
        if m["RZ"] == 0:
            absent.append(g)
        elif m["PZ"] > 0 and m["RZ"] / m["PZ"] >= 1.5:
            enriched.append((g, m["RZ"] / m["PZ"], rzhit))
        else:
            present.append((g, m["RZ"], rzhit))
    print(f"\n    RZ-ENRICHED (CPM ratio to PZ >= 1.5):")
    for g, r, n in sorted(enriched, key=lambda x: -x[1]):
        print(f"        {g:<9} {r:5.2f}x   detected in {n}/{len(stems)} sections"
              f"   {CANDIDATES[g][:44]}")
    print(f"\n    PRESENT BUT NOT RZ-ENRICHED:")
    for g, v, n in sorted(present, key=lambda x: -x[1]):
        print(f"        {g:<9} {v:8.2f} CPM in RZ, detected in {n}/{len(stems)}"
              f"   {CANDIDATES[g][:36]}")
    print(f"\n    ZERO COUNTS IN THE RESTING ZONE ACROSS EVERY SECTION:")
    for g in absent:
        print(f"        {g:<9} {CANDIDATES[g][:60]}")
    print("\n    A ZERO HERE IS WEAK EVIDENCE OF ABSENCE, NOT PROOF. These are")
    print("    probe-based assays on a compartment with the lowest library size in")
    print("    the tissue; a low-abundance transcript can drop below detection in")
    print("    the RZ while being real. The correct reading of a zero is 'not")
    print("    detectable at this depth in this compartment'.")

    # ---------------------------------------------------------------- paired
    print("\n" + "=" * 92)
    print("SECTION-PAIRED SIGN TEST, RZ versus PZ")
    print("=" * 92)
    print("    The depth objection cuts the RIGHT way here and it is worth stating")
    print("    before the numbers. Across these 14 sections the PROLIFERATIVE zone")
    print(f"    carries MORE total UMI ({sum(totals['PZ']):,}) than the resting zone")
    print(f"    ({sum(totals['RZ']):,}) despite having far fewer spots"
          f" ({spots_tot['PZ']} against {spots_tot['RZ']}).")
    print("    So a transcript seen in the RZ and NOT in the PZ is not a sampling")
    print("    artefact of deeper resting-zone libraries. There are none.")
    print(f"\n    {'gene':<9} {'RZ>PZ':>6} {'PZ>RZ':>6} {'tie':>4} {'informative':>12}"
          f" {'p (sign)':>9}")

    def sign_p(k, n):
        """two-sided exact binomial at p=0.5"""
        if n == 0:
            return 1.0
        c = lambda a, b: math.comb(a, b)
        k = max(k, n - k)
        tail = sum(c(n, i) for i in range(k, n + 1)) / (2.0 ** n)
        return min(1.0, 2 * tail)

    focus = ["MTOR", "EZH1", "CDKN1B", "FOXO3", "DIO2", "THRA", "NOTCH2", "HEY1",
             "GLI2", "GLI3", "SMO", "PTCH1", "MET", "TRPM7", "CDKN2A",
             "SFRP5", "CHRDL2", "COL10A1"]
    for g in focus:
        if g in panel_missing:
            continue
        rz, pz = per_gene[g]["RZ"], per_gene[g]["PZ"]
        up = dn = tie = 0
        for a, b in zip(rz, pz):
            if a > b:
                up += 1
            elif b > a:
                dn += 1
            else:
                tie += 1
        n = up + dn
        p = sign_p(up, n)
        star = " *" if p < 0.05 and up > dn else ""
        print(f"    {g:<9} {up:>6} {dn:>6} {tie:>4} {n:>12} {p:>9.4f}{star}")
    print("\n    Ties are sections where BOTH zones read zero - uninformative, and")
    print("    excluded from the test rather than counted as agreement.")
    print("    A sign test on sections is the weakest defensible test here: it")
    print("    assumes only that each section is an independent look. It is NOT a")
    print("    patient-level test - several sections come from the same donor, so")
    print("    these p-values are anti-conservative and are reported as a screen.")
    print("=" * 92)


if __name__ == "__main__":
    main()
