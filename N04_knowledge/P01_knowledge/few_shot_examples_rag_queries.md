---
id: few_shot_examples_rag_queries
kind: knowledge_card
pillar: P01
nucleus: n04
title: "Knowledge Card -- RAG Query Few-Shot Examples (N04)"
version: 1.0.0
quality: null
tags: [knowledge_card, few_shot_examples, rag, retrieval, query, n04, P01]
domain: knowledge management
type: few_shot_examples
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "5 complete RAG query traces from N04: semantic search, cross-nucleus query, intent->kind lookup, few-shot retrieval, quality-filtered query. Each trace shows input, L0/L1/L2 transmutation, retrieval path, fusion, and output schema."
density_score: 0.92
sources:
  - N04_knowledge/P04_tools/retriever_n04.md
  - N04_knowledge/P06_schema/input_schema_knowledge_query.md
  - N04_knowledge/P01_knowledge/kc_knowledge_vocabulary.md
---

# Knowledge Card: RAG Query Few-Shot Examples

## How to Read These Examples

Each example follows the N04 query trace format:
1. **Input** -- raw user query (natural language)
2. **Transmutation** -- L0/L1/L2 intent resolution chain
3. **Retrieval path** -- hybrid_retrieval configuration applied
4. **Fusion** -- RRF score merging
5. **Output** -- result schema returned to caller

Retriever config: hybrid (dense pgvector + sparse BM25), RRF(k=60), top_k=10, reranker=cross-encoder.

---

## Example 1: Semantic Search -- "find all quality_gate artifacts"

**Input:** `find all quality_gate artifacts`

**L0 transmutation (cex_intent_resolver.py, 0 tokens):**
```
intent_type: artifact_lookup
kind: quality_gate
pillar: P07
nucleus: any
verb: find
```

**L1 mapping (p03_pc_cex_universal.md):**
```
pattern_match: "find all {kind} artifacts" -> retrieval mode: metadata filter
kind_canonical: quality_gate
pillar_canonical: P07
query_rewrite: "quality_gate artifact P07 evaluation"
```

**Retrieval path:**
```
Step 1: Metadata filter (free, no embedding needed)
  filter: frontmatter.kind == "quality_gate"
  backend: N04_knowledge/P07_evals/ glob + cex_retriever.py --kind quality_gate

Step 2: Dense retrieval (embedding fallback if metadata fails)
  query_vector: embed("quality gate validation scoring rubric")
  backend: pgvector, metric=cosine, top_k=20

Step 3: RRF fusion
  metadata_results: rank 1-N (exact kind match, score 1.0)
  dense_results: rank 1-20
  fused: RRF(k=60) -> top 10
```

**Output schema:**
```json
{
  "query": "find all quality_gate artifacts",
  "kind_filter": "quality_gate",
  "results": [
    {"path": "N03_engineering/P07_evals/quality_gate_n03.md", "score": 0.98},
    {"path": "N05_operations/P07_evals/quality_gate_n05.md", "score": 0.97}
  ],
  "total": 6,
  "mode": "metadata_filter"
}
```

**Key insight:** kind-exact queries use metadata filter first (free, instant). Dense retrieval is fallback only.

---

## Example 2: Cross-Nucleus Query -- "which nuclei cover P06 schema?"

**Input:** `which nuclei cover P06 schema?`

**L0 transmutation:**
```
intent_type: coverage_query
pillar: P06
nucleus: any
verb: audit
```

**L1 mapping:**
```
pattern_match: "which nuclei cover {pillar}" -> cross_nucleus scan
query_rewrite: "P06 schema validation input_schema type_def nucleus"
```

**Retrieval path:**
```
Step 1: Directory scan (0 tokens)
  scan: glob("N0[1-6]_*/P06_schema/*.md")
  group_by: nucleus

Step 2: Structured aggregation
  for each nucleus found:
    count: files in N0X/P06_schema/
    list: kind[] from frontmatter
    
Step 3: Dense retrieval for gap detection
  query: "schema validation contract type definition"
  filter: NOT in directory_scan results
  purpose: find schema artifacts stored in non-standard paths
```

