---
kind: knowledge_card
id: bld_knowledge_retrieval_evaluator
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for retrieval_evaluator production -- evaluation of retrieval system quality
sources: BEIR benchmark, MTEB retrieval tasks, NDCG/MRR literature, TREC evaluation methodology
quality: null
title: "Retrieval Evaluator Builder - Knowledge ISO"
version: "1.0.0"
author: n03_builder
tags: [retrieval_evaluator, builder, knowledge]
tldr: "Domain knowledge for building retrieval evaluators covering ranking metrics, relevance judgment, and evaluation methodology."
domain: "retrieval evaluation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_retrieval_evaluator
  - bld_eval_retrieval_evaluator
  - bld_schema_retrieval_evaluator
---

# Domain Knowledge: retrieval_evaluator

## Executive Summary

Retrieval evaluators measure how well a search or RAG system returns relevant results for a given query. They compute ranking-aware metrics (NDCG, MRR, MAP), set-based metrics (precision, recall, F1), and latency/throughput indicators. A retrieval evaluator is a P07 artifact -- it defines WHAT to measure and HOW to score, not the retrieval logic itself.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P07 (evaluation) |
| Core metrics | NDCG@k, MRR, MAP, Precision@k, Recall@k |
| Judgment types | binary (relevant/not), graded (0-3 scale) |
| Evaluation modes | offline (gold set), online (click-through), hybrid |
| Key benchmarks | BEIR, MTEB retrieval subset, TREC |

## Patterns

- **NDCG@k** -- normalized discounted cumulative gain; preferred for graded relevance where position matters
- **MRR** -- mean reciprocal rank; best when only the first relevant result matters (QA, navigational)
- **MAP** -- mean average precision; balances precision and recall across the full ranked list
- **Precision@k vs Recall@k** -- trade-off between accuracy of top-k results vs coverage of all relevant documents
- **Statistical significance** -- always report confidence intervals; single-run metrics are unreliable
- **Query set size** -- minimum 50 queries for stable metric estimates; 200+ for publication-grade

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| Single metric only | No single metric captures all retrieval quality dimensions |
| No baseline comparison | Absolute scores are meaningless without a reference system |
| Ignoring position | Set-based metrics (precision/recall) miss ranking quality |
| Too few queries | < 30 queries produce unstable metric estimates |
| Mixing judgment scales | Binary and graded relevance in same eval set corrupts NDCG |
| No latency tracking | A perfect ranker at 10s/query is unusable in production |

## Application

1. Define query set with known relevant documents (gold standard)
2. Select metrics matching the use case: NDCG@k for ranked results, MRR for single-answer
3. Establish baseline (BM25 or previous system)
4. Run evaluation pipeline: query -> retrieve -> judge -> score
5. Report with confidence intervals and statistical tests (paired t-test or bootstrap)
6. Track metrics over time to detect retrieval regression
