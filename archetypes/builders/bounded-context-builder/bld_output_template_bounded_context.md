---
id: bld_tpl_bounded_context
kind: prompt_template
pillar: P03
llm_function: PRODUCE
version: 1.0.0
quality: null
tags: [bounded_context, template, output]
title: "Output Template: bounded_context"
---
# Output Template: bounded_context
```markdown
---
id: bc_{{context_snake}}
kind: bounded_context
pillar: P08
title: "{{ContextName}} Bounded Context"
version: 1.0.0
quality: null
context_name: {{ContextNamePascalCase}}
team_owner: {{team_name}}
scope_statement: "{{What domain model applies within this boundary -- 1-2 sentences.}}"
domain_vocabulary: dv_{{context_snake}}_vocabulary
tags: [{{context}}, bounded-context, ddd]
---

# {{ContextName}} Bounded Context

## Scope
{{scope_statement expanded: what domain model applies here, what does NOT apply here.}}

## Aggregates
| Aggregate | Role | Key Invariants |
|-----------|------|---------------|
| {{AggName}} | {{role}} | {{business_rule}} |

## Integration Patterns
| Neighbor Context | Pattern | Direction | Rationale |
|-----------------|---------|-----------|-----------|
| {{bc_neighbor}} | {{ACL/OHS/CF/Partnership}} | upstream/downstream | {{why this pattern}} |

## Domain Events Published
| Event | Consumers |
|-------|-----------|
| {{EventName}} | [{{bc_consumer_1}}, {{bc_consumer_2}}] |

## Key Business Rules
- {{rule that holds WITHIN this BC and NOT in other BCs}}

## Context Map Position
{{Brief description of where this BC sits in the overall context map.}}
```
