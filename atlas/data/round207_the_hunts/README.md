# Round 207 — both hunts run to ground

## Hunt 1: the NHP L1–L4 data — RESOLVED via the EMA EPAR

`BMN-111-11-035` is a sponsor internal report and is not obtainable. **The EMA CHMP assessment report
(EMA/397108/2021, 191 pp) reproduces what was needed and adds what the FDA review omitted** — fetched
directly, saved as `voxzogo_epar.pdf` / `.txt`.

**The design I asked for:** cynomolgus monkey, juvenile, 2–3 y, **7 M + 7 F in control and high dose**,
4+4 in low and mid, 26 wk + 28 d recovery, 0/20/90/300 µg/kg. So the L1–L4 null is a **seven-per-sex**
comparison — better than round 205 assumed. Confirmed verbatim: *"There were no vosoritide-related
changes in the L1 to L4 vertebral length, foramen magnum dimensions, or skull measurements."*

**And the cross-species pattern, which is what the gap actually needed** — TD mice, 10 days:

| segment | 240 µg/kg | 800 µg/kg |
|---|---|---|
| femur | +3.41 %* | +5.23 %* |
| tibia | +3.69 % | +6.64 %* |
| AP skull | +2.88 % | +4.77 %* |
| naso-anal | +4.51 %* | +5.29 %* |
| **L4–L6** | **+2.84 %** | **+3.26 %** |

**L4–L6 is the only segment failing significance at both doses.** In juvenile rats the axial skeleton
*does* respond (crown-rump, tail, lumbar spine length all up) — but at the dose that produces it:
**scoliosis, kyphosis, fractures, femur BMD −19 %**. Converges with the round-203 human census where
3 of 6 constitutive CNP-axis reports carried scoliosis.

**Two bonuses, both favourable:**
- **The sex split is an exposure artefact** — *"likely due to higher vosoritide exposures in males"*. Resolves the round-205 CORR-191 flag benignly.
- **An age gate running the right way** — growth increases, BMD reduction and overgrowth signs *"largely not appearing until rats reached adolescence to adulthood (approximately 8–15 weeks)"*. Second independent line after `cnpmeta2026`'s larger gain above age 5.

## Hunt 2: resveratrol PK in cartilage — NOT FOUND, and the hypothesis got worse

No study measures resveratrol or its conjugates in cartilage, in any species. But the primary paper
behind the mechanism, **`kunihiro2019`**, names the enzyme source: GUSB is *"a deconjugating enzyme
expressed by **hematopoietic marrow cells**"*, the hydrolysis was localised to **marrow**, abolished by
saccharolactone and reduced/absent in two GUSB-deficient strains.

**The growth plate is avascular and marrow-free**, and the resting zone sits at maximum diffusion
distance from the nearest marrow. **My round-206 resting-zone hypothesis moves from plausible to
unlikely.** Not dead — the chondro-osseous junction abuts marrow and could supply the hypertrophic zone
retrograde — but reach to the *reserve* is now the problem.

## Unexpected: a stack interaction with erdafitinib

`cinque2025` — FGF signalling controls **lysosome biogenesis in chondrocytes** via the M6P receptor
pathway through TFEB/TFE3. FGFR3/4-deficient chondrocytes **hypersecrete lysosomal enzymes** with
impaired lysosomal function. **GUSB is a lysosomal hydrolase trafficked by that pathway, and erdafitinib
is an FGFR inhibitor in this stack.**

**The direction is genuinely undetermined** — hypersecretion puts *more* enzyme into the matrix where an
extracellular glucuronide actually is; impaired lysosomal function means less. Neither literature has
looked. New gap with the MUG-assay experiment specified.

## Also read

`abubakar2019` in full — a platform paper. Its value: the **postnatal tibia** is culturable ex vivo to
P13 (23.87 ± 0.80 % growth over 72 h vs metatarsal 40.38 ± 0.95 %), sectionable without decalcification.
Almost all ex vivo work in this atlas is metatarsal; the tibia is the closer analogue to the knee, which
the open-site register makes the largest contributor. Measures chondrocyte **density**, not cell height —
so no h_term value. n falls to 4 by 72 h.

`schneider2022` — a long-acting CNP already exists: [Gln6,14]CNP-38 on tetra-PEG microspheres,
β-eliminative linkers, terminal t½ ~200 and ~600 h, weekly/monthly dosing, mouse growth **equal to or
exceeding daily vosoritide**.

## Files
`voxzogo_epar.pdf` / `.txt` (self-fetched), plus `atlas/data/round206_supplied_bundle_2/abubakar2019.txt`.
