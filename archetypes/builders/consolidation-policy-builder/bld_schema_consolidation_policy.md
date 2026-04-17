---
kind: schema
id: bld_schema_consolidation_policy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for consolidation_policy
quality: 9.2
title: "Schema: consolidation_policy"
version: "2.0.0"
author: n06_commercial
tags: [consolidation_policy, builder, schema]
tldr: "Schema for LLM agent memory consolidation policy artifacts: promotion rules, eviction strategy, importance scoring, compliance config"
domain: "LLM agent memory consolidation"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

## Frontmatter Fields

### Required

| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | null | Must match `^p10_cp_[a-z][a-z0-9_]+$` |
| kind | string | yes | "consolidation_policy" | Fixed value |
| pillar | string | yes | "P10" | Fixed value |
| title | string | yes | null | Descriptive name for the policy |
| version | string | yes | "1.0.0" | Semver |
| created | string | yes | null | ISO 8601 date |
| updated | string | yes | null | ISO 8601 date |
| author | string | yes | null | Nucleus or person responsible |
| domain | string | yes | null | Agent domain (e.g., "customer-support") |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Keywords including tier and strategy |
| tldr | string | yes | null | One-sentence summary |
| tier | string | yes | null | free, pro, enterprise |
| eviction_strategy | string | yes | null | lru, lfu, ttl, importance, generational, hybrid |
| consolidation_async | boolean | yes | true | Must be true; sync consolidation blocks agent |

### Recommended

| Field | Type | Notes |
|---|---|---|
| importance_floor | float | Below this score, evict (e.g., 0.3) |
| retention_days | integer | Episodic memory TTL in days |
| promotion_threshold | float | Importance score for semantic promotion (e.g., 0.7) |
| compliance | dict | GDPR, HIPAA, data_residency settings (enterprise only) |
| audit_trail | boolean | Log every consolidation event |

## ID Pattern

```
^p10_cp_[a-z][a-z0-9_]+$
```

Example IDs:
- `p10_cp_customer_support_pro`
- `p10_cp_research_agent_enterprise`
- `p10_cp_minimal_ttl_only`

## Body Structure

1. **Overview** -- agent type, tier, consolidation strategy summary
2. **Promotion Rules** -- table: trigger | source_layer | target_layer | condition
3. **Eviction Rules** -- table: layer | strategy | trigger | action
4. **Importance Scoring** -- formula or model reference for scoring memory units
5. **Consolidation Job** -- async trigger, schedule, timeout, failure handling
6. **Commercial Tier Matrix** -- FREE/PRO/ENTERPRISE capability comparison
7. **Compliance Config** -- retention_days, data_residency, audit_trail, gdpr_erasure

## Constraints

- `consolidation_async` MUST be `true` -- synchronous consolidation blocks agent.
- `eviction_strategy` must be one of: lru, lfu, ttl, importance, generational, hybrid.
- Enterprise tier artifacts MUST include Compliance Config section.
- `promotion_threshold` must be in range [0.0, 1.0].
- quality MUST be null (never self-assign a score).
- No OS memory management terminology (GC, slab, heap, fragmentation, TLB).
