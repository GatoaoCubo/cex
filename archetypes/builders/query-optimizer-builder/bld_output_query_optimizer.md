---
kind: output_template
id: bld_output_query_optimizer
pillar: P05
llm_function: PRODUCE
purpose: Template for producing a query_optimizer artifact
quality: null
title: "Query Optimizer Builder - Output ISO"
version: "1.0.0"
author: n03_builder
tags: [query_optimizer, builder, output]
tldr: "Output template for query optimizer: frontmatter field guide, required body sections, filled example, and quality gate checklist for query rewriting, expansion, and multi-hop decomposition rules for rag retrieval."
domain: "query optimization"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_query_optimizer
---

# Output Template: query_optimizer

```yaml
id: p01_qo_{{optimizer_slug}}
kind: query_optimizer
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
target_system: "{{retrieval_system}}"
techniques: [{{technique_list}}]
reranker_model: "{{cross_encoder_or_null}}"
latency_budget_ms: {{integer}}
domain: "{{domain_value}}"
quality: null
tags: [query, optimizer, {{technique_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```

## Strategy
`{{pipeline_order_and_technique_selection}}`

## Rewriting
`{{llm_prompt_for_query_reformulation}}`

## Expansion
`{{synonym_sources_expansion_limits}}`

## Re-ranking
`{{model_topn_rerank_count}}`

## Latency Budget
`{{time_allocation_per_step}}`

## Fallback
`{{behavior_on_optimization_failure}}`

## Quality Gate Checklist

| Gate | Check | Pass Condition |
|------|-------|---------------|
| H01 | Frontmatter complete | All required fields present with valid types |
| H02 | ID matches filename | id field equals filename stem |
| H03 | Naming convention | Follows p01_qo_{{name}}.md + .yaml pattern |
| H04 | Body sections present | All required sections non-empty |
| H05 | Size within limits | Total <= 5120 bytes |
| H06 | No placeholder text | No {{var}} unreplaced |
| H07 | quality: null | Never self-scored |

## Properties

| Property | Value |
|----------|-------|
| Kind | `output` |
| Pillar | P05 |
| Domain | query optimizer construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
