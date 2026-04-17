---
kind: instruction
id: bld_instruction_knowledge_graph
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for knowledge_graph
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction: knowledge_graph"
version: "1.0.0"
author: n03_builder
tags: [knowledge_graph, builder, instruction, P01]
tldr: "3-phase process: research domain entities/relations, compose schema with 6 required sections, validate gates and byte budget."
domain: "knowledge graph construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Instructions: How to Produce a knowledge_graph

## Phase 1: RESEARCH

1. Identify the domain: what subject area does this knowledge graph cover?
   Examples: biomedical, financial, legal, software architecture, competitive intelligence.
2. Enumerate entity types needed for this domain -- aim for 3-10 types.
   Start with nouns: Organization, Person, Product, Technology, Concept, Event, Location.
   Constrain aggressively -- each added type increases extraction noise.
3. Enumerate relation types needed -- aim for 5-15 types.
   Start with verbs: acquired, employs, uses, competes_with, developed_by, located_in.
   For each relation, identify: source_type, target_type, directionality (directed/undirected).
4. Determine extraction strategy: LLM prompt for triplet extraction? Named entity recognition?
   Schema-constrained extraction (give the LLM a whitelist)? Pattern matching?
5. Select storage backend based on scale and query patterns:
   - in_memory: prototyping, < 10k nodes, no persistence needed
   - json: simple persistence, < 50k nodes, no complex traversal
   - falkordb: production, in-memory Cypher, high performance, Redis-compatible
   - neo4j: production, full ACID, complex Cypher queries, large graphs
6. Determine traversal strategy:
   - local: entity-centric retrieval (answer "what do I know about entity X?")
   - global: community-based retrieval (answer "what are the main themes in this corpus?")
   - hybrid: combine both (most versatile, recommended default)
7. Define deduplication strategy:
   - exact: string equality only (fast, misses "OpenAI" vs "Open AI")
   - fuzzy: edit distance / embedding similarity (good default)
   - llm: LLM resolves ambiguous cases (most accurate, higher cost)
8. Check existing knowledge_graph artifacts via cex_retriever for the same domain --
   avoid duplicating a schema that already covers this domain.

## Phase 2: COMPOSE

1. Read bld_schema_knowledge_graph.md -- source of truth for all fields.
2. Read bld_output_template_knowledge_graph.md -- fill the template following schema constraints.
3. Fill all required frontmatter fields; set quality: null -- never self-score.
4. Write **Overview** section: what domain, why graph (not flat vector), what questions it answers.
5. Write **Entity Types** section: table with columns name, description, extraction_hint, examples.
   - Extraction hint: phrase or pattern that signals this entity type in text.
   - Examples: 2-3 instance values to clarify the type boundary.
6. Write **Relation Types** section: table with columns name, source_type, target_type, description, directionality.
   - directionality: directed (A -> B) or undirected (A -- B).
   - Every relation must reference only entity types defined in the Entity Types section.
7. Write **Extraction Config** section:
   - Extraction prompt template or reference to a prompt_template artifact.
   - Output format: JSON triplets {subject, predicate, object} or structured YAML.
   - LLM model and temperature recommendation for extraction.
8. Write **Storage and Traversal** section:
   - Storage backend with rationale (why this backend for this scale/use case).
   - Traversal strategy with max_depth and pruning rules.
   - Query patterns supported (Cypher, Gremlin, SPARQL, or Python API).
9. Write **Integration** section:
   - Embedding model reference (or link to embedding_config artifact).
   - Dedup strategy with threshold configuration.
   - Community detection algorithm and granularity.
   - Downstream consumers: which agents or pipelines use this graph.
10. Confirm body <= 8192 bytes.

## Phase 3: VALIDATE

1. Check bld_quality_gate_knowledge_graph.md -- verify each HARD gate manually.
2. Confirm YAML frontmatter parses without errors.
3. Confirm id matches `^p01_kg_[a-z][a-z0-9_]+$`.
4. Confirm entity_types list is non-empty and matches the Entity Types table names exactly.
5. Confirm relation_types list is non-empty and matches the Relation Types table names exactly.
6. Confirm each relation type references only entity types defined in entity_types list.
7. Confirm storage_backend is one of: neo4j, falkordb, in_memory, json.
8. Confirm traversal_strategy is one of: local, global, hybrid.
9. Confirm quality is null.
10. Confirm body <= 8192 bytes.
11. Cross-check: is this a schema definition? If this contains actual entity instances (data),
    move instances to entity_memory (P10). If this is a vector index config, it belongs in
    knowledge_index (P10). If this is an external source pointer, it belongs in rag_source (P01).
12. If score < 8.0: revise in the same pass before outputting.
