"""Download the FULL record - protocol AND results - for every trial that measured a
stature endpoint and posted its results.  506 trials nobody has read for growth."""
import json, os, time, urllib.request, urllib.parse
keep=[k for k in json.load(open("ctg_growth_trials.json")) if k["has_results"]]
os.makedirs("ctg", exist_ok=True)
API="https://clinicaltrials.gov/api/v2/studies/"
done=0
for k in keep:
    p=f"ctg/{k['nct']}.json"
    if os.path.exists(p) and os.path.getsize(p)>500: done+=1; continue
    for a in range(4):
        try:
            req=urllib.request.Request(API+k["nct"]+"?format=json",
                                       headers={"User-Agent":"growth-plate-atlas/1.0"})
            with urllib.request.urlopen(req,timeout=90) as r: open(p,"wb").write(r.read())
            done+=1; break
        except Exception as e:
            if a==3: print("FAIL",k["nct"],e)
            else: time.sleep(2**a)
    time.sleep(0.15)
    if done%50==0: print(f"  {done}/{len(keep)}",flush=True)
print(f"downloaded {done}/{len(keep)} full trial records")
