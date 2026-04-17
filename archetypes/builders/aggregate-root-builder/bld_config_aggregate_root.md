---
id: bld_context_sources_aggregate_root
kind: knowledge_card
pillar: P06
title: "Aggregate Root Builder -- Context Sources"
version: 1.0.0
quality: null
tags: [builder, aggregate_root, context]
llm_function: INJECT
---
# Context Sources: aggregate_root
## Mandatory Loads (F3 INJECT)
| Source | Path | Purpose |
|--------|------|---------|
| Kind KC | N00_genesis/P01_knowledge/library/kind/kc_aggregate_root.md | Primary definition |
| Schema | archetypes/builders/aggregate-root-builder/bld_schema_aggregate_root.md | Field constraints |
| Output template | archetypes/builders/aggregate-root-builder/bld_output_template_aggregate_root.md | Structure guide |
| Examples | archetypes/builders/aggregate-root-builder/bld_examples_aggregate_root.md | Golden patterns |
| Pillar schema | N00_genesis/P06_schema/_schema.yaml | Pillar constraints |
## Related Kind KCs
| KC | Relationship |
|----|-------------|
| kc_value_object.md | members inside the aggregate cluster |
| kc_interface.md | repository contract that aggregate depends on |
| kc_input_schema.md | validates data before it enters the aggregate |
| kc_domain_event.md | facts emitted by the aggregate |
## External References
| Source | Relevance |
|--------|----------|
| Evans DDD (2003) Ch. 6 | Original aggregate pattern definition |
| Vernon IDDD (2013) Ch. 10 | Aggregate sizing, event sourcing integration |
| Microsoft DDD guide | Aggregate root in CQRS + event sourcing contexts |
## CEX Artifact Examples
Search: `kind: aggregate_root` in any N03_engineering or N05_operations directory
