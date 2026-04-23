---
quality: 7.6
id: bld_rules_aggregate_root
kind: knowledge_card
pillar: P06
title: "Aggregate Root Builder -- Rules"
version: 1.0.0
quality: 7.3
tags: [builder, aggregate_root, rules]
llm_function: COLLABORATE
author: builder
density_score: 0.82
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_architecture_kind
  - bld_collaboration_builder
  - p03_sp__builder_builder
  - kind-builder
  - p03_sp_kind_builder
  - bld_collaboration_validation_schema
  - p03_sp_n03_creation_nucleus
  - bld_collaboration_retriever
  - p03_sp_type-def-builder
  - bld_collaboration_input_schema
---
# Rules: aggregate_root
## Absolute Rules (HARD -- never violate)
1. One transaction = one aggregate. Never span two aggregates in a single transaction.
2. External references to cluster members go through the root only -- never directly.
3. Cross-aggregate references use IDs (value_object), never object instances.
4. Repository interface: find_by_id and save only. No query methods on the aggregate repo.
5. Invariants must be checkable after every command -- they are not guidelines.
6. quality: null always -- never self-score.
## Soft Rules (RECOMMEND -- deviate with justification)
1. Aggregate cluster size: prefer 2-5 members. Document reason if > 7.
2. Optimistic concurrency preferred over pessimistic unless contention proven.
3. Domain events should be named in past tense (OrderPlaced, not PlaceOrder).
4. Invariant count: 2-5 per aggregate. More than 8 suggests over-aggregation.
## Boundary Rules
1. THIS BUILDER handles: aggregate_root (P06)
2. NOT this builder: interface (contract definition) -> interface-builder
3. NOT this builder: input_schema (data validation) -> input-schema-builder
4. NOT this builder: value_object (immutable attribute type) -> value-object-builder
5. NOT this builder: domain event specification -> domain-event-builder
## CEX-Specific Rules
1. id pattern: p06_ar_{slug} -- always prefix p06_ar_
2. Pillar: always P06 (Schema)
3. Producing nucleus: N03 (Engineering) -- not N04 or N05
4. Compile after save: python _tools/cex_compile.py {path}

## Orchestration Checklist

- Verify workflow topology matches dependency graph
- Validate handoff protocol between upstream and downstream
- Cross-reference with dispatch rules for routing correctness
- Test wave sequencing with dry-run before live dispatch

## Orchestration Pattern

```yaml
# Workflow validation
topology: verified
handoffs: validated
routing: checked
sequencing: tested
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope orchestration
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.28 |
| [[bld_collaboration_builder]] | downstream | 0.24 |
| [[p03_sp__builder_builder]] | upstream | 0.24 |
| [[kind-builder]] | downstream | 0.24 |
| [[p03_sp_kind_builder]] | upstream | 0.23 |
| [[bld_collaboration_validation_schema]] | related | 0.23 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.23 |
| [[bld_collaboration_retriever]] | downstream | 0.22 |
| [[p03_sp_type-def-builder]] | upstream | 0.22 |
| [[bld_collaboration_input_schema]] | downstream | 0.22 |
