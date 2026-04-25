---
id: bld_memory_bounded_context
kind: entity_memory
pillar: P10
llm_function: INJECT
version: 1.0.0
quality: 8.1
tags: [bounded_context, memory, ddd]
title: "Memory Patterns: bounded_context"
author: builder
tldr: "Bounded Context memory: context persistence, recall triggers, and state management"
density_score: 0.94
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_instruction_kind
---
# Memory Patterns: bounded_context
## What to Remember
- bounded_context = SEMANTIC boundary, not technical (not service, not namespace)
- Each BC has its own model; same word means different things in different BCs
- Integration patterns matter: ACL protects, OHS publishes, CF conforms
- Every BC needs a domain_vocabulary; domain_vocabulary scoped to the BC
- CEX nuclei (N01-N07) map to bounded contexts with their own vocabularies

## Common Mistakes
| Mistake | Correction |
|---------|-----------|
| BC = microservice | BC is a team/model boundary, not a deployment unit |
| One model for all | Each BC has its own aggregates and rules |
| No context map | Always document integration patterns with neighbors |
| Missing vocabulary ref | Every BC should reference its domain_vocabulary |

## Cross-Kind Memory
- domain_vocabulary: each BC has exactly one, scoped to the BC
- domain_event: events originate within a BC; cross-BC events need data_contract
- data_contract: formalizes Published Language between BCs
- component_map: deployment structure -- separate concern from BC

## Reuse Signals
- Check if BC already exists: grep P08 for bc_ prefix files
- nucleus_def_n0X.md may already define a BC implicitly
- Context map (if it exists) lists all registered BCs

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
| [[bld_instruction_kind]] | upstream | 0.16 |
