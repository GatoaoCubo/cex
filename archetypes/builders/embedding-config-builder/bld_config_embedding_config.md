---
kind: config
id: bld_config_embedding_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
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
- Output: `cex/P01_knowledge/examples/p01_emb_{model_slug}.yaml`
- Compiled: `cex/P01_knowledge/compiled/p01_emb_{model_slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 512 bytes
- Total: ~1000 bytes including frontmatter
- Density: >= 0.80

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
