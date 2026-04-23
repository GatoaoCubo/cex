---
kind: quality_gate
id: p11_qg_rag_source
pillar: P11
llm_function: GOVERN
version: 1.0.0
quality: 9.0
title: 'Gate: RAG Source'
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: 'Quality gate for external source pointers: verifies URL format, domain class,
  freshness policy, and pointer-only body constraint.'
domain: rag_source
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - p11_qg_quality_gate
  - p03_ins_rag_source
  - bld_knowledge_card_rag_source
  - p11_qg_response_format
  - bld_schema_rag_source
  - bld_examples_rag_source
  - bld_memory_rag_source
  - p11_qg_creation_artifacts
  - p11_qg_prompt_template
  - p11_qg_runtime_state
---

## Quality Gate

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

## Examples

# Examples: rag_source
## Golden Example
**Artifact**: p01_rs_anthropic_claude_api_docs
```yaml
id: p01_rs_anthropic_claude_api_docs
kind: rag_source
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: builder
url: "https://docs.anthropic.com/en/api/getting-started"
domain: llm_providers
last_checked: "2026-03-26"
quality: 8.9
tags: [rag-source, llm_providers, html]
tldr: "Official Anthropic Claude API reference covering authentication, models, messages API, and rate limits."
keywords: [anthropic, claude, api, llm, documentation]
reliability: high
format: html
extraction_method: crawl
## Source Description
Official Anthropic developer documentation covering the Claude API. Maintained by Anthropic engineering. Includes authentication patterns, model capabilities, messages endpoint reference, tool use, and rate limit policies.
## Freshness Policy
- Re-check interval: 30 days
- Staleness threshold: 60 days
- Trigger: on Claude model release or API version bump
- Last verified: 2026-03-26
## Extraction Notes
- Method: crawl
- Format: html
- Auth required: no (public docs)
- Known quirks: versioned paths change on major releases — track /en/api/ root
## References
- Parent domain: llm_providers
- Related sources: none
```
### Why This Is Golden
| Gate | Status | Reason |
|------|--------|--------|
| H01 | PASS | YAML parses cleanly |
| H02 | PASS | id matches ^p01_rs_[a-z][a-z0-9_]+$ |
| H03 | PASS | id == filename stem |
| H04 | PASS | kind == rag_source |
| H05 | PASS | quality == null |
| H06 | PASS | all 5 required fields present |
| H07 | PASS | body <= 1024 bytes |
| S01 | PASS | tldr <= 160 chars |
| S03 | PASS | URL is valid https:// |
| S06 | PASS | no content body — pointer only |
## Anti-Example
**Artifact**: p01_rs_bad_source (DO NOT PRODUCE THIS)
```yaml
id: rs_anthropic_docs
kind: rag_source
pillar: P01
url: docs.anthropic.com
last_checked: today
quality: 8.5
tags: [source]
## Content
The Anthropic API uses bearer token authentication. You pass the API key as a header:
Authorization: Bearer sk-ant-...
The messages endpoint accepts a JSON body with model, max_tokens, and messages array.
Each message has role (user or assistant) and content (string or array)...
[continues for 800 more bytes of extracted API documentation]
```
### Why This Fails
| Gate | Status | Failure |
|------|--------|---------|
| H01 | FAIL | Missing required fields — YAML incomplete |
| H02 | FAIL | id "rs_anthropic_docs" missing p01_ prefix |
| H04 | PASS | kind correct |
| H05 | FAIL | quality == 8.5 — never self-score |
| H06 | FAIL | domain field missing |
| H07 | FAIL | body > 1024 bytes |
| S03 | FAIL | URL missing https:// scheme |
| S06 | FAIL | body contains extracted content — this is a knowledge_card, not a rag_source |
**Root cause**: Author confused rag_source (pointer) with knowledge_card (content). The extracted API documentation belongs in a knowledge_card, not in a rag_source body.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
