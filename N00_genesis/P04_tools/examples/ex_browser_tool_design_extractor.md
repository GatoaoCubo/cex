---
id: p04_browser_design_extractor
name: organization-design-extractor
description: Extrair design tokens e Tailwind configs de qualquer website URL
version: 1.0.0
pillar: P04
kind: browser_tool
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
domain: building
quality: 9.1
tags: [design-tokens, tailwind, css, extraction, visual-design]
tldr: Pipeline URL-to-tokens - Discover(Chrome)>Extract(parser)>Transform(Style Dictionary)>Build(components)>Validate(ODiff)
user_invocable: true
trigger: /design-extractor
when_to_use: Extrair tokens de site para replicar visual, migrar design system, audit de consistencia
when_not_to_use: Criar design do zero (usar web-design-agent), apenas screenshots (usar bowser)
phases:
  - Discover (Chrome MCP)
  - Extract (HTML parser)
  - Transform (Style Dictionary)
  - Build (builder_agent components)
  - Validate (ODiff)
examples:
  - /design-extractor https://linear.app
  - /design-extractor https://stripe.com --tokens-only
  - /design-extractor --compare https://site-a.com https://site-b.com
density_score: 0.86
linked_artifacts:
  agent: records/agents/design-extractor/README.md
title: "Example: Browser Tool Design Extractor"
related:
  - p12_wf_brand_propagation
  - p01_kc_brand_propagation_arch
  - p02_agent_visual_frontend_marketing
  - bld_architecture_landing_page
  - p03_sp_visual_frontend_marketing
  - bld_tools_landing_page
  - p08_ac_visual_frontend_marketing
  - spec_n02_visual_frontend_engineer
  - spec_n02_part2
  - p01_kc_brand_tokens_pipeline
---

# Design Extractor Skill

## Purpose

Pipeline completo de URL ate design tokens production-ready. Captura screenshots, extrai cores/tipografia/espacamento/shadows/borders via HTML parsing, transforma em W3C DTCG tokens, gera Tailwind config / CSS vars / SCSS, opcionalmente gera React components, e valida pixel-perfect com ODiff.

## Workflow Phases

### Phase 1: Discover
**Input**: `url`, optional `pages` array
**Action**: Chrome MCP navega, captura screenshots, mapeia URLs
**Output**: Screenshots + URL map

### Phase 2: Extract
**Input**: Screenshots + HTML pages
**Action**: HTML parser extrai design primitives (cores, fonts, spacing)
**Output**: W3C DTCG tokens raw

### Phase 3: Transform
**Input**: DTCG tokens raw
**Action**: Style Dictionary transforma para formato target
**Output**: `tailwind.config.js`, CSS custom properties, SCSS vars

### Phase 4: Build (opcional)
**Input**: Tokens + component patterns
**Action**: builder_agent gera React/Vue components usando tokens
**Output**: Component library

### Phase 5: Validate
**Input**: Original screenshots + generated output
**Action**: ODiff compara pixel-perfect
**Output**: Diff report com delta scores

## Usage

```bash
# Full extraction from URL
/design-extractor https://linear.app

# Extract tokens only (sem component generation)
/design-extractor https://stripe.com --tokens-only

# Compare two sites
/design-extractor --compare https://site-a.com https://site-b.com

# Export as Tailwind config
/design-extractor https://vercel.com --format tailwind
```

## Input / Output

```yaml
input:
  url: string
  pages: array              # Optional specific pages
  format: enum              # tailwind | css-vars | scss | dtcg
  compare_url: string       # Optional second URL
  components: boolean       # Generate React components (default: false)

output:
  design_tokens:
    colors: [{name, value, usage}]
    typography: [{family, sizes, weights, line_heights}]
    spacing: [scale_values]
    borders: [{radius, width, style}]
    shadows: [{name, value}]
    breakpoints: [{name, min_width}]
  tailwind_config: path
  css_variables: path
  screenshots: [paths]
  audit_report: path
```

## Quality Gates

| Gate | Threshold | Acao se Falhar |
|------|-----------|----------------|
| Token extraction completeness | >= 90% | Manual review |
| Color accuracy | Delta E < 2.0 | Re-extract com higher precision |
| Typography matching | 100% font families | Fallback computed styles |
| Tailwind config validity | Passes build | Fix syntax errors |

## Anti-Patterns

- Extrair sem screenshots de referencia: nao tem como validar resultado — always capture first
- Ignorar Delta E em cores: "close enough" em design = visualmente errado — threshold < 2.0
- Gerar components sem tokens: hardcoded values = design system fragil — tokens first, components second
- Nao validar Tailwind build: config com syntax error = build quebrado — always `npx tailwindcss build`

## Cross-References

- `styling` agent: CSS/Tailwind styling systems
- `web-design` agent: Architecture e layout decisions
- `vision-to-code` agent: Screenshot to code conversion
- `react-component` agent: Component generation from tokens

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_brand_propagation]] | downstream | 0.32 |
| [[p01_kc_brand_propagation_arch]] | upstream | 0.24 |
| [[p02_agent_visual_frontend_marketing]] | upstream | 0.23 |
| [[bld_architecture_landing_page]] | downstream | 0.23 |
| [[p03_sp_visual_frontend_marketing]] | upstream | 0.22 |
| [[bld_tools_landing_page]] | related | 0.21 |
| [[p08_ac_visual_frontend_marketing]] | downstream | 0.20 |
| [[spec_n02_visual_frontend_engineer]] | downstream | 0.19 |
| [[spec_n02_part2]] | downstream | 0.19 |
| [[p01_kc_brand_tokens_pipeline]] | upstream | 0.19 |
