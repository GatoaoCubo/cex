---
id: bld_memory_alert_rule
kind: entity_memory
pillar: P10
llm_function: INJECT
version: 1.0.0
quality: 8.3
tags: [alert_rule, memory, patterns]
title: "Memory Patterns: alert_rule"
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p03_sp_guardrail_builder
  - bld_architecture_guardrail
  - p10_lr_guardrail_builder
  - bld_instruction_guardrail
  - guardrail-builder
  - bld_knowledge_card_guardrail
  - bld_collaboration_guardrail
  - bld_tools_guardrail
  - p11_qg_guardrail
  - p06_security_validation_schema
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

## Memory Persistence Checklist

- Verify memory type matches taxonomy (entity, episodic, procedural, working)
- Validate retention policy aligns with data lifecycle rules
- Cross-reference with memory_scope for boundary correctness
- Check for stale entries that need decay or pruning

## Memory Pattern

```yaml
# Memory lifecycle
type: classified
retention: defined
scope: bounded
decay: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_memory_update.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_guardrail_builder]] | upstream | 0.29 |
| [[bld_architecture_guardrail]] | upstream | 0.29 |
| [[p10_lr_guardrail_builder]] | related | 0.29 |
| [[bld_instruction_guardrail]] | upstream | 0.27 |
| [[guardrail-builder]] | downstream | 0.23 |
| [[bld_knowledge_card_guardrail]] | upstream | 0.21 |
| [[bld_collaboration_guardrail]] | downstream | 0.21 |
| [[bld_tools_guardrail]] | upstream | 0.20 |
| [[p11_qg_guardrail]] | downstream | 0.20 |
| [[p06_security_validation_schema]] | upstream | 0.20 |
