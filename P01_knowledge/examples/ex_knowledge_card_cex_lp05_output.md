---
id: p01_kc_cex_lp05_output
kind: knowledge_card
pillar: P01
title: "CEX LP05 Output — Delivery Formats Between LLM and System"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp05, output, response-format, parser, formatter]
tldr: "P05 define COMO o LLM entrega resultados via 4 tipos: response_format, parser, formatter e naming_rule"
when_to_use: "Entender formatos de entrega LLM e a fronteira entre geracao (P05) e validacao (P06)"
keywords: [output, response-format, parser, formatter, naming-rule]
long_tails:
  - "Como definir o formato de resposta de um agente LLM"
  - "Qual a diferenca entre response_format e validation_schema"
axioms:
  - "SEMPRE separar formato de resposta (P05) de validacao (P06)"
  - "NUNCA confundir parser (extrai) com formatter (transforma)"
linked_artifacts:
  primary: p01_kc_cex_lp06_schema
  related: [p01_kc_cex_lp07_evals]
density_score: 1.0
data_source: "https://docs.anthropic.com/en/docs/build-with-claude/structured-output"
---

## Quick Reference

topic: P05 Output | scope: delivery formats | criticality: high
types: 4 | function: CONSTRAIN | layer: spec + runtime + governance

## Conceitos Chave

- P05 define COMO o agente entrega, nao O QUE entrega
- response_format eh injetado no prompt (LLM ve e segue)
- validation_schema P06 eh pos-geracao (LLM nao ve)
- parser extrai dados estruturados de output bruto
- formatter converte entre formatos (json, md, yaml)
- naming_rule governa nomenclatura de artefatos gerados
- LP mais enxuto do CEX: 4 tipos, todos < 4096 bytes
- Funcao dominante: CONSTRAIN (formatar pos-geracao)
- response_format usa machine_format json (spec layer)
- parser usa machine_format yaml (runtime layer)
- formatter opera na camada runtime (conversao ativa)
- naming_rule opera na camada governance (padronizacao)
- P05 depende de P06: schemas definem o que P05 formata
- P05 eh avaliado por P07: formatos incorretos detectados
- P05 eh moldado por P02: identidade define tom e estilo
- Sem response_format, LLM gera formato imprevisivel

## Fases

1. Definir response_format no prompt do agente
2. LLM gera output seguindo formato especificado
3. Parser extrai dados estruturados do output bruto
4. Formatter converte para formato de consumo downstream
5. Naming_rule garante nomenclatura consistente
6. P06 validation_schema valida o resultado final

## Regras de Ouro

- SEMPRE definir response_format antes de chamar o LLM
- NUNCA validar dentro de P05 (validacao eh P06)
- SEMPRE usar parser para output semi-estruturado
- NUNCA assumir que LLM segue formato sem instrucao
- SEMPRE separar extracao (parser) de conversao (fmt)

## Comparativo

| Aspecto | P05 Output | P06 Schema |
|---------|-----------|------------|
| Quando atua | Pre e pos-geracao | Pos-geracao |
| Visibilidade | LLM ve response_format | Sistema aplica, LLM nao ve |
| Funcao | Formatar entrega | Validar contrato |
| Modo de falha | Output malformado | Violacao de contrato |
| Qtd tipos | 4 (rf, parser, fmt, nr) | 7 (is, td, val, iface, vs, bp, gram) |

## Flow

```
[LLM] --response_format--> [raw output]
  |                            |
  v                            v
[P05: format hint]      [parser: extract]
                               |
                               v
                        [formatter: convert]
                               |
                               v
                        [P06: validate contract]
                               |
                               v
                        [downstream consumer]
```

## References

- source: https://docs.anthropic.com/en/docs/build-with-claude/structured-output
- source: https://platform.openai.com/docs/guides/structured-outputs
- related: p01_kc_cex_lp06_schema
- related: p01_kc_cex_lp07_evals


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating
