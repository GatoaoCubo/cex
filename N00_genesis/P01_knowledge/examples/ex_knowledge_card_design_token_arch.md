---
id: p01_kc_design_token_arch
kind: knowledge_card
pillar: P01
title: "Design Token Architecture — Three-Layer System for Scalable Theming"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: design_systems
quality: 9.1
tags: [design-tokens, css-variables, theming, dark-mode, design-system]
tldr: "3-layer token arch (Primitive->Semantic->Component) enables theme switching by changing only the semantic layer"
when_to_use: "Building or refactoring a design system with theming, dark mode, or white-label support"
keywords: [design-tokens, css-custom-properties, semantic-tokens, primitive-tokens]
long_tails:
  - "How to structure CSS design tokens in three layers"
  - "How to implement dark mode with design tokens"
axioms:
  - "NEVER hardcode hex values in components — always reference tokens"
  - "ALWAYS change themes at the semantic layer only"
linked_artifacts:
  primary: null
  related: []
density_score: null
data_source: null
related:
  - p01_kc_brand_propagation_arch
  - p01_kc_color_theory_applied
  - n02_kc_color_theory_applied
  - p10_dtc_design_token_contract
  - p01_kc_email_html_responsive
  - n06_output_visual_identity
  - p05_output_email_template
  - p12_wf_brand_propagation
  - n02_kc_email_html_responsive
  - p06_schema_tailwind_palette
---

## TL;DR

Design tokens organized in 3 layers — Primitive (raw values), Semantic (purpose aliases), Component (per-component overrides) — enable theme switching by modifying only the semantic layer. Dark mode, white-label, and brand changes become a single-layer operation.

## Conceito Central

Token architecture separates WHAT a value is from WHY it exists and WHERE it applies. Primitives define raw values (`--color-blue-600: #2563EB`), semantics assign purpose (`--color-primary: var(--color-blue-600)`), and component tokens scope usage (`--button-bg: var(--color-primary)`). Each layer changes at different cadence: primitives rarely, semantics per theme, components per feature.

## Arquitetura / Patterns

| Layer | Example | Changes When | References |
|-------|---------|-------------|------------|
| Primitive | `--color-blue-600: #2563EB` | Brand redesign | Nothing |
| Semantic | `--color-primary: var(--color-blue-600)` | Theme switch | Primitives |
| Component | `--button-bg: var(--color-primary)` | Feature scope | Semantics |

Naming convention: `--{category}-{item}-{variant}-{state}`.

Dark mode overrides only the semantic layer:

```css
.dark {
  --color-background: var(--color-gray-900);
  --color-foreground: var(--color-gray-50);
}
/* Component tokens inherit automatically — zero changes needed */
```

Migration from flat tokens: extract hex into primitives, create semantic aliases, update component references. W3C DTCG JSON format (`$value`, `$type`) standardizes cross-tool interchange.

File organization options: separate files (`primitives.css`, `semantic.css`, `components.css`, `index.css`) or single file with section comments.

## Exemplos Praticos

```css
/* Primitive — raw values, rarely change */
:root {
  --color-blue-600: #2563EB;
  --color-gray-50: #F9FAFB;
  --space-4: 1rem;
}

/* Semantic — purpose aliases, change per theme */
:root {
  --color-primary: var(--color-blue-600);
  --color-background: var(--color-gray-50);
  --spacing-section: var(--space-4);
}

/* Component — scoped overrides, change per feature */
:root {
  --button-bg: var(--color-primary);
  --card-padding: var(--spacing-section);
}
```

HSL for opacity control: `hsl(var(--primary) / 0.5)`.

## Anti-Patterns

- Hardcode hex in component CSS (breaks theming)
- Skip semantic layer, reference primitives directly
- Create tokens without real reuse (token bloat)
- Overly descriptive names (`--color-cta-button-hover`)
- Change component tokens for theme switching

## Referencias

- W3C Design Tokens Community Group (DTCG format)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_brand_propagation_arch]] | sibling | 0.52 |
| [[p01_kc_color_theory_applied]] | sibling | 0.44 |
| [[n02_kc_color_theory_applied]] | sibling | 0.39 |
| [[p10_dtc_design_token_contract]] | downstream | 0.33 |
| [[p01_kc_email_html_responsive]] | sibling | 0.27 |
| [[n06_output_visual_identity]] | downstream | 0.25 |
| [[p05_output_email_template]] | downstream | 0.25 |
| [[p12_wf_brand_propagation]] | downstream | 0.23 |
| [[n02_kc_email_html_responsive]] | sibling | 0.22 |
| [[p06_schema_tailwind_palette]] | downstream | 0.20 |
