---
quality: 7.4
id: bld_schema_bounded_context
kind: input_schema
pillar: P06
llm_function: CONSTRAIN
version: 1.0.0
quality: 7.2
tags: [bounded_context, schema, ddd]
title: "Schema Bounded Context"
density_score: 1.0
updated: "2026-04-17"
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
