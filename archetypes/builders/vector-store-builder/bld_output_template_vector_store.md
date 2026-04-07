---
kind: output_template
id: bld_output_template_vector_store
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a vector_store
pattern: every field here exists in SCHEMA — template derives, never invents
---

# Output Template: vector_store
```yaml
id: p01_vdb_{{backend}}
kind: vector_store
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
backend: "{{pinecone|pgvector|chroma|faiss|qdrant|weaviate|milvus|other}}"
connection:
  host: "{{host_or_localhost}}"
  port: {{port_integer}}
  api_key_env: "{{ENV_VAR_NAME_or_null}}"
  tls: {{bool}}
  database: {{database_name_or_null}}
collection: "{{collection_name}}"
dimensions: {{integer}}
distance_metric: "{{cosine|l2|dot_product|inner_product}}"
index_type: "{{hnsw|ivf|flat|ivf_pq|costm}}"
hnsw:
  M: {{integer_4_to_64}}
  ef_construction: {{integer_100_to_500}}
  ef_search: {{integer_50_to_500}}
max_vectors: {{integer_or_null}}
metadata_filtering: {{bool}}
metadata_schema:
  {{field_name}}: {{type}}
persistence: "{{auto|manual|external}}"
namespace_strategy: "{{strategy_description}}"
cloud_region: {{region_or_null}}
pricing: {{pricing_object_or_null}}
domain: vector_storage
quality: null
tags: [vector-store, {{backend}}, {{index_type}}, {{deployment}}]
tldr: "{{backend}} — {{deployment}}, {{index_type}}, {{dimensions}}d, {{metric}}, {{highlight}}"
keywords: [{{backend}}, vectordb, {{index_type}}, {{deployment}}]
linked_artifacts:
  primary: null
  related: [{{upstream_embedder_provider}}]
data_source: "{{backend_docs_url}}"
## Boundary
vector_store IS: storage and indexing config for {{backend}} ({{index_type}}, {{dimensions}} dimensions, {{metric}}).
vector_store IS NOT: embedder_provider, model_provider, retriever, chunker.
## Backend Matrix
| Parameter | Value | Source |
|-----------|-------|--------|
| Backend | {{backend}} | {{url}} |
| Version | {{version}} | {{url}} |
| Host | {{host}}:{{port}} | {{url}} |
| Auth | {{auth_method}} | {{url}} |
| Dimensions | {{dimensions}} | Upstream: {{embedder_provider_id}} |
| Distance Metric | {{metric}} ({{normalization_rationale}}) | {{source}} |
| Index Type | {{index_type}} | {{url}} |
| Max Vectors | {{limit_or_unlimited}} | {{url}} |
| Persistence | {{persistence_behavior}} | {{url}} |
| Metadata Filtering | {{filtering_capabilities}} | {{url}} |
## Index Configuration
| Parameter | Value | Effect |
|-----------|-------|--------|
| M | {{M}} | {{tradeoff_description}} |
| ef_construction | {{ef_construction}} | {{tradeoff_description}} |
| ef_search | {{ef_search}} | {{tradeoff_description}} |
Scale guidance:
- < {{small_threshold}} vectors: {{small_recommendation}}
- {{small_threshold}}-{{large_threshold}} vectors: {{medium_recommendation}}
- > {{large_threshold}} vectors: {{large_recommendation}}
## Namespace Strategy
- {{namespace_rule_1}}
- {{namespace_rule_2}}
- {{namespace_rule_3}}
## Lifecycle Operations
1. **Create**: {{create_command}}
2. **Reindex**: {{reindex_procedure}}
3. **Backup**: {{backup_procedure}}
4. **Restore**: {{restore_procedure}}
## Anti-Patterns
1. {{anti_pattern_1}} — {{consequence}}
2. {{anti_pattern_2}} — {{consequence}}
3. {{anti_pattern_3}} — {{consequence}}
4. {{anti_pattern_4}} — {{consequence}}
## References
- docs: {{backend_docs_url}}
- github: {{github_url}}
- api: {{api_reference_url}}
```
