---
kind: config
id: bld_config_fallback_chain
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
quality: 9.0
title: "Config Fallback Chain"
version: "1.0.0"
author: n03_builder
tags: [fallback_chain, builder, examples]
tldr: "Golden and anti-examples for fallback chain construction, demonstrating ideal structure and common pitfalls."
domain: "fallback chain construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_model_provider
  - bld_config_model_card
  - bld_config_memory_scope
  - bld_examples_model_provider
  - bld_config_handoff_protocol
  - bld_config_retriever_config
  - bld_config_prompt_version
  - bld_config_output_validator
  - bld_config_embedder_provider
  - p01_kc_universal_llm
---
# Config: fallback_chain Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_fc_{slug}.md` | `p02_fc_research_model.md` |
| Builder directory | kebab-case | `fallback-chain-builder/` |
| Frontmatter fields | snake_case | `steps_count`, `timeout_per_step_ms` |
| FC slug | snake_case, lowercase | `research_model`, `api_gateway` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P02_model/examples/p02_fc_{slug}.md`
- Compiled: `cex/P02_model/compiled/p02_fc_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5800 bytes
- Density: >= 0.80
## Provider Enum
| Value | Models | Notes |
|-------|--------|-------|
| anthropic | claude-opus-4-6, claude-sonnet-4-6, claude-haiku-4-5 | Primary CEX provider |
| openai | gpt-4.1, gpt-4.1-mini, gpt-4.1-nano | Alternative provider |
| google | gemini-2.5-pro, gemini-2.5-flash | Google models |
| local | ollama/organizationft:v3, ollama/nomic-embed-text | Self-hosted models |
## Degradation Order Guidelines
| Tier | Capability | Cost | Latency | Example |
|------|-----------|------|---------|---------|
| 1 (primary) | Highest | Highest | Slowest | opus-4-6, gpt-4.1 |
| 2 (degraded) | Medium | Medium | Medium | sonnet-4-6, gpt-4.1-mini |
| 3 (minimum) | Lowest | Lowest | Fastest | haiku-4-5, gpt-4.1-nano |
## Timeout Guidelines
| Task type | Recommended timeout | Rationale |
|-----------|-------------------|-----------|
| Simple (classification) | 5000-10000 ms | Fast response expected |
| Medium (generation) | 15000-30000 ms | Standard LLM generation |
| Complex (research) | 30000-60000 ms | Multi-step reasoning |
| Batch (non-interactive) | 60000-120000 ms | Latency not critical |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_model_provider]] | sibling | 0.35 |
| [[bld_config_model_card]] | sibling | 0.33 |
| [[bld_config_memory_scope]] | sibling | 0.33 |
| [[bld_examples_model_provider]] | upstream | 0.30 |
| [[bld_config_handoff_protocol]] | sibling | 0.30 |
| [[bld_config_retriever_config]] | sibling | 0.28 |
| [[bld_config_prompt_version]] | sibling | 0.28 |
| [[bld_config_output_validator]] | sibling | 0.28 |
| [[bld_config_embedder_provider]] | sibling | 0.28 |
| [[p01_kc_universal_llm]] | upstream | 0.27 |
