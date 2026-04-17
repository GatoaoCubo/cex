---
id: bld_instruction_slo_definition
kind: instruction
pillar: P09
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
title: "SLO Definition Builder Instructions"
target: "slo-definition-builder agent"
phases_count: 4
prerequisites:
  - "Service or agent is identified"
  - "SLI metric type is known (availability, latency, throughput, error rate)"
  - "Measurement window is defined (rolling 30d, calendar month)"
quality: null
tags: [instruction, slo_definition, P09, reliability]
llm_function: REASON
tldr: "Build an slo_definition with SLI metric, target threshold, error budget, and alerting policy."
density_score: null
---
## Context
The slo-definition-builder produces an `slo_definition` artifact -- a structured specification of a measurable reliability target. NOT enterprise_sla (contractual SLA with external parties), NOT quality_gate (build-time artifact scoring), NOT benchmark (point-in-time performance measurement).

**Input contract**:
- `service_name`: string -- the service or agent being governed
- `sli_type`: enum -- availability | latency | error_rate | throughput | saturation
- `sli_metric`: string -- the specific metric query (e.g. Prometheus PromQL)
- `target_percent`: float -- target (e.g. 99.9 for 99.9%)
- `window_days`: integer -- rolling window (e.g. 30)
- `error_budget_policy`: enum -- block_deploy | alert_only | auto_rollback

## Phases

### Phase 1: Define the SLI
Identify the Service Level Indicator:
- What is being measured? (availability, p99 latency, error rate, etc.)
- How is it measured? (metric query, synthetic probe, log-based)
- What is the denominator? (total requests, total time, etc.)

### Phase 2: Set the Target
- target_percent: the % threshold that defines "good"
- window_days: the rolling window over which the SLO is measured
- Derive: error_budget_minutes = (1 - target/100) * window_days * 24 * 60

### Phase 3: Error Budget Policy
Define what happens when the error budget is consumed:
- burn_rate_threshold_1h: fast burn alert (e.g. 14x)
- burn_rate_threshold_6h: slow burn alert (e.g. 6x)
- error_budget_policy: block_deploy | alert_only | auto_rollback
- owner: team or nucleus responsible

### Phase 4: Compose Artifact
Required frontmatter: id, kind, pillar, service_name, sli_type, target_percent, window_days, error_budget_minutes, quality: null.
Required body sections: SLI Definition, Target, Error Budget, Alerting Policy.
