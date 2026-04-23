---
id: n00_hitl_config_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "HITL Config -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, hitl_config, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_hitl_config
  - bld_schema_reranker_config
  - hitl-config-builder
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_playground_config
  - bld_schema_multimodal_prompt
  - bld_schema_nps_survey
  - bld_schema_usage_report
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A hitl_config (Human-in-the-Loop configuration) defines the approval flow and escalation protocol that pauses autonomous agent execution and routes decisions to human reviewers. It specifies what triggers a human review, who the reviewers are, what information they receive, and what happens after approval or rejection.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `hitl_config` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| trigger_conditions | array | yes | Conditions that invoke human review |
| reviewer_roles | array | yes | Human roles authorized to review (e.g. compliance_officer) |
| review_timeout_hours | integer | yes | Hours before auto-reject or auto-approve if no response |
| timeout_action | enum | yes | auto_approve \| auto_reject \| escalate |
| context_provided | array | yes | Information surfaced to reviewer (agent output, audit trail) |
| notification_channel | string | yes | Where review requests are sent (slack \| email \| webhook) |

## When to use
- When deploying agents in high-stakes domains where human oversight is mandatory
- When implementing EU AI Act Article 14 human oversight requirements
- When configuring content_filter fallback to human review for edge cases

## Builder
`archetypes/builders/hitl_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind hitl_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: hitl_high_value_decisions
kind: hitl_config
pillar: P11
nucleus: n07
title: "Example HITL Config"
version: 1.0
quality: null
---
# HITL: High-Value Decision Review
trigger_conditions: ["budget > 10000", "enterprise contract", "critical guardrail violation"]
reviewer_roles: [compliance_officer, cto]
review_timeout_hours: 24
timeout_action: auto_reject
notification_channel: slack
```

## Related kinds
- `guardrail` (P11) -- safety boundary that triggers HITL review on violation
- `content_filter` (P11) -- filter that may route flagged content to HITL
- `incident_report` (P11) -- post-mortem created after HITL interventions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_hitl_config]] | upstream | 0.50 |
| [[bld_schema_reranker_config]] | upstream | 0.44 |
| [[hitl-config-builder]] | related | 0.44 |
| [[bld_schema_integration_guide]] | upstream | 0.44 |
| [[bld_schema_benchmark_suite]] | upstream | 0.44 |
| [[bld_schema_playground_config]] | upstream | 0.43 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.43 |
| [[bld_schema_nps_survey]] | upstream | 0.43 |
| [[bld_schema_usage_report]] | upstream | 0.43 |
| [[bld_schema_search_strategy]] | upstream | 0.42 |