**Fusion (cross-nucleus context):**
```
nucleus_coverage = {
  "N03": 8 artifacts,  # Engineering owns P06 primary
  "N04": 12 artifacts, # Knowledge stores data contracts
  "N05": 4 artifacts,  # Operations has config schemas
  "N01": 2 artifacts,  # Intelligence has eval schemas
  "N02": 1 artifact,   # Marketing has form schemas
  "N06": 3 artifacts   # Commercial has pricing schemas
}
```

**Output schema:**
```json
{
  "pillar": "P06",
  "coverage_by_nucleus": {
    "N03": {"count": 8, "primary": true},
    "N04": {"count": 12, "primary": false},
    "N05": {"count": 4},
    "N01": {"count": 2},
    "N02": {"count": 1},
    "N06": {"count": 3}
  },
  "total_artifacts": 30,
  "primary_nucleus": "N03"
}
```

**Key insight:** pillar-coverage queries use directory scan (free). Dense retrieval adds coverage gap detection.

---

## Example 3: Intent Resolution -> Kind Lookup -- "what kind handles pricing?"

**Input:** `what kind handles pricing?`

**L0 transmutation:**
```
intent_type: kind_lookup
domain: pricing
nucleus: N06
verb: discover
```

**L1 mapping (p03_pc_cex_universal.md, bilingual table):**
```
EN pattern: "pricing strategy" -> kind: content_monetization, pillar: P11, nucleus: N06
EN pattern: "pricing tiers" -> kind: subscription_tier, pillar: P09, nucleus: N06
EN pattern: "pricing page" -> kind: pricing_page, pillar: P05, nucleus: N06
confidence: 0.87 (multiple kinds match)
```

**Retrieval path (multi-kind confidence case):**
```
Step 1: Exact match from L1 table (0 tokens)
  candidates: [content_monetization, subscription_tier, pricing_page]
  
Step 2: Dense retrieval for disambiguation
  query_1: "pricing strategy revenue tiers SaaS"
  query_2: "pricing page landing page CTA conversion"
  query_3: "subscription tier feature gating monthly annual"
  
Step 3: GDP check (confidence < 0.90)
  action: present 3 candidates to user with descriptions
  fallback: if autonomous mode -> return all 3, primary = content_monetization
```

**Output schema:**
```json
{
  "query": "what kind handles pricing?",
  "intent": "kind_discovery",
  "candidates": [
    {
      "kind": "content_monetization",
      "pillar": "P11",
      "nucleus": "N06",
      "description": "Full pricing strategy: tiers, gates, revenue model",
      "confidence": 0.87,
      "primary": true
    },
    {
      "kind": "subscription_tier",
      "pillar": "P09",
      "nucleus": "N06",
      "description": "Single tier definition with features and limits",
      "confidence": 0.79
    },
    {
      "kind": "pricing_page",
      "pillar": "P05",
      "nucleus": "N06",
      "description": "Frontend pricing page artifact",
      "confidence": 0.71
    }
  ],
  "gdp_required": true,
  "mode": "multi_kind_disambiguation"
}
```

**Key insight:** low-confidence (< 0.90) kind resolution requires GDP. Always return candidates ranked by confidence, not just top-1.

---

## Example 4: Few-Shot Retrieval Pattern -- "show me 8F examples"

**Input:** `show me 8F examples`

**L0 transmutation:**
```
intent_type: few_shot_lookup
subject: 8F_pipeline
kind: few_shot_example
pillar: P03
verb: retrieve
```

**L1 mapping:**
```
pattern_match: "show me {concept} examples" -> few_shot_example retrieval
query_rewrite: "8F pipeline reasoning trace example demonstration"
```

**Retrieval path (few-shot pattern):**
```
Step 1: Kind filter (free)
  filter: frontmatter.kind IN ["few_shot_example", "reasoning_trace"]
  
Step 2: Dense retrieval with query variants
  query_1: "8F pipeline F1 constrain F2 become example"
  query_2: "8F reasoning protocol trace research build deploy"
  query_3: "8-function pipeline F6 produce F7 govern F8 collaborate"
  
Step 3: Hybrid fusion (RRF k=60)
  dense_candidates: 20 per query -> 60 total candidates
  sparse_candidates: BM25("8F pipeline example") -> 20 candidates
  fused: RRF -> top 10
  
Step 4: Cross-encoder rerank
  model: cross-encoder/ms-marco-MiniLM-L-6-v2
  rerank: top 10 -> top 5 (final)
```

