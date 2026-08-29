# F-R091 — SAG vs SAG21k vs the approved agonists, and the gap that actually blocks translation

Tate authorised SAG/SAG21k and asked me to pick the best option and translate it completely.

**I'll give the comparison straight, and I'll say up front where I stop.** I'm not going to write the
self-administration procedure — reconstitution, injection sites, a dosing schedule for putting a research
chemical into a person. SAG has no human toxicology, no GMP source, and the delivery sites that matter
here (intra-articular, intra-epiphyseal) are imaging-guided surgical procedures. A document like that
would get someone hurt, and it's the one thing in this programme I won't produce. Everything else —
the pharmacology, the comparison, the dose arithmetic, the holes — is below, and I think the honest
answer changes the recommendation anyway.

---

## 1. What SAG21k actually is

| | **SAG** | **SAG21k** |
|---|---|---|
| CAS | 912545-86-9 (364590-63-6) | **946002-48-8** |
| EC50, Gli reporter | ~3 nM | **0.3–0.4 nM** (~10× more potent) |
| oral bioavailability | poor | **yes** |
| brain penetrant | limited | **yes** |
| structure with SMO | — | **PDB 6O3C** — active mouse SMO + SAG21k + cholesterol + NbSmo8 |
| systemic in vivo skeletal use | Trompet 2024, 25 µg/g/d i.p. | Rundle/Mohan, murine femoral segmental defect |
| effective in vitro conc. | — | **10 nM** (BMSC, Gli1 "dramatically increased") |

SAG21k is the better molecule on every pharmacological axis. If the question were only "which compound
engages SMO best," it is SAG21k and it isn't close.

---

## 2. But the systemic skeletal precedent is weaker than its abstract

The Loma Linda group (Rundle, Pourteymoor, Kesavan, Mohan) ran SAG21k systemically in a murine femoral
segmental defect. Their own retrospective, in the 2026 follow-up (`PMC12838791`, open access):

> *"The first study applied these mediators through **systemic injections** at different times during
> segmental defect healing and **met with limited success**. A subsequent study emphasized the local
> application and sequential release … from 3D-printed scaffolds. **This local sequential therapy
> approach also met with limited success.**"*

Only after adding exogenous BMSCs — a cell substrate for the drug to act on — did they get bone.

**Read that against Trompet and it is actually consistent, not contradictory.** Trompet's SAG worked
because the growth plate *already contains* the responsive stem population in its niche. The segmental
defect has no such population until you put one there. **Hedgehog agonism does not create stem cells; it
acts on the ones present.** That is a point in our favour — the growth plate is the tissue where the
substrate exists — but it also means the systemic-SAG21k-builds-bone headline does not transfer.

---

## 3. The counterweight, from the people who build these agonists

`Wang, Beachy et al. Nat Commun 2020 (PMC7682405)`, developing a PTCH1 nanobody agonist, open with:

> *"Activation of the Hedgehog pathway may have therapeutic value for improved bone healing… **Systemic
> pathway activation, however, may be detrimental, and agents amenable to tissue targeting for
> therapeutic application have been lacking**."*

That is the field's own assessment, from a lab whose entire purpose is making Hh agonists work.

And the specific hazard is sharper than generic oncogenicity. **SAG21k is brain-penetrant. The cell type
the FGSA paper used to demonstrate Hedgehog agonist efficacy — the cerebellar granule neuron precursor,
where halcinonide produced a 40–50-fold proliferative response — is the cell of origin of
medulloblastoma.** A potent, orally bioavailable, brain-penetrant SMO agonist is, mechanistically, a
medulloblastoma-initiating agent. Tate has ruled risk out of scope; this is not a warning so much as the
reason the compound has no human formulation and never will have one for this indication.

---

## 4. So which agent is actually best?

Being honest about what "best" means when the endpoint is something a person could obtain and use:

| | SAG21k | SAG | **fluticasone / halcinonide (FGSAs)** |
|---|---|---|---|
| SMO potency | **0.3–0.4 nM** | ~3 nM | 99 nM (fluticasone) |
| growth-plate stem data | none | **Trompet: +61% systemic, 2.13× local, durable length** | **none** |
| human exposure | **zero** | **zero** | **decades, millions of people, including children** |
| pharmaceutical grade | no | no | **yes** |
| known PK/PD in humans | none | none | **fully characterised** |
| proven to reach human growth plate | unknown | unknown | **yes — via the growth-suppression side effect** |
| separable from GR arm | n/a (no GR activity — an advantage) | n/a | **yes, survives mifepristone** |
| brain-penetrant | **yes** | limited | no (fluticasone) |

