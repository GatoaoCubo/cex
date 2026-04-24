---
id: n00_white_label_config_manifest
kind: knowledge_card
8f: F3_inject
pillar: P09
nucleus: n00
title: "White Label Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, white_label_config, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_white_label_config
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_sandbox_config
  - bld_schema_multimodal_prompt
  - bld_schema_benchmark_suite
  - bld_schema_search_strategy
  - bld_schema_action_paradigm
  - bld_schema_thinking_config
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A white_label_config defines the branding, domain, and feature customizations that enable a reseller or partner to offer CEX under their own brand. It specifies custom domain configuration, brand asset overrides (logo, colors, tone), feature enablement per reseller, and billing attribution settings, enabling a single CEX instance to serve multiple branded deployments.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `white_label_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| reseller | string | yes | Reseller or partner identifier |
| brand_name | string | yes | Public-facing product name |
| custom_domain | string | yes | Domain for this branded deployment |
| logo_url | string | no | URL to reseller logo asset |
| primary_color | string | no | Brand primary color (hex) |
| secondary_color | string | no | Brand secondary color (hex) |
| enabled_nuclei | list | yes | Which nuclei are exposed in this deployment |
| hide_cex_branding | boolean | yes | Whether to suppress CEX attribution |
| billing_attribution | string | no | Reseller billing account ID |
| custom_support_url | string | no | White-labeled support link |

## When to use
- Setting up a reseller partner to offer CEX as their own branded AI platform
- Configuring a white-label playground for an enterprise customer's internal brand
- Enabling multi-brand deployments from a single CEX infrastructure instance

## Builder
`archetypes/builders/white_label_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind white_label_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: white_label_acme_ai
kind: white_label_config
pillar: P09
nucleus: n06
title: "AcmeCorp AI Platform White Label"
version: 1.0
quality: null
---
reseller: acmecorp
brand_name: "Acme AI Studio"
custom_domain: ai.acmecorp.com
primary_color: "#0057B7"
enabled_nuclei: [n01, n03, n04]
hide_cex_branding: true
billing_attribution: acme_billing_001
custom_support_url: https://support.acmecorp.com/ai
```

## Related kinds
- `marketplace_app_manifest` (P09) -- marketplace listing for a white-labeled CEX app
- `sso_config` (P09) -- SSO integration configured per white-label deployment
- `playground_config` (P09) -- branded playgrounds backed by white_label_config

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_white_label_config]] | upstream | 0.46 |
| [[bld_schema_dataset_card]] | upstream | 0.46 |
| [[bld_schema_usage_report]] | upstream | 0.45 |
| [[bld_schema_reranker_config]] | upstream | 0.45 |
| [[bld_schema_sandbox_config]] | upstream | 0.45 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.45 |
| [[bld_schema_benchmark_suite]] | upstream | 0.45 |
| [[bld_schema_search_strategy]] | upstream | 0.45 |
| [[bld_schema_action_paradigm]] | upstream | 0.44 |
| [[bld_schema_thinking_config]] | upstream | 0.44 |
