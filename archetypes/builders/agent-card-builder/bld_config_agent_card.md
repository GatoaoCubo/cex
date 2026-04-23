---
kind: config
id: bld_config_agent_card
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
title: "Config Agent Card"
version: "1.0.0"
author: n03_builder
tags: [agent_card, builder, examples]
tldr: "Golden and anti-examples for agent card construction, demonstrating ideal structure and common pitfalls."
domain: "agent card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_retriever_config
  - bld_config_kind
  - bld_config_memory_scope
  - bld_examples_agent_card
  - bld_config_spawn_config
  - bld_config_prompt_version
  - bld_config_validation_schema
  - bld_config_output_validator
  - bld_config_hook_config
  - bld_config_input_schema
---
# Config: agent_card Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p08_ac_{name_lower}.yaml` | `p08_ac_shaka.yaml` |
| Builder directory | kebab-case | `agent-card-builder/` |
| Frontmatter fields | snake_case | `domain_area`, `boot_sequence` |
| Agent_group names | UPPERCASE in name field | `researcher`, `builder`, `marketer` |
| Name slugs | lowercase in id | `shaka`, `edison`, `lily` |
Rule: id MUST equal filename stem.
## File Paths
1. Output: `cex/P08_architecture/examples/p08_ac_{name_lower}.yaml`
2. Compiled: `cex/P08_architecture/compiled/p08_ac_{name_lower}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Total: ~6000 bytes including frontmatter
3. Density: >= 0.80
## Model Enum
| Model | When to use |
|-------|-------------|
| opus | Complex reasoning, code generation, architecture |
| sonnet | Balanced cost/quality, research, marketing |
| haiku | Simple tasks, classification, formatting |
## MCP Convention
1. List all MCPs even if empty: `mcps: []`
2. Use short names: `brain`, `firecrawl`, `railway`, `pg`
3. MCP config path follows: `.mcp-{sat_lower}.json`
## Scaling Defaults
| Field | Default | Max |
|-------|---------|-----|
| max_concurrent | 1 | 3 (BSOD prevention) |
| timeout_minutes | 30 | 120 |
| memory_limit_mb | 2048 | 8192 |

## Metadata

```yaml
id: bld_config_agent_card
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-agent-card.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_retriever_config]] | sibling | 0.32 |
| [[bld_config_kind]] | sibling | 0.31 |
| [[bld_config_memory_scope]] | sibling | 0.31 |
| [[bld_examples_agent_card]] | upstream | 0.30 |
| [[bld_config_spawn_config]] | sibling | 0.29 |
| [[bld_config_prompt_version]] | sibling | 0.29 |
| [[bld_config_validation_schema]] | sibling | 0.29 |
| [[bld_config_output_validator]] | sibling | 0.29 |
| [[bld_config_hook_config]] | sibling | 0.28 |
| [[bld_config_input_schema]] | sibling | 0.28 |
