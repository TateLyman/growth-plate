MWs=770.0; MWm=639.82
def uM(ng,MW): return (ng*1e-9/1e-3)/MW*1e6
def ng(u,MW):  return u*1e-6*MW*1e9/1000.0
IC50s=0.103   # selamectin Wnt/BrdU IC50, Melotti Fig 2B mean
IC50m=1.27
TARGET=0.40
Cneed=TARGET/(1-TARGET)*IC50s
print("TARGET  = %.0f%% Wnt engagement (Spin4 loss = 38-45%%)"%(TARGET*100))
print("SELAMECTIN IC50 = %.3f uM ; concentration needed = %.4f uM = %.1f ng/mL"%(IC50s,Cneed,ng(Cneed,MWs)))
print()
print("== SELAMECTIN DOG PK (PMID 12213114) ==")
print("  oral 24 mg/kg  -> Cmax 7630 ng/mL (F=62%%) = %.2f uM = %.0fx IC50"%(uM(7630,MWs),uM(7630,MWs)/IC50s))
print("  topical 24 mg/kg -> Cmax 86.5 ng/mL (F=4.4%%) = %.4f uM = %.0f%% engaged"%(uM(86.5,MWs),100*uM(86.5,MWs)/(uM(86.5,MWs)+IC50s)))
print("  IV: Cl 1.18 mL/min/kg, Vdss 1.24 L/kg, t1/2 14 h (dog) ; cat t1/2 69 h")
print("  LINEARITY established in dogs up to 636 ng/mL -- our target %.0f ng/mL is INSIDE it"%ng(Cneed,MWs))
print()
d1=24.0*ng(Cneed,MWs)/7630.0
Cl=1.18*60*24/1000.0   # mL/min/kg -> L/day/kg
d2=ng(Cneed,MWs)*Cl/0.62/1000.0
print("== ORAL DOSE REQUIRED FOR 40%% ENGAGEMENT — TWO INDEPENDENT METHODS ==")
print("  (a) linear scaling from Cmax:      %.3f mg/kg"%d1)
print("  (b) from clearance, Css=D*F/(Cl*t): %.3f mg/kg/day   [Cl=%.3f L/day/kg, F=0.62]"%(d2,Cl))
print("  -> CONVERGENT at ~0.15 mg/kg  (= %.1f mg for a 60 kg subject)"%(0.15*60))
print()
print("== SAFETY MARGIN, IN THE WORST-CASE GENOTYPE ==")
print("  Revolution label: ORAL 2.5, 10 and 15 mg/kg in IVERMECTIN-SENSITIVE (P-gp-NULL) COLLIES")
print("     -> NO adverse reactions (one transient ataxia at 5 mg/kg, then tolerated 10 and 15)")
print("  margin = 15 / %.3f = %.0fx  IN P-gp-DEFICIENT ANIMALS, BY THE ORAL ROUTE"%(d1,15/d1))
print("  Griffin 2005 in vitro: selamectin P-gp inhibition IC50 0.1 uM = %.0f ng/mL"%ng(0.1,MWs))
print("     -> at our target we sit at %.0f%% P-gp inhibition"%(100*Cneed/(Cneed+0.1)))
print("     BUT the worst case of P-gp inhibition IS P-gp ABSENCE, and that is the Collie genotype.")
print()
print("== FOR CONTRAST: MOXIDECTIN ==")
print("  needs %.2f uM = %.0f ng/mL sustained -> 250 mg/week (36 mg human ceiling)"%(TARGET/(1-TARGET)*IC50m, ng(TARGET/(1-TARGET)*IC50m,MWm)))
print("  P-gp-null Collie ORAL: 1.0 mg/kg -> 4/5 COMA, EUTHANIZED")
print("  ProHeart 12 depot 0.5 mg/kg SC: Cmax 8.5-15.9 ng/mL = %.4f-%.4f uM = %.1f-%.1f%% engaged"%(
      uM(8.5,MWm),uM(15.9,MWm),100*uM(8.5,MWm)/(uM(8.5,MWm)+IC50m),100*uM(15.9,MWm)/(uM(15.9,MWm)+IC50m)))
print("     tmax 10-30 DAYS, trough at 6 mo 0.33-2.26 ng/mL, little/no accumulation over 3 doses")
