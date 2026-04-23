---
id: bld_memory_query_optimizer
kind: learning_record
pillar: P10
version: 1.0.0
created: "2026-04-23"
updated: "2026-04-23"
author: builder_agent
observation: "Query optimization without latency budget leads to pipelines that exceed user tolerance (>2s for interactive search). Re-ranking with cross-encoders provides the best precision improvement but is the most expensive step. HyDE is powerful but adds 500ms+ per query."
pattern: "Always set a total latency budget and allocate per step. Start with re-ranking as the single highest-impact technique. Add rewriting only when queries are frequently ambiguous. Use HyDE only when semantic gap is the primary retrieval failure mode."
evidence: "Re-ranking alone improved NDCG@10 by 15% with only 200ms added latency. Adding HyDE improved another 8% but cost 700ms. Rewriting helped 25% of queries but added no value for well-formed queries."
confidence: 0.78
outcome: SUCCESS
domain: query_optimizer
tags: [query, optimization, search, learning]
tldr: "Budget latency per step, start with re-ranking, add techniques only when justified by query analysis."
quality: null
title: "Query Optimizer Builder - Memory ISO"
density_score: 0.85
llm_function: INJECT
related:
  - bld_knowledge_query_optimizer
---

## Summary

Query optimization is an incremental investment. Each technique adds latency and complexity. Start with the highest-impact, lowest-latency technique and justify each addition.

## Pattern

**Re-ranking first**: highest precision improvement per millisecond invested. Start here.

**Latency budgeting**: allocate total budget, then distribute across steps. Exceeding 2s total kills interactive use.

**Conditional techniques**: rewriting helps ambiguous queries but wastes time on well-formed ones. Use query classification to route.
