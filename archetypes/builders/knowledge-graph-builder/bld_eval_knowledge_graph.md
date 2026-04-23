---
kind: quality_gate
id: p11_qg_knowledge_graph
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of knowledge_graph artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.1
title: "Gate: knowledge_graph"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, knowledge-graph, GraphRAG, entities, relations, P11]
tldr: "Gates for knowledge_graph artifacts: validates entity/relation lists, relation source/target consistency, storage and traversal enums, extraction config, and section completeness."
domain: "knowledge_graph -- graph-based knowledge schemas with entity types, relation types, extraction logic, storage backend, and traversal strategies"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
related:
  - bld_instruction_knowledge_graph
  - knowledge-graph-builder
  - p03_sp_knowledge_graph_builder
  - bld_schema_knowledge_graph
  - bld_config_knowledge_graph
  - p01_kc_knowledge_graph
  - bld_examples_knowledge_graph
  - bld_knowledge_card_knowledge_graph
  - p10_lr_knowledge_graph_builder
  - bld_output_template_knowledge_graph
---

## Quality Gate

# Gate: knowledge_graph

## Definition

| Field | Value |
|-------|-------|
| metric | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator | AND (all HARD) + weighted_sum (SOFT) |
| scope | All artifacts where `kind: knowledge_graph` |

## HARD Gates

All must pass. Any single failure = REJECT regardless of SOFT score.

| ID | Check | Failure message |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p01_kg_[a-z][a-z0-9_]+$` | "ID fails knowledge_graph namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"knowledge_graph"` | "Kind is not 'knowledge_graph'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, domain, entity_types, relation_types, storage_backend, traversal_strategy, version, created, author, tags, tldr | "Missing required field(s)" |
| H07 | `entity_types` list is non-empty (>= 1 type defined) | "entity_types list is empty -- graph has no nodes" |
| H08 | `relation_types` list is non-empty (>= 1 type defined) | "relation_types list is empty -- graph has no edges" |
| H09 | Each relation type in Relation Types table references only entity types from the entity_types list | "Relation references undefined entity type" |
| H10 | `storage_backend` is one of: neo4j, falkordb, in_memory, json | "Invalid storage_backend value" |
| H11 | `traversal_strategy` is one of: local, global, hybrid | "Invalid traversal_strategy value" |
| H12 | Body contains all 6 required sections: Overview, Entity Types, Relation Types, Extraction Config, Storage and Traversal, Integration | "Missing required body section(s)" |

## SOFT Scoring

Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.

| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Entity type specificity | 1.0 | Extraction hints and example instances provided per entity type |
| Relation type completeness | 1.0 | Source type, target type, directionality documented per relation |
| Extraction config quality | 1.5 | Extraction prompt template included; LLM and output format specified |
| Storage backend rationale | 0.5 | Storage choice justified against scale and query pattern requirements |
| Traversal strategy rationale | 0.5 | Strategy (local/global/hybrid) justified against use-case query types |
| Deduplication specification | 1.0 | Dedup strategy and threshold defined; entity resolution approach clear |
| Embedding integration | 1.0 | embedding_integration boolean set; model reference or artifact link included |
| Community detection | 0.5 | Algorithm and granularity specified when global traversal is used |
| Domain coverage | 1.0 | Entity and relation types comprehensively cover the declared domain |
| Boundary clarity | 1.0 | Explicitly not entity_memory (P10), knowledge_index (P10), rag_source (P01) |
| Downstream integration | 1.0 | Downstream consumers and integration points documented |
| tldr density | 0.5 | tldr names domain, entity count, relation count, storage backend |

Weight sum: 1.0+1.0+1.5+0.5+0.5+1.0+1.0+0.5+1.0+1.0+1.0+0.5 = 10.0 (100%)

## Actions

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0 | REJECT | Return to author with failure report |

## Bypass

| Field | Value |
|-------|-------|
| conditions | Early-stage domain exploration where entity types are not yet finalized |
| approver | Domain expert or N03 builder approval required (written); H07/H08 (empty lists) never bypassed |

## Examples

# Examples: knowledge-graph-builder

## Golden Example

INPUT: "Create a knowledge graph schema for competitive intelligence -- companies, products, and market relationships"

OUTPUT:
```yaml
id: p01_kg_competitive_intel
kind: knowledge_graph
pillar: P01
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "builder_agent"
domain: "competitive intelligence"
entity_types:
  - Organization
  - Product
  - Technology
  - Market
  - Person
relation_types:
  - acquired
  - competes_with
  - developed_by
  - operates_in
  - employs
  - uses_technology
quality: null
tags: [knowledge_graph, competitive-intelligence, graphrag, P01]
tldr: "Competitive intel graph: 5 entity types, 6 relation types, hybrid traversal, neo4j, leiden community detection"
description: "Knowledge graph schema for competitive intelligence covering companies, products, technologies, and market relationships"
max_depth: 3
embedding_integration: true
dedup_strategy: fuzzy
community_detection: leiden
extraction_prompt: "LLM schema-constrained triplet extraction with entity type whitelist"
```

