---
kind: config
id: bld_config_embedder_provider
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: low
max_turns: 25
disallowed_tools: []
fork_context: inline
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Embedder Provider"
version: "1.0.0"
author: n03_builder
tags: [embedder_provider, builder, examples]
tldr: "Golden and anti-examples for embedder provider construction, demonstrating ideal structure and common pitfalls."
domain: "embedder provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_model_provider
  - bld_config_model_card
  - bld_knowledge_card_embedder_provider
  - bld_schema_embedder_provider
  - p03_ins_embedder_provider
  - model-provider-builder
  - bld_collaboration_model_provider
  - p11_qg_embedder_provider
  - bld_collaboration_embedder_provider
  - p03_sp_embedder_provider_builder
---
# Config: embedder_provider Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p01_emb_{provider}_{slug}.yaml` | `p01_emb_openai_text_embedding_3_small.yaml` |
| Builder directory | kebab-case | `embedder-provider-builder/` |
| Frontmatter fields | snake_case | `max_tokens`, `batch_size` |
| Provider values | lowercase single word | `openai`, `cohere`, `voyage`, `local` |
| Model slug | snake_case, no provider prefix | `text_embedding_3_small`, `embed_english_v3_0` |
Rule: id MUST equal filename stem (validator checks this).
## File Paths
1. Output: `cex/P01_knowledge/examples/p01_emb_{provider}_{slug}.yaml`
2. Compiled: `cex/P01_knowledge/compiled/p01_emb_{provider}_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Frontmatter: ~600-900 bytes (20+ fields)
2. Body: max 4096 bytes (excl frontmatter)
3. Total: max 5000 bytes
4. Density: >= 0.85
## Provider Enum
Valid: openai, cohere, voyage, jina, nomic, local, huggingface, other
If provider not in list: use "other" and add provider name in tags.
## Dimension Policy (aligned with SCHEMA)
1. Frontmatter: native dimensions unless matryoshka reduction is configured
2. If matryoshka: document reduced dimension in `dimensions_override` field
3. ALWAYS integer, never float or string
4. Common dimensions: 384, 512, 768, 1024, 1536, 3072
## Normalization Policy
1. ALWAYS explicit boolean: true or false
2. true: output vectors are L2-normalized (unit length), use cosine similarity
3. false: raw vectors, use dot-product or L2 distance
4. If provider normalizes by default: set `normalize: true` and note in body
## Authentication
1. NEVER hardcode API keys in artifacts
2. ALWAYS use environment variable reference: `api_key_env: "OPENAI_API_KEY"`
3. For local models: `api_key_env: null` (no auth needed)
## Freshness
1. updated field must be within 90 days of current date
2. Embedding models change less frequently than LLMs, but pricing changes
3. Stale configs (>90d) flagged by lifecycle_rule for review

## Metadata

```yaml
id: bld_config_embedder_provider
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-embedder-provider.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | embedder provider construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_model_provider]] | sibling | 0.55 |
| [[bld_config_model_card]] | sibling | 0.51 |
| [[bld_knowledge_card_embedder_provider]] | upstream | 0.44 |
| [[bld_schema_embedder_provider]] | upstream | 0.44 |
| [[p03_ins_embedder_provider]] | upstream | 0.40 |
| [[model-provider-builder]] | upstream | 0.38 |
| [[bld_collaboration_model_provider]] | upstream | 0.38 |
| [[p11_qg_embedder_provider]] | downstream | 0.37 |
| [[bld_collaboration_embedder_provider]] | upstream | 0.37 |
| [[p03_sp_embedder_provider_builder]] | upstream | 0.37 |
