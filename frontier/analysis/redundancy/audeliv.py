"""DOES ORAL GOLD REACH SKELETAL TISSUE AT A CONCENTRATION THAT MATTERS?
Cottrill 1989, J Chem Soc Perkin Trans II: 199Au-auranofin, 2.5 mg/kg ORAL,
Wistar rats ~200 g (young, growth plates OPEN), %dose/g at 2/5/24/48/168 h."""
AF={'Blood':[0.93,1.3,1.8,0.83,0.076],'Kidney':[1.1,3.1,6.8,7.1,6.6],
    'Liver':[0.34,0.63,0.65,0.32,0.30],'Spleen':[0.28,0.58,0.99,0.69,0.53],
    'Lung':[0.38,0.60,0.92,0.51,0.21],'Joint':[0.12,0.24,0.45,0.37,0.30],
    'Bone':[0.11,0.15,0.31,0.21,0.14],'Muscle':[0.068,0.12,0.20,0.17,0.059],
    'Skin':[0.097,0.17,0.28,0.27,0.18]}
T=['2h','5h','24h','48h','168h']
print("="*94); print("TISSUE : BLOOD RATIO OVER TIME  (oral auranofin, %dose/g)"); print("="*94)
print("%-8s %8s %8s %8s %8s %8s"%("organ",*T))
print("-"*58)
for k,v in AF.items(): print("%-8s %8.3f %8.3f %8.3f %8.3f %8.3f"%(k,*v))
print()
print("%-8s %8s %8s %8s %8s %8s"%("ratio/blood",*T))
print("-"*58)
b=AF['Blood']
for k in ['Joint','Bone','Muscle','Kidney']:
    print("%-8s %8.2f %8.2f %8.2f %8.2f %8.2f"%(k,*[AF[k][i]/b[i] for i in range(5)]))
print()
print("  -> BLOOD falls 1.8 -> 0.076 (24x) between 24 h and 168 h.")
print("     JOINT falls 0.45 -> 0.30 (1.5x)  = 67%% RETAINED")
print("     BONE  falls 0.31 -> 0.14 (2.2x)  = 45%% RETAINED")
print("  => at 168 h JOINT gold is %.1fx BLOOD and BONE is %.1fx BLOOD."%(0.30/0.076,0.14/0.076))
print("     GOLD PARTITIONS INTO AND IS RETAINED BY SKELETAL TISSUE.")

print()
print("="*94); print("CONVERT TO ABSOLUTE CONCENTRATION"); print("="*94)
MW_AF,MW_AU=678.5,197.0
dose_af=2.5           # mg/kg
f_au=MW_AU/MW_AF
dose_au=dose_af*f_au  # mg Au per kg
print("  auranofin 2.5 mg/kg  ->  gold dose %.3f mg Au/kg  (Au is %.1f%% of auranofin by mass)"%(dose_au,100*f_au))
for organ in ['Joint','Bone']:
    for i,lab in [(2,'24h'),(4,'168h')]:
        pct=AF[organ][i]
        ug_per_g=pct/100.0*dose_au*1000.0        # ug Au per g tissue (per kg bw dose basis)
        uM=ug_per_g/MW_AU*1000.0                 # nmol/g == uM at density 1
        print("   %-6s %-5s : %.3f %%dose/g -> %.3f ug Au/g -> %.2f uM"%(organ,lab,pct,ug_per_g,uM))
print()
CELL=0.10
j168=AF['Joint'][4]/100.0*dose_au*1000.0/MW_AU*1000.0
print("  cellular concentration that lowered 5hmC (Chen 2023, serum present) : %.2f uM"%CELL)
print("  JOINT gold at 168 h after ONE 2.5 mg/kg oral dose                   : %.2f uM  = %.0fx"%(j168,j168/CELL))

