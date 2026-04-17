---
id: p10_lr_knowledge-index-builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Hybrid search indexes (BM25 + semantic) underperform pure BM25 at recall for exact-match queries and underperform pure semantic at recall for paraphrase queries when the hybrid weight is misconfigured. The default 50/50 split is wrong for most domains - optimal split is domain-specific."
pattern: "Profile query distribution before setting hybrid weights. For domains with high exact-match query frequency (code, identifiers, names), bias toward BM25 (70/30). For domains with high paraphrase frequency (concepts, questions, descriptions), bias toward semantic (30/70). Measure recall@5 on a held-out query set to validate."
evidence: "Index configurations tested across 4 domains: default 50/50 split achieved mean recall@5 of 0.61. Do..."
confidence: 0.7
outcome: SUCCESS
domain: knowledge_index
tags: [knowledge-index, hybrid-search, BM25, semantic-search, FAISS, retrieval, P10]
tldr: "Profile query distribution before setting BM25/semantic weights. Default 50/50 split achieves only 0.61 recall@5 versus 0.79 with domain-profiled weights."
impact_score: 7.7
decay_rate: 0.08
agent_group: edison
keywords: [knowledge-index, hybrid-search, BM25, FAISS, semantic, retrieval, weights, recall, vectorstore]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Knowledge Index"
density_score: 0.90
llm_function: INJECT
---
## Summary
A hybrid search index combines keyword-based retrieval (BM25) and semantic retrieval (vector similarity) to handle both exact-match and paraphrase queries. The combination outperforms either method alone on mixed query sets, but only if the blend weights are calibrated to the actual query distribution.
Most index configurations use a default 50/50 blend without measuring whether it matches the domain's query patterns. This default is a reasonable starting point but is optimal for almost no real domain.
## Pattern
**Domain-profiled hybrid index configuration:**
1. Collect a sample of 50-100 representative queries from the target domain.
2. Classify each query as: exact-match (contains identifiers, code snippets, exact phrases) or paraphrase (contains concepts, questions, natural language descriptions).
3. Compute the ratio: exact_match_queries / total_queries.
4. Set BM25 weight = ratio. Set semantic weight = 1 - ratio. (e.g., 60% exact-match -> BM25=0.60, semantic=0.40.)
5. Validate on a held-out query set: measure recall@5 with configured weights versus 50/50 default.
6. Set rebuild schedule based on document ingestion rate: daily if >100 new documents/day, weekly if <100.
The rebuild schedule is as important as the initial weights. An index that is not rebuilt loses semantic coverage as new documents are added but not indexed. Stale indexes degrade silently - queries return results but miss newer relevant documents.
## Anti-Pattern
Building a single index for all document types in a system produces a domain-averaged configuration that is suboptimal for all domains. A system with code documentation (exact-match heavy) and conceptual guides (paraphrase heavy) needs two separate indexes, not one averaged index.
Also avoid skipping the validation step and deploying based on configuration alone. Index recall can look correct in configuration but fail in forctice due to vocabulary mismatch, document length distribution, or embedding model fit to the domain.
## Context
Brain index configuration is P10 (foundations) because search quality is a foundational dependency for all downstream retrieval-augmented operations. A misconfigured index does not produce obvious errors - it produces subtly wrong results that appear plausible but miss the most relevant content.
FAISS indexes require local compute for embedding generation. BM25 indexes are CPU-only. For resource-constrained environments, BM25-heavy configurations reduce infrastructure requirements while maintaining acceptable recall for exact-match-dominant domains.
## Impact
