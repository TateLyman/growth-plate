# F-R035 — The two papers hunted to exhaustion, and the delivery term that changes the answer

**Branch:** `claude/height-enhancement-research-v34b4r`
**Date:** 2026-08-28
**Status:** 1969 substantively recovered; 1980 partially recovered and verified genuinely closed. Both
change F-R034 §7. A third thing turned up that matters more than either.

---

## 1. Retrieval report

I did not route around any paywall. Everything below came from indexed abstracts, open repositories,
citing-work restatements, or files already in this repository.

### Brighton, Ray, Soble & Kuettner 1969 — **results recovered, PDF not**

*"In vitro epiphyseal-plate growth in various oxygen tensions."* **JBJS Am 51(7):1383–96, PMID 4186275,
DOI `10.2106/00004623-196951070-00018`.**

**The findings, which is what I wanted:**

- **The cartilage portion of the plate showed maximum growth at 21% O₂ (160 mmHg).**
- **Maximum metaphyseal bone formation — by macrophotography, microradiography and tetracycline
  staining — occurred at 5% O₂ (38 mmHg).**
- **Above 21%:** cartilage narrowing, *"a progressive loss of acid mucopolysaccharide stainability,
  eventual loss of the zone of hypertrophic cells, and an accumulation of neutral mucopolysaccharide or
  glycomucoprotein at its base."*

**A retrieval note worth recording so nobody repeats it.** Unpaywall reports this DOI as **`is_oa: true`,
`oa_status: green`**, pointing at a figshare thesis deposit — *"IN VITRO EPIPHYSEAL PLATE GROWTH IN
VARIOUS OXYGEN TENSIONS", Carl Theodore Brighton*, `figshare.com/articles/thesis/…/10911983`. **That is a
false positive.** `api.figshare.com/v2/articles/10911983` returns `files: []` and
`/files` returns `[]`; the license is *"In Copyright"*; it is a metadata-only ProQuest dissertation stub.
The UIC INDIGO handle `10027/14248` — on this branch's standing list since an earlier round as
*"Brighton thesis, Restricted Access"* — resolves to **the same record**. So the standing "Brighton
thesis" ask and this paper are one item, and it has no file behind it anywhere.

### Stambaugh & Brighton 1980 — **partially recovered, verified genuinely closed**

*"Diffusion in the various zones of the normal and the rachitic growth plate."* **JBJS Am 62(5):740–749,
PMID 7391097, DOI `10.2106/00004623-198062050-00007`.**

**What I recovered**, via Serrat et al. 2014 (PMC3921350), which cites it in text rather than only in its
reference list:

> *"**Stambaugh and Brighton demonstrated that diffusion coefficients for radioactively labeled insulin
> in the reserve growth plate zone were over twofold greater at 22°C than at 4°C.**"*

So: the solute was **radiolabelled insulin (~5.8 kDa)**, the endpoint was **zone-specific diffusion
coefficients**, there is a **temperature dependence of >2× over 4→22°C in the reserve zone**, and the
design compared **normal against rachitic** plates.

**What I could not get: the zone-by-zone table.** Routes tried and their outcomes —

| route | result |
|---|---|
| PubMed abstract | none — pre-abstract-era JBJS |
| Unpaywall | `is_oa:false`, `has_repository_copy:false`, `oa_locations: []` |
| Europe PMC / PMC | no record |
| Internet Archive (fatcat) | no scan |
| OpenAlex | `oa_status: closed`, no OA URL |
| JBJS / LWW / Ovid | Cloudflare 403; Ovid returns **HTTP 402 Payment Required** |
| citation harvest | 11 citing works; **1** in Europe PMC full text; **1** quantitative restatement (above) |
| figshare / UIC INDIGO | no deposit |

That is as far as legitimate retrieval goes. **It needs a library scan or an interlibrary loan** —
a photocopy of pages 740–749 of *JBJS Am* vol. 62 no. 5 (July 1980) would close it.

---

## 2. What the 1969 dose-response does to F-R034 §7

F-R034 concluded that **hypoxia is the pool-preserving `a − b` lever**. The 1969 data refines that and
puts a ceiling on it.

| O₂ tension | effect |
|---|---|
| 5% (38 mmHg) | **maximum metaphyseal bone formation** — the discharge/ossification end |
| **21% (160 mmHg)** | **maximum cartilage growth** — the plate's own production |
| >21% | **toxic**: narrowing, loss of proteoglycan stainability, **loss of the hypertrophic zone** |

Set beside `leijten2012` (2.5% vs 21% fetal explants): 21% → more length, bigger hypertrophic zone,
hypertrophic genes; 2.5% → bigger resting zone, chondrogenic genes, GREM1/FRZB/DKK1. **The two agree.**

