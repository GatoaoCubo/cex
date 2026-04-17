---
id: bld_architecture_domain_event
kind: component_map
pillar: P08
llm_function: CONSTRAIN
version: 1.0.0
quality: 6.8
tags: [domain_event, architecture, ddd]
title: "Architecture Domain Event"
density_score: 1.0
updated: "2026-04-17"
---
# Architecture: domain_event
## Position in CEX Kind Taxonomy
```
P12 Orchestration
  domain_event      <-- THIS KIND (what happened)
  workflow          (what to do next)
  schedule          (when to do it)
  dispatch_rule     (who handles it)

P11 Feedback
  signal            (system telemetry -- NOT domain_event)
  audit_log         (compliance record -- NOT domain_event)
```

## Relationships
| Relation | Kind | Direction | Notes |
|----------|------|-----------|-------|
| owned by | bounded_context | many-to-one | Events belong to one BC |
| emitted by | agent / workflow | one-to-many | Aggregates emit events |
| triggers | workflow | one-to-many | Events may start workflows |
| published to | data_contract | via | Events cross BC boundary |
| stored as | audit_log | downstream | Compliance systems consume |

## When to Use domain_event (vs. alternatives)
| Scenario | Use |
|----------|-----|
| Business fact occurred (OrderPlaced) | domain_event |
| System health metric emitted | signal |
| Compliance-required activity record | audit_log |
| Cross-system integration payload | data_contract |
| Workflow step completion | workflow |

## Event Sourcing Pattern
domain_event is the source record in event sourcing:
aggregate state = fold(initial_state, [domain_events])
CEX does not enforce event store, but domain_event schema enables it.
