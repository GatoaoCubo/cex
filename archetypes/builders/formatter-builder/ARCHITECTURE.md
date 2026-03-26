---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of formatter in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: formatter in the CEX

## Boundary
formatter EH: transformador de apresentacao runtime — regras de formatacao que convertem dados
estruturados em representacoes legiveis ou consumiveis (JSON, Markdown, HTML, tabelas). O
formatter APRESENTA dados ja extraidos usando templates, serializacao, e regras de transformacao.

formatter NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| parser | parser EXTRAI dados de input bruto; formatter APRESENTA dados ja estruturados | P05 parser |
| response_format | response_format DEFINE o formato que o LLM produz; formatter TRANSFORMA dados pos-extracao | P05 response_format |
| naming_rule | naming_rule define CONVENCOES de nomes; formatter FORMATA dados para display | P05 naming_rule |
| output_schema (P06) | output_schema VALIDA formato de saida; formatter PRODUZ o formato | P06 output_schema |
| validator | validator VALIDA conteudo contra regras; formatter APRESENTA sem julgar | P06 validator |
| template (P03) | prompt_template INSTRUI o LLM; formatter TRANSFORMA output pos-LLM | P03 prompt_template |

Regra: "como apresentar estes dados estruturados neste formato?" -> formatter.

## Position in Output Flow

```text
LLM response --> parser (P05) --> structured data --> formatter (P05) --> display/consumer
                  [extraction]                         [presentation]
                                       |
                                  validator (P06)
                                   [validation]
```

formatter is the PRESENTATION LAYER — sits between structured data and final consumption,
converting typed data into the requested display or serialization format.

## Dependency Graph

```text
formatter <--receives-- parser (P05) (structured data to format)
formatter <--receives-- agent (P02) (typed output to present)
formatter <--receives-- knowledge_card (P01) (facts to render as table/list)
formatter --produces_for--> display/UI (final formatted output)
formatter --produces_for--> API response (serialized payload)
formatter --produces_for--> file export (formatted file content)
formatter --independent-- router, fallback_chain, workflow, signal, scraper
```

## Fractal Position
Pillar: P05 (Output — WHAT comes out)
Function: PRESENT (render structured data into target format)
Layer: runtime (executes per-output, stateless transform)
Scale: L0 (infrastructure — every system that displays data needs formatting)
