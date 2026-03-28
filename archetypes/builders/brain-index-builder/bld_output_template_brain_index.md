---
kind: output_template
id: bld_output_template_brain_index
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for brain_index production
pattern: derives from SCHEMA.md — no extra fields
---

# Output Template: brain_index
```yaml
id: p10_bi_{{index_slug}}
kind: brain_index
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
tags: [brain-index, {{scope}}, {{algorithm}}]
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
