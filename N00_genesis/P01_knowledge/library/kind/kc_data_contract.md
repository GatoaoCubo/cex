---
id: p01_kc_data_contract
kind: knowledge_card
type: kind
pillar: P01
title: "Data Contract -- Deep Knowledge for data_contract"
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
domain: data_contract
quality: 8.8
tags: [data_contract, p06, CONSTRAIN, kind-kc, schema, sla, published-language]
tldr: "Schema-level agreement between data producer and consumer defining structure, semantics, and SLA; NOT dataset_card (metadata) nor validation_schema (LLM output)."
when_to_use: "Formalizing data exchange between teams or systems that cross a bounded context boundary"
keywords: [data-contract, schema-agreement, sla, producer-consumer, published-language]
feeds_kinds: [data_contract]
density_score: null
aliases: ["schema agreement", "data API contract", "producer-consumer contract", "published language"]
user_says: ["define contract between X and Y", "schema agreement", "what data does X expose to Y", "SLA for data"]
long_tails: ["define the schema and SLA between a data producer and consumer", "formalize what data one service exposes to another", "create a schema contract for cross-team data exchange"]
related:
  - bld_collaboration_input_schema
  - bld_instruction_interface
  - p10_lr_interface_builder
  - enterprise-sla-builder
  - bld_knowledge_card_interface
  - p11_qg_interface
  - bld_collaboration_validation_schema
  - bld_knowledge_card_input_schema
  - p01_kc_input_schema
  - p03_sp_validation-schema-builder
---

# Data Contract

## Spec
```yaml
kind: data_contract
pillar: P06
llm_function: CONSTRAIN
max_bytes: 4096
naming: dc_{producer}_{consumer}_{entity}.md
```

## What It Is
A data_contract is a schema-level agreement between a data producer and consumer defining structure, semantics, and SLA. It implements the DDD Published Language pattern -- a formalized, versioned schema that both parties agree to honor. Three components: schema (field names, types, nullable flags), semantics (field meanings and business rules), SLA (freshness, availability, latency thresholds). The contract is versioned INDEPENDENTLY from the producer's implementation version -- contract v1.2.0 can coexist with service v3.5.0.

## Boundary
| Aspect | data_contract | dataset_card | validation_schema |
|--------|-------------|--------------|-------------------|
| Purpose | Cross-boundary agreement | Data asset catalog | LLM output check |
| Parties | Producer + Consumer | Catalog + users | LLM + evaluator |
| SLA | Required | Optional metadata | N/A |
| DDD pattern | Published Language | Data catalog | N/A |

## SLA Metrics Reference
| Metric | Definition | Typical Thresholds |
|--------|-----------|-------------------|
| freshness | Max age of data at consumption | < 5s (real-time), < 15min (near-RT), daily (batch) |
| availability | Pipeline uptime | 99.5% (standard), 99.9% (mission-critical) |
| latency_p99 | 99th percentile response time | < 200ms (API), < 1s (event bus) |
| completeness | Non-null rate for required fields | >= 99% |
| accuracy | Data quality score | domain-specific, usually >= 95% |

## Versioning Policy (Industry Standard)
- Major bump (1.0.0 -> 2.0.0): breaking change (field removed/renamed, type changed)
- Minor bump (1.0.0 -> 1.1.0): additive change (new optional field)
- Patch bump: documentation update only
- Breaking changes require: 30-day deprecation notice + migration guide + old version support period
- Consumer-driven: consumers specify what they need; producers comply or negotiate

## Framework Equivalents
| Framework | Equivalent | Notes |
|-----------|-----------|-------|
| Apache Avro | Schema + registry subject | Kafka ecosystem, schema evolution |
| Protobuf IDL | .proto message + service | gRPC, binary, high-performance |
| OpenAPI 3.x | components/schemas | REST APIs, human-readable |
| dbt contracts (1.5+) | model contracts | SQL data warehouses |
| Pact | Consumer-driven CDC | Microservices integration testing |
| AsyncAPI | message schemas | Event-driven APIs |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Implicit schema (undocumented) | Consumers break on schema changes | Explicit data_contract per exchange |
| Contract = implementation spec | Couples consumer to producer internals | Consumer-centric: expose only what consumer needs |
| Vague SLA ("fast") | Unmeasurable, unenforceable | Numeric thresholds with units |
| Contract tied to service version | Forces synchronized releases | Independent contract_version |

## Decision Tree
- IF data crosses team/system boundary -> data_contract
- IF validating LLM output format -> validation_schema
- IF cataloging a data asset -> dataset_card
- IF single system input spec -> input_schema
- IF event crossing bounded context -> domain_event + data_contract (Published Language)
- DEFAULT: data_contract for any formal cross-boundary data exchange agreement

## Quality Criteria
- GOOD: typed schema, numeric SLA, producer + consumer named, independent contract_version
- GREAT: schema registry ref + backward compat policy + contract tests + deprecation notice
- FAIL: vague SLA OR missing producer/consumer OR no typed schema fields

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_input_schema]] | downstream | 0.26 |
| [[bld_instruction_interface]] | downstream | 0.25 |
| [[p10_lr_interface_builder]] | downstream | 0.23 |
| [[enterprise-sla-builder]] | downstream | 0.23 |
| [[bld_knowledge_card_interface]] | sibling | 0.22 |
| [[p11_qg_interface]] | downstream | 0.22 |
| [[bld_collaboration_validation_schema]] | downstream | 0.22 |
| [[bld_knowledge_card_input_schema]] | sibling | 0.22 |
| [[p01_kc_input_schema]] | sibling | 0.21 |
| [[p03_sp_validation-schema-builder]] | downstream | 0.20 |
