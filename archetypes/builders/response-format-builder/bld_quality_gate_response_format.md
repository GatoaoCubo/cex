---
id: p11_qg_response_format
kind: quality_gate
pillar: P11
title: "Gate: Response Format"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: response_format
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - response-format
  - p11
  - output-structure
  - llm
tldr: "Quality gate for LLM output structure specs: verifies format type, injection point, section definitions, and downstream parseability."
llm_function: GOVERN
---
## Definition
A response format artifact specifies the exact output structure an LLM must produce. It declares a format type (json, yaml, markdown, csv, or plaintext), an injection point where the spec is delivered to the model (system prompt or user message), and a section structure with field-level definitions. The artifact is consumed by the LLM at generation time — it is not a post-generation validator.
Scope: files with `kind: response_format`. Does not apply to validation schemas (P06), which check outputs after generation.
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p05_rf_*` | `id.startswith("p05_rf_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `response_format` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | `format_type` is one of: json, yaml, markdown, csv, plaintext | enum membership check |
| H08 | `injection_point` is one of: system_prompt, user_message | enum membership check |
| H09 | Section structure defined with at least one named section | sections table or list has >= 1 entry |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Each section has explicit field definitions (name, type, required/optional) | 1.0 |
| 3  | At least one complete example output present for the declared format | 1.0 |
| 4  | Injection point matches the use case (system for persistent structure, user for per-request) | 1.0 |
| 5  | Format is parseable by a downstream consumer without ambiguity | 1.0 |
| 6  | Tags list includes `response-format` | 0.5 |
| 7  | Scope note confirms this is for LLM generation time, not post-generation validation | 1.0 |
| 8  | Field constraints documented (max length, allowed values, nullable) | 1.0 |
| 9  | Fallback format described for partial or truncated LLM output | 0.5 |
| 10 | Format is compatible with the target model's context window and output style | 0.5 |
| 11 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 9.0. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for format design |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Format is under active negotiation with a new model provider whose output style is not yet finalized |
| approver | Domain lead must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |
| expiry | 14 days from bypass grant; format must reach full compliance once model behavior is confirmed |
