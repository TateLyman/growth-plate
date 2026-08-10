# Round 218 supplied bundle — the two documents that audited round 217

Both supplied by the user on 2026-08-10 with the instruction to *be absolutely sure* about the
round-217 claims. Both came back negative against round 217. Text extracted with PyMuPDF and archived
here because the uploads directory is ephemeral.

| file | source | ref_id | what it settles |
|---|---|---|---|
| `fafilek2017_statins_do_not_inhibit_fgfr_signaling.txt` | Fafilek B et al., *Osteoarthritis and Cartilage* 2017, PMID 28583899, doi 10.1016/j.joca.2017.05.014 — 9 pp | `fafilek2017` | **Refutes the receptor-abundance series node.** Four statins (atorvastatin, fluvastatin, lovastatin, pravastatin) across four systems (RCS chondrocytes, cultured mouse embryonic tibias, limb-bud micromasses, human control + thanatophoric chondrocytes from the ISDR): no change in FGFR3 protein for WT, G380R or K650M, transfected or CRISPR-flag-tagged endogenous, at 12/24/48/72 h. Positive controls run both ways — AZD4547 rescued every readout in the same experiments, Ras prenylation band-shift confirmed statin activity. At 1 µM, statins **alone** inhibited embryonic tibia growth comparably to FGF2. |
| `recifercept_euctr_2020-001189-13_results.txt` | EU Clinical Trials Register, EudraCT **2020-001189-13**, results v1 published **07 Oct 2023**, global end of trial 27 Mar 2023. Pfizer protocol **C4181005**, NCT04638153 — 78 pp | `recifercept_euctr_2023` | **Refutes the ligand series node in humans.** Ratio of observed/expected change in standing height: month 6 **0.9 / 1.1 / 1.0**, month 9 **1.0 / 1.0 / 1.0**, month 12 **0.9 / 1.1 / 0.8** across 1 mg/kg QW (n=20), 2 mg/kg BIW (n=19), 1.5 mg/kg QD (n=18). Day-61 troughs **183.8 / 974.8 / ~3800 ng/mL** — dose-proportional, accumulating, ~20-fold span, so **not** an exposure failure. Terminated 18 Nov 2022 for failing the pre-specified 6-month efficacy criteria, explicitly not for safety. |

## What is NOT in this bundle and was not needed

The `soluble_fgfr3_decoy` node in this atlas **already contained** the recifercept result before the
document arrived. The failure of round 217 was not missing data — it was not opening the atlas's own
node. See CORR-213.

## Provenance note

`fafilek2017` was located and added to the bibliography by PMID during round 218; the supplied PDF is the
same paper and was read in full. The EUCTR document is not PubMed-indexed and was added with
`addref.py --manual` (`verify_by_hand: true`).
