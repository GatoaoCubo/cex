---
id: n00_safety_policy_manifest
kind: knowledge_card
8f: F3_inject
pillar: P11
nucleus: n00
title: "Safety Policy -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, safety_policy, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_safety_policy
  - bld_schema_rbac_policy
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_audit_log
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_app_directory_entry
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A safety_policy defines the organizational AI safety governance rules that constrain all nucleus operations, specifying prohibited use cases, mandatory oversight requirements, incident escalation protocols, and the ethical principles that override commercial objectives. It is the constitutional document for the CEX system's responsible AI behavior.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `safety_policy` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| policy_scope | array | yes | Nuclei and use cases this policy governs |
| prohibited_uses | array | yes | Explicitly banned use cases |
| mandatory_controls | array | yes | Controls that must always be active (e.g. content_filter, audit_log) |
| incident_escalation | object | yes | Severity levels with escalation paths and SLA |
| review_cycle | enum | yes | quarterly \| semi_annual \| annual |
| policy_owner | string | yes | Role or nucleus accountable for this policy |

## When to use
- When establishing the safety baseline for a new CEX enterprise deployment
- When onboarding a nucleus into a regulated industry (healthcare, finance, legal)
- When preparing documentation for AI governance audits or board reporting

## Builder
`archetypes/builders/safety_policy-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind safety_policy --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: sp_cex_enterprise_v1
kind: safety_policy
pillar: P11
nucleus: n07
title: "Example Safety Policy"
version: 1.0
quality: null
---
# CEX Enterprise Safety Policy
policy_scope: [n01, n02, n03, n04, n05, n06, n07]
prohibited_uses: ["generate CSAM", "manipulate elections", "bypass legal protections"]
mandatory_controls: [content_filter, audit_log, hitl_config]
policy_owner: n07
review_cycle: quarterly
```

## Related kinds
- `guardrail` (P11) -- technical enforcement of this safety policy
- `ai_rmf_profile` (P11) -- NIST RMF mapping that operationalizes this policy
- `compliance_framework` (P11) -- regulatory framework this policy aligns with

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_safety_policy]] | upstream | 0.53 |
| [[bld_schema_rbac_policy]] | upstream | 0.46 |
| [[bld_schema_integration_guide]] | upstream | 0.44 |
| [[bld_schema_reranker_config]] | upstream | 0.44 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.43 |
| [[bld_schema_audit_log]] | upstream | 0.43 |
| [[bld_schema_benchmark_suite]] | upstream | 0.43 |
| [[bld_schema_usage_report]] | upstream | 0.43 |
| [[bld_schema_search_strategy]] | upstream | 0.42 |
| [[bld_schema_app_directory_entry]] | upstream | 0.42 |
