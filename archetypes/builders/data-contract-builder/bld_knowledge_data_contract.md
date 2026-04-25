---
id: bld_kc_data_contract
kind: knowledge_card
pillar: P01
llm_function: INJECT
version: 1.0.0
quality: 7.6
tags: [data_contract, schema, published-language, knowledge]
title: "Knowledge: Data Contract Pattern"
author: builder
tldr: "Data Contract knowledge: domain knowledge, terminology, and contextual background"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_collaboration_input_schema
  - bld_collaboration_validation_schema
  - bld_knowledge_card_interface
  - p10_lr_action-prompt-builder
  - bld_collaboration_interface
  - bld_instruction_interface
  - p03_sp_validation-schema-builder
  - enterprise-sla-builder
  - input-schema-builder
  - validation-schema-builder
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

## Knowledge Injection Checklist

- Verify domain facts are sourced and citable
- Validate density_score >= 0.85 (no filler content)
- Cross-reference with related KCs for consistency
- Check for outdated facts that need refresh

## Injection Pattern

```yaml
# KC injection at F3
source: verified
density: 0.85+
cross_refs: checked
freshness: current
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_retriever.py --query "{DOMAIN}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_input_schema]] | downstream | 0.27 |
| [[bld_collaboration_validation_schema]] | downstream | 0.21 |
| [[bld_knowledge_card_interface]] | sibling | 0.19 |
| [[p10_lr_action-prompt-builder]] | downstream | 0.19 |
| [[bld_collaboration_interface]] | downstream | 0.18 |
| [[bld_instruction_interface]] | downstream | 0.18 |
| [[p03_sp_validation-schema-builder]] | downstream | 0.17 |
| [[enterprise-sla-builder]] | downstream | 0.17 |
| [[input-schema-builder]] | downstream | 0.17 |
| [[validation-schema-builder]] | downstream | 0.17 |
