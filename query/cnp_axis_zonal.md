# Zonal expression, human growth plate (GSE288028)

Donors 1 and 2 only. **donor3 dropped** - COL10A1 83-98% in every zone, so its zone labels are
untrustworthy (same exclusion the existing zone_enrich.py makes). **donor4 dropped** - no
proliferative-zone column exists for it. Values are % of cells in that zone with a non-zero count.

| gene | stem/RZ | prolif | prehyp | hypertrophic | peak zone |
|---|---|---|---|---|---|
| PDE3A | 20.3 | 38.6 | 21.6 | 9.2 | **proliferative** |
| PDE3B | 21.7 | 31.4 | 19.8 | 23.9 | **proliferative** |
| PDE5A | 17.8 | 15.1 | 15.0 | 12.9 | **2_stem** |
| PDE10A | 22.3 | 35.7 | 18.7 | 7.7 | **proliferative** |
| NPPC | - | - | - | - | NOT IN TABLE |
| NPR2 | 4.2 | 4.4 | 2.8 | 2.8 | **proliferative** |
| NPR3 | 1.1 | 0.5 | 0.3 | 0.5 | **2_stem** |
| MME | 9.5 | 2.8 | 4.9 | 6.7 | **2_stem** |
| PRKG2 | 8.0 | 26.5 | 12.4 | 6.9 | **proliferative** |
| KCNMA1 | 30.7 | 45.0 | 35.4 | 19.2 | **proliferative** |
| TRPM7 | 54.7 | 60.5 | 57.5 | 48.1 | **proliferative** |
| CREB1 | 38.7 | 47.5 | 45.2 | 37.2 | **proliferative** |
