---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for optimizer
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce an optimizer

## Phase 1: RESEARCH
1. Identify the target process: what pipeline, workflow, or system is being optimized?
2. Determine the primary metric: what single number best captures process health?
3. Determine metric.direction: is lower better (minimize) or higher better (maximize)?
4. Search existing optimizers for this domain: brain_query [IF MCP] "optimizer {domain}"
5. Find the current baseline value: measure under normal operating conditions
6. Document baseline conditions: date, load level, environment, config version
7. Identify what actions are available: tune parameters, prune elements, scale capacity, replace component, restructure flow
8. Assess automation risk: can the action fire without human approval?

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints exactly
3. Set id = p11_opt_{target_slug} where slug matches ^[a-z][a-z0-9_]+$
4. Set kind = optimizer, pillar = P11, quality = null
5. Set metric.name, metric.unit, metric.direction
6. Set thresholds: if minimize then trigger < target < critical; if maximize then trigger > target > critical
7. Set action.type from enum [tune, prune, scale, replace, restructure]
8. Set action.automated = true only if risk.level = low AND rollback is instant
9. Set frequency based on how fast the metric changes (latency -> continuous, cost -> daily)
10. Write baseline with value, measured_at, conditions
11. Set improvement.current = baseline.value, improvement.target = threshold.target
12. Set cost.compute and cost.time as floats (overhead per optimization cycle)
13. Write ## Target Process section: scope, in-scope, out-of-scope boundaries
14. Write ## Metrics section: primary metric table + secondary metrics table
15. Write ## Actions section: trigger-condition rows + rollback procedure
16. Write ## Risk Assessment section: risk table + cost summary
17. Write ## Monitoring section: dashboard, alerts list, reporting cadence

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format regex, kind, pillar, quality==null, all 15 H-gates
3. HARD: threshold ordering matches metric.direction
4. SOFT: rollback defined, secondary metrics present, >= 2 alerts
5. Verify: every action trigger is numeric (no subjective conditions)
6. Verify: automated=true actions have risk.level=low
7. Verify: monitoring.alerts are specific threshold violations
8. If score < 8.0: revise before outputting
