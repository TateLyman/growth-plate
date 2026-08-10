# Round 197 — the gain-of-function arms, and the shape

## Supplied

| file | what it is | what it gave |
|---|---|---|
| `correa2010.pdf` | Correa et al., *Dev Cell* 2010 — Zfp521 as PTHrP target/effector | **The only dataset in the whole PTH1R line reporting cells per column and terminal cell height separately** (Hunziker stereology) |
| `wezeman2003.pdf` | Wezeman et al., *Alcohol* 2003 — vertebral body height in growing rats | The vertebral-height method, normative values, **and the size of the nutrition artefact** |
| `koh2022.pdf` | the Osteoporos Int paper whose full text I had already pulled from EPMC in round 196 | figures for the six length nulls |

## Found by hunting (not supplied)

- **`weir1996`** (PMID 8816783) — Col2-driven PTHrP overexpression → **short-limbed dwarfism**. The mouse gain-of-function arm that was missing.
- **`toromanoff1998`** (PMID 9514214) — traced from `schmitt2000`'s reference 17. The lone healthy-animal femoral-length positive: 10-week-old **female** rats, 50 µg/kg/d × 15 d. Systemic **IGF-I fell**.
- **`klaus1994`** (PMID 7523093) — `schmitt2000`'s reference 16, the "biphasic" citation. The abstract never says biphasic, and **hPTH(28-48) — which cannot activate PTH1R — matched PTH(1-34)**.
- **GSE288028** — `chu2026`'s deposited data. Checked and rejected as a route to the decisive question (see below).

## The shape

`atlas/tools/pth1r_inverted_u.py` → `inverted_u_output.txt`

Bone length falls at **both** extremes of PTHrP–PTH1R tone:

| tone | evidence | length |
|---|---|---|
| zero | Blomstrand, PTHrP null, chondrocyte PTH1R KO | short / lethal |
| low | Zfp521 cKO, human PTHLH haploinsufficiency | short |
| low → normal | uraemia + PTH(1-37); achondroplasia + PTH | **rescued** |
| **optimum** | **wild type** | **reference** |
| above | agonist in WT mouse pup, male rat, rat to terminal, randomised children | **no change** |
| high | Col2-PTHrP overexpression (mouse) | short-limbed dwarfism |
| maximal | Jansen (human) | severe short stature |

An agonist can only add length **from below the optimum** — which is exactly where the two rescues sit and exactly where a healthy subject does not.

## The sampling ceiling — why the decisive gap cannot be closed with existing data

Every molecular dataset of the human growth plate in existence comes from **one surgical route**: percutaneous epiphysiodesis at Karolinska for constitutional tall stature or leg-length discrepancy.

- `chu2026` — 10 participants, **11–14 y, Tanner B/G2–B/G4**, GSE288028
- `avijgan2026` — **12 y 2 mo – 14 y 6 mo, Tanner 2–4** (its Table 1)
- `kindblom2002` — 10 patients, Greulich-Pyle bone ages topping out near 14 y

That operation is only performed **while there is growth left to stop**. The tissue at bone age 16 has never been sampled and cannot be obtained by the route that produced every existing sample. Re-analysing GSE288028 would not answer the question even if run perfectly — the data do not reach the stage in question. The gap's discriminating experiment has been rewritten around archived pathology, within-range proxies, and a fusing-species surrogate.

## Access barrier (genuine)

`toromanoff1998` — *Bone* 22:217–223, DOI 10.1016/s8756-3282(97)00271-8. Unpaywall: **not OA anywhere**; no PMC record. Its **body-weight table** is the single most valuable unread number in the line, because it is the one healthy-animal femoral-length positive and round 195 showed every other positive rides on body weight.
