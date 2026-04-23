---
id: bld_tpl_bounded_context
kind: prompt_template
pillar: P03
llm_function: PRODUCE
version: 1.0.0
quality: 8.1
tags: [bounded_context, template, output]
title: "Output Template: bounded_context"
author: builder
density_score: 1.0
created: "2026-04-17"
updated: "2026-04-17"
related:
  - kc_model_context_protocol
  - bld_knowledge_card_context_doc
  - context-doc-builder
  - bld_collaboration_context_doc
  - p01_kc_context_doc
  - bld_knowledge_card_context_window_config
  - p01_kc_context_window_config
  - bld_instruction_context_doc
  - bld_output_template_context_doc
  - bld_config_context_window_config
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_model_context_protocol]] | upstream | 0.34 |
| [[bld_knowledge_card_context_doc]] | upstream | 0.33 |
| [[context-doc-builder]] | upstream | 0.25 |
| [[bld_collaboration_context_doc]] | downstream | 0.24 |
| [[p01_kc_context_doc]] | upstream | 0.22 |
| [[bld_knowledge_card_context_window_config]] | upstream | 0.18 |
| [[p01_kc_context_window_config]] | related | 0.17 |
| [[bld_instruction_context_doc]] | related | 0.16 |
| [[bld_output_template_context_doc]] | downstream | 0.16 |
| [[bld_config_context_window_config]] | downstream | 0.16 |
