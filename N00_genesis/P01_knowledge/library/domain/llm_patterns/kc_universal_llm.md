---
id: p01_kc_universal_llm
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Universal LLM Patterns — Provider-Agnostic Design"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: llm_patterns
quality: 9.0
tags: [universal, provider-agnostic, claude, gpt, gemini, llama]
tldr: "Design for any LLM: use text in/out as primitive, structured output as JSON, tool use via MCP, avoid provider-specific features as core dependencies."
when_to_use: "Building systems that must work across Claude, GPT, Gemini, Llama, or future models"
keywords: [universal, provider-agnostic, portability, abstraction, llm-interface]
density_score: 0.93
updated: "2026-04-07"
related:
  - p01_kc_tool_use
  - p01_kc_caching
  - p01_kc_schema_validation
  - p01_kc_claude_md_patterns
  - bld_examples_model_provider
  - spec_cex_system_map
  - bld_config_fallback_chain
  - p01_kc_test_automation
  - p02_mc_google_gemini_2_5_pro
  - p03_sp_model_provider_builder
---

# Universal LLM Patterns

## The Primitive
Every LLM accepts text → produces text. Build on this, not on provider-specific APIs.

## Universal Capabilities (all major LLMs)

| Capability | Claude | GPT | Gemini | Llama |
|-----------|--------|-----|--------|-------|
| Text generation | ✅ | ✅ | ✅ | ✅ |
| System prompts | ✅ | ✅ | ✅ | ✅ |
| JSON output | ✅ | ✅ | ✅ | ✅ |
| Tool/function calls | ✅ | ✅ | ✅ | ✅* |
| Image input | ✅ | ✅ | ✅ | ✅* |
| Streaming | ✅ | ✅ | ✅ | ✅ |

*Depends on hosting platform

## Provider-Specific (avoid as core dependency)

| Feature | Provider | Portable Alternative |
|---------|----------|---------------------|
| Artifacts | Claude | Write to file |
| Prompt caching | Claude | External cache |
| Batch API | GPT | Sequential + cache |
| Code execution | GPT | Local subprocess |
| Grounding | Gemini | MCP fetch + search |

## CEX Design Principle
- `claude -p` subprocess = portable (swap for `gemini`, `llm`, etc.)
- Prompts are text files (.md) = any LLM can read them
- No `import anthropic` in tools = zero SDK dependency
- MCP = universal tool interface

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_universal_llm`
- **Tags**: [universal, provider-agnostic, claude, gpt, gemini, llama]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_tool_use]] | sibling | 0.29 |
| [[p01_kc_caching]] | sibling | 0.28 |
| [[p01_kc_schema_validation]] | sibling | 0.25 |
| [[p01_kc_claude_md_patterns]] | sibling | 0.25 |
| [[bld_examples_model_provider]] | downstream | 0.24 |
| [[spec_cex_system_map]] | related | 0.23 |
| [[bld_config_fallback_chain]] | downstream | 0.23 |
| [[p01_kc_test_automation]] | sibling | 0.23 |
| [[p02_mc_google_gemini_2_5_pro]] | downstream | 0.22 |
| [[p03_sp_model_provider_builder]] | downstream | 0.22 |
