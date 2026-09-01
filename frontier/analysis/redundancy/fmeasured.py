"""f IS MEASURED. Table S-5 of PMC11738990 gives rentosertib's IC50 on its own
GCK-IV paralogs -- and R150 showed exactly how similar those paralogs' pockets are.
"""
IC50 = {'TNIK': 31, 'MINK1': 115, 'MAP4K4': 277, 'MAP4K5': 1228}
# from R150: contact-surface identity to TNIK, and divergence at rentosertib's OWN
# published design pharmacophore (Cys108 hinge anchor + back cavity M105/L73/L103/A52/V104)
CONTACT = {'MINK1': (23, 23, 0), 'MAP4K4': (23, 23, 0), 'MAP4K5': (17, 23, 4), 'NRK': (17, 23, 1)}
T = IC50['TNIK']
W = (0.38, 0.45)
def nrk_at(Ew, f): return f*Ew/(1-Ew+f*Ew)

print("="*100)
print("MEASURED: RENTOSERTIB vs ITS OWN CLADE  (Eurofins KinaseProfiler, 430 kinases; Table S-5)")
print("="*100)
print("%-9s %9s %10s %16s %26s"%("kinase","IC50 (nM)","fold vs","f = IC50(TNIK)","contact identity / design"))
print("%-9s %9s %10s %16s %26s"%("","","TNIK","  / IC50(X)","divergence vs TNIK"))
print("-"*100)
for k in ['TNIK','MINK1','MAP4K4','MAP4K5']:
    f = T/IC50[k]
    c = CONTACT.get(k)
    cs = ("%d/%d contacts, %d design"%(c[0],c[1],c[2])) if c else "(reference)"
    print("%-9s %9d %10s %16.3f %26s"%(k, IC50[k], "%.1fx"%(IC50[k]/T), f, cs))

print()
print("="*100)
print("THE DECISIVE INFERENCE")
print("="*100)
print("  MINK1 and MAP4K4 have 23/23 IDENTICAL ligand-contact surfaces with TNIK and")
print("  0/6 divergence at rentosertib's OWN published design pharmacophore.")
print("  They are the BEST-CASE paralogs -- structurally indistinguishable where the drug binds.")
print()
print("     -> and rentosertib STILL loses %.1fx on MINK1 (f=%.2f) and %.1fx on MAP4K4 (f=%.2f)."
      %(IC50['MINK1']/T, T/IC50['MINK1'], IC50['MAP4K4']/T, T/IC50['MAP4K4']))
print()
print("  NRK is strictly WORSE matched than either: 17/23 contacts, 1 design residue diverged.")
print("  So f(NRK) is CAPPED by the best paralog value, %.2f -- and realistically well below it."
      % (T/IC50['MINK1']))

print()
print("="*100)
print("FEED THE MEASURED CEILING INTO R148's EQUATION  E_nrk = f*E_wnt/(1-E_wnt+f*E_wnt)")
print("="*100)
print("%-34s %-26s %s"%("case","f","NRK engagement at Wnt 38-45%"))
print("-"*92)
rows=[("MINK1 (identical pocket) = CEILING", T/IC50['MINK1']),
      ("MAP4K4 (identical pocket)", T/IC50['MAP4K4']),
      ("MAP4K5 (17/23, like NRK)", T/IC50['MAP4K5']),
      ("what the both-arms case NEEDED", 0.70)]
for lab,f in rows:
    lo,hi = 100*nrk_at(W[0],f), 100*nrk_at(W[1],f)
    tag = "  <-- REQUIRED" if lab.startswith("what") else ("  DEAD" if lo<15 else "")
    print("%-34s %-26s %.1f%% - %.1f%%%s"%(lab,"%.3f"%f,lo,hi,tag))
print()
print("  -> the measured CEILING on NRK engagement at the SPIN4 Wnt window is %.1f-%.1f%%."
      %(100*nrk_at(W[0],T/IC50['MINK1']), 100*nrk_at(W[1],T/IC50['MINK1'])))
print("     R148 required 30%+ for the arm to be real. THE CEILING IS BELOW THE FLOOR.")
