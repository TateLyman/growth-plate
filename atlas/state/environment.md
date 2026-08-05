# Environment — what works, what is blocked

Probed 2026-08-05. Re-probe at the start of every session; append, do not overwrite.

## Network access — CONFIRMED WORKING

| Endpoint | Status | Use |
|---|---|---|
| `eutils.ncbi.nlm.nih.gov` (E-utilities) | **200** | ESearch/ESummary/EFetch — PMID resolution, pubtype/retraction flags |
| `www.ebi.ac.uk/europepmc/webservices/rest` | **200** | Primary literature search, DOI→record, full-text availability, citation counts |
| `doi.org` | **302** (resolves) | DOI validation |
| `clinicaltrials.gov/api/v2` | **200** | L12 trial records + posted results |
| WebSearch / WebFetch tools | available | grey literature, regulatory docs, dataset portals |

This is the single most important environmental fact: **the atlas can verify its own
citations programmatically.** Every reference is machine-populated from the live
record rather than typed from memory (`tools/addref.py`), and every reference is
re-resolved against NCBI/EPMC with author+year cross-check (`tools/verify_refs.py`).
A fabricated PMID cannot enter the bibliography — verified by negative test.

## Toolchain — verified end-to-end 2026-08-05

- `tools/addref.py` — accepted PMID 30356214 and DOI 10.1038/s41586-018-0662-5 with
  correct resolved metadata; **refused** fabricated PMID 99999999.
- `tools/validate.py` — caught 10/10 deliberately injected defects (bad node type,
  bad confidence grade, ghost ref_id, dangling edge endpoints, bad relation, bad
  evidence tier, missing refs, hypothesized_link without gap_id, wrong confidence
  on hypothesized_link).
- `tools/verify_refs.py` — resolved 1/1 refs, 0 mismatches, retraction check active.

## Local tooling

Python 3.11.15 · PyYAML 6.0.1 · requests 2.33.1 · pandas availability: see below.

## Known limits / routes around them

- **Publisher full text is generally not fetchable** (Elsevier/Wiley/Springer paywalls).
  Route: Europe PMC open-access subset first (`inEPMC`/`isOpenAccess` flags are stored
  on every ref by `addref.py`), then PMC, then escalate to the user via
  `sources/access_queue.md`. Never bypass a paywall.
- Reading a figure panel is often impossible without the PDF. When only the abstract
  was read, the ref must be typed `primary_abstract_only` — this is enforced by
  vocabulary, and it is the honest failure mode, not a silent one.
- NCBI rate limit without an API key ≈3 req/s; `addref.py`/`verify_refs.py` sleep 0.2–0.34 s.

## Log

- 2026-08-05 — initial probe; all four endpoints live; toolchain built and negative-tested.
