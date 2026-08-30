# F-R114: every candidate arm in the file, and what happened when the pathway was pushed
# in the correct direction in an animal, with bone length measured.
ROWS=[
 ("Hedgehog, PARTIAL/het dose","PTCH1 +/- human; SAG bead in SOC","TALLER (+0.8 to +3.8 SD human); femur/tibia/leg longer at 1,2,6 months","SURVIVES"),
 ("Hedgehog, FULL/sustained","Sufu-cKO (Xiu); Ptch1 full loss","SHORTER (-3.7 mm at P120); Gorlin","fails at full dose"),
 ("oestrogen blockade (deadline)","aromatase / ERa deficiency human","TALLER, 204 cm, epiphyses open at 28","SURVIVES"),
 ("proteoglycan sulfation","PAPSS2 / SLC26A2 / CHSY1 loss","SHORTER (brachyolmia, diastrophic dysplasia)","LOF only; no GOF exists"),
 ("DNA methylation (DNMT1)","Dnmt1 dPrx1","SHORTER (<half length)","LOF only"),
 ("chromatin de-repression","Ezh1-/-;Col2-Cre Ezh2 fl/fl","SHORTER - 'EZH1/2 PROMOTE skeletal growth' (Nat Commun 2016)","FAILS - and it raised the imprinted network z=+7.5"),
 ("HIF / hypoxia stabilisation","Vhl cKO in chondrocytes","SEVERE DWARFISM, reduced proliferation (Pfander 2004 Development)","FAILS - and this is what roxadustat does"),
 ("GH / IGF-1","somatropin; GSE288028 human GP","null on the length axis (r=+0.029); pool-negative","FAILS"),
 ("injury / regeneration","remote fracture, GSE3298","growth plate imprinted network unchanged (z +0.16 to -3.47)","does not reach the plate"),
 ("FGFR3 inhibition","Fgfr3-GOF is the disease; infigratinib/erdafitinib","achondroplasia rescue","RESCUE only - never above normal"),
 ("CNP / NPR2","vosoritide; NPR2 GOF human","TALLER (NPR2 activating variants -> tall stature)","SURVIVES (rescue-proven; GOF human genetics)"),
]
w=max(len(r[0]) for r in ROWS)
print('%-*s  %-42s  %s'%(w,'ARM','WHAT WAS DONE','LENGTH OUTCOME'))
print('-'*150)
for a,b,c,d in ROWS:
    print('%-*s  %-42s  %s\n%-*s  %-42s  => %s'%(w,a,b[:42],c,w,'','',d))
print('\nSURVIVING: Hedgehog at partial dose; oestrogen blockade; CNP/NPR2.')
print('EVERY OTHER CANDIDATE HAS AN EXPRESSION CORRELATE POINTING THE RIGHT WAY')
print('AND A GAIN-OF-FUNCTION EXPERIMENT POINTING THE WRONG WAY.')
