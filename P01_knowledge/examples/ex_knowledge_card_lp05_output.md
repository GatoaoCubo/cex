---
id: p01_kc_lp05_output
kind: knowledge_card
pillar: P01
title: "P05 Output: O Que o Agente Entrega"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [output, schema, parser, formatter, naming]
tldr: "P05 define 4 tipos de artefato de saida (output_schema, parser, formatter, naming_rule) que padronizam o que cada agente entrega — max 4096 bytes cada"
when_to_use: "Quando precisar definir ou validar formatos de saida de agentes CEX"
keywords: [output_schema, parser, formatter, naming_rule]
long_tails:
  - "como definir o formato de saida de um agente CEX"
  - "qual a diferenca entre output_schema e formatter em P05"
axioms:
  - "Todo agente deve ter output_schema definido — saida sem contrato eh saida imprevisivel"
linked_artifacts:
  agent: null
  skill: null
density_score: 0.84
---

# P05 Output: O Que o Agente Entrega

## Executive Summary
P05 padroniza as saidas do sistema CEX com 4 tipos de artefato. Output schemas definem estrutura (JSON/YAML), parsers extraem dados, formatters transformam entre formatos, e naming rules garantem consistencia de nomenclatura. Todos limitados a 4096 bytes.

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 4 | output_schema, parser, formatter, naming_rule |
| Max bytes (todos) | 4096 | Uniforme entre tipos |
| output_schema naming | p05_os_{{format}}.yaml | Contrato YAML |
| parser naming | p05_parser_{{target}}.md | Extrator com docs |
| formatter naming | p05_fmt_{{format}}.md | json, md, yaml |
| naming_rule naming | p05_nr_{{scope}}.md | Regra de nomenclatura |

## Patterns
1. Output schema em YAML define contrato exato: campos, tipos, required, examples
2. Parser extrai dados estruturados de saida raw (regex, JSON path, YAML parse)
3. Formatter transforma entre formatos (JSON > MD, YAML > table, etc)
4. Naming rules cascateiam: LP > tipo > topic — garante `id == filename stem`

## Anti-Patterns
1. Agente sem output_schema: saida varia entre execucoes
2. Parser sem target definido: nao sabe o que extrair
3. Naming rule ambigua: colisao de IDs entre artefatos
4. Formatter sem format de entrada: transformacao impossivel

## Application
No CEX, P05 trabalha em par com P06 (Schema) — P05 define "o que sai", P06 valida "o contrato". O agent_package de P02 mapeia output_template.md para P05, garantindo que todo agente tem saida definida.

## References
1. P05_output/_schema.yaml (fonte de verdade)
2. P02_model/_schema.yaml (agent_package.lp_mapping: output_template=P05)

## Retrieval

```yaml
query: "meta-construction"
kind_filter: knowledge_card
top_k: 5
threshold: 0.7
```

```bash
python _tools/cex_retriever.py "meta-construction" --top 5
```
