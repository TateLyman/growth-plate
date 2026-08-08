# CNP vs MEK-inhibition top-50 overlap (hirota2018 S2-S5), computed here

list sizes: CNP-up 50, CNP-down 50, U0126-up 50, U0126-down 50

| comparison | direction | shared genes | n |
|---|---|---|---|
| CNP-up vs U0126-up | CONCORDANT | Gpx2, LOC498316 | **2** |
| CNP-down vs U0126-down | CONCORDANT | Ccl19 | **1** |
| CNP-up vs U0126-down | discordant | (none) | **0** |
| CNP-down vs U0126-up | discordant | Rhbdd1 | **1** |

**Concordant overlap total: 3 genes out of 100 pairwise slots = 3%.**
Expected by chance on a ~25,000-probe rat array: 50*50/25000 = 0.10 genes per comparison.
So 3 concordant is ~15x chance - real enrichment, consistent with the authors' GSEA p<0.001 -
but 2/50 and 1/50 at the extremes is a weak distributional shift, NOT a shared target set.

CNP-up ion-channel / Ca-handling block (the kawabe chain): Atp2b3, Camk2d, Clcn4, Cnga1, Kcnj9
plus chondrogenic/patterning: Ptch2, Sox9, Wnt8a
U0126-up character: solute carriers Slc30a10, Slc38a11, Slc6a1, Slc7a11 + metabolism/muscle
U0126-down character: angiogenic Dll4, Ephb1, Flt1, Gja4 + inflammatory C7, Ccl19, Ccl20, Ccl6, Ifi204, Il1a, Tnf
