MWm=639.82   # moxidectin
MWs=770.0    # selamectin (C43H63NO11)
def uM(ng,MW): return ng*1e-6/MW*1e6/1000.0*1000.0/1000.0   # ng/mL -> uM
def uM(ng,MW): return (ng*1e-9/1e-3)/MW*1e6                 # ng/mL -> umol/L
def ng(u,MW):  return u*1e-6*MW*1e9/1000.0                  # uM -> ng/mL
def eng(C,ic50): return 100*C/(C+ic50)

print("="*74)
print("THE CALIBRATION CONSTANT  (Lui 2023 Fig 6C/6D, isolated growth-plate chondrocytes)")
print("="*74)
print("  TOPFLASH   WT 1.00  ->  Spin4-KO 0.62      = %.0f%% reduction in Wnt output  (P=0.015)"%(100*(1-0.62)))
print("  Axin2 mRNA WT ~6.0  ->  Spin4-KO ~3.3      = %.0f%% reduction               (P=0.009)"%(100*(1-3.3/6.0)))
print("  -> SPIN4 LOSS = ~38-45%% REDUCTION IN CANONICAL WNT OUTPUT")
print("     and that produces: +5.06%% tibia, RZ progenitors up, h_term untouched")
print()
print("="*74)
print("MOXIDECTIN IC50, NOW MEASURED DIRECTLY (Melotti Fig 2B, BrdU, uM)")
print("="*74)
mox=[1.2,1.2,1.4]; sel=[0.14,0.08,0.09]; ivm=[2.3,0.8,1.0,1.7]
print("  moxidectin CC14/DLD1/Ls174T = 1.2 / 1.2 / 1.4   -> mean %.2f uM"%(sum(mox)/3))
print("  selamectin                  = 0.14/ 0.08/ 0.09  -> mean %.3f uM  (%.1fx more potent)"%(sum(sel)/3,(sum(mox)/3)/(sum(sel)/3)))
print("  ivermectin                  = 0.8-2.3                            (R139 assumed 1.5 - close)")
IC50m=sum(mox)/3; IC50s=sum(sel)/3
print()
print("  CROSS-CHECK from AXIN2 data (Fig 2D), Hill n=1:")
for name,C,frac in [("ivermectin DLD1",5.0,0.1),("ivermectin Ls174T",5.0,0.3),
                    ("selamectin DLD1",0.5,0.3),("selamectin Ls174T",0.5,0.3)]:
    print("    %-20s %0.1f uM -> AXIN2 %.2f  => implied Wnt IC50 %.3f uM"%(name,C,frac,C*frac/(1-frac)))
print("  -> AXIN2-derived Wnt IC50 agrees with BrdU IC50 within ~2x. The proxy holds.")
print()
print("="*74)
print("MOXIDECTIN ENGAGEMENT vs THE 38-45%% TARGET   (IC50 %.2f uM)"%IC50m)
print("="*74)
print("%-34s %9s %10s %14s"%("regimen","uM","% engaged","vs 40% target"))
for n,c,kind in [("3 mg Cmax",22.4,"peak"),("8 mg TABLET Cmax (APPROVED)",58.9,"peak"),
                 ("8 mg fed Cmax",78.9,"peak"),("18 mg Cmax",141.0,"peak"),
                 ("36 mg Cmax (MAX EVER DOSED)",289.0,"peak"),
                 ("8 mg fed WEEKLY  Css",29.0,"sustained"),
                 ("8 mg fed 2x/week Css",58.1,"sustained"),
                 ("36 mg fasted weekly Css",64.4,"sustained")]:
    u=uM(c,MWm); e=eng(u,IC50m)
    print("%-34s %9.4f %9.1f%% %13.1fx short"%(n+" ["+kind+"]",u,e,40.0/e))
print()
need=0.40/0.60*IC50m
print("  To reach 40%% SUSTAINED engagement with moxidectin: C = %.3f uM = %.0f ng/mL"%(need,ng(need,MWm)))
print("  -> dose/day = %.1f mg  =  %.0f mg/WEEK   ** vs a 36 mg single-dose human ceiling **"%(ng(need,MWm)*66.2/1000, ng(need,MWm)*66.2/1000*7))
print()
print("="*74)
print("SELAMECTIN-CLASS POTENCY: WHAT THE CHEMOTYPE ALREADY OFFERS  (IC50 %.3f uM)"%IC50s)
print("="*74)
needs=0.40/0.60*IC50s
print("  To reach 40%% engagement with selamectin: C = %.4f uM = %.1f ng/mL"%(needs,ng(needs,MWs)))
print("  For comparison, human moxidectin 8 mg already reaches Cmax %.1f ng/mL"%58.9)
print("  -> the REQUIRED PLASMA CONCENTRATION IS ALREADY ACHIEVED BY AN APPROVED DOSE OF A")
print("     LESS POTENT FAMILY MEMBER. The gap is POTENCY, not exposure.")
print("  potency gap moxidectin->selamectin = %.1fx ; potency NEEDED = %.1fx"%(IC50m/IC50s, (0.40/0.60*IC50m)/uM(58.9,MWm)))