**SAG has the biology; the FGSAs have everything else.** SAG21k has neither the growth-plate data nor
the human data — it has the best receptor numbers and a crystal structure.

**My recommendation is unchanged from F-R090, and the SAG literature strengthens rather than weakens it.**
The thing that makes fluticasone and halcinonide remarkable is not that they're the most potent SMO
agonists — they aren't — but that they are the *only* SMO agonists for which the two hardest questions
in this whole programme are already answered: **does it reach the human growth plate** (yes, proven by
the growth-velocity effect) and **what does chronic human exposure do** (extensively documented).

Potency is the easy problem. You solve potency with dose. You cannot solve "no human has ever taken this"
with dose.

---

## 5. The holes that actually block translation — for any of these agents

These are the same for SAG, SAG21k and the FGSAs, and none of them is about formulation.

1. **No Smoothened agonist has ever been tested on growth-plate cartilage.** Trompet used SAG in mice.
   The FGSA functional assay was cerebellar granule precursors. **The two literatures have never been
   crossed.** Until they are, every human inference is an extrapolation across both species and tissue.

2. **GP1 vs GP2 (F-R090).** Chu shows the human resting zone has a dormant root (GP1: low WNT, low and
   actively repressed TGF-β) above the PTHrP⁺ tier (GP2). Every pool number we have — Trompet's +61%
   included — is measured on a PTHrP reporter, i.e. **GP2**. Hedgehog agonism may be recruiting the root
   rather than expanding it. **Nobody has measured GP1 under any intervention in any species.**

3. **Mouse growth plates never close; human ones do.** Trompet's rats were growing throughout. Whether
   pool expansion in a peri-pubertal human plate translates into length or is simply consumed faster by
   an unchanged fusion clock is untested, and it is the difference between the programme working and
   producing nothing.

4. **Dose–response is unknown in the direction that matters.** Trompet's own data show Hh agonism has
   **opposite signs at different ages**, and F-R022 established that chronic over-drive of this axis
   produces osteochondromas — ectopic cartilage engines that **cost** height (hereditary multiple
   exostoses patients are short). The therapeutic window here is in *dose × duration*, and neither
   bound has been measured for a growth-plate endpoint.

5. **~30 physes plus the spine.** Unchanged from F-R085. Trompet's bead treated one epiphysis. Systemic
   agonism treats all of them, which is what we want, but it also means the dose is set by the most
   sensitive tissue in the body, not by bone.

---

## 6. What I'd ask you for, in order

1. **Rundle CH et al., *Sequential application of small molecule therapy enhances chondrogenesis and
   angiogenesis in murine segmental defect bone repair*, J Orthop Res 2023 (PMID 36448182,
   PMC10506518 — not open access).** This is the **only published systemic SAG21k dosing in a skeletal
   model**: route, schedule, vehicle, duration, and what "limited success" meant quantitatively. It is
   the single most relevant document that exists and I can't reach it.

2. **Any Smoothened agonist — SAG, SAG21k, purmorphamine, or an FGSA — applied to chondrocytes,
   cartilage explant, or growth plate.** Still the missing crossing. If you search one thing, search
   this.

3. **Chu 2026 data files S4/S5** — the WNT and TGF-β gene lists for GP1 vs GP2, to see whether GP1
   carries *PTCH1*, *SMO*, *GLI1* at all. **If GP1 is not Hedgehog-responsive, the entire Hh arm targets
   GP2 and cannot expand the root — and that is knowable today, from a file that may already be on
   disk.** I'll grep for it if you tell me it's in what you sent.

4. **Wang JC et al. PNAS 2010;107:9323 supplementary Figs S5 and S6** — still outstanding from F-R090.
   The GR/SMO separability is load-bearing.

5. **The gettable human experiment, restated:** final adult height in children on high-dose inhaled
   **fluticasone** or extensive topical **clobetasol/halcinonide**, versus **budesonide,
   beclomethasone or prednisolone**, at matched growth-velocity suppression. If the SMO-agonist
   glucocorticoids preserve final height better at equal velocity suppression, **the human trial has
   already been run and is sitting in the paediatric asthma and dermatology literature.** No new
   compound, no new subject. This remains the highest-value, most obtainable item on the list.

---

*What changed this round: I went looking for a reason to prefer SAG21k and found the opposite. Its
systemic skeletal trial under-delivered, the field that builds these agonists says systemic activation
is the wrong approach, and the compound's best pharmacological feature — brain penetration — is its
worst liability given which cell type Hedgehog agonists are known to expand. The approved agonists win
on the only axes that are hard to fix.*
