---
kind: examples
id: bld_examples_optimizer
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of optimizer artifacts
---

# Examples: optimizer-builder
## Golden Example
INPUT: "Crie optimizer para latency de geraction de knowledge cards"
OUTPUT:
```yaml
id: p11_opt_kc_generation_latency
kind: optimizer
pillar: P11
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "system"
domain: "knowledge_card_pipeline"
quality: null
tags: [optimizer, knowledge-card, latency, continuous]
tldr: "Optimize KC generation latency via batch/model tuning; trigger 3s, target 1.5s, critical 8s"
density_score: 0.91
target: "KC pipeline: embed -> retrieve -> generate -> validate"
metric:
  name: "p99_generation_latency"
  unit: "seconds"
  direction: "minimize"
action:
  type: "tune"
  description: "Reduce batch_size or switch model tier when p99 exceeds trigger"
  automated: true
threshold:
  trigger: 3.0
  target: 1.5
  critical: 8.0
frequency: "continuous"
baseline:
  value: 4.2
  measured_at: "2026-03-20"
  conditions: "50 req/min, GPT-4o, batch_size=32, Railway prod"
improvement:
  current: 4.2
  target: 1.5
  history:
    - date: "2026-03-20"
      value: 4.2
cost:
  compute: 0.05
  time: 0.8
  risk: "low — tune reversible, rollback restores batch_size in 1 cycle"
risk:
  level: "low"
  mitigation: "Rollback restores batch_size; circuit breaker halts at action_fire_rate > 10/hour"
monitoring:
  dashboard: "railway-metrics/kc-pipeline-latency"
  alerts:
    - "p99 > 3.0s for 3 consecutive minutes"
    - "p99 > 8.0s (critical — page on-call)"
  reporting: "daily: p99/p95/p50 + action count + delta vs baseline"
## Target Process
Scope: KC generation from raw input to validated artifact.
In scope: embed, vector retrieve, LLM generate, YAML validate.
Out of scope: upstream ingestion, pool merge, user-facing API.
## Metrics
| Metric | Unit | Direction | Trigger | Target | Critical |
|--------|------|-----------|---------|--------|----------|
| p99_generation_latency | seconds | minimize | 3.0 | 1.5 | 8.0 |
### Secondary Metrics
| Metric | Unit | Purpose |
|--------|------|---------|
| action_fire_rate | actions/hour | Detect thrashing |
| validation_pass_rate | percent | Ensure quality not degraded by speed |
## Actions
| Trigger Condition | Type | Description | Automated |
|-------------------|------|-------------|-----------|
| p99 > 3.0s for 3 min | tune | Reduce batch_size 32->16 | Yes |
| p99 > 5.0s for 5 min | tune | Switch to faster model tier | Yes |
| p99 > 8.0s (critical) | scale | Add replica + page on-call | No |
### Rollback
Thrash guard: freeze config 30min if action_fire_rate > 10/hour.
Manual: `kc-pipeline config restore --version previous`
## Risk Assessment
| Risk | Level | Mitigation |
|------|-------|-----------|
| Quality regression | low | validation_pass_rate alert < 95% |
| Thrashing | medium | circuit breaker at 10 actions/hour |
Cost: compute=0.05, time=0.8s/cycle
## Monitoring
- Dashboard: railway-metrics/kc-pipeline-latency
- Alerts: p99 > 3.0s/3min (warn), p99 > 8.0s (critical)
- Reporting: daily, latency percentiles + action log
```
## Anti-Example
```yaml
id: kc_optimizer
kind: optimizer
title: "Make KC generation fast"
quality: 8.5
Check if KC generation is slow. If it is, do something to speed it up.
Maybe reduce batch size or use a faster model. Monitor and adjust as needed.
```
FAILURES:
1. [H02] id missing p11_opt_ prefix — fails ^p11_opt_[a-z][a-z0-9_]+$
2. [H06] quality: 8.5 — must be null; self-scoring forbidden
3. [H05] pillar field missing — required literal "P11"
4. [H07] target field missing — no process scope defined
5. [H08] metric object missing — no name, unit, direction
6. [H10] threshold object missing — no trigger/target/critical
7. [H14] improvement object missing — no current/target/history
8. [H15] all 5 body sections absent — Target Process, Metrics, Actions, Risk Assessment, Monitoring
9. [S05] no rollback — "do something" is not a rollback procedure
10. [S06] "if slow" / "as needed" — subjective triggers, no numeric conditions
