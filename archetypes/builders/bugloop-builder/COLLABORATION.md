---
pillar: P12
llm_function: COLLABORATE
purpose: How bugloop-builder works in crews
---

# Collaboration: bugloop-builder

## My Role
I define WHAT the correction cycle does (detect pattern, fix strategy, verify suite, escalation policy).
I do NOT implement HOW detection runs (validator-builder, P06).
I do NOT implement HOW the fix executes (executor agent).
I do NOT define pass/fail quality barriers (quality-gate-builder, P11).

## Crew: "Add Automated Correction to New Type"
```
  1. quality-gate-builder  -> defines HARD/SOFT gates (what must pass)
  2. bugloop-builder       -> defines correction cycle (what runs when gate fails)
  3. validator-builder     -> implements detect.pattern check in code [PLANNED]
```
Note: quality-gate-builder refs bugloop-builder (gate triggers loop on fail).
      bugloop-builder refs quality-gate-builder (loop fires on gate failure).
      Bidirectional cross-ref enforced per BUILDER_NORMS LAW 12.

## Crew: "Full Feedback Loop for Pipeline"
```
  1. bugloop-builder       -> correction cycle policy
  2. lifecycle-rule-builder -> archive/promote rules post-correction [PLANNED]
  3. optimizer-builder     -> continuous improvement after stability restored [PLANNED]
```

## Crew: "Archetype Quality Automation"
```
  1. quality-gate-builder  -> QUALITY_GATES.md for each kind
  2. bugloop-builder       -> correction cycle when gate fails in CI
  3. golden-test-builder   -> verify.assertions reference [PLANNED]
```

## Handoff Protocol
### I Receive
- scope: what system/module/pipeline to monitor
- failure_class: what known failure signature to target
- fix_safety: how much blast radius is acceptable (determines confidence floor)
- escalation_owner: who owns the escalation (human, system, queue)

### I Produce
- bugloop artifact in P11_feedback/examples/p11_bl_{scope}.md

## Builders I Depend On
| Builder | Why |
|---------|-----|
| quality-gate-builder | Gate failures are the primary trigger for bugloops |
| validator-builder [PLANNED] | Implements detect.pattern; bugloop policy references it |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | References bugloop as the correction cycle on gate failure |
| lifecycle-rule-builder [PLANNED] | May trigger bugloop before archive/promote decisions |
| optimizer-builder [PLANNED] | Bugloop stabilizes; optimizer then improves |

## Cross-Reference Contract
Per BUILDER_NORMS LAW 12: quality-gate-builder COLLABORATION.md lists bugloop-builder
as a dependent builder. This file lists quality-gate-builder as a dependency.
Both refs are active and symmetric.
