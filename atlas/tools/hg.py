import urllib.request, json, time
q='{ target(ensemblId:"%s"){ approvedSymbol associatedDiseases(page:{index:0,size:250}){ rows{ score disease{ name } } } } }'
def ot(e):
    r=urllib.request.Request('https://api.platform.opentargets.org/api/v4/graphql',
        data=json.dumps({"query":q%e}).encode(),headers={'Content-Type':'application/json'})
    return json.load(urllib.request.urlopen(r,timeout=60))
def ensembl(s):
    u=f"https://rest.ensembl.org/xrefs/symbol/homo_sapiens/{s}?content-type=application/json"
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'a'}),timeout=40))
        for x in d:
            if x.get('type')=='gene': return x['id']
    except Exception: pass
    return None
rows=json.load(open('/home/user/growth-plate/query/target_screen/compounds.json'))
GO=["A","B","C","D","E","speculative","X"]
targets=sorted({t for r in rows if r['helps'] and r['expressed_in_human_gp']
                and GO.index(r['best_grade'])<=3 for t in r['targets']})
TALL=('tall stature','overgrowth','gigantism','macrosomia')
SHORT=('short stature','dwarf','growth retardation','brachyolmia')
out={}
for i,s in enumerate(targets):
    e=ensembl(s)
    if not e:
        print(f"{i+1}/{len(targets)} {s}: no ensembl",flush=True); continue
    try: d=ot(e)
    except Exception as ex:
        print(f"{i+1}/{len(targets)} {s}: ERR",flush=True); continue
    t=(d.get('data') or {}).get('target')
    if not t: continue
    hits=[(x['disease']['name'],x['score']) for x in t['associatedDiseases']['rows']]
    out[s]={'tall':[h for h in hits if any(k in h[0].lower() for k in TALL)],
            'short':[h for h in hits if any(k in h[0].lower() for k in SHORT)],'ensembl':e}
    print(f"{i+1}/{len(targets)} {s}: tall={len(out[s]['tall'])} short={len(out[s]['short'])}",flush=True)
json.dump(out,open('/home/user/growth-plate/query/target_screen/height_genetics.json','w'),indent=1)
print("DONE")
