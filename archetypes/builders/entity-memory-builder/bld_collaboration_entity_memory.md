---
kind: collaboration
id: bld_collaboration_entity_memory
pillar: P12
llm_function: COLLABORATE
purpose: How entity-memory-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: entity-memory-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the structured facts about this named entity, and how is it linked to other entities in the knowledge graph?"
I do not store learning outcomes. I do not store ephemeral session data. I do not build reusable execution phases.
I produce compact, confidence-scored entity fact records so agents can ground their responses in verified knowledge about named things.
## Crew Compositions
### Crew: "Knowledge Graph Build"
```
  1. entity-memory-builder -> "entity fact records (attributes, relationships, confidence)"
  2. learning-record-builder -> "outcome records from tasks involving those entities"
  3. knowledge-card-builder -> "deep domain knowledge documents that reference entities"
```
### Crew: "Research Pipeline"
```
  1. shaka-satellite (research) -> "raw entity mentions and facts from web research"
  2. entity-memory-builder -> "structured entity_memory artifacts from raw facts"
  3. pytha-satellite (knowledge) -> "indexes entity records into brain for retrieval"
```
### Crew: "Memory System"
```
  1. entity-memory-builder -> "persistent entity facts (people, tools, concepts)"
  2. session-state-builder -> "ephemeral runtime context for active session"
  3. learning-record-builder -> "outcome-based patterns from completed tasks"
```
## Handoff Protocol
### I Receive
- seeds: entity name, entity type, raw facts or source URLs
- optional: relationship hints (known links to other entities), confidence signals
- optional: existing entity slug if updating an existing record
### I Produce
- entity_memory artifact (.md with YAML frontmatter)
- committed to: `cex/P10_memory/examples/p10_entity_{name}.md`
- entity slug registered in: `cex/P10_memory/ENTITY_INDEX.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons (most common: too few attributes, missing update_policy)
## Builders I Depend On
| Builder | Why |
|---------|-----|
| knowledge-card-builder | Knowledge cards provide domain context that surfaces attribute candidates |
| system-prompt-builder | System prompts declare which entities to pre-load in agent context |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| learning-record-builder | Learning records reference entities by slug in their domain field |
| session-state-builder | Session state may reference entity slugs for active entity tracking |
| instruction-builder | Instructions may reference entity attributes as grounding for steps |
| system-prompt-builder | System prompts inject entity_memory records as context blocks |
## Conflict Resolution with Sibling Builders
| Scenario | Resolution |
|----------|-----------|
| Fact belongs in entity_memory vs learning_record | Entity_memory: observable attribute (version, endpoint, owner). Learning_record: outcome of using the entity (success rate, failure pattern). |
| Fact belongs in entity_memory vs session_state | Entity_memory: persists across sessions, version-controlled. Session_state: resets each session, never committed. |
| Fact belongs in entity_memory vs knowledge_card | Entity_memory: structured map for a single named entity. Knowledge_card: prose domain knowledge covering a topic area. |
