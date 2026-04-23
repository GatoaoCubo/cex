---
kind: quality_gate
id: p11_qg_router
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of router artifacts
pattern: "few-shot learning \u2014 LLM reads these before producing"
quality: 9.0
title: 'Gate: Router'
version: 1.0.0
author: builder
tags:
- eval
- P11
- quality_gate
- examples
tldr: 'Quality gate for task routing logic: verifies route table completeness, confidence
  threshold, fallback reachability, and pattern uniqueness.'
domain: router
created: '2026-03-27'
updated: '2026-03-27'
density_score: 0.85
related:
  - p11_qg_quality_gate
  - bld_examples_router
  - p03_sp_router_builder
  - p03_ins_router
  - bld_knowledge_card_router
  - p11_qg_response_format
  - p11_qg_runtime_state
  - bld_memory_router
  - bld_schema_router
  - bld_architecture_router
---

## Quality Gate

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

## Examples

# Examples: router-builder
## Golden Example
INPUT: "Create a router for dispatching tasks to CEX directors based on domain"
OUTPUT:
```yaml
id: p02_router_director_task
kind: router
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
routes_count: 7
fallback_route: "builder_agent"
confidence_threshold: 0.7
domain: "director_dispatch"
quality: 8.9
tags: [router, director, dispatch, P02, multi-agent]
tldr: "Routes incoming tasks to 7 CEX directors by domain pattern matching with 0.7 confidence gate"
timeout_ms: 3000
retry_count: 1
load_balance: "priority"
keywords: [director, dispatch, routing, task-assignment, domain-routing]
density_score: 0.88
```
## Routes
| Pattern | Destination | Priority | Confidence Min | Conditions |
|---------|-------------|----------|----------------|------------|
| research, scrape, competitor, market | research_agent | 90 | 0.7 | - |
| marketing, copy, ads, listing, social | marketing_agent | 90 | 0.7 | - |
| build, code, component, refactor, test | builder_agent | 85 | 0.7 | - |
| knowledge, document, index, embed | knowledge_agent | 80 | 0.7 | - |
| deploy, infra, database, migrate | operations_agent | 85 | 0.8 | requires_auth |
| monetize, course, pricing, funnel | commercial_agent | 80 | 0.7 | - |
| orchestrate, dispatch, spawn, monitor | orchestrator | 95 | 0.9 | admin_only |
## Decision Logic
Algorithm: priority-first with confidence gating.
Each incoming task is scored against all route patterns simultaneously.
Only routes where confidence >= confidence_min are candidates.
Among candidates, highest priority wins. Ties broken by most specific pattern match.
## Fallback
Default destination: builder_agent (general-purpose build director).
Trigger: no route scores above 0.7 confidence.
Behavior: route to builder_agent with metadata flag `routed_by_fallback: true`.
## Escalation
Trigger: two or more routes score within 0.05 confidence of each other.
Action: return both candidates with scores; let orchestrator arbitrate.
Notification: signal `p12_sig_routing_ambiguous` with candidate list.
## Integration
- Receives from: orchestrator, user input
- Routes to: 7 agents (see Routes table)
- Consults: dispatch_rules (P12)
- Signal on failure: `p12_sig_routing_failed`
## References
- CEX TAXONOMY_LAYERS.yaml — director definitions
- CEX orchestrator_RULES.md — routing table reference
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p02_router_ pattern (H02 pass) | kind: router (H04 pass)
- 19 fields present (H06 pass) | routes_count: 7 matches table (H07 pass)
- confidence_threshold: 0.7 valid (H08 pass) | fallback_route: builder_agent set (H06 pass)
- tldr: 86ch (S01 pass) | tags: 5 items includes "router" (S02 pass) | density: 0.88 (S09 pass)
- Routes table 7 rows (S03 pass) | Decision Logic present (S04 pass) | No filler (S10 pass)
## Anti-Example
INPUT: "Make a router for tasks"
BAD OUTPUT:
```yaml
id: task_router
kind: dispatch
pillar: P12
routes_count: 1
quality: 7.5
tags: [routing]
tldr: "This router helps route various tasks to the apownte destinations in the system."
```
Route all tasks to the main handler. If something goes wrong, try again.
FAILURES:
1. id: no `p02_router_` prefix -> H02 FAIL
2. kind: "dispatch" not "router" -> H04 FAIL
3. pillar: "P12" not "P02" -> H06 FAIL
4. quality: 7.5 (not null) -> H05 FAIL
5. Missing fields: version, created, updated, author, fallback_route, confidence_threshold, domain -> H06 FAIL
6. routes_count: 1 but no route table in body -> H07 FAIL
7. tags: only 1 item, missing "router" -> S02 FAIL
8. tldr: 83 chars but is filler ("This router helps...") -> S10 FAIL
9. No ## Routes table in body -> S03 FAIL
10. No ## Decision Logic section -> S04 FAIL
11. No ## Fallback section with concrete destination -> S05 FAIL
12. No ## Escalation section -> S06 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
