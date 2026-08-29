import json,re
recs=json.load(open('recs.json'))
AXES={
 'METHYLOME/5hmC':(['methylom','methylation','bisulfite','RRBS','WGBS','5hmC','hydroxymethyl','MeDIP','DNMT','TET'],6),
 'RESTING/STEM ZONE':(['resting zone','reserve zone','PTHrP','Pthlh','skeletal stem','epiphyseal stem','stem cell niche','FoxA2','CD73'],5),
 'AGE/SENESCENCE SERIES':(['senescen','aging','ageing','age-related','postnatal age','time course','weeks of age','juvenile','maturation'],4),
 'HUMAN':(['Homo sapiens'],4),
 'HEDGEHOG':(['hedgehog','Ihh','Shh','Gli','Ptch','Smo','SAG'],3),
 'REPROGRAMMING':(['reprogram','Yamanaka','OSK','Oct4','rejuven'],5),
 'OESTROGEN/FUSION':(['estrogen','oestrogen','fusion','epiphyseal fusion','ovariectom','aromatase'],3),
 'ZONE-DISSECTED':(['microdissect','laser capture','zone','proliferative zone','hypertrophic zone'],3),
 'SINGLE CELL':(['single cell','single-cell','scRNA','10x'],2),
}
for r in recs:
    blob=(r['title']+' '+r['summary']+' '+r['org']+' '+r['gdstype']).lower()
    r['hits']={}; s=0
    for ax,(kws,w) in AXES.items():
        h=[k for k in kws if k.lower() in blob]
        if h: r['hits'][ax]=h; s+=w
    if 'homo sapiens' in r['org'].lower(): s+=2
    r['score']=s
recs.sort(key=lambda x:-x['score'])
print('%-12s %-4s %-6s %-28s %s'%('GSE','n','score','organism','axes'))
for r in recs[:45]:
    print('%-12s %-4s %-6d %-28s %s'%(r['acc'],r['n'],r['score'],r['org'][:28],','.join(r['hits'].keys())[:70]))
json.dump(recs,open('scored.json','w'),indent=1)
