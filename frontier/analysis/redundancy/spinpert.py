import json,re,collections
d=json.load(open('spin4_harmonizome.json'))
rum=collections.defaultdict(lambda:{'dn':0,'up':0,'gse':set(),'sp':set()})
pat=re.compile(r'^(?P<gse>[^_]+)_(?P<a>\d+)_v_(?P<b>\d+)_(?P<drug>.+)_(?P<sp>[a-z ]+)$')
for x in d['associations']:
    n=x['geneSet']['name']
    if '/' not in n: continue
    setn,ds=n.split('/',1)
    if not ds.startswith('RummaGEO Drug'): continue
    m=pat.match(setn)
    if not m: print('UNPARSED',setn); continue
    g=rum[m.group('drug')]
    tv=x.get('thresholdValue')
    g['dn' if tv<0 else 'up']+=1
    g['gse'].add(m.group('gse')); g['sp'].add(m.group('sp'))
out=[]
for k,v in rum.items():
    out.append((v['dn'],v['up'],len(v['gse']),','.join(sorted(v['sp'])),k))
out.sort(key=lambda r:(-r[0],r[1]))
print('%-26s %4s %4s %5s  %s'%('agent','DOWN','UP','#GSE','species'))
for dn,up,ng,sp,k in out:
    if dn>=3: print('%-26s %4d %4d %5d  %s%s'%(k,dn,up,ng,sp,'   <-- CLEAN' if up==0 else ''))
print()
print('total agents with >=1 SPIN4-down signature:',sum(1 for r in out if r[0]))
print('total distinct agents:',len(out))
