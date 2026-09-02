import urllib.request, urllib.parse, json, time, re, sys
E='https://www.ebi.ac.uk/europepmc/webservices/rest/search'
UA={'User-Agent':'growth-atlas/1.0 (research use)'}
def srch(q, n=100):
    u=E+'?'+urllib.parse.urlencode({'query':q,'format':'json','pageSize':n,'resultType':'core'})
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60) as r:
                return json.loads(r.read().decode())['resultList']['result']
        except Exception as e:
            if i==2: print('ERR',q,e,file=sys.stderr); return []
            time.sleep(2**i)

QUERIES = {
 'A_pth_uremic_growth': '(PTH OR "parathyroid hormone" OR teriparatide) AND (uremi* OR uraemi* OR "renal failure" OR "chronic kidney") AND ("longitudinal growth" OR "growth plate" OR "body length" OR "linear growth" OR "growth velocity")',
 'B_pth_chondrocyte_proliferation_dose': '("parathyroid hormone" OR PTHrP) AND "growth plate chondrocyte*" AND (proliferation OR "dose-dependent" OR biphasic)',
 'C_bone_age_under_pth': '(teriparatide OR "PTH(1-34)" OR abaloparatide OR "parathyroid hormone") AND ("bone age" OR "skeletal maturation" OR "epiphyseal fusion" OR "growth plate closure")',
 'D_pth1r_human_puberty': '(PTH1R OR "PTH/PTHrP receptor" OR "parathyroid hormone 1 receptor") AND ("human growth plate" OR "pubertal" OR "Tanner")',
 'E_vertebral_height_pth': '(teriparatide OR "parathyroid hormone" OR abaloparatide) AND ("vertebral body height" OR "vertebral height" OR "spine length" OR "crown-rump")',
 'F_pairfed_pth': '("parathyroid hormone" OR teriparatide OR PTHrP) AND ("pair-fed" OR "pair fed" OR "pairfed")',
 'G_teriparatide_children': '(teriparatide OR abaloparatide OR "PTH(1-34)") AND (child* OR pediatric OR paediatric OR adolescent OR juvenile) AND (growth OR height OR stature)',
 'H_pth_tibial_femoral_length': '("parathyroid hormone" OR teriparatide OR PTHrP OR abaloparatide) AND ("femur length" OR "femoral length" OR "tibial length" OR "tibia length" OR "bone length")',
 'I_pth_growth_plate_histomorph': '("parathyroid hormone" OR teriparatide OR PTHrP analog*) AND ("growth plate" ) AND (histomorphometr* OR "hypertrophic zone" OR "proliferative zone" OR "cells per column")',
 'J_pth_resting_zone': '("parathyroid hormone" OR PTHrP OR teriparatide) AND ("resting zone" OR "reserve zone" OR "stem cell" ) AND (growth plate)',
}
out={}
for k,q in QUERIES.items():
    r=srch(q)
    out[k]=r
    print(k, len(r), flush=True)
    time.sleep(0.5)
json.dump(out, open('/tmp/claude-0/-home-user-growth-plate/ff8695a0-73a2-59bb-bfe0-8312b6c78a9b/scratchpad/hunt196.json','w'))
print('DONE')
