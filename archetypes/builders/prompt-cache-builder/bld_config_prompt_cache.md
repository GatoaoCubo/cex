---
kind: config
id: bld_config_prompt_cache
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 20
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
permission_scope: nucleus
quality: 9.0
title: "Config Prompt Cache"
version: "1.0.0"
author: n03_builder
tags: [prompt_cache, builder, examples]
tldr: "Golden and anti-examples for prompt cache construction, demonstrating ideal structure and common pitfalls."
domain: "prompt cache construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: prompt_cache Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_pc_{name_slug}.yaml` | `p10_pc_rag_agent_shared.yaml` |
| Builder directory | kebab-case | `prompt-cache-builder/` |
| Frontmatter fields | snake_case | `ttl_seconds`, `eviction_strategy` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `P10_memory/examples/p10_pc_{name}.yaml`
2. Compiled: `P10_memory/compiled/p10_pc_{name}.yaml`
## Size Limits
1. Total file: max 2048 bytes
2. tldr: <= 160 chars
## TTL Guidelines
| Freshness Need | TTL | Use Case |
|----------------|-----|----------|
| Real-time | 60s | Live data, streaming |
| Standard | 300s | General prompts, Anthropic default |
| Stable | 3600s | System prompts, few-shot |
| Long-lived | 86400s | Static reference, rarely changes |
## Provider-Specific Caching
| Provider | Type | Config | Discount |
|----------|------|--------|----------|
| Anthropic | Explicit breakpoints | cache_control: ephemeral | 90% read |
| OpenAI | Automatic prefix | >= 1024 token prefix | 50% read |
| Google | Explicit context | >= 32768 tokens | 75% read |

## Metadata

```yaml
id: bld_config_prompt_cache
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-prompt-cache.md
```
