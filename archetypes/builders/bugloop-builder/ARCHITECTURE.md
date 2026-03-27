---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of bugloop in the CEX fractal
---

# Architecture: bugloop in the CEX

## Boundary
bugloop EH: ciclo automatico de correcao (detect > fix > verify) para classes de falha CONHECIDAS.
bugloop NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| quality_gate | quality_gate BLOQUEIA com pass/fail score. bugloop CORRIGE pos-falha. | P11 quality_gate |
| lifecycle_rule | lifecycle_rule define freshness/archive/promote. bugloop reage a falhas, nao a idade. | P11 lifecycle_rule |
| guardrail | guardrail PREVINE acoes inseguras antes de executar. bugloop CORRIGE apos falha ocorrer. | P11 guardrail |
| optimizer | optimizer MELHORA metricas continuamente sem falha como trigger. bugloop reage a regressoes. | P11 optimizer |
| validator | validator IMPLEMENTA o check em codigo (P06). bugloop DEFINE o ciclo de correcao (P11). | P06 validator |
| unit_eval | unit_eval avalia manualmente qualidade (P07). bugloop nao testa manualmente. | P07 unit_eval |

## Dependency Graph
```
bugloop --uses_signal_from--> validator (P06 implements detect.pattern check)
bugloop --verifies_via--> test_suite (P07 golden_tests define assertions)
bugloop --triggers_on_fail--> quality_gate (P11 gate failure feeds bugloop)
bugloop --escalates_to--> signal_bus / human_operator
bugloop --may_rollback_via--> lifecycle_rule (P11 rollback strategy alignment)
bugloop --independent--> optimizer, guardrail
```

## Fractal Position
Pillar: P11 (Feedback)
Function: GOVERN
Scale: L0 (governance artifact — defines policy, not implementation)
Layer: governance

## Cycle Flow
```
[TRIGGER: detect.trigger fires]
        |
        v
[MATCH: detect.pattern? YES/NO]
        |
       YES
        |
        v
[FIX: fix.strategy, attempt 1..max_attempts]
        |
        +--[verify: run test_suite, check assertions, within timeout]
        |           |
        |         PASS --> [done, cycle ends]
        |         FAIL --> [increment cycle]
        |
        +--[cycle >= escalation.threshold] --> [ESCALATE to escalation.target]
        |
        +--[cycle >= cycle_count] --> [ESCALATE + optional ROLLBACK]
```

## Layer Contract
bugloop is a GOVERNANCE artifact:
- It defines WHAT the cycle does (policy)
- It does NOT implement the detection check (validator P06)
- It does NOT implement the fix code (executor agent)
- It does NOT define evaluation criteria (scoring_rubric P07)

## P11 Pillar Map
```
P11 (Feedback)
 ├── quality_gate    — pass/fail barrier (threshold + score)
 ├── bugloop         --> THIS — detect > fix > verify cycle
 ├── lifecycle_rule  — freshness, archive, promote rules
 ├── guardrail       — safety boundary (prevent unsafe actions)
 └── optimizer       — continuous metric improvement
```
