---
id: bld_memory_alert_rule
kind: entity_memory
pillar: P10
llm_function: INJECT
version: 1.0.0
quality: 6.2
tags: [alert_rule, memory, patterns]
title: "Memory Patterns: alert_rule"
density_score: 1.0
updated: "2026-04-17"
---
# Memory Patterns: alert_rule
## What to Remember
- alert_rule GOVERNS observability (system threshold -> action)
- NOT guardrail (LLM behavior) -- completely different concern
- for_duration prevents flapping: always set >= 1m for warning, can be 0s for critical
- Severity must route to different destinations: critical=page, warning=ticket, info=log
- Every critical alert needs a runbook (link or inline steps)

## Common Mistakes
| Mistake | Correction |
|---------|-----------|
| Missing for_duration | Always set; 0s if instant, 5m typical for warning |
| Vague metric expression ("high traffic") | PromQL expression with numeric threshold |
| Conflating with guardrail | alert_rule = system metric; guardrail = LLM behavior |
| Routing all to same channel | Critical -> PD; Warning -> Slack; Info -> log |
| No runbook | Every critical alert needs remediation path |

## Cross-Kind Memory
- signal: what alert_rule evaluates (alert fires on signal threshold)
- guardrail: LLM behavior constraints (NOT alert_rule)
- quality_gate: artifact scoring gates (NOT alert_rule)
- workflow: alert_rule may trigger auto-remediation workflow

## Reuse Signals
- Check existing alert_rules: grep P09 for ar_ prefix files
- Check if Prometheus/Alertmanager config already has rules to avoid duplication
- Group related alerts by system for inhibition rules
