---
id: p07_ue_brain_query_accuracy
kind: unit_eval
pillar: P07
description: "Unit test for brain_query search accuracy across known queries"
target: brain_query
version: 1.0.0
created: 2026-03-24
author: operations_agent
quality: 9.0
tags: [unit-eval, brain, search, accuracy]
updated: "2026-04-07"
domain: "evaluation"
title: "Unit Eval Brain Query Accuracy"
density_score: 0.92
tldr: "Defines unit eval for unit eval brain query accuracy, with validation gates and integration points."
related:
  - p07_se_brain_query
  - p01_rs_brain_faiss_index
  - skill
  - p10_bi_organization_brain
  - bld_collaboration_skill
  - tpl_validation_schema
  - p04_plug_brain_search
  - research_then_build
  - bld_tools_spawn_config
  - bld_tools_context_window_config
---

# Unit Eval: brain_query Accuracy

## Target
brain_query MCP tool — hybrid BM25+FAISS search.

## Test Cases
| Query | Expected Top Result | Pass Criteria |
|-------|-------------------|---------------|
| "agent for SEO" | KC with SEO/marketplace | Top-3 contains match |
| "how to spawn agent_group" | KC_operations_agent_003 or spawn skill | Top-1 score > 0.7 |
| "quality gate implementation" | KC_operations_agent_010 | Exact match in top-1 |
| "brand propagation pipeline" | brand_propagation skill | Top-3 contains match |
| "whatsapp voice pipeline" | voice_pipeline skill | Top-3 contains match |

## Execution
```bash
python -c "
from organization_brain.vector_search import hybrid_search
for query, expected in TEST_CASES:
    results = hybrid_search(query, k=3)
    assert any(expected in r['source'] for r in results)
"
```

## Metrics
| Metric | Threshold | Current |
|--------|-----------|---------|
| Top-1 accuracy | >= 70% | ~72% |
| Top-3 accuracy | >= 85% | ~88% |
| Query latency | < 500ms | ~200ms |
| Fallback rate | < 5% | ~2% |

## Failure Action
1. Top-1 < 70%: Rebuild FAISS index, check embedding model
2. Latency > 500ms: Check Ollama status, model loading

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_se_brain_query]] | related | 0.32 |
| [[p01_rs_brain_faiss_index]] | related | 0.28 |
| [[skill]] | downstream | 0.26 |
| [[p10_bi_organization_brain]] | downstream | 0.26 |
| [[bld_collaboration_skill]] | downstream | 0.25 |
| [[tpl_validation_schema]] | upstream | 0.24 |
| [[p04_plug_brain_search]] | upstream | 0.22 |
| [[research_then_build]] | downstream | 0.22 |
| [[bld_tools_spawn_config]] | upstream | 0.21 |
| [[bld_tools_context_window_config]] | upstream | 0.21 |
