---
id: p06_is_brand_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "input-schema-builder"
scope: "CEX brand bootstrap — identity configuration contract for cex_bootstrap.py"
owner: "cex_bootstrap"
fields:
  - name: brand_name
    type: string
    required: true
    default: null
    description: "Official company or brand name (1-100 chars)"
    error_message: "brand_name is required — provide the official company or brand name"
  - name: tagline
    type: string
    required: true
    default: null
    description: "Short memorable brand phrase (10-100 chars)"
    error_message: "tagline is required — provide a memorable brand phrase between 10 and 100 characters"
  - name: mission
    type: string
    required: true
    default: null
    description: "What the brand does and why (20-500 chars) — one to three sentences"
    error_message: "mission is required — describe what your brand does in one to three sentences"
  - name: values
    type: list
    required: true
    default: null
    description: "Core brand values as a string list (3-7 items, each ≤ 30 chars)"
    error_message: "values is required — provide 3 to 7 core brand values as a list"
  - name: personality
    type: string
    required: false
    default: "professional"
    description: "Tone and character descriptor (e.g. bold, playful, authoritative, technical)"
    error_message: null
  - name: target_audience
    type: string
    required: false
    default: "professionals"
    description: "Primary customer segment (e.g. 'SMB founders', 'data engineers at Series B startups')"
    error_message: null
  - name: archetype
    type: string
    required: false
    default: "Creator"
    description: "One of 12 standard brand archetypes: Hero, Sage, Creator, Caregiver, Explorer, Rebel, Magician, Lover, Jester, Everyman, Ruler, Innocent"
    error_message: null
  - name: brand_voice
    type: string
    required: false
    default: "professional"
    description: "Content generation tone applied by all nuclei — formal, casual, technical, friendly, bold"
    error_message: null
  - name: revenue_model
    type: string
    required: false
    default: null
    description: "Primary monetization model — subscription, one-time, freemium, course, consulting, marketplace"
    error_message: null
  - name: primary_color
    type: string
    required: false
    default: null
    description: "Primary brand color as hex code (e.g. '#1A73E8'); '#' prefix applied via coercion if absent"
    error_message: null
  - name: secondary_color
    type: string
    required: false
    default: null
    description: "Secondary brand color as hex code; same coercion as primary_color"
    error_message: null
  - name: slogan
    type: string
    required: false
    default: null
    description: "Campaign-specific slogan distinct from tagline — short, punchy, time-bound"
    error_message: null
coercion:
  - from: string
    to: list
    rule: "Split comma-separated string on ',' and strip whitespace per item — applies to 'values' field only"
  - from: string
    to: string
    rule: "Normalize hex color: prepend '#' if absent (e.g. '1A73E8' → '#1A73E8') — applies to primary_color and secondary_color"
examples:
  - brand_name: "Acme Labs"
    tagline: "Build smarter, ship faster"
    mission: "We help engineering teams reduce deployment friction through intelligent automation."
    values: ["speed", "reliability", "transparency"]
    personality: "technical and direct"
    target_audience: "senior engineers at growth-stage startups"
    archetype: "Sage"
    brand_voice: "concise and technical"
    revenue_model: "subscription"
    primary_color: "#1A73E8"
    secondary_color: "#34A853"
  - brand_name: "FlowCo"
    tagline: "Your growth, automated"
    mission: "Automate marketing workflows so founders focus on product."
    values: ["clarity", "growth", "automation"]
domain: "brand-configuration"
quality: 9.1
tags: [input-schema, brand-configuration, brand-bootstrap, P06]
tldr: "Input contract for CEX brand bootstrap: 4 required fields (name, tagline, mission, values); 8 optional with sane defaults."
keywords: [brand_config, bootstrap, brand_name, values, personality, target_audience, archetype, revenue_model, hex_color]
density_score: 0.92
---
## Contract Definition
CEX brand data model input schema — the unilateral contract between a brand owner and `cex_bootstrap.py`. Callers supply four required identity fields; all eight optional fields have defaults so bootstrapping succeeds with minimal input. After bootstrap, N06 uses this data to populate `brand_config.yaml` (41 variables, 7 sections), which every nucleus reads at startup to inject brand context into generated artifacts.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | brand_name | string | YES | — | Official brand name (1-100 chars) |
| 2 | tagline | string | YES | — | Memorable brand phrase (10-100 chars) |
| 3 | mission | string | YES | — | Brand mission statement (20-500 chars) |
| 4 | values | list | YES | — | 3-7 core brand values |
| 5 | personality | string | NO | "professional" | Tone and character descriptor |
| 6 | target_audience | string | NO | "professionals" | Primary customer segment |
| 7 | archetype | string | NO | "Creator" | Standard brand archetype (1 of 12) |
| 8 | brand_voice | string | NO | "professional" | Content generation tone |
| 9 | revenue_model | string | NO | null | Primary monetization model |
| 10 | primary_color | string | NO | null | Hex color (auto-prefixed with '#') |
| 11 | secondary_color | string | NO | null | Hex color (auto-prefixed with '#') |
| 12 | slogan | string | NO | null | Campaign-specific slogan |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | list | Comma-split `values` input: `"bold, honest, fast"` → `["bold", "honest", "fast"]` |
| string | string | Hex normalize: strip whitespace, prepend `#` if missing from `primary_color` / `secondary_color` |

## Examples
**Full input:**
```json
{
  "brand_name": "Acme Labs",
  "tagline": "Build smarter, ship faster",
  "mission": "We help engineering teams reduce deployment friction through intelligent automation.",
  "values": ["speed", "reliability", "transparency"],
  "personality": "technical and direct",
  "target_audience": "senior engineers at growth-stage startups",
  "archetype": "Sage",
  "brand_voice": "concise and technical",
  "revenue_model": "subscription",
  "primary_color": "#1A73E8",
  "secondary_color": "#34A853"
}
```

**Minimal valid input (required fields only):**
```json
{
  "brand_name": "FlowCo",
  "tagline": "Your growth, automated",
  "mission": "Automate marketing workflows so founders focus on product.",
  "values": ["clarity", "growth", "automation"]
}
```

## References
- Consumer: `_tools/cex_bootstrap.py --from-file` (writes `brand_config.yaml`)
- Downstream schema: `.cex/brand/brand_config.yaml` — 7 sections, 41 variables
- Validation: `_tools/brand_validate.py` (13 required brand fields checked post-bootstrap)