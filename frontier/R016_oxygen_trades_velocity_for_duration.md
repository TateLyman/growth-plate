# F-R016 — Oxygen trades velocity against duration, and R015 was half right

## 0. On the retrieval request

I won't route around paywalls — no Sci-Hub, LibGen, credential sharing, or scraping past access
controls. That is the one thing I'm not going to do, and it isn't a judgement about you or the goal.

What I did instead was work every legitimate channel systematically, and it produced more than the
paywalled PDFs would have. **Two of the four targets are now recovered in substance, one is located
precisely enough for you to request it, and a paper nobody in this branch had seen falsifies the
central claim of F-R015.** That last one is worth more than the PDFs.

---

## 1. Retrieval report

Built `frontier/screens/brighton_recovery/cite_harvest.py` — resolves each Brighton paper in OpenAlex,
enumerates every work citing it, pulls full text for the open-access ones (Europe PMC XML → OA PDF →
landing page), and regex-scans for quantitative restatements. Across the five seed papers:
**79 + 243 + 16 + 20 + 14 = 372 citing works, 71 open access, 13 quantitative restatements captured.**

| target | outcome |
|---|---|
| `brighton1969` in vitro O₂ tensions | **abstract recovered** (F-R015), full text not obtained |
| `brighton1971` zone map, PMID 5580029 | **numbers already held** — Table I of the A-V fistula paper *is* the control-side zone map |
| `brighton1972` A-V fistula, PMID 5133323 | **read in full** (F-R014, from your scans) |
| **`brighton1983` glycerol phosphate shuttle** | **✅ RECOVERED IN FULL SUBSTANCE — §2** |
| `brighton1980` diffusion in zones | not recovered. 20 citations, **1 open access**, no restatement. Correct citation is **Stambough & Brighton, JBJS 1980;62A:740** |
| **Brighton's thesis** | **✅ LOCATED PRECISELY — §3** |

Channels that failed, recorded so nobody repeats them: journals.lww **HTTP 402**; ovid **402**;
PubMed via fetch **cookie wall**; CORE **429**; HathiTrust full-text API **403**; OATD **403**;
Internet Archive full-text search **502 through the proxy**; bioRxiv **429 on every path and every
user-agent**; figshare landing page **403**. Internet Archive's serials collection has **only the
1969 JBJS Vol 51-A *index*, not the issues**, and **no Surgical Forum volumes at all**.

One correction to the record: **`brighton1983` is PMID 6406512**, not the PMID I fetched last round.

---

## 2. Recovered — `brighton1983`, and it is a structural proof

**Brighton CT et al., *Absence of the glycerol phosphate shuttle in the various zones of the growth
plate*, J Bone Joint Surg Am 1983;65(8):1134–1143, PMID 6406512.**

Growth plate of the rib of six-week-old male New Zealand White rabbits, zones separated with a
**purpose-built guillotine slicing apparatus**, each zone assayed for glycerol phosphate
dehydrogenase by a fluorimetric resazurin → resorufin conversion in the presence of NAD.

> **"No glycerol phosphate dehydrogenase activity was detectable in any zone of the growth plate,
> whereas control liver slices exhibited abundant enzyme activity. Thus the glycerol phosphate
> shuttle, one pathway whereby reducing equivalents are carried or shuttled from cytoplasmic
> nicotinamide adenine dinucleotide to the intramitochondrial respiratory chain, is entirely lacking
> in growth-plate chondrocytes."**

**Not low. Absent. In every zone.**

A cell without the glycerol-phosphate shuttle cannot pass cytosolic NADH to the respiratory chain by
that route. Unless the malate–aspartate shuttle carries the whole load — which this paper did not
test, and which is the obvious next question — the plate must regenerate cytosolic NAD⁺ by reducing
pyruvate to lactate. **That is obligate glycolysis by construction, not by circumstance.** It is the
mechanical floor under Brighton's 1971 observation that *"little oxygen was consumed in the face of
active bone growth"* and under Stegen's *"glycolysis is the most important energy-producing pathway
in chondrocytes."* Giving this tissue more oxygen does not give it more ATP, because the machinery
that would convert the offer is not installed.

---

## 3. Located — the thesis, and exactly how to get it

The OpenAlex/Unpaywall "green OA full text" for `brighton1969` resolves to a Figshare record with an
empty file list. Querying the Figshare API for its *full* metadata rather than its summary identifies
what it actually is:

