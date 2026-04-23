---
id: kc_retrieval_evaluator
kind: knowledge_card
title: Retrieval Evaluator -- RAG-Specific IR Metrics Suite
version: 1.0.0
quality: null
pillar: P01
tags:
  - retrieval
  - evaluation
  - rag
  - information-retrieval
  - P07
related:
  - kc_eval_metric
  - kc_benchmark_suite
  - kc_retriever_config
  - kc_rag_source
  - kc_embedding_config
  - kc_eval_framework
---

# Retrieval Evaluator

A retrieval evaluator is a specialized evaluation suite that measures the quality of document retrieval in Retrieval-Augmented Generation (RAG) systems. Unlike a single eval_metric (which defines one measure) or a benchmark (which tests end-to-end system performance), a retrieval evaluator combines multiple information retrieval (IR) metrics into a coherent assessment of how well a retriever surfaces relevant documents for downstream generation.

## Description

RAG systems live or die by retrieval quality. A perfect generator fed irrelevant documents produces confident hallucinations. A retrieval evaluator applies classical IR metrics -- adapted for the chunked, embedding-based retrieval that modern RAG pipelines use -- to quantify whether the right documents reach the generator's context window.

The evaluator operates at three granularities: per-query (did this specific question find its answer?), per-corpus (how well does the index serve the full query distribution?), and per-chunk (are chunk boundaries preserving retrievable units of meaning?).

## Key Concepts

| Concept | Definition | Typical Range |
|---------|-----------|---------------|
| MRR (Mean Reciprocal Rank) | Average of 1/rank for the first relevant result across queries | 0.0 -- 1.0 |
| NDCG (Normalized Discounted Cumulative Gain) | Measures ranking quality with position-weighted relevance scores | 0.0 -- 1.0 |
| Precision@k | Fraction of retrieved documents in the top-k that are relevant | 0.0 -- 1.0 |
| Recall@k | Fraction of all relevant documents that appear in the top-k | 0.0 -- 1.0 |
| Hit Rate (Success@k) | Binary: did at least one relevant document appear in top-k? | 0.0 -- 1.0 |
| MAP (Mean Average Precision) | Mean of average precision scores across all queries | 0.0 -- 1.0 |
| Retrieval Latency | Time from query embedding to ranked result set, in milliseconds | 10 -- 500ms |
| Faithfulness Proxy | Correlation between retrieval rank and downstream answer correctness | 0.0 -- 1.0 |

## Related Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| eval_metric | P07 | Parent -- retrieval_evaluator is a composite of eval_metrics |
| benchmark | P07 | Sibling -- benchmarks test full systems; retrieval_evaluator tests the retriever |
| retriever_config | P01 | Upstream -- the retriever being evaluated |
| rag_source | P01 | Upstream -- the corpus the retriever searches |
| embedding_config | P01 | Upstream -- the vector space in which retrieval happens |
| scoring_rubric | P07 | Sibling -- defines how to interpret metric thresholds |
| chunk_strategy | P01 | Upstream -- chunk boundaries affect all retrieval metrics |

## Anti-Patterns

- **Single-metric tunnel vision**: Reporting only hit rate while ignoring ranking quality (NDCG). A system that always returns one relevant doc at position 10 has perfect hit@10 but terrible MRR.
- **Evaluation without relevance labels**: Running metrics against unlabeled corpora produces meaningless numbers. At minimum use LLM-as-judge to generate relevance assessments.
- **Ignoring corpus coverage**: Evaluating on a query set that covers 5% of the corpus gives false confidence. Stratify queries by topic, difficulty, and document density.
- **Conflating retrieval and generation quality**: A low-quality final answer does not mean retrieval failed. Isolate retrieval evaluation from end-to-end evaluation.
- **Static evaluation only**: Retrieval quality degrades as the corpus grows and query distribution shifts. Run retrieval evaluation continuously, not once.

## Properties

| Property | Value |
|----------|-------|
| Kind | knowledge_card |
| Pillar | P01 (knowledge domain), P07 (evaluation domain) |
| Domain | Information retrieval evaluation |
| Pipeline | 8F (F1-F8) |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_eval_metric]] | parent | 0.45 |
| [[kc_benchmark_suite]] | sibling | 0.38 |
| [[kc_retriever_config]] | upstream | 0.42 |
| [[kc_rag_source]] | upstream | 0.40 |
| [[kc_embedding_config]] | upstream | 0.37 |
| [[kc_eval_framework]] | sibling | 0.33 |
| [[kc_chunk_strategy]] | upstream | 0.30 |
| [[kc_scoring_rubric]] | sibling | 0.28 |
