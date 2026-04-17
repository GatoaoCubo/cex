---
id: n00_app_directory_entry_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "App Directory Entry -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, app_directory_entry, p05, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
App directory entry produces a structured listing artifact for FREE-tier discovery platforms such as Product Hunt, G2, Capterra, AppSumo, or marketplace directories. It packages the product description, category tags, screenshots, and social proof into the format required for directory submission and SEO-optimized discovery.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `app_directory_entry` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Product name as listed |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_directory | string | yes | Platform name (Product Hunt, G2, Capterra, etc.) |
| tagline | string | yes | One-line value proposition (< 60 chars) |
| description_short | string | yes | 150-char elevator pitch |
| description_long | string | yes | Full listing body (500-1000 chars) |
| category_tags | list | yes | Primary and secondary categories |
| pricing_tier | string | yes | free / freemium / paid / open-source |

## When to use
- Launching a new product or feature on a discovery platform
- Updating a stale directory listing with new positioning or features
- Targeting a new marketplace for distribution (AppSumo deal, G2 reviews campaign)

## Builder
`archetypes/builders/app_directory_entry-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind app_directory_entry --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N02 marketing owns discovery listings
- `{{SIN_LENS}}` -- Creative Lust: compelling copy that converts browsers to signups
- `{{TARGET_AUDIENCE}}` -- directory visitors searching for the product category
- `{{DOMAIN_CONTEXT}}` -- product category, free tier feature set, competitive differentiators

## Example (minimal)
```yaml
---
id: app_directory_entry_cex_producthunt
kind: app_directory_entry
pillar: P05
nucleus: n02
title: "CEX Platform -- Product Hunt Listing"
version: 1.0
quality: null
---
target_directory: Product Hunt
tagline: "Enterprise AI brain -- typed knowledge, 8F pipeline"
pricing_tier: open-source
```

## Related kinds
- `landing_page` (P05) -- full conversion page; directory entry links there
- `partner_listing` (P05) -- partner-specific directory format with co-branding
- `press_release` (P05) -- launch announcement often paired with directory submission
