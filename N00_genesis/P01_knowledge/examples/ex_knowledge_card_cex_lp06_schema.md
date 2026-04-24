---
id: p01_kc_cex_lp06_schema
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP06 Schema — Data Contracts That Constrain LLM Output"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp06, schema, contracts, validation, grammar, blueprint]
tldr: "P06 define 7 tipos de contrato que restringem output: de input_schema a grammar (constraint no decoder)"
when_to_use: "Entender contratos de dados em sistemas LLM e como soft CONSTRAIN vira hard CONSTRAIN"
keywords: [schema, contracts, validation, grammar, blueprint, type-def]
long_tails:
  - "Como definir contratos de dados entre agentes LLM"
  - "Qual a diferenca entre grammar e validator no CEX"
axioms:
  - "SEMPRE ter input_schema antes de aceitar dados"
  - "NUNCA confundir grammar (durante geracao) com validator (pos)"
linked_artifacts:
  primary: p01_kc_cex_lp05_output
  related: [p01_kc_cex_lp07_evals]
density_score: 1.0
data_source: "https://json-schema.org/understanding-json-schema"
related:
  - p01_kc_cex_lp05_output
  - p01_kc_cex_function_constrain
  - p06_gram_json_object
  - p01_kc_validation_schema
  - p01_kc_lp06_schema
  - validation-schema-builder
  - p01_kc_input_schema
  - bld_architecture_validation_schema
  - bld_knowledge_card_constraint_spec
  - bld_architecture_type_def
---

## Quick Reference

topic: P06 Schema | scope: data contracts | criticality: high
types: 7 | function: CONSTRAIN + GOVERN | layer: spec + governance

## Conceitos Chave

- P06 eh onde soft CONSTRAIN vira hard CONSTRAIN
- input_schema define dados requeridos na entrada
- validation_schema valida output pos-geracao (sistema)
- type_def cria tipos customizados reutilizaveis
- interface eh contrato bilateral entre agentes
- artifact_blueprint eh meta-template (shape de artefato)
- grammar restringe tokens DURANTE geracao (no decoder)
- Unifica conceitos de BNF, EBNF, FSM e WHERE clauses
- Nenhum framework popular tem esses 7 tipos juntos
- Guidance usa BNF/EBNF para controle caractere a caractere
- Outlines usa FSMs e CFGs para constraint formal
- LMQL usa WHERE clauses declarativas pos-geracao
- P06 eh consumido por P05: schemas definem o que formatar
- P06 eh validado por P07: conformidade com schema testada
- P06 eh informado por P01: schemas refletem o dominio
- input_schema max 3072 bytes (spec layer, core: true)
- grammar max 3072 bytes (spec layer, core: false)

## Fases

1. Definir input_schema com campos requeridos
2. Criar type_defs para tipos customizados do dominio
3. Estabelecer interfaces entre agentes cooperantes
4. Escrever artifact_blueprints para artefatos recorrentes
5. Configurar validation_schema para pos-geracao
6. Aplicar grammar quando precisao > 99% eh critica

## Regras de Ouro

- SEMPRE validar input antes de processar (input_schema)
- NUNCA confundir response_format P05 com validation_schema
- SEMPRE usar grammar para output deterministico critico
- NUNCA auto-atribuir quality em artifact_blueprint
- SEMPRE documentar boundary de cada tipo (evita overlap)

## Comparativo

| Mecanismo | Quando Atua | Quem Aplica | Precisao |
|-----------|-------------|-------------|----------|
| response_format P05 | Pre-geracao | LLM interpreta | ~85% |
| validation_schema | Pos-geracao | Sistema valida | ~99% |
| grammar | Durante geracao | Decoder constrains | ~100% |
| validator | Pos-geracao | Pipeline pass/fail | ~99% |

## Flow

```
[input] --input_schema--> [validated input]
                              |
                              v
              [LLM + grammar] --> [constrained output]
                              |
                              v
              [validation_schema] --> pass/fail
                              |
                              v
              [interface] --> [next agent receives]
                              |
                              v
              [type_def checks] --> [type-safe system]
```

## References

- source: https://json-schema.org/understanding-json-schema
- source: https://github.com/guidance-ai/guidance
- related: p01_kc_cex_lp05_output
- related: p01_kc_cex_lp07_evals


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp05_output]] | sibling | 0.42 |
| [[p01_kc_cex_function_constrain]] | sibling | 0.40 |
| [[p06_gram_json_object]] | downstream | 0.31 |
| [[p01_kc_validation_schema]] | sibling | 0.30 |
| [[p01_kc_lp06_schema]] | sibling | 0.29 |
| [[validation-schema-builder]] | downstream | 0.28 |
| [[p01_kc_input_schema]] | sibling | 0.27 |
| [[bld_architecture_validation_schema]] | downstream | 0.25 |
| [[bld_knowledge_card_constraint_spec]] | sibling | 0.25 |
| [[bld_architecture_type_def]] | downstream | 0.25 |
