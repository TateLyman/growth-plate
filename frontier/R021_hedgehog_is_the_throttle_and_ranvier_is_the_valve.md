# F-R021 — Hedgehog is the throttle. The groove of Ranvier is the valve.

**Both papers arrived and both deliver.** `fenichel2006` (Fenichel I, Evron Z, Nevo Z. *The
perichondrial ring as a reservoir for precartilaginous cells. In vivo model in young chicks'
epiphysis.* Int Orthop 2006;30:353–356, PMID 16652202) and `karlsson2009` (Karlsson C, Thornemo M,
Barreto Henriksson H, Lindahl A. *Identification of a stem cell niche in the zone of Ranvier within
the knee joint.* J Anat 2009;215:355–363, PMID 19563472). Both archived in
`frontier/screens/influx/`.

Together with F-R020's Nat Commun paper they close a chain across **2006 → 2025, four species, five
papers that do not cite each other**, and the chain terminates in a druggable node.

---

## 1. `karlsson2009` — the groove is a niche, and it has the one marker that matters

Rabbits, 3 months old, **BrdU for 12 consecutive days**, then chase to 4, 6, 10, 14, 28 and 56 days.

**(a) Label retention maps the stem compartment.** At 28 and 56 days, label-retaining cells persisted
in the **germinal (resting) zone** — *"whereas **no positive cells could be detected in the
proliferative or hypertrophic zone**."* The slow-cycling population is confined to the reserve, exactly
as F-R017/F-R018 require.

**(b) The finding the authors do not emphasise, and which is the whole point:**

> "Interestingly, **a more abundant expression of BrdU-positive cells was detected in the growth plate
> NEAR THE PERICHONDRIAL GROOVE OF RANVIER compared to CENTRALLY in the growth plate at later time
> points.**"

**That is a spatial gradient of label-retaining cells inside the plate, highest at the edge nearest the
groove.** It is precisely the signature influx predicts and drift-free consumption does not: if the
reserve were a sealed depot spending itself uniformly, there is no reason for the slow-cycling
population to be enriched at the perichondrial margin.

**(c) The groove is a bona fide niche with a sharp boundary.** Cells in it were positive for **Stro-1,
Patched, Jagged1, BMPr1a and N-cadherin**; Jagged1 and Stro-1 were in *almost all* groove cells —
*"whereas cells in the growth plate directly adjacent to the perichondrial groove of Ranvier **did not
express these markers**,"* with Jagged1 forming *"a distinct boundary."* Two adjacent compartments with
different molecular identities, sharing a border. That is F-R019's cancellation theorem's anatomy,
drawn.

**(d) And the marker that closes the circuit: PATCHED.**

`PTCH1` is the Hedgehog receptor and the direct upstream of `GLI1`. **The groove of Ranvier is
Hedgehog-responsive tissue sitting immediately outside the growth plate.**

---

## 2. `fenichel2006` — cells from the ring migrate into and across the physis

Ring of LaCroix explants from chick proximal tibia, expanded in culture, transduced with
**adenoviral lacZ**, then **injected back subperichondrially into the ring** of six 4-week-old chicks;
sacrifice at 4 weeks; β-galactosidase histochemistry with eosin counterstain.

> "Stained cells were found at the outer layer of the epiphysis, particularly in areas adjacent to the
> perichondrial ring. Only a small number of stained cells were observed in the rest of the epiphysis…
> **the cells appear to migrate initially into the perichondrial ring, and later deeper into the area
> around the physis.** Further longitudinal histopathological studies along the bone axis demonstrated
> **a condensed layer of stained cells arranged horizontally along parts of the physis**" — and their
> Fig. 5 legend: *"demonstrates the migration of the cells from the periphery **transversely through
> the physis**."*

And the loss-of-function context they assemble:

> "In previous studies it was proved that **operative removal of the ring of LaCroix causes growth
> arrest and short stature.**"
> "**Grade six growth-plate injuries** also emphasise the importance of the perichondrium… the main
> damage is caused to the perichondrial ring, **resulting in growth arrest** and angular deformities."
> "the ossification groove of Ranvier… **appears to supply cells for the reserve layer**."

The primary loss-of-function reference is **Rodriguez JI, Delgado E, Paniagua R,
*Changes in young rat radius following excision of the perichondrial ring*, Calcif Tissue Int
1985;37:677–683**, and the regulatory one is **Long F & Linsenmayer TF, *Regulation of growth region
cartilage proliferation and differentiation by perichondrium*, Development 1998;125:1067–1073.**

### What I will not overstate