- **Repository: INDIGO, the University of Illinois at Chicago institutional repository**
  (`figshare` is the platform; `group_id 24597`)
- **Public record: `https://indigo.uic.edu/articles/thesis/IN_VITRO_EPIPHYSEAL_PLATE_GROWTH_IN_VARIOUS_OXYGEN_TENSIONS_/10911983`**
- **Handle: `10027/14248`**
- **Degree Grantor: "University of Illinois at Chicago, Health Sciences Center." Degree Level: Doctoral.**
- Author: **CARL THEODORE BRIGHTON**
- And the custom field that explains everything:
  **`"File(s) available to UIC only. Log in with UIC Net ID to access:"`**

This makes sense: **Robert D. Ray**, second author on the 1969 paper, chaired orthopaedics at
Illinois. Brighton took his doctorate there and the thesis went into the university's repository.

**So the file exists, is catalogued, has a handle, and is access-restricted to UIC — not lost.** The
routes that work for a document in that state, in order of likelihood:
1. **UIC Library's document delivery / "Ask a Librarian"** — institutional repositories routinely
   supply restricted ETDs to outside researchers on request; cite handle `10027/14248`.
2. **Interlibrary loan** through any public or university library, citing the handle.
3. **ProQuest Dissertations & Theses Global**, which almost certainly carries it.

A thesis behind a 14-page paper typically runs 100+ pages with every raw table. **This is still the
highest-value document in the branch**, and it is now a request rather than a search.

---

## 4. The falsification — and it is a good one

The citation harvest surfaced a paper this branch and the atlas both lack, and it is the exact
experiment F-R015 §6 asked for:

**Leijten JCH, Moreira Teixeira LS, Landman EBM, van Blitterswijk CA, Karperien M. *Hypoxia inhibits
hypertrophic differentiation and endochondral ossification in explanted tibiae.* PLoS ONE
2012;7(11):e49896. PMID 23185479, PMC3503827.** Fetal mouse tibia explants (E17.5), cultured **21
days at 21% vs 2.5% O₂**, with growth kinetics, histology, gene expression and secreted protein.

> "Compared to hypoxia, **normoxia increased the length of the tibiae, length of the hypertrophic
> zone**, calcification of the cartilage and mRNA levels of hypertrophic differentiation-related genes
> e.g. *MMP9, MMP13, RUNX2, COL10A1* and *ALPL*. Compared to normoxia, **hypoxia increased the size of
> the cartilaginous epiphysis, length of the resting zone**, calcification of the bone and mRNA levels
> of hyaline cartilage-related genes e.g. ***ACAN, COL2A1* and *SOX9***."

> "**hypoxia retains chondrocytes in the resting zone while normoxia stimulates them to progress
> towards the hypertrophic zone.**"

Hypoxia also raised **GREM1, FRZB and DKK1** — secreted brakes on hypertrophy — at mRNA and protein
level. Normoxic tibiae showed a progressive increase in **hypertrophic zone** length; hypoxic tibiae
a progressive increase in **resting zone** length and a significantly **larger total cartilaginous
area**.

**This replicates `brighton1969` exactly — maximum cartilage growth at 21% — with modern methods,
43 years later, on a real length endpoint. And it falsifies F-R015's chain.**

### What survives and what dies

**Survives — the matrix-program half of the 8% switch.** Leijten's hypoxic explants raised **ACAN**,
COL2A1 and SOX9; the normoxic ones raised COL10A1 and MMP13. That is Li 2014's threshold
(< 8% → proteoglycan, > 8% → collagen) reproduced in growth-plate tissue with an independent design.
**F-R015 §3 stands.**

**Dies — my inference in F-R015 §4 that the proteoglycan program *drives elongation*.** It does the
opposite in this system. I reasoned: proteoglycan → fixed charge → swelling → hypertrophy →
elongation. The measurement says low O₂ **holds cells in the resting zone** and high O₂ **releases
them into hypertrophy**. I had the osmotic mechanics right and the control logic backwards.

---

## 5. The corrected model — oxygen is the velocity/duration knob

Put Leijten against `brighton1972` and the contradiction resolves into something better than either.

| system | pool | O₂ | result |
|---|---|---|---|
| **Leijten explant** — closed, 21 days, no renewal | fixed | 21% | pool **spent** into hypertrophy → **more length now** |
| | | 2.5% | pool **preserved** → longer resting zone, bigger epiphysis, **less length now** |
| **A-V fistula puppy** — open, months, renewing | renewing | ↓ every zone | **limb lengthens in 100%** |

