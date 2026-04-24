---
id: n00_guardrail_manifest
kind: knowledge_card
8f: F3_inject
pillar: P11
nucleus: n00
title: "Guardrail -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, guardrail, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_guardrail
  - guardrail-builder
  - bld_architecture_guardrail
  - bld_collaboration_guardrail
  - bld_schema_safety_policy
  - bld_schema_reranker_config
  - p03_sp_guardrail_builder
  - bld_schema_multimodal_prompt
  - bld_schema_integration_guide
  - bld_schema_usage_report
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A guardrail defines a safety restriction (safety boundary) that constrains agent behavior within acceptable limits. It specifies what actions are prohibited, what outputs are blocked, and what escalation paths activate when violations are detected. Guardrails are the primary mechanism for enforcing organizational AI safety policy at the inference level.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `guardrail` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| guardrail_type | enum | yes | input \| output \| action \| reasoning |
| prohibited_patterns | array | yes | Patterns or conditions that trigger the guardrail |
| enforcement_mode | enum | yes | block \| warn \| log_only \| human_review |
| severity | enum | yes | critical \| high \| medium \| low |
| scope | array | yes | Nuclei or kinds this guardrail applies to |
| override_policy | string | no | Conditions under which the guardrail can be overridden |

## When to use
- When implementing safety boundaries for customer-facing agent deployments
- When enforcing brand safety constraints on N02 marketing outputs
- When complying with EU AI Act prohibited practices (Article 5) restrictions

## Builder
`archetypes/builders/guardrail-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind guardrail --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: gr_no_pii_in_output
kind: guardrail
pillar: P11
nucleus: n00
title: "Example Guardrail"
version: 1.0
quality: null
---
# Guardrail: Block PII in Outputs
guardrail_type: output
prohibited_patterns: ["SSN pattern", "credit card pattern", "email in logs"]
enforcement_mode: block
severity: critical
scope: [n01, n02, n03, n04, n05, n06, n07]
```

## Related kinds
- `content_filter` (P11) -- filter pipeline implementing guardrail checks
- `safety_policy` (P11) -- organizational policy that mandates this guardrail
- `hitl_config` (P11) -- human review flow activated on critical guardrail violations

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_guardrail]] | upstream | 0.57 |
| [[guardrail-builder]] | related | 0.50 |
| [[bld_architecture_guardrail]] | upstream | 0.47 |
| [[bld_collaboration_guardrail]] | downstream | 0.44 |
| [[bld_schema_safety_policy]] | upstream | 0.40 |
| [[bld_schema_reranker_config]] | upstream | 0.40 |
| [[p03_sp_guardrail_builder]] | upstream | 0.40 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.39 |
| [[bld_schema_integration_guide]] | upstream | 0.39 |
| [[bld_schema_usage_report]] | upstream | 0.39 |
