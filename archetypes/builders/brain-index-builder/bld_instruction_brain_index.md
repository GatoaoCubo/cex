---
kind: instruction
id: bld_instruction_brain_index
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for brain_index
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a brain_index
## Phase 1: RESEARCH
1. Identify the content scope (corpus): which files, directories, or artifact types this index covers
2. Determine the search algorithm: BM25 (keyword-based), FAISS (vector similarity), or hybrid (both combined with weighted scores)
3. Assess freshness requirements: how often does the corpus change, what staleness is acceptable
4. Map the ranking strategy: scoring formula, boost factors for recency or authority, tie-breaking rule
5. Identify filter dimensions: metadata fields (pillar, kind, agent_node, tag) that users filter by, and their allowed values
6. Check for existing brain_index artifacts with overlapping scope to avoid redundant indexes
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
3. HARD gate: kind == brain_index
4. HARD gate: quality == null
5. HARD gate: algorithm is specified (not blank)
6. HARD gate: scope contains at least one include path
7. HARD gate: rebuild schedule is defined
8. Cross-check: does this index scope overlap with any existing brain_index? Overlapping scopes cause inconsistent search results
9. Cross-check: is this a brain_index (search configuration) and not an embedding_config (embedding model settings) or rag_source (retrieval source definition)?
10. If score < 8.0: revise before outputting
