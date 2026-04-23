---
kind: config
id: bld_config_model_card
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
title: "Config Model Card"
version: "1.0.0"
author: n03_builder
tags: [model_card, builder, examples]
tldr: "Golden and anti-examples for model card construction, demonstrating ideal structure and common pitfalls."
domain: "model card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_model_provider
  - bld_config_embedder_provider
  - bld_collaboration_model_provider
  - model-provider-builder
  - bld_config_memory_scope
  - bld_config_retriever_config
  - bld_config_output_validator
  - bld_config_handoff_protocol
  - bld_memory_model_provider
  - bld_config_prompt_version
---
# Config: model_card Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_mc_{provider}_{slug}.md` | `p02_mc_google_gemini_2_5_pro.md` |
| Builder directory | kebab-case | `model-card-builder/` |
| Frontmatter fields | snake_case | `context_window`, `max_output` |
| Provider values | lowercase single word | `anthropic`, `openai`, `google` |
| Model slug | snake_case, no provider prefix | `opus_4`, `gpt_4o`, `gemini_2_5_pro` |
Rule: id MUST equal filename stem (validator checks this).
## File Paths
1. Output: `cex/P02_model/examples/p02_mc_{provider}_{slug}.md`
2. Compiled: `cex/P02_model/compiled/p02_mc_{provider}_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Frontmatter: ~800-1200 bytes (26 fields)
2. Body: max 4096 bytes (excl frontmatter)
3. Total: max 5300 bytes
4. Density: >= 0.85
## Provider Enum (same as SCHEMA)
Valid: anthropic, openai, google, meta, mistral, cohere, deepseek, alibaba, ai21, other
If provider not in list: use "other" and add provider name in tags.
## Pricing Policy (aligned with SCHEMA)
1. Frontmatter: BASE TIER only (lowest published standard API price)
2. If tiered: document higher tiers in body Specifications table
3. ALWAYS per_1M_tokens, USD only
4. open-weight: null (not 0, not "free")
5. commercial free tier: 0.00 (not null)
6. cache_write: null if provider has no symmetric cache write price
## Freshness
1. updated field must be within 90 days of current date
2. If model deprecated: status = "deprecated", linked_artifacts must point to replacement
3. Stale cards (>90d) flagged by lifecycle_rule for review

## Metadata

```yaml
id: bld_config_model_card
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-model-card.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | model card construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_model_provider]] | sibling | 0.58 |
| [[bld_config_embedder_provider]] | sibling | 0.50 |
| [[bld_collaboration_model_provider]] | upstream | 0.44 |
| [[model-provider-builder]] | upstream | 0.43 |
| [[bld_config_memory_scope]] | sibling | 0.39 |
| [[bld_config_retriever_config]] | sibling | 0.38 |
| [[bld_config_output_validator]] | sibling | 0.37 |
| [[bld_config_handoff_protocol]] | sibling | 0.36 |
| [[bld_memory_model_provider]] | downstream | 0.36 |
| [[bld_config_prompt_version]] | sibling | 0.36 |
