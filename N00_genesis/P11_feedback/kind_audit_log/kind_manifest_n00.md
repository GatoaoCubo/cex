---
id: n00_audit_log_manifest
kind: knowledge_card
pillar: P11
nucleus: n00
title: "Audit Log -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, audit_log, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_audit_log
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_sandbox_config
  - bld_schema_usage_report
  - bld_schema_rbac_policy
  - audit-log-builder
  - bld_schema_dataset_card
  - bld_schema_sandbox_spec
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An audit_log defines the immutable audit logging configuration required for SOC2 Type II compliance, specifying what events are logged, the retention policy, tamper-evidence mechanism, and access controls. It ensures that all agent actions, data accesses, and configuration changes are recorded in a cryptographically verifiable chain that satisfies external auditors.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `audit_log` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| log_scope | array | yes | Event categories to log (auth, data_access, config_change, inference) |
| retention_days | integer | yes | Log retention period (SOC2 minimum: 365) |
| tamper_evidence | enum | yes | hash_chain \| merkle_tree \| worm_storage |
| storage_backend | string | yes | Where logs are stored (e.g. s3://bucket/audit/) |
| access_control | array | yes | Roles permitted to read audit logs |
| alert_on | array | no | Event patterns that trigger security alerts |

## When to use
- When deploying a CEX nucleus in a SOC2 Type II certified environment
- When configuring audit trails for GDPR data access compliance
- When setting up tamper-evident logging for high-risk AI systems under EU AI Act

## Builder
`archetypes/builders/audit_log-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind audit_log --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: al_cex_soc2_production
kind: audit_log
pillar: P11
nucleus: n05
title: "Example Audit Log Config"
version: 1.0
quality: null
---
# Audit Log: SOC2 Production
log_scope: [auth, data_access, config_change, inference]
retention_days: 365
tamper_evidence: hash_chain
storage_backend: "s3://cex-audit-logs/production/"
```

## Related kinds
- `compliance_checklist` (P11) -- checklist that references audit log as a control
- `incident_report` (P11) -- post-mortem that queries audit logs for evidence
- `agent_grounding_record` (P10) -- inference provenance that feeds into audit logs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_audit_log]] | upstream | 0.51 |
| [[bld_schema_integration_guide]] | upstream | 0.42 |
| [[bld_schema_reranker_config]] | upstream | 0.41 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.41 |
| [[bld_schema_sandbox_config]] | upstream | 0.41 |
| [[bld_schema_usage_report]] | upstream | 0.40 |
| [[bld_schema_rbac_policy]] | upstream | 0.40 |
| [[audit-log-builder]] | related | 0.40 |
| [[bld_schema_dataset_card]] | upstream | 0.40 |
| [[bld_schema_sandbox_spec]] | upstream | 0.40 |