## Overview
Covers competitive intelligence for technology markets -- organizations, their products,
the technologies they use, and the markets they compete in.
Graph enables multi-hop queries like "which companies use technology X and compete in market Y?"
Answers: competitor mapping, technology adoption patterns, M&A activity tracking.

## Entity Types

| Name | Description | Extraction Hint | Examples |
|------|-------------|----------------|----------|
| Organization | Company, startup, or institution | "Inc.", "Corp.", "Ltd.", capital name | OpenAI, Google, Anthropic |
| Product | Named product or service offering | product name, "platform", "API", "model" | GPT-4, Gemini, Claude |
| Technology | Technical capability or framework | tech noun, "framework", "model type" | Transformer, RLHF, RAG |
| Market | Industry vertical or use-case segment | "market", "sector", "vertical", "space" | Enterprise AI, EdTech, FinTech |
| Person | Named individual, founder, executive | person name + title context | Sam Altman, Demis Hassabis |

## Relation Types

| Name | Source Type | Target Type | Description | Directionality |
|------|-------------|-------------|-------------|----------------|
| acquired | Organization | Organization | Acquisition or merger event | directed |
| competes_with | Organization | Organization | Direct market competition | undirected |
| developed_by | Product | Organization | Who built the product | directed |
| operates_in | Organization | Market | Which market a company serves | directed |
| employs | Organization | Person | Employment relationship | directed |
| uses_technology | Product | Technology | Technical capability in a product | directed |

## Extraction Config

| Parameter | Value |
|-----------|-------|
| Method | schema_constrained LLM triplet extraction |
| LLM model | gpt-4o or claude-3-5-sonnet |
| Temperature | 0.0 |
| Output format | JSON list of {subject, predicate, object} |
| Extraction prompt | schema-constrained with entity type whitelist |

## Storage and Traversal

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Storage backend | neo4j | Production-grade, complex Cypher queries for multi-hop |
| Traversal strategy | hybrid | Local for company profiles, global for market trend summaries |
| Max depth | 3 | Balances context richness vs query latency |
| Query language | cypher | Native neo4j, expressive for graph patterns |
| Pruning rule | relevance_score >= 0.6 | Prune low-relevance edges during retrieval |

## Integration

| Component | Value |
|-----------|-------|
| Embedding model | text-embedding-3-small |
| Dedup strategy | fuzzy |
| Dedup threshold | 0.85 |
| Community detection | leiden |
| Community granularity | medium |
| Downstream consumers | competitive-intel-agent, market-research-pipeline |

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches ^p01_kg_[a-z][a-z0-9_]+ pattern (H02 pass)
- kind: knowledge_graph (H04 pass)
- entity_types and relation_types non-empty (H07, H08 pass)
- all relation types reference entity types in entity_types list (H09 pass)
- storage_backend valid enum value (H10 pass)
- traversal_strategy valid enum value (H10 pass)
- all 6 required body sections present (H06 pass)
- tldr: 83 chars <= 160 (S01 pass)
- tags: 4 items, includes "knowledge_graph" (S02 pass)
- embedding_integration and dedup_strategy documented (S03, S04 pass)

---

## Anti-Example

INPUT: "Create knowledge graph for my company data"

BAD OUTPUT:
```yaml
id: company-knowledge-graph
kind: graph
pillar: knowledge
domain: company
entities: [Company, Employee, Project]
quality: 8.5
tags: [graph]
```

Company has employees and projects.
Store in database.

FAILURES:
1. id: "company-knowledge-graph" uses hyphens, no p01_kg_ prefix -> H02 FAIL
2. kind: "graph" not "knowledge_graph" -> H04 FAIL
3. pillar: "knowledge" not "P01" -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. entity_types field missing (uses "entities" instead) -> H07 FAIL
6. relation_types field completely missing -> H08 FAIL
7. storage_backend field missing -> H10 FAIL
8. traversal_strategy field missing -> H10 FAIL
9. tags: only 1 item, missing "knowledge_graph" -> S02 FAIL
10. body missing all 6 required sections (Overview, Entity Types, Relation Types, Extraction Config, Storage and Traversal, Integration) -> H06 FAIL
11. No extraction prompt defined -- graph cannot be populated -> S05 FAIL
12. No dedup strategy -- same entity will appear as multiple nodes -> S04 FAIL
13. version, created, updated, author, tldr missing -> H06 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
