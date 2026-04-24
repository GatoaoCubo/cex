---
id: p01_kc_cex_pipeline_execution
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Pipeline Execution — The 8-Function Sequence From Input to Output"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.0
tags: [cex, pipeline, execution, 8-functions, boot-sequence, llm-processing]
tldr: "Pipeline de 8 funcoes (BECOME-INJECT-REASON-CALL-PRODUCE-CONSTRAIN-GOVERN-COLLABORATE) eh o processamento real de todo sistema LLM"
when_to_use: "Entender a sequencia completa de execucao de um agente ou agent_group LLM do input ao output"
keywords: [pipeline, execution, 8-functions, boot-sequence, processing]
long_tails:
  - "Qual a sequencia de execucao de um agente LLM do input ao output"
  - "Como funciona o boot sequence de um agent_group organization"
axioms:
  - "SEMPRE executar funcoes na ordem BECOME-INJECT-REASON-CALL-PRODUCE-CONSTRAIN-GOVERN-COLLABORATE"
  - "NUNCA pular BECOME (identidade precede tudo)"
linked_artifacts:
  primary: p01_kc_cex_function_become
  related: [p01_kc_cex_agent_group_concept, p01_kc_cex_cortex_enterprise]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_llm_function_concept
  - p01_kc_cex_function_become
  - p01_kc_cex_function_produce
  - spec_seed_words
  - p01_kc_cex_lp03_prompt
  - p01_kc_cex_agent_group_concept
  - p01_kc_cex_function_call
  - p01_kc_cex_taxonomy
  - p01_kc_cex_learning_package_concept
  - bld_architecture_dataset_card
---

## Summary

Todo sistema LLM executa as mesmas 8 funcoes na mesma ordem logica. Um prompt simples executa 1-2 (BECOME implicito + PRODUCE). Um agente executa 4-5. Um agent_group com lifecycle completo executa todas as 8. A diferenca entre prompt e agent_group nao eh de natureza — eh de completude. A boot sequence de um Cortex Enterprise eh ela mesma uma instanciacao dessas 8 funcoes.

## Spec

| # | Funcao | O que faz | Boot Equivalente |
|---|--------|-----------|------------------|
| 1 | BECOME | Configura identidade, persona, papel | Carregar PRIME.md + mental_model.yaml |
| 2 | INJECT | Fornece contexto, dados, conhecimento | Indexar pool de KCs via Brain MCP |
| 3 | REASON | Planeja, decompoe, decide estrategia | Ler tarefa, decompor em sub-tarefas |
| 4 | CALL | Usa ferramentas externas, APIs, MCPs | brain_query() + conectar MCPs |
| 5 | PRODUCE | Gera output: codigo, KCs, copy, deploy | Executar agent teams por agent_group |
| 6 | CONSTRAIN | Valida contra schemas, formata output | Validar tipos, aplicar templates |
| 7 | GOVERN | Avalia qualidade, testa, benchmarka | Quality gate >= 7.0, pre-commit hooks |
| 8 | COLLABORATE | Sinaliza, commita, despacha proximo | Signal file + git commit + next task |

## Patterns

| Trigger | Action |
|---------|--------|
| Prompt simples sem agente | Executa BECOME (implicito) + PRODUCE |
| Agente com tools | Adiciona INJECT + REASON + CALL ao pipeline |
| Agent_group completo | Executa todas as 8 funcoes em sequencia |
| Boot de Cortex Enterprise | Instancia as 8 funcoes como boot sequence |
| Falha em GOVERN (score < 7.0) | Loop de retry: REASON-PRODUCE-CONSTRAIN-GOVERN |

## Anti-Patterns

- Pular BECOME (gera output sem identidade, inconsistente)
- INJECT antes de BECOME (contexto sem papel = ruido)
- PRODUCE sem REASON (output sem planejamento = lixo)
- GOVERN ausente (sem quality gate = degradacao silenciosa)
- COLLABORATE sem GOVERN (propaga erros para proximo no pipeline)

## Code

<!-- lang: python | purpose: 8-function pipeline execution -->
```python
pipeline = [
    ("BECOME",      load_prime, load_mental_model),
    ("INJECT",      index_pool, load_routing_table),
    ("REASON",      read_task, decompose_subtasks),
    ("CALL",        brain_query, connect_mcps),
    ("PRODUCE",     run_agent_teams, generate_artifacts),
    ("CONSTRAIN",   validate_schema, apply_templates),
    ("GOVERN",      quality_gate, run_tests),
    ("COLLABORATE", write_signal, git_commit),
]
for name, *steps in pipeline:
    for step in steps:
        step()  # each function executes in order
# Prompt: executes BECOME(implicit) + PRODUCE only
# Agent: adds INJECT + REASON + CALL
# Agent_group: all 8 functions, full lifecycle
```

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_function_become
- related: p01_kc_cex_agent_group_concept
- related: p01_kc_cex_cortex_enterprise

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.62 |
| [[p01_kc_cex_function_become]] | sibling | 0.31 |
| [[p01_kc_cex_function_produce]] | sibling | 0.30 |
| [[spec_seed_words]] | related | 0.28 |
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.25 |
| [[p01_kc_cex_agent_group_concept]] | sibling | 0.25 |
| [[p01_kc_cex_function_call]] | sibling | 0.25 |
| [[p01_kc_cex_taxonomy]] | sibling | 0.24 |
| [[p01_kc_cex_learning_package_concept]] | sibling | 0.24 |
| [[bld_architecture_dataset_card]] | downstream | 0.24 |
