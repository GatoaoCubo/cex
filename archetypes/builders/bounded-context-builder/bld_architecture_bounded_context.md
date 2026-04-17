---
id: bld_architecture_bounded_context
kind: component_map
pillar: P08
llm_function: CONSTRAIN
version: 1.0.0
quality: null
tags: [bounded_context, architecture, ddd, context-map]
title: "Architecture Bounded Context"
---
# Architecture: bounded_context
## Position in CEX Kind Taxonomy
```
P08 Architecture
  bounded_context   <-- THIS KIND (semantic boundary)
  component_map     (deployment topology -- NOT bounded_context)
  decision_record   (ADR -- architecture decisions)
  interface         (integration contract spec)
  agent_card        (agent capability definition)
```

## Context Map Relationships
```
BC_A (upstream, Open Host Service)
    |
    | data_contract (Published Language)
    v
BC_B (downstream, Anti-Corruption Layer)
    |
    | domain_event (internal, not shared)
    v
BC_B aggregates (internal domain model)
```

## Relationships
| Relation | Kind | Direction | Notes |
|----------|------|-----------|-------|
| governed by | domain_vocabulary | one-to-one | Each BC has one vocabulary |
| emits | domain_event | one-to-many | Events stay within BC unless published |
| publishes | data_contract | one-to-many | Published Language to other BCs |
| maps to | component_map | loose | BC may span multiple services |
| owns | agent / nucleus | one-to-many | Nuclei belong to a BC |

## CEX Bounded Contexts
| BC | Nucleus | Domain |
|----|---------|--------|
| bc_intelligence | N01 | Research and analysis |
| bc_marketing | N02 | Content and campaigns |
| bc_engineering | N03 | Build and scaffold |
| bc_knowledge | N04 | Knowledge management |
| bc_operations | N05 | Code, test, deploy |
| bc_commercial | N06 | Pricing and revenue |
| bc_orchestration | N07 | Mission orchestration |

## Context Map Patterns (Evans)
- ACL prevents corruption from upstream model vocabulary
- OHS standardizes how this context exposes itself to consumers
- Partnership requires coordinated changes between two teams
- Big Ball of Mud: avoid -- no explicit boundary = semantic drift
