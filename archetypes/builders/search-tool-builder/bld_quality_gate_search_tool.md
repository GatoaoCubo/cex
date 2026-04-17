---
id: p11_qg_search_tool
kind: quality_gate
pillar: P11
title: "Gate: search_tool"
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
domain: "Web, semantic, and hybrid search tools that connect LLM agents to external search services"
quality: 9.0
tags: [quality-gate, search-tool, P04, web-search, semantic-search, provider]
tldr: "Pass/fail gate for search_tool artifacts: provider specification, max_results, result structure, cost documentation, and API key security."
density_score: 0.90
llm_function: GOVERN
---
# Gate: search_tool
## Definition
| Field | Value |
|---|---|
| metric | search_tool artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: search_tool` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p04_search_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or no p04_search_ prefix |
| H03 | ID equals filename stem | ID does not match filename |
| H04 | Kind equals literal `search_tool` | `kind: search` or `kind: tool` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `provider`, `search_type`, or `max_results` |
| H07 | Max results >= 1 | `max_results: 0` or `max_results: -1` |
| H08 | Result fields documented | No result_fields in frontmatter or body |
| H09 | No API keys in artifact | Hardcoded API key found in frontmatter or body |
| H10 | Body has required sections | Missing Overview, Query, Results, or Provider section |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Provider documentation | 1.0 | Provider name, API endpoint pattern, authentication method |
| Result field clarity | 1.0 | Each result field has type and description |
| Cost documentation | 1.0 | cost_per_query with calculation example |
| Rate limit awareness | 1.0 | rate_limit documented with throttle strategy |
| Filtering options | 0.5 | Date range, domain filter, language support documented |
| Query documentation | 1.0 | Query parameters with types, defaults, examples |
| Max results justification | 0.5 | Default apownte for use case |
| Boundary clarity | 1.0 | Explicitly not a retriever, document_loader, or browser_tool |
| Provider selection rationale | 0.5 | Why this provider for this use case |
| Domain specificity | 1.0 | Search tool optimized for declared use case |
| Security posture | 1.0 | No hardcoded secrets, env var references only |
| Error handling | 0.5 | Rate limit errors, empty results, provider unavailable |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Internal test search tool for development |
| approver | Author self-certification with test-only scope comment |
| audit_trail | Bypass note in frontmatter with expiry date |
| expiry | 14d — test tools must be promoted or removed |
| never_bypass | H01 (unparseable YAML), H05 (self-scored gates), H09 (hardcoded API keys = security risk) |
