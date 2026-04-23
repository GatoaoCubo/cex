---
id: p07_em_n04_knowledge
kind: eval_metric
pillar: P07
nucleus: n04
title: "Eval Metric -- N04 Retrieval Quality Metrics"
version: "1.0.0"
quality: 9.1
tags: [eval_metric, n04, MRR, NDCG, precision, recall, P07, retrieval]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "Formal metric definitions for N04 retrieval quality evaluation: MRR@K, NDCG@K, Precision@K, Recall@K, Hit Rate, and composite Knowledge Quality Score (KQS). Includes formulas, interpretation, and alert thresholds."
density_score: null
related:
  - p07_ue_brain_query_accuracy
  - n01_sdk_validation_self_audit
  - p01_gl_rag
  - n04_rc_knowledge
  - p01_kc_anti_file_storage
  - kc_agentic_rag
  - bld_schema_reranker_config
  - bld_knowledge_card_retriever_config
  - bld_schema_optimizer
  - p10_lr_knowledge-index-builder
---

# Eval Metric: N04 Retrieval Quality Metrics

## Metric Taxonomy

| Metric | Type | Measures | Higher is Better |
|--------|------|---------|-----------------|
| MRR@K | Ranking | First relevant document rank | YES |
| NDCG@K | Ranking | Graded relevance, position-discounted | YES |
| Precision@K | Relevance | Fraction of top-K that are relevant | YES |
| Recall@K | Relevance | Fraction of relevant docs in top-K | YES |
| Hit Rate@K | Binary | At least one relevant in top-K | YES |
| MAP@K | Ranking | Average precision across queries | YES |
| KQS | Composite | Overall knowledge retrieval quality | YES |

---

## Metric Definitions

### MRR@K (Mean Reciprocal Rank)

**Formula**:
```
MRR@K = (1/|Q|) * sum_{q=1}^{|Q|} (1 / rank_q)

where rank_q = rank of first relevant document for query q
      if no relevant document in top-K: 1/rank_q = 0
```

**Interpretation**:
- 1.0 = perfect (relevant document always ranked #1)
- 0.5 = relevant document typically at rank 2
- 0.33 = relevant document typically at rank 3
- < 0.25 = poor (relevant result not in top-4 on average)

**N04 Target**: >= 0.83 | **Alert**: < 0.75 | **Revert**: < 0.70

---

### NDCG@K (Normalized Discounted Cumulative Gain)

**Formula**:
```
DCG@K = sum_{i=1}^{K} (rel_i / log2(i + 1))
NDCG@K = DCG@K / IDCG@K

where rel_i = relevance score at rank i (binary: 0 or 1; or graded: 0-3)
      IDCG = ideal DCG (perfect ranking)
```

**Graded relevance for CEX**:
- 3 = exact answer source
- 2 = closely related document
- 1 = tangentially relevant
- 0 = not relevant

**N04 Target**: >= 0.80 | **Alert**: < 0.72

---

### Precision@K

**Formula**:
```
Precision@K = (# relevant documents in top-K) / K
```

**Interpretation**:
- 1.0 = all top-K results are relevant
- 0.5 = half of top-K results are relevant

**N04 Target**: >= 0.76 | **Alert**: < 0.68

---

### Recall@K

**Formula**:
```
Recall@K = (# relevant documents in top-K) / (# total relevant documents)
```

**Note**: For N04, "total relevant documents" is typically 1-3 per query (ground truth has 1-3 sources).
When total relevant = 1, Recall@K = Hit Rate@K.

**N04 Target**: >= 0.76 | **Alert**: < 0.68

---

### Knowledge Quality Score (KQS) -- Composite

N04-specific composite metric:

```
KQS = 0.40 * MRR@10
    + 0.30 * NDCG@10
    + 0.15 * Precision@5
    + 0.10 * Recall@10
    + 0.05 * (1 - latency_penalty)

latency_penalty = min(1.0, max(0.0, (p95_ms - 500) / 1000))
```

**Interpretation**:
- >= 0.90 = excellent knowledge retrieval
- 0.80-0.89 = good, production-ready
- 0.70-0.79 = acceptable, improvement queued
- < 0.70 = poor, self-improvement loop triggered

**Current baseline KQS**: ~0.83 (estimated from memory_benchmark_n04.md values)

---

## Per-Query-Type Targets

| Query Type | MRR@10 Target | NDCG@10 Target |
|-----------|--------------|----------------|
| Factual (Type A) | >= 0.88 | >= 0.85 |
| Conceptual (Type B) | >= 0.82 | >= 0.79 |
| Multi-hop (Type C) | >= 0.71 | >= 0.68 |
| Cross-pillar (Type D) | >= 0.74 | >= 0.71 |
| Overall | >= 0.83 | >= 0.80 |

---

## Metric Calculation

```python
def calculate_mrr(queries: list[dict], retriever) -> float:
    reciprocal_ranks = []
    for q in queries:
        results = retriever.query(q["query"], top_k=10)
        rank = next(
            (i+1 for i, r in enumerate(results)
             if r["source"] in q["ground_truth_sources"]),
            None
        )
        reciprocal_ranks.append(1/rank if rank else 0.0)
    return sum(reciprocal_ranks) / len(reciprocal_ranks)

def calculate_ndcg_at_k(queries: list[dict], retriever, k: int = 10) -> float:
    ndcg_scores = []
    for q in queries:
        results = retriever.query(q["query"], top_k=k)
        dcg = sum(
            relevance(r["source"], q) / log2(i+2)
            for i, r in enumerate(results[:k])
        )
        idcg = sum(1 / log2(i+2) for i in range(min(len(q["ground_truth_sources"]), k)))
        ndcg_scores.append(dcg / idcg if idcg > 0 else 0.0)
    return sum(ndcg_scores) / len(ndcg_scores)
```

---

## Usage

```bash
# Full metric report
python _tools/cex_retriever.py --eval \
  --dataset N04_knowledge/P07_evals/eval_dataset_n04.md \
  --metrics mrr,ndcg,precision,recall \
  --k 10

# KQS composite score
python _tools/cex_retriever.py --kqs \
  --dataset N04_knowledge/P07_evals/eval_dataset_n04.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_ue_brain_query_accuracy]] | related | 0.22 |
| [[n01_sdk_validation_self_audit]] | downstream | 0.20 |
| [[p01_gl_rag]] | upstream | 0.20 |
| [[n04_rc_knowledge]] | related | 0.20 |
| [[p01_kc_anti_file_storage]] | upstream | 0.18 |
| [[kc_agentic_rag]] | upstream | 0.18 |
| [[bld_schema_reranker_config]] | upstream | 0.18 |
| [[bld_knowledge_card_retriever_config]] | upstream | 0.17 |
| [[bld_schema_optimizer]] | upstream | 0.17 |
| [[p10_lr_knowledge-index-builder]] | downstream | 0.17 |
