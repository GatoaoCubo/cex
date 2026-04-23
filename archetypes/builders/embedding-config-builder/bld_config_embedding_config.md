---
kind: config
id: bld_config_embedding_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Embedding Config"
version: "1.0.0"
author: n03_builder
tags: [embedding_config, builder, examples]
tldr: "Golden and anti-examples for embedding config construction, demonstrating ideal structure and common pitfalls."
domain: "embedding config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_embedder_provider
  - bld_examples_embedding_config
  - p01_emb_openai_text_embedding_3_small
  - bld_knowledge_card_embedding_config
  - bld_config_retriever_config
  - bld_architecture_embedding_config
  - p01_kc_embedding_config
  - bld_collaboration_embedding_config
  - p01_emb_nomic_embed_text
  - bld_config_model_provider
---
# Config: embedding_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p01_emb_{model_slug}.yaml` | `p01_emb_nomic_embed_text.yaml` |
| Builder directory | kebab-case | `embedding-config-builder/` |
| Frontmatter fields | snake_case | `model_name`, `chunk_size` |
| Model slugs | snake_case, lowercase | `nomic_embed_text`, `text_embedding_3_small` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `cex/P01_knowledge/examples/p01_emb_{model_slug}.yaml`
2. Compiled: `cex/P01_knowledge/compiled/p01_emb_{model_slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 512 bytes
2. Total: ~1000 bytes including frontmatter
3. Density: >= 0.80
## Distance Metric Enum
| Metric | When to use | Normalize |
|--------|-------------|-----------|
| cosine | Default, most retrieval tasks | true (required) |
| euclidean | When absolute distance matters | false |
| dot_product | Pre-normalized vectors, max inner product | false |
## Common Model Specs
| Model | Provider | Dimensions | Max Tokens |
|-------|----------|-----------|------------|
| nomic-embed-text | ollama | 768 | 8192 |
| mxbai-embed-large | ollama | 1024 | 512 |
| text-embedding-3-small | openai | 1536 | 8191 |
| text-embedding-3-large | openai | 3072 | 8191 |
| embed-english-v3.0 | cohere | 1024 | 512 |

## Metadata

```yaml
id: bld_config_embedding_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-embedding-config.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_embedder_provider]] | sibling | 0.39 |
| [[bld_examples_embedding_config]] | upstream | 0.38 |
| [[p01_emb_openai_text_embedding_3_small]] | upstream | 0.37 |
| [[bld_knowledge_card_embedding_config]] | upstream | 0.36 |
| [[bld_config_retriever_config]] | sibling | 0.36 |
| [[bld_architecture_embedding_config]] | upstream | 0.34 |
| [[p01_kc_embedding_config]] | upstream | 0.33 |
| [[bld_collaboration_embedding_config]] | downstream | 0.33 |
| [[p01_emb_nomic_embed_text]] | upstream | 0.32 |
| [[bld_config_model_provider]] | sibling | 0.31 |
