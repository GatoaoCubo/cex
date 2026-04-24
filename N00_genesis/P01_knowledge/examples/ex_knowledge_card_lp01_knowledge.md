---
id: p01_kc_lp01_knowledge
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "P01 Knowledge: O Que o Agente Sabe"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [knowledge, KC, RAG, facts, density]
tldr: "P01 define 6 tipos de artefato de conhecimento (KC, RAG source, glossary, context doc, embedding config, few-shot) com density_min 0.8 e quality_min 7.0"
when_to_use: "Quando precisar criar, validar ou entender artefatos de conhecimento no CEX"
keywords: [knowledge_card, rag_source, glossary_entry, density, embedding]
long_tails:
  - "como criar um knowledge card valido no CEX"
  - "quais sao os tipos de artefato de P01 Knowledge"
axioms:
  - "Todo KC deve ter density >= 0.8 — sem filler, sem repeticao"
linked_artifacts:
  agent: null
  skill: p04_skill_cex_forge
density_score: 0.88
related:
  - bld_config_knowledge_card
  - p03_sp_forge_agent
  - bld_knowledge_card_knowledge_card
  - bld_instruction_knowledge_card
  - p06_bp_knowledge_card
  - bld_schema_knowledge_card
  - p01_kc_lp02_model
  - p03_sp_knowledge_card_builder
  - p01_kc_knowledge_best_practices
  - output_kc_quality_audit_20260408
---

# P01 Knowledge: O Que o Agente Sabe

## Executive Summary
P01 eh o dominio de conhecimento do CEX, responsavel por 6 tipos de artefato que capturam fatos atomicos pesquisaveis. KCs (knowledge cards) sao o tipo principal, com constraints de density_min 0.8, max_bytes 5120 e quality_min 7.0, validados via 2 variantes de body (domain_kc e meta_kc).

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 6 | KC, RAG source, glossary, context doc, embedding config, few-shot |
| KC max_bytes | 5120 | ~4KB de conteudo util |
| KC density_min | 0.8 | Cada frase deve conter info unica |
| KC quality_min | 7.0 | Pool >= 8.0, Golden >= 9.5 |
| KC min_bullets | 3 | Minimo de bullets por secao |
| Body variants | 2 | domain_kc (7 secoes) e meta_kc (6 secoes) |
| Frontmatter fields | 13 required + 5 CEX extended | 18 campos totais |

## Patterns
- domain_kc para KCs de negocio (quick_reference + conceitos + strategy + regras + visual + comparativo + artefatos)
- meta_kc para KCs tecnicos (summary + spec_table + patterns + anti_patterns + application + references)
- Frontmatter CEX extended (keywords, long_tails, axioms) melhora recall no Brain search em ~30%
- Naming padrao `p01_kc_{{topic}}.md` garante id == filename stem

## Anti-Patterns
- Densidade < 0.8: KC vira texto generico sem valor de busca
- Tags como string unica: schema exige lista de strings separadas
- Secoes com < 3 linhas: devem ser expandidas ou removidas
- Bullets > 80 chars: quebram layout e reduzem scanability

## Application
Todos os 12 LPs do CEX geram KCs em P01 para documentar seus proprios dominios. O forge (cex_forge.py) usa _schema.yaml de P01 para enforcar constraints automaticamente nos prompts gerados.

## References
- P01_knowledge/_schema.yaml (fonte de verdade)
- P01_knowledge/templates/tpl_knowledge_card_meta.md
- P01_knowledge/templates/tpl_knowledge_card_domain.md

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_knowledge_card]] | downstream | 0.27 |
| [[p03_sp_forge_agent]] | downstream | 0.26 |
| [[bld_knowledge_card_knowledge_card]] | sibling | 0.26 |
| [[bld_instruction_knowledge_card]] | downstream | 0.22 |
| [[p06_bp_knowledge_card]] | downstream | 0.22 |
| [[bld_schema_knowledge_card]] | downstream | 0.21 |
| [[p01_kc_lp02_model]] | sibling | 0.20 |
| [[p03_sp_knowledge_card_builder]] | downstream | 0.19 |
| [[p01_kc_knowledge_best_practices]] | sibling | 0.19 |
| [[output_kc_quality_audit_20260408]] | sibling | 0.19 |
