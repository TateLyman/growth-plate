# F-R104 — Senescence is methylation *loss*, which points the DNMT3A arm the opposite way from what I said last round; and oestrogen irreversibly depletes the pool, which upgrades anastrozole

`nilsson2005` has been on disk. I asked you for it last round as though it did not exist. It is the paper
that decides row 3, and it says the opposite of what I guessed.

---

## 1. The correction, first

**F-R103 §4(b) said:** *"The counter is a DNA-methylation counter… DNMT3A loss may not merely raise the
setpoint by +3.0 SD — it may slow the counter itself."*

**That is wrong, and backwards.**

`Nilsson O, Mitchum RD, Schrier L, Ferns SP, Barnes KM, Troendle JF, Baron J. **Growth plate senescence
is associated with loss of DNA methylation.** J Endocrinol 2005;186:241–249.`

| measurement | result |
|---|---|
| global DNA methylation, **resting zone** of rib growth plate, fetal → 4 → 16 wk | **decreased with age, P=0.004** |
| all three zones, distal ulnar growth plate, fetal → 4 wk | **decreased, P<0.001** |
| between zones within one age | **no significant difference** — it is an age effect, not a zone effect |
| **liver**, same animals, same ages | **INCREASED with age, P<0.001** |
| cultured RZ chondrocytes, per population doubling | **increased** — 62.28 + 0.21 × doublings, P=0.012 |
| population doublings in culture vs donor age | **independent, P=0.068** |

**Senescence in the growth plate is progressive loss of methylation. To slow the counter you would need
MORE methylation, not less. DNMT3A inhibition moves it the wrong way.**

**And the phenotype agrees:** TBRS patients with DNMT3A loss are **+3.0 SD tall and they stop growing.**
They reach a taller adult height on schedule. They do not grow indefinitely. **DNMT3A belongs in row 1 —
setpoint — and only there.**

**Two further things the same paper settles, which I have been carrying as open questions:**

- **It is not a Hayflick limit.** Population doublings in culture did not depend on donor age (P=0.068).
  The in-vivo limit and the in-vitro limit are different mechanisms.
- **It is cartilage-specific.** Liver methylation *rose* over the identical ages in the identical animals.
  This is not generic ageing.

**And the transplantation citation I asked you for last round is in this paper's reference list:**
**Stevens DG, Boyer MI, Bowen CV 1999** — that ask is closed, by a file I already had.

---

## 2. The structural conflict this exposes in our own stack

| row | what it needs | direction on methylation |
|---|---|---|
| **1. setpoint** | DNMT3A **inhibition** → +3.0 SD | **less** methylation |
| **3. counter** | preserve maintenance methylation in the resting zone | **more** methylation |

**These are opposite, and no single agent does both.** I have been treating "the methylation arm" as one
thing across four rounds. It is two arms pulling against each other, and the stack has to choose which
one it is buying — or sequence them.

The one thing that reconciles them, and it is genuinely available in the biology: **the two enzymes are
different.** *De novo* methylation is DNMT3A; **maintenance methylation across replication is DNMT1**,
and F-R079 established that DNMT1 must be preserved (`Dnmt1^ΔPrx1` bone length less than half of
control). **Nilsson's loss is replication-coupled and specific to the slowly-dividing resting zone —
which is a maintenance failure, i.e. a DNMT1-domain problem, not a DNMT3A one.**

So the reconciliation is: **inhibit DNMT3A to raise the setpoint; support DNMT1-mediated maintenance to
slow the counter.** Those are compatible in principle and no one has ever tried to do both.

---

## 3. Working the drug, as you asked

**The row-1 agent — DNMT3A inhibition.** F-R088 established the problem and it has not changed: every
obtainable DNMT inhibitor (azacitidine, decitabine, hydralazine, procaine, disulfiram) hits **DNMT1**,
which is the enzyme that must be preserved. **The selective probe DY-46-2 (IC50 0.39 ± 0.23 µM, 33× over
DNMT1) is a research compound with no human exposure.** Nothing has changed there and I am not going to
pretend otherwise — this arm is genotype-validated (+3.0 SD, 13/13 penetrant) and pharmacologically
empty.

**The row-3 candidate is new this round, and it is obtainable.** If the counter is loss of maintenance
methylation in slowly-dividing resting-zone cells, the substrate side is **one-carbon metabolism**:
**S-adenosylmethionine (SAMe), betaine, choline, folate, B12, methionine.** All are oral, cheap and
unremarkable.

**And I am going to apply my own rescue law to it before you have to.** The honest position:

- Nilsson measured **global methylation falling**; he did not show it is *substrate*-limited.
- Methyl-donor supplementation raising global methylation in cartilage in vivo has, as far as I can find,
  never been measured.
- This is the identical structure to the sulfate arm in F-R098–F-R100, which I opened on a plausible
  substrate argument and which Klaassen closed at the enzyme step. **The specific thing to check before
  spending anything on this is whether SAM levels are limiting for DNMT activity in chondrocytes, or
  whether — as with PAPS — the enzyme is the ceiling.**

