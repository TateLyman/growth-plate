# ASK LIST — the root-cell programme (rounds 240–242)

**Every item below was checked against `holdings.py --have` and against the bibliography before it was
written here.** That check is mandatory and it is why this list is short: the previous version of this list
led with a paper the atlas had held for five days (CORR-250). Items that turned out to be obtainable were
removed rather than left in with a note.

**Do not send anything from the "already resolved" section — those are recorded only so the next round does
not re-ask.**

---

## Genuinely unobtained, in value order

### 1. Qin T et al., *Science* 2023 — the ABPC discovery paper
- **PMID 36821675**, "A population of stem cells with strong regenerative potential discovered in deer antlers"
- **Not open access. No PMC record. No preprint found** (searched Europe PMC `SRC:PPR`, bioRxiv API, OpenAlex, Semantic Scholar).
- **Why it matters:** it is the primary source for antler blastema progenitor cells and for the claim, cited
  second-hand by three papers now in the atlas, that ABPCs are *driven by PRRX1+ mesenchymal cells*. Round
  242 currently rests the PRRX1 story on two cell-culture papers from a single laboratory. This is the
  paper that would tell us whether PRRX1 marks the regenerative population in vivo, and at what clonal
  scale.
- **What specifically is needed:** the main text, and the figure showing the PRRX1+ population's contribution
  and clonal output. Supplementary would be a bonus, not the point.

### 2. Hu P et al., *Int J Biol Macromol* 2025 — PRRX1/miR-143-3p
- **PMID 39638193**, doi 10.1016/j.ijbiomac.2024.138366. Not OA, no PMC, no preprint.
- **Why it matters:** it is currently in the atlas at **abstract only, `value_unverified: true`, direction
  only, no magnitude** (round 242). It is the one independent corroboration that PRRX1 overexpression
  *decreases* proliferation and maintains the undifferentiated state — the finding that inverts the obvious
  intervention. A direction-only citation is doing more work than it should be.
- **What specifically is needed:** the proliferation assay figure and its effect size and replicate count.

### 3. `chu2026` supplementary data files S1–S6 — *Sci Transl Med* 2026
- **PMID 41984930**, doi 10.1126/scitranslmed.adw3590. **The main text IS held** (`data/round194_the_supplied_bundle/chu2026.txt`) — do not send that again.
- **The supplementary data files are not held**, and they are where the numbers live:
  - **data file S1** — cluster-specific marker gene lists (would give the exact GP1 signature)
  - **data files S2–S5** — the 147 cross-validated TF regulons along the trajectory, and the β-catenin /
    SMAD2 / SOX4 regulon activity tables that round 241's central claim rests on
  - **data file S4** — the top-160 ligand–receptor pairs by specificity and magnitude
  - **data file S6** — the 113 TFs differentially active in c-GP2 after GH
- **Why it matters:** round 241 records "nine soluble WNT inhibitors against four ligands" from the figure
  text. **The nine are not named anywhere in the main text.** Naming them is the difference between a
  pathway-level claim and a druggable list.
- **Note:** the underlying dataset **GSE288028 is already in the atlas** and has been since Phase 5 — so if
  the supplement is hard to get, most of S1–S3 could in principle be recomputed. That is a fallback, not a
  substitute, and it would be graded as re-analysis.

### 4. *PeerJ* 2026 — antler tip endochondral proteomics
- **PMID 42534826**, "Proteomic dynamics in endochondral ossification: insights from antler tip analysis". Not OA.
- **Lowest priority of the four.** It would add a protein-level check on the transcript-level antler
  signature (do THBS1/THBS4 and the SFRPs show up as protein?), which would strengthen the cross-species
  convergence in round 241 from "gene lists overlap" toward something firmer. Useful, not blocking.

---

## Already resolved — do not send

| What I nearly asked for | Why it was withdrawn |
|---|---|
| `chu2026` main text (Sci Transl Med, the human root-cell atlas) | **Held since 2026-08-06.** Full text on disk, 17,212 words. Round 241 is built from it. CORR-250. |
| `ba2025` (iMeta, antler growth centre multi-omics) | Marked `full_text_read` but never archived, so invisible to search. **Re-fetched from PMC12747533 and archived this round.** CORR-251. |
| The functional PRRX1 experiment | Found open access: **hu2024, PMID 38643083, PMC11031908**, Prrx1/miR-140-3p reciprocal feedback with overexpression and RNAi. This is round 242. |
| Antler single-cell datasets | Three obtained OA this round: PMC12015367 (antlerogenic periosteum, RXFP2 founder), PMC12690211 (antler tip), PMC12747533 (antler growth centre). |
| bioRxiv preprint of `chu2026` | Exists (doi 10.1101/2025.03.14.642964, CC-BY-NC-ND) and bioRxiv was rate-limiting (Cloudflare 1015), but it is **moot** — the published full text is already held. |

---

## Not an ask — the experiment nobody has run

Stated here because it is the real bottleneck and no document will fix it.

**GP1 did not survive explant culture.** In `chu2026`, CYTL1 fell from 175 to 4 reads per positive cell, the
root cluster was recoverable only by a semi-supervised model, and the authors explicitly excluded it from
analysis. So the GH-response transcriptomics are measured in **c-GP2, the PTHrP-positive cell**, and the only
readouts that include root-cell territory are the compartment-level p-Smad2 and p-Smad1/5 counts.

**Nobody has measured what GH does to the root cell itself.** That is the highest-value missing experiment in
this programme, it is not in any paper, and asking for a document will not produce it.

Two further gaps of the same kind, both recorded in the graph rather than here:
- No human number exists for root-cell **self-renewal fraction, pool size, or replacement rate**. GP1's
  proliferative index is a rank across clusters, not a rate.
- **No positive regulator of root-cell self-renewal has been identified** in human growth plate, mouse
  lineage tracing, or antler regeneration. All three literatures have functional handles on the *exit* only.

---

*Last verified 2026-08-11, rounds 240–242. Re-run `holdings.py --have <id>` before acting on any line above —
availability is a timestamped claim, not a standing fact (CORR-250).*
