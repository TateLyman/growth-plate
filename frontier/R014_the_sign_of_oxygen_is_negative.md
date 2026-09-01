# F-R014 — The sign of oxygen is negative

**Sources read in full this round:** `brighton1971b` (Brighton CT, Heppenstall RB. *Oxygen Tension of
the Epiphyseal Plate Distal to an Arteriovenous Fistula.* Clin Orthop Relat Res 1971;80:167–173 —
**PMID 5133323**, the paper whose abstract is not deposited anywhere; recovered from scanned page
images) · `serrat2010` (Serrat MA, Williams RM, Farnum CE. *Exercise mitigates the stunting effect of
cold temperature on limb elongation in mice by increasing solute delivery to the growth plate.*
J Appl Physiol 2010;109:1869–1879, **PMID 20930127**) · `zhang2024` (Zhang Z, Boggavarapu NR, … Sävendahl
L, Zaman F. *Genomic Effects of Biomechanical Loading in Adolescent Human Growth Plate Cartilage:
A Pilot Study.* Cartilage 2026;17(3):829–844, **PMID 39655393**) · `yoshida2018` (Yoshida E, Suzuki T,
Morita M, … Yamamoto M. *Hyperactivation of Nrf2 leads to hypoplasia of bone in vivo.* Genes Cells
2018;23:386–392).

---

## 0. The correction, first

I have had the sign of oxygen wrong for four rounds.

