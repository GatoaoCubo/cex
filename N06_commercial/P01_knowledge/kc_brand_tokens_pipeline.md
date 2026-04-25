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

Brand como sistema vivo onde um arquivo Markdown (brand-guidelines.md) e a unica fonte de verdade. Scripts de sync propagam automaticamente para design tokens JSON, CSS variables e contexto de prompt. Elimina desincronizacao entre design e codigo.

## Conceito Central

O problema central de brand em projetos de software e a fragmentacao: cores definidas num Figma, tipografia num CSS, tom de voz num documento que ninguem le. A solucao e tratar brand como pipeline de dados: uma fonte editavel por humanos (Markdown) que se transforma automaticamente em artefatos consumiveis por maquinas.

A arquitetura usa 3 camadas de tokens: primitivos (valores brutos como #E8B4B8), semanticos (roles como primary, accent) e componentes (aplicacoes como button-bg, header-text). Cada camada adiciona significado sem perder rastreabilidade ate a fonte. O sync e unidirecional: guidelines.md e a unica entrada, todo o resto e gerado.

O voice framework complementa o visual com 4 dimensoes: personality traits, tone variations, language rules e content examples. Isso permite que LLMs gerem copy on-brand automaticamente usando o contexto injetado via script.

## Arquitetura/Patterns

| Camada | Arquivo | Papel |
|--------|---------|-------|
| Fonte | brand-guidelines.md | Editavel por humanos |
| Tokens | design-tokens.json | Primitivo, semantico, componente |
| CSS | design-tokens.css | CSS variables para import |
| Contexto | inject-brand-context.cjs | Injeta brand em prompts LLM |

Pipeline de sync:
```
guidelines.md
  -> sync-brand-to-tokens.cjs
    -> design-tokens.json
      -> design-tokens.css
        -> import em componentes
```

Sistema de cores (3 tipos por brand):
- **Primary**: CTAs, headers — cor principal da marca
- **Secondary**: backgrounds, bordas — suporte visual
- **Accent**: badges, alerts — destaque pontual

Cada cor inclui: hex, HSL (para opacity), on-color (texto sobre fundo), semantic role. Tipografia segue pattern similar: heading font + body font com tamanhos e pesos definidos.

Validacao automatica: script detecta valores hardcoded em componentes que deveriam usar tokens. Pre-flight checklist antes de publicar qualquer asset.

Escala do pattern: projetos com 55+ CSVs de design usam a mesma pipeline — cada CSV e um dominio visual (cores, tipografia, layouts) e brand-guidelines.md governa todos. O sync unidirecional garante que a unica operacao humana e editar o Markdown fonte; todo o resto e derivado automaticamente via scripts Node.js.

## Exemplos Praticos

| Operacao | Comando | Resultado |
|----------|---------|-----------|
| Sync brand | `node sync-brand-to-tokens.cjs` | Tokens atualizados |
| Injetar contexto | `node inject-brand-context.cjs` | Brand em prompt |
| Validar asset | `node validate-asset.cjs <path>` | Nome, formato, tamanho |
| Extrair cores | `node extract-colors.cjs --palette` | Paleta atual |

Template minimo para nova marca:
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

- Editar tokens JSON diretamente sem passar por guidelines
- Multiplas fontes de verdade (Figma + CSS + doc separados)
- Cores sem semantica — hex puro sem token nomeado
- Voice framework vago ("seja profissional" nao e acionavel)
- Assets publicados sem passar pelo approval checklist
- CSS com font-family literal ao inves de var(--typography-*)

## Referencias

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
