---
id: p01_kc_lp06_schema
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "P06 Schema: Contratos de Validacao"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [schema, validation, contract, interface, type_def]
tldr: "P06 define 5 tipos de contrato (input_schema, type_def, validator, interface, output_schema) que governam validacao de entrada, saida e integracao entre agentes — max 3072 bytes"
when_to_use: "Quando precisar definir contratos de validacao, interfaces entre agentes ou tipos customizados"
keywords: [input_schema, validator, interface, type_def, output_schema]
long_tails:
  - "como definir um contrato de validacao entre agentes CEX"
  - "qual a diferenca entre P05 output_schema e P06 output_schema"
axioms:
  - "Contrato definido em P06 eh inviolavel — se a validacao falha, o artefato eh rejeitado"
linked_artifacts:
  agent: null
  skill: null
density_score: 0.85
related:
  - p01_kc_lp05_output
  - input-schema-builder
  - interface-builder
  - p01_kc_cex_lp06_schema
  - bld_architecture_type_def
  - p01_kc_cex_type_artifact
  - validator-builder
  - bld_architecture_validator
  - p01_kc_interface
  - naming-rule-builder
---

# P06 Schema: Contratos de Validacao

## Executive Summary
P06 eh a camada de contratos do CEX — o meta-schema que valida todos os outros LPs. Define 5 tipos de artefato focados em validacao: input_schema (entrada), output_schema (saida), type_def (tipos custom), validator (regras de gate) e interface (contratos inter-agente). Todos em YAML, max 3072 bytes.

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 5 | input_schema, type_def, validator, interface, output_schema |
| Max bytes (todos) | 3072 | Contratos devem ser concisos |
| input_schema naming | p06_is_{{scope}}.yaml | Contrato de entrada |
| type_def naming | p06_td_{{type}}.yaml | Tipo customizado |
| validator naming | p06_val_{{rule}}.yaml | Quality gate rule |
| interface naming | p06_iface_{{contract}}.yaml | Contrato inter-agente |
| output_schema naming | p06_os_{{scope}}.yaml | Duplica P05 por design |

## Patterns
- Input schema valida antes do agente executar — fail fast
- Interface contracts definem o "handshake" entre agentes upstream/downstream
- Validator rules alimentam quality gates (P11) com criterios pass/fail
- Type defs permitem tipos customizados reutilizaveis entre LPs
- Output schema em P06 duplica P05 intencionalmente: P05=formato, P06=contrato

## Anti-Patterns
- Agente sem input_schema: aceita qualquer lixo como entrada
- Interface sem ambos os lados definidos: contrato unilateral
- Validator sem score threshold: gate nao tem criterio de pass/fail
- Type def circular: tipo A referencia B que referencia A

## Application
Cada _schema.yaml dos 12 LPs eh ele mesmo um artefato P06 (meta-schema). O forge usa P06 para extrair regras de validacao e injeta-las nos prompts gerados, fechando o loop schema > prompt > artefato > validacao.

## References
- P06_schema/_schema.yaml (fonte de verdade — meta-meta-schema)
- Cada LP/_schema.yaml (instancias de P06 em acao)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_lp05_output]] | sibling | 0.41 |
| [[input-schema-builder]] | downstream | 0.29 |
| [[interface-builder]] | downstream | 0.28 |
| [[p01_kc_cex_lp06_schema]] | sibling | 0.26 |
| [[bld_architecture_type_def]] | downstream | 0.24 |
| [[p01_kc_cex_type_artifact]] | sibling | 0.24 |
| [[validator-builder]] | downstream | 0.23 |
| [[bld_architecture_validator]] | downstream | 0.23 |
| [[p01_kc_interface]] | sibling | 0.22 |
| [[naming-rule-builder]] | downstream | 0.22 |
