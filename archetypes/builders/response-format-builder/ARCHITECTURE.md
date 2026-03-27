---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of response_format in the CEX fractal
---

# Architecture: response_format in the CEX

## Boundary
response_format EH: formato de resposta injetado no prompt do LLM para guiar como ele estrutura seu output.

response_format NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| validation_schema | validation_schema eh aplicado pelo SISTEMA pos-geracao. response_format eh visto pelo LLM. | P06 validation_schema |
| parser | parser EXTRAI dados de output existente. response_format GUIA a geracao. | P05 parser |
| formatter | formatter TRANSFORMA formato de output. response_format DEFINE formato original. | P05 formatter |
| grammar | grammar restringe TOKENS no decoder. response_format instrui em linguagem natural. | P06 grammar |
| prompt_template | prompt_template eh template completo. response_format eh apenas a parte de formato. | P03 prompt_template |

Regra: "como o LLM deve formatar sua resposta?" -> response_format.

## Position in Generation Pipeline

```text
system_prompt + response_format injection -> LLM generation (follows format) -> raw output -> validation_schema check
```

response_format is PRE-GENERATION LAYER — injected before the LLM generates, guiding output structure.

## Dependency Graph

```text
response_format --injected_in--> system_prompt (P03 includes format instructions)
response_format --consumed_by--> parser (P05 extracts data from formatted output)
response_format --validated_by--> validation_schema (P06 checks output matches format)
response_format <--derives_from-- artifact_blueprint (P06 defines artifact shape)
response_format --independent-- signal, handoff, benchmark, scoring_rubric
```

## Fractal Position
Pillar: P05 (Output — what the entity delivers)
Function: CONSTRAIN
Scale: L0 (spec artifact)
response_format is unique in P05 because it is the LLM-VISIBLE CONTRACT — the only output spec that the LLM reads during generation.
