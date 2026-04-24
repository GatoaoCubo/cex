---
id: p01_kc_cex_learning_package_concept
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Learning Packages — 12 Dimensions That Define Any LLM Entity"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, learning-package, dimensions, lp, entity-model]
tldr: "12 LPs sao dimensoes (nao categorias) que definem qualquer entidade LLM -- de prompt (1 LP) a agent_group (12 LPs)"
when_to_use: "Entender as 12 dimensoes de uma entidade LLM e como LPs se cruzam com funcoes"
keywords: [learning-package, dimensions, entity, orthogonality, completeness]
long_tails:
  - "Qual a diferenca entre Learning Package e categoria de artefato"
  - "Como os 12 LPs se relacionam com as 8 funcoes LLM"
axioms:
  - "SEMPRE tratar LPs como dimensoes ortogonais, nao pastas"
  - "NUNCA confundir LP (o que entidade TEM) com funcao (o que LLM FAZ)"
linked_artifacts:
  primary: p01_kc_cex_taxonomy
  related: [p01_kc_cex_llm_function_concept, p01_kc_cex_type_artifact]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_fractal_architecture
  - p01_kc_cex_maturity_level
  - p01_kc_cex_llm_function_concept
  - p01_kc_cex_pipeline_execution
  - p01_kc_cex_taxonomy
  - p01_kc_cex_agent_group_concept
  - p01_kc_cex_type_artifact
  - bld_architecture_memory_architecture
  - p01_kc_cex_function_become
  - p01_kc_lp02_model
---

## Summary

Learning Packages (LPs) sao as 12 dimensoes que definem qualquer entidade LLM. Nao sao categorias de artefatos -- sao PERGUNTAS. P01 pergunta "o que sabe?", P02 "quem e?", P03 "como fala?". Um prompt preenche 1 LP (P03). Um agente preenche 3-4. Um agent_group preenche todos os 12. A diferenca entre entidades eh dimensionalidade, nao natureza. LPs sao ortogonais as funcoes: LP = o que a entidade TEM, funcao = o que o LLM FAZ.

## Spec

| LP | Nome | Pergunta | Funcao Dominante |
|----|------|----------|-----------------|
| P01 | Knowledge | O que sabe? | INJECT |
| P02 | Model | Quem e? | BECOME |
| P03 | Prompt | Como fala? | REASON + CONSTRAIN |
| P04 | Tools | O que usa? | CALL |
| P05 | Output | O que entrega? | CONSTRAIN |
| P06 | Schema | Que contratos? | CONSTRAIN + GOVERN |
| P07 | Evals | Como medir? | GOVERN |
| P08 | Architecture | Como escala? | BECOME + GOVERN |
| P09 | Config | Como configura? | GOVERN |
| P10 | Memory | O que lembra? | INJECT |
| P11 | Feedback | Como melhora? | GOVERN |
| P12 | Orchestration | Como coordena? | COLLABORATE |

Ortogonalidade: cada tipo CEX tem 1 LP primario e 1 funcao primaria. LP classifica por dimensao da entidade. Funcao classifica por estagio do pipeline. As duas classificacoes sao independentes e complementares.

## Patterns

| Trigger | Action |
|---------|--------|
| Entidade sem memoria entre sessoes | Adicionar LP P10 (Memory) |
| Agente com output inconsistente | Verificar LP P05 (Output) e P06 (Schema) |
| Sistema sem quality gates | Implementar LP P07 (Evals) |
| Novo agente criado | Preencher P02 (Model) + P03 (Prompt) minimo |
| Agent_group completo necessario | Garantir todos 12 LPs preenchidos |

## Code

<!-- lang: python | purpose: LP dimensionality of an entity -->
```python
ENTITY_LPS = {
    "prompt":    {"P03": True},                    # 1 LP
    "agent":     {"P02": True, "P03": True,
                  "P04": True, "P10": True},       # 4 LPs
    "agent_group": {f"P{i:02d}": True
                  for i in range(1, 13)},          # 12 LPs
}
# completude = len(filled_lps) / 12
# prompt = 8%, agente = 33%, agent_group = 100%
```

## Anti-Patterns

- Tratar LPs como pastas de filesystem (sao dimensoes)
- Confundir LP com funcao (TEM vs FAZ)
- Criar entidade sem P02+P03 minimo (sem identidade)
- Preencher LPs em ordem numerica (ordem eh semantica)
- Ignorar ortogonalidade LP x funcao na classificacao

## References

- source: https://arxiv.org/abs/2308.00352
- related: p01_kc_cex_taxonomy
- related: p01_kc_cex_llm_function_concept
- related: p01_kc_cex_type_artifact

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_fractal_architecture]] | sibling | 0.40 |
| [[p01_kc_cex_maturity_level]] | sibling | 0.33 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.31 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.30 |
| [[p01_kc_cex_taxonomy]] | sibling | 0.29 |
| [[p01_kc_cex_agent_group_concept]] | sibling | 0.26 |
| [[p01_kc_cex_type_artifact]] | sibling | 0.26 |
| [[bld_architecture_memory_architecture]] | downstream | 0.24 |
| [[p01_kc_cex_function_become]] | sibling | 0.23 |
| [[p01_kc_lp02_model]] | sibling | 0.23 |
