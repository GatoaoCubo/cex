---
kind: tools
id: bld_tools_rate_limit_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for rate_limit_config production
quality: 9.0
title: "Tools Rate Limit Config"
version: "1.0.0"
author: n03_builder
tags: [rate_limit_config, builder, examples]
tldr: "Golden and anti-examples for rate limit config construction, demonstrating ideal structure and common pitfalls."
domain: "rate limit config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_function_def
  - rate-limit-config-builder
  - bld_tools_search_tool
  - bld_tools_batch_config
  - bld_knowledge_card_rate_limit_config
  - bld_tools_model_provider
  - bld_tools_response_format
  - bld_collaboration_rate_limit_config
  - bld_instruction_rate_limit_config
  - bld_examples_rate_limit_config
---

# Tools: rate-limit-config-builder

This ISO encodes a rate limit policy -- throttle bounds, quota windows, and backoff behavior.
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing rate_limit_config artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, rate_limit_config kind |
| CEX Examples | P09_config/examples/ | Real rate_limit_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P09_rate_limit_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| Anthropic Docs | docs.anthropic.com/en/api/rate-limits | Live RPM/TPM values per tier |
| OpenAI Docs | platform.openai.com/docs/guides/rate-limits | Live RPM/TPM values per tier |
| LiteLLM Docs | docs.litellm.ai/docs/proxy/rate_limit | Proxy rate limit config reference |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern matches `^p09_rl_[a-z][a-z0-9_]+$`,
rpm and tpm are positive integers, all 4 body sections present, quality == null,
tags includes "rate_limit_config", body <= 1024 bytes.
## Provider Lookup Guide
When building for a known provider, verify limits from official docs before writing:
- Anthropic: API Console > Settings > Rate Limits shows live tier limits
- OpenAI: Platform > Usage > Rate Limits shows per-model limits by tier
- LiteLLM: proxy/config.yaml `router_settings` section defines limits
- Azure OpenAI: Azure Portal > Resource > Deployments > Rate Limits

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_function_def]] | sibling | 0.52 |
| [[rate-limit-config-builder]] | downstream | 0.47 |
| [[bld_tools_search_tool]] | sibling | 0.46 |
| [[bld_tools_batch_config]] | sibling | 0.46 |
| [[bld_knowledge_card_rate_limit_config]] | upstream | 0.46 |
| [[bld_tools_model_provider]] | sibling | 0.45 |
| [[bld_tools_response_format]] | sibling | 0.45 |
| [[bld_collaboration_rate_limit_config]] | downstream | 0.45 |
| [[bld_instruction_rate_limit_config]] | upstream | 0.44 |
| [[bld_examples_rate_limit_config]] | downstream | 0.44 |
