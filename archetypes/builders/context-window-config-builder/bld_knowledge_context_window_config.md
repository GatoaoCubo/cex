---
kind: knowledge_card
id: bld_knowledge_card_context_window_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for context_window_config production
sources: kc_context_window_config.md, provider documentation, cex_token_budget.py
quality: 9.0
title: "Knowledge Card Context Window Config"
version: "1.0.0"
author: n03_builder
tags: [context_window_config, builder, examples]
tldr: "Golden and anti-examples for context window config construction, demonstrating ideal structure and common pitfalls."
domain: "context window config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_context_window_config
  - p03_sp_context_window_config_builder
  - context-window-config-builder
  - p10_lr_context_window_config_builder
  - bld_collaboration_context_window_config
  - bld_collaboration_model_card
  - p01_kc_model_card
  - bld_instruction_context_window_config
  - p11_qg_context_window_config
  - bld_memory_model_provider
---

# Domain Knowledge: context_window_config
## Executive Summary
Context window configs allocate token budgets across prompt sections within a model's finite context limit. They define per-section budgets, priority tiers for overflow truncation, and compression fallbacks. Critical for RAG pipelines, multi-agent systems, and any prompt assembly exceeding 50% of model capacity.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 (Prompt) |
| LLM Function | CONSTRAIN |
| Max bytes | 2048 |
| Naming | p03_cwc_{model}.yaml |
| Core | true |
| Default split | system 10%, examples 15%, context 40%, query 5%, output 30% |
## Key Model Limits
| Model | Context | Default Output |
|-------|---------|---------------|
| Claude Opus/Sonnet | 200K | 8K (configurable) |
| Claude Opus (extended) | 1M | 64K |
| GPT-4o | 128K | 16K |
| Gemini 1.5 Pro | 2M | 8K |
## Patterns
- **Fixed allocation**: Predictable prompts — fixed budgets per section
- **Dynamic scaling**: RAG pipelines — context gets remaining after fixed sections
- **Priority truncation**: Drop lowest-priority tier first on overflow
- **Compression fallback**: Summarize retrieved context when truncation insufficient
- **Model profiles**: Different configs per model, selected at runtime
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No output reserve | Model truncates mid-response |
| Equal budgets | Wastes capacity, ignores priority |
| Ignore model limit | 300K prompt for 128K model |
| Static for dynamic | Fixed 8K for variable RAG (2-20K) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_context_window_config]] | sibling | 0.52 |
| [[p03_sp_context_window_config_builder]] | downstream | 0.38 |
| [[context-window-config-builder]] | downstream | 0.37 |
| [[p10_lr_context_window_config_builder]] | downstream | 0.33 |
| [[bld_collaboration_context_window_config]] | downstream | 0.31 |
| [[bld_collaboration_model_card]] | downstream | 0.30 |
| [[p01_kc_model_card]] | sibling | 0.28 |
| [[bld_instruction_context_window_config]] | downstream | 0.25 |
| [[p11_qg_context_window_config]] | downstream | 0.25 |
| [[bld_memory_model_provider]] | downstream | 0.25 |
