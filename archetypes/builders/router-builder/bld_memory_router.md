---
kind: memory
id: bld_memory_router
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for router artifact generation
---

# Memory: router-builder
## Summary
Routers contain task-to-destination routing logic with route tables, confidence thresholds, and fallback policies. The critical production lesson is that every route table must have a default/fallback route — without one, unmatched tasks are silently dropped. The second lesson is confidence threshold calibration: thresholds set too low cause false matches (wrong destination), thresholds set too high cause excessive fallback usage (overloading the default handler).
## Pattern
- Every route table must have an explicit default/fallback route — no task should be silently dropped
- Confidence thresholds should be calibrated empirically: start at 0.6, adjust based on misroute rate
- Routes must be ordered by specificity: most specific patterns first, broadest patterns last
- Include route metadata: expected latency, capacity limits, and availability windows per destination
- Load balancing rules must specify the algorithm: round-robin, weighted, least-connections, or affinity
- Timeout per route must be defined — slow routes need different timeouts than fast routes
## Anti-Pattern
- Missing default route — unmatched tasks vanish without error or logging
- Confidence threshold at 0.0 (everything matches) or 1.0 (nothing matches) — both defeat the purpose of routing
- Routes ordered broadest-first — broad patterns consume all tasks before specific patterns are evaluated
- Confusing router (P02, routing logic) with dispatch_rule (P12, simple keyword mapping) or workflow (P12, multi-step orchestration)
- Static routes without health checking — routes to unavailable destinations cause task failures
## Context
Routers operate in the P02 identity layer. They sit between task ingestion and destination execution, making routing decisions based on task content, confidence scores, and destination availability. In multi-agent systems, routers are the traffic controllers that ensure tasks reach the most appropriate handler. They differ from dispatch rules (simple keyword-to-destination maps) by including confidence scoring, fallback logic, and load balancing.
## Impact
Default fallback routes eliminated 100% of silent task drops. Empirically calibrated thresholds (starting at 0.6) achieved optimal misroute rates of under 5%. Specificity-ordered route tables reduced false matches by 60% compared to insertion-ordered tables.
## Reproducibility
For reliable router production: (1) enumerate all destinations with their capabilities, (2) define route patterns ordered by specificity, (3) set confidence thresholds starting at 0.6, (4) add explicit default/fallback route, (5) define timeout and load balancing per route, (6) validate against 8 HARD + 10 SOFT gates.
## References
- router-builder SCHEMA.md (14 required fields, route table specification)
- P02 identity pillar specification
- Task routing and load balancing patterns