> **Oxygen does not set how fast a growth plate grows. It sets whether the progenitor pool is being
> preserved or spent.**
> **High O₂ → differentiate now → velocity up, duration down.**
> **Low O₂ → stay resting → velocity down, duration up.**

This is the atlas's own identity — `height = Σ_plates Σ_years (velocity × duration)` — with a knob on
the trade between its two terms. And it explains every result that has been fighting in this branch:

- **In a 21-day explant with no renewal, only velocity can be observed.** Leijten and `brighton1969`
  measure the velocity arm and both find 21% wins. Neither can see duration; there isn't any.
- **In a puppy with an open plate and months to run, duration is most of the answer.** The fistula
  lowers pO₂, preserves the resting zone, and the limb ends up longer. Brighton's own paradox — *the
  in vivo plate grows 5× faster at 4–5× lower pO₂ than the in vitro plate* — is the same fact:
  in vivo the pool is being renewed, and low O₂ is what maintains the renewal.
- **`newton2019`** (F-R008): the resting zone collapses 31.7 → 15.0 in controls between P28 and P90
  while the Tsc1 mutant's *grows* 36.2 → 57.0, and the mutant keeps growing. Pool preservation is the
  whole game, and Leijten says oxygen is one of its inputs.
- **`stegen2019`**: chondrocytes made *less hypoxic* — pushed toward the spend side — with a
  collagen-program matrix and a **shorter** tibia. Spending faster is not the same as growing more.
- **CORR-203** in its sharpest form: an intervention that raises growth velocity in a closed assay may
  be *shortening* the animal.

### And the target changes accordingly

F-R015 said: hold the plate below 8% and flood it with proteoglycan substrate. That is now only half a
strategy, and on its own it is the *slow* half.

> **The two arms have opposite optima, so run them in sequence, not together.**
> **Preserve the pool at low pO₂ for as long as possible; then spend it at high pO₂.**

Nothing in this literature has ever done that deliberately. Every experiment holds oxygen constant for
its whole duration and reports whichever arm its timescale could see. **A staged protocol — hypoxic
expansion, then normoxic differentiation — is standard practice in stem-cell manufacturing and has
never been applied to a growth plate.** In the metatarsal assay it is one extra pipetting step.

---

## 6. Asks

**#1 — Brighton's thesis, now a request rather than a search.** UIC INDIGO, handle **`10027/14248`**,
record `indigo.uic.edu/articles/thesis/…/10911983`, file marked "available to UIC only." Ask UIC
Library document delivery, or any library's ILL, or ProQuest. Cite the handle.

**#2 — Stambough & Brighton, JBJS 1980;62A:740, *Diffusion in the various zones of the normal and the
rachitic growth plate*.** 20 citations, one of them open access, no restatement anywhere. This is the
transport term measured directly with a disease control, and it is the last completely dark paper in
the set. Library-only.

**#3 — PMID 5383117**, *The site of action of oxygen toxicity during in vitro epiphyseal plate
growth*, Surgical Forum 1970:465–467. Internet Archive holds **no** Surgical Forum volumes; this one
is a physical-library item.

**#4 — the experiment, restated so it can actually decide something.** Metatarsal or fetal-tibia organ
culture, three arms over 21 days: **constant 2.5%**, **constant 21%**, and **staged — 2.5% for days
0–14 then 21% for days 14–21**. Endpoints: total length, resting-zone height, hypertrophic-zone
height, ACAN/COL10A1. If §5 is right, the staged arm beats both constants on final length, and no
single-tension arm can. Leijten's group at Twente already has the rig and the assay; so does
Sävendahl's at Karolinska. **This is one email and a two-month experiment, and it is the first
question in this branch whose answer nobody can currently guess.**

**Still open:** `stegen2019` DCA+BPTES tibia length (Carmeliet); Kelly's lengthening series for the
millimetres behind "100 per cent"; `zhang2024` count matrix; the lateral thoracolumbar spine film.

---

*Rule I of this branch: before proposing a new mechanism, ask what instrument would have seen it.
F-R015's mechanism failed because the instrument that would have seen it — a 21-day explant — cannot
see duration, and I built a lifetime claim on assays that only measure velocity. The instrument that
would settle it does not exist yet, and it is one pipetting step away from one that does.*
