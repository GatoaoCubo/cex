---
id: p01_kc_cex_type_artifact
kind: knowledge_card
pillar: P01
title: "CEX Type Artifacts — 78 Named Units with Contract, Boundary and Schema"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, type, artifact, contract, boundary, schema, naming]
tldr: "78 tipos CEX sao contratos atomicos: cada um tem funcao, LP, camada, tamanho maximo e naming padronizado"
when_to_use: "Consultar o vocabulario completo de tipos CEX e seus contratos"
keywords: [type-artifact, contract, boundary, schema, naming-convention]
long_tails:
  - "Quantos tipos de artefato o CEX define e como sao organizados"
  - "Como funciona o contrato de um tipo CEX"
axioms:
  - "SEMPRE verificar se tipo CEX existe antes de criar nomenclatura"
  - "NUNCA criar artefato sem boundary e schema explicitados"
linked_artifacts:
  primary: p01_kc_cex_taxonomy
  related: [p01_kc_cex_llm_function_concept, p01_kc_cex_learning_package_concept]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_taxonomy
  - p01_kc_cex_boundary_concept
  - p01_kc_lp06_schema
  - p01_kc_lp05_output
  - p01_kc_cex_learning_package_concept
  - p01_kc_cex_lp01_knowledge
  - p01_kc_cex_function_become
  - p01_kc_cex_function_inject
  - p01_kc_cex_function_govern
  - p01_kc_cex_lp05_output
---

## Summary

Tipos CEX sao as 78 unidades atomicas do vocabulario -- o menor elemento com semantica propria e identidade independente. Cada tipo eh um contrato: define funcao LLM primaria, LP primario, camada (content/spec/prompt/runtime/governance), tamanho maximo e naming convention prefixada pelo LP. Quando algo eh tipado como knowledge_card, sabe-se: fato atomico, funcao INJECT, LP P01, max 5KB, density >= 0.8.

## Spec

| LP | Tipos Exemplo | Qtd | Camada |
|----|---------------|-----|--------|
| P01 Knowledge | knowledge_card, embedding, glossary | 7 | content |
| P02 Model | agent, persona, mental_model, model_card | 6 | spec |
| P03 Prompt | system_prompt, instruction, hop | 8 | prompt |
| P04 Tools | tool, skill, mcp_server | 5 | runtime |
| P05 Output | report, code, copy, artifact | 7 | content |
| P06 Schema | schema, blueprint, template | 6 | spec |
| P07 Evals | quality_gate, benchmark, test | 7 | governance |
| P08 Architecture | pattern, law, component_map | 6 | spec |
| P09 Config | config, boot_config, env | 5 | runtime |
| P10 Memory | memory, session_log, context | 6 | runtime |
| P11 Feedback | feedback, review, signal | 5 | governance |
| P12 Orchestration | workflow, handoff, dispatch | 10 | runtime |

Contrato por tipo: (1) funcao LLM primaria, (2) LP primario, (3) camada, (4) tamanho maximo, (5) naming `{lp_code}_{type}_{slug}.md`.

Cinco camadas: content (dados), spec (definicoes), prompt (instrucoes), runtime (execucao), governance (controle).

## Patterns

| Trigger | Action |
|---------|--------|
| Novo artefato criado | Verificar tipo CEX e usar naming convention |
| Artefato sem boundary claro | Definir camada + tamanho maximo |
| Tipo nao encontrado nos 78 | Verificar se eh variante de tipo existente |
| Migracao de framework | Mapear tipos proprietarios para tipos CEX |
| Validacao de artefato | Checar contrato: funcao + LP + camada |

## Code

<!-- lang: python | purpose: type contract definition -->
```python
TYPE_CONTRACT = {
    "knowledge_card": {
        "function": "INJECT",
        "lp": "P01",
        "layer": "content",
        "max_bytes": 5120,
        "naming": "p01_kc_{slug}.md",
        "density_min": 0.8,
    },
}
# 78 tipos, cada um com este contrato
# naming = {lp_code}_{type_abbrev}_{slug}.md
```

## Anti-Patterns

- Criar artefato sem tipo CEX definido (artefato orfao)
- Inventar tipo novo sem verificar os 78 existentes
- Ignorar naming convention (quebra indexacao e busca)
- Tipo sem tamanho maximo (artefatos infinitos = ruido)
- Confundir camada com LP (camada = natureza, LP = dimensao)

## References

- source: https://arxiv.org/abs/2308.00352
- related: p01_kc_cex_taxonomy
- related: p01_kc_cex_llm_function_concept
- related: p01_kc_cex_learning_package_concept

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_taxonomy]] | sibling | 0.34 |
| [[p01_kc_cex_boundary_concept]] | sibling | 0.32 |
| [[p01_kc_lp06_schema]] | sibling | 0.24 |
| [[p01_kc_lp05_output]] | sibling | 0.22 |
| [[p01_kc_cex_learning_package_concept]] | sibling | 0.22 |
| [[p01_kc_cex_lp01_knowledge]] | sibling | 0.22 |
| [[p01_kc_cex_function_become]] | sibling | 0.21 |
| [[p01_kc_cex_function_inject]] | sibling | 0.21 |
| [[p01_kc_cex_function_govern]] | sibling | 0.19 |
| [[p01_kc_cex_lp05_output]] | sibling | 0.19 |
