---
kind: examples
id: bld_examples_router
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of router artifacts
pattern: few-shot learning — LLM reads these before producing
---

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
quality: null
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
