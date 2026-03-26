---
lp: P08
llm_function: CONSTRAIN
purpose: Boundary and position of quality_gate in the CEX fractal
---

# Architecture: quality_gate in the CEX

## Boundary
quality_gate EH: barreira de qualidade com score numerico (pass/fail + weighted dimensions).
quality_gate NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| validator | validator IMPLEMENTA check em codigo. gate DEFINE criterio. | P06 validator |
| scoring_rubric | rubric define COMO avaliar. gate define SE passa. | P07 scoring_rubric |
| bugloop | bugloop eh ciclo detect-fix-verify. gate eh barreira unica. | P11 bugloop |
| guardrail | guardrail previne DANOS. gate garante QUALIDADE. | P11 guardrail |

## Dependency Graph
```
quality_gate <--implements-- validator (P06 codes the check)
quality_gate <--uses_criteria-- scoring_rubric (P07 defines dimensions)
quality_gate <--triggers-- bugloop (P11 cycles on failure)
quality_gate --independent-- lifecycle_rule, optimizer
```

## Fractal Position
LP: P11 (Feedback)
Function: GOVERN
Scale: L0 (governance artifact)
