import pickle,subprocess,sys,collections,json,os,gzip
names,kmap=pickle.load(open('sra/kmers.pkl','rb'))
K=32; STRIDE=16; NREADS=8_000_000
RUNS={'Ctrl1':'SRR29528359','Ctrl2':'SRR29528358','Ctrl3':'SRR29528357',
      'cKO1':'SRR29528356','cKO2':'SRR29528355','cKO3':'SRR29528354'}
def url(r):
    import json; return json.load(open("sra/urls.json"))[r]
res={}
for lab,run in RUNS.items():
    u=url(run); print(f"[{lab}] {u}",flush=True)
    p=subprocess.Popen(['curl','-sSL','--max-time','3600',u],stdout=subprocess.PIPE,bufsize=1<<24)
    g=gzip.GzipFile(fileobj=p.stdout)
    c=collections.Counter(); n=0; ln=0
    try:
        for line in g:
            ln+=1
            if ln%4!=2: continue
            n+=1
            s=line.decode().strip()
            seen=set()
            for j in range(0,len(s)-K+1,STRIDE):
                v=kmap.get(s[j:j+K])
                if v is not None: seen.add(v)
            for v in seen: c[v]+=1
            if n>=NREADS: break
    except Exception as e:
        print(f"  [{lab}] stream ended: {e}",flush=True)
    try: p.kill()
    except: pass
    res[lab]={'reads':n, **{names[i]:c[i] for i in range(len(names))}}
    print(f"  [{lab}] reads={n:,}  " + "  ".join(f"{names[i]}={c[i]}" for i in range(len(names))),flush=True)
    json.dump(res,open('sra/counts.json','w'),indent=1)
print("DONE",flush=True)
