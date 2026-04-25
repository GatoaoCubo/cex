---
id: bld_architecture_data_contract
kind: component_map
pillar: P08
llm_function: CONSTRAIN
version: 1.0.0
quality: 8.3
tags: [data_contract, architecture, published-language]
title: "Architecture Data Contract"
author: builder
tldr: "Data Contract architecture: component map, dependencies, and structural constraints"
density_score: 1.0
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p03_sp_validation-schema-builder
  - bld_collaboration_validation_schema
  - p01_kc_validation_schema
  - p01_kc_input_schema
  - bld_architecture_validation_schema
  - validation-schema-builder
  - bld_collaboration_input_schema
  - bld_knowledge_card_validation_schema
  - bld_knowledge_card_input_schema
  - input-schema-builder
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_validation-schema-builder]] | upstream | 0.32 |
| [[bld_collaboration_validation_schema]] | upstream | 0.30 |
| [[p01_kc_validation_schema]] | upstream | 0.28 |
| [[p01_kc_input_schema]] | upstream | 0.26 |
| [[bld_architecture_validation_schema]] | related | 0.26 |
| [[validation-schema-builder]] | upstream | 0.25 |
| [[bld_collaboration_input_schema]] | downstream | 0.24 |
| [[bld_knowledge_card_validation_schema]] | upstream | 0.23 |
| [[bld_knowledge_card_input_schema]] | upstream | 0.22 |
| [[input-schema-builder]] | upstream | 0.22 |
