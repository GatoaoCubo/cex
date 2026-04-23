---
kind: tools
id: bld_tools_model_provider
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for model_provider production
quality: 9.1
title: "Tools Model Provider"
version: "1.0.0"
author: n03_builder
tags: [model_provider, builder, examples]
tldr: "Golden and anti-examples for model provider construction, demonstrating ideal structure and common pitfalls."
domain: "model provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_model_card
  - bld_examples_model_provider
  - bld_tools_rate_limit_config
  - bld_tools_embedder_provider
  - bld_tools_batch_config
  - bld_examples_model_card
  - bld_tools_function_def
  - p03_sp_model_provider_builder
  - bld_tools_response_format
  - bld_knowledge_card_model_provider
---

# Tools: model-provider-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing model_provider configs in pool | Phase 1 (check duplicates) | CONDITIONAL |
| cex_router.py | Validate provider config against routing rules | Phase 3 (cross-check) | ACTIVE |
| cex_model_updater.py | Check model ID freshness and deprecation status | Phase 1 (verify models) | ACTIVE |
| cex_compile.py | Compile .md to .yaml | Phase 4 (post-save) | ACTIVE |
| validate_artifact.py | Validate any artifact kind via builder gates | Phase 3 | [PLANNED] |
## Data Sources (APIs and Docs)
| Source | URL | Data |
|--------|-----|------|
| Anthropic API | https://docs.anthropic.com/en/api | Claude API reference |
| Anthropic rate limits | https://docs.anthropic.com/en/api/rate-limits | RPM/TPM per tier |
| Anthropic models | https://docs.anthropic.com/en/docs/about-claude/models | Model list + specs |
| OpenAI API | https://platform.openai.com/docs/api-reference | GPT API reference |
| OpenAI rate limits | https://platform.openai.com/docs/guides/rate-limits | RPM/TPM per tier |
| OpenAI models | https://platform.openai.com/docs/models | Model list + deprecations |
| Google Gemini | https://ai.google.dev/gemini-api/docs | Gemini API reference |
| Google quotas | https://ai.google.dev/gemini-api/docs/quota | Rate limits |
| Ollama API | https://github.com/ollama/ollama/blob/main/docs/api.md | Local model API |
| Groq API | https://console.groq.com/docs | Groq inference API |
| LiteLLM | https://docs.litellm.ai/ | Multi-provider proxy |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation (until validate_artifact.py exists)
Manually check each QUALITY_GATES gate against produced artifact.
All 10 HARD gates must pass. SOFT gates contribute to score.
## Provider SDK Reference
| Provider | SDK | Install | Auth Header |
|----------|-----|---------|-------------|
| Anthropic | `anthropic` | `pip install anthropic` | x-api-key |
| OpenAI | `openai` | `pip install openai` | Authorization: Bearer |
| Google | `google-generativeai` | `pip install google-generativeai` | API key param |
| Ollama | `ollama` | `pip install ollama` | None (local) |
| Groq | `groq` | `pip install groq` | Authorization: Bearer |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_model_card]] | sibling | 0.62 |
| [[bld_examples_model_provider]] | downstream | 0.53 |
| [[bld_tools_rate_limit_config]] | sibling | 0.44 |
| [[bld_tools_embedder_provider]] | sibling | 0.42 |
| [[bld_tools_batch_config]] | sibling | 0.38 |
| [[bld_examples_model_card]] | downstream | 0.37 |
| [[bld_tools_function_def]] | sibling | 0.36 |
| [[p03_sp_model_provider_builder]] | upstream | 0.36 |
| [[bld_tools_response_format]] | sibling | 0.36 |
| [[bld_knowledge_card_model_provider]] | upstream | 0.36 |
