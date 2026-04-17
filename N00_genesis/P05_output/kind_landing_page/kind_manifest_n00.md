---
id: n00_landing_page_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Landing Page -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, landing_page, p05, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Landing page produces a complete production-ready HTML artifact with 12 standard sections: hero, problem, solution, features, social proof, pricing, FAQ, CTA, footer, and supporting sections. The output is responsive, dark-mode compatible, SEO-optimized, and accessibility-compliant. It is the highest-complexity single-file output in the P05 pillar.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `landing_page` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Page title / product name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| sections | list | yes | 12 ordered sections with content specs |
| cta_primary | string | yes | Primary call-to-action text and destination |
| cta_secondary | string | no | Secondary CTA (demo, learn more) |
| tech_stack | string | yes | HTML+Tailwind / React / Vue / plain CSS |
| seo_title | string | yes | Meta title (< 60 chars) |
| seo_description | string | yes | Meta description (< 155 chars) |

## When to use
- Launching a new product, feature, or campaign with a dedicated conversion page
- A/B testing a new value proposition against an existing page
- Building a landing page for a specific audience segment or traffic source

## Builder
`archetypes/builders/landing_page-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind landing_page --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N02 marketing creates; N03 engineering builds the HTML
- `{{SIN_LENS}}` -- Creative Lust: irresistible conversion-optimized copy
- `{{TARGET_AUDIENCE}}` -- specific buyer persona driving the traffic source
- `{{DOMAIN_CONTEXT}}` -- product positioning, pricing, social proof, design system

## Example (minimal)
```yaml
---
id: landing_page_cex_main
kind: landing_page
pillar: P05
nucleus: n02
title: "CEX Platform -- Main Landing Page"
version: 1.0
quality: null
---
cta_primary: "Start free -- no credit card"
tech_stack: "HTML + Tailwind CSS"
seo_title: "CEX -- Enterprise AI Brain for Teams"
```

## Related kinds
- `pricing_page` (P05) -- dedicated page for tier comparison; linked from landing page
- `user_journey` (P05) -- maps the full funnel; landing page is the awareness/acquisition step
- `app_directory_entry` (P05) -- discovery artifact that drives traffic to the landing page
