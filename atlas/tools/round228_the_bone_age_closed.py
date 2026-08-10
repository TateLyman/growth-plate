#!/usr/bin/env python3
"""ROUND 228 - the bone-age question CLOSED, and a flat human dose-response found on the way.

CLOSED means the data does not exist, established by exhaustion rather than by
failure to look. Five routes were checked and all five are negative:

  1. TRIAL REGISTRIES  - no FGFR-inhibitor paediatric trial ever registered a
                         bone-age endpoint (round 226, five trials)
  2. THE ONE COHORT    - APEC1621B took baseline and serial physeal films by
     THAT TOOK FILMS     protocol and its only publication contains not one word
                         about them (round 227)
  3. NCTN DATA ARCHIVE - APEC1621B is NOT deposited. The public catalogue lists
                         27 trials and requires a PMID from which data are
                         available; APEC1621B has no full publication, so the
                         request route recommended in round 226 DOES NOT WORK
  4. TCIA              - 155 imaging collections, no Pediatric MATCH, no APEC1621
  5. FDA POSTMARKETING - the FDA's own five-case evaluation assessed no bone age
                         in any of the five

And the case series that closes it also quantifies a child this atlas had recorded
as unquantified, which turns the human dose-response FLAT.
"""
W = 92
def rule(c="="): print(c * W)
def head(n, t):
    print(); rule(); print(f"[{n}] {t}"); rule("-")
def wrap(s, ind=4):
    out, line = [], ""
    for w in s.split():
        if len(line) + len(w) + 1 > W - ind:
            out.append(" " * ind + line); line = w
        else:
            line = (line + " " + w).strip()
    if line: out.append(" " * ind + line)
    return "\n".join(out)

head(1, "THE FIVE ROUTES, ALL NEGATIVE - THIS IS CLOSURE BY EXHAUSTION")
rows = [
 ("trial registries", "5 paediatric FGFR trials queried against the CTG v2 API",
  "NO bone-age or skeletal-maturation outcome registered in any"),
 ("APEC1621B publication", "the only output is ASCO 2023 abstract 10007",
  "not one word about the growth plate, though films were mandated"),
 ("NCTN Data Archive", "public catalogue, 27 trials, 35,240 patients",
  "APEC1621B NOT LISTED - deposition needs a PMID and there is no full paper"),
 ("TCIA imaging archive", "155 collections queried via the NBIA API",
  "no Pediatric MATCH, no APEC1621, no COG FGFR collection"),
 ("FDA postmarketing", "nadeaunguyen2026, the agency's own five-case evaluation",
  "NO BONE AGE ASSESSED OR REPORTED IN ANY OF THE FIVE"),
]
for a, b, c in rows:
    print(f"    {a:<24s} {b}")
    print(f"    {'':<24s}   -> {c}")
print()
print(wrap(
    "AND ROUND 226's RECOMMENDATION HAS TO BE WITHDRAWN. It named the NCTN Data Archive request as the "
    "one route that would get the films. The catalogue shows deposition follows FULL PUBLICATION - every "
    "listed trial carries a PMID from which data are available - and APEC1621B has none. THE REQUEST "
    "ROUTE DOES NOT WORK UNTIL SOMEBODY PUBLISHES THE TRIAL."))

head(2, "THE FIVE CASES, AND THE ONE THE ATLAS HAD ONLY AS AN ADJECTIVE")
print("    FDA Office of Surveillance and Epidemiology, five postmarketing cases, all from the")
print("    literature, three also in FAERS:")
print()
cases = [
 ("1", "13 M", "astrocytoma", "SCFE", "84 d", "obesity; surgery"),
 ("2", "13 M", "glioma", "SCFE", "137 d", "obesity; surgery"),
 ("3", "15 M", "astrocytoma", "ACCELERATED GROWTH 14.3 cm / 9 mo", "274 d", "kyphoscoliosis; surgery"),
 ("4", "13 M", "glioma", "ACCELERATED GROWTH 9.8 cm / 6 mo", "183 d", "ON GROWTH HORMONE; testosterone mgmt"),
 ("5", "10 F", "ependymoma", "accelerated growth", "120 d", "growth chart"),
]
print(f"    {'#':<3}{'age/sex':<9}{'tumour':<14}{'event':<36}{'onset':<8}notes")
for c in cases:
    print(f"    {c[0]:<3}{c[1]:<9}{c[2]:<14}{c[3]:<36}{c[4]:<8}{c[5]}")
