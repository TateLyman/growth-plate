import glob,os,sload,json
res=json.load(open('suptbl.json'))
n=0
for f in sorted(glob.glob('sup/*')):
    acc=os.path.basename(f).split('__')[0]
    if f.endswith(('.tar','.h5','.mtx','.xlsx')) or acc in res: continue
    if os.path.getsize(f)>200_000_000: continue
    try: D=sload.load_tbl(f)
    except Exception: D=None
    if D is None: continue
    res[acc]=[f,[D['X'].shape[1],D['X'].shape[0]],D['cols'][:6],[str(x) for x in D['g'][:3]]]
    n+=1
json.dump(res,open('suptbl.json','w'))
print('new suppl tables:',n,'total:',len(res),flush=True)
