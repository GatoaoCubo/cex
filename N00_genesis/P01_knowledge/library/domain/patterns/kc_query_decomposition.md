---
id: p01_kc_query_decomposition
kind: knowledge_card
type: domain
pillar: P01
title: "Query Decomposition"
version: 1.1.0
created: 2026-03-31
updated: 2026-04-07
author: n07_orchestrator
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, retrieval, multi-step-reasoning]
tldr: "Split complex queries into independent sub-queries, resolve each with the best source, merge into a single answer."
keywords: [decomposition, sub-query, divide-conquer, complex, fan-out, merge]
when_to_use: "Query has 2+ implicit questions, requires multiple sources, or mixes retrieval types (internal + external)."
density_score: 0.95
related:
  - spec_infinite_bootstrap_loop
  - p01_kc_skill_references
  - bld_knowledge_card_agentic_rag
  - bld_knowledge_card_research_pipeline
  - p01_report_intent_resolution
  - p01_kc_research_pipeline
  - atom_07_llamaindex
  - bld_output_template_agentic_rag
  - p02_agent_research_pipeline_intelligence
  - p07_judge_answer_relevance
---

# Query Decomposition

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | One complex query -> N independent sub-queries -> merge |
| Trigger | Query contains AND/OR logic, comparisons, or multi-source needs |
| Benefit | Each sub-query hits the optimal retrieval path |
| Risk if skipped | Partial answers, hallucinated gaps, context overflow |

## Key Concepts

- **Atomic sub-query**: single-fact question answerable by one source
- **Fan-out**: dispatch sub-queries in parallel when independent
- **Dependency graph**: some sub-queries need prior results (serial)
- **Merge strategy**: combine sub-answers into coherent final response

## Strategy Phases

| Phase | Action | Output |
|-------|--------|--------|
| 1. Detect | Count implicit questions in user query | N sub-queries |
| 2. Classify | Tag each sub-query: internal, external, computed | Source map |
| 3. Resolve | Execute each sub-query against its source | N partial answers |
| 4. Merge | Synthesize partials into unified answer | Final response |
| 5. Verify | Cross-check merged answer for contradictions | Confidence flag |

## Golden Rules

- Never answer a multi-part query as a single retrieval -- split first
- Sub-queries must be self-contained (no dangling references)
- If sub-query count > 6, re-group into 2-3 composite sub-queries
- Always preserve the user's original framing in the merged output
- Flag low-confidence sub-answers instead of silently merging them

## Visual Flow

```
User query
  |
  +--[detect]--> sub-Q1 (internal) ---> answer-1 --+
  |                                                  |
  +--[detect]--> sub-Q2 (external) ---> answer-2 --+--> MERGE --> final
  |                                                  |
  +--[detect]--> sub-Q3 (computed) ---> answer-3 --+
```

## Worked Examples

| Complex Query | Sub-Queries | Sources |
|---------------|-------------|---------|
| "Compare our pricing with 3 competitors" | 1. Our pricing 2. Competitor prices 3. Gap analysis 4. Recommendations | 1. Internal DB 2. Web research 3. Computed 4. Computed |
| "Summarize Q1 sales and predict Q2" | 1. Q1 sales data 2. Q1 trends 3. Q2 forecast | 1. CRM 2. Analytics 3. Model inference |
| "Which framework is fastest and easiest to learn?" | 1. Benchmark speed 2. Learning curve 3. Rank by both | 1. Benchmark DB 2. Survey data 3. Computed |

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| Single monolithic retrieval | Mixes contexts, dilutes relevance |
| Over-decomposition (>6 splits) | Token waste, merge noise |
| Ignoring dependencies | Sub-Q3 needs Sub-Q1 result but runs in parallel |
| Dropping the merge step | User gets a list, not an answer |

## Linked Artifacts

- `p01_kc_source_triangulation` -- verify sub-answers across sources
- `p01_kc_token_budgeting` -- budget context across N sub-queries
- `p01_kc_confidence_scoring` -- score each sub-answer before merge

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_infinite_bootstrap_loop]] | related | 0.24 |
| [[p01_kc_skill_references]] | sibling | 0.24 |
| [[bld_knowledge_card_agentic_rag]] | sibling | 0.22 |
| [[bld_knowledge_card_research_pipeline]] | sibling | 0.21 |
| [[p01_report_intent_resolution]] | sibling | 0.20 |
| [[p01_kc_research_pipeline]] | sibling | 0.19 |
| [[atom_07_llamaindex]] | sibling | 0.19 |
| [[bld_output_template_agentic_rag]] | downstream | 0.18 |
| [[p02_agent_research_pipeline_intelligence]] | downstream | 0.17 |
| [[p07_judge_answer_relevance]] | downstream | 0.16 |
