# GSE9160 — the zone-resolved human growth plate array

Downloaded from GEO by this atlas on 2026-08-10 and archived here because it is the only platform that
can answer detection questions in the human growth plate (CORR-114 disqualifies droplet scRNA-seq for
low-abundance secreted and regulatory transcripts).

| file | what it is |
|---|---|
| `GSE9160_series_matrix.txt.gz` | the series matrix as downloaded, 2.2 MB. `https://ftp.ncbi.nlm.nih.gov/geo/series/GSE9nnn/GSE9160/matrix/` |
| `panel_output.txt` | output of `atlas/tools/gse9160_panel.py`, standing panel, every probe set × every donor |

**Not archived:** `GPL570.txt`, the HG-U133 Plus 2.0 annotation table (~79 MB). Fetch from
`https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPL570nnn/GPL570/annot/` and pass the containing directory
to `--dir`.

## The design

Laser-capture microdissected, zone-resolved. **Five compartments** — reserve, proliferative,
prehypertrophic, hypertrophic, perichondrium — from **two normal children**, female 11y10m and male
13y3m, distal femoral growth plate. MAS5, linear scale, trimmed mean target 100. GEO sample titles are
`"<Zone>, replicate N"`; **replicate 1 is the female donor**.

## The calibrator band, printed on every run

| gene | range across 10 samples | role |
|---|---|---|
| NPPC | **4 – 20** | the floor — a gene the plate demonstrably does not make |
| PTHLH | 7 – 309 | canonical low-abundance paracrine regulator |
| GDF5 | 31 – 604 | known essential secreted regulator |
| COL2A1 | 6,354 – 104,438 | tissue identity |

A gene inside the PTHLH/GDF5 band is **detected on a platform with no dropout**. It is not thereby
present as functional protein, and n = 2 donors is n = 2 donors.

## What this extraction settled

- **CORR-218** — KLB (β-klotho) is detected in **ten of ten samples** (`244276_at` 180–847, `235708_at`
  23–339), reversing the absence claim CORR-041 and CORR-042 took from droplet data.
- **CORR-220** — MME (neprilysin) is **donor-variable**, 18–160 in donor 1 against 200–1062 in donor 2;
  quoting its maximum overstated it.
- **Round 220** — NPPC at the floor in 10/10 confirms the plate is a CNP *consumer*; ECE1 (≤2495) and IDE
  (≤1847) out-transcribe MME (≤1062), confirming the neprilysin write-off on an admissible platform.
- **OSTN has no probe set on GPL570**, so osteocrin expression in the human growth plate is unmeasured by
  this route.
