# F-R107 — The answer on methylation: no to raising writers, yes to removing erasers. And row 3's direction as I stated it was wrong.

You asked me to settle whether raising methylation is right for the stack before anything gets added.
**It is not, and I can now show why from three independent lines — two of them analyses I ran on data
already held. This also corrects the direction I gave you in F-R104 and F-R105.**

---

## 1. The resting zone is a DNMT3A compartment, not a DNMT1 compartment

I had been reasoning about "the growth plate." The relevant compartment is the **resting zone**, where
the stem cells are and where Nilsson measured the methylation loss. GSE16981 has all three zones at
1 week. Mean expression:

| gene | **resting zone** | proliferative zone | hypertrophic | RZ / PZ |
|---|---|---|---|---|
| **Dnmt3a** | **3260.8** | 1862.8 | 2079.1 | **1.75×** |
| Dnmt1 | **365.9** | 563.8 | 259.6 | **0.65×** |
| Dnmt3b | 99.2 | 94.8 | 24.1 | 1.05× |
| Uhrf1 | **252.3** | 356.5 | 225.0 | **0.71×** |
| Pcna | **2508.9** | 4059.2 | 2181.6 | **0.62×** |
| **Tet1** | **865.5** | 631.3 | 145.1 | **1.37×** |
| **Tet2** | **1442.7** | 858.7 | 644.2 | **1.68×** |
| *Sfrp5 (RZ identity check)* | *4243.1* | *276.4* | *80.9* | *15.4×* |
| *Pthlh (RZ identity check)* | *1012.0* | *222.7* | *83.2* | *4.5×* |

**In the resting zone there is 8.9× more *Dnmt3a* transcript than *Dnmt1*.** The maintenance machinery —
DNMT1, UHRF1, PCNA — is **lower** in the resting zone than in the proliferative zone, which is exactly
what you expect of replication-coupled proteins in a slowly-dividing cell. **That is not a defect. It is
the design.**

**And the erasers are enriched where the loss happens:** TET1 1.37× and TET2 1.68× above the
proliferative zone.

## 2. The maintenance machinery does not fail with senescence

Correlating against log age in the proliferative-zone time course (3→12 wk, castrated):

| gene | r vs age |
|---|---|
| **Dnmt1** | **+0.200 — does not fall** |
| Uhrf1 | +0.312 — does not fall |
| **Pcna** | **+0.709 — rises** |
| Mecp2 | +0.599 |
| **Dnmt3a** | **−0.628 — this is the writer that falls** |
| Tet1 / Tet2 / Tdg | +0.543 / +0.388 / +0.401 |
| Dnmt3b | +0.219 |

**There is no maintenance-machinery failure to correct.** DNMT1, UHRF1 and PCNA are flat-to-rising as the
plate senesces. **The writer that declines is DNMT3A** — the one whose loss makes humans **+3.0 SD
taller**.

*(Limitation, stated: the time course is proliferative zone only; the resting-zone samples are all
1-week, so I cannot test the age trajectory in the RZ itself. And mRNA is not protein or activity —
DNMT1 in particular is regulated by acetylation, which the pirfenidone paper measured and this array
cannot.)*

## 3. The human genetics of all three writers, and only one sets height

| gene | human condition | stature |
|---|---|---|
| **DNMT3A** loss (het) | Tatton-Brown-Rahman | **TALL, +3.0 SD, 13/13 penetrant** |
| **DNMT3A** gain (PWWP) | Heyn 2019 | **microcephalic dwarfism** |
| **DNMT3B** loss (biallelic) | ICF syndrome type 1 | **growth delay, failure to thrive — short** |
| **DNMT1** (het missense) | HSAN1E / ADCA-DN | **no stature phenotype** — hearing loss, sensory neuropathy, cognitive decline, ataxia, narcolepsy |

**DNMT3A is bidirectional and it is the height gene: less methylation, taller; more, dwarfed. DNMT1
heterozygous mutation in humans produces no height phenotype at all.**

---

