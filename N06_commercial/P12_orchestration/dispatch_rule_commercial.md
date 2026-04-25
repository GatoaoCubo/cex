---
id: p12_dr_commercial
kind: dispatch_rule
8f: F8_collaborate
pillar: P12
title: "N06 Dispatch Rule — Brand + Monetization Routing"
version: 4.0.0
created: 2026-03-30
updated: 2026-04-01
author: n06_commercial
domain: brand-identity-monetization
keywords: [brand, marca, identidade, brand-book, persona, arquetipo, voz, naming, tagline, posicionamento, UVP, ICP, design-tokens, paleta, pricing, curso, funnel, monetizar, receita, upsell, checkout, infoproduto, hotmart, kiwify, stripe]
model: sonnet
model_escalation: opus
mcps: [fetch, stripe, hotmart]
quality: 9.1
updated: 2026-04-07
tags: [dispatch_rule, commercial, N06, brand, monetization, routing]
tldr: "N06 routes brand discovery + identity + monetization. 25 keywords, dual-model (sonnet default, opus for brand-from-scratch). N06 runs FIRST on new CEX instances."
density_score: 0.94
axioms:
  - "N06 ALWAYS runs first on new instances — brand identity precedes all other nucleus work."
  - "ALWAYS escalate to Opus for brand-from-scratch — Sonnet handles incremental updates."
linked_artifacts:
  primary: p02_agent_commercial_nucleus
  related: [p12_wf_commercial, p03_sp_commercial_nucleus, p08_ac_commercial_nucleus]
related:
  - p02_agent_commercial_nucleus
  - spec_n06_brand_verticalization
  - p03_sp_brand_nucleus
  - p08_ac_commercial_nucleus
  - p02_agent_brand_nucleus
  - p08_ac_brand_nucleus
  - p02_mm_commercial_nucleus
  - agent_card_n06
  - p03_sp_commercial_nucleus
  - p12_wf_commercial
---

# N06 Dispatch Rule — Brand + Monetization

## Priority

**N06 is the FIRST nucleus to run on a new CEX instance.**
Brand identity must exist (brand_config.yaml) before other nuclei produce branded output.

Priority: 10 (highest — brand blocks all other branded output)

## Keywords (25)

### Brand Keywords (13)
`brand`, `marca`, `identidade`, `brand-book`, `persona`, `arquétipo`, `voz`, `naming`, `tagline`, `posicionamento`, `UVP`, `ICP`, `design-tokens`

### Monetization Keywords (12)
`pricing`, `precificar`, `curso`, `funnel`, `funil`, `monetizar`, `receita`, `upsell`, `checkout`, `infoproduto`, `hotmart`, `kiwify`

## Trigger Phrases

### Brand Triggers (EN canonical + PT-BR community aliases)
- "create brand book" / "criar brand book"
- "discover brand identity" / "descobrir identidade da marca"
- "define brand voice" / "definir voz da marca"
- "fill brand_config" / "preencher brand_config"
- "audit brand consistency" / "auditar marca"
- "propagate brand to nuclei" / "propagar marca"
- "select archetype" / "selecionar arquetipo"
- "create color palette" / "criar paleta de cores"

### Monetization Triggers (EN canonical + PT-BR community aliases)
- "price a product" / "precificar produto"
- "build sales funnel" / "montar funil de vendas"
- "structure online course" / "estruturar curso online"
- "design upsell sequence" / "sequencia de upsell"
- "revenue model" / "modelo de receita"
- "optimize checkout" / "otimizar checkout"
- "create pricing page" / "criar pagina de precos"
- "calculate LTV" / "calcular LTV"
- "design tier structure" / "montar tiers"

## Model Selection

| Context | Model | Rationale |
|---------|-------|-----------|
| Brand Discovery interview | sonnet | Empathy + structured questioning |
| Brand Book generation | sonnet | Creative + structured output |
| Brand-from-scratch (minimal input) | opus | Deep reasoning for sparse data |
| Brand Audit | sonnet | Systematic scoring |
| Pricing strategy | sonnet | Analytical + persuasive |
| Funnel copywriting | sonnet | Creative + conversion-focused |
| Complex revenue modeling | opus | Multi-variable analysis |

## Receives From

| Source | What | When |
|--------|------|------|
| N01 Research | Market data, competitor analysis | Before brand positioning |
| N07 Admin | New instance trigger | "Initialize brand" |
| User | Brand discovery answers | During interview |

## Hands Off To

| Target | What | When |
|--------|------|------|
| N02 Marketing | BRAND_VOICE + BRAND_COLORS | After brand_config.yaml exists |
| N03 Builder | BRAND_COLORS + BRAND_FONTS + BRAND_STYLE | After visual identity defined |
| N05 Operations | BRAND_NAME + BRAND_LOGO_URL | After config propagated |
| N04 Knowledge | BRAND_CATEGORY + BRAND_CONTENT_PILLARS | After positioning defined |

## Handoff Format

```yaml
# .cex/runtime/handoffs/n06_to_n02.md
source: N06
target: N02
type: brand_propagation
payload:
  brand_config: .cex/brand/brand_config.yaml
  sections: [voice, visual]
  message: "Brand Book done. Use BRAND_VOICE for all copy. Use BRAND_COLORS for all HTML."
```

## NOT N06 (route elsewhere)

| Request | Route To | Why |
|---------|----------|-----|
| Deploy landing page | N05 | Infrastructure, not brand |
| Write production code | N05 | Engineering, not strategy |
| Research market size | N01 | Research, not brand |
| Editorial content | N02 | Marketing copy, not identity |
| Build UI components | N03 | Design, not brand definition |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_commercial_nucleus]] | upstream | 0.67 |
| [[spec_n06_brand_verticalization]] | upstream | 0.62 |
| [[p03_sp_brand_nucleus]] | upstream | 0.62 |
| [[p08_ac_commercial_nucleus]] | upstream | 0.59 |
| [[p02_agent_brand_nucleus]] | upstream | 0.57 |
| [[p08_ac_brand_nucleus]] | upstream | 0.53 |
| [[p02_mm_commercial_nucleus]] | upstream | 0.51 |
| [[agent_card_n06]] | upstream | 0.49 |
| [[p03_sp_commercial_nucleus]] | upstream | 0.48 |
| [[p12_wf_commercial]] | related | 0.47 |
