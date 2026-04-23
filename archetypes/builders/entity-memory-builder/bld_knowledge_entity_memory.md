---
kind: knowledge_card
id: bld_knowledge_card_entity_memory
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for entity_memory production — entity memory specification
sources: LangChain EntityMemory, Zep entity graphs, Mem0 graph memory, cognitive science entity models
quality: 9.2
title: "Knowledge Card Entity Memory"
version: "1.0.0"
author: n03_builder
tags: [entity_memory, builder, examples]
tldr: "Golden and anti-examples for entity memory construction, demonstrating ideal structure and common pitfalls."
domain: "entity memory construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - entity-memory-builder
  - p03_sp_entity_memory_builder
  - bld_collaboration_entity_memory
  - bld_schema_entity_memory
  - p01_kc_entity_memory
  - bld_instruction_entity_memory
  - bld_architecture_entity_memory
  - p10_lr_entity_memory_builder
  - bld_output_template_entity_memory
  - p01_kc_memory_persistence
---

# Domain Knowledge: entity_memory
## Executive Summary
Entity memory stores structured facts about named entities — people, tools, concepts, organizations, projects, services. Facts are typed key-value attributes with confidence scores and source attribution. Entity records persist across sessions and are injected into LLM context to ground responses in verified knowledge. Entity memory is distinct from learning records (outcome-based) and session state (ephemeral runtime).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (Memory) |
| llm_function | INJECT (grounding context) |
| Entity types | person, tool, concept, organization, project, service |
| Attribute format | map[string, string] — snake_case keys, string values |
| Confidence | float 0.0-1.0 — reliability of stored facts |
| Update policies | append, overwrite, merge, versioned |
| Max bytes | 2048 (body only) |
| Machine format | yaml |
| Naming | p10_entity_{scope}.md |
## Implementation Patterns
- **LangChain EntityMemory**: extracts entity mentions via NER, stores as key-value pairs, injects as "known facts" prefix. Conflict = last-write-wins.
- **Zep entity graphs**: server-side extraction, nodes with typed edges, temporal tracking, graph traversal queries.
- **Mem0 graph memory**: entity + relationship + attribute triples, deduplication via embedding similarity, merge operations.
- **Cognitive science model**: identity + attributes + relationships; activation spreads from queried entity to related nodes.

| Pattern | Example | When to use |
|---------|---------|-------------|
| Flat attributes | `{role: "LLM", provider: "Anthropic"}` | Simple tool/service facts |
| Typed attributes | `{release_date: "2024-03-01", api_version: "v1"}` | Versioned entities |
| Relationship graph | `uses -> firecrawl, owns -> organization-core` | Complex inter-entity models |
| Versioned facts | `{v1: {...}, v2: {...}}` | Entities with breaking changes |

- **Conflict resolution**: last-write-wins (overwrite), confidence-weighted merge, versioned history with timestamp.
- **Staleness handling**: set expiry on volatile entities; purge or flag entities not referenced in > N days.
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Unbounded entity growth | Memory bloat; inject cost exceeds grounding benefit |
| No confidence scoring | Cannot distinguish verified fact from rumor |
| Stale facts without expiry | Tool version "1.0" injected when v3.0 is current |
| Storing inferences as facts | `best_tool: true` — opinion, not fact |
| No relationship links | Isolated nodes miss graph traversal value |
| Mixing entity_memory with learning_record | Outcome data corrupts factual attribute map |
| PII in version-controlled artifacts | Security / privacy violation |
## Application
1. Name the entity: unique slug, human-readable name, entity_type
2. Extract attributes: >= 3 specific facts from primary sources
3. Score confidence: verified=0.9+, inferred=0.5-0.69
4. Map relationships: 1+ links with typed relation verbs
5. Set update_policy: volatile API -> overwrite; stable concept -> append
6. Set expiry: null for stable concepts, date for versioned tools/services
7. Validate: id pattern, attributes non-empty, entity_type in enum, quality null
## References
- LangChain EntityMemory: `langchain.memory.entity`
- Zep: zep.dev entity graph documentation
- Mem0: mem0.ai graph memory architecture
- Cognitive science: spreading activation model (Collins & Loftus, 1975)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[entity-memory-builder]] | downstream | 0.62 |
| [[p03_sp_entity_memory_builder]] | downstream | 0.60 |
| [[bld_collaboration_entity_memory]] | downstream | 0.56 |
| [[bld_schema_entity_memory]] | downstream | 0.53 |
| [[p01_kc_entity_memory]] | sibling | 0.52 |
| [[bld_instruction_entity_memory]] | downstream | 0.51 |
| [[bld_architecture_entity_memory]] | downstream | 0.47 |
| [[p10_lr_entity_memory_builder]] | downstream | 0.46 |
| [[bld_output_template_entity_memory]] | downstream | 0.43 |
| [[p01_kc_memory_persistence]] | sibling | 0.40 |
