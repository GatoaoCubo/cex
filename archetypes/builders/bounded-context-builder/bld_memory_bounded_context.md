---
id: bld_memory_bounded_context
kind: entity_memory
pillar: P10
llm_function: INJECT
version: 1.0.0
quality: null
tags: [bounded_context, memory, ddd]
title: "Memory Patterns: bounded_context"
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