> **Within the physiological range, raising pO₂ shifts cells from reserve toward hypertrophy — `a − b`
> falls, elongation rises. Lowering it holds them in reserve — `a − b` rises, elongation falls.
> The cartilage optimum is ~21%, and above that the tissue is damaged rather than driven.**

So the F-R034 §7 reading survives as a **monotone knob with a ceiling**, not as "hypoxia is good." And it
sharpens the in-vivo picture: Brighton's own electrode data put the proliferative zone at **6.0–7.1%** —
**the living plate runs far below its in vitro cartilage-growth optimum**, on the reserve-preserving side
of the curve. That is the velocity-versus-duration trade of F-R016, now with a measured dose axis.

---

## 3. The contradiction I flagged in F-R034 is resolved, and it is perfusion

F-R034 recorded an unresolved 40-year clash: Brighton's A-V fistula **lowered** pO₂ in every zone and
lengthened **100%** of puppies, while Leijten's normoxia **raised** length. The resolution is that the
fistula does not test oxygen.

**An arteriovenous fistula is a massive flow intervention.** Serrat 2014 quantifies what raising limb
perfusion does: **blood velocity +118%, vessel diameter +31%**, and tracer entry into the growth plate
up **>150%** for a 10 kDa solute. Serrat 2009: with body core clamped at 36°C, immersing the hindlimb at
36 versus 23°C **nearly doubled** fluorescein infiltration into the plate. A fistula's low pO₂ is the
*signature* of arteriovenous shunting, not its growth mechanism.

And this branch's transport conclusion converges with an independent atlas result I had not read.
`the_plate_is_advection_fed_not_diffusion_limited` reaches the same place by measurement rather than by
Brighton's 1971 reasoning:

- measured diffusivity across the plate, **20–60 µm²/s** for a 10 kDa tracer — not the theoretical value
- **interstitial flow ≈ +2.5 µm/s through the epiphyseal half and −2 µm/s through the metaphyseal half,
  converging near position 0.62** — inward from *both* junctions
- **Péclet number 6–25 → delivery is advective**
- **Damköhler number 0.015–0.185 → only 1–18% of arriving ligand is consumed in transit.**
  *"A tissue that consumes a few per cent of what crosses it is not consumption-limited."*
- the axial profile is a **hump toward the centre, not a U** — convergent inflow, not a depleted interior

**That is Brighton's "little oxygen was consumed in the face of active bone growth", derived
independently, quantitatively, from a modern FRAP dataset.** Two routes, one conclusion. It also
corrects my geometry a second time: F-R033 modelled a one-sided slab; the plate is fed **convergently
from both junctions**.

> **F-R034 §3 stands and is sharpened: oxygen is a signal, not a supply. The supply is advective flow —
> and it carries everything else.**

---

## 4. The thing that matters more than either paper: the size gate

Hunting the 1980 paper produced Serrat 2014 in full, and with it a constraint that governs every
intervention this programme could ever propose:

> *"Williams et al. further described a **transport block at the metaphyseal chondro-osseous junction**
> and showed that **molecules >10 kDa were essentially size excluded from the growth plate**."*

Serrat's own numbers: heating 22→34°C raised **10 kDa** entry **>150%**, but **40 and 70 kDa** by
**<50%** — *"the 10-kDa dextrans were partially size excluded"*, and even at 10 kDa the entry is limited
while a 332 Da tracer *"appeared bright in both vasculature and growth plate within minutes."*
Charge matters too: anionic solutes are repelled by the matrix proteoglycans.

**Put the therapeutic sizes against that gate:**

| agent | mass | verdict |
|---|---|---|
| small molecules (SAG, CREB inhibitors, HIF stabilisers) | <500 Da | **enter freely** |
| CNP-38 / vosoritide class | ~4 kDa | enters, partway down the partition slope |
| **IGF-1** | **7.6 kDa** | **enters** — and Serrat 2017 images it reaching a live plate within 30 min |
| **growth hormone** | **22 kDa** | **essentially size-excluded** |
| monoclonal antibodies | ~150 kDa | excluded |

**And that predicts `chu2026`'s null.** GH acts on human plate *explants* — 1–2 mm slices bathed in
medium, no barrier — where it triples GP3 cycling. In an intact limb, a 22 kDa protein is on the wrong
side of a 10 kDa gate. **The direct-GH-on-plate mechanism may be largely an explant artefact of
bypassing the transport block**, which is a testable, non-obvious reconciliation of the whole GH
literature with `chu2026`'s **P = 0.1827** length endpoint.

**This is a hard filter on the agent list, and it applies before any of the mechanism questions.**

---

## 5. Credit where the atlas already had it

