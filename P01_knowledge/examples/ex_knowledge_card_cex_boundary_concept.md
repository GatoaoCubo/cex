---
id: p01_kc_cex_boundary_concept
kind: knowledge_card
pillar: P01
title: "CEX Boundary — Explicit Exclusion That Prevents Type Confusion"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, boundary, type-safety, disambiguation, taxonomy]
tldr: "Boundary define o que um tipo NAO EH, reduzindo ambiguidade em 78 tipos e prevenindo classificacao errada por LLMs"
when_to_use: "Definir novos tipos CEX ou diagnosticar classificacao incorreta de artefatos"
keywords: [boundary, exclusion, type-safety, disambiguation]
long_tails:
  - "Como definir fronteiras entre tipos de artefato no CEX"
  - "Por que boundaries previnem confusao em taxonomias LLM"
axioms:
  - "SEMPRE definir boundary antes de specs para novos tipos"
  - "NUNCA assumir que titulo ou descricao bastam para desambiguar"
linked_artifacts:
  primary: p01_kc_cex_function_become
  related: [p01_kc_cex_fractal_architecture]
density_score: null
data_source: null
---

## Summary

Boundary define explicitamente o que um tipo CEX NAO EH. Em uma taxonomia de 78 tipos, titulo e descricao nao bastam para desambiguar — LLMs confundem knowledge_card com instrucao, template com configuracao. Boundary resolve declarando exclusoes: "KC NAO EH instrucao, NAO EH config, NAO EH template". Custo sem boundary: conhecimento perdido entre sessoes, agentes descartaveis e debito tecnico invisivel.

## Spec

| Tipo | Boundary (NAO EH) | Confusao Comum |
|------|-------------------|----------------|
| knowledge_card (P01) | instrucao, config, template, teste | LLM gera "faca X" dentro de KC |
| instruction (P03) | knowledge, config, schema | Mescla dados factuais com comandos |
| skill (P04) | knowledge, prompt, workflow | Confunde def/class com documentacao |
| agent (P02) | prompt, chain, runtime | Trata agente como prompt complexo |
| schema (P06) | template, config, knowledge | Confunde validacao com geracao |
| workflow (P12) | instruction, chain, script | Trata orquestracao como step unico |

Regra geral: se tem `def/class` executavel, eh skill (P04). Se tem `faca X` imperativo, eh instruction (P03). Se tem dados factuais destilados, eh knowledge_card (P01).

Custo do caos sem boundaries:
- Conhecimento perdido: cada sessao LLM esquece tudo
- Agentes descartaveis: 50 agentes = 50x custo de definicao
- Debito tecnico: dependencias invisiveis entre artefatos

## Patterns

| Trigger | Action |
|---------|--------|
| Novo tipo proposto no CEX | Definir boundary ANTES de specs |
| KC rejeitado por validador | Checar se conteudo viola boundary |
| LLM classifica artefato errado | Adicionar boundary explicito ao tipo |
| Dois tipos parecem sobrepostos | Boundary define a linha divisoria |
| Importando artefatos externos | Mapear para tipo CEX via boundaries |

## Anti-Patterns

- Definir tipo so por descricao positiva (sem dizer NAO EH)
- Boundaries vagos como "nao eh outro tipo" (sem especificar)
- Omitir boundary em tipos novos (confusao futura garantida)
- Boundary que contradiz specs do proprio tipo
- Confiar que LLM inferira boundaries sozinho

## References

- related: p01_kc_cex_fractal_architecture
- related: p01_kc_cex_function_become