print()
print("    median onset 137 days, range 84-274. ALL FIVE DISCONTINUED. THREE REQUIRED SURGERY.")
print()
print(wrap(
    "CASE 3 IS erdachild2024. CASE 5 IS raimann2024 PATIENT 2. AND CASE 4 IS raimann2024 PATIENT 1, "
    "WHOSE VELOCITY THE PAPER LEFT AS 'A DRAMATIC GROWTH SPURT' AND WHICH CORR-226 RECORDED AS NOT "
    "QUANTIFIED. THE FDA QUANTIFIES IT: 9.8 cm OVER 6 MONTHS."))

head(3, "AND THAT MAKES THE HUMAN DOSE-RESPONSE FLAT")
pts = [
 ("raimann2024 patient 1 (FDA case 4)", "5 then 3 mg", 9.8, 6.0, "ON GROWTH HORMONE, hypogonadotropic"),
 ("erdachild2024 (FDA case 3)", "7 then 5 mg", 14.3, 9.0, "Tanner 2-3, normal GH and IGF-1"),
]
print(f"    {'child':<38}{'dose':<14}{'gain':<12}{'annualised':<12}context")
for n, d, cm, mo, ctx in pts:
    print(f"    {n:<38}{d:<14}{f'{cm} cm/{mo:.0f} mo':<12}{cm*12/mo:>6.1f} cm/y   {ctx}")
print()
print(wrap(
    "TWO CHILDREN, DOSES DIFFERING ROUGHLY TWOFOLD, AND THE SAME ANNUALISED VELOCITY TO WITHIN THREE PER "
    "CENT. Rounds 216 to 218 built a dose-response curve across 3 to 9 mg on the premise that more "
    "exposure buys more growth. CORR-226 showed the curve could not be identified because its lower "
    "anchor spliced two patients. THIS IS WORSE FOR THE PREMISE AND BETTER FOR THE EVIDENCE - the anchor "
    "is now unspliced, and what it shows is NO DOSE-RESPONSE AT ALL ACROSS 3 TO 7 mg."))
print()
print(wrap(
    "THE CONFOUND IS REAL AND IT CUTS BOTH WAYS. Case 4 was ON GROWTH HORMONE and hypogonadotropic; case "
    "3 was not on growth hormone and had normal growth-axis hormones. So the flat comparison is "
    "GH-plus-low-dose against erdafitinib-alone-at-higher-dose. EITHER the erdafitinib dose-response is "
    "flat in this range, OR growth hormone substituted for the missing 2 to 4 mg. Both readings matter "
    "for this stack, which contains both agents, and NEITHER supports the round-217 premise that the way "
    "up is more erdafitinib."))

head(4, "WHAT THE THIRD CHILD DOES TO THE PICTURE")
print(wrap(
    "raimann2024 patient 2 - FDA case 5 - is the 10-year-old girl with ependymoma who grew at 10 cm/year, "
    "and her dose is stated NOWHERE, not in the paper and not in the FDA series. She is prepubertal at "
    "10.9 years, so a 10 cm/year velocity is high but not extraordinary. THE THREE CHILDREN WITH "
    "QUANTIFIED GROWTH SIT AT 19.6, 19.1 AND 10 cm/YEAR, AND THE ONLY ONE BELOW 19 IS THE ONLY ONE WHOSE "
    "DOSE IS UNKNOWN."))
print()
print(wrap(
    "AND TWO OF THE FIVE DID NOT GROW AT ALL - cases 1 and 2 presented with SLIPPED EPIPHYSES at 84 and "
    "137 days, both obese, both requiring surgery, with no growth acceleration recorded. Together with "
    "brizini2024, that is THREE CHILDREN IN WHOM THE PHYSIS FAILED MECHANICALLY WITHOUT THE HEIGHT "
    "MOVING. Round 227 read that as evidence for arrested remodelling over preserved reserve; the FDA "
    "series adds two more instances of the same dissociation."))

head(5, "THE QUESTION IS CLOSED AND WHAT REPLACES IT")
for line in [
 "CLOSED - there is no on-treatment bone age under an FGFR inhibitor anywhere in the public",
 "  record. Five independent routes, all negative. This is exhaustion, not failure to look.",
 "",
 "AND THE CLOSURE IS ITSELF INFORMATIVE. The FDA reviewed every postmarketing case of skeletal",
 "  toxicity on this drug and NOBODY MEASURED A BONE AGE - not the treating teams, not the case",
 "  authors, not the agency. In a drug whose signature toxicity is accelerated growth and",
 "  slipped epiphyses, the single measurement that would say whether the growth is bought or",
 "  borrowed was never taken by anyone.",
 "",
 "WHAT REPLACES IT AS THE LIVE QUESTION is round 227's - whether the physeal widening is",
 "  preserved reserve or arrested remodelling - because that CAN be answered from data that",
 "  exists, and because five of five FDA cases and brizini2024 now bear on it.",
]:
    print("    " + line if line else "")
rule()
