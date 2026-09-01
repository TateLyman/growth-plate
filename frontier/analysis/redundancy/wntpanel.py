import urllib.request,json,os,re,collections,time
PANEL=["AXIN2","LEF1","TCF7","NKD1","RNF43","ZNRF3","SP5","CCND1","NOTUM","TNFRSF19"]
def fetch(g):
    fn="hz_%s.json"%g
    if os.path.exists(fn): return json.load(open(fn))
    u="https://maayanlab.cloud/Harmonizome/api/1.0/gene/%s?showAssociations=true"%g
    d=json.load(urllib.request.urlopen(u,timeout=180))
    json.dump(d,open(fn,"w")); time.sleep(1); return d
pat=re.compile(r'^(?P<gse>[^_]+)_(\d+)_v_(\d+)_(?P<drug>.+)_(?P<sp>[a-z ]+)$')
def drugsigs(d):
    """-> {signature_name: +1/-1} for RummaGEO drug sets"""
    out={}
    for x in d.get('associations',[]):
        n=x['geneSet']['name']
        if '/' not in n: continue
        s,ds=n.split('/',1)
        if not ds.startswith('RummaGEO Drug'): continue
        out[s]=-1 if x['thresholdValue']<0 else 1
    return out
S4=drugsigs(fetch("SPIN4"))
print("SPIN4 signatures:",len(S4))
W={}
for g in PANEL:
    try:
        W[g]=drugsigs(fetch(g)); print("  %-9s %d sigs"%(g,len(W[g])))
    except Exception as e: print("  ERR",g,e)
# For each agent: within signatures where SPIN4 is DOWN, how do Wnt targets behave?
agent=collections.defaultdict(lambda: collections.Counter())
for sig,v in S4.items():
    m=pat.match(sig)
    if not m or v>0: continue           # only SPIN4-DOWN signatures
    a=m.group('drug')
    for g,d in W.items():
        if sig in d:
            agent[a]['wnt_dn' if d[sig]<0 else 'wnt_up']+=1
    agent[a]['n_s4dn']+=1
print()
print("Within SPIN4-DOWN signatures: co-occurrence of canonical Wnt target genes")
print("%-24s %7s %7s %7s  %s"%("agent","S4dn","WNTdn","WNTup","call"))
rows=sorted(agent.items(),key=lambda kv:-(kv[1]['wnt_dn']))
tot_dn=tot_up=0
for a,c in rows:
    tot_dn+=c['wnt_dn']; tot_up+=c['wnt_up']
    if c['wnt_dn']+c['wnt_up']==0: continue
    call="WNT DOWN too" if c['wnt_dn']>c['wnt_up'] else ("WNT UP" if c['wnt_up']>c['wnt_dn'] else "split")
    print("%-24s %7d %7d %7d  %s"%(a,c['n_s4dn'],c['wnt_dn'],c['wnt_up'],call))
print()
print("TOTAL within SPIN4-down signatures:  WNT-down=%d  WNT-up=%d  -> down frac %.3f"%(tot_dn,tot_up,tot_dn/max(1,tot_dn+tot_up)))
