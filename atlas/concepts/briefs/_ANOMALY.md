# ANOMALY HUNT — shared brief (R439)

You are hunting **ANOMALIES**, not building an enumeration. A previous round already enumerated
2,193 concepts across 21 domains. This is a different job and the difference matters.

## WHAT AN ANOMALY IS

An observation that is (a) **reproducible or large**, (b) **about height, longitudinal bone growth,
or body size in humans or mammals**, and (c) **has no accepted mechanism, or has an explanation the
field itself disputes, or was measured and then filed under the wrong question.**

The round that produced this brief found one by accident and it is the template. A 1984 paper ran
flow cytometry on the growing rat growth plate and reported **binuclear and mononuclear tetraploid
chondrocytes**. The author interpreted it as a by-product of rapid proliferation and it was never
followed up. Nobody has asked whether **ploidy sets terminal chondrocyte volume** — which is what
endoreduplication does in hepatocyte, megakaryocyte, trophoblast and cardiomyocyte, and terminal
cell volume is the largest single term in longitudinal bone growth. **The observation existed. The
question was never asked.** That is what you are looking for.

## THE FOUR SHAPES WORTH FINDING, IN ORDER

1. **MEASURED AND MISFILED.** A real result whose stated interpretation forecloses a bigger question.
   Old papers, non-English journals, methods sections, negative-result papers, control arms.
2. **LARGE AND UNEXPLAINED.** A magnitude the field accepts and cannot account for mechanistically.
3. **CONTESTED.** The field has two or more named hypotheses and no resolution. Say who holds which.
4. **THE DOG THAT DID NOT BARK.** Something that should be true given the accepted model and is not,
   or an experiment that is obvious, cheap and has never been done.

## WHAT IS *NOT* AN ANOMALY — do not report these

- A disease that makes people short. There are ~1,500 and they are already mapped.
- A gene with a height association and no mechanism. Already have 207 with signed effect sizes.
- A drug that damages growth. Useful only if the *mechanism* is unexplained.
- A review saying "the mechanism remains unclear". Find the primary measurement it is referring to.

## HARD RULES

- **NEVER invent a citation, author, year, journal or number.** If you are not certain of a PMID,
  write `PMID unverified` and give the title and first author. A fabricated identifier is worse than
  a missing one and will be caught.
- **Every claim carries its species and, for animal work, the developmental stage.**
- **Reviews are an index, not a source.** Cite the primary. If you only have the review, say so.
- **Prefer measurements to opinions.** A number with an n and a p is worth ten mechanisms.
- **Paraphrase. Do not reproduce article text.** Short quotes only where exact wording carries the
  claim, under fifteen words, one per source.
- **Search the whole internet**, not just PubMed: Europe PMC, Google Scholar, regulatory documents,
  theses, conference abstracts, non-English literature, historical/archived journals, preprints.
- **Do not read the repository you are running inside.** Your value is that you do not already know
  what it contains. Work from the outside literature only.

## OUTPUT FORMAT

A markdown table, then prose for the best three rows.

| # | ANOMALY (one line) | SHAPE (1-4) | MAGNITUDE | SPECIES | WHAT IS ACTUALLY MEASURED | ACCEPTED EXPLANATION | WHY IT IS WEAK / WHAT WAS NEVER ASKED | PMID or source | CONFIDENCE |

Then, for your three strongest rows, 150–250 words each: what exactly was measured, by whom, in
what system, what the authors concluded, and **precisely which question their interpretation
foreclosed**. Name the experiment that would settle it.

Aim for **25–60 rows**. Depth beats breadth — a row that is merely surprising is not an anomaly.
End with a short section: **"THINGS I EXPECTED TO FIND AND DID NOT"**, which is a real result.
