---
id: p01_kc_cex_function_reason
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Function REASON — Structured Thinking Before Action"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, reason, chain-of-thought, planning, routing]
tldr: "REASON gera tokens internos (CoT, ReAct, planning) antes de agir — 7 tipos que separam pensar de produzir"
when_to_use: "Entender por que raciocinio e funcao separada de geracao e como tipificar thinking patterns"
keywords: [reason, chain-of-thought, react, planner, router, tree-of-thought]
long_tails:
  - "Qual a diferenca entre chain of thought e tree of thought no CEX"
  - "Por que REASON e funcao separada de PRODUCE no CEX"
axioms:
  - "SEMPRE usar REASON antes de CALL em tarefas complexas"
  - "NUNCA confundir planner (gera plano) com router (seleciona handler)"
linked_artifacts:
  primary: p01_kc_cex_function_call
  related: [p01_kc_cex_function_become, p01_kc_cex_function_inject]
density_score: null
data_source: "https://arxiv.org/abs/2309.07864"
related:
  - p01_kc_cex_lp03_prompt
  - p01_kc_cex_function_produce
  - p01_kc_cex_llm_function_concept
  - p03_plan_task_decomposition
  - p01_kc_academic_agent_patterns
  - p01_kc_cex_pipeline_execution
  - planning-strategy-builder
  - bld_output_template_planning_strategy
  - cex_llm_vocabulary_whitepaper
  - p01_kc_chain_of_thought
---

## Summary

REASON e a operacao meta-cognitiva de PENSAR antes de agir. O LLM gera tokens para si mesmo (chain-of-thought, planning, decomposicao) antes de gerar output final. Com 7 tipos (9% do CEX), e arquiteturalmente distinta de PRODUCE — confirmado por DSPy (ChainOfThought separado de Predict), Semantic Kernel (Planner como tipo de primeira classe) e literatura academica (Wang et al. 2023).

## Spec

| Tipo | LP | Funcao | Detalhe |
|------|-----|--------|---------|
| chain_of_thought | P03 | Raciocinio linear | Passo a passo explicito ate conclusao |
| react | P03 | Think-Act-Observe | Intercala raciocinio com acoes no ambiente |
| planner | P03 | Plano dinamico | Cria workflow em runtime baseado no goal |
| router | P02 | Selecao de handler | Direciona input ao especialista correto |
| tree_of_thought | P03 | Raciocinio paralelo | Multiplas ramificacoes com avaliacao |
| decomposition | P03 | Quebra de problema | Sub-problemas independentes tratados em partes |
| goal | P03 | Criterio de sucesso | Objetivo mensuravel que guia REASON |

Hierarquia de complexidade: CoT < ReAct < Planner < ToT.
CoT e linear (1 caminho). ReAct intercala com ambiente.
Planner gera sequencia completa. ToT explora N caminhos.
Router NAO e raciocinio profundo — e classificacao rapida.
REASON produz tokens INTERNOS (para o proprio LLM), nao output final.
Separacao REASON vs PRODUCE: DSPy ChainOfThought != Predict.

## Code

<!-- lang: python | purpose: ReAct reasoning loop -->
```python
# ReAct: Thought -> Action -> Observation -> repeat
thought = reason("Preciso verificar preco atual do produto")
action = call(tool="scraper", url=product_url)
observation = parse(action.result)
thought = reason(f"Preco={observation.price}, comparar com meta")
# REASON intercala com CALL ate resolver
```

## Patterns

| Trigger | Action |
|---------|--------|
| Tarefa requer logica explicita | Usar chain_of_thought |
| Tarefa requer interacao com ambiente | Usar react (think-act-observe) |
| Sequencia de acoes imprevisivel | Usar planner para gerar workflow |
| Multiplos handlers disponiveis | Router seleciona o melhor |
| Problema com multiplas solucoes | tree_of_thought para explorar |
| Problema grande demais para resolver | decomposition em sub-tasks |

## Anti-Patterns

- CoT em tarefas triviais (overhead sem ganho)
- Planner com acoes hardcoded (use workflow, nao planner)
- Router com 10+ opcoes (LLM nao discrimina bem)
- Confundir planner com router (sequencia vs selecao)
- REASON sem INJECT (raciocinar sem dados = alucinacao)
- Pular REASON e ir direto a CALL (acao sem plano)

## References

- source: https://arxiv.org/abs/2309.07864
- source: https://arxiv.org/abs/2305.10601
- related: p01_kc_cex_function_call
- related: p01_kc_cex_function_inject

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.37 |
| [[p01_kc_cex_function_produce]] | sibling | 0.31 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.25 |
| [[p03_plan_task_decomposition]] | downstream | 0.24 |
| [[p01_kc_academic_agent_patterns]] | sibling | 0.22 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.21 |
| [[planning-strategy-builder]] | downstream | 0.17 |
| [[bld_output_template_planning_strategy]] | downstream | 0.17 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.16 |
| [[p01_kc_chain_of_thought]] | sibling | 0.16 |