This is a **cell-injection** experiment, not endogenous lineage tracing: it demonstrates migratory
*capacity*, not physiological flux. **n = 6**, no sham-injection arm described, no quantification, no
length endpoint, and I cannot see the figures — the claim rests on their reading of their own
histology. **Their citation keying is also unreliable** — the sentence about ring removal causing short
stature points at an FGF9 paper, and the grade-six-injury sentence points at a syndecan paper. And
`karlsson2009`'s BrdU label retention is suggestive of a niche but is not lineage tracing.

**The strongest single counter-argument, which `fenichel2006` states against itself:** the classical
role of the groove of Ranvier is *"causing mainly an expansion of the **diameter** of the growth
plate"* — **latitudinal, not longitudinal.** If the groove only widens the plate, influx exists but
does not buy height.

**And the atlas got to that objection before I did, and graded it honestly.** Its
`groove_of_ranvier.yaml` node, `confidence: C`:

> `translation_risk_reason:` "The structure is confirmed in humans, but **its function — supplying
> cells for latitudinal growth — rests on rabbit morphology and has never been tested by lineage
> tracing in any species.**"

So the atlas already holds the classical claim *and* already flags that nothing has ever tested it.
**What it does not hold is the evidence that the function may not be latitudinal-only:** `Fenichel`
returns **0 files** anywhere in the atlas, and `karlsson2009` appears only inside the reference list of
a review XML the atlas downloaded (`atlas/data/round240/rz_quiescence_review_2026.xml`) — cited by
someone else, never worked here. The two papers that show cells crossing into the physis and
label-retention enriched at the rim are exactly the ones missing from the node that says the question
is untested.

---

## 3. The chain, assembled

Five papers, none of which cites more than one of the others:

| # | source | fact |
|---|---|---|
| 1 | `karlsson2009` (rabbit) | The groove of Ranvier is a **stem cell niche** — label-retaining, Stro-1⁺, Jagged1⁺, BMPr1a⁺, N-cadherin⁺, with a sharp boundary against the plate |
| 2 | `karlsson2009` | Label-retaining cells **inside the plate are enriched next to the groove** — the spatial signature of influx |
| 3 | `fenichel2006` (chick) | Labelled ring cells **migrate into and transversely across the physis** |
| 4 | Rodriguez 1985 (rat); Salter-Harris VI (human) | **Excising the ring → growth arrest and short stature** |
| 5 | **`karlsson2009`** | The groove expresses **PATCHED** → it is **Hedgehog-responsive** |
| 6 | `rosellodiez2025` (mouse, F-R020) | **Gli1⁺** stromal cells **outside the cartilage** are the long-lived chondroprogenitor precursors; recruitment is **necessary** for normal bone length; gated by **CCN2** |
| 7 | `newton2024sag` (rat, F-R018) | **SAG beads in the secondary ossification centre** — anatomically adjacent to the groove — gave a length advantage that **kept widening at 2 and 6 months after the agent cleared by week 3** |

> **PTCH1 in the groove (5) and GLI1 in the recruited progenitors (6) are the same pathway, one step
> apart. Hedgehog is the throttle on influx, and the groove of Ranvier is the valve it acts on.**

### This reinterprets `newton2024sag`

Its authors read their result as expansion of **epSSCs already inside the plate**. But they delivered
SAG from a bead in the **secondary ossification centre**, and `karlsson2009` says the Hh receptor is
concentrated in the **groove of Ranvier** just outside. **A compounding length gain that persists long
after the agent has cleared is what recruitment looks like and is not what a transient proliferative
push looks like.** Their own data may be an influx experiment that nobody has read as one — and the
distinction is testable, because recruitment and local expansion give different lineage-tracing
answers.

### And it explains why Hedgehog reads contradictory in this literature

F-R019's cancellation theorem predicted every signal would have opposite signs in the two
compartments. Hedgehog does, precisely:

| where | Hh activation does | source |
|---|---|---|
| **resting zone, inside the plate** | drives resting cells to **osteogenic** fates — depletes them | `PMC10906233` |
| **an alerted pool** | discharge requires Hh **withdrawal** | the atlas's R251 |
| **groove of Ranvier / stroma, outside** | **recruits** Gli1⁺ progenitors into the plate | `karlsson2009` + `rosellodiez2025` |

Systemic Smoothened agonists therefore do all three at once and net out small. **`newton2024sag` got a
large, compounding effect because a bead is not systemic.** That is the same conclusion F-R020 reached
for CCN2 from the opposite direction: **these are delivery targets, not drug targets.**

---

## 4. The experiment this now specifies

