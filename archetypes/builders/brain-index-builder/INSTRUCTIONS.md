---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for brain_index
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a brain_index

## Phase 1: RESEARCH
1. Identify the corpus: what content needs to be indexed
2. Find existing brain_indexes for the same scope (search P10_memory/examples/)
3. Determine the search pattern: keyword, semantic, or hybrid
4. Assess corpus size and update frequency requirements
5. Check brain_query [IF MCP] for duplicate indexes

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all 17 required + 4 recommended fields (quality: null)
4. Set algorithm to the primary search method
5. Define BM25 parameters: k1, b, and tokenizer settings
6. Define FAISS parameters: index type, nprobe, metric
7. Define hybrid weights: BM25 vs FAISS contribution
8. Define scope: what content is included in the index
9. Define filters: pre-search and post-search filters
10. Define ranking: scoring formula and boost factors
11. Define rebuild_schedule: when index is refreshed
12. Define freshness_policy: max staleness tolerance

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, algorithm valid
3. SOFT: BM25 params present, scope defined, rebuild_schedule set
4. Verify: algorithm matches the content type (text=BM25, vector=FAISS)
5. If score < 8.0: revise before outputting
