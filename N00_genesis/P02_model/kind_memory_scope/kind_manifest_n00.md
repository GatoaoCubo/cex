---
id: n00_memory_scope_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Memory Scope -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, memory_scope, p02, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Memory Scope defines the memory configuration for an AI agent: which memory types are active (correction, preference, convention, context), the storage backend, retention policy, and decay parameters. It controls what an agent remembers across sessions, how long memories persist, and when outdated memories are pruned. Injected into agent prompts to provide persistent context.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `memory_scope` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Scope name and agent |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nucleus | string | yes | Owning nucleus |
| memory_types | list | yes | Active types: correction, preference, convention, context |
| storage_path | string | yes | Path to memory storage directory |
| decay_days | int | yes | Days until memory weight decays to 0 |
| max_memories | int | no | Maximum memories to retain before pruning |
| inject_top_n | int | yes | Number of relevant memories to inject per session |

## When to use
- When configuring persistent memory for a nucleus or agent
- When tuning memory retention and decay for a specific task domain
- When enabling user preference learning across sessions

## Builder
`archetypes/builders/memory_scope-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind memory_scope --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- the agent this memory scope serves
- `{{DOMAIN_CONTEXT}}` -- task domain and session characteristics

## Example (minimal)
```yaml
---
id: memory_scope_n07_orchestrator
kind: memory_scope
pillar: P02
nucleus: n07
title: "N07 Orchestrator Memory Scope"
version: 1.0
quality: null
---
nucleus: n07
memory_types: [correction, preference, convention, context]
storage_path: ".cex/runtime/memory/n07/"
decay_days: 365
max_memories: 500
inject_top_n: 10
```

## Related kinds
- `agent` (P02) -- agent this memory scope is attached to
- `entity_memory` (P10) -- specific entity records within this scope
- `memory_summary` (P10) -- compressed memory for token efficiency
