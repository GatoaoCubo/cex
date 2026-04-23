---
id: bld_output_template_aggregate_root
kind: output_template
pillar: P06
title: "Aggregate Root Builder -- Output Template"
version: 1.0.0
quality: 7.4
tags: [builder, aggregate_root, template]
llm_function: PRODUCE
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_output_template_invariant
  - bld_memory_invariant
  - bld_output_template_input_schema
  - bld_collaboration_invariant
  - bld_schema_invariant
---
# Output Template: aggregate_root
```yaml
---
id: p06_ar_{slug}
kind: aggregate_root
pillar: P06
title: "Aggregate Root: {Name}"
version: 0.1.0
bounded_context: "{BoundedContext}"
invariants:
  - "{Invariant 1: concrete measurable rule}"
  - "{Invariant 2: concrete measurable rule}"
commands:
  - "{CommandName}: precondition={X}, postcondition={Y}"
domain_events:
  - "{EventName}: emitted when {condition}, payload={fields}"
repository: "{Name}Repository"
cluster_members:
  - "{EntityName} (entity)"
  - "{ValueObjectName} (value_object)"
identity_type: uuid
concurrency_strategy: optimistic
quality: null
tags: [aggregate_root, {bounded_context}, {domain_slug}]
tldr: "{Name} aggregate root: owns {N} members, enforces {K} invariants, emits {M} events"
---

## Identity
**Root entity**: {Name}
**Bounded context**: {BoundedContext}
**Cluster members**: {list with types}

## Invariants
1. {Invariant 1 -- stated as an always-true fact, not a wish}
2. {Invariant 2}

## Commands
### {CommandName}(params)
- Precondition: {what must be true before}
- Postcondition: {what is guaranteed after}
- Emits: {DomainEvent}

## Domain Events
### {EventName}
- Trigger: {which command emits this}
- Payload: {field: type, ...}

## Repository
Interface: {Name}Repository
- find_by_id(id: {IdType}) -> Optional[{Name}]
- save(aggregate: {Name}) -> void

## Boundaries
**Inside**: {list of entities and value objects}
**Outside**: {aggregates referenced by ID only}
```

## Output Template Checklist

- Verify output format matches target kind schema
- Validate all frontmatter fields are present in template
- Cross-reference with eval gate for completeness
- Test template rendering with sample data before publishing

## Output Pattern

```yaml
# Output validation
format_match: true
frontmatter_complete: true
eval_gate_aligned: true
sample_rendered: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_invariant]] | sibling | 0.18 |
| [[bld_memory_invariant]] | downstream | 0.17 |
| [[bld_output_template_input_schema]] | sibling | 0.15 |
| [[bld_collaboration_invariant]] | downstream | 0.15 |
| [[bld_schema_invariant]] | downstream | 0.15 |
