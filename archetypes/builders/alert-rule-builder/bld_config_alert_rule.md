---
id: bld_context_sources_alert_rule
kind: rag_source
pillar: P10
llm_function: CONSTRAIN
version: 1.0.0
quality: 6.0
tags: [alert_rule, context, rag]
title: "Context Sources: alert_rule"
density_score: 1.0
updated: "2026-04-17"
---
# Context Sources: alert_rule
## Mandatory Sources (load at F3 INJECT)
| Source | Path | Why |
|--------|------|-----|
| Kind KC | N00_genesis/P01_knowledge/library/kind/kc_alert_rule.md | Definition + boundary |
| Schema | archetypes/builders/alert-rule-builder/bld_schema_alert_rule.md | Required fields |
| Examples | archetypes/builders/alert-rule-builder/bld_examples_alert_rule.md | Golden patterns |

## Optional Sources (load if relevant)
| Source | Path | When to Load |
|--------|------|-------------|
| signal KC | N00_genesis/P01_knowledge/library/kind/kc_signal.md | If building signal-based alert |
| guardrail KC | N00_genesis/P01_knowledge/library/kind/kc_guardrail.md | Boundary disambiguation |
| Existing alerts | {nucleus}/P09_*/ar_*.md | Consistency + inhibition rules |

## Search Queries for Retrieval
- "Prometheus alerting rule PromQL threshold"
- "Alertmanager routing severity PagerDuty Slack"
- "SLO alerting error budget burn rate"
- "observability alert runbook remediation"

## Anti-Sources (do NOT confuse with)
- guardrail (LLM behavior, not system threshold)
- quality_gate (artifact scoring, not system metric)
- signal (what to observe, not when to fire alert)
