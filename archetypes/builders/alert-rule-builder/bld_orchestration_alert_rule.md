---
id: bld_rules_alert_rule
kind: guardrail
pillar: P11
llm_function: COLLABORATE
version: 1.0.0
quality: 7.7
tags: [alert_rule, rules, guardrail]
title: "Rules: alert_rule Builder"
author: builder
tldr: "Alert Rule feedback: workflow coordination, handoffs, and lifecycle management"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p03_sp_guardrail_builder
  - p03_sp_validator-builder
  - p03_sp_system-prompt-builder
  - p03_sp_context_window_config_builder
  - p03_sp_kind_builder
  - p03_sp_quality_gate_builder
  - p03_sp_type-def-builder
  - p03_sp_optimizer_builder
  - p03_sp_few_shot_example_builder
  - p03_sp_validation-schema-builder
---
# Builder Rules: alert_rule
## ALWAYS
- ALWAYS include a numeric threshold in metric_expression
- ALWAYS set for_duration (prevents flapping; 0s valid for critical)
- ALWAYS align routing with severity (critical -> page; warning -> ticket)
- ALWAYS provide runbook_url or remediation_steps for critical alerts
- ALWAYS set quality: null

## NEVER
- NEVER use alert_rule for LLM behavior constraints (use guardrail)
- NEVER use alert_rule for artifact quality scoring (use quality_gate)
- NEVER write vague metric expressions ("when it's slow", "if errors happen")
- NEVER page on warning severity -- warning creates tickets, not pages
- NEVER omit routing target

## EDGE CASES
| Case | Rule |
|------|------|
| Alert should suppress others | Add inhibit_rules referencing other alert IDs |
| SLO-based alert | Use burn_rate expression (not raw threshold) |
| Composite condition (A AND B) | Single expression using PromQL AND operator |
| Maintenance window suppression | Add silence configuration (separate from rule) |

## Naming Conventions
| Pattern | Example |
|---------|---------|
| ar_{system}_{metric}_{level} | ar_api_error_rate_high |
| alert_name PascalCase | ApiErrorRateHigh |
| severity levels | critical, warning, info (lowercase) |

## Size Budget
max_bytes: 2048 (minimal kind -- expression + routing + runbook = ~1KB typical)

## Orchestration Checklist

- Verify workflow topology matches dependency graph
- Validate handoff protocol between upstream and downstream
- Cross-reference with dispatch rules for routing correctness
- Test wave sequencing with dry-run before live dispatch

## Orchestration Pattern

```yaml
# Workflow validation
topology: verified
handoffs: validated
routing: checked
sequencing: tested
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope orchestration
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_guardrail_builder]] | upstream | 0.29 |
| [[p03_sp_validator-builder]] | upstream | 0.28 |
| [[p03_sp_system-prompt-builder]] | upstream | 0.26 |
| [[p03_sp_context_window_config_builder]] | upstream | 0.23 |
| [[p03_sp_kind_builder]] | upstream | 0.22 |
| [[p03_sp_quality_gate_builder]] | upstream | 0.22 |
| [[p03_sp_type-def-builder]] | upstream | 0.21 |
| [[p03_sp_optimizer_builder]] | upstream | 0.20 |
| [[p03_sp_few_shot_example_builder]] | upstream | 0.20 |
| [[p03_sp_validation-schema-builder]] | upstream | 0.20 |
