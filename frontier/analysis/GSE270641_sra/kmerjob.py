import json,gzip,subprocess,sys,collections,pickle,os
K=32
seqs=json.load(open('sra/targets.json'))
comp=str.maketrans('ACGTacgt','TGCAtgca')
def rc(s): return s.translate(comp)[::-1]
kmap={}          # kmer -> locus id
dup=set()
names=sorted(seqs)
for i,n in enumerate(names):
    s=seqs[n]
    for j in range(len(s)-K+1):
        km=s[j:j+K]
        if km.islower() or 'N' in km.upper(): continue   # drop repeat-masked
        km=km.upper()
        for v in (km, rc(km)):
            if v in kmap and kmap[v]!=i: dup.add(v)
            else: kmap[v]=i
for v in dup: kmap.pop(v,None)
print(f"loci: {len(names)}  unique non-repeat {K}-mers: {len(kmap):,} (dropped {len(dup):,} shared)",flush=True)
cnt=collections.Counter()
for v in kmap.values(): cnt[v]+=1
for i,n in enumerate(names): print(f"  {n:12s} {cnt[i]:>9,} kmers",flush=True)
pickle.dump((names,kmap),open('sra/kmers.pkl','wb'))