print()
print("="*94); print("BRIDGE TO THE HUMAN DOSE"); print("="*94)
hum_mgkg=6.0/70.0
tau,thalf=1.0,35.0
acc=1/(1-2**(-tau/thalf))
print("  human RA dose 6 mg/day / 70 kg      = %.4f mg/kg/day"%hum_mgkg)
print("  t1/2 35 d, daily dosing -> accumulation ratio 1/(1-2^-(tau/t1/2)) = %.1fx"%acc)
print("  steady-state single-dose EQUIVALENT = %.4f x %.1f = %.2f mg/kg"%(hum_mgkg,acc,hum_mgkg*acc))
print("  rat single dose in Cottrill         = %.2f mg/kg"%dose_af)
print("  ratio human steady state : rat single dose = %.2fx"%(hum_mgkg*acc/dose_af))
print()
print("  -> the human steady-state exposure is the SAME ORDER as the single rat dose")
print("     that produced ~%.1f uM gold in joint tissue. Allometry not applied;"%j168)
print("     rats clear gold faster than humans, so this is if anything CONSERVATIVE.")

print()
print("="*94); print("SHARMA 1984 — SUBCELLULAR GOLD AFTER REPEATED ORAL AURANOFIN (ug Au/g fraction)"); print("="*94)
LIV={'Liver tissue':[1.78,2.89,4.49],'Nuclear':[1.04,0.90,0.95],'Mitochondrial':[1.21,1.46,1.52],
     'Lysosomal':[1.52,1.71,2.06],'Microsomal':[1.89,1.45,1.11],'Cytosol':[0.76,1.14,1.96]}
KID={'Kidney tissue':[9.04,13.54,16.55],'Nuclear':[2.09,2.33,2.46],'Mitochondrial':[1.28,1.43,1.93],
     'Lysosomal':[2.59,2.52,2.63],'Microsomal':[3.90,2.28,1.77],'Cytosol':[2.93,4.85,6.06]}
MW=197.0
for nm,D in [('LIVER',LIV),('KIDNEY',KID)]:
    print("\n%s   auranofin 5 / 10 / 15 mg/kg/day x3"%nm)
    print("  %-16s %8s %8s %8s   | as uM (density 1)"%("fraction","5","10","15"))
    for k,v in D.items():
        print("  %-16s %8.2f %8.2f %8.2f   | %5.1f %5.1f %5.1f"%(k,*v,*[x/MW*1000 for x in v]))
print()
print("  >>> NUCLEAR GOLD, THE COMPARTMENT WHERE TET1 LIVES:")
print("      liver  %.2f-%.2f ug/g = %.1f-%.1f uM"%(min(LIV['Nuclear']),max(LIV['Nuclear']),
      min(LIV['Nuclear'])/MW*1000,max(LIV['Nuclear'])/MW*1000))
print("      kidney %.2f-%.2f ug/g = %.1f-%.1f uM"%(min(KID['Nuclear']),max(KID['Nuclear']),
      min(KID['Nuclear'])/MW*1000,max(KID['Nuclear'])/MW*1000))
print("      vs the cellular 5hmC-active concentration of 0.10 uM  ->  %.0f-%.0fx"
      %(min(LIV['Nuclear'])/MW*1000/0.1, max(KID['Nuclear'])/MW*1000/0.1))
print()
print("  >>> AND THE NUCLEAR COMPARTMENT IS SATURABLE:")
for nm,D in [('liver',LIV),('kidney',KID)]:
    t=list(D.values())[0]; n=D['Nuclear']
    print("      %-6s: 3x dose raises TOTAL tissue %.2f -> %.2f (%.1fx) but NUCLEAR %.2f -> %.2f (%.2fx)"
          %(nm,t[0],t[2],t[2]/t[0],n[0],n[2],n[2]/n[0]))
print()
print("      => a 3x dose increase changes nuclear gold by 0-18%. THE NUCLEUS IS BUFFERED.")
print("         For an agent that must NOT exceed ~50% target engagement, that is a")
print("         SECOND independent self-limiting mechanism alongside 2-OG competition.")
