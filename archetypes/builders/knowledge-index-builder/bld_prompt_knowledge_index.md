---
kind: instruction
id: bld_instruction_knowledge_index
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for knowledge_index
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Knowledge Index"
version: "1.0.0"
author: n03_builder
tags: [knowledge_index, builder, examples]
tldr: "Golden and anti-examples for knowledge index construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge index construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_golden_test
  - p11_qg_knowledge_index
  - bld_instruction_retriever_config
  - bld_instruction_agent
  - bld_instruction_memory_scope
  - p03_sp_knowledge_index_builder
  - bld_instruction_output_validator
  - bld_instruction_boot_config
  - bld_instruction_chunk_strategy
  - bld_instruction_context_doc
---

# Instructions: How to Produce a knowledge_index
## Phase 1: RESEARCH
1. Identify the content scope (corpus): which files, directories, or artifact types this index covers
2. Determine the search algorithm: BM25 (keyword-based), FAISS (vector similarity), or hybrid (both combined with weighted scores)
3. Assess freshness requirements: how often does the corpus change, what staleness is acceptable
4. Map the ranking strategy: scoring formula, boost factors for recency or authority, tie-breaking rule
5. Identify filter dimensions: metadata fields (pillar, kind, agent_group, tag) that users filter by, and their allowed values
6. Check for existing knowledge_index artifacts with overlapping scope to avoid redundant indexes
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Fill frontmatter: all required fields (quality: null, never self-score)
4. Write Algorithm section: selected algorithm name, key parameters (k, threshold, hybrid weights for BM25 vs FAISS)
5. Write Scope section: include paths, exclude paths, and file type filters that define the corpus boundary
6. Write Ranking section: scoring formula, boost conditions, and tie-breaking rule
7. Write Filters section: each metadata dimension with its allowed values
8. Write Rebuild Schedule section: trigger condition (time-based or event-based), estimated duration, and maximum staleness threshold
9. Write Health Check section: integrity verification steps to confirm index is valid and current
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. HARD gate: id matches `p10_bi_` pattern
3. HARD gate: kind == knowledge_index
4. HARD gate: quality == null
5. HARD gate: algorithm is specified (not blank)
6. HARD gate: scope contains at least one include path
7. HARD gate: rebuild schedule is defined
8. Cross-check: does this index scope overlap with any existing knowledge_index? Overlapping scopes cause inconsistent search results
9. Cross-check: is this a knowledge_index (search configuration) and not an embedding_config (embedding model settings) or rag_source (retrieval source definition)?
10. If score < 8.0: revise before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify knowledge
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | knowledge index construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_golden_test]] | sibling | 0.41 |
| [[p11_qg_knowledge_index]] | downstream | 0.40 |
| [[bld_instruction_retriever_config]] | sibling | 0.39 |
| [[bld_instruction_agent]] | sibling | 0.38 |
| [[bld_instruction_memory_scope]] | sibling | 0.38 |
| [[p03_sp_knowledge_index_builder]] | related | 0.37 |
| [[bld_instruction_output_validator]] | sibling | 0.37 |
| [[bld_instruction_boot_config]] | sibling | 0.36 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.36 |
| [[bld_instruction_context_doc]] | sibling | 0.36 |
