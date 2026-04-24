---
id: p01_kc_cex_llm_function_concept
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LLM Functions — 8 Pipeline Stages from BECOME to COLLABORATE"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, pipeline, execution-sequence, become-collaborate]
tldr: "8 funcoes LLM (BECOME a COLLABORATE) descrevem o pipeline real de execucao -- sequencia, nao categorias"
when_to_use: "Entender como LLMs processam artefatos e por que a sequencia importa"
keywords: [llm-function, pipeline, execution-stages, become, collaborate]
long_tails:
  - "Quais sao as 8 funcoes que um LLM executa em cada interacao"
  - "Qual a diferenca entre funcao LLM e categoria de artefato"
axioms:
  - "SEMPRE respeitar a sequencia BECOME antes de INJECT"
  - "NUNCA tratar funcoes como categorias estaticas de arquivo"
linked_artifacts:
  primary: p01_kc_cex_taxonomy
  related: [p01_kc_cex_function_become, p01_kc_cex_function_inject]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_pipeline_execution
  - p01_kc_cex_lp03_prompt
  - p01_kc_cex_function_become
  - p01_kc_cex_taxonomy
  - p01_kc_cex_function_produce
  - bld_architecture_dataset_card
  - bld_architecture_webinar_script
  - spec_seed_words
  - bld_architecture_experiment_tracker
  - p01_kc_cex_function_collaborate
---

## Summary

Funcao LLM eh o que o modelo FAZ com um artefato, nao o que o artefato EH. As 8 funcoes (BECOME, INJECT, REASON, CALL, PRODUCE, CONSTRAIN, GOVERN, COLLABORATE) formam o pipeline real de execucao de qualquer sistema LLM. Um prompt simples executa 1-2 funcoes. Um agente executa 4-5. Um agent_group com lifecycle completo executa todas as 8. A diferenca eh de completude, nao de natureza.

## Spec

| Funcao | Estagio | O Que Faz | Tipos Exemplo |
|--------|---------|-----------|---------------|
| BECOME | 1 | Configura identidade e papel | agent, persona, system_prompt |
| INJECT | 2 | Carrega contexto e conhecimento | knowledge_card, memory, embedding |
| REASON | 3 | Raciocina e decompoe | chain_of_thought, planner, react |
| CALL | 4 | Usa ferramentas externas | tool, mcp_server, api_call |
| PRODUCE | 5 | Gera artefatos de saida | code, copy, report |
| CONSTRAIN | 6 | Valida contra schemas | schema, template, output_format |
| GOVERN | 7 | Aplica quality gates | quality_gate, benchmark, lifecycle |
| COLLABORATE | 8 | Coordena com outros agentes | handoff, signal, shared_state |

Pipeline completo: INPUT -> BECOME -> INJECT -> REASON -> CALL -> PRODUCE -> CONSTRAIN -> GOVERN -> COLLABORATE -> OUTPUT.

Funcoes 1-2 configuram. Funcoes 3-5 executam. Funcoes 6-8 validam e comunicam. Descoberta empirica: hipotese inicial de 6 funcoes expandiu para 8 ao constatar que REASON e COLLABORATE tinham artefatos dedicados em todos os frameworks analisados.

## Patterns

| Trigger | Action |
|---------|--------|
| Agente sem identidade definida | BECOME com system_prompt + mental_model |
| Resposta sem contexto relevante | Verificar se INJECT carregou knowledge |
| Output com formato inconsistente | Adicionar CONSTRAIN com schema explicito |
| Sistema multi-agente sem coordenacao | Implementar COLLABORATE com signals |
| Raciocinio opaco em decisoes criticas | Ativar REASON com chain_of_thought |

## Code

<!-- lang: python | purpose: LLM function pipeline sequence -->
```python
PIPELINE = [
    "BECOME",      # 1. identidade
    "INJECT",      # 2. contexto
    "REASON",      # 3. raciocinio
    "CALL",        # 4. ferramentas
    "PRODUCE",     # 5. geracao
    "CONSTRAIN",   # 6. validacao
    "GOVERN",      # 7. quality gates
    "COLLABORATE", # 8. coordenacao
]
# prompt simples: BECOME(implicit) + PRODUCE
# agente: BECOME + INJECT + REASON + CALL + PRODUCE
# agent_group: todas as 8 funcoes
```

## Anti-Patterns

- Pular BECOME e enviar input direto (sem identidade)
- Confundir INJECT com BECOME (contexto vs identidade)
- Executar CALL antes de REASON (acao sem planejamento)
- PRODUCE sem CONSTRAIN (output sem contrato de formato)
- Tratar funcoes como categorias de pasta no filesystem

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_function_become
- related: p01_kc_cex_function_inject

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.68 |
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.34 |
| [[p01_kc_cex_function_become]] | sibling | 0.34 |
| [[p01_kc_cex_taxonomy]] | sibling | 0.33 |
| [[p01_kc_cex_function_produce]] | sibling | 0.31 |
| [[bld_architecture_dataset_card]] | downstream | 0.31 |
| [[bld_architecture_webinar_script]] | downstream | 0.29 |
| [[spec_seed_words]] | related | 0.28 |
| [[bld_architecture_experiment_tracker]] | downstream | 0.28 |
| [[p01_kc_cex_function_collaborate]] | sibling | 0.28 |
