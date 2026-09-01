import lib,json,glob,os,numpy as np
recs={r['acc']:r for r in json.load(open('recs.json'))}
out=[]
for f in sorted(glob.glob('mat/*.txt')):
    acc=os.path.basename(f)[:-4]
    try: D=lib.load(acc)
    except Exception as e:
        print("FAIL",acc,type(e).__name__,e); continue
    if D is None:
        print("NOTAB",acc); continue
    r=recs.get(acc,{})
    out.append(dict(acc=acc,plat=D['plat'],n=len(D['titles']),nrow=int(D['X'].shape[0]),
        sym=int((D['g']!='').sum()),title=r.get('title',''),org=r.get('org',''),
        titles=D['titles'],chars=D['chars']))
json.dump(out,open('inv.json','w'))
print("loaded",len(out),"| with symbols:",sum(1 for o in out if o['sym']>1000))
