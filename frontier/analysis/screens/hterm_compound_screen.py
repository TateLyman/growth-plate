import json,urllib.request,time
Q='''query($id:String!){ target(ensemblId:$id){ approvedSymbol
 tractability{label modality value}
 drugAndClinicalCandidates{ count rows{ maxClinicalStage drug{ name drugType maximumClinicalStage } } } } }'''
GENES=[
 ('A  IGF/phase-3','PAPPA','ENSG00000182752'),('A  IGF/phase-3','PAPPA2','ENSG00000116183'),
 ('A  IGF/phase-3','STC2','ENSG00000113739'),('A  IGF/phase-3','IGFBP4','ENSG00000141753'),
 ('A  IGF/phase-3','IGFBP5','ENSG00000115461'),('A  IGF/phase-3','IGF1','ENSG00000017427'),
 ('A  IGF/phase-3','IGF1R','ENSG00000140443'),
 ('B  CNP axis','NPPC','ENSG00000163273'),('B  CNP axis','NPR2','ENSG00000159899'),
 ('B  CNP axis','NPR3','ENSG00000113389'),('B  CNP axis','OSTN','ENSG00000188010'),
 ('B  CNP axis','MME','ENSG00000196549'),
 ('C  hypertrophy','IHH','ENSG00000163501'),('C  hypertrophy','PTHLH','ENSG00000087494'),
 ('C  hypertrophy','PTH1R','ENSG00000160801'),('C  hypertrophy','HDAC4','ENSG00000068024'),
 ('C  hypertrophy','SOX9','ENSG00000125398'),('C  hypertrophy','RUNX2','ENSG00000124813'),
 ('C  hypertrophy','GLI2','ENSG00000074047'),('C  hypertrophy','SMO','ENSG00000128602'),
 ('D  volume/other','INPPL1','ENSG00000165458'),('D  volume/other','MTOR','ENSG00000198793'),
 ('D  volume/other','FGFR3','ENSG00000068078'),
]
def gql(v):
    req=urllib.request.Request('https://api.platform.opentargets.org/api/v4/graphql',
        data=json.dumps({'query':Q,'variables':{'id':v}}).encode(),
        headers={'Content-Type':'application/json'})
    return json.load(urllib.request.urlopen(req,timeout=90))
res={}
print('%-15s %-8s %6s  %-34s %s'%('tier','gene','nDrug','tractability (SM / AB)','top agents by stage'))
print('-'*128)
for tier,g,e in GENES:
    try:
        d=gql(e)['data']['target']
        tr={ (t['modality'],t['label']):t['value'] for t in (d.get('tractability') or []) }
        sm='approved' if tr.get(('SM','Approved Drug')) else ('clin' if tr.get(('SM','Advanced Clinical')) or tr.get(('SM','Phase 1 Clinical')) else ('pocket' if tr.get(('SM','High-Quality Pocket')) else '-'))
        ab='approved' if tr.get(('AB','Approved Drug')) else ('clin' if tr.get(('AB','Advanced Clinical')) or tr.get(('AB','Phase 1 Clinical')) else '-')
        dc=d.get('drugAndClinicalCandidates') or {}
        rows=dc.get('rows') or []
        best={}
        for r in rows:
            n=r['drug']['name']; st=str(r.get("maxClinicalStage") or "")
            if n not in best or len(st)>len(best[n][0]): best[n]=(st,r["drug"].get("drugType"))
        top=sorted(best.items(),key=lambda x: str(x[1][0]),reverse=True)[:4]
        s=', '.join('%s(ph%s,%s)'%(n[:20],v[0],(v[1] or '')[:12]) for n,v in top)
        print('%-15s %-8s %6s  SM:%-9s AB:%-9s  %s'%(tier,g,dc.get('count',0),sm,ab,s or '-- none --'))
        res[g]=(dc.get('count',0),sm,ab,[(n,v[0],v[1]) for n,v in top])
    except Exception as ex: print('%-15s %-8s ERR %s'%(tier,g,str(ex)[:60]))
    time.sleep(0.35)
json.dump(res,open('hterm_screen.json','w'),indent=1)
