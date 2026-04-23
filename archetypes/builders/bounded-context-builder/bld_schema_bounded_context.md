---
quality: 8.0
quality: 7.5
id: bld_schema_bounded_context
kind: input_schema
pillar: P06
llm_function: CONSTRAIN
version: 1.0.0
tags: [bounded_context, schema, ddd]
title: "Schema Bounded Context"
author: builder
density_score: 1.0
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_sandbox_config
  - bld_schema_benchmark_suite
  - bld_schema_quickstart_guide
  - bld_schema_action_paradigm
  - bld_schema_search_strategy
---
# Schema: bounded_context
## Frontmatter Fields (Required)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| id | string (bc_{context}) | YES | snake_case domain name |
| kind | literal "bounded_context" | YES | — |
| pillar | literal "P08" | YES | — |
| title | string | YES | "{ContextName} Bounded Context" |
| version | semver | YES | 1.0.0 start |
| quality | null | YES | Never self-score |
| context_name | string (PascalCase) | YES | Domain name of this context |
| team_owner | string | YES | Team or squad name |
| scope_statement | string | YES | What model applies here (1-2 sentences) |
| domain_vocabulary | string | REC | Reference to dv_{context}_vocabulary |
| tags | list[string] | YES | >= 3 tags |

## Body Sections (Required)
```markdown
## Aggregates
| Aggregate | Role | Key Invariants |
|-----------|------|---------------|
| {AggName} | {role in this BC} | {business rules} |

## Integration Patterns
| Neighbor Context | Pattern | Direction | Notes |
|-----------------|---------|-----------|-------|
| {context} | ACL|OHS|CF|Partnership | upstream|downstream | {rationale} |

## Key Business Rules
- {rule that holds WITHIN this BC}
```

## Integration Pattern Reference
| Pattern | Abbreviation | Meaning |
|---------|-------------|---------|
| Anti-Corruption Layer | ACL | Protect this BC from upstream model |
| Open Host Service | OHS | Publish public API for consumers |
| Conformist | CF | Adopt upstream model as-is |
| Partnership | P | Two teams coordinate changes together |
| Published Language | PL | Formalized schema (see data_contract) |

## ID Pattern
`^bc_[a-z][a-z0-9_]+$`
Example: bc_sales, bc_billing, bc_identity, bc_cex_orchestration

## Constraints
- max_bytes: 4096
- scope_statement max 200 chars
- aggregates section min 1 aggregate

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | related | 0.56 |
| [[bld_schema_usage_report]] | related | 0.55 |
| [[bld_schema_pitch_deck]] | related | 0.55 |
| [[bld_schema_dataset_card]] | related | 0.55 |
| [[bld_schema_integration_guide]] | related | 0.54 |
| [[bld_schema_sandbox_config]] | related | 0.53 |
| [[bld_schema_benchmark_suite]] | related | 0.53 |
| [[bld_schema_quickstart_guide]] | related | 0.53 |
| [[bld_schema_action_paradigm]] | related | 0.52 |
| [[bld_schema_search_strategy]] | related | 0.52 |
