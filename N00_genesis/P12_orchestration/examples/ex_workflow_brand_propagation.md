---
id: p12_wf_brand_propagation
name: brand_propagation
description: "Propaga identidade de marca organization em 4 fases: guidelines -> tokens -> CSS -> inject em prompts de agent_groups"
user_invocable: true
trigger: "Quando precisar atualizar ou propagar brand identity para agent_groups ou frontend"
phases:
  - "1. EDIT — Atualizar brand-guidelines.md (source-of-truth)"
  - "2. SYNC — Extrair valores para design-tokens.json (DTCG format)"
  - "3. GENERATE — Gerar CSS custom properties a partir dos tokens"
  - "4. INJECT — Injetar contexto de marca em prompts de agent_groups"
when_to_use: "Atualizar voz, personalidade, tokens visuais ou injetar brand context em content generation"
when_not_to_use: "Criar brand strategy do zero (use marca-agent); implementar CSS em componentes (use styling-agent)"
examples:
  - "/brand edit --file brand-guidelines.md"
  - "/brand sync"
  - "/brand generate --format css"
  - "/brand inject --agent_group lily --task 'gerar copy para Instagram'"
pillar: P12
kind: workflow
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: builder_agent
domain: brand
quality: 9.1
tags: [brand, design-system, propagation, tokens, identity]
tldr: "Source-of-truth brand propagation: guidelines -> tokens -> CSS -> prompt injection across all agent_groups"
density_score: 0.91
sub_skills: [edit, sync, generate, inject]
platforms: [claude]
related:
  - p01_kc_brand_tokens_pipeline
  - p01_kc_brand_skill
  - p03_sp_brand_nucleus
  - p02_agent_commercial_nucleus
  - p01_kc_brand_propagation_arch
  - spec_n06_brand_verticalization
  - p12_dr_commercial
  - p02_agent_brand_nucleus
  - p01_kc_brand_book_patterns
  - p04_browser_design_extractor
---

# Brand Propagation Skill

## Purpose
brand_propagation gerencia a **propagacao de identidade de marca** no organization. Guidelines sao a unica fonte-da-verdade e se propagam deterministicamente ate o contexto de prompt dos agent_groups. Nenhum agent_group hardcoda valores de marca — tudo vem do pipeline.

## Workflow Phases

### Phase 1: EDIT (Guidelines)
- **Input**: `brand-guidelines.md` (source-of-truth file)
- **Action**: Editar voz, personalidade, tons, regras visuais. Cada alteracao gera changelog entry
- **Output**: Updated `brand-guidelines.md` com version bump
- **Voice Framework**:
  - Personality: tecnico-confiante, direto, sem jargao vazio
  - Tone variations: formal (docs), casual (social), urgente (alerts)
  - Language rules: pt-BR, ASCII-only em configs, sem emojis em code

### Phase 2: SYNC (Tokens)
- **Input**: Updated `brand-guidelines.md`
- **Action**: Extrair cores, tipografia, espacamento para `design-tokens.json` (DTCG format). Tres camadas: primitives (raw values) -> semantic (intent) -> component (usage)
- **Output**: `design-tokens.json` validado contra DTCG spec
- **Token Naming**: `--{category}-{item}-{variant}-{state}` (e.g. `--color-primary-default`)

### Phase 3: GENERATE (CSS)
- **Input**: `design-tokens.json`
- **Action**: Gerar CSS custom properties. Dark mode overrides apenas semantic layer (primitives intocados)
- **Output**: `design-tokens.css` consumivel por frontend (fresh-start)
- **Size**: Tipicamente < 2KB (flat custom properties, no nesting)

### Phase 4: INJECT (Prompt Context)
- **Input**: `brand-guidelines.md` + `design-tokens.json`
- **Action**: Montar brand context block e injetar em handoffs de marketing_agent (marketing), builder_agent (components), marca-agent
- **Output**: Brand-aware prompt section (~500 tokens) com voz, tons, cores, regras
- **Format**: Markdown block com ## Brand Context header

## Anti-Patterns
- Editar tokens diretamente sem atualizar guidelines: tokens divergem da fonte-da-verdade
- Pular sync apos edit: frontend fica com valores antigos, inconsistencia visual
- Hardcoded brand values em prompts: qualquer mudanca exige grep+replace manual
- Guidelines > 200 linhas monoliticas: separar em sub-arquivos via references/

## Metrics
| Metrica | Valor | Nota |
|---------|-------|------|
| Propagation time | < 5s | Edit -> inject em uma execucao |
| Token file size | < 2KB | DTCG JSON flat |
| CSS output size | < 2KB | Custom properties only |
| Inject context size | ~500 tokens | Dentro do budget de agent_group |
| Supported agent_groups | 3 | marketing_agent, builder_agent, marca-agent |

## Usage

```bash
/brand edit --file brand-guidelines.md
/brand sync
/brand generate --format css
/brand inject --agent_group lily --task "gerar copy para Instagram"
```

## Input / Output

```yaml
input:
  command: enum     # edit|sync|generate|inject
  file: string      # Path to guidelines (edit phase)
  agent_group: string # Target agent_group (inject phase)
  format: enum      # css|scss|json (generate phase)

output:
  guidelines: path  # Updated brand-guidelines.md
  tokens: path      # design-tokens.json (DTCG format)
  css: path         # design-tokens.css (<2KB)
  context: string   # Brand prompt block (~500 tokens)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_brand_tokens_pipeline]] | upstream | 0.46 |
| [[p01_kc_brand_skill]] | upstream | 0.46 |
| [[p03_sp_brand_nucleus]] | upstream | 0.36 |
| [[p02_agent_commercial_nucleus]] | upstream | 0.35 |
| [[p01_kc_brand_propagation_arch]] | upstream | 0.34 |
| [[spec_n06_brand_verticalization]] | upstream | 0.31 |
| [[p12_dr_commercial]] | related | 0.31 |
| [[p02_agent_brand_nucleus]] | upstream | 0.31 |
| [[p01_kc_brand_book_patterns]] | upstream | 0.30 |
| [[p04_browser_design_extractor]] | upstream | 0.29 |
