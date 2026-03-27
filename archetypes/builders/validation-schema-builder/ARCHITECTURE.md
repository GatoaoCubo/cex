---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of validation_schema in the CEX fractal
---

# Architecture: validation_schema in the CEX

## Boundary
validation_schema EH: contrato formal de validacao pos-geracao aplicado pelo SISTEMA (nao pelo LLM).

validation_schema NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| response_format | response_format eh INJETADO no prompt. validation_schema eh APLICADO pos-geracao. | P05 response_format |
| validator | validator eh regra INDIVIDUAL pass/fail. validation_schema eh contrato ESTRUTURAL completo. | P06 validator |
| input_schema | input_schema valida ENTRADA. validation_schema valida SAIDA. | P06 input_schema |
| grammar | grammar restringe TOKENS no decoder. validation_schema valida o OUTPUT ja gerado. | P06 grammar |
| quality_gate | quality_gate usa SCORING numerico. validation_schema usa tipo/constraint check. | P11 quality_gate |

Regra: "o que o sistema deve checar DEPOIS que o LLM gerou output?" -> validation_schema.

## Position in Generation Pipeline

```text
prompt (with response_format) -> LLM generation -> validation_schema check -> pass/fail -> publish or retry
```

validation_schema is POST-GENERATION LAYER — the system applies it after the LLM produces output, before accepting the result.

## Dependency Graph

```text
validation_schema --validates--> response_format (P05 output is checked against P06 schema)
validation_schema --enforces_for--> quality_gate (P11 uses schema pass as prerequisite)
validation_schema <--fields_from-- input_schema (P06 provides field definitions)
validation_schema --independent-- signal, handoff, knowledge_card, benchmark
```

## Fractal Position
Pillar: P06 (Schema — contracts of validation)
Function: GOVERN
Scale: L0 (spec artifact)
validation_schema is unique in P06 because it is the INVISIBLE CONTRACT — the LLM never sees it, but the system enforces it.
