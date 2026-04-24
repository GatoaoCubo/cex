---
id: n00_renewal_workflow_manifest
kind: knowledge_card
8f: F3_inject
pillar: P12
nucleus: n00
title: "Renewal Workflow -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, renewal_workflow, p12, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_renewal_workflow
  - bld_schema_reranker_config
  - bld_schema_bugloop
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_multimodal_prompt
  - bld_schema_voice_pipeline
  - bld_schema_quickstart_guide
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A renewal_workflow defines the staged process for renewing subscriptions, contracts, or access credentials, specifying owners at each stage, automation triggers, escalation paths, and failure handling. It prevents revenue churn and compliance lapses by automating the renewal lifecycle from first notice through confirmation.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `renewal_workflow` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| renewal_type | enum | yes | subscription \| contract \| credential \| license |
| stages | array | yes | Ordered stages with name, owner, trigger, and SLA days |
| first_notice_days | integer | yes | Days before expiry to send first renewal notice |
| escalation_days | integer | yes | Days before expiry to escalate to human reviewer |
| automation_level | enum | yes | full \| semi_automated \| manual |
| failure_action | enum | yes | suspend \| downgrade \| cancel \| grace_period |

## When to use
- When automating SaaS subscription renewal reminders and collection
- When managing annual enterprise contract renewal cycles
- When refreshing expiring vc_credential or API key credentials

## Builder
`archetypes/builders/renewal_workflow-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind renewal_workflow --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: rw_saas_annual_renewal
kind: renewal_workflow
pillar: P12
nucleus: n06
title: "Example Renewal Workflow"
version: 1.0
quality: null
---
# Renewal Workflow: SaaS Annual Subscription
renewal_type: subscription
first_notice_days: 60
escalation_days: 14
automation_level: semi_automated
failure_action: grace_period
stages:
  - name: first_notice, owner: n06, trigger: scheduled, sla_days: 60
  - name: final_notice, owner: n06, trigger: scheduled, sla_days: 7
```

## Related kinds
- `subscription_tier` (P11) -- subscription tier being renewed by this workflow
- `schedule` (P12) -- schedule triggers that fire renewal workflow stages
- `signal` (P12) -- completion signal emitted when renewal is confirmed

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_renewal_workflow]] | upstream | 0.45 |
| [[bld_schema_reranker_config]] | upstream | 0.43 |
| [[bld_schema_bugloop]] | upstream | 0.41 |
| [[bld_schema_dataset_card]] | upstream | 0.41 |
| [[bld_schema_usage_report]] | upstream | 0.41 |
| [[bld_schema_integration_guide]] | upstream | 0.41 |
| [[bld_schema_benchmark_suite]] | upstream | 0.40 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.40 |
| [[bld_schema_voice_pipeline]] | upstream | 0.40 |
| [[bld_schema_quickstart_guide]] | upstream | 0.40 |
