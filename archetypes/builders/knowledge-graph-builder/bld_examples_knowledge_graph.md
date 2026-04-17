---
kind: examples
id: bld_examples_knowledge_graph
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of knowledge_graph artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.2
title: "Examples: knowledge_graph"
version: "1.0.0"
author: n03_builder
tags: [knowledge_graph, builder, examples, P01]
tldr: "Golden and anti-examples for knowledge_graph construction demonstrating ideal entity/relation schema and common pitfalls."
domain: "knowledge graph construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.91
---

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
