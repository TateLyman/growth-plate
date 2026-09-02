import json, sys, re
B='/home/user/growth-plate/query/'
D=json.load(open(B+'derived.json'))
G=json.load(open(B+'graph.json'))
P=json.load(open(B+'parameters.json'))
GP=json.load(open(B+'gaps.json'))
N=G['nodes']; E=G['edges']; R=G['refs']
A=D['alias_to_id']

def alias(s):
    s=s.lower()
    return {k:v for k,v in A.items() if s in k}

def node(i, full=False):
    n=N.get(i)
    if not n: print('NO NODE',i); return
    for k,v in n.items():
        if v is None: continue
        s=json.dumps(v) if not isinstance(v,str) else v
        if not full and len(s)>1600: s=s[:1600]+'...'
        print(f'--{k}: {s}')

def edges(i,dirn='both'):
    for e in E:
        if (dirn in ('both','out') and e['source']==i) or (dirn in ('both','in') and e['target']==i):
            print(e['edge_id'],e['source'],'-',e['relation'],e['sign'],'->',e['target'],'|',e['confidence'],'|use',e['traversal_usable'],'|',(e.get('context') or '')[:90])

def edge(i):
    for e in E:
        if e['edge_id']==i: print(json.dumps(e,indent=1))

def reach(i,lim=4000):
    print(json.dumps(D['reachability'].get(i),indent=1)[:lim])

def gaps(**kw):
    for x in GP['gaps']:
        if all(x.get(k)==v for k,v in kw.items()): print(x['gap_id'],x.get('layer'),x.get('type'),x.get('tractability'),'|',x['question'][:130])

def gapsearch(s):
    s=s.lower()
    for x in GP['gaps']:
        if s in json.dumps(x).lower(): print(x['gap_id'],x.get('layer'),x.get('type'),x.get('tractability'),'|',x['question'][:150])

def gap(i):
    for x in GP['gaps']:
        if x['gap_id']==i: print(json.dumps(x,indent=1))

def nodesearch(s):
    s=s.lower()
    for k,n in N.items():
        if s in k.lower() or s in n.get('name','').lower(): print(k,'|',n['layer'],n['confidence'],'|',n['name'])

def deepsearch(s):
    s=s.lower()
    for k,n in N.items():
        if s in json.dumps(n).lower(): print(k,'|',n['layer'],n['confidence'],'|',n['name'])

def param(i,lim=4000):
    print(json.dumps(P['by_node'].get(i),indent=1)[:lim])

def psearch(s,lim=300):
    s=s.lower()
    for k,v in P['by_node'].items():
        for row in (v if isinstance(v,list) else [v]):
            if s in json.dumps(row).lower(): print(k,'|',json.dumps(row)[:lim])

def disp(s=None,lim=3000):
    for k,v in P['disputed'].items():
        if s is None or s.lower() in k.lower() or s.lower() in json.dumps(v).lower():
            print('==',k); print(json.dumps(v,indent=1)[:lim])

def ref(i):
    print(json.dumps(R.get(i),indent=1))

SIGN={'+':1,'-':-1}
def bfs(start,maxd=4):
    out={}; frontier=[(start,1,[])]
    seen={start}
    d=0
    while frontier and d<maxd:
        d+=1; nxt=[]
        for (n,s,p) in frontier:
            for e in E:
                if e['source']==n and e.get('traversal_usable') and e.get('sign') in SIGN:
                    t=e['target']
                    if t in seen: continue
                    seen.add(t); ns=s*SIGN[e['sign']]
                    out[t]={'sign':ns,'depth':d,'path':p+[e['edge_id']]}
                    nxt.append((t,ns,p+[e['edge_id']]))
        frontier=nxt
    return out
