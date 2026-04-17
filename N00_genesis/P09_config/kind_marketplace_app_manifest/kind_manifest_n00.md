---
id: n00_marketplace_app_manifest_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Marketplace App Manifest -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, marketplace_app_manifest, p09, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A marketplace_app_manifest is the submission specification for publishing a CEX-powered application to AI marketplaces such as Anthropic's Claude App Store, LangChain Hub, or HuggingFace Spaces. It declares app metadata, capability descriptions, pricing, required permissions, and integration endpoints in the format expected by each marketplace.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `marketplace_app_manifest` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable app name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| app_name | string | yes | Display name in marketplace |
| short_description | string | yes | One-line description (max 120 chars) |
| long_description | string | yes | Full description with capabilities |
| target_marketplace | list | yes | anthropic \| langchain \| huggingface \| custom |
| permissions | list | yes | Required OAuth scopes or permissions |
| pricing_model | enum | yes | free \| freemium \| paid \| usage_based |
| webhook_url | string | no | Integration endpoint for marketplace events |
| support_url | string | no | URL for user support |
| category | list | no | Marketplace category tags |

## When to use
- Publishing a CEX nucleus capability as a standalone marketplace product
- Registering a multi-agent workflow as an app in the Anthropic ecosystem
- Submitting a specialized builder to LangChain Hub or HuggingFace

## Builder
`archetypes/builders/marketplace_app_manifest-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind marketplace_app_manifest --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: marketplace_cex_intelligence
kind: marketplace_app_manifest
pillar: P09
nucleus: n06
title: "CEX Intelligence App"
version: 1.0
quality: null
---
app_name: "CEX Intelligence"
short_description: "Enterprise AI research nucleus -- 8F pipeline for deep analysis"
target_marketplace: [anthropic]
permissions: [read_conversations, create_artifacts]
pricing_model: usage_based
category: [research, enterprise, analysis]
```

## Related kinds
- `white_label_config` (P09) -- white-label configs that customize marketplace apps per reseller
- `oauth_app_config` (P09) -- OAuth credentials for marketplace authentication
- `content_monetization` (P11) -- pricing strategy that informs the pricing_model field
