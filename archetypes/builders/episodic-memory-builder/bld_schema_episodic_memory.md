---
quality: 8.9
quality: 8.2
kind: schema
id: bld_schema_episodic_memory
pillar: P10
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for episodic_memory
title: "Schema Episodic Memory"
version: "1.0.0"
author: n03_builder
tags: [episodic_memory, builder, schema]
tldr: "Frontmatter + body schema for episodic_memory: episode_schema, retrieval_config, decay_policy, episode_count."
domain: "episodic memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_memory_scope
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_search_strategy
  - bld_schema_golden_test
  - bld_schema_quickstart_guide
  - bld_schema_chunk_strategy
---

# Schema: episodic_memory

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p10_ep_{slug}) | YES | - | Namespace compliance |
| kind | literal "episodic_memory" | YES | - | Type integrity |
| pillar | literal "P10" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| owner | string | YES | - | Agent or nucleus that owns this store |
| episode_schema | map[string, type_string] | YES | - | Fields each episode has |
| retrieval_method | enum: recency, relevance, hybrid | YES | - | How episodes are retrieved |
| episode_count | int | YES | - | Max episodes retained |
| decay_policy | {method, rate} | YES | - | How episodes age and are pruned |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "episodic_memory" |
| tldr | string <= 160ch | YES | - | Dense summary |
| promotion_sources | list[string] | REC | - | working_memory IDs that feed this store |
| retrieval_keys | list[string] | REC | - | Fields used for embedding/keyword index |
| index_method | enum: embedding, keyword, hybrid | REC | - | How retrieval_keys are indexed |
| description | string <= 200ch | REC | - | What agent and purpose this serves |

## ID Pattern
Regex: `^p10_ep_[a-z][a-z0-9_]+$`

## Body Structure
1. `## Overview` -- agent served, purpose, why episodic memory is needed
2. `## Episode Schema` -- field table with types and purpose
3. `## Retrieval Config` -- method, keys, indexing
4. `## Decay Policy` -- aging, pruning, limits
5. `## Example Episodes` -- 1-2 example instances

## Constraints
- max_bytes: 4096
- episode_schema MUST include timestamp field
- episode_count MUST be numeric (not null in production)
- decay_policy MUST be declared
- quality: null always

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.67 |
| [[bld_schema_reranker_config]] | sibling | 0.67 |
| [[bld_schema_usage_report]] | sibling | 0.67 |
| [[bld_schema_memory_scope]] | sibling | 0.66 |
| [[bld_schema_handoff_protocol]] | sibling | 0.65 |
| [[bld_schema_output_validator]] | sibling | 0.65 |
| [[bld_schema_search_strategy]] | sibling | 0.65 |
| [[bld_schema_golden_test]] | sibling | 0.65 |
| [[bld_schema_quickstart_guide]] | sibling | 0.65 |
| [[bld_schema_chunk_strategy]] | sibling | 0.65 |
