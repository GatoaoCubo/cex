---
kind: output_template
id: bld_output_template_embedder_provider
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an embedder_provider
pattern: every field here exists in SCHEMA — template derives, never invents
quality: 9.1
title: "Output Template Embedder Provider"
version: "1.0.0"
author: n03_builder
tags: [embedder_provider, builder, examples]
tldr: "Golden and anti-examples for embedder provider construction, demonstrating ideal structure and common pitfalls."
domain: "embedder provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_embedder_provider
  - p11_qg_embedder_provider
  - bld_schema_embedder_provider
  - bld_output_template_model_provider
  - bld_knowledge_card_embedder_provider
  - p03_sp_embedder_provider_builder
  - bld_config_embedder_provider
  - bld_output_template_model_card
  - bld_examples_embedder_provider
  - p01_emb_openai_text_embedding_3_small
---

# Output Template: embedder_provider
```yaml
id: p01_emb_{{provider}}_{{model_slug}}
kind: embedder_provider
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
provider: "{{openai|cohere|voyage|jina|nomic|local|huggingface|other}}"
model: "{{official_model_id}}"
dimensions: {{integer}}
dimensions_override: {{integer_or_null}}
max_tokens: {{integer}}
batch_size: {{integer}}
normalize: {{bool}}
truncate: {{bool_or_string}}
distance_metric: "{{cosine|dot_product|euclidean}}"
matryoshka: {{bool}}
sparse_support: {{bool}}
api_key_env: "{{ENV_VAR_NAME_or_null}}"
api_base_url: {{url_or_null}}
pricing:
  per_1m_tokens: {{float_or_null}}
  per_request: {{float_or_null}}
  currency: USD
mteb_score: {{float_or_null}}
domain: embedding
quality: null
tags: [embedder-provider, {{provider}}, {{model_family}}, {{key_use_case}}]
tldr: "{{model}} — {{provider}}, {{dimensions}}d, ${{price}}/1M tokens, {{highlight}}"
keywords: [{{provider}}, {{model}}, {{domain_terms}}]
linked_artifacts:
  primary: null
  related: [{{other_embedder_providers_or_null}}]
data_source: "{{provider_docs_url}}"
## Boundary
embedder_provider IS: connection config for {{model}} (dimensions, normalization, batch limits).
embedder_provider IS NOT: vector_store, model_provider, retriever, chunker.
## Configuration Matrix
| Parameter | Value | Source |
|-----------|-------|--------|
| Provider | {{provider}} | {{url}} |
| Model | {{official_model_id}} | {{url}} |
| Dimensions | {{dimensions}} (native), {{reduced}} (MRL) | {{url}} |
| Max Tokens | {{max_tokens}} | {{url}} |
| Batch Size | {{batch_size}} texts/request | {{url}} |
| Normalize | {{bool}} | {{url}} |
| Truncate | {{truncate_behavior}} | {{url}} |
| Distance Metric | {{metric}} | {{rationale}} |
| Pricing | ${{price}} per 1M tokens | {{pricing_url}} |
## Dimension Tradeoffs
| Dimensions | MTEB Score | Storage/vec | Latency | Use Case |
|------------|------------|-------------|---------|----------|
| {{native_dim}} | {{score}}% | {{bytes}} | baseline | {{use_case}} |
| {{reduced_dim}} | {{score}}% | {{bytes}} | {{delta}} | {{use_case}} |
## Integration Pattern
````{{language}}`
`{{sdk_initialization_code}}`
`{{embedding_call_example}}`
`{{vector_extraction}}`
```
## Anti-Patterns
1. {{anti_pattern_1}} — {{consequence}}
2. {{anti_pattern_2}} — {{consequence}}
3. {{anti_pattern_3}} — {{consequence}}
4. {{anti_pattern_4}} — {{consequence}}
## References
- docs: {{provider_docs_url}}
- pricing: {{pricing_page_url}}
- mteb: {{mteb_leaderboard_url}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_embedder_provider]] | upstream | 0.57 |
| [[p11_qg_embedder_provider]] | downstream | 0.46 |
| [[bld_schema_embedder_provider]] | downstream | 0.45 |
| [[bld_output_template_model_provider]] | sibling | 0.42 |
| [[bld_knowledge_card_embedder_provider]] | upstream | 0.42 |
| [[p03_sp_embedder_provider_builder]] | upstream | 0.39 |
| [[bld_config_embedder_provider]] | downstream | 0.39 |
| [[bld_output_template_model_card]] | sibling | 0.38 |
| [[bld_examples_embedder_provider]] | downstream | 0.38 |
| [[p01_emb_openai_text_embedding_3_small]] | upstream | 0.35 |
