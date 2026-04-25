---
id: bld_memory_data_contract
kind: entity_memory
pillar: P10
llm_function: INJECT
version: 1.0.0
quality: 8.3
tags: [data_contract, memory, patterns]
title: "Memory Patterns: data_contract"
author: builder
tldr: "Data Contract memory: context persistence, recall triggers, and state management"
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_collaboration_validation_schema
  - p03_sp_validation-schema-builder
  - validation-schema-builder
  - p01_kc_validation_schema
  - bld_instruction_interface
  - bld_collaboration_input_schema
  - bld_architecture_validation_schema
  - bld_collaboration_enterprise_sla
  - enterprise-sla-builder
  - p03_sp_enterprise_sla_builder
---
# Memory Patterns: data_contract
## What to Remember
- Contract versioning is INDEPENDENT from service versioning
- SLA must be numeric -- not "fast" or "reliable" but "< 200ms" and "99.9%"
- Producer owns the schema; consumer specifies what they need (CDC pattern)
- data_contract boundary: schema+SLA between systems, NOT LLM output validation

## Common Mistakes
| Mistake | Correction |
|---------|-----------|
| Conflating with validation_schema | data_contract = cross-system; validation_schema = LLM output |
| Vague SLA ("near real-time") | Numeric: "< 5 seconds", "99.9%", "< 200ms p99" |
| Contract version tied to service | Contract v1.2.0 independent from service v3.5.1 |
| Missing consumer_system | Always name both sides of the agreement |

## Cross-Kind Memory
- domain_event: events crossing BC boundaries need data_contracts
- bounded_context: contracts formalize BC-to-BC communication
- validation_schema: downstream consumers use this to validate incoming data
- dataset_card: separate concern -- data asset metadata, not exchange agreement

## Reuse Signals
- Check existing contracts: grep P06 for dc_ prefix files
- Check schema registry (if configured) before creating new contract
- Consumer-driven: ask consumer team what fields they actually need

## Memory Persistence Checklist

- Verify memory type matches taxonomy (entity, episodic, procedural, working)
- Validate retention policy aligns with data lifecycle rules
- Cross-reference with memory_scope for boundary correctness
- Check for stale entries that need decay or pruning

## Memory Pattern

```yaml
# Memory lifecycle
type: classified
retention: defined
scope: bounded
decay: configured
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_memory_update.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_validation_schema]] | upstream | 0.25 |
| [[p03_sp_validation-schema-builder]] | upstream | 0.24 |
| [[validation-schema-builder]] | upstream | 0.24 |
| [[p01_kc_validation_schema]] | upstream | 0.23 |
| [[bld_instruction_interface]] | upstream | 0.22 |
| [[bld_collaboration_input_schema]] | downstream | 0.22 |
| [[bld_architecture_validation_schema]] | upstream | 0.21 |
| [[bld_collaboration_enterprise_sla]] | downstream | 0.21 |
| [[enterprise-sla-builder]] | downstream | 0.21 |
| [[p03_sp_enterprise_sla_builder]] | upstream | 0.21 |
