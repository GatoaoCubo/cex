---
kind: knowledge_card
id: bld_knowledge_card_compression_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for compression_config production — context compression strategies
sources: OpenAI context window research, Anthropic prompt engineering, LangChain memory modules, academic papers on conversation summarization
quality: 9.1
title: "Knowledge Card Compression Config"
version: "1.0.0"
author: n03_builder
tags: [compression_config, builder, examples]
tldr: "Golden and anti-examples for compression config construction, demonstrating ideal structure and common pitfalls."
domain: "compression config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_compression_config_builder
  - bld_examples_compression_config
  - p03_sp_compression_config_builder
  - bld_instruction_compression_config
  - p01_kc_compression_config
  - p10_cc_rolling_window_50pct
  - bld_config_compression_config
  - compression-config-builder
  - bld_output_template_compression_config
  - p11_qg_compression_config
---

# Domain Knowledge: compression_config
## Executive Summary
Compression configs define the token reduction contract for an LLM agent — specifying when compression triggers, what strategy executes, which message types are protected, and how priority decays with age. As context windows grow (128K-1M tokens), compression becomes less about survival and more about signal-to-noise: removing redundant or low-value context to improve reasoning quality and reduce cost. They differ from token budgets (how much to allocate), session backends (where to store), and memory configs (what to remember).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (memory) |
| llm_function | INJECT |
| Frontmatter fields | 16+ |
| Quality gates | 10 HARD + 12 SOFT |
| Strategy options | summarize, truncate_oldest, rolling_window, priority_keep, tiered |
| Trigger range | 0.50-0.99 (recommended: 0.80-0.90) |
| Naming | p10_cc_{name}.yaml |
## Patterns
- **Tiered compression pipeline**: execute stages in order of information loss
| Stage | Loss Level | Method | When |
|-------|-----------|--------|------|
| Semantic dedup | None | Remove near-duplicate messages | Always first |
| Summarize | Low-Medium | LLM condenses old messages | When dedup insufficient |
| Truncate oldest | Medium | Drop oldest low-priority messages | When summary insufficient |
| Hard drop | High | Remove all messages below threshold | Emergency only |
- **Priority-based preservation**: not all context is equal
| Priority | Message Types | Decay Rate |
|----------|--------------|------------|
| Critical (never compress) | system_prompt, tool_definition | 0.00 |
| High (compress last) | pinned, recent tool_result | 0.01-0.03 |
| Medium (compress when needed) | user messages, recent assistant | 0.03-0.08 |
| Low (compress first) | old assistant, old observations | 0.08-0.15 |
- **Rolling window**: keep last N tokens of conversation, discard earlier. Simple but loses important early context.
- **Semantic dedup**: detect and merge near-identical messages (e.g., repeated tool results with minor variations).
| Source | Concept | Application |
|--------|---------|-------------|
| OpenAI | Summarize-and-replace | Replace old messages with summary |
| Anthropic | Prompt caching | Preserve cached prefixes, compress suffix |
| LangChain | ConversationSummaryBufferMemory | Hybrid: summary + recent buffer |
| MemGPT | Tiered memory with paging | Move old context to "archival storage" |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| trigger_ratio < 0.50 | Premature compression — destroys useful context when window is half empty |
| Compressing system prompts | Agent loses identity, role, and constraints |
| Summarizing tool outputs | Summaries lose structured data (JSON, tables) needed for reasoning |
| No preserve_types | Structural messages (system prompt, tool defs) eligible for deletion |
| No decay weights | All message types treated equally — old system prompts same priority as old observations |
| Single strategy without fallback | If summarization fails or is insufficient, no backup plan |
| No min_context_tokens | Compression can collapse context to near-zero, leaving no room for conversation |
## Application
1. Identify target agent and model context window size
2. Catalog message types used in typical conversations
3. Assign priority and decay weight to each message type
4. Select strategy based on workload (tiered for production, rolling_window for simple agents)
5. Set trigger_ratio (0.80-0.90 recommended) and target_ratio (0.50-0.70)
6. Define preserve_types (system_prompt mandatory, tool_definition recommended)
7. Set min_context_tokens >= 2x system prompt token count
8. Test with real conversations to calibrate decay weights
## References
- MemGPT: Towards LLMs as Operating Systems (Packer et al., 2023)
- LangChain ConversationSummaryBufferMemory documentation
- Anthropic prompt engineering: managing long conversations
- OpenAI: best forctices for context window management

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_compression_config_builder]] | downstream | 0.53 |
| [[bld_examples_compression_config]] | downstream | 0.47 |
| [[p03_sp_compression_config_builder]] | downstream | 0.46 |
| [[bld_instruction_compression_config]] | downstream | 0.43 |
| [[p01_kc_compression_config]] | sibling | 0.40 |
| [[p10_cc_rolling_window_50pct]] | downstream | 0.35 |
| [[bld_config_compression_config]] | downstream | 0.33 |
| [[compression-config-builder]] | downstream | 0.33 |
| [[bld_output_template_compression_config]] | downstream | 0.30 |
| [[p11_qg_compression_config]] | downstream | 0.30 |
