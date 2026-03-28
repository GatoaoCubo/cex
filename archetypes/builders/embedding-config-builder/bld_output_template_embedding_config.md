---
kind: output_template
id: bld_output_template_embedding_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an embedding_config
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{model_name_provider_and_key_specs}}
## Chunking
{{chunk_size_overlap_and_tokenizer_strategy}}
## Performance
{{latency_throughput_and_cost_characteristics}}
## Integration
{{how_to_use_this_config_in_rag_pipeline}}
## References
- {{reference_1}}
- {{reference_2}}
