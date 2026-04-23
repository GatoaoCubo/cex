---
kind: architecture
id: bld_architecture_entity_memory
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of entity_memory — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Entity Memory"
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
  - bld_collaboration_entity_memory
  - p03_sp_entity_memory_builder
  - p11_qg_entity_memory
  - bld_knowledge_card_entity_memory
  - bld_instruction_entity_memory
  - bld_schema_entity_memory
  - bld_output_template_entity_memory
  - p01_kc_entity_memory
  - bld_tools_entity_memory
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| entity_id | Unique identifier for the entity record | entity_memory | required |
| entity_type | Classification (person/tool/concept/org/project/service) | entity_memory | required |
| attributes | Key-value fact map — core payload | entity_memory | required |
| relationships | Typed links to other entity records | entity_memory | required |
| confidence | Float 0.0-1.0 reflecting attribute reliability | entity_memory | required |
| update_policy | Declared semantics for how facts are added or replaced | entity_memory | required |
| expiry | Date after which facts should be re-verified | entity_memory | optional |
| source | Provenance of attributes | entity_memory | optional |
| inject_context | Runtime context block assembled from attributes for LLM prompt | P10 runtime | consumer |
| entity_index | Registry of all entity slugs for dedup and traversal | P10 runtime | external |
| ner_extractor | NLP pipeline that identifies entity mentions and extracts attributes | P02 | producer |
| learning_record | Stores outcomes and lessons — distinct from entity facts | P10 | sibling |
| session_state | Stores ephemeral runtime data — does not persist | P10 | sibling |

## Dependency Graph
```
ner_extractor    --produces--> attributes
source           --produces--> attributes
source           --produces--> confidence
attributes       --depends-->  entity_memory
entity_type      --depends-->  entity_memory
relationships    --depends-->  entity_memory
update_policy    --depends-->  entity_memory
entity_memory    --produces--> inject_context
entity_memory    --produces--> entity_index
expiry           --governs-->  entity_memory
```

## Boundary Table
| entity_memory IS | entity_memory IS NOT |
|-----------------|---------------------|
| Facts about a named entity, stored persistently | Outcomes from a task (that is learning_record) |
| Key-value attribute map with confidence and source | Ephemeral flags or counters (that is session_state) |
| Injected as grounding context into LLM prompts | A reusable execution phase sequence (that is skill) |
| Linked to other entities via typed relationships | A one-shot executable (that is cli_tool) |
| Versioned and expires when facts become stale | An interaction transcript (that is memory_store) |
| Scoped to a single named entity | A general knowledge document (that is knowledge_card) |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| provenance | source, ner_extractor | Supply and validate raw facts |
| identity | entity_id, entity_type, name | Define what entity is described |
| payload | attributes, confidence | Store facts with reliability metadata |
| graph | relationships | Link entity into the knowledge graph |
| governance | update_policy, expiry | Control write semantics and staleness |
| runtime | inject_context, entity_index | Consume entity memory at inference time |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[entity-memory-builder]] | downstream | 0.63 |
| [[bld_collaboration_entity_memory]] | downstream | 0.61 |
| [[p03_sp_entity_memory_builder]] | downstream | 0.58 |
| [[p11_qg_entity_memory]] | downstream | 0.57 |
| [[bld_knowledge_card_entity_memory]] | upstream | 0.51 |
| [[bld_instruction_entity_memory]] | upstream | 0.49 |
| [[bld_schema_entity_memory]] | downstream | 0.47 |
| [[bld_output_template_entity_memory]] | upstream | 0.47 |
| [[p01_kc_entity_memory]] | downstream | 0.47 |
| [[bld_tools_entity_memory]] | upstream | 0.40 |
