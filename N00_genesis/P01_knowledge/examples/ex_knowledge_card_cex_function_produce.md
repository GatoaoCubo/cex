---
id: p01_kc_cex_function_produce
kind: knowledge_card
pillar: P01
title: "CEX Function PRODUCE — Executing Work and Generating Output"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, produce, chain, workflow, dag, meta-prompt, completion]
tldr: "PRODUCE gera output final (texto, codigo, dados) via 5 tipos — a funcao de EXECUCAO do pipeline LLM"
when_to_use: "Entender como LLMs materializam output e a fronteira entre PRODUCE (output externo) e REASON (pensamento interno)"
keywords: [produce, chain, workflow, dag, meta_prompt, completion, generation]
long_tails:
  - "Qual a diferenca entre PRODUCE e REASON no CEX"
  - "Quais os 5 tipos de producao na taxonomia CEX"
axioms:
  - "SEMPRE distinguir REASON (pensamento interno) de PRODUCE (output externo)"
  - "NUNCA usar workflow quando chain linear resolve"
linked_artifacts:
  primary: p01_kc_cex_function_call
  related: [p01_kc_cex_function_reason, p01_kc_cex_function_constrain]
density_score: null
data_source: "https://arxiv.org/abs/2210.03629"
related:
  - chain-builder
  - p01_kc_cex_lp03_prompt
  - p01_kc_cex_pipeline_execution
  - p01_kc_chain
  - bld_collaboration_chain
  - p01_kc_cex_llm_function_concept
  - p03_sp_chain_builder
  - p01_kc_cex_function_reason
  - p01_kc_workflow
  - workflow-builder
---

## Summary

PRODUCE gera o output principal do pipeline LLM — texto, codigo, dados estruturados, artefatos. Com 5 tipos (6% do CEX), cobre de completions brutas a DAGs complexos com dependencias. Fronteira critica: REASON produz PENSAMENTO (operacao interna, meta-cognitiva); PRODUCE produz OUTPUT (operacao externa, artefato consumivel). A funcao menos diferenciadora — todos fazem PRODUCE bem; o diferencial esta nas funcoes ao redor (INJECT, REASON, CONSTRAIN, GOVERN).

## Spec

| Tipo | LP | Complexidade | Funcao | Detalhe |
|------|-----|-------------|--------|---------|
| completion | P03 | Baixa | Output bruto | Texto pre-pos-processamento |
| meta_prompt | P03 | Media | Prompt gera prompt | Auto-referencialidade aplicada |
| chain | P12 | Media | Sequencia linear | Output A alimenta input B |
| workflow | P12 | Alta | Grafo com branches | Condicionais, loops, paralelismo |
| dag | P12 | Alta | Grafo aciclico | Dependencias sem ciclos |

Hierarquia de complexidade: completion < meta_prompt < chain < workflow.
DAG e workflow cobrem necessidades distintas: DAG garante aciclicidade
(execucao em ordem topologica), workflow permite ciclos e loops.
chain e a forma minima de composicao: A -> B -> C linear.
PRODUCE e a 5a funcao no pipeline (apos INJECT, BECOME, REASON, CALL).
Otimizacoes de REASON (melhorar raciocinio) e de PRODUCE (melhorar
geracao) requerem tecnicas fundamentalmente diferentes.
completion eh materia-prima — output bruto antes de CONSTRAIN formatar.
meta_prompt eh o artefato metacircular do CEX: prompt que gera prompt,
auto-referencialidade aplicada. Nao confundir com prompt_template
(CONSTRAIN) que parametriza prompts existentes.
LangChain Chains, DSPy Modules, Haystack Pipelines — todos confirmam
que composicao de operacoes LLM eh cidadao de primeira classe.
PRODUCE eh a razao de existir do LLM, mas paradoxalmente a funcao
menos diferenciadora. Todos os modelos fazem PRODUCE. O que separa
sistemas mediocres de excelentes sao as 7 funcoes ao redor.

## Patterns

| Trigger | Action |
|---------|--------|
| Output simples sem composicao | completion direto |
| Pipeline linear sem branches | chain (A -> B -> C) |
| Pipeline com decisoes condicionais | workflow com branches |
| Dependencias complexas sem ciclos | dag com ordem topologica |
| Gerar prompts otimizados automaticamente | meta_prompt (prompt que gera prompt) |
| Mesmo padrao aplicado a inputs variados | chain + prompt_template (CONSTRAIN) |
| Tarefa requer raciocinio antes de gerar | REASON primeiro, PRODUCE depois |

## Code

<!-- lang: python | purpose: chain and workflow PRODUCE patterns -->
```python
# chain: composicao linear A -> B -> C
chain = [summarize, translate, format_md]
result = input_text
for step in chain:
    result = step(result)  # output de cada step alimenta o proximo

# workflow: grafo com branches condicionais
if complexity(task) > 0.7:
    result = workflow.run(dag=dependency_graph, parallel=True)
else:
    result = chain_run(steps=[analyze, produce], input=task)

# meta_prompt: prompt que gera prompt otimizado
meta = "Generate a prompt that extracts product specs as JSON"
optimized_prompt = llm.complete(meta)  # PRODUCE de segundo ordem
```

## Anti-Patterns

- Workflow para pipeline linear simples (complexidade sem necessidade)
- DAG com ciclos implicitos (viola definicao, use workflow)
- PRODUCE sem REASON previo em tarefas complexas (output raso)
- Completion como tipo persistente (use chain ou workflow)
- meta_prompt sem avaliacao de qualidade (espiral de degradacao)
- Confundir REASON (chain-of-thought) com PRODUCE (texto final)

## References

- source: https://arxiv.org/abs/2210.03629
- source: https://arxiv.org/abs/2305.10601
- related: p01_kc_cex_function_reason
- related: p01_kc_cex_function_call
- related: p01_kc_cex_function_constrain

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[chain-builder]] | downstream | 0.34 |
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.31 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.30 |
| [[p01_kc_chain]] | sibling | 0.30 |
| [[bld_collaboration_chain]] | downstream | 0.29 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.29 |
| [[p03_sp_chain_builder]] | downstream | 0.28 |
| [[p01_kc_cex_function_reason]] | sibling | 0.26 |
| [[p01_kc_workflow]] | sibling | 0.26 |
| [[workflow-builder]] | downstream | 0.25 |
