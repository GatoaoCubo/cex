---
id: p01_kc_lp03_prompt
kind: knowledge_card
pillar: P01
title: "P03 Prompt: Como o Agente Fala"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [prompt, system_prompt, template, variables, chain]
tldr: "P03 define 5 tipos de prompt (system, action, template, instruction, chain) com sintaxe de variaveis em 2 tiers: {{MUSTACHE}} para engine e [BRACKET] para humano"
when_to_use: "Quando precisar criar prompts, templates ou chains de prompts no CEX"
keywords: [system_prompt, prompt_template, action_prompt, chain, variables]
long_tails:
  - "qual a sintaxe correta de variaveis em templates CEX"
  - "como criar um system prompt valido em P03"
axioms:
  - "GOLDEN = Specific Frontmatter + Clear Purpose + Typed Variables + Structured Body + Quality Gates + Examples + Semantic Bridge"
linked_artifacts:
  agent: null
  skill: p04_skill_cex_forge
density_score: 0.86
---

# P03 Prompt: Como o Agente Fala

## Executive Summary
P03 governa como agentes se comunicam, com 5 tipos de artefato de prompt. A formula golden destilada de 257 HOPs mostra que semantic bridge esta presente em 60% dos templates golden. Sintaxe de variaveis usa 2 tiers: {{MUSTACHE}} resolvido por engine, [BRACKET] resolvido por humano/agente.

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 5 | system_prompt, action_prompt, prompt_template, instruction, chain |
| System prompt max_bytes | 4096 | Identidade + regras + output format |
| Template max_bytes | 8192 | Maior tipo — comporta examples + semantic bridge |
| Variable tier 1 | {{MUSTACHE}} | Resolvido por template engine |
| Variable tier 2 | [BRACKET] | Resolvido por humano/agente |
| Deprecated syntax | {single_curly} | NAO usar |
| Golden HOPs evidence | 257 | Base de destilacao |

## Patterns
1. System prompt: 3 secoes (identity, rules, output_format) — max 4096 bytes
2. Prompt template obriga variables_table (name/type/description/example) + quality_gates + examples
3. Semantic bridge obrigatorio se quality >= 8.0 (presente em 60% dos golden)
4. Chain type modela pipelines: prompt A > B > C com flow definido

## Anti-Patterns
1. {single_curly} syntax: deprecated, causa conflito com JSON/YAML
2. Template sem variables_table: impossivel de validar ou reusar
3. System prompt > 4096 bytes: excede context budget de muitos providers
4. Prompt sem quality_gates: nao tem criterio de validacao

## Application
O forge usa P03 templates para gerar system prompts de novos agentes. Cada agente ISO tem system_instruction.md (P03) como arquivo obrigatorio, garantindo que todo agente tem identidade formatada.

## References
1. P03_prompt/_schema.yaml (fonte de verdade)
2. DISTILL_GOLDEN_TPL_HOP_PATTERNS.md (257 golden HOPs)
3. P03_prompt/templates/ (templates validados)

## Retrieval

```yaml
query: "meta-construction"
kind_filter: knowledge_card
top_k: 5
threshold: 0.7
```

```bash
python _tools/cex_retriever.py "meta-construction" --top 5
```
