# L2 — Stem and progenitor biology

**35 nodes · 38 edges · 11 gaps · 44 references · 5 logged contradictions · 1 X-grade claim**

Evidence profile: `human_evidence` **absent on 21 of 35 nodes**, indirect on 9, direct on 5.
`translation_risk` **high on 24 of 35**. Confidence: A 1 · B 2 · C 20 · D 10 · E 1 · X 1.

That profile is the layer's central fact and is not an artefact of incomplete searching.
The defining technique of this field — inducible Cre-lox clonal lineage tracing — cannot
be performed in humans. Nearly everything below is mouse, and the reader should hold that
in mind before transferring any of it.

---

## 1. What is actually established

**The resting zone contains slowly-cycling cells that generate columns clonally, in mice.**
PTHrP-expressing (Pthlh⁺) chondrocytes appear in the centre of the mouse growth plate around
P3 and expand between P6 and P9. They are markedly less proliferative than the cells beneath
them — 6.1% versus 30.5% EdU⁺ at P9, a ratio of 0.20 — and after a P6 pulse their descendants
remain in the resting zone for roughly a week before generating first short (<10-cell) and
then long (>10-cell) columns, continuing for at least a year. Confetti labelling shows each
column is monochromatic, i.e. clonal.

**Multipotency is acquired late, not held in reserve.** Descendants become
Col1a1(2.3kb)-GFP⁺ osteoblasts and Cxcl12-GFP⁺ marrow stromal cells, but **not** adipocytes
in vivo (0 of 443 cells scored under rosiglitazone plus high-fat diet). Whatever the resting
zone cell is, it is not a classical tri-potent mesenchymal stem cell.

**Only a small minority behave as long-term stem cells.** Of P12-pulsed colonies, 16.3%
formed secondary colonies and 12.5% of those could be passaged nine times — roughly **2–3%
of PTHrP⁺ colony-forming cells**. An independent method agrees on the order of magnitude:
durable label-retaining chondrocytes plateau at **2.6% (SE 0.9)** after a doxycycline chase,
decaying with a half-life of ~1.0–1.2 weeks. Two unrelated assays converging on ~2–3% is the
strongest quantitative result in this layer.

**Hypertrophic chondrocytes become osteoblasts, and in young mice they are the dominant
source.** Col10a1-lineage tracing gives **63%** of trabecular and **62%** of endosteal
osteocalcin⁺ osteoblasts at 1 month, and **60%/68%** of Col1a1(2.3kb)-GFP⁺ osteoblasts at
3 weeks. Dual Cre/Dre fate mapping shows this dominance ends at adolescence. This overturns
the older view that hypertrophic chondrocytes simply die.

---

## 2. Where the field disagrees — and it disagrees more than reviews admit

Five schemes claim to describe the skeletal stem cell. They are logged as an explicit
`contradicts` network (C-L2-01…05) rather than blended into a consensus that does not exist.

| Scheme | Marker definition | Problem |
|---|---|---|
| mSSC (Chan/Longaker) | CD45⁻Ter119⁻Tie2⁻CD51⁺CD90⁻6C3⁻CD105⁻CD200⁺ | Panel is **identical to Debnath's periosteal PSC panel**, so it does not specify compartment |
| hSSC (human) | CD45⁻CD235a⁻TIE2⁻CD31⁻PDPN⁺CD146⁻CD73⁺CD164⁺ | **No shared antigen with the mouse panel** |
| PTHrP⁺ / FoxA2⁺ resting chondrocytes | reporter lineage | FoxA2⁺ and PTHrP⁺ barely overlap (0.017% double-positive at P18) |
| Grem1⁺ OCR cells | reporter lineage | Non-adipogenic (0/19 clones), conflicts with LepR⁺ scheme |
| LepR⁺ stroma / CTSK periosteal | reporter lineage | 94% of marrow CFU-F but a different compartment again |

**The most consequential contradiction is anatomical.** The human SSC was localised to the
**pre-hypertrophic/hypertrophic zone** of a 17-week fetal femur — not the resting zone where
all the mouse stem-cell work points. A 2026 report further finds the human resting-zone
"root" cell is **PTHLH-negative**. If both hold, the mouse resting-zone paradigm may not
describe human tissue at all, and the discovery specimen was a *single* fetal femur.

---

## 3. The claim this layer refuses to pass downstream

**"Secondary ossification centre formation triggers resting-zone stem cell acquisition"
has no causal evidence.** Both anchor papers report only that the two events coincide in
time. A Europe PMC search for any SOC ablation, blockade, or delay experiment with a
resting-zone stemness readout returned **zero hits** (logged, gap `g_l2stem_003`).

This matters because L7 (fusion) would otherwise inherit it as mechanism. It is recorded as
`hypothesized_link` edges carrying `confidence: speculative` and a linked gap — which the
validator enforces — so it cannot be silently upgraded to fact by a later pass.

---

## 4. Senescence, catch-up growth, and a model falsified by its own authors

The finite-proliferative-capacity model holds that plates exhaust a fixed division budget.
Catch-up growth supports the **division-dependent** version: catch-up is local to the
growth plate, not systemically driven. But the model's own originators falsified its
Hayflick-style reading — rabbit resting-zone population doublings in vitro are **independent
of donor age**. What does change with senescence is **global DNA methylation, which
decreases**, with no change across the resting-to-hypertrophic transition.

**Telomere attrition is grade X.** It is the most commonly invoked molecular clock for this
model and is routinely asserted in reviews, yet no primary measurement of telomere length or
telomerase activity in *human* growth plate chondrocytes as a function of age could be
traced. Nearest datum is murine and indirect. Logged as `x001`.

---

## 5. The gaps that matter most

Full register in `gaps/gaps.yaml` (`g_l2stem_001`–`011`). The four highest-value:

1. **`g_l2stem_001`** *(method_blocked)* — which human resting-zone cell self-renews, and
   does it express PTHLH? Blocked because clonal lineage tracing is impossible in humans.
   Discriminating route: clonal somatic-mutation phylogenies from microdissected human
   physeal tissue, which needs no genetic labelling.
2. **`g_l2stem_002`** *(quantitative_gap)* — what fraction of *human* osteoblasts derives
   from hypertrophic chondrocytes? The mouse number is 60–68%; no human number exists.
3. **`g_l2stem_009`** *(search_established)* — does the hSSC panel label human resting-zone
   cells, or only pre-hypertrophic/hypertrophic cells as originally reported?
4. **`g_l2stem_011`** *(species_gap)* — does the postnatal clonal switch occur in any
   species that actually **fuses** its growth plates? Every demonstration is in a species
   that does not. This is the hinge between L2 and L7.

---

## 6. How to read this layer

- Treat every marker panel as **species-specific until proven otherwise**; mSSC and hSSC
  share no antigen, so "the skeletal stem cell" is not one entity across species.
- Treat the ~2–3% long-term self-renewing fraction as the layer's most robust number, since
  two independent methods agree.
- Do not carry the SOC-triggers-stemness claim into any mechanistic argument.
- Blocked at source: Chu 2026 (*Sci Transl Med*, **P1**) and Newton 2019 (*Nature*, **P2**)
  are abstract-only. The Newton clonal kinetics and the human PTHLH panel could not be
  verified at source; both nodes are flagged `pending_source` with confidence dropped one
  grade, and both are queued in `sources/access_queue.md`.
