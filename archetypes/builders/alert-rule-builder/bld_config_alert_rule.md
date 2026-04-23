---
id: bld_context_sources_alert_rule
kind: rag_source
pillar: P10
llm_function: CONSTRAIN
version: 1.0.0
quality: 8.1
tags: [alert_rule, context, rag]
title: "Context Sources: alert_rule"
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_architecture_kind
  - bld_instruction_kind
  - bld_collaboration_kind
  - bld_tools_kind
  - bld_collaboration_cost_budget
  - bld_output_template_kind
  - bld_collaboration_citation
  - p10_lr_kind_builder
  - kind-builder
  - bld_collaboration_signal
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

## Configuration Checklist

- Verify all required fields are present in frontmatter before saving
- Validate config values against schema constraints (type, range, enum)
- Cross-reference with related configs to avoid contradictions
- Test config loading in target runtime before committing

## Validation

```yaml
# Required config validation
fields_present: true
types_valid: true
ranges_checked: true
cross_refs_verified: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | upstream | 0.26 |
| [[bld_instruction_kind]] | upstream | 0.23 |
| [[bld_collaboration_kind]] | downstream | 0.23 |
| [[bld_tools_kind]] | upstream | 0.22 |
| [[bld_collaboration_cost_budget]] | downstream | 0.21 |
| [[bld_output_template_kind]] | upstream | 0.20 |
| [[bld_collaboration_citation]] | downstream | 0.20 |
| [[p10_lr_kind_builder]] | related | 0.20 |
| [[kind-builder]] | upstream | 0.19 |
| [[bld_collaboration_signal]] | downstream | 0.18 |
