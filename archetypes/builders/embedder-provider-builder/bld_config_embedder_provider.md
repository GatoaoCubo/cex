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
- Output: `cex/P01_knowledge/examples/p01_emb_{provider}_{slug}.yaml`
- Compiled: `cex/P01_knowledge/compiled/p01_emb_{provider}_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Frontmatter: ~600-900 bytes (20+ fields)
- Body: max 4096 bytes (excl frontmatter)
- Total: max 5000 bytes
- Density: >= 0.85
## Provider Enum
Valid: openai, cohere, voyage, jina, nomic, local, huggingface, other
If provider not in list: use "other" and add provider name in tags.
## Dimension Policy (aligned with SCHEMA)
- Frontmatter: native dimensions unless matryoshka reduction is configured
- If matryoshka: document reduced dimension in `dimensions_override` field
- ALWAYS integer, never float or string
- Common dimensions: 384, 512, 768, 1024, 1536, 3072
## Normalization Policy
- ALWAYS explicit boolean: true or false
- true: output vectors are L2-normalized (unit length), use cosine similarity
- false: raw vectors, use dot-product or L2 distance
- If provider normalizes by default: set `normalize: true` and note in body
## Authentication
- NEVER hardcode API keys in artifacts
- ALWAYS use environment variable reference: `api_key_env: "OPENAI_API_KEY"`
- For local models: `api_key_env: null` (no auth needed)
## Freshness
- updated field must be within 90 days of current date
- Embedding models change less frequently than LLMs, but pricing changes
- Stale configs (>90d) flagged by lifecycle_rule for review
