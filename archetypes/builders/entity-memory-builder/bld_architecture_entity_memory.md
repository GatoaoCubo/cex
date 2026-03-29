---
kind: architecture
id: bld_architecture_entity_memory
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of entity_memory — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| entity_id | Unique identifier for the entity record | entity_memory | required |
| entity_type | Classification of entity (person/tool/concept/org/project/service) | entity_memory | required |
| attributes | Key-value fact map — the core payload of the memory record | entity_memory | required |
| relationships | Typed links to other entity records | entity_memory | required |
| confidence | Float 0.0-1.0 reflecting reliability of the attribute set | entity_memory | required |
| update_policy | Declared semantics for how facts are added or replaced | entity_memory | required |
| expiry | Date after which facts should be re-verified or discarded | entity_memory | optional |
| source | Provenance — where attributes originated | entity_memory | optional |
| inject_context | Runtime context block assembled from attributes for LLM prompt | P10 runtime | consumer |
| entity_index | Registry of all known entity slugs for dedup and traversal | P10 runtime | external |
| ner_extractor | NLP pipeline that identifies entity mentions and extracts attributes | P02 | producer |
| learning_record | Stores outcomes and lessons — distinct from entity facts | P10 | sibling |
| session_state | Stores ephemeral runtime data — does not persist across sessions | P10 | sibling |
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
| From | To | Type | Data |
|------|----|------|------|
| ner_extractor | attributes | produces | extracted entity spans as key-value pairs |
| source | attributes | produces | primary-source facts populating the map |
| source | confidence | produces | source quality determines confidence float |
| attributes | entity_memory | depends | core payload — record is empty without facts |
| entity_type | entity_memory | depends | classification required for routing and filtering |
| relationships | entity_memory | depends | graph links enable traversal and context enrichment |
| update_policy | entity_memory | depends | update semantics required for write operations |
| entity_memory | inject_context | produces | assembled fact block injected into LLM prompt |
| entity_memory | entity_index | produces | slug registered in global entity registry |
| expiry | entity_memory | governs | staleness check gates re-injection |
## Boundary Table
| entity_memory IS | entity_memory IS NOT |
|-----------------|---------------------|
| Facts about a named entity, stored persistently | Outcomes from a task or experiment (that is learning_record) |
| Key-value attribute map with confidence and source | Ephemeral runtime flags or counters (that is session_state) |
| Injected as grounding context into LLM prompts | A reusable execution phase sequence (that is skill) |
| Linked to other entities via typed relationships | A one-shot executable with exit codes (that is cli_tool) |
| Versioned and expires when facts become stale | An interaction transcript or dialogue history (that is memory_store) |
| Scoped to a single named entity | A general knowledge document (that is knowledge_card) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| provenance | source, ner_extractor | Supply and validate raw facts before storage |
| identity | entity_id, entity_type, name | Define what entity this record describes |
| payload | attributes, confidence | Store facts with reliability metadata |
| graph | relationships | Link entity into the knowledge graph |
| governance | update_policy, expiry | Control write semantics and staleness |
| runtime | inject_context, entity_index | Consume entity memory at inference time |
