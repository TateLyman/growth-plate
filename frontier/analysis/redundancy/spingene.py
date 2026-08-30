import json,re,collections
d=json.load(open('spin4_harmonizome.json'))
g=collections.defaultdict(lambda:{'dn':0,'up':0,'gse':set(),'sp':set()})
pat=re.compile(r'^(?P<gse>[^_]+)_(\d+)_v_(\d+)_(?P<pert>.+)_(?P<sp>[a-z ]+)$')
tf=collections.Counter()
for x in d['associations']:
    n=x['geneSet']['name']
    if '/' not in n: continue
    setn,ds=n.split('/',1)
    if ds.startswith('RummaGEO Gene Perturbation'):
        m=pat.match(setn)
        if not m: continue
        r=g[m.group('pert')]
        r['dn' if x['thresholdValue']<0 else 'up']+=1
        r['gse'].add(m.group('gse')); r['sp'].add(m.group('sp'))
    elif ds.startswith('Rummagene Transcription Factor'):
        tf[setn]+=1
out=sorted(((v['dn'],v['up'],len(v['gse']),','.join(sorted(v['sp'])),k) for k,v in g.items()),key=lambda r:(-r[0],r[1]))
print('=== GENE PERTURBATIONS that lower SPIN4 (RummaGEO) ===')
print('%-30s %4s %4s %5s  %s'%('perturbation','DOWN','UP','#GSE','species'))
for dn,up,ng,sp,k in out:
    if dn>=3: print('%-30s %4d %4d %5d  %s%s'%(k,dn,up,ng,sp,'   <-- CLEAN' if up==0 else ''))
tot_dn=sum(v['dn'] for v in g.values()); tot_up=sum(v['up'] for v in g.values())
print('base rate gene-pert: DOWN=%d UP=%d (%.3f)'%(tot_dn,tot_up,tot_dn/(tot_dn+tot_up)))
print()
print('=== TFs whose target set contains SPIN4 (Rummagene TF Assoc 2026), top 25 ===')
print(', '.join(k for k,_ in tf.most_common(25)))
print('n TFs:',len(tf))
