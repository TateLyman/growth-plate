"""Does HETEROZYGOUS Tet1 loss lengthen bone? IMPC systematic phenotyping.
The 'Tet1 mice are smaller' threat is a HOMOZYGOUS claim; the human evidence is
HETEROZYGOUS. IMPC has the het, measured blind, by DXA, with weight in the model."""
import json,math,urllib.request
U=("https://www.ebi.ac.uk/mi/impc/solr/statistical-result/select"
   "?q=marker_symbol:Tet1&rows=400&wt=json")
d=json.load(urllib.request.urlopen(U))['response']['docs']
MSK=['body length','bone mineral','fat mass','lean mass','grip strength','bone area',
     'bmc','fat/body','bmc/body','body weight','tibia','femur','bone']
seen=set(); tested=[]
for x in d:
    if x.get('status')!='Successful': continue
    pm=x.get('male_ko_effect_p_value'); n=x.get('parameter_name')
    if pm is None or n is None: continue
    k=(n,x.get('zygosity'))
    if k in seen: continue
    seen.add(k)
    tested.append((n,float(pm),any(m in n.lower() for m in MSK),x.get('effect_size'),x.get('zygosity')))
N=len(tested); K=sum(1 for t in tested if t[2])
hits=[t for t in tested if t[1]<0.05]; k=len(hits); kmsk=sum(1 for t in hits if t[2])
print("Tet1 IMPC male-effect tests: %d (musculoskeletal %d = %.1f%%)"%(N,K,100*K/N))
for n,p,m,e,z in sorted(hits,key=lambda x:x[1]):
    print("  %-46s %-13s eff=%-8s p=%.4g  %s"%(n[:46],z,('%.3f'%e) if e is not None else '-',p,"MSK" if m else "other"))
C=math.comb
pe=sum(C(K,i)*C(N-K,k-i) for i in range(kmsk,min(k,K)+1))/C(N,k)
print("\nhits %d, of which MSK %d, expected %.2f  ->  HYPERGEOMETRIC P = %.4g"%(k,kmsk,k*K/N,pe))
