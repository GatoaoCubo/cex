---
kind: config
id: bld_config_model_provider
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
title: "Config Model Provider"
version: "1.0.0"
author: n03_builder
tags: [model_provider, builder, examples]
tldr: "Golden and anti-examples for model provider construction, demonstrating ideal structure and common pitfalls."
domain: "model provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_model_provider
  - bld_config_model_card
  - bld_memory_model_provider
  - model-provider-builder
  - p03_ins_model_provider
  - bld_knowledge_card_model_provider
  - p03_sp_model_provider_builder
  - bld_config_embedder_provider
  - bld_examples_model_provider
  - bld_schema_model_provider
---
# Config: model_provider Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_mp_{provider}.yaml` | `p02_mp_anthropic.yaml` |
| Builder directory | kebab-case | `model-provider-builder/` |
| Frontmatter fields | snake_case | `rate_limit_rpm`, `api_key_env` |
| Provider values | lowercase single word | `anthropic`, `openai`, `google` |
| Model IDs | exact provider identifier | `claude-opus-4-6`, `gpt-4o-2024-08-06` |
Rule: id MUST equal filename stem (validator checks this).
## File Paths
1. Output: `cex/P02_model/examples/p02_mp_{provider}.yaml`
2. Compiled: `cex/P02_model/compiled/p02_mp_{provider}.yaml`
3. Router config: `cex/.cex/config/router_config.yaml` (consumes model_provider)
## Size Limits (aligned with SCHEMA)
1. Frontmatter: ~700-1000 bytes (22+ fields)
2. Body: max 4096 bytes (excl frontmatter)
3. Total: max 5100 bytes
4. Density: >= 0.85
## Provider Enum
Valid: anthropic, openai, google, ollama, groq, mistral, together, fireworks, deepseek, other
If provider not in list: use "other" and add provider name in tags.
## Model ID Policy
1. ALWAYS use the full versioned model identifier (e.g., `gpt-4o-2024-08-06`, not `gpt-4o`)
2. For providers with stable IDs (Anthropic): use current published name
3. For Ollama: use `model:tag` format (e.g., `llama3.1:70b`)
4. NEVER use deprecated model IDs — check provider deprecation schedule
## Rate Limit Policy
1. Document the ACTUAL tier limits for the user's account
2. Free tier limits are default when tier is unspecified
3. RPM (requests per minute) and TPM (tokens per minute) are separate constraints
4. If provider uses different rate limit structure: document in body, set standard fields to null
## Authentication
1. NEVER hardcode API keys in artifacts
2. ALWAYS use environment variable reference: `api_key_env: "ANTHROPIC_API_KEY"`
3. For Ollama/local: `api_key_env: null` (no auth needed)
## Freshness
1. updated field must be within 90 days of current date
2. Model IDs change frequently — check provider model list on every build
3. Rate limits change with account tier upgrades — verify on each update

## Metadata

```yaml
id: bld_config_model_provider
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-model-provider.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | model provider construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_model_provider]] | upstream | 0.52 |
| [[bld_config_model_card]] | sibling | 0.52 |
| [[bld_memory_model_provider]] | downstream | 0.52 |
| [[model-provider-builder]] | upstream | 0.51 |
| [[p03_ins_model_provider]] | upstream | 0.50 |
| [[bld_knowledge_card_model_provider]] | upstream | 0.50 |
| [[p03_sp_model_provider_builder]] | upstream | 0.49 |
| [[bld_config_embedder_provider]] | sibling | 0.47 |
| [[bld_examples_model_provider]] | upstream | 0.43 |
| [[bld_schema_model_provider]] | upstream | 0.42 |
