---
id: n00_partner_listing_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Partner Listing -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, partner_listing, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_partner_listing
  - bld_schema_integration_guide
  - bld_schema_marketplace_app_manifest
  - bld_collaboration_partner_listing
  - bld_schema_reranker_config
  - bld_schema_app_directory_entry
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Partner listing produces a co-branded directory entry for a partner ecosystem marketplace or integration catalog. It documents the partner relationship type, integration capabilities, pricing, and mutual value proposition in the format required by the platform's listing submission process. Output serves both discovery (partners finding each other) and trust-building (mutual brand association).

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `partner_listing` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Partner name + integration name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| partner_name | string | yes | Name of the partner company |
| partnership_type | enum | yes | technology / reseller / referral / oem |
| target_directory | string | yes | Marketplace where listing is submitted |
| integration_summary | string | yes | What the integration does (150-300 chars) |
| co_marketing_approved | bool | yes | Whether co-branding is permitted |

## When to use
- Submitting a technology partnership to a platform marketplace (AWS, Salesforce AppExchange)
- Publishing a new integration to an integration catalog for discoverability
- Formalizing a reseller or referral partner relationship with a directory entry

## Builder
`archetypes/builders/partner_listing-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind partner_listing --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N06 commercial manages partner relationships and listings
- `{{SIN_LENS}}` -- Strategic Greed: maximize ecosystem leverage from each partnership
- `{{TARGET_AUDIENCE}}` -- buyers browsing the partner directory for integration solutions
- `{{DOMAIN_CONTEXT}}` -- partner tier, integration depth, mutual ICP overlap

## Example (minimal)
```yaml
---
id: partner_listing_cex_aws
kind: partner_listing
pillar: P05
nucleus: n06
title: "CEX Platform -- AWS Marketplace Listing"
version: 1.0
quality: null
---
partner_name: Amazon Web Services
partnership_type: technology
target_directory: AWS Marketplace
co_marketing_approved: true
```

## Related kinds
- `app_directory_entry` (P05) -- product-first listing; partner listing is relationship-first
- `integration_guide` (P05) -- technical doc backing the integration described in the listing
- `case_study` (P05) -- mutual success story that strengthens the partner listing

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_partner_listing]] | downstream | 0.54 |
| [[bld_schema_integration_guide]] | downstream | 0.45 |
| [[bld_schema_marketplace_app_manifest]] | downstream | 0.39 |
| [[bld_collaboration_partner_listing]] | downstream | 0.39 |
| [[bld_schema_reranker_config]] | downstream | 0.39 |
| [[bld_schema_app_directory_entry]] | downstream | 0.38 |
| [[bld_schema_usage_report]] | downstream | 0.38 |
| [[bld_schema_dataset_card]] | downstream | 0.38 |
| [[bld_schema_pitch_deck]] | downstream | 0.38 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.38 |
