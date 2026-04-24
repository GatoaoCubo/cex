---
id: p01_kc_cex_lens_concept
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Lens — Cognitive Perspective That Refracts All Input"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lens, perspective, cognitive-filter, agent_group]
tldr: "Lens eh perspectiva cognitiva que filtra TODA percepcao e producao — mesmo input, outputs radicalmente diferentes por lens"
when_to_use: "Entender como agent_groups processam o mesmo input de formas distintas"
keywords: [lens, cognitive-perspective, refraction, prismatic-model]
long_tails:
  - "Como lenses diferenciam agent_groups que recebem o mesmo input"
  - "Qual a diferenca entre lens e role em sistemas multi-agente"
axioms:
  - "SEMPRE definir lens no mental_model antes de atribuir tarefas"
  - "NUNCA tratar lens como role simples (lens colore TODA percepcao)"
linked_artifacts:
  primary: p01_kc_cex_function_become
  related: [p01_kc_cex_fractal_architecture, p01_kc_cex_boundary_concept]
density_score: null
data_source: null
related:
  - bld_memory_lens
  - bld_architecture_lens
  - lens-builder
  - p03_sp_lens_builder
  - p11_qg_lens
  - bld_collaboration_lens
  - p03_ins_lens
  - bld_schema_lens
  - bld_tools_lens
  - p01_kc_lens
---

## Summary

Lens eh o conceito mais original do CEX. Diferente de "role" (papel funcional), lens eh perspectiva cognitiva que filtra TODA percepcao e producao de uma entidade. Implementada como artefato P02 no mental_model.yaml de cada agent_group. Modelo prismatico: mesmo input (luz branca) passa por 6 lenses e produz 6 refracoes. O LensEngine orquestra roteamento automatico, execucao por lens especifica e pipelines multi-lens.

## Spec

| Satelite | Lens | Input Exemplo | Output Refratado |
|----------|------|---------------|-----------------|
| research_agent | Analytical Envy | "mercado fones BT" | Tabela comparativa, 15 concorrentes, fontes |
| marketing_agent | Creative Lust | "mercado fones BT" | 5 gatilhos emocionais, copy de venda |
| knowledge_agent | Knowledge Gluttony | "mercado fones BT" | KC indexada por categoria, preco, canal |
| commercial_agent | Strategic Greed | "mercado fones BT" | Margem por faixa, canal mais lucrativo |
| builder_agent | Inventive Pride | "mercado fones BT" | Prototipo de scraper, componente React |
| operations_agent | Gating Wrath | "mercado fones BT" | Deploy pipeline, testes E2E, monitoramento |

Conceito industria mais proximo: "Role" (MetaGPT), "backstory" (CrewAI). Diferenca: role descreve funcao, lens colore TODA percepcao.

Implementacao: campo `lens` em `mental_model.yaml`. LensEngine orquestra 3 modos: roteamento automatico para lens mais adequada, execucao com intensidade configuravel, pipeline multi-lens sequencial.

Modelo prismatico: 6 lenses + setima consciencia (usuario/orchestrator). Combinacoes de lenses sao composicionais — 2 lenses em sequencia produzem resultado que nenhuma produziria sozinha.

## Patterns

| Trigger | Action |
|---------|--------|
| Mesmo input precisa de multiplas perspectivas | Rotear para 2+ agent_groups com lenses distintas |
| Output generico sem personalidade | Verificar se lens esta definida |
| Satelite produz output fora do esperado | Checar se lens esta alinhada com tarefa |
| Novo agent_group sendo criado | Definir lens ANTES de tools e knowledge |
| Pipeline precisa de refino progressivo | Encadear lenses em sequencia |

## Anti-Patterns

- Tratar lens como role descritivo (eh cognitiva, nao funcional)
- Dois agent_groups com lenses identicas (redundancia total)
- Omitir lens e depender so de instructions (output generico)
- Mudar lens mid-session (incoerencia de perspectiva)
- Ignorar modelo prismatico para tarefas multi-perspectiva

## References

- related: p01_kc_cex_function_become
- related: p01_kc_cex_fractal_architecture
- related: p01_kc_cex_boundary_concept

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_lens]] | downstream | 0.53 |
| [[bld_architecture_lens]] | downstream | 0.52 |
| [[lens-builder]] | downstream | 0.49 |
| [[p03_sp_lens_builder]] | downstream | 0.45 |
| [[p11_qg_lens]] | downstream | 0.44 |
| [[bld_collaboration_lens]] | downstream | 0.42 |
| [[p03_ins_lens]] | downstream | 0.42 |
| [[bld_schema_lens]] | downstream | 0.42 |
| [[bld_tools_lens]] | downstream | 0.41 |
| [[p01_kc_lens]] | sibling | 0.40 |