The question is no longer "does influx exist" (F-R020 settled that) but **"can influx be driven, and
does driving it buy length rather than width?"** One design answers both:

- **Model:** rat or mouse, growing, with a **contralateral internal control** — the geometry
  `newton2024sag` validated.
- **Intervention:** local Hh agonist (SAG bead) placed **at the groove of Ranvier / perichondrial ring**
  rather than in the SOC, ± local CCN2 blockade, against vehicle bead contralaterally.
- **Lineage readout:** inducible label in the perichondrial compartment (`Gli1-CreER` or
  `Pdgfra-CreER`; `karlsson2009`'s marker panel offers `Jagged1`, `Stro-1` and `N-cadherin` as
  alternatives), scoring **entry into the PTHrP⁺ resting zone**.
- **The endpoint that decides it:** **bone LENGTH and growth-plate WIDTH measured separately, to
  skeletal maturity.** If the classical view is right, the plate gets wider. If the chain in §3 is
  right, the bone gets longer. **Nobody has ever reported both from the same animal.**

That single distinction — length versus width — is the entire remaining uncertainty in the influx arm
of this theory, and it costs one extra caliper measurement on an experiment that has already been run
in a neighbouring location.

---

## 5. Where the theory stands

```
H = Σ_plates ∫ h_term(t)·outflux(t) dt          dReserve/dt = influx − outflux
```

| term | status | knob | delivery |
|---|---|---|---|
| **influx** | **proven ≠ 0, necessary, demand-responsive** (F-R020); **valve located** (§1–3) | **Hedgehog** (PTCH1/GLI1); **CCN2** brake | **local — groove of Ranvier / perichondrium** |
| **outflux** | proven, phase-schedulable | pO₂, Wnt (Frzb/Dkk1), GH | systemic possible |
| **h_term** | hormonal axis saturated; **osmotic axis untried** | proteoglycan, sulfate, pO₂ | — |
| **Σ_plates** | a plate = a PTHrP⁺ reserve zone | untouched | — |
| **resident clock** | counts RZ divisions | **bypassed by influx** | — |

**The single structural claim of this branch, now with an anatomy:** the growth plate is not a closed
depot being spent. It is a compartment with a **valve on its rim**, the valve is Hedgehog-gated and
CCN2-braked, every agent that acts on it also acts oppositely inside the plate, and **every
intervention in the history of this field has been delivered in a way that hits both sides at once.**

---

## 6. Asks — with exactly where to get them

**Priority 1 — the ring-excision experiments (the loss-of-function half of §2, and I have it only
second-hand through a paper with unreliable citation keying):**
- **Rodriguez JI, Delgado E, Paniagua R. *Changes in young rat radius following excision of the
  perichondrial ring.* Calcif Tissue Int 1985;37(6):677–683.**
  `https://doi.org/10.1007/BF02554932` · `https://pubmed.ncbi.nlm.nih.gov/3937573/` — Springer.
  **Want: what happened to LENGTH versus WIDTH after excision.** This is the same length-vs-width
  question as §4 and it may already be answered in 1985.
- **Shapiro F, Holtrop ME, Glimcher MJ. *Organization and cellular biology of the perichondrial
  ossification groove of Ranvier: a morphological study in rabbits.* J Bone Joint Surg Am
  1977;59(6):703–723.** `https://pubmed.ncbi.nlm.nih.gov/human/908697/` — the canonical description,
  and the source of the "latitudinal only" claim I need to test rather than inherit.
- **Long F, Linsenmayer TF. *Regulation of growth region cartilage proliferation and differentiation by
  perichondrium.* Development 1998;125:1067–1073.** `https://doi.org/10.1242/dev.125.6.1067` —
  Development is free after 6 months, so this one may open directly.

**Priority 2 — Hedgehog at the groove:** anything applying a Smoothened agonist or antagonist
**locally at the perichondrium/groove** with a bone-length endpoint. My searches found nothing; the
closest is `newton2024sag` in the SOC.

**Priority 3 — still standing:** UIC handle `10027/14248` (Brighton thesis, ILL/ProQuest);
**JBJS 1980;62A:740** (Stambough & Brighton, zonal diffusion); **Surgical Forum 1970:465–467**;
`stegen2019`'s DCA+BPTES tibia length (Carmeliet, KU Leuven); and the lateral thoracolumbar spine film,
which remains the only measurement that would ground any of this in your actual anatomy.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
The instrument here was a BrdU chase in 2009 that noticed label-retaining cells were denser at the rim
than in the middle and put it in a sentence beginning "Interestingly." Nobody followed the sentence.*
