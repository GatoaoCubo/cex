---
id: bld_memory_aggregate_root
kind: knowledge_card
pillar: P06
title: "Aggregate Root Builder -- Memory"
version: 1.0.0
quality: 8.4
tags: [builder, aggregate_root, memory, ddd, session_patterns]
llm_function: INJECT
density_score: 0.90
created: "2026-04-17"
updated: "2026-04-22"
author: builder
domain: domain_driven_design
tldr: "Session patterns for aggregate_root: size limits, invariant quality, repository constraints, concurrency defaults, event sourcing."
related:
  - p01_kc_signal
  - bld_schema_invariant
  - p03_sp_agents_md_builder
  - bld_instruction_hook
  - bld_memory_invariant
  - bld_output_template_invariant
  - bld_memory_runtime_state
  - p03_sp_signal_builder
  - p11_qg_runtime_state
  - p03_ins_law
---
# Memory: aggregate_root
## Session Patterns to Remember
- Aggregate size: most production aggregates have 2-5 members. >7 is a smell.
- Invariant quality signal: if an invariant says "must be valid" -- it is not concrete. Push for specific field constraints.
- Repository rule: find_by_id and save are the only methods on the aggregate repository. Queries belong in read models.
- Concurrency: optimistic locking (version field) is the default. Use pessimistic only when contention is proven high.
- Event sourcing: if the domain uses event sourcing, `commands` list becomes `apply(event)` handlers.
## Common Mistakes Seen
- Defining repository with list/query methods: redirect to read model or query service
- Putting domain logic in the repository: domain logic belongs in the root, not the repo
- Forgetting to list domain_events: every command that changes state emits at least one event
- Using service IDs as cluster members: cluster_members must be entities or value objects, not foreign aggregates
## Boundary Vocabulary
- "Cluster" = set of objects inside the aggregate boundary
- "Root" = the single entity with global identity that owns the cluster
- "Invariant" = a business rule that must hold true after every command
- "Command" = a request to change state (may fail if invariant would be violated)
- "Domain event" = a fact that state changed (never fails, past tense)

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
| [[p01_kc_signal]] | sibling | 0.19 |
| [[bld_schema_invariant]] | downstream | 0.18 |
| [[p03_sp_agents_md_builder]] | upstream | 0.18 |
| [[bld_instruction_hook]] | upstream | 0.17 |
| [[bld_memory_invariant]] | downstream | 0.17 |
| [[bld_output_template_invariant]] | related | 0.16 |
| [[bld_memory_runtime_state]] | downstream | 0.16 |
| [[p03_sp_signal_builder]] | upstream | 0.16 |
| [[p11_qg_runtime_state]] | downstream | 0.16 |
| [[p03_ins_law]] | upstream | 0.15 |
