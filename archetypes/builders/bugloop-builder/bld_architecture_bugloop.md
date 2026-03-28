---
kind: architecture
id: bld_architecture_bugloop
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of bugloop — inventory, dependencies, and architectural position
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| detect | Trigger evaluation — pattern matching against failure signals | bugloop | required |
| fix | Correction strategy — applies remediation up to max_attempts | bugloop | required |
| verify | Assertion suite — confirms fix success within timeout | bugloop | required |
| escalation | Threshold + target for unresolved failures | bugloop | required |
| rollback_policy | Revert strategy when all fix attempts fail | bugloop | optional |
| cycle_counter | Tracks current attempt number against max | bugloop | runtime |
| test_suite | External golden tests consumed by verify phase | P07 | external |
| quality_gate | External pass/fail barrier that feeds detect trigger | P11 | external |
| validator | Implements the concrete detection check logic | P06 | external |

## Dependency Graph

```
quality_gate    --signals-->  detect
validator       --signals-->  detect
detect          --produces--> fix
fix             --produces--> verify
verify          --produces--> cycle_counter
cycle_counter   --signals-->  escalation
fix             --depends-->  test_suite
verify          --depends-->  test_suite
escalation      --produces--> rollback_policy
```

| From | To | Type | Data |
|------|----|------|------|
| quality_gate | detect | signals | failure event with error class |
| validator | detect | signals | pattern match result (bool) |
| detect | fix | produces | matched failure class + context |
| fix | verify | produces | remediation result + attempt number |
| verify | cycle_counter | produces | pass/fail assertion result |
| cycle_counter | escalation | signals | attempt_count >= threshold |
| fix | test_suite | depends | test run request |
| verify | test_suite | depends | assertion evaluation |
| escalation | rollback_policy | produces | escalation target + revert trigger |

## Boundary Table

| bugloop IS | bugloop IS NOT |
|------------|----------------|
| Automated detect-fix-verify correction cycle | A pass/fail quality barrier (that is quality_gate) |
| Triggered by known failure classes | Triggered by metric drift (that is optimizer) |
| Bounded by max_attempts and timeout | A safety pre-check before execution (that is guardrail) |
| Defines escalation path when retries exhaust | A freshness or archive policy (that is lifecycle_rule) |
| Produces rollback on terminal failure | The implementation of the detection check (that is validator) |
| Reactive — responds to failure events | Proactive — continuously improving without failure trigger |

## Layer Map

| Layer | Components | Purpose |
|-------|-----------|---------|
| trigger | detect, quality_gate (external), validator (external) | Identify that a known failure class has occurred |
| correction | fix, cycle_counter | Apply remediation strategy up to max_attempts |
| verification | verify, test_suite (external) | Confirm fix resolved the failure within timeout |
| governance | escalation, rollback_policy | Handle exhausted retries — escalate and/or revert |
