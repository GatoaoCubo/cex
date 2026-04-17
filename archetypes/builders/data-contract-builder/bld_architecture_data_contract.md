---
id: bld_architecture_data_contract
kind: component_map
pillar: P08
llm_function: CONSTRAIN
version: 1.0.0
quality: 6.8
tags: [data_contract, architecture, published-language]
title: "Architecture Data Contract"
density_score: 1.0
updated: "2026-04-17"
---
# Architecture: data_contract
## Position in CEX Kind Taxonomy
```
P06 Schema
  data_contract     <-- THIS KIND (cross-boundary agreement)
  validation_schema (LLM output validation -- different scope)
  input_schema      (single system input spec)
  type_def          (custom type definitions)
```

## Relationships
| Relation | Kind | Direction | Notes |
|----------|------|-----------|-------|
| formalizes | domain_event schema | one-to-one | Events crossing BCs need contracts |
| constrains | dataset_card | downstream | Contract precedes dataset catalog |
| referenced by | bounded_context | many-to-one | BCs publish contracts |
| validated by | validation_schema | optional | Consumer validates incoming data |

## DDD Published Language Pattern
data_contract IS the DDD Published Language: an explicit schema shared between
bounded contexts that reduces coupling and enables independent evolution.

```
Bounded Context A (Producer)
  +-- domain_event (what happened internally)
  +-- data_contract (what A exposes to outside world)
        |
        v
Bounded Context B (Consumer)
  +-- data_contract (what B accepts)
  +-- validation_schema (B validates incoming against contract)
```

## When to Use
| Scenario | Use |
|----------|-----|
| Data crosses team/system boundary | data_contract |
| Validating LLM output format | validation_schema |
| Cataloging a dataset asset | dataset_card |
| Single system input spec | input_schema |

## Schema Registry Integration
data_contract maps to Apache Avro schema, Protobuf IDL, JSON Schema, or OpenAPI:
- Avro: schema + registry subject name
- Protobuf: .proto message definition
- JSON Schema: $schema + properties
- OpenAPI: components/schemas entry
