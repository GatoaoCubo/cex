---
id: p01_kc_cex_taxonomy
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Taxonomy — Universal Classification for LLM Enterprise Artifacts"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, taxonomy, llm-artifacts, standardization, interoperability]
tldr: "CEX classifica 78 tipos de artefatos LLM em 8 funcoes e 12 LPs, cobrindo 91% de 12 frameworks -- o TCP/IP cognitivo"
when_to_use: "Entender a estrutura completa do CEX e por que padronizar artefatos LLM"
keywords: [cex, taxonomy, normalization, tcp-ip, artifact-types]
long_tails:
  - "O que eh o CEX e por que padronizar artefatos de IA empresarial"
  - "Quantos tipos de artefato existem em sistemas LLM"
axioms:
  - "SEMPRE usar o vocabulario CEX antes de inventar nomenclatura"
  - "NUNCA tratar funcoes como pastas -- sao estagios de pipeline"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_llm_function_concept, p01_kc_cex_learning_package_concept, p01_kc_cex_type_artifact]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_llm_function_concept
  - p01_kc_cex_type_artifact
  - p01_kc_cex_pipeline_execution
  - p01_kc_cex_function_govern
  - p01_kc_cex_boundary_concept
  - p01_kc_cex_learning_package_concept
  - p01_kc_cex_function_produce
  - p01_kc_cex_lp08_architecture
  - p01_kc_cex_function_inject
  - n04_competitive_knowledge
---

## Summary

CEXAI (Cognitive Exchange AI) eh uma taxonomia universal que classifica todos os artefatos de sistemas LLM empresariais. Auditoria de 12 frameworks (DSPy, LangChain, CrewAI, AutoGen, Haystack, etc.) revelou 86 tipos com zero padrao compartilhado. CEX reduz a 78 tipos normalizados em 8 funcoes e 12 Learning Packages, cobrindo 91% dos artefatos da industria (70% direto + 21% parcial).

## Spec

| Dimensao | Valor | Detalhe |
|----------|-------|---------|
| Tipos totais | 78 | Vocabulario completo de artefatos LLM |
| Funcoes | 8 | BECOME, INJECT, REASON, CALL, PRODUCE, CONSTRAIN, GOVERN, COLLABORATE |
| Learning Packages | 12 | P01 Knowledge a P12 Orchestration |
| Frameworks auditados | 12 | DSPy, LangChain, Semantic Kernel, AutoGen, CrewAI, Haystack, LlamaIndex, Guidance, Instructor, Outlines, LMQL, LangGraph |
| Frameworks CN extras | 10 | Qwen-Agent, ModelScope-Agent, XAgent, AgentScope, MetaGPT, CAMEL, ChatDev, AutoAgents, AgentVerse, ToolBench |
| Cobertura | 91% | 70% mapeamento direto + 21% parcial |
| Gaps (9%) | 4 areas | Multi-agent coord, constrained gen, pipeline, planning |
| Analogia | TCP/IP | Vocabulario compartilhado entre redes isoladas |
| Camadas | 5 | content, spec, prompt, runtime, governance |
| Tipos por funcao | 6-14 | PRODUCE tem mais tipos, COLLABORATE menos |

## Patterns

| Trigger | Action |
|---------|--------|
| Novo artefato LLM criado | Classificar por funcao + LP + tipo CEX |
| Migracao entre frameworks | Mapear tipos do framework para CEX |
| Auditoria de sistema LLM | Listar artefatos existentes por tipo CEX |
| Onboarding de engenheiro | Ensinar 8 funcoes antes de mostrar codigo |
| Interop entre sistemas | Trocar artefatos via contratos CEX |

## Code

<!-- lang: python | purpose: CEX type classification -->
```python
CEX_FUNCTIONS = [
    "BECOME", "INJECT", "REASON", "CALL",
    "PRODUCE", "CONSTRAIN", "GOVERN", "COLLABORATE",
]
CEX_LPS = {f"P{i:02d}": name for i, name in enumerate([
    "Knowledge", "Model", "Prompt", "Tools",
    "Output", "Schema", "Evals", "Architecture",
    "Config", "Memory", "Feedback", "Orchestration",
], 1)}
# 78 tipos = sum(tipos_por_lp.values())
# Cada tipo tem: funcao, lp, camada, max_size, naming
```

## Anti-Patterns

- Inventar nomenclatura propria sem consultar vocabulario CEX
- Tratar funcoes como pastas de arquivo em vez de pipeline
- Ignorar LPs e classificar artefatos apenas por funcao
- Mapear 1:1 com framework especifico (perde universalidade)
- Criar tipos novos sem boundary e schema explicitados

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_llm_function_concept
- related: p01_kc_cex_learning_package_concept
- related: p01_kc_cex_type_artifact

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.37 |
| [[p01_kc_cex_type_artifact]] | sibling | 0.36 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.30 |
| [[p01_kc_cex_function_govern]] | sibling | 0.28 |
| [[p01_kc_cex_boundary_concept]] | sibling | 0.27 |
| [[p01_kc_cex_learning_package_concept]] | sibling | 0.27 |
| [[p01_kc_cex_function_produce]] | sibling | 0.26 |
| [[p01_kc_cex_lp08_architecture]] | sibling | 0.24 |
| [[p01_kc_cex_function_inject]] | sibling | 0.24 |
| [[n04_competitive_knowledge]] | related | 0.23 |
