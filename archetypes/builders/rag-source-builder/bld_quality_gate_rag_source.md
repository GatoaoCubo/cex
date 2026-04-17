---
id: p11_qg_rag_source
kind: quality_gate
pillar: P11
title: "Gate: RAG Source"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: rag_source
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - rag-source
  - p11
  - indexing
  - freshness
tldr: "Quality gate for external source pointers: verifies URL format, domain class, freshness policy, and pointer-only body constraint."
llm_function: GOVERN
---
## Definition
A RAG source artifact is a pointer to an external, indexable resource. It contains a validated URL, a domain classification, a last-checked date, and a freshness policy specifying how often the source should be re-validated. The body must remain a pointer — it must not contain extracted content from the source.
Scope: files with `kind: rag_source`. Does not apply to knowledge cards (P04), which contain extracted and synthesized content.
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p01_rs_*` | `id.startswith("p01_rs_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `rag_source` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr, url, last_checked all present |
| H07 | `url` field value starts with `https://` or `http://` | `url.startswith(("https://", "http://"))` |
| H08 | `last_checked` field is a valid ISO date (YYYY-MM-DD) | `datetime.strptime(last_checked, "%Y-%m-%d")` raises no error |
| H09 | Total file size is <= 1024 bytes (pointer only, no extracted content) | `os.path.getsize(file) <= 1024` |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Freshness policy present with an explicit re-check schedule (e.g. every 30 days) | 1.0 |
| 3  | Reliability rating assigned (high / medium / low) with brief rationale | 1.0 |
| 4  | Format classified as one of: html, json, api, pdf, csv | 1.0 |
| 5  | Staleness condition explicit (what event or age triggers a re-check) | 1.0 |
| 6  | Tags list includes `rag-source` | 0.5 |
| 7  | Body contains no extracted paragraphs or quoted content from the source | 1.0 |
| 8  | Source accessibility pre-validated (URL returned 2xx at last_checked date) | 1.0 |
| 9  | Crawl schedule is realistic for the source's update frequency | 0.5 |
| 10 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 8.5. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; include in primary index rotation |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready for indexing pipeline |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; pointer must be corrected before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Source is internal (intranet or private API) where public accessibility check cannot apply |
| approver | Domain lead must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |
| expiry | 60 days from bypass grant; source must be re-validated or retired |
H01 (YAML parses) and H05 (quality is null) may never be bypassed under any circumstance. Bypassing H09 (size limit) is never permitted — body content belongs in a knowledge card, not a source pointer.
