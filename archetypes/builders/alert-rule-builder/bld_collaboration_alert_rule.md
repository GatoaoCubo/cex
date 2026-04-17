---
id: bld_rules_alert_rule
kind: guardrail
pillar: P11
llm_function: GOVERN
version: 1.0.0
quality: null
tags: [alert_rule, rules, guardrail]
title: "Rules: alert_rule Builder"
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
