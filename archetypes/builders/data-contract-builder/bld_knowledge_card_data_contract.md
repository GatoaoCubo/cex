---
id: bld_kc_data_contract
kind: knowledge_card
pillar: P01
llm_function: INJECT
version: 1.0.0
quality: 6.5
tags: [data_contract, schema, published-language, knowledge]
title: "Knowledge: Data Contract Pattern"
density_score: 1.0
updated: "2026-04-17"
---
# Domain Knowledge: data_contract
## Core Facts
- DDD Published Language (Evans 2003): explicit schema shared between BCs
- Industry standard: Atlan/Monte Carlo data contracts (2022+), dbt contracts (1.5+)
- Three components: schema (structure), semantics (meaning), SLA (quality)
- Versioned independently from producer implementation (contract v1 != service v1)
- Consumer-driven contract testing: consumers define what they need, producers comply

## Framework Equivalents
| Framework | Equivalent | Notes |
|-----------|-----------|-------|
| Protobuf IDL | message definition | Binary, schema registry |
| Apache Avro | Schema + subject | Kafka ecosystem standard |
| OpenAPI | components/schemas | REST API contracts |
| dbt | model contracts (1.5+) | SQL data warehouse |
| Pact | Consumer-driven CDC | Microservices testing |

## SLA Metrics Reference
| Metric | Typical Threshold | Measurement |
|--------|------------------|-------------|
| freshness | < 15min (near-real-time) | Max age of newest record |
| availability | 99.5% - 99.9% | Uptime of data pipeline |
| latency_p99 | < 500ms (API) | 99th percentile response |
| completeness | >= 99% | Non-null rate for required fields |

## Anti-Patterns
| Anti-Pattern | Correct Approach |
|-------------|-----------------|
| Implicit schema (undocumented) | Explicit data_contract per exchange |
| Contract = implementation spec | Contract is consumer view, not internal |
| Single versioning (tied to service) | Contract versioned independently |
