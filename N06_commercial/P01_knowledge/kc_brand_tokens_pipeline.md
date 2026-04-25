---
id: p01_kc_brand_tokens_pipeline
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Brand Tokens Pipeline — Living Brand System from Guidelines to Code"
version: 1.1.0
created: 2026-03-26
updated: 2026-04-07
author: builder_agent
domain: cex_taxonomy
quality: 9.0
tags: [brand, design-tokens, design-system, brand-guidelines, css-variables]
tldr: "Brand as a living system: guidelines.md (single source) -> JSON tokens -> CSS vars -> code, with automatic sync"
when_to_use: "Implement programmatic visual identity with single source of truth and automatic propagation"
keywords: [brand-system, design-tokens, brand-guidelines, brand-sync]
long_tails:
  - "How to create a brand system with automatic propagation to code"
  - "What is the design token architecture from guidelines to CSS"
  - "How to sync brand config with CSS variables automatically"
axioms:
  - "ALWAYS edit brand-guidelines.md first, never tokens directly"
  - "NEVER have more than 1 source of truth -- brand_config.yaml is canonical."
  - "ALWAYS validate compiled tokens against brand_config before deploy."
  - "NEVER use hardcoded hex in components -- use CSS variables"
linked_artifacts:
  primary: p01_kc_brand_propagation_arch
  related: [n06_output_visual_identity, n06_schema_brand_config, n06_output_brand_config, p01_kc_agentskills_spec]
density_score: 0.93
data_source: "https://www.designtokens.org/glossary/"
related:
  - p01_kc_brand_skill
  - p12_wf_brand_propagation
  - p01_kc_brand_propagation_arch
  - p03_sp_brand_nucleus
  - p02_agent_commercial_nucleus
  - p01_kc_brand_book_patterns
  - spec_n06_brand_verticalization
  - p01_kc_brand_best_practices
  - p02_agent_brand_nucleus
  - p12_dr_commercial
---

## TL;DR

Brand as a living system where a single Markdown file (brand-guidelines.md) is the sole source of truth. Sync scripts automatically propagate to design tokens JSON, CSS variables, and prompt context. Eliminates design-code desynchronization — the #1 cause of "off-brand" output at scale.

## Core Concept

The central problem of brand in software projects is fragmentation: colors defined in Figma, typography in CSS, voice tone in a document nobody reads. The solution is to treat brand as a data pipeline: a human-editable source (Markdown) that automatically transforms into machine-consumable artifacts.

The architecture uses 3 token layers: primitives (raw values like #E8B4B8), semantic (roles like primary, accent), and components (applications like button-bg, header-text). Each layer adds meaning without losing traceability back to the source. Sync is unidirectional: guidelines.md is the only input, everything else is generated. ROI: one edit, every platform updated — zero manual propagation cost.

The voice framework complements visual with 4 dimensions: personality traits, tone variations, language rules, and content examples. This enables LLMs to generate on-brand copy automatically using context injected via script.

## Architecture/Patterns

| Layer | File | Role |
|-------|------|------|
| Source | brand-guidelines.md | Human-editable single source of truth |
| Tokens | design-tokens.json | Primitive, semantic, component layers |
| CSS | design-tokens.css | CSS variables for import |
| Context | inject-brand-context.cjs | Injects brand into LLM prompts |

Sync pipeline:
```
guidelines.md
  -> sync-brand-to-tokens.cjs
    -> design-tokens.json
      -> design-tokens.css
        -> import em componentes
```

Color system (3 types per brand):
- **Primary**: CTAs, headers — main brand color (highest conversion impact)
- **Secondary**: backgrounds, borders — visual support
- **Accent**: badges, alerts — punctual highlighting (urgency, promotions)

Each color includes: hex, HSL (for opacity), on-color (text on background), semantic role. Typography follows the same pattern: heading font + body font with defined sizes and weights.

Automatic validation: script detects hardcoded values in components that should use tokens. Pre-flight checklist before publishing any asset.

Scale: projects with 55+ design CSVs use the same pipeline — each CSV is a visual domain (colors, typography, layouts) and brand-guidelines.md governs all. Unidirectional sync ensures the only human operation is editing the Markdown source; everything else is derived automatically via Node.js scripts.

## Practical Examples

| Operation | Command | Result |
|-----------|---------|--------|
| Sync brand | `node sync-brand-to-tokens.cjs` | Tokens updated across all platforms |
| Inject context | `node inject-brand-context.cjs` | Brand injected into LLM prompts |
| Validate asset | `node validate-asset.cjs <path>` | Name, format, size checked |
| Extract colors | `node extract-colors.cjs --palette` | Current palette exported |

Minimum template for a new brand:
```markdown
# Brand Guidelines: [Nome]
## Identity
- Mission: [proposito]
- Values: [3-5 valores]
## Colors
- Primary: #HEX (on-primary: white)
- Secondary: #HEX
- Accent: #HEX
## Typography
- Heading: [Font Name]
- Body: [Font Name]
## Voice
- Tone: [3 adjetivos]
- Avoid: [palavras proibidas]
```

## Anti-Patterns

- Editing tokens JSON directly without going through guidelines — breaks source-of-truth chain
- Multiple sources of truth (Figma + CSS + separate docs) — guaranteed drift
- Colors without semantic layer — raw hex without named tokens leads to inconsistency
- Vague voice framework ("be professional" is not actionable) — must be measurable dimensions
- Published assets without approval checklist — brand debt accumulates silently
- CSS with literal font-family instead of var(--typography-*) — breaks theme switching

## References

- source: https://www.designtokens.org/glossary/
- source: https://tr.designtokens.org/format/
- related: p01_kc_agentskills_spec
- related: p01_kc_csv_as_knowledge

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_brand_skill]] | sibling | 0.93 |
| [[p12_wf_brand_propagation]] | downstream | 0.58 |
| [[p01_kc_brand_propagation_arch]] | sibling | 0.40 |
| [[p03_sp_brand_nucleus]] | downstream | 0.38 |
| [[p02_agent_commercial_nucleus]] | downstream | 0.36 |
| [[p01_kc_brand_book_patterns]] | sibling | 0.35 |
| [[spec_n06_brand_verticalization]] | downstream | 0.32 |
| [[p01_kc_brand_best_practices]] | sibling | 0.31 |
| [[p02_agent_brand_nucleus]] | downstream | 0.30 |
| [[p12_dr_commercial]] | downstream | 0.30 |
