---
kind: knowledge_card
id: bld_knowledge_card_entity_memory
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for entity_memory production — entity memory specification
sources: LangChain EntityMemory, Zep entity graphs, Mem0 graph memory, cognitive science entity models
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
- **LangChain EntityMemory**: extracts entity mentions from conversation via NER, stores as key-value pairs in a dict, injects as "known facts" prefix in next prompt. Conflict = last-write-wins by default.
- **Zep entity graphs**: server-side entity extraction, stores entities as nodes with typed edges (relationships), temporal tracking via created/updated timestamps, supports graph traversal queries.
- **Mem0 graph memory**: knowledge graph approach with entity + relationship + attribute triples. Deduplication via embedding similarity. Supports merge operations for conflicting facts.
- **Cognitive science model**: entities have identity (name, type), attributes (properties), and relationships (links). Activation spreads from queried entity to related nodes — hence relationship mapping matters for retrieval.
| Pattern | Example | When to use |
|---------|---------|-------------|
| Flat attributes | `{role: "LLM", provider: "Anthropic"}` | Simple tool/service facts |
| Typed attributes | `{release_date: "2024-03-01", api_version: "v1"}` | Versioned entities |
| Relationship graph | `uses -> firecrawl, owns -> codexa-core` | Complex inter-entity models |
| Versioned facts | `{v1: {...}, v2: {...}}` | Entities with breaking changes |
- **Entity extraction via NER**: tools like spaCy, Stanza identify entity spans in text and classify them (PERSON, ORG, PRODUCT). Output feeds attribute population.
- **Conflict resolution strategies**: last-write-wins (overwrite), confidence-weighted merge (keep higher-confidence fact), versioned history (append all versions with timestamp).
- **Staleness handling**: set expiry on volatile entities; check last_referenced date; purge or flag entities not referenced in > N days.
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Unbounded entity growth | Memory bloat; inject cost exceeds grounding benefit |
| No confidence scoring | Cannot distinguish verified fact from rumor |
| Stale facts without expiry | Tool version "1.0" injected when v3.0 is current |
| Storing inferences as facts | `best_tool: true` — opinion, not fact |
| No relationship links | Isolated entity nodes miss graph traversal value |
| Mixing entity_memory with learning_record | Outcome data corrupts factual attribute map |
| PII in version-controlled artifacts | Security / privacy violation |
## Application
1. Name the entity: unique slug, human-readable name, entity_type
2. Extract attributes: gather >= 3 specific facts from primary sources
3. Score confidence: assign float based on source quality (verified=0.9+, inferred=0.5-0.69)
4. Map relationships: identify 1+ links to other entities with typed relation verbs
5. Set update_policy: match to entity volatility (volatile API -> overwrite; stable concept -> append)
6. Set expiry: null for stable concepts, date for versioned tools/services
7. Validate: id pattern, attributes non-empty, entity_type in enum, quality null
## References
- LangChain EntityMemory: `langchain.memory.entity`
- Zep: zep.dev entity graph documentation
- Mem0: mem0.ai graph memory architecture
- Cognitive science: spreading activation model (Collins & Loftus, 1975)
