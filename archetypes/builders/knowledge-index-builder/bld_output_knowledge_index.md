---
kind: output_template
id: bld_output_template_knowledge_index
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for knowledge_index production
pattern: derives from SCHEMA.md — no extra fields
quality: 9.1
title: "Output Template Knowledge Index"
version: "1.0.0"
author: n03_builder
tags: [knowledge_index, builder, examples]
tldr: "Golden and anti-examples for knowledge index construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge index construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_knowledge_index
  - p11_qg_knowledge_index
  - p03_sp_knowledge_index_builder
  - bld_schema_knowledge_index
  - bld_instruction_knowledge_index
  - p01_kc_knowledge_index
  - knowledge-index-builder
  - bld_collaboration_knowledge_index
  - bld_knowledge_card_knowledge_index
  - bld_architecture_knowledge_index
---

# Output Template: knowledge_index
```yaml
id: p10_bi_{{index_slug}}
kind: knowledge_index
pillar: P10
title: "Brain Index: {{index_name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
scope: "{{what_content_indexed}}"
algorithm: "{{bm25_or_faiss_or_hybrid}}"
corpus_type: "{{text_or_vector_or_structured}}"
domain: "{{domain_value}}"
quality: null
tags: [knowledge-index, {{scope}}, {{algorithm}}]
tldr: "{{dense_summary_max_160ch}}"
rebuild_schedule: "{{on_change_or_hourly_or_daily_or_weekly_or_manual}}"
freshness_max_days: {{number}}
embedding_model: "{{model_name_if_faiss_or_hybrid}}"
density_score: {{0.80_to_1.00}}
corpus_size_estimate: "{{approximate_size}}"
linked_artifacts:
  primary: "{{related_embedding_config_or_rag_source}}"
  related: [{{related_refs}}]
## Scope
{{what_content_is_indexed_and_why}}
## Algorithm Config
### BM25 Parameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| k1 | {{saturation_param}} | {{term_frequency_saturation}} |
| b | {{length_norm_param}} | {{document_length_normalization}} |
| tokenizer | {{tokenizer_type}} | {{tokenization_method}} |
### FAISS Parameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| index_type | {{index_type}} | {{flat_ivf_hnsw}} |
| nprobe | {{nprobe_value}} | {{search_breadth}} |
| metric | {{distance_metric}} | {{l2_or_cosine_or_ip}} |
| dimensions | {{vector_dims}} | {{embedding_dimensions}} |
### Hybrid Weights
| Component | Weight | Notes |
|-----------|--------|-------|
| BM25 | {{bm25_weight}} | {{keyword_contribution}} |
| FAISS | {{faiss_weight}} | {{semantic_contribution}} |
## Filters
| Filter | Type | Condition | Applied |
|--------|------|-----------|---------|
| {{filter_1}} | {{pre_or_post}} | {{condition}} | {{when}} |
| {{filter_2}} | {{pre_or_post}} | {{condition}} | {{when}} |
## Ranking
| Factor | Weight | Description |
|--------|--------|-------------|
| {{factor_1}} | {{weight}} | {{what_it_boosts}} |
| {{factor_2}} | {{weight}} | {{what_it_boosts}} |
## Rebuild
| Trigger | Schedule | Duration | Impact |
|---------|----------|----------|--------|
| {{trigger_1}} | {{when}} | {{estimated_time}} | {{service_impact}} |
| {{trigger_2}} | {{when}} | {{estimated_time}} | {{service_impact}} |
## Monitoring
| Metric | Threshold | Alert |
|--------|-----------|-------|
| {{metric_1}} | {{threshold}} | {{action}} |
| {{metric_2}} | {{threshold}} | {{action}} |
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_knowledge_index]] | downstream | 0.44 |
| [[p11_qg_knowledge_index]] | downstream | 0.42 |
| [[p03_sp_knowledge_index_builder]] | upstream | 0.39 |
| [[bld_schema_knowledge_index]] | downstream | 0.34 |
| [[bld_instruction_knowledge_index]] | upstream | 0.32 |
| [[p01_kc_knowledge_index]] | downstream | 0.29 |
| [[knowledge-index-builder]] | downstream | 0.27 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.27 |
| [[bld_knowledge_card_knowledge_index]] | upstream | 0.26 |
| [[bld_architecture_knowledge_index]] | downstream | 0.26 |
