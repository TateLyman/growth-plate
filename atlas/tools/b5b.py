import sys, yaml, os
sys.path.insert(0,'.')
from w import _B, R, q, DIR

def load(nid): return yaml.safe_load(open(os.path.join(DIR,nid+'.yaml')))
def save(nid,d):
    open(os.path.join(DIR,nid+'.yaml'),'w').write(
        yaml.dump(d,sort_keys=False,default_flow_style=False,width=92,allow_unicode=True))
    print('extended',nid)

# ---- height_heritability: append non-twin and secular-trend evidence ----
d=load('height_heritability')
d['summary']=d['summary'].rstrip()+"""

Two later designs sharpen this. Jelenkovic 2016 pooled 40 twin cohorts and 143,390 complete twin
pairs born 1886-1994 and found adult heritability of 0.69-0.84 in men and 0.53-0.78 in women with
no clear secular pattern: genetic variance trended upward across birth years but heritability did
not, and although total height variance was greatest in North America and Australia and lowest in
East Asia, the heritability proportion was similar across all three regions. That is a direct
refutation, on 143,390 pairs, of the frequently repeated claim that height heritability is lower in
populations with poor living standards and rises as conditions improve. Sidorenko 2024 provides the
non-twin cross-check that the equal-environments assumption cannot contaminate: recombination-rate-
stratified identity-by-descent sharing between 119,000 sibling pairs gives 0.76 +/- 0.05, which
sits inside the twin range and above the GREML-LDMS tagged estimate, exactly as expected if the
molecular estimate is limited by imputation of rare variants."""
d['quantitative'] += [
 q('adult height heritability, men','0.69-0.84','h2 (proportion of variance)','40 twin cohorts, 143,390 complete twin pairs born 1886-1994','human','jelenkovic2016a','range across birth-year cohorts; no secular trend detected'),
 q('adult height heritability, women','0.53-0.78','h2 (proportion of variance)','same','human','jelenkovic2016a','range across birth-year cohorts'),
 q('peak heritability of height in adolescence, boys','0.83','h2 (proportion of variance)','45 twin cohorts, 20 countries, 180,520 paired measurements ages 1-19','human','jelenkovic2016','age-specific maximum'),
 q('peak heritability of height in adolescence, girls','0.76','h2 (proportion of variance)','same','human','jelenkovic2016','age-specific maximum'),
 q('height heritability, sibling identity-by-descent design','0.76','h2 (proportion of variance)','119,000 sibling pairs, recombination-rate-stratified IBD sharing','human','sidorenko2024','SE 0.05; does not rest on the equal-environments assumption'),
]
d['key_refs'] += [
 R('jelenkovic2016','Pooled 45 twin cohorts: shared-environment variance is greatest in early childhood and heritability peaks in adolescence at 0.83 (boys) and 0.76 (girls).'),
 R('jelenkovic2016a','143,390 twin pairs born 1886-1994 show adult height heritability 0.69-0.84 (men) and 0.53-0.78 (women) with no secular trend across birth cohorts or regions.'),
 R('sidorenko2024','Recombination-stratified sibling IBD gives an unbiased height heritability of 0.76 +/- 0.05.'),
]
d['claim_grades']=[
 dict(claim='The narrow-sense heritability of adult height is approximately 0.7-0.8.',grade='A',
      basis='Twin pooling across 143,390 pairs (jelenkovic2016a) and an independent sibling IBD estimate 0.76 +/- 0.05 that does not use the equal-environments assumption (sidorenko2024).'),
 dict(claim='Height heritability rises from birth through adolescence rather than being constant.',grade='A',
      basis='Meta-analysis of 28 twin and 26 family studies (dewau2025) and pooled analysis of 45 twin cohorts with 180,520 paired measurements (jelenkovic2016), by independent groups and designs.'),
 dict(claim='Height heritability does not increase as living standards improve.',grade='A',
      basis='143,390 twin pairs across birth years 1886-1994 and three geographic-cultural regions show no secular pattern (jelenkovic2016a).'),
]
save('height_heritability',d)

# ---- missing_heritability_height ----
d=load('missing_heritability_height')
d['summary']=d['summary'].rstrip()+"""

Wainschtein 2026 closed the remaining accounting. Whole-genome sequencing of 347,630
European-ancestry UK Biobank participants, covering 40 million single-nucleotide and short indel
variants with MAF above 0.01%, captures on average about 88% of pedigree-based narrow-sense
heritability across 34 complex traits: 68% from common variants (MAF >= 1%) and 20% from rare
variants, with 79% of the rare-variant component sitting in non-coding rather than coding sequence.
Fifteen of the 34 traits showed no significant difference between WGS-based and pedigree-based
estimates at all. The gap that motivated a decade of theorising about epistasis and gene-environment
interaction was therefore mostly rare, mostly regulatory variation that genotyping arrays never
assayed - not a failure of the additive model. One residual is now well characterised rather than
merely absent: Sidorenko 2024 shows sibling linkage signals colocalise with GWAS loci and that the
heritability still unaccounted for by GWAS-identified variants is polygenic and enriched near those
same loci, implying allelic heterogeneity at known loci rather than undiscovered biology."""
d['quantitative'] += [
 q('fraction of pedigree heritability captured by whole-genome sequencing','88','%','347,630 UK Biobank European-ancestry whole genomes, 40M variants MAF>0.01%, mean across 34 traits','human','wainschtein2026','15 of 34 traits showed no significant WGS-pedigree difference'),
 q('share of pedigree heritability from common variants (MAF >= 1%)','68','%','same analysis','human','wainschtein2026','cross-trait mean'),
 q('share of pedigree heritability from rare variants (MAF < 1%)','20','%','same analysis','human','wainschtein2026','cross-trait mean'),
 q('share of rare-variant heritability that is non-coding','79','%','same analysis; coding accounts for the remaining 21%','human','wainschtein2026','cross-trait mean'),
 q('height heritability, sibling IBD design','0.76','proportion of variance','119,000 sibling pairs','human','sidorenko2024','SE 0.05'),
]
d['key_refs'] += [
 R('wainschtein2026','WGS in 347,630 individuals captures ~88% of pedigree heritability across 34 traits: 68% common, 20% rare, with 79% of the rare component non-coding.'),
 R('sidorenko2024','Residual heritability not captured by GWAS-identified loci is polygenic and enriched near those same loci, indicating allelic heterogeneity rather than unknown biology.'),
 R('hawkes2024','29 independent rare non-coding height signals with effects from -7 cm to +4.7 cm demonstrate that the missing component is reachable by sequencing.'),
]
d['claim_grades']=[
 dict(claim='The missing heritability of height is largely accounted for by rare and non-coding variation not assayed on genotyping arrays.',grade='B',
      basis='One very large WGS variance partition (wainschtein2026) plus concordant discovery of large-effect rare non-coding signals (hawkes2024); the 88% figure is a cross-trait average not independently replicated at that precision.'),
 dict(claim='Common SNP discovery for height is saturated.',grade='A',
      basis='12,111 independent SNPs capture nearly all common-SNP heritability in 5.4M individuals (yengo2022), consistent with the 68% common-variant share measured by WGS (wainschtein2026).'),
]
save('missing_heritability_height',d)
