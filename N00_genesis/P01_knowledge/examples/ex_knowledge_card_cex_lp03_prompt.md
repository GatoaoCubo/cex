---
id: p01_kc_cex_lp03_prompt
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP03 Prompt — Como a LLM Fala (10 Tipos de Engenharia de Prompt)"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [cex, lp03, prompt, reason, constrain, template, chain-of-thought]
tldr: "P03 Prompt governa comunicacao do LLM via 10 tipos — de system_prompt a meta_prompt — cobrindo 5 funcoes LLM"
when_to_use: "Classificar artefatos de prompt ou entender como P03 orquestra raciocinio e formato"
keywords: [prompt-template, system-prompt, cot, react, few-shot, meta-prompt, chain]
long_tails:
  - "Quais tipos de prompt existem no CEX"
  - "Diferenca entre chain_of_thought e react no CEX"
axioms:
  - "SEMPRE usar {{MUSTACHE}} para variaveis tier-1"
  - "NUNCA misturar instrucao (P03) com conhecimento (P01)"
linked_artifacts:
  primary: p01_kc_cex_lp01_knowledge
  related: [p01_kc_cex_lp02_model, p01_kc_cex_lp04_tools]
density_score: 1.0
data_source: "https://arxiv.org/abs/2201.11903"
related:
  - p01_kc_cex_function_reason
  - p01_kc_cex_llm_function_concept
  - p01_kc_cex_function_produce
  - p01_kc_cex_pipeline_execution
  - p01_kc_cex_lp02_model
  - p01_kc_cex_lp04_tools
  - p01_kc_cex_function_become
  - p01_kc_cex_function_inject
  - p01_kc_cex_lp01_knowledge
  - bld_architecture_dataset_card
---

## Quick Reference

topic: LP03 Prompt | scope: 10 tipos de artefato | criticality: high
funcoes_llm: BECOME + INJECT + REASON + PRODUCE + CONSTRAIN
analogia: idioma + sotaque + registro

## Conceitos Chave

- P03 responde: "como esta entidade se comunica?"
- LP mais populoso do CEX (10 tipos) — linguagem eh o meio
- system_prompt usa BECOME (identidade persistente)
- user_prompt e few_shot usam INJECT (tarefa + exemplos)
- chain_of_thought e react usam REASON (raciocinio)
- chain e meta_prompt usam PRODUCE (gerar outputs)
- prompt_template usa CONSTRAIN (molde com variaveis)
- Variaveis: {{MUSTACHE}} tier-1, [BRACKET] tier-2 authoring
- router_prompt classifica input e roteia para handler
- planner decompoe tarefa em plano executavel de steps
- P03 eh moldado por P02 (identidade define registro)
- P03 consome P01 (templates referenciam knowledge cards)
- P03 eh otimizado por P11 (prompts melhoram com feedback)
- CoT: raciocinio explicito sem tools (Wei et al. 2022)
- ReAct: Thought/Action/Observation com tools (Yao 2023)
- meta_prompt gera/otimiza outros prompts (MIPRO, OPRO)
- chain encadeia prompts: output A vira input B (pipeline)

## Fases

1. Identidade: system_prompt define papel via BECOME
2. Contexto: user_prompt + few_shot injetam tarefa via INJECT
3. Raciocinio: CoT ou ReAct estruturam pensamento via REASON
4. Producao: chain ou meta_prompt geram outputs via PRODUCE
5. Restricao: prompt_template constrange formato via CONSTRAIN

## Regras de Ouro

- SEMPRE separar system_prompt (quem) de user_prompt (o que)
- SEMPRE usar few_shot com min 2, max 5 exemplos
- NUNCA hardcodar dados em prompt_template (usar variaveis)
- NUNCA usar CoT quando task eh simples (overhead sem ganho)
- SEMPRE preferir ReAct sobre CoT quando tools disponiveis

## Comparativo

| Tipo | Funcao LLM | Proposito | Core |
|------|------------|-----------|------|
| system_prompt | BECOME | Identidade + regras | sim |
| user_prompt | INJECT | Tarefa especifica | sim |
| prompt_template | CONSTRAIN | Molde com {{vars}} | sim |
| few_shot | INJECT | Exemplos input/output | sim |
| chain_of_thought | REASON | Raciocinio step-by-step | nao |
| react | REASON | Thought/Action/Observation | nao |
| chain | PRODUCE | Sequencia de prompts | nao |
| meta_prompt | PRODUCE | Prompt que gera prompts | nao |
| router_prompt | REASON | Classificar + rotear input | nao |
| planner | REASON | Decompor tarefa em steps | nao |

## Flow

```
[system_prompt] -- BECOME --> identidade ativa
        |
[user_prompt + few_shot] -- INJECT --> contexto
        |
[CoT / ReAct / planner] -- REASON --> raciocinio
        |
[chain / meta_prompt] -- PRODUCE --> output
        |
[prompt_template] -- CONSTRAIN --> formato final
```

## References

- source: https://arxiv.org/abs/2201.11903
- source: https://arxiv.org/abs/2210.03629
- deepens: p01_kc_cex_lp01_knowledge
- related: p01_kc_cex_lp02_model


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_function_reason]] | sibling | 0.37 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.35 |
| [[p01_kc_cex_function_produce]] | sibling | 0.34 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.29 |
| [[p01_kc_cex_lp02_model]] | sibling | 0.28 |
| [[p01_kc_cex_lp04_tools]] | sibling | 0.25 |
| [[p01_kc_cex_function_become]] | sibling | 0.24 |
| [[p01_kc_cex_function_inject]] | sibling | 0.22 |
| [[p01_kc_cex_lp01_knowledge]] | sibling | 0.22 |
| [[bld_architecture_dataset_card]] | downstream | 0.22 |
