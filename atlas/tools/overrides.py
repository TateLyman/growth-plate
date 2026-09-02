# Manual corrections applied after reading the extracted snippets for every ref the
# automated pass assigned a sex to. Each entry was checked against the source text.
SEX_OVERRIDE = {
    # extractor read a background/comparison sentence, not the study subjects
    "bethlehem2022": "both", "guevel2026": "both", "huckert2015": "both",
    "kamrulhasan2026": "both", "ni2026": "both", "savarirayan2026": "both",
    "yuen2026": "both", "zhu2010": "both", "cao2026": "both", "kochar2025": "both",
    "li2025": "both", "martn2026": "both", "victora2008": "both",
    "giannopoulou2024": "both", "yadav2011": "both", "hppner2025": "both",
    "gevers1996": "both", "rubin2024": "both", "seminara2003": "both",
    # single-sex studies the extractor over-called as mixed
    "kodama2025": "female", "hua2025": "male", "yu2025": "male", "sivaraj2022": "male",
    # reviews whose sex words describe cited work, not an experiment
    "ursachi2026": None,
}
# Reviews/meta-analyses only keep a sex if the TITLE names one.
REVIEW_TYPES = {"review", "systematic_review", "meta_analysis", "narrative_review"}
