---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of validator in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: validator in the CEX

## Boundary
validator EH: regra de validacao tecnica pass/fail aplicada a artifacts antes de aceitacao.

validator NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| quality_gate (P11) | quality_gate PONTUA com weighted dimensions. validator PASSA ou FALHA. | P11 quality_gate |
| scoring_rubric (P07) | rubric define CRITERIOS subjetivos. validator checa REGRAS objetivas. | P07 scoring_rubric |
| input_schema (P06) | input_schema define SHAPE de entrada. validator checa REGRAS sobre dados. | P06 input_schema |
| validation_schema (P06) | validation_schema eh aplicado PELO SISTEMA silenciosamente. validator eh EXPLICITO. | P06 validation_schema |
| guardrail (P11) | guardrail limita COMPORTAMENTO. validator checa DADOS. | P11 guardrail |

Regra: "este campo/propriedade esta correto?" -> validator.

## Position in Governance Flow

```text
artifact produced -> [validator] -> pass? -> quality_gate (P11) -> publish/reject
                         |
                     fail? -> error_message -> author fixes -> retry
```

validator is the FIRST gate. It runs BEFORE quality_gate scoring.
If validator fails, quality_gate never runs.

## Dependency Graph

```text
validator <--checked_by-- quality_gate (quality_gate validates validators too)
validator <--used_by-- pre-commit hooks (automation layer)
validator <--referenced_by-- bugloop (P11, uses validators to detect regressions)
validator --validates--> all artifact kinds (knowledge_card, model_card, signal, etc.)
validator --independent-- scoring_rubric, input_schema, dispatch_rule
```

## Fractal Position
Pillar: P06 (Schema — CONTRACTS and validation)
Function: GOVERN (enforce correctness)
Scale: L0 (governance infrastructure — validators are checked before any artifact ships)
Validators are the only P06 kind in the governance layer — they bridge schema contracts to runtime enforcement.
