---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of router artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: router-builder

## Golden Example

INPUT: "Create a router for dispatching tasks to CEX satellites based on domain"

OUTPUT:
```yaml
---
id: p02_router_satellite_task
kind: router
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
routes_count: 7
fallback_route: "EDISON"
confidence_threshold: 0.7
domain: "satellite_dispatch"
quality: null
tags: [router, satellite, dispatch, P02, multi-agent]
tldr: "Routes incoming tasks to 7 CEX satellites by domain pattern matching with 0.7 confidence gate"
timeout_ms: 3000
retry_count: 1
load_balance: "priority"
keywords: [satellite, dispatch, routing, task-assignment, domain-routing]
density_score: 0.88
---
```

## Routes

| Pattern | Destination | Priority | Confidence Min | Conditions |
|---------|-------------|----------|----------------|------------|
| research, scrape, competitor, market | SHAKA | 90 | 0.7 | - |
| marketing, copy, ads, listing, social | LILY | 90 | 0.7 | - |
| build, code, component, refactor, test | EDISON | 85 | 0.7 | - |
| knowledge, document, index, embed | PYTHA | 80 | 0.7 | - |
| deploy, infra, database, migrate | ATLAS | 85 | 0.8 | requires_auth |
| monetize, course, pricing, funnel | YORK | 80 | 0.7 | - |
| orchestrate, dispatch, spawn, monitor | STELLA | 95 | 0.9 | admin_only |

## Decision Logic
Algorithm: priority-first with confidence gating.
Each incoming task is scored against all route patterns simultaneously.
Only routes where confidence >= confidence_min are candidates.
Among candidates, highest priority wins. Ties broken by most specific pattern match.

## Fallback
Default destination: EDISON (general-purpose build satellite).
Trigger: no route scores above 0.7 confidence.
Behavior: route to EDISON with metadata flag `routed_by_fallback: true`.

## Escalation
Trigger: two or more routes score within 0.05 confidence of each other.
Action: return both candidates with scores; let STELLA arbitrate.
Notification: signal `p12_sig_routing_ambiguous` with candidate list.

## Integration
- Receives from: STELLA (task dispatch), user input (direct)
- Routes to: SHAKA, LILY, EDISON, PYTHA, ATLAS, YORK, STELLA
- Consults: dispatch_rules (P12) for keyword hints
- Signal on failure: `p12_sig_routing_failed`

## References
- CEX TAXONOMY_LAYERS.yaml — satellite definitions
- CEX STELLA_RULES.md — routing table reference

WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p02_router_ pattern (H02 pass) | kind: router (H04 pass)
- 19 fields present (H06 pass) | routes_count: 7 matches table (H07 pass)
- confidence_threshold: 0.7 valid (H08 pass) | fallback_route: EDISON set (H06 pass)
- tldr: 86ch (S01 pass) | tags: 5 items includes "router" (S02 pass) | density: 0.88 (S09 pass)
- Routes table 7 rows (S03 pass) | Decision Logic present (S04 pass) | No filler (S10 pass)

## Anti-Example

INPUT: "Make a router for tasks"

BAD OUTPUT:
```yaml
---
id: task_router
kind: dispatch
pillar: P12
routes_count: 1
quality: 7.5
tags: [routing]
tldr: "This router helps route various tasks to the appropriate destinations in the system."
---
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