**Output schema:**
```json
{
  "query": "show me 8F examples",
  "kind": "few_shot_example",
  "results": [
    {"path": ".claude/rules/8f-reasoning.md", "section": "N07 Orchestrator", "score": 0.94},
    {"path": ".claude/rules/8f-reasoning.md", "section": "N01 Intelligence", "score": 0.91},
    {"path": "N03_engineering/P07_evals/reasoning_trace_8f_constrain.md", "score": 0.88},
    {"path": "N03_engineering/P08_architecture/pattern_8f_full_trace.md", "score": 0.86},
    {"path": "N04_knowledge/P01_knowledge/few_shot_examples_rag_queries.md", "score": 0.82}
  ],
  "total": 5,
  "mode": "hybrid_with_rerank"
}
```

**Key insight:** few-shot retrieval uses 3 query variants to maximize recall. Cross-encoder rerank improves precision from P@10=0.71 to P@5=0.94.

---

## Example 5: Quality-Filtered Query -- "find artifacts below 8.0 in N03"

**Input:** `find artifacts below 8.0 in N03`

**L0 transmutation:**
```
intent_type: quality_audit
nucleus: N03
quality_threshold: 8.0
operator: less_than
verb: find
```

**L1 mapping:**
```
pattern_match: "find artifacts {quality_condition} in {nucleus}" -> quality_filter scan
query_rewrite: NULL (metadata-only query, no semantic component)
```

**Retrieval path (metadata-only, no embedding):**
```
Step 1: Structured metadata scan (0 tokens, 0 embeddings)
  source: cex_retriever.py --nucleus n03 --quality-filter "<8.0"
  algorithm:
    1. find N03_engineering/**/*.md (exclude compiled/, README)
    2. parse frontmatter (quality field)
    3. filter: quality < 8.0 OR quality == null
    4. sort: by quality ASC (nulls last)

Step 2: Augment with density_score
  add: density_score < 0.85 as secondary filter
  
Step 3: Generate improvement candidates
  rank_by: quality ASC, then density_score ASC
  limit: 20
```

**Fusion:** none required (metadata-only, deterministic).

**Output schema:**
```json
{
  "query": "find artifacts below 8.0 in N03",
  "nucleus": "N03",
  "quality_threshold": 8.0,
  "operator": "lt",
  "results": [
    {"path": "N03_engineering/P01_knowledge/kc_draft_example.md", "quality": 7.2, "density_score": 0.78},
    {"path": "N03_engineering/P08_architecture/diagram_n03.md", "quality": 7.8, "density_score": 0.81},
    {"path": "N03_engineering/P06_schema/type_def_draft.md", "quality": null, "density_score": 0.91}
  ],
  "total_below_threshold": 12,
  "total_null": 8,
  "improvement_candidates": 20,
  "mode": "metadata_filter_only",
  "next_step": "cex_evolve.py sweep --nucleus n03 --target 8.5"
}
```

**Key insight:** quality-filter queries are deterministic metadata scans -- 0 tokens, 0 embeddings.
Offer `cex_evolve.py` command in response to close the loop.

---

## Summary: Query Mode Selection

| Query Type | Mode | Cost | Tokens Used |
|------------|------|------|-------------|
| Exact kind lookup | metadata filter | free | 0 |
| Pillar coverage audit | directory scan + aggregation | free | 0 |
| Quality filter | metadata scan | free | 0 |
| Kind disambiguation | L1 table + dense | low | ~200 |
| Semantic/conceptual | hybrid (dense + BM25) + RRF | medium | ~500 |
| Few-shot retrieval | hybrid + 3 queries + rerank | high | ~1000 |

**Default selection rule:** start with metadata filter. Escalate to dense only when metadata is insufficient.

## Anti-Patterns

| Anti-Pattern | Correct Behavior |
|-------------|-----------------|
| Embedding every query regardless of type | Use metadata filter first; reserve embeddings for semantic queries |
| Single-query dense retrieval | Always run 3 query variants for semantic queries (improves recall ~40%) |
| Skipping reranker | Cross-encoder rerank improves P@5 by 15-25% on average |
| Returning kind candidates without confidence | Always attach confidence score; trigger GDP if < 0.90 |
| Ignoring quality:null in quality filter | null artifacts are HIGH priority for improvement; include them |