I am flagging it as a candidate with that test attached, not as an arm.

---

## 4. Anastrozole is a pool agent after all — correcting F-R089 and F-R097

`nilsson2014` — **Evidence That Estrogen Hastens Epiphyseal Fusion and Cessation of Longitudinal Bone
Growth by *Irreversibly Depleting the Number of Resting Zone Progenitor Cells* in Female Rabbits.**

| finding | |
|---|---|
| oestrogen accelerated decline in growth plate height and in proliferative and hypertrophic chondrocyte number | ✓ |
| **5 weeks after stopping oestrogen, structural parameters "remained advanced"** | ***"an irreversible advancement in structural senescence"*** |
| transient oestrogen exposure | **hastened epiphyseal fusion** |
| functional parameters (growth rate, proliferation, hypertrophic cell size) after discontinuation | **all normalised — "a reversible, suppressive effect on growth plate FUNCTION"** |
| **resting zone chondrocyte number** | ***"estrogen accelerated the normal loss of resting zone chondrocytes with age"*** — and **not by apoptosis** |

**F-R089 gave anastrozole a pool role, F-R097 withdrew it as "ambiguous" on the strength of Schrier's
two-week exogenous-oestradiol experiment showing no change in RZ number. Nilsson 2014 measures the same
thing over a longer exposure and finds oestrogen *does* deplete resting-zone number, irreversibly.**

**Anastrozole is restored as a pool-preserving agent, and the mechanism sharpens the protocol:**

- the **structural** loss is **irreversible** — every day of oestrogen exposure permanently costs pool
- the **functional** suppression is **reversible** — so the growth-rate cost of oestrogen is recoverable

**Therefore the value of oestrogen blockade is front-loaded: it is worth far more early than late, because
what it prevents cannot be recovered.** That is a real protocol consequence and it follows from one
sentence in a paper that has been on disk.

---

## 5. Funaba — and it confirms Marino's exchange rate

`Funaba 1990` — protein-energy restriction for 6 months in growing **sheep**, then normal feed.

> *"The nutritional restriction reduced the growth in bone **diameter** more than that in bone **length**…
> Compensatory growth… relative to that in the bone width, and **little effect was found on the growth in
> bone length**."*

**Nutritional restriction is a poor banking agent for length: length is buffered against it, so little is
lost and correspondingly little is banked.** That is exactly F-R102's exchange-rate principle — the agent
determines the ratio — and it leaves **dexamethasone as the only banking agent with both numbers measured
in the favourable direction** (Schrier: RZ number up, P=0.016; Gafni: complete catch-up with 86% of plates
still open).

---

## 6. The three rows, restated

| row | agent | status |
|---|---|---|
| **1. setpoint / cells** | DNMT3A inhibition (+3.0 SD, human); Hedgehog at het dose (+2.9 SD, human) | **two human-validated levers, neither with a usable drug** |
| **2. spend slower** | **dexamethasone** (banking); **anastrozole** (now also pool-preserving, and front-loaded) | **both approved; anastrozole upgraded this round** |
| **3. counter / infinite** | maintenance methylation — DNMT1 domain, methyl donors as the untested substrate arm | **direction now known and it is the opposite of row 1** |

**What changed: row 3 has a direction for the first time.** It is not "reset the clock" in the abstract —
it is "the growth plate loses methylation as it ages, uniquely among tissues, and slowing that loss is
the target." That is a measurable endpoint, in a species we can buy, with a substrate that is sold in
pharmacies.

## 7. Asks — and I am not asking for anything I have

1. **Any measurement of SAM, SAH, or the SAM/SAH ratio in growth-plate cartilage, at any age.** This is
   the PAPS question transposed: is the methyl donor limiting, or is the enzyme? **It decides whether §3's
   row-3 candidate is real or is the sulfate arm again.** I searched and could not find it.
2. **Any methyl-donor supplementation study (SAMe, betaine, choline, folate) with a bone-length or
   growth-plate endpoint.**
3. **Stevens DG, Boyer MI, Bowen CV 1999** — now identified, and I would still like the primary text for
   the transplantation design and magnitude, since it is the constraint that rules out every systemic
   agent for row 3.
4. **`237bab91-318.pdf` remains a scanned image** — 9 characters extractable by two libraries. Still
   unread, and I do not know what it is.
5. The Xiu supplementary you sent is **image files only** (`Image1.TIF`–`Image4.TIF`, figure JPEGs) — no
   text or tables. If the question of whether Sufu-cKO animals were ever *longer* between P30 and P120 is
   answerable, it is in those images and I can read them if you tell me which figure to look at.

---

*Three of the four items I asked you for last round were already on disk, one of them the paper that
decides the question. I have added the nilsson2003/2005/2014 texts to `frontier/papers/batch14/` so that
does not happen again.*