I found the Serrat body of work by hunting citations of the 1980 paper and briefly thought it was new.
**It is not — the atlas holds it, graded, in `local_limb_warming_is_a_free_delivery_and_growth_lever`**,
with serrat2008/2009/2010/2013/2014/2015/2017 and racine2018. Its numbers: unilateral 40°C, 40 min/day
for 14 days post-weaning gave **femur +1.3%, tibia +1.5%, tibial elongation rate +12% (15 µm/day)**,
persisting at ~1% seven weeks later, with **body mass and humerus unaffected** and left–right differences
**absent in controls**; racine2018 replicated at one week (tibia t=7.7, femur t=11.5, both p<0.001).

**And it holds the two things that stop it being an answer**, which I would have missed:

- **serrat2013** resolved elongation into two phases — *"an initial RAPID phase whose rate is directly
  temperature-dependent, and a second phase in which rates are IDENTICAL across 7, 21 and 27°C."*
  **The skeleton is temperature-responsive only inside a window of rapid growth.**
- **Ring & Lee 1958**, via nordentoft1964: **40°C maintained around the epiphyseal zones at the knee in
  four children** with poliomyelitis sequelae — **no influence on longitudinal growth.** Same
  temperature, same anatomical target, same endpoint, in humans.

**serrat2008 is the one that keeps it alive as mechanism rather than plumbing:** chondrocyte
proliferation and matrix volume correlate with temperature in **metatarsals cultured without any
vasculature.** Temperature acts on the cartilage directly, not only through flow.

---

## 6. Where the three terms stand

| term | status |
|---|---|
| **never close** | solved in humans, both directions (ESR1 receptor-level durable; ligand-level a knife edge) |
| **unlimited** | `a − b ≥ 0` has a lever with a dose axis: pO₂, monotone to ~21%, toxic above, acting through GREM1/FRZB/DKK1 — the same antagonist set that defines the human root niche in `chu2026`. Not a tumour suppressor. Local by nature |
| **fast** | still the hard one. Every candidate now has to clear the **10 kDa gate** first, and the delivery term is **advective** — which is why heat, exercise and an A-V fistula all work, and why they are window-limited and have one small human negative |

**What this round killed:** "hypoxia is good" as a simple statement — 21% is the cartilage optimum and
above it the tissue is damaged; and the last of my one-sided-slab geometry.
**What it fixed:** the Brighton-vs-Leijten contradiction (perfusion, not oxygen), and my §3 supply
claim, which was right about oxygen and wrong to conclude there is no supply term at all — there is, and
it is advection.
**What it added:** the size gate, which is the first constraint in this programme that filters *agents*
rather than *mechanisms*, and which predicts `chu2026`'s null.

---

## 7. What I still need

**1. Stambaugh & Brighton 1980, *JBJS* 62A:740–749 — a library scan or ILL copy.** Everything else is
exhausted (§1). What the table would settle: **the zone-by-zone diffusion coefficients**, which is the
only existing measurement of how a peptide-sized solute moves through each compartment, and the
**rachitic comparison** — a natural experiment in a plate whose zone geometry is grossly deranged. With
the size gate now load-bearing, this is the paper that calibrates it.

**2. Williams et al. — the >10 kDa size-exclusion study.** Cited as ref 99 in Serrat 2014 alongside
Farnum (ref 22). I have the claim but not the primary, and the exact cut-off and its zone dependence now
govern the agent list. I can chase the citation myself next round; flagging it in case it is closed.

**3. Brighton, Ray, Soble & Kuettner 1969 — the full PDF**, if it is ever reachable. **Downgraded to
optional**: I have the three headline results with numbers. What the full text would add is the shape of
the dose-response between 5% and 21% and above, which would tell me whether the `a − b` knob is linear or
has a threshold. Useful, not blocking.

**4. Schaffzin & Brighton, *Surg Forum* 1969;20:465–7 — "The site of action of oxygen toxicity during in
vitro epiphyseal plate growth" (PMID 5383117),** and **Brighton & Schaffzin, *Calcif Tissue Res*
1970;6(2):151–61 (PMID 4100477, DOI `10.1007/BF02196194`)** — the companion pair on what high oxygen
actually damages. Both closed (the Springer one checked: `is_oa:false`). These matter only if we intend
to run the oxygen knob near its ceiling.

**Experiments still unrun, unchanged in rank:**
- pool count at 1, 2, 6 months after a Hedgehog pulse
- a second pulse
- **does raising `a − b` by pO₂ preserve the stem pool in a plate that has one** — Leijten used fetal
  explants with no influx, so the reserve-zone expansion he saw has never been checked for stem-cell
  number
- glucose and lactate gradients across a plate — never measured, any species
