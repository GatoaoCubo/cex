---
kind: config
id: bld_config_rate_limit_config
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
title: "Config Rate Limit Config"
version: "1.0.0"
author: n03_builder
tags: [rate_limit_config, builder, examples]
tldr: "Golden and anti-examples for rate limit config construction, demonstrating ideal structure and common pitfalls."
domain: "rate limit config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_rate_limit_config
  - bld_knowledge_card_rate_limit_config
  - bld_collaboration_rate_limit_config
  - bld_config_model_provider
  - bld_instruction_rate_limit_config
  - bld_schema_rate_limit_config
  - bld_examples_model_provider
  - rate-limit-config-builder
  - p11_qg_rate_limit_config
  - bld_knowledge_card_model_provider
---
# Config: rate_limit_config Production Rules

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_ratelimit_{provider}.md` | `p09_ratelimit_anthropic.md` |
| Builder directory | kebab-case | `rate-limit-config-builder/` |
| Frontmatter fields | snake_case | `rpm`, `tpm`, `budget_usd`, `retry_after` |
| Provider slug | snake_case, lowercase, no hyphens | `anthropic`, `openai`, `litellm_proxy` |
| Tier values | lowercase string | `free`, `build`, `scale`, `enterprise` |
| Model override keys | provider model id format | `claude-3-5-sonnet`, `gpt-4o` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P09_config/examples/p09_ratelimit_{provider}.md`
- Compiled: `cex/P09_config/compiled/p09_ratelimit_{provider}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2000 bytes
- Density: >= 0.80 (no filler)
## Provider Registry
| Provider | Slug | Notes |
|----------|------|-------|
| Anthropic | anthropic | Claude API; tiers: Free/Build/Scale |
| OpenAI | openai | GPT API; tiers: Free/Tier1-5 |
| LiteLLM | litellm | Proxy aggregating multiple providers |
| Azure OpenAI | azure_openai | Region-scoped rate limits |
| Google Vertex | google_vertex | Per-model quotas via Vertex AI |
## Tier Conventions
| Tier | Typical RPM range | Typical TPM range |
|------|------------------|------------------|
| free | 3–5 | 20K–40K |
| build | 50–500 | 80K–200K |
| scale | 1K–4K | 400K–2M |
| enterprise | 4K+ | 2M+ |
Rule: tier value MUST be one of: free, build, scale, enterprise, or a provider-specific string.
## Numeric Constraints
- rpm: positive integer, > 0
- tpm: positive integer, > 0
- rpd: positive integer, > rpm (rpd >= rpm * 60 * operating_hours)
- concurrent: positive integer, typically 1–100
- retry_after: integer seconds, typically 1–60
- alert_threshold: float in [0.0, 1.0]
- budget_usd: positive float

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_rate_limit_config]] | upstream | 0.50 |
| [[bld_knowledge_card_rate_limit_config]] | upstream | 0.49 |
| [[bld_collaboration_rate_limit_config]] | downstream | 0.46 |
| [[bld_config_model_provider]] | sibling | 0.46 |
| [[bld_instruction_rate_limit_config]] | upstream | 0.45 |
| [[bld_schema_rate_limit_config]] | upstream | 0.43 |
| [[bld_examples_model_provider]] | upstream | 0.41 |
| [[rate-limit-config-builder]] | related | 0.41 |
| [[p11_qg_rate_limit_config]] | downstream | 0.41 |
| [[bld_knowledge_card_model_provider]] | upstream | 0.40 |
