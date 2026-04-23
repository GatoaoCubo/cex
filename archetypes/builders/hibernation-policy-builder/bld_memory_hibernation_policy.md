---
kind: entity_memory
id: bld_memory_hibernation_policy
pillar: P10
llm_function: INJECT
purpose: P10 memory hooks for hibernation_policy builder
quality: 8.1
title: "Memory: hibernation_policy Builder"
version: "1.0.0"
author: n03_engineering
tags: [hibernation_policy, builder, memory]
tldr: "P10 memory hooks for hibernation_policy builder"
domain: "hibernation_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_architecture_entity_memory
  - bld_collaboration_memory_type
  - p01_kc_memory_scope
  - bld_collaboration_entity_memory
  - p01_kc_memory_persistence
  - entity-memory-builder
  - bld_collaboration_session_backend
  - bld_examples_memory_scope
  - bld_knowledge_card_memory_scope
  - memory-architecture-builder
---

## hibernation_policy Memory Hooks

### What to remember across sessions

| Entity | Memory type | Why |
|--------|-------------|-----|
| Target backend for this project | entity_memory | Avoids re-asking backend type on every build |
| Wake latency SLA requirements | entity_memory | Organization-level SLA may apply to all policies |
| Cost savings targets | entity_memory | Budget context informs estimate_pct |
| Sibling terminal_backend artifact IDs | entity_memory | Enables consistency check on rebuild |

### Session-level context (working_memory)
- Which backends are active in this deployment
- Any exceptions to the standard idle threshold (e.g., a 5-minute override for a specific GPU job)
- Whether the user has specified an explicit N07 signal pattern for hibernate/wake

## Memory Anti-patterns
- Do NOT store the actual YAML frontmatter in memory -- read the file
- Do NOT cache the backend support matrix -- it changes; read the KC
- Do NOT remember costs as hard facts -- they are estimates; re-derive from context

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_entity_memory]] | upstream | 0.30 |
| [[bld_collaboration_memory_type]] | downstream | 0.30 |
| [[p01_kc_memory_scope]] | upstream | 0.29 |
| [[bld_collaboration_entity_memory]] | downstream | 0.28 |
| [[p01_kc_memory_persistence]] | upstream | 0.28 |
| [[entity-memory-builder]] | related | 0.26 |
| [[bld_collaboration_session_backend]] | downstream | 0.25 |
| [[bld_examples_memory_scope]] | upstream | 0.23 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.23 |
| [[memory-architecture-builder]] | related | 0.23 |
