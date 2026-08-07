# Round 34 — the unbiased head-to-head, and the arithmetic on cycling

## The comparison that settles it, and it splits

The cleanest unbiased test is lifelong perturbation of each axis, in humans, to adult height.

| | genotype | adult height |
|---|---|---|
| **FGFR3 partial loss** (CATSHL, p.R621H, 27 affected) | lifelong | **males 195.6 cm (~+2.8 SD)**, 5/5 >97th centile; females 177.8 cm (~+2.3 SD) |
| **NPR2 activating** | lifelong | **221 cm (+5.2 SD)** — *after epiphysiodesis* |
| **NPR3 biallelic loss** | lifelong | **211.1 cm (+4.9 SD)** — *after epiphysiodesis* |

**Pushed for a lifetime, the CNP axis delivers roughly two more standard deviations of adult height than
partial FGFR3 loss — and the CNP numbers are floors, because both individuals were surgically stopped.**

But pushed acutely, FGFR inhibition wins by a distance: **19.06 cm/yr vs 8.09.**

**That is exactly the velocity-versus-yield distinction this atlas is built on, now with matched human
genetics at both extremes: the bigger velocity lever converts to less adult height.**

### The objection, and it is strong

**CATSHL is partial, heterozygous loss.** It bounds *partial* FGFR3 inhibition, not maximal. No complete
human FGFR3 null is on record, the Fgfr3-null mouse overgrows more, and the erdafitinib case is direct
evidence that harder inhibition is achievable in a living person. So this does **not** exclude the
possibility that maximal FGFR3 blockade beats the CNP ceiling. It shows that the *genetic doses nature
supplies* do not.

Also: n=5 men vs n=1 per CNP genotype, different kindreds, and the SD conversions are my arithmetic on
assumed population parameters — flagged `value_unverified`.

## The thing I had wrong, and it removes my main argument against erdafitinib

I framed spinal deformity as the cost of the FGFR route. **It is the cost of the growth, on either axis:**

- CATSHL — **scoliosis is in the syndrome's name**
- NPR3 loss — spinal fusion at 12 for a 39° Cobb angle
- NPR2 activating — severe scoliosis with vertebral fractures
- erdafitinib — kyphoscoliosis with cord compression
- vosoritide — three slipped capital femoral epiphyses

**Every route to extreme endochondral growth produces spinal deformity — genetic and pharmacological,
CNP and FGFR alike.** So spinal morbidity **cannot be used to prefer one drug over the other.** You were
right that "scary growth" wasn't a real argument. It's the shared price of the growth, and it's what
williams2001 predicts when a plate is driven thicker.

## Verdict

**Different terms, so the answer isn't "which" — it's that nobody has combined them.**

- **CNP → h_term**, hypertrophic zone, bone-age-sparing, better lifetime conversion, capped by hypotension
- **FGFR3 → amplification + resting-zone turnover**, proliferative zone, far bigger acute velocity, capped by phosphate and by the spine

The FGFR axis also has **demonstrated dose headroom nobody uses**: infigratinib at 0.25 mg/kg gives
+1.74 cm/yr; erdafitinib at an oncology dose gives +19. **An 11-fold range within one drug class, and
the entire space between is unexplored** — oncology doses downward, achondroplasia doses cautiously
upward, and nothing has been titrated for growth in a normal plate.

## The tractability-5 dive: does cycling the pool work?

**The arithmetic nearly kills it.** `forcinito2011` measured the exchange rate directly: **four weeks of
growth inhibition delayed senescence by about two.** Charge costs four weeks of calendar, buys two weeks
of capacity — a losing trade. The clinical catch-up literature agrees: children return *toward* target,
not past it.

**One number rescues it.** The same paper establishes *why* the trade might not be straight — senescence
tracks **growth, not time**, so capacity is spent on divisions, not on the calendar. And `nilsson2005`
found rabbit resting-zone population doublings **independent of donor age**. If quiescent progenitors
don't age, a charge phase is *free storage*, and the two-weeks-per-four figure understates it — because
that experiment measured senescence markers, not banked progenitors, and `oichi2023` shows the
progenitors do bank.

**And a second number sets the condition under which it could work.** Senescence may track growth, but
**puberty tracks the calendar.** Oestrogen arrives on a hormonal schedule and closes the plate regardless
of remaining capacity — which is exactly what `herrmann2002` shows from the other side: a man whose
plates never closed because the signal never came.

> **A charge phase spends calendar against a pubertal deadline that does not pause.**

So cycling should net **positive only in a prepubertal child with years of runway**, and **negative near
puberty**. And it predicts that **cycling combined with holding the pubertal clock** — GnRH agonist or
aromatase inhibition — is the only version with a clean rationale. That combination has never been tried.

## CORR-039

Adding the CATSHL reference I **invented a DOI** (`10.1086/510020`; the real one is `10.1086/508433`) —
and added a reference **the atlas had held since 2026-08-05**. Both are repeat failures (CORR-032 on
composed identifiers, CORR-034 on checking before adding). The duplicate-key loader caught it — its
third catch, my second in two rounds. Without it the atlas would carry a wrong DOI and a `cited_by` reset
from 112 to 0, while looking clean. Fixed by merging, not replacing.

Validator: 643 nodes, 1246 edges, 321 gaps, 1144 refs — 0 errors, 0 warnings.
