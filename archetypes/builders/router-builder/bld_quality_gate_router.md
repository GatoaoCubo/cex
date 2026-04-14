---
id: p11_qg_router
kind: quality_gate
pillar: P11
title: "Gate: Router"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: router
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - router
  - p11
  - task-routing
  - dispatch
tldr: "Quality gate for task routing logic: verifies route table completeness, confidence threshold, fallback reachability, and pattern uniqueness."
llm_function: GOVERN
---
## Definition
A router artifact maps incoming task patterns to destination agents or workers using a route table, a confidence threshold, and a guaranteed fallback. It specifies priority ordering when multiple routes could match, escalation behavior for low-confidence cases, and timeout policies per route. Every route must have a unique pattern — overlapping patterns produce unpredictable dispatch behavior.
Scope: files with `kind: router`. Does not apply to dispatch rules (P02 sub-kind) or lifecycle rules (P09), which govern behavior after routing.
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p02_router_*` | `id.startswith("p02_router_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `router` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | Route table present with >= 3 routes, each having pattern and destination | count rows >= 3; each row has both columns non-empty |
| H08 | `confidence_threshold` field present and value is between 0.0 and 1.0 inclusive | float range check |
| H09 | Fallback route declared and points to a named destination (not empty or null) | `fallback_route` field is non-empty string |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Every route has a pattern, destination, and confidence floor documented | 1.0 |
| 3  | Confidence threshold value is justified with a rationale comment | 1.0 |
| 4  | Fallback route is always reachable regardless of input (no conditional fallback) | 1.0 |
| 5  | Load balancing strategy documented if multiple destinations share a pattern | 0.5 |
| 6  | Tags list includes `router` | 0.5 |
| 7  | Timeout policy defined per route or as a global default | 1.0 |
| 8  | Escalation path documented for cases below confidence threshold | 1.0 |
| 9  | Priority ordering documented when multiple routes could match the same input | 1.0 |
| 10 | No two routes share an overlapping pattern (checked by author) | 1.0 |
| 11 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 9.5. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for routing design |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Router covers a domain with fewer than 3 known patterns at design time (bootstrapping phase) |
| approver | Domain lead must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |
| expiry | 21 days from bypass grant; route table must reach >= 3 routes before expiry |
