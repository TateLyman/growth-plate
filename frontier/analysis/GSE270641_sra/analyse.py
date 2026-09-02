import json,math,statistics as st
from scipy import stats
d=json.load(open('sra/counts.json'))
loci=[k for k in d['Ctrl1'] if k!='reads']
C=['Ctrl1','Ctrl2','Ctrl3']; K=['cKO1','cKO2','cKO3']
print("RAW READS PER 8,000,000 (unnormalised)")
print(f"{'locus':12s} " + " ".join(f"{s:>7s}" for s in C+K))
for L in ['NEG_desert']+sorted(x for x in loci if x!='NEG_desert'):
    print(f"{L:12s} " + " ".join(f"{d[s][L]:7d}" for s in C+K))
print("\n--> the gene desert rises %.1fx in cKO: MBD pulldown specificity collapses as methylation is lost."
      % (st.mean(d[s]['NEG_desert'] for s in K)/st.mean(d[s]['NEG_desert'] for s in C)))
print("    Raw counts are therefore NOT interpretable. Normalise each locus to the desert.\n")
print("ENRICHMENT RELATIVE TO THE GENE DESERT  (locus reads / desert reads)")
print(f"{'locus':12s} {'Ctrl mean':>10s} {'cKO mean':>10s} {'cKO/Ctrl':>9s} {'log2':>7s} {'Welch p':>9s}")
rows=[]
for L in sorted(x for x in loci if x!='NEG_desert'):
    c=[d[s][L]/d[s]['NEG_desert'] for s in C]
    k=[d[s][L]/d[s]['NEG_desert'] for s in K]
    t,p=stats.ttest_ind(c,k,equal_var=False)
    fc=st.mean(k)/st.mean(c)
    rows.append((fc,L,st.mean(c),st.mean(k),p))
for fc,L,mc,mk,p in sorted(rows):
    flag=''
    if p<0.05 and fc<0.6: flag='  <<< METHYLATION LOST'
    print(f"{L:12s} {mc:10.3f} {mk:10.3f} {fc:9.2f} {math.log2(fc):7.2f} {p:9.4f}{flag}")

print("\n\nNORMALISATION-INDEPENDENT VIEW: raw fold-change cKO/Ctrl per locus")
print("(the desert rises 4.6x. A locus rising LESS than the desert lost methylation; one rising WITH it did not.)")
print(f"{'locus':12s} {'raw fold':>9s}   vs desert 4.60x")
fr=[]
for L in ['NEG_desert']+sorted(x for x in loci if x!='NEG_desert'):
    f=st.mean(d[s][L] for s in K)/st.mean(d[s][L] for s in C)
    fr.append((f,L))
for f,L in sorted(fr):
    tag='DESERT (background)' if L=='NEG_desert' else ('rises WITH background -> no Dnmt1 dependence' if f>3.5 else 'rises LESS than background -> methylation lost')
    if L=='Dnmt1': tag='FALLS in raw counts -> the floxed-exon DELETION itself'
    print(f"{L:12s} {f:9.2f}   {tag}")
