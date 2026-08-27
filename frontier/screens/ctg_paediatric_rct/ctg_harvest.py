#!/usr/bin/env python3
"""Harvest ClinicalTrials.gov v2 for paediatric interventional trials that POSTED a
height / stature / growth-velocity OUTCOME measure. Saves raw JSON; no interpretation here."""
import json,os,sys,time,urllib.parse,urllib.request

BASE="https://clinicaltrials.gov/api/v2/studies"
UA={'User-Agent':'height-frontier/0.1 (hello@tateprograms.com)'}
OUT="ctg_raw"
os.makedirs(OUT,exist_ok=True)

TERMS=[ "height","stature","growth velocity","height velocity","height SDS",
        "height z-score","height standard deviation","linear growth","body length",
        "growth rate","final height","adult height","height percentile"]

def fetch(term):
    studies=[];token=None;page=0
    q=f"AREA[OutcomeMeasureTitle]({urllib.parse.quote(term)})"
    while True:
        url=(f"{BASE}?query.term={q}&aggFilters=results:with&pageSize=100&countTotal=true")
        if token: url+=f"&pageToken={token}"
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=120)
            d=json.load(r)
        except Exception as e:
            print(f"  ! {term} page {page}: {e}");break
        studies+=d.get('studies',[])
        token=d.get('nextPageToken');page+=1
        if page==1: print(f"  {term}: totalCount={d.get('totalCount')}")
        if not token: break
        time.sleep(0.3)
    return studies

allstudies={}
for t in TERMS:
    for s in fetch(t):
        nct=s['protocolSection']['identificationModule']['nctId']
        allstudies[nct]=s
    print(f"  running unique: {len(allstudies)}")

json.dump(allstudies,open(f"{OUT}/studies.json","w"))
print("TOTAL UNIQUE STUDIES WITH RESULTS + A HEIGHT-LIKE OUTCOME TITLE:",len(allstudies))
