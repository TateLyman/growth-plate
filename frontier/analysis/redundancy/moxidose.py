MW=639.82                      # moxidectin, g/mol
def nM(ng_per_mL): return ng_per_mL*1e-6/MW*1e9      # ng/mL -> nM
def uM(ng_per_mL): return nM(ng_per_mL)/1000.0

print("MOXIDECTIN MW %.2f  |  1 ng/mL = %.3f nM"%(MW,nM(1)))
print()
print("== HUMAN SINGLE-DOSE Cmax, CONVERTED ==")
print("%-22s %9s %9s %9s"%("regimen","Cmax ng/mL","nM","uM"))
rows=[("3 mg liquid (Cotreau)",22.4),("8 mg TABLET fasted (tropmed)",58.9),
      ("8 mg tablet FED (+34%)",58.9*1.34),("9 mg liquid",57.9),
      ("10 mg TABLET (CPDD)",67.1),("18 mg liquid",141.0),
      ("36 mg liquid fasted",289.0),("36 mg liquid FED",296.0)]
for n,c in rows: print("%-22s %9.1f %9.1f %9.4f"%(n,c,nM(c),uM(c)))

print()
print("== MELOTTI ACTIVE CONCENTRATIONS ==")
print("  moxidectin  BrdU IC50   ~1.0-2.5 uM  ('comparable to ivermectin')")
print("  ivermectin  BrdU IC50    1.0-2.4 uM ; TCF targets 0.5-5 uM")
print("  selamectin  BrdU IC50    0.08-0.14 uM ; spheroid 0.01-0.1 uM")

def hill(C,ic50): return 100.0*C/(C+ic50)
print()
print("== FRACTIONAL PATHWAY ENGAGEMENT (Hill n=1, IC50 1.5 uM for moxidectin) ==")
print("%-22s %10s %10s"%("regimen","Cmax uM","% engaged"))
for n,c in rows: print("%-22s %10.4f %9.1f%%"%(n,uM(c),hill(uM(c),1.5)))

print()
print("== SUSTAINED EXPOSURE: Css,avg = AUC_per_dose / tau  (this ALREADY includes accumulation) ==")
CL=2.76           # L/h, 8 mg tablet
AUC8=3387.0       # ng.h/mL, 8 mg tablet fasted
AUC8f=AUC8*1.44   # fed, +44%
AUC36=451.0*24    # 36 mg liquid fasted, ng.d/mL -> ng.h/mL
print("%-28s %11s %9s %9s %10s"%("regimen","Css ng/mL","nM","uM","% engaged"))
for label,auc,tau in [("8 mg fasted MONTHLY",AUC8,720),("8 mg fasted WEEKLY",AUC8,168),
                      ("8 mg FED weekly",AUC8f,168),("8 mg FED twice-weekly",AUC8f,84),
                      ("16 mg fed weekly",AUC8f*2,168),("36 mg fasted monthly",AUC36,720),
                      ("36 mg fasted weekly",AUC36,168)]:
    css=auc/tau
    print("%-28s %11.1f %9.1f %9.4f %9.1f%%"%(label,css,nM(css),uM(css),hill(uM(css),1.5)))

print()
print("== DOSE REQUIRED FOR A TARGET SUSTAINED CONCENTRATION ==")
print("  Css,avg = (Dose x F) / (CL/F x tau)  ->  Dose/tau = Css x CL/F")
CLd=CL*24  # L/day
print("  CL/F = %.2f L/h = %.1f L/day"%(CL,CLd))
print("%-14s %12s %14s %14s %16s"%("target uM","target ng/mL","mg/day","mg/week","6-mo cumulative"))
for t in [0.01,0.02,0.03,0.05,0.10,0.15]:
    ng=t*1000*MW/1e3   # uM -> ng/mL :  uM*1e-6 mol/L *MW g/mol = g/L ; *1e6 = ng/mL... do directly
    ng=t*1e-6*MW*1e9/1000.0
    mgd=ng*CLd/1000.0
    print("%-14.3f %12.1f %14.2f %14.1f %16.0f mg"%(t,ng,mgd,mgd*7,mgd*182))

print()
print("== TIME TO STEADY STATE, AND ACCUMULATION ==")
import math
for th in [32.7,43.0]:
    print("  t1/2 = %.1f d  ->  90%% of steady state at %.0f d (3.3 half-lives); 95%% at %.0f d"%(th,3.32*th,4.32*th))
for tau,th in [(7,32.7),(7,43.0),(30,32.7)]:
    R=1/(1-math.exp(-0.693*tau/th))
    print("  dosing every %2d d, t1/2 %.1f d  ->  accumulation ratio %.2f x"%(tau,th,R))
print()
print("== LOADING DOSE TO REACH TARGET IMMEDIATELY:  Load = Css_target x Vd/F ==")
Vd=2829.0
for t in [0.02,0.03,0.05]:
    ng=t*1e-6*MW*1e9/1000.0
    print("  target %.3f uM (%.1f ng/mL)  ->  load = %.0f mg   %s"%(t,ng,ng*Vd/1000.0,
          "<= 36 mg TESTED" if ng*Vd/1000.0<=36 else ">> 36 mg  ** EXCEEDS TESTED MAXIMUM **"))
