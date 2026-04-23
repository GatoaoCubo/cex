---
id: p01_kc_slide_generation
kind: knowledge_card
pillar: P01
title: "CSV-Driven Slide Generation Pipeline with Design Tokens and Emotion Arcs"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: content_generation
quality: 9.1
tags: [slides, html-generation, design-tokens, chart-js, emotion-arc, csv-pipeline, presentation]
tldr: "Pipeline gera slides HTML via 8 CSVs (estrategia, layout, cor, tipografia) com Chart.js, design tokens e Duarte Sparkline emotion arcs"
when_to_use: "Gerar apresentacoes HTML data-driven com estrategia de engajamento baseada em emotion arcs"
keywords: [slide-generation, design-tokens, chart-js, sparkline, csv-pipeline, duarte-method]
long_tails:
  - "Como gerar slides HTML automaticamente a partir de dados CSV"
  - "Como aplicar emotion arcs em apresentacoes para manter engajamento"
axioms:
  - "SEMPRE usar design tokens (var(--x)) — NUNCA hardcoded hex"
  - "SEMPRE usar Chart.js para dados — NUNCA CSS-only bars"
  - "NUNCA colocar mais de 1 mensagem principal por slide"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://www.duarte.com/resources/books/resonate/"
related:
  - kc_webinar_script
  - bld_output_template_pitch_deck
  - p03_sp_pitch_deck_builder
  - bld_instruction_pitch_deck
  - p05_qg_pitch_deck
  - p01_kc_marp_cli
  - bld_collaboration_pitch_deck
  - bld_tools_pitch_deck
  - p03_sp_webinar_script_builder
  - p01_kc_brand_propagation_arch
---

## Summary

Pipeline CSV-driven que gera slides HTML com design tokens, Chart.js e emotion arcs (Duarte Sparkline).
8 CSVs controlam estrategia (15 deck structures), layout (25 variants), tipografia, cor, backgrounds, copy (25 formulas como PAS/AIDA/FAB), charts (25 tipos Chart.js) e animacoes CSS.
BM25 contextual search seleciona componentes por posicao no deck e emocao anterior.
Token validator (slide-token-validator.py) rejeita qualquer hardcoded hex no HTML final.

## Spec

| CSV | Conteudo | Qtd |
|-----|----------|-----|
| slide-strategies | Deck structures + emotion arcs + sparkline beats | 15 |
| slide-layouts | Layout variants + component + animations | 25 |
| slide-layout-logic | Goal → Layout + break_pattern flag | — |
| slide-typography | Content type → Typography scale | — |
| slide-color-logic | Emotion → Color treatment | — |
| slide-backgrounds | Slide type → Image category (Pexels/Unsplash) | — |
| slide-copy | Copywriting formulas (PAS, AIDA, FAB) | 25 |
| slide-charts | Chart.js tipos com config | 25 |

Pipeline por slide: layout-logic → typography → color-logic → backgrounds → animations → HTML.
Duarte Sparkline calcula break patterns em 1/3 e 2/3 do deck, alternando "What Is" (frustration) com "What Could Be" (hope).
Design system persistido em MASTER.md (global) + pages/*.md (overrides por pagina).
Retrieval: page-specific override → fallback MASTER — garante consistencia visual.

## Patterns

| Trigger | Action |
|---------|--------|
| Novo deck solicitado | BM25 busca em slide-strategies.csv por estrutura + emotion arc |
| Slide na posicao 1/3 ou 2/3 | Ativar break_pattern flag (inverter emocao) |
| Dados quantitativos no slide | Chart.js com tokens (borderColor: var(--x)) |
| Brand customization | Persistir design system: MASTER.md + page overrides |
| Busca por componente especifico | Contextual search: --position N --prev-emotion X |

## Anti-Patterns

- Hardcoded hex (#FF6B6B) em HTML — token validator rejeita
- CSS-only bars para dados — sempre Chart.js via CDN
- Slide sem navegacao (setas teclado, click, progress bar)
- Deck monotono sem emotion arc — audiencia desengaja
- Slide com multiplas mensagens (cognitive overload)

## Code

<!-- lang: python | purpose: contextual slide search with BM25 -->
```bash
# Busca basica: encontra estrategia de deck
python scripts/search-slides.py "investor pitch"

# Busca contextual: considera posicao e emocao anterior
python scripts/search-slides.py "problem slide" \
  --context --position 2 --total 9

# Busca por dominio especifico
python scripts/search-slides.py "revenue growth" -d chart
```

```css
/* Design tokens — source of truth */
background: var(--slide-bg);
color: var(--color-primary);
font-family: var(--typography-font-heading);

/* Chart.js com tokens */
borderColor: var(--color-primary);
```

## References

- source: https://www.duarte.com/resources/books/resonate/
- source: https://www.chartjs.org/docs/latest/
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_webinar_script]] | sibling | 0.44 |
| [[bld_output_template_pitch_deck]] | downstream | 0.39 |
| [[p03_sp_pitch_deck_builder]] | downstream | 0.36 |
| [[bld_instruction_pitch_deck]] | downstream | 0.34 |
| [[p05_qg_pitch_deck]] | downstream | 0.30 |
| [[p01_kc_marp_cli]] | sibling | 0.29 |
| [[bld_collaboration_pitch_deck]] | downstream | 0.28 |
| [[bld_tools_pitch_deck]] | downstream | 0.26 |
| [[p03_sp_webinar_script_builder]] | downstream | 0.25 |
| [[p01_kc_brand_propagation_arch]] | sibling | 0.23 |