F-R005 named avascularity as the ceiling and built a ladder whose rungs included *"perfuse without
ossifying."* F-R011 compressed the branch to **`Growth = SYNTHESIS × DISCHARGE, and OXYGEN sets
both`**. F-R013 corrected the target to *delivery to an avascular tissue* — right term, but I left
oxygen inside "delivery," as though more of everything were better.

`brighton1971b` is the experiment that decides it, and it says the opposite:

> **"The optimum oxygen tension at the bone-cartilage junction is low; low oxygen tension enhances
> anaerobic metabolism and stimulates plate growth; high oxygen tension enhances aerobic metabolism
> and retards plate growth."**
>
> **Low O₂ Tension → Anaerobic Metabolism → Increased Plate Growth.**
> **High O₂ Tension → Aerobic Metabolism → Decreased Plate Growth.**

Oxygen does set it. **It sets it with a negative sign.**

---

## 1. `brighton1971b` — the one experiment that manipulates limb perfusion and measures plate pO₂

Side-to-side anastomosis, left common femoral artery to vein, 18 mongrel puppies. Oxygen
microcathode inserted under a dissecting microscope into each named zone of the proximal tibial
plate, calibrated in 21/15/10/5/0% O₂ at 37 °C; **electrode position confirmed histologically by a
deliberate electrical burn defect** (60 V, 100 mA at the cathode tip), and *"any reading that could
not be so confirmed was disregarded."* Contralateral limb as the paired internal control. Readings
at 1 day, 3 days, 1 week, 3 weeks. Six dogs whose fistula spontaneously closed serve as a negative
control.

**The model is the point.** They chose it because it is the one manipulation that reliably lengthens
a limb:

> "When the fistula was created further distally, between the femoral artery and vein, **the
> ipsilateral tibia exhibited lengthening in 100 per cent of the puppies.**"

### Table I — the pO₂ map of the growth plate

First value mmHg, parenthesis **% O₂** (this is stated in the table footnote and is not a standard
deviation — I nearly read it as one):

| zone | control | A-V side, 3 wk |
|---|---|---|
| secondary epiphysis | 115.5 (15.2%) | 82.8 (10.9%) |
| **zone of cell columns** | **45.6–53.2 (6.0–7.0%)** | **23.6–30.4 (3.1–4.0%)** |
| **zone of hypertrophic cells** | **16.0–16.7 (2.1–2.2%)** | **7.6–9.1 (1.0–1.2%)** |
| metaphysis | 11.4–47.1 (1.5–6.2%) | 3.8–8.4 (0.5–1.1%) |
| diaphysis | 106.4–115.5 (14.0–15.2%) | 76.7–85.1 (10.1–11.2%) |

That table is the answer to the ask I made two rounds ago, withdrew last round as probably
nonexistent, and reinstated in F-R013. **The normal growth plate runs its proliferative zone at
6–7% O₂ and its hypertrophic zone at 2.0–2.2%, between a 15% epiphysis above and a 14% diaphysis
below.** It is a hypoxic slot cut into well-oxygenated bone.

### The result

Oxygen tension distal to the fistula was **significantly lower in every zone**, and the deficit
*widened* with time:

| | paired t-test, all zones |
|---|---|
| day 1 | P < 0.2 (ns) |
| day 3 | **P < 0.01** |
| week 1 | **P < 0.01** |
| week 3 | **P < 0.001** |

Zone-wise at 3 weeks: cell columns **−3.48% O₂, t = −6.94, P < 0.001**; hypertrophic cells
**−1.00% O₂, t = −6.32, P < 0.001**; metaphysis −1.64%, P < 0.05; diaphysis −3.20%, P < 0.001.
**In the six dogs whose fistula closed, there was no significant difference between sides** — the
negative control works.

> "Since the plate distal to a patent, functioning arteriovenous fistula is growing at an increased
> rate, **the lowered oxygen tension found in such a plate is associated with increased plate
> growth.**"

### And it is not a consumption artefact

The obvious objection is that a faster-growing plate burns more O₂. They had already killed it:

> "…oxygen tension in the different zones of in vitro epiphyseal plates **did not decrease when
> dormant explants began growing.** … the oxygen tension at day 0 was the same as that at day 3 and
> day 7 in that experiment. **Despite increased epiphyseal plate growth, the oxygen tension at the
> zone level did not change. Little oxygen was consumed in the face of active bone growth.**"

So the plate's low pO₂ is a **delivery** property, not a consumption product — which is precisely
what makes it a manipulable variable rather than a readout.

### Two more dose-responses in the same direction

1. **In vitro (Brighton, Ray, Soble & Kuettner, JBJS 1969;51A:1383 — "In vitro epiphyseal plate
   growth in various oxygen tensions"):** *"when **less** oxygen was supplied to epiphyseal plate
   explants, there was **greater** bone formation, and when **more** oxygen was supplied, there was
   **less** bone formation."*
2. **The in vivo/in vitro contrast:** *"the in vivo plate grows at a rate **five times greater** than
   the in vitro plate, yet the oxygen tension in the former is some **four to five times lower**."*

Three independent designs — surgical, culture, and natural contrast — all with a negative slope.

---

## 2. `serrat2010` — the other arm, measured directly, and it is local

68 weanling female mice, 16 °C or 25 °C, ± voluntary running wheel, 11 days. **In vivo multiphoton
microscopy of fluorescein delivered by intracardiac injection**, imaged in the proximal tibial growth
plate at rest under anaesthesia.

- **All runners had significantly longer limbs, regardless of temperature**: femur F = 18.3
  (**P < 0.001**), radius F = 10.4 (P = 0.001), tibia F = 8.7 (P = 0.003), humerus F = 7.4 (P = 0.005).
- **Solute delivery: fluorescein intensity ≈1.5-fold greater in the growth plates of wheel-running
  mice within 5 min of injection, regardless of temperature.**
- **The control that makes it:** *"Tail length was increased by temperature but was unaffected by
  wheel running, indicating that the exercise effect occurred directly on the weight-bearing
  limbs."* Not endocrine. Not systemic. **Local, and mediated by transport.**
- And the dissociation: temperature changed limb length but **not** solute delivery, so temperature
  and exercise lengthen limbs by different routes. Exercise's route is delivery.

---

## 3. The two arms move in opposite directions on oxygen — and the fistula does both at once

This is the round's result.

| intervention | solute/flow delivery | plate pO₂ | length |
|---|---|---|---|
| femoral A-V fistula (`brighton1971b`) | ↑ (flow, congestion) | **↓ every zone, P<0.001** | **↑ in 100% of puppies** |
| wheel running (`serrat2010`) | **↑ 1.5× (measured)** | not measured | **↑ all four long bones** |
| more O₂ in culture (Brighton 1969) | — | ↑ | **↓** |
| in vivo vs in vitro | ↑ | ↓ 4–5× | **↑ 5×** |

An arteriovenous fistula raises limb blood **flow** and venous pressure while shunting arterial blood
past the capillary bed — it delivers **more volume and less oxygen** to the tissue. That is not a
side effect of the model. **It is a device that does exactly the two things this table says lengthen
a bone, and it is the single most reliable lengthening intervention in the literature: 100%.**

So the branch's equation is not `Growth = f(delivery)`. It is:

> **Length ∝ (substrate delivery) × (glycolytic capacity), with pO₂ entering NEGATIVELY.**

You do not want to oxygenate the growth plate. You want to **flood it with glucose and amino acids
while keeping it hypoxic.** F-R005's rung *"perfuse without ossifying"* had the right verb and the
wrong cargo.

### This also reconciles Stegen 2019, which I had been reading backwards

F-R011 and F-R012 treated `stegen2019` as evidence that hypoxic signalling costs length. Re-reading
its own text against Brighton, the actual oxygen went the other way:

> "Mitochondrial content was reduced… Consistently, mitochondrial oxygen consumption was decreased,
> **making centrally localized chondrocytes less hypoxic.**" — `stegen2019`

**Stegen's dysplastic, short-tibia mutant is a *less hypoxic* plate.** Brighton predicts that plate
grows worse, and it does (tibia length P = 1×10⁻⁸). The two papers agree, 48 years apart, and I had
them in opposition. Brighton even anticipated Stegen's metabolic finding from enzyme histochemistry:
the plate is *"predominantly glycolytic in character,"* the **zone of cell columns contains the
highest activity of the glycolytic enzymes**, the hypertrophic zone *"too, followed predominantly an
anaerobic pathway,"* and there is *"low oxygen consumption in epiphyseal cartilage."* Stegen's
sentence — *"Glycolysis is the most important energy-producing pathway in chondrocytes"* — is the
same claim with isotope tracing instead of a microelectrode.

---

## 4. `zhang2024` — what the human plate does when you load it

Three children, biopsies taken at epiphysiodesis, cultured ex vivo, **cyclical loading at peak 0.4 N,
0.77 Hz, for 30 seconds**, RNA-seq 24 h later. The only transcriptomic read-out of mechanical loading
in human growth-plate cartilage that exists.

Upregulated pathways: **notch**, **oxytocin**, **tight junction**. Downregulated: **lysosome**,
**sphingolipid metabolism**, **PPAR**. Genes: PSEN2, HEY1, NCOR2 (notch); CACNB1, PPP3R2 (oxytocin);
ACTR3C, WHAMM, ARHGEF18 (tight junction); ARSA, SMPD1, CD68 (lysosome); **SLC27A4 and AQP7 (PPAR),
both down**; and **AQP9 up** among the genes shared between patients.

Two aquaporins and a solute carrier move, and the tight-junction pathway — the machinery that sets
what crosses a tissue — is one of only three upregulated. **Thirty seconds of physiological cyclic
load, and 24 hours later the human growth plate has remodelled its water-and-solute transport
apparatus.** Cartilage is avascular and is perfused by convection driven by cyclic loading; this is
the human plate's transcriptional half of Serrat's fluorescein measurement.

Limits, plainly: n = 3, ex vivo, a single 30-second bout, no length endpoint, and the authors call it
a pilot. It is a mechanism read-out, not a result.

---

## 5. `yoshida2018` — the mammalian counterweight to F-R013's NRF2 lead, and I am taking it seriously

I asked last round for *"anything with Nrf2 and a mammalian bone-length endpoint."* Here it is, from
Yamamoto's lab — the lab that discovered Keap1 — and it points the other way.

NEKO mice (Keap1⁻/⁻ with squamous-epithelium-specific Nrf2 deletion to rescue the juvenile lethality,
so Nrf2 is constitutively hyperactive in nearly every tissue): small body, **significantly shorter
femur (n = 6 vs 6, P < 0.05)**, increased radiolucency, decreased cortical thickness, decreased vBMD
and cortical TMD, and low blood ionized calcium. Mechanism assigned to **osteoblasts** — both
osteoclast and osteoblast differentiation were attenuated in Keap1-null primary cells, with
osteoblast impairment dominant.

Two things keep this from simply cancelling `chang2023`, and one thing makes it stick:

- **It is not the growth plate.** *"Thickness of femur growth plate was not affected in the mice"*;
  Alcian-blue cartilage intensity only *"tends to be decreased."* The lesion is osteoblastic bone
  formation, not chondrocyte output.
- **It is constitutive, systemic, lifelong, maximal activation** from germline Keap1 deletion — with
  nephrogenic diabetes insipidus and hypocalcaemia on board. That is not a drug dose. Nrf2 is a
  textbook hormetic factor, and `chang2023`'s own reference 13 (Nrf2 overexpression inhibits ATDC5
  differentiation) sits on the same side.
- **But their renal control is good**: kidney-specific Keap1 knockouts have the same diabetes
  insipidus and **normal femur length**, so the skeletal phenotype is not secondary to the renal one.
  They did not control for the hypocalcaemia or the general failure to thrive.

**Re-grade:** F-R013 called NRF2 the best out-of-the-box lead in the repository. It is now a
**dose-dependent lead with an unresolved direction in mammals** — positive on endochondral length in
zebrafish under transient pharmacology, negative on bone mass and femur length in mice under
constitutive maximal activation, with the growth plate itself spared in the negative study. It stays
on the list. It does not stay at the top of it, and I am not going to quietly keep the good half.

There is also a clean mechanistic reason not to abandon it: NRF2's program is **glutathione, NADPH
and the pentose phosphate pathway** — reductive, cytosolic, anaerobic-compatible capacity. That is
the arm Brighton says the plate runs on. NEKO's lesion is in osteoblasts, which are the aerobic
compartment on the far side of the chondro-osseous junction. The two results may not even be about
the same cell.

---

## 6. What this makes of the branch

Everything the branch has found now sits on one axis with a sign on it:

- **F-R003**: the plate is a transport-limited, avascular, cysteine-poor compartment secreting
  collagen at the plasma-cell ceiling. → the substrate arm.
- **F-R012**: length is bioenergetic, spent at prehypertrophy where collagen synthesis runs 17–20×
  the proliferative rate (Oohira); matrix clearance is a mass valve, not a length valve.
- **F-R013**: six starred, unworked leads that are all delivery.
- **F-R014**: the delivery is of **substrate**, and **oxygen is the term that must go DOWN.**

The productive intervention class is therefore not an agonist, not a protease, not a cross-link
manipulation, and not oxygenation. It is: **raise convective solute delivery to the plate while
holding or lowering its oxygen tension, and raise the cell's glycolytic/reductive capacity to use
what arrives.** Loading and exercise do the first (Serrat: 1.5×, local, four bones). An A-V fistula
does the first and second simultaneously and lengthens 100% of limbs. Nothing in the literature has
ever done all three at once, and nothing has ever tried the third deliberately.

### What the atlas actually holds — I checked before claiming, and my first draft was wrong

I drafted this section asserting the atlas held none of it. It holds most of it, and well. Correcting
myself rather than shipping the claim:

| term | files | what is there |
|---|---|---|
| `arteriovenous fistula` | 14 | **`R450 — the perfusion term and the metaphyseal delivery route`** is a full node on exactly this: *"every abandoned method that worked worked by raising local perfusion"*, Brodin 1955, Nordentoft 1964, sympathectomy, the human anisomelia series |
| `Serrat` | 35 | **`local_limb_warming_is_a_free_delivery_and_growth_lever.yaml`** holds serrat2008/2009/2010/2014/2015/2017 as a corpus |
| `solute delivery` | 20 | in those two nodes |
| `Brighton` | 51 | `brighton1971` (PMID 5580029) is in the bibliography and in `hypoxic_gradient_signaling.yaml` |

**So the delivery term is not the gap. F-R013's "the plate is supply-limited" was, to a large extent,
already this atlas's position — R450 says it plainly and I should have found it before writing that
sentence.** The gap is narrower and it is the whole of this round:

`atlas/nodes/L3_signaling_networks/hypoxic_gradient_signaling.yaml` carries `brighton1971` as
**`type: primary_abstract_only`** — the atlas has never read it — with this as its entire recorded
content:

> `one_line_finding: Oxygen tension was measured by microelectrode across epiphyseal plate zones,
> metaphysis and diaphysis in rats and rabbits.`

**No numbers. No zone values. No direction. No sign.** The node's framing throughout is oxygen as a
*positional patterning cue* for HIF1A — `confidence: D`, `human_evidence: absent`. And a grep for any
statement that low oxygen *increases* growth rate returns **nothing anywhere in the atlas.**

Meanwhile `atlas/gaps/search_log.yaml` records both papers as sought and not obtained — and describes
**PMID 5133323 as "rabbit."** It is 18 mongrel **puppies**. The atlas has been carrying a species
error on a paper it could not get.

**The gap, precisely: the atlas holds oxygen as a patterning gradient and has never held it as a
rate-setting variable with a negative sign.** That is what these two papers supply, and it is why
R450's excellent perfusion node stops at "raise local perfusion" without asking what is being
perfused — the one question that separates a vasodilator from an A-V fistula, which R450's own alias
list (*"why a vasodilator is not an AV fistula"*) shows it was already circling.

---

## 6a. Proposed atlas changes

1. **Upgrade `brighton1971` from `primary_abstract_only` to primary**, and replace its one-line
   finding with the zone table in §1 and the direction. Its companion, **PMID 5133323
   (`brighton1971b`)**, should be entered as a new primary — and the search log's species should be
   corrected from *rabbit* to *dog (18 mongrel puppies)*.
2. **`hypoxic_gradient_signaling.yaml` needs a second claim.** It currently says oxygen *patterns*
   the plate. It should also say oxygen *rate-limits* it, with a negative sign, on three independent
   designs (A-V fistula in vivo, explant culture dose-response, in vivo/in vitro contrast).
3. **A correction-ledger entry.** Proposed wording: **"Perfusion is not oxygenation. The one
   manipulation that lengthens a limb in 100% of animals — a femoral A-V fistula — raises flow and
   LOWERS growth-plate pO₂ in every zone (P<0.001 at 3 weeks). Before pricing any delivery
   intervention, ask which it does to oxygen. (brighton1971b; and Brighton 1969: less O₂ to explants
   → more bone formation, more O₂ → less.)"** This is the missing half of R450.
4. **`serrat2010`'s exercise arm deserves separating from the warming node.** Temperature changed
   limb length but *not* solute delivery; exercise changed both. They are two mechanisms filed as
   one.
5. **Re-grade the F-R013 NRF2 lead** with `yoshida2018` attached, per §5.

---

## 7. Asks

**#1 — Brighton, Ray, Soble & Kuettner, JBJS 1969;51A:1383**, *"In vitro epiphyseal plate growth in
various oxygen tensions."* This is now the most important unread paper in the branch. It is the
**dose-response curve of growth against pO₂** — the thing that says whether the optimum is 2%, 1%, or
lower, and whether the curve has a floor. Every quantitative claim in §3 rests on a one-sentence
summary of it. Also **Brighton & Heppenstall, JBJS 1971;53A:719–728** (the companion zone-map paper,
PMID 5580029) if you can still get it — I have its content second-hand through this paper but not its
own tables.

**#2 — Kelly (ref 12 in `brighton1971b`), the tibial lengthening series.** The "100 per cent of
puppies" claim and the *"tibial nutrient artery and vein oxygen saturation differences highest at 3
weeks… in 18 puppies followed for up to 25 weeks."* I want the actual **millimetres of lengthening
per limb** and how long it persisted after 3 weeks. That number is the effect size of the best
intervention in this literature and I am currently quoting a proportion without a magnitude.

**#3 — `zhang2024` supplementary / the count matrix.** The paper reports 15 pathway genes plus 20
up / 6 down shared between two patients. I want the full differential-expression table to test one
specific prediction: **does the human plate's loading response include glycolytic enzymes, glucose
transporters (SLC2A1/3), or HIF targets?** If loading raises glycolytic capacity as well as
transport, §6's three arms collapse into one intervention. `zhengpei.zhang@ki.se` /
`farasat.zaman@ki.se` are in the paper.

**#4 — any modern replication of the A-V fistula result with a length endpoint**, or any measurement
of growth-plate pO₂ in a *human*. The fistula literature is 1950s–1970s orthopaedics; if someone has
redone it with µCT and a modern oxygen probe, that paper decides whether §3 is a curiosity or a
programme.

**Still open and unchanged:** `stegen2019` DCA+BPTES tibia length (Carmeliet, KU Leuven — still the
single most decisive unmeasured number); McGarry 2024 (PMID 39090666) full text; and the lateral
thoracolumbar spine film.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
The instrument here was a glass microelectrode with a burn-marked tip, in 1971, and it has been
sitting in the atlas's own coverage table at tier ZERO with the abstract not deposited anywhere on
the internet. The answer was not hard to see. It was hard to find.*
