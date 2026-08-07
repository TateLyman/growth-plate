# Round 28 — clearing the two held-but-unread papers, and the lui2018 fold-changes

Three things were outstanding: `glasson2005` and `williams2001`, both flagged by the new
`held_but_unread` validator check (PDF on disk, still typed `primary_abstract_only`, cited by nodes);
and `lui2018`'s transcriptomic fold-changes, which `senescence_rate_is_a_regulated_variable` explicitly
recorded as missing. All three are cleared. **Each one turned out to contain a correction, not just a
gap-fill.**

## 1. `williams2001` — a sheep node built on a cattle paper

The node `ovine_growth_plate_model` said physeal tensile properties were characterised *"in ovine
tissue"*, cited `williams2001` as its anchor primary, and used it as the `source_ref` for the node's
translation-risk score.

**The paper contains no sheep.** It is bovine — 12–18-month heifers and 5-month calves, proximal tibia
— plus eight human capital femoral specimens from two cerebral palsy patients.

**And the zonal claim was independently wrong.** The node read *"ovine PHZ: tensile failure occurs
preferentially near the hypertrophic zone."* The paper reports failure through the **zone of columnation
just below the resting zone**, sometimes deviating *into* the reserve zone — the opposite end of the
plate. Getting the species right would not have caught this; they were two separate errors.

Both corrected; `williams2001` removed as a key ref there, `stokes2006` (genuinely ovine in part) put in
its place. Logged as **CORR-036**.

### What reading it recovered

| finding | value |
|---|---|
| thickness–strength regression | ultimate stress (MPa) = **3.2 − 2.8 × thickness (mm)**, R² 0.55, P < 0.0001 — thicker plates are *weaker* |
| human physis, absolute | stress **0.98 ± 0.29 MPa**, modulus **4.16 ± 1.22 MPa**, strain **31 ± 7 %**, thickness **1.35 ± 0.33 mm** |
| **human reserve zone proportion** | **60–80 % of plate thickness**, against ~30 % in bovine |
| age effect (bovine) | older plate 25 % thinner, 34 % stronger, 65 % greater failure strain |

The atlas had recorded *"absolute values not in abstract"* for the human numbers — they were in a PDF on
disk.

**The reserve-zone proportion is the one that reaches beyond L5.** If the human resting zone really is
60–80 % of the plate against ~30 % in cattle, the compartment this whole project treats as the limiting
resource is proportionally far larger in humans than in the animals the depletion literature is built
on. It is recorded as a flag for a question, not a norm: two cerebral palsy patients aged 8 and 14, the
capital femoral physis specifically, abnormal loading, a range with no per-specimen values.

**A fourth correction:** the atlas carried "+33 % lateral vs medial" strength from the abstract. The
Results give 30 % for that comparison at **P = 0.08 — not significant**. The significant contrast is
lateral vs *centre*, 40 %, P = 0.02.

## 2. `glasson2005` — the abstract says the opposite of the growth-plate result

The abstract is entirely about ADAMTS5 and osteoarthritis. The growth-plate finding is in the body:

> G1-TEGE373 stained strongly in wild-type growth plate, was **negligible in ADAMTS4−/−**, and in
> **ADAMTS5−/− looked like wild type**

**ADAMTS4, not ADAMTS5, does the visible aggrecan cleavage in the murine growth plate.** The atlas had
inherited the joint hierarchy and applied it to the plate — recording the inverse.

**It sharpens the node's own stated hole rather than filling it.** ADAMTS4−/− abolishes the neoepitope
and the bones still reach normal length with normal plate histology; `majumdar2007`'s double null is
normal too. So the cleavage that can be *seen* is **dispensable** — either aggrecan is cleared by a route
generating no TEGE373, or its clearance is not rate-limiting for elongation.

Also recovered: the Adamts5 **heterozygote is protected** (gene-dosage effect, not in the abstract);
summed scores < 50 % of wild type, P < 0.05.

**Not cleared:** an unread erratum stands against this paper. Europe PMC confirms an Erratum linked to
PMID 15800624 but returns neither identifier nor title, so it could not be retrieved. `correction_checked`
stays `false`, and every number taken from the paper carries that caveat on the node.

## 3. `lui2018` fold-changes — the signature is real, and the atlas mixed two axes

S3, S5 and S6 Tables downloaded (CC-BY). **Nine of the twelve signature genes are confirmed on the
bone axis, FDR-corrected and replicated in both mouse and rat** — much stronger than the
directions-only version implied:

| | log2 FC (mouse / rat), positive = phalanx-high |
|---|---|
| **phalanx-high** | Igfbp4 +1.47/+2.77 · Igfbp5 +1.73/+2.81 · Wif1 +2.08/+3.12 (PZ), +1.28/+3.19 (HZ) · Dkk3 +2.51/+1.66 · Bmp3 +1.62/+2.22 · Bmper +1.82/+2.10 |
| **tibia-high** | Wnt4 −1.32/−1.34 · Bmp6 −2.36/−1.74 · Wnt5b −1.49/−1.90 |

Sign convention verified independently two ways: Pitx1 (hindlimb determinant) is −7.23, and my own mean
of the per-sample counts for Igfbp4 gives +1.69 against the table's +1.47.

**Three of the twelve were not bone-axis genes at all.** `Igfbp7` (+1.15/+1.96) and `Wnt5a`
(−1.79/−2.01) belong to the **age** axis (S3 Table, 1wk vs 4wk tibia). And **`Igf2` is on neither
list** — in the paper's own per-sample counts it is 17.66 in 1-week phalanx PZ against 17.78 in 1-week
tibia, *no difference at all*, while falling to 12.5 by 4 weeks. The atlas's claim that "tibias carry
high Igf2" was wrong as a between-bone statement.

The confusion is understandable — lui2018's own thesis is that the two axes correlate — but the atlas
presented all twelve as between-bone differences and only nine are.

## 4. What the checks caught, versus what the reading caught

Three separate mechanical checks fired in one round:

- **`held_but_unread`** (added last round) surfaced both papers in the first place.
- **The duplicate-key loader** (CORR-033) caught my own edit writing `full_text_read` and `local_pdf`
  twice into `glasson2005`.
- **A new check**, added this round, makes `full_text_read`/`access_route` alongside
  `type: primary_abstract_only` a validator **error** — a record contradicting itself.

That third one exists because `glasson2005` was in exactly that state: `full_text_read: '2026-08-06'`,
`access_route: user-supplied full-text PDF`, and `type: primary_abstract_only`, all at once, while a
node cited it. **This corrects CORR-035's own proposed fix** — that entry said `full_text_read` should
be "set only when extraction happens" and implied the atlas was gaining the field. It already existed on
53 records, and on this one it had already failed the same way `has_full_text` did. A date stamp records
that someone believed they read something; it does not record that anything was extracted.

**The reading caught the science; the checks caught the bookkeeping; neither would have caught the
other's.** No validator would ever have noticed that ADAMTS4 is the growth-plate aggrecanase, or that a
sheep node was built on cattle. Equally, reading carefully would not have caught a key written twice.

## State

Validator: 641 nodes, 1239 edges, 318 gaps, 1142 refs — **0 errors, 0 warnings.** The `held_but_unread`
backlog is empty.
