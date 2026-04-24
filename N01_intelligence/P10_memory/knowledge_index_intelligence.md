---
id: p10_bi_intelligence_outputs
kind: knowledge_index
8f: F3_inject
pillar: P10
title: "Knowledge Index — N01 Intelligence Outputs"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n01_intelligence
agent_group: n01-research-analyst
domain: research-intelligence
algorithm: hybrid
quality: 9.0
tags: [knowledge-index, search, intelligence, n01, retrieval, hybrid]
tldr: "Hybrid BM25+FAISS index over N01's 41 artifacts — enables semantic and keyword search across research outputs, schemas, and knowledge cards."
density_score: 0.92
related:
  - bld_knowledge_card_knowledge_index
  - bld_examples_knowledge_index
  - p03_sp_knowledge_index_builder
  - bld_instruction_knowledge_index
  - p01_kc_knowledge_index
  - p04_plug_brain_search
  - p10_bi_organization_brain
  - p10_lr_knowledge-index-builder
  - knowledge-index-builder
  - p01_rs_brain_faiss_index
---

## Algorithm

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Algorithm** | Hybrid (BM25 + FAISS) | BM25 catches exact terms (competitor names, metric labels); FAISS catches semantic similarity (related concepts, paraphrased queries). Neither alone covers N01's mixed content. |
| **BM25 weight** | 0.4 | Research artifacts contain precise terms that BM25 matches well |
| **FAISS weight** | 0.6 | Semantic search is primary — most queries are conceptual, not exact |
| **k (results)** | 5 | Optimal for research context injection — more dilutes relevance |
| **Similarity threshold** | 0.65 | Below this, results are noise. Tuned on N01's 41-artifact corpus. |
| **Embedding model** | text-embedding-004 (768d) | Matches `embedding_config_intelligence.md` specification |

### Alternative Considered: Pure BM25

BM25-only would be faster (~3ms vs ~15ms per query) but misses semantic matches. Testing on 20 sample queries showed BM25-only retrieves relevant results 68% of the time vs hybrid at 89%. The 12ms latency cost is negligible for research workflows that take minutes.

### Alternative Considered: Pure FAISS

FAISS-only misses exact-match needs (e.g., searching for "text-embedding-004" or "firecrawl" returns conceptually related but wrong artifacts). Precision drops from 89% to 74% on exact-term queries.

## Scope

### Include Paths
- `N01_intelligence/P05_output/*.md` — 15 research deliverables (primary search corpus)
- `N01_intelligence/P01_knowledge/*.md` — 6 knowledge cards (domain reference)
- `N01_intelligence/P06_schema/*.md` — 6 schema contracts (methodology reference)
- `N01_intelligence/P02_model/*.md` — 1 agent definition
- `N01_intelligence/P03_prompt/*.md` — 2 prompt artifacts
- `N01_intelligence/quality/*.md` — 3 quality artifacts
- `N01_intelligence/P10_memory/*.md` — memory artifacts (self-referential for meta-queries)

### Exclude Paths
- `N01_intelligence/compiled/*.yaml` — compiled versions are derivative, not source
- `N01_intelligence/P11_feedback/` — transient quality gate logs
- `N01_intelligence/P04_tools/` — tool configs are not searchable content

### File Types
- `.md` only — YAML compiled versions excluded to avoid duplicate indexing

## Ranking

| Factor | Weight | Description |
|--------|--------|-------------|
| **Semantic similarity** | 0.6 | Cosine similarity from FAISS |
| **Keyword match (BM25)** | 0.4 | TF-IDF keyword relevance |
| **Recency boost** | 1.1x | Artifacts updated in last 30 days get 10% boost |
| **Output boost** | 1.15x | `output/` artifacts boosted — most queried subdir |
| **Tie-breaking** | By `updated` date | Newer artifact wins ties |

## Filters

| Dimension | Allowed Values | Purpose |
|-----------|---------------|---------|
| `kind` | knowledge_card, context_doc, embedding_config, rag_source, scoring_rubric, agent, benchmark, learning_record | Filter by artifact type |
| `pillar` | P01, P02, P04, P07, P10 | Filter by pillar domain |
| `subdir` | output, knowledge, schemas, agents, prompts, quality, memory | Filter by artifact location |
| `freshness` | current (<90d), recent (<180d), stale (>180d) | Filter by data age |

## Rebuild Schedule

| Trigger | Condition | Est. Duration |
|---------|-----------|---------------|
| **Time-based** | Every 24h at 03:00 UTC | ~45 seconds for 41 artifacts |
| **Event-based** | On any `git commit` touching `N01_intelligence/` | ~45 seconds |
| **Manual** | `python _tools/cex_kc_index.py --rebuild --scope N01` | ~45 seconds |
| **Max staleness** | 48h — after this, index is unreliable | Forced rebuild |

## Health Check

1. Verify artifact count matches filesystem: `find N01_intelligence -name "*.md" | wc -l` should equal index document count
2. Run 3 known-good queries and verify expected results appear in top-3:
   - "competitive analysis framework" → should return `competitive_analysis_contract.md`
   - "market size pet brasil" → should return `p01_kc_fontes_dados_pesquisa_mercado_pet_brasil.md`
   - "research quality scoring" → should return `scoring_rubric_intelligence.md`
3. Check index file timestamp is within `max_staleness` (48h)
4. Verify embedding dimensions match config: 768 (text-embedding-004)

```bash
python _tools/cex_kc_index.py --health-check --scope N01
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_knowledge_index]] | upstream | 0.41 |
| [[bld_examples_knowledge_index]] | upstream | 0.34 |
| [[p03_sp_knowledge_index_builder]] | upstream | 0.31 |
| [[bld_instruction_knowledge_index]] | upstream | 0.30 |
| [[p01_kc_knowledge_index]] | related | 0.29 |
| [[p04_plug_brain_search]] | upstream | 0.29 |
| [[p10_bi_organization_brain]] | sibling | 0.29 |
| [[p10_lr_knowledge-index-builder]] | related | 0.28 |
| [[knowledge-index-builder]] | related | 0.28 |
| [[p01_rs_brain_faiss_index]] | related | 0.27 |
