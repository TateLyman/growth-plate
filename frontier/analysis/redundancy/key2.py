import numpy as np, gzip, json
exec(open("key.py").read().split("# THE REJUVENATING CORE")[0])
nA,nU,nP=len(AMF),len(AU),len(P3)
mA=np.nanmean(X[:,AMF],1); sA=np.nanstd(X[:,AMF],1,ddof=1)
mU=np.nanmean(X[:,AU],1);  sU=np.nanstd(X[:,AU],1,ddof=1)
mP=np.nanmean(X[:,P3],1);  sP=np.nanstd(X[:,P3],1,ddof=1)
pooled=np.sqrt((sA**2/nA)+(sU**2/nU))+0.05
tACT=(mA-mU)/pooled
pooled2=np.sqrt((sP**2/nP)+(sU**2/nU))+0.05
tYTH=(mP-mU)/pooled2
# real expression floor: gene must be well above array background in the HIGH group
lo=np.nanpercentile(X[np.isfinite(X)],25)
hi_enough=np.maximum(mA,mU)>np.nanpercentile(X[np.isfinite(X)],60)
ok=hi_enough&np.isfinite(tACT)&np.isfinite(tYTH)&(S!="")
print(f"probes passing expression+finite filter: {ok.sum()}")
sel=ok&(tACT>4)&(tYTH>2)&(ACT>0.5)&(YOUTH>0.3)
print(f"CONSISTENT: induced by adult microfracture AND higher in youth: {sel.sum()} probes")
SEC={"Bmp2","Bmp4","Bmp6","Bmp7","Gdf5","Wnt5a","Wnt4","Wnt11","Sfrp1","Sfrp2","Sfrp4","Sfrp5","Dkk1","Dkk2","Dkk3","Wif1","Notum","Grem1","Grem2","Nog","Chrd","Fgf2","Fgf9","Fgf18","Igf1","Igf2","Tgfb1","Tgfb2","Tgfb3","Vegfa","Pdgfa","Pdgfb","Ctgf","Ccn2","Ccn3","Nov","Cyr61","Ccn1","Thbs1","Thbs2","Spp1","Postn","Angptl1","Angptl2","Angptl4","C1qtnf3","Sulf1","Sulf2","Ihh","Shh","Ptch1","Gli1","Pthlh","Nppc","Ostn","Ngf","Bdnf","Ntf3","Slit2","Slit3","Robo1","Robo2","Ngfr","Sema3a","Netrin1","Ntn1","Il6","Il11","Lif","Osm","Ccl2","Cxcl12","Tnc","Lox","Loxl2","Mgp","Sost","Wnt16","Wnt3a","Rspo1","Rspo2","Rspo3","Lgr5","Lgr6","Prlr","Prl","Ghr","Inhba","Fst","Bmper","Twsg1"}
IMP={"Igf2","H19","Plagl1","Mest","Peg3","Dlk1","Meg3","Gtl2","Grb10","Ndn","Cdkn1c","Slc38a4","Zim1","Peg10","Rasgrf1","Impact","Nnat","Airn"}
rows={}
for i in np.where(sel)[0]:
    s=S[i]
    if s not in rows or tACT[i]>rows[s][0]: rows[s]=(tACT[i],ACT[i],YOUTH[i],tYTH[i])
print(f"unique genes: {len(rows)}")
def show(title,keys):
    hits={k:v for k,v in rows.items() if k in keys}
    print(f"\n=== {title} ({len(hits)}) ===")
    if not hits: print("   none"); return
    print(f"{'gene':11s}{'tACT':>7s}{'ACT':>7s}{'YOUTH':>7s}")
    for k,v in sorted(hits.items(),key=lambda x:-x[1][0]):
        print(f"{k:11s}{v[0]:7.1f}{v[1]:+7.2f}{v[2]:+7.2f}")
show("SECRETED / DRUGGABLE LIGANDS & RECEPTORS",SEC)
show("IMPRINTED NETWORK (the R111 counter)",IMP)
print("\n=== TOP 30 BY CONSISTENCY (any gene) ===")
print(f"{'gene':14s}{'tACT':>7s}{'ACT':>7s}{'YOUTH':>7s}")
for k,v in sorted(rows.items(),key=lambda x:-x[1][0])[:30]:
    print(f"{k:14s}{v[0]:7.1f}{v[1]:+7.2f}{v[2]:+7.2f}")