## 4. Therefore: pirfenidone is wrong for this stack, on the data rather than on the caution

F-R106 held it out on hypothesis-level grounds. **This is a stronger and more specific reason.**

Pirfenidone raises **DNMT1, UHRF1, PCNA and DNMT3a**. In the compartment that matters:

- **DNMT3a is the dominant writer (8.9× DNMT1) and raising it moves our single largest human height lever
  backwards.** Its p-value in the pirfenidone paper (<0.0001) is *stronger* than DNMT1's (<0.001).
- **DNMT1/UHRF1/PCNA are constitutively low in the resting zone by design, do not fall with senescence,
  and human DNMT1 dose does not set height.** Raising them corrects nothing and moves a variable the
  genetics says is not height-limiting.

**Both arms of the drug are either wrong-signed or inert in the compartment we care about. It is out, and
not on a technicality.**

---

## 5. The correction to F-R104 and F-R105

**I told you the counter was a maintenance-methylation failure and that row 3 needed more DNMT1. The data
do not support that.**

- maintenance machinery does not decline (§2)
- it is not the dominant writer in the relevant compartment (§1)
- its human dose does not set height (§3)

**What the data support instead:** the methylation loss Nilsson measured in the resting zone happens in a
compartment that is **DNMT3A-dominant and TET-enriched**, and the writer that declines with age is
DNMT3A. **So global methylation loss is plausibly a *consequence* of the normal growth programme —
DNMT3A falling, TETs present — rather than a failure that ends it.**

**And if that is right, then "methylation falls as the plate senesces" is a correlate of growth, not its
brake — which means row 3 as I framed it in F-R104 does not exist as stated.** I am not going to keep
building on a direction I cannot support.

---

## 6. What survives, and it is asymmetric

**The writers: leave them alone. The erasers: stop feeding them.**

TET1 and TET2 are **enriched in the resting zone** (1.37× and 1.68×) — positioned exactly where the
methylation loss occurs — and they are **Fe(II)/2-oxoglutarate dioxygenases requiring ascorbate**.

| agent | in our stack | action |
|---|---|---|
| **calcium α-ketoglutarate** | demoted F-R087, not removed | **REMOVE.** 2KG is the obligate TET co-substrate; Yanagihara names it in that role and it rises when DNMT1 is lost |
| **ascorbate** | retained F-R087, ~500 mg/day | **reduce to the minimum for prolyl hydroxylation.** It is a TET cofactor; supplementing above requirement buys collagen at the cost of the mark |
| DNMT3A inhibition | row 1 | **unchanged — still the largest lever, still no usable drug** |
| pirfenidone | proposed | **not added** (§4) |

**Both surviving actions are subtractions from our own stack, both are free, and both are correctly
signed on the data above.** That is the entire methylation arm.

---

## 7. What would reopen it — and what I would need

**One measurement decides whether §5 is right:** *does TET activity, or 5hmC, rise in the resting zone
with age?* If yes, the loss is active demethylation, the eraser-subtraction is the right move, and there
may be room for a TET inhibitor. If no, the loss is passive and nothing in this arm matters.

**Asks — and these are the only three:**

1. **Any 5hmC measurement in growth-plate cartilage at more than one age.** Nilsson measured 5mC only.
   5hmC is the direct footprint of TET activity and it would settle §5 in one figure.
2. **Any resting-zone-specific expression time course** — GSE16981's RZ samples are all 1-week, so the
   age trajectory in the compartment that matters is unmeasured. If a dataset exists with RZ at multiple
   ages, it tests §2 in the right zone.
3. **Stevens, Boyer & Bowen 1999** — still outstanding, still the constraint that rules out systemic
   agents for row 3.

*(Searched and not found: any 5hmC growth-plate data; any TET manipulation with a bone-length endpoint;
any RZ multi-age transcriptome.)*

---

*The honest summary: I gave you a direction two rounds ago that the data I already had does not support.
The methylation arm is not an addition — it is two removals, and the largest methylation lever in the
file is still DNMT3A inhibition, which we cannot buy.*
