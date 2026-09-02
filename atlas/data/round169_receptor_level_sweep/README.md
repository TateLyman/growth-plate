# Round 169 — the receptor-level oestrogen sweep

**Task, in the user's words:** *"we gotta go back to receptor level. you haven't checked every compound
every niche possible thing."*

**Verdict: add nothing. The arm closes — on a class mechanism plus a human trial, not on absence of data.**

---

## The spec the compound had to meet

Delay vascular invasion → fusion, while **not**: lowering IGF-1 (GH arm), inhibiting CYP2C9/3A4
(erdafitinib arm), being redundant with anastrozole, killing resting-zone chondrocytes, or suppressing
proliferation.

## What was searched

| class | members checked | growth-plate / longitudinal-growth studies found |
|---|---|---|
| pure antagonist / SERD (injectable) | fulvestrant = **ICI 182,780** | **4** — sibonga1998, gunther1999, turner2000, movrareskrtic2014 |
| oral SERDs | elacestrant, giredestrant, camizestrant, imlunestrant, amcenestrant, palazestrant | **0** |
| PROTAC degrader | vepdegestrant (ARV-471) | **0** |
| CERAN / SERCA | palazestrant, H3B-6545 / borestrant | **0** |
| further SERMs | toremifene, bazedoxifene, lasofoxifene, ospemifene, arzoxifene, droloxifene | **0** |
| ERα/ERβ tool antagonists | MPP, PHTPP | **0** at the plate |
| human genetics | ESR1 nulls | 5 subjects / 4 families |

Search routes used: Europe PMC title and **abstract** field queries, DailyMed SPL (Faslodex setid
`83d7a440-e904-4e36-afb5-cb02b1c919f7`, v43, 16 Feb 2026), Europe PMC full-text XML for `PMC3488024`.

## The three things that decided it

**1 — In wild-type animals a pure antagonist does nothing to longitudinal growth. Three times.**
`sibonga1998` (rat, female, growing; **complete uterine antagonism in the same animals** proves
engagement; no effect on tibial longitudinal growth rate) · `turner2000` (rat, **male**; no effect on
endochondral or intramembranous growth, while **orchiectomy in the same experiment did** reduce growth) ·
`movrareskrtic2014` (mouse, OVX; **no effect in wild-type** on growth plate height). The only positive,
`gunther1999`, is a **rescue** of exogenous-oestradiol-accelerated maturation back to control.

**2 — The mechanism that explains all three, and generalises.** `movrareskrtic2014`: ICI acts at the plate
**only once AF-2 is disabled**, and then as an *inverse agonist* — from which the authors infer plate ERα
is **constitutively active without ligand**. `brjesson2012` (already in the atlas, and **wrongly indexed —
see CORR-180**): closure runs on ERα functions that **do not require AF-1**, and **AF-1 opposes closure**.
Every drug in this class is an **AF-2 agent**. They are aimed at a function that does not need AF-2.

**3 — The human trial exists, and its height endpoint is null.** `sims2012` / NCT00278915 — 30 girls, mean
age 5.9 y, McCune-Albright, **fulvestrant 4 mg/kg IM monthly × 12 months**, prospective, multicentre, and
carried on the **FDA label**:

| endpoint | before | on treatment | statistics |
|---|---|---|---|
| bone age advancement ΔBA/ΔCA | 1.99 | **1.06** | mean change −0.93, 95% CI −1.43 to −0.43, **p = 0.0007** |
| growth velocity Z-score | +2.35 | — | mean change **−1.14**, 95% CI −2.67 to 0.38, p = 0.135 |
| **predicted adult height** | 163.0 ± 6.9 cm | **163.5 ± 6.3 cm** | FDA: *no clinically meaningful change* |
| vaginal bleeding | 12.0 d/y | 1.0 d/y | median change −3.6, p = 0.0146 |

No serious treatment-related adverse events. Uterine and ovarian volumes unchanged — the clean proof of
**no partial agonism**, which is exactly what tamoxifen and raloxifene failed.

**The clock slowed and the growth slowed with it.** Same shape as `gunther1999`: cancel a pathological
excess, return to baseline, gain nothing beyond it.

## Two further findings that matter

**The compartment was wrong.** `brjesson2010` — cartilage-specific ERα-null mice grew **normally** through
sexual maturation; the tall phenotype of *total* ERα loss ran through the **GH/IGF-1 axis**. Plate ERα
mattered only for the high-dose-E2 response and in elderly mice. A plate-directed antioestrogen aims at a
compartment that is not carrying the pubertal effect — while systemic ligand removal (anastrozole) acts on
the one that is.

**Fulvestrant is the one compound that stacks cleanly, and it does not matter.** FDA label: **no known
drug-drug interactions**; no significant inhibition of CYP1A2/2C9/2C19/2D6/3A4 in vitro; no CYP3A4
inhibition against midazolam in vivo; PK unchanged by rifampin and ketoconazole. That is the *exact*
objection that disqualified resveratrol (erdafitinib is 39% CYP2C9 + 20% CYP3A4), and fulvestrant clears
it. On the GH arm the direction is favourable rather than hostile — oestrogen *suppresses* hepatic IGF-I
(`gibney2005`, `wolthers2001`) — though no one has ever measured IGF-I under fulvestrant. **The compound
that stacks cleanly is the compound with a null height endpoint.**

## The price, recorded although risk is out of scope for this case

`smith2008` — spine aBMD 0.745 → 0.684 g/cm², **Z −3.85**, cortex 641 µm, trabecular volume 10.6%, **while
bone age still advanced** 15 → 17.5 y. `feigerlova2025` — lumbar Z **−3.9 → −5.6**, femoral neck −1.8 →
−4.4, **unresponsive to ethinyl-oestradiol and to tamoxifen**, alongside growth continuing to +3 SD at
28.6 y. FDA label: paediatric bone mineral density under fulvestrant **has not been studied**.

## What is genuinely left open (2 gaps, neither a lever)

- `g_l12_does_fulvestrant_degrade_eralpha_in_growth_plate_chondrocytes` — **nobody has ever measured ERα
  protein in growth-plate cartilage under fulvestrant.** Uterus degraded + plate intact ⇒ the class failed
  on *delivery* and the arm reopens as a formulation problem. Both degraded + no growth change ⇒ closed
  permanently.
- `g_l12_final_height_of_the_sims2012_extension_cohort` — **24 of 29 girls entered an extension with
  yearly data collection in 2012 and nothing has ever been published.** Those girls have now reached adult
  height. It is the only existing route to a final-height endpoint for a pure ER antagonist in humans, and
  it is a retrieval, not an experiment.

## Files

- `sims2012_fulltext.xml` — Europe PMC full-text XML, PMC3488024, CC-BY open access. Retrieved 2026-08-09.

## Corrections raised this round

- **CORR-180** — `brjesson2012`'s bibliography one-line finding stated the **opposite** of the paper's
  conclusion. Confined to the index string; the node had it right.
- **CORR-181** — my own working claim that no pure antagonist or SERD had ever been tested at a growth
  plate was **false**. Cause: searched marketed names in titles; this literature uses the research code
  `ICI 182,780` in abstracts. Second instance of the CORR-171 failure mode.
