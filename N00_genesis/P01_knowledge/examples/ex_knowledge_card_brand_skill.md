---
id: p01_kc_brand_skill
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Brand Skill — Living Brand System from Guidelines to Code"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: cex_taxonomy
quality: 9.0
tags: [brand, design-tokens, design-system, brand-guidelines, css-variables]
tldr: "Brand as a living system: guidelines.md (single source) -> JSON tokens -> CSS vars -> code, with automatic sync"
when_to_use: "Implement programmatic visual identity with single source of truth and automatic propagation"
keywords: [brand-system, design-tokens, brand-guidelines, brand-sync]
long_tails:
  - "How to create a brand system with automatic propagation to code"
  - "What is the design tokens architecture from guidelines to CSS"
axioms:
  - "ALWAYS edit brand-guidelines.md first, never tokens directly"
  - "NEVER use hardcoded hex in components — use CSS variables"
linked_artifacts:
  primary: null
  related: [p01_kc_agentskills_spec, p01_kc_csv_as_knowledge]
density_score: null
data_source: "https://www.designtokens.org/glossary/"
related:
  - p01_kc_brand_tokens_pipeline
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

Brand as a living system where a Markdown file (brand-guidelines.md) is the single source of truth. Sync scripts propagate automatically to design tokens JSON, CSS variables, and prompt context. Eliminates desynchronization between design and code.

## Core Concept

The central problem of brand in software projects is fragmentation: colors defined in Figma, typography in CSS, tone of voice in a document nobody reads. The solution is to treat brand as a data pipeline: a human-editable source (Markdown) that automatically transforms into machine-consumable artifacts.

The architecture uses 3 token layers: primitives (raw values like #E8B4B8), semantic (roles like primary, accent), and components (applications like button-bg, header-text). Each layer adds meaning without losing traceability to the source. Sync is unidirectional: guidelines.md is the only input, everything else is generated.

The voice framework complements visual with 4 dimensions: personality traits, tone variations, language rules, and content examples. This allows LLMs to generate on-brand copy automatically using context injected via script.

## Architecture/Patterns

| Layer | File | Role |
|-------|------|------|
| Source | brand-guidelines.md | Human-editable |
| Tokens | design-tokens.json | Primitive, semantic, component |
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
- **Primary**: CTAs, headers — main brand color
- **Secondary**: backgrounds, borders — visual support
- **Accent**: badges, alerts — spot highlight

Each color includes: hex, HSL (for opacity), on-color (text over background), semantic role. Typography follows similar pattern: heading font + body font with defined sizes and weights.

Automatic validation: script detects hardcoded values in components that should use tokens. Pre-flight checklist before publishing any asset.

Pattern scale: projects with 55+ design CSVs use the same pipeline — each CSV is a visual domain (colors, typography, layouts) and brand-guidelines.md governs all. Unidirectional sync ensures the only human operation is editing the source Markdown; everything else is derived automatically via Node.js scripts.

## Practical Examples

| Operation | Command | Result |
|-----------|---------|--------|
| Sync brand | `node sync-brand-to-tokens.cjs` | Tokens updated |
| Inject context | `node inject-brand-context.cjs` | Brand in prompt |
| Validate asset | `node validate-asset.cjs <path>` | Name, format, size |
| Extract colors | `node extract-colors.cjs --palette` | Current palette |

Minimum template for new brand:
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
- Avoid: [forbidden words]
```

## Anti-Patterns

- Editing JSON tokens directly without going through guidelines
- Multiple sources of truth (Figma + CSS + separate docs)
- Colors without semantics — raw hex without named token
- Vague voice framework ("be professional" is not actionable)
- Assets published without going through approval checklist
- CSS with literal font-family instead of var(--typography-*)

## References

- source: https://www.designtokens.org/glossary/
- source: https://tr.designtokens.org/format/
- related: p01_kc_agentskills_spec
- related: p01_kc_csv_as_knowledge

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_brand_tokens_pipeline]] | sibling | 0.93 |
| [[p12_wf_brand_propagation]] | downstream | 0.58 |
| [[p01_kc_brand_propagation_arch]] | sibling | 0.40 |
| [[p03_sp_brand_nucleus]] | downstream | 0.38 |
| [[p02_agent_commercial_nucleus]] | downstream | 0.36 |
| [[p01_kc_brand_book_patterns]] | sibling | 0.35 |
| [[spec_n06_brand_verticalization]] | downstream | 0.32 |
| [[p01_kc_brand_best_practices]] | sibling | 0.31 |
| [[p02_agent_brand_nucleus]] | downstream | 0.30 |
| [[p12_dr_commercial]] | downstream | 0.30 |
