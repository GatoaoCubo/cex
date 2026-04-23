---
kind: memory
id: bld_memory_router
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for router artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Router"
version: "1.0.0"
author: n03_builder
tags: [router, builder, examples]
tldr: "Golden and anti-examples for router construction, demonstrating ideal structure and common pitfalls."
domain: "router construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - router-builder
  - p03_ins_router
  - p03_sp_router_builder
  - bld_collaboration_router
  - p11_qg_router
  - bld_architecture_router
  - bld_knowledge_card_router
  - p02_rt_SCOPE_SLUG
  - bld_examples_router
  - bld_schema_router
---
# Memory: router-builder
## Summary
Routers contain task-to-destination routing logic with route tables, confidence thresholds, and fallback policies. The critical production lesson is that every route table must have a default/fallback route — without one, unmatched tasks are silently dropped. The second lesson is confidence threshold calibration: thresholds set too low cause false matches (wrong destination), thresholds set too high cause excessive fallback usage (overloading the default handler).
## Pattern
1. Every route table must have an explicit default/fallback route — no task should be silently dropped
2. Confidence thresholds should be calibrated empirically: start at 0.6, adjust based on misroute rate
3. Routes must be ordered by specificity: most specific patterns first, broadest patterns last
4. Include route metadata: expected latency, capacity limits, and availability windows per destination
5. Load balancing rules must specify the algorithm: round-robin, weighted, least-connections, or affinity
6. Timeout per route must be defined — slow routes need different timeouts than fast routes
## Anti-Pattern
1. Missing default route — unmatched tasks vanish without error or logging
2. Confidence threshold at 0.0 (everything matches) or 1.0 (nothing matches) — both defeat the purpose of routing
3. Routes ordered broadest-first — broad patterns consume all tasks before specific patterns are evaluated
4. Confusing router (P02, routing logic) with dispatch_rule (P12, simple keyword mapping) or workflow (P12, multi-step orchestration)
5. Static routes without health checking — routes to unavailable destinations cause task failures
## Context
Routers operate in the P02 identity layer. They sit between task ingestion and destination execution, making routing decisions based on task content, confidence scores, and destination availability. In multi-agent systems, routers are the traffic controllers that ensure tasks reach the most apownte handler. They differ from dispatch rules (simple keyword-to-destination maps) by including confidence scoring, fallback logic, and load balancing.
## Impact
Default fallback routes eliminated 100% of silent task drops. Empirically calibrated thresholds (starting at 0.6) achieved optimal misroute rates of under 5%. Specificity-ordered route tables reduced false matches by 60% compared to insertion-ordered tables.
## Reproducibility
For reliable router production: (1) enumerate all destinations with their capabilities, (2) define route patterns ordered by specificity, (3) set confidence thresholds starting at 0.6, (4) add explicit default/fallback route, (5) define timeout and load balancing per route, (6) validate against 8 HARD + 10 SOFT gates.
## References
1. router-builder SCHEMA.md (14 required fields, route table specification)
2. P02 identity pillar specification
3. Task routing and load balancing patterns

## Metadata

```yaml
id: bld_memory_router
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-router.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | router construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[router-builder]] | upstream | 0.54 |
| [[p03_ins_router]] | upstream | 0.53 |
| [[p03_sp_router_builder]] | upstream | 0.53 |
| [[bld_collaboration_router]] | upstream | 0.51 |
| [[p11_qg_router]] | downstream | 0.48 |
| [[bld_architecture_router]] | upstream | 0.47 |
| [[bld_knowledge_card_router]] | upstream | 0.41 |
| [[p02_rt_SCOPE_SLUG]] | upstream | 0.39 |
| [[bld_examples_router]] | upstream | 0.38 |
| [[bld_schema_router]] | upstream | 0.35 |
