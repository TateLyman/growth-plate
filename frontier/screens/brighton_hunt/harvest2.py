import json,urllib.request,urllib.parse,re,time,sys,os
UA={'User-Agent':'Mozilla/5.0 (research; contact research@example.org)'}
def get(u,timeout=50):
    try:
        r=urllib.request.Request(u,headers=UA)
        return urllib.request.urlopen(r,timeout=timeout).read()
    except Exception as e:
        return None

TARGETS={
 'brighton1969_oxygen':'W1626063061',
 'stambaugh1980_diffusion':'W2289442815',
}
out={}
for name,wid in TARGETS.items():
    cits=[]
    cursor='*'
    while True:
        u=('https://api.openalex.org/works?filter=cites:%s&per-page=200&cursor=%s'
           '&select=id,doi,title,publication_year,open_access,primary_location,type,ids'
           '&mailto=research@example.org')%(wid,cursor)
        b=get(u)
        if not b: break
        d=json.loads(b)
        cits+=d.get('results',[])
        cursor=(d.get('meta') or {}).get('next_cursor')
        if not cursor or not d.get('results'): break
        time.sleep(0.3)
    out[name]=cits
    oa=[c for c in cits if (c.get('open_access') or {}).get('is_oa')]
    print('%-28s citing=%-4d OA=%-4d'%(name,len(cits),len(oa)))
    for c in oa:
        print('    %s %s'%(c.get('publication_year'),(c.get('title') or '')[:95]))
json.dump(out,open('citing.json','w'))
