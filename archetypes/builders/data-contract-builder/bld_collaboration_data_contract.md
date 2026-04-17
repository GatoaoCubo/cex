---
id: bld_rules_data_contract
kind: guardrail
pillar: P11
llm_function: COLLABORATE
version: 1.0.0
quality: 6.5
tags: [data_contract, rules, guardrail]
title: "Rules: data_contract Builder"
density_score: 1.0
updated: "2026-04-17"
---
# Builder Rules: data_contract
## ALWAYS
- ALWAYS name both producer_system and consumer_system explicitly
- ALWAYS version the contract independently from the service version
- ALWAYS use numeric SLA thresholds (< 200ms, 99.9%, < 5s)
- ALWAYS type every schema field (string, uuid, decimal, ISO-4217, etc.)
- ALWAYS set quality: null

## NEVER
- NEVER use data_contract for LLM output validation (use validation_schema)
- NEVER use data_contract for data catalog (use dataset_card)
- NEVER write vague SLAs ("fast", "reliable", "near real-time")
- NEVER tie contract_version to service implementation version
- NEVER omit nullable flag for schema fields

## EDGE CASES
| Case | Rule |
|------|------|
| Bidirectional contract (A->B and B->A) | Create two contracts, one per direction |
| Contract with multiple consumers | One contract per consumer (consumer-driven) |
| Schema change breaking | New contract_version (semver major bump) + migration guide |
| Deprecated field | Keep in schema with deprecated: true + removal_date |

## Naming Conventions
| Pattern | Example |
|---------|---------|
| dc_{producer}_{consumer}_{entity} | dc_sales_billing_order |
| Entity is PascalCase | Order, ClickEvent, UserProfile |
| Systems are kebab-case | sales-service, analytics-warehouse |

## Size Budget
max_bytes: 4096 (schema table + SLA table + versioning = ~2.5KB typical)
Table format preferred over YAML blocks for schema fields.
