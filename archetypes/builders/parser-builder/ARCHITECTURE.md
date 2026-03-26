---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of parser in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: parser in the CEX

## Boundary
parser EH: extrator de dados estruturados runtime — extraction rules que convertem output bruto
(texto, JSON, HTML) em dados tipados e normalizados. O parser EXTRAI campos especificos de
input nao-estruturado ou semi-estruturado usando patterns concretos (regex, json_path, selectors).

parser NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| formatter | formatter APRESENTA dados em formato legivel; parser EXTRAI dados de input bruto | P05 formatter |
| validator | validator VALIDA conteudo contra regras; parser EXTRAI sem julgar | P06 validator |
| naming_rule | naming_rule define CONVENCOES de nomes; parser extrai DADOS de texto | P05 naming_rule |
| output_schema | output_schema define FORMATO de saida; parser IMPLEMENTA extracao | P05/P06 output_schema |
| scraper | scraper COLETA dados da web; parser PROCESSA dados ja coletados | P04 scraper |
| connector | connector CONECTA a servico externo; parser TRANSFORMA dados localmente | P04 connector |

Regra: "como extrair dados estruturados deste output bruto?" -> parser.

## Position in Output Flow

```text
LLM response --> parser (P05) --> structured data --> formatter (P05) --> display
                    |                    |
               [extraction]         [validation]
                                         |
                                    validator (P06)
```

parser is the EXTRACTION LAYER — sits between raw LLM output and structured consumption,
converting unstructured text into typed, normalized data fields.

## Dependency Graph

```text
parser <--receives-- agent (P02) (raw output to parse)
parser <--receives-- scraper (P04) (scraped content to extract from)
parser <--receives-- output_schema (P05/P06) (target schema for extraction)
parser --produces_for--> formatter (P05) (structured data for presentation)
parser --produces_for--> validator (P06) (extracted data for validation)
parser --produces_for--> knowledge_card (P01) (extracted facts for distillation)
parser --independent-- router, fallback_chain, workflow, signal
```

## Fractal Position
Pillar: P05 (Output — WHAT comes out)
Function: EXTRACT (pull structured data from raw output)
Layer: runtime (executes per-output, stateless transform)
Scale: L0 (infrastructure — every system that processes LLM output needs parsing)
