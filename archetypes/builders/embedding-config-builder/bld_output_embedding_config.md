---
kind: output_template
id: bld_output_template_embedding_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an embedding_config
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Embedding Config"
version: "1.0.0"
author: n03_builder
tags: [embedding_config, builder, examples]
tldr: "Golden and anti-examples for embedding config construction, demonstrating ideal structure and common pitfalls."
domain: "embedding config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_input_schema
  - bld_output_template_agent_card
  - bld_output_template_golden_test
  - bld_schema_embedding_config
  - bld_output_template_feature_flag
  - bld_output_template_runtime_rule
  - bld_output_template_lens
  - bld_output_template_output_validator
  - bld_output_template_skill
  - bld_output_template_constraint_spec
---

# Output Template: embedding_config
```yaml
id: p01_emb_{{model_slug}}
kind: embedding_config
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
model_name: "{{embedding_model_identifier}}"
provider: "{{provider_name}}"
dimensions: {{integer}}
chunk_size: {{integer}}
overlap: {{integer}}
tokenizer: "{{tokenizer_name}}"
distance_metric: "{{cosine_or_euclidean_or_dot_product}}"
batch_size: {{integer}}
normalize: {{boolean}}
max_tokens: {{integer}}
cost_per_1m_tokens: {{float_or_null}}
domain: "{{domain_value}}"
quality: null
tags: [embedding, {{provider_tag}}, {{model_tag}}]
tldr: "{{dense_summary_max_160ch}}"
```
## Model
`{{model_name_provider_and_key_specs}}`
## Chunking
`{{chunk_size_overlap_and_tokenizer_strategy}}`
## Performance
`{{latency_throughput_and_cost_characteristics}}`
## Integration
`{{how_to_use_this_config_in_rag_pipeline}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Template Standards

1. Define all required sections for this output kind
2. Include frontmatter schema with mandatory fields
3. Provide structural markers for post-validation
4. Specify format constraints for markdown YAML JSON
5. Reference the validation_schema for automated checks

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | embedding config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_input_schema]] | sibling | 0.39 |
| [[bld_output_template_agent_card]] | sibling | 0.39 |
| [[bld_output_template_golden_test]] | sibling | 0.38 |
| [[bld_schema_embedding_config]] | downstream | 0.37 |
| [[bld_output_template_feature_flag]] | sibling | 0.36 |
| [[bld_output_template_runtime_rule]] | sibling | 0.35 |
| [[bld_output_template_lens]] | sibling | 0.34 |
| [[bld_output_template_output_validator]] | sibling | 0.33 |
| [[bld_output_template_skill]] | sibling | 0.32 |
| [[bld_output_template_constraint_spec]] | sibling | 0.31 |
