---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of input_schema in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: input_schema in the CEX

## Boundary
input_schema EH: contrato unilateral de entrada que define dados requeridos por um agente/operacao.

input_schema NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| interface (P06) | interface define CONTRATO bilateral. input_schema define ENTRADA unilateral. | P06 interface |
| type_def (P06) | type_def define TIPO abstrato reutilizavel. input_schema define CONTRATO concreto. | P06 type_def |
| validator (P06) | validator CHECA regras pass/fail. input_schema DEFINE shape esperado. | P06 validator |
| validation_schema (P06) | validation_schema eh aplicado silenciosamente pos-geracao. input_schema eh declarativo. | P06 validation_schema |
| output_schema (P05/P06) | output_schema define SAIDA. input_schema define ENTRADA. | P05/P06 output_schema |

Regra: "que dados este agente precisa receber?" -> input_schema.

## Position in Contract Flow

```text
caller prepares data -> [input_schema] validates shape -> agent processes -> output_schema validates result
                              |
                        fields: name/type/required/default
```

input_schema is a DESIGN-TIME artifact. It defines what data MUST be provided.

## Dependency Graph

```text
input_schema <--validates-- validator (P06, checks compliance)
input_schema <--used_by-- interface (P06, method input types)
input_schema <--referenced_by-- system_prompt (P03, documents required inputs)
input_schema --independent-- signal, dispatch_rule, quality_gate
```

## Fractal Position
Pillar: P06 (Schema — CONTRACTS and validation)
Function: CONSTRAIN (define input requirements)
Scale: L0 (spec layer — input_schemas define data contracts before runtime)
Input_schemas are the unilateral contract kind in P06 — complementing bilateral interfaces.

## Dependency Graph

```text
input_schema <--receives-- interface (P06) — method signatures to formalize
input_schema --produces_for--> validator (P06) — validates against input schema
input_schema --produces_for--> action_prompt (P03) — input format reference
input_schema --independent-- output_template, glossary_entry, knowledge_card
```

input_schema is CONTRACT LAYER — defines what goes IN
