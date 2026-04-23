---
kind: instruction
id: bld_instruction_compression_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for compression_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Compression Config"
version: "1.0.0"
author: n03_builder
tags: [compression_config, builder, examples]
tldr: "Golden and anti-examples for compression config construction, demonstrating ideal structure and common pitfalls."
domain: "compression config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_memory_scope
  - bld_instruction_retriever_config
  - bld_instruction_chunk_strategy
  - bld_instruction_output_validator
  - bld_instruction_context_doc
  - bld_instruction_session_backend
  - bld_instruction_trace_config
  - p03_sp_compression_config_builder
  - bld_instruction_handoff_protocol
  - bld_instruction_prompt_version
---

# Instructions: How to Produce a compression_config
## Phase 1: RESEARCH
1. Identify the target agent or scope: which agent or system component needs compression?
2. Determine the context window size and model token limit for the target
3. Catalog the message types present in typical conversations: system_prompt, user, assistant, tool_call, tool_result, pinned, observation
4. Classify each message type by priority: critical (never compress), high (compress last), medium (compress when needed), low (compress first)
5. Determine the trigger ratio: at what percentage of token budget should compression activate? (recommended: 0.80-0.90)
6. Select primary strategy: summarize (semantic), truncate_oldest (positional), rolling_window (sliding), priority_keep (weighted), or tiered (multi-stage)
7. Define decay weights: how quickly does each message type lose priority as it ages?
8. Check existing compression_configs via brain_query [IF MCP] for the same scope — do not duplicate
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` — never self-score
4. Write **Strategy Specification** section: primary strategy, trigger ratio, target ratio after compression
5. Write **Preserve Types** section: list of message types that are never compressed, with rationale
6. Write **Decay Weights** section: table mapping message types to priority multipliers and age decay curves
7. Write **Compression Pipeline** section: ordered stages from least lossy to most lossy
8. Write **Token Accounting** section: how tokens are counted, what counts toward the budget, overhead estimates
9. Confirm body <= 4096 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p10_cc_[a-z][a-z0-9_]+$`
4. Confirm strategy is one of: summarize, truncate_oldest, rolling_window, priority_keep, tiered
5. Confirm trigger_ratio is between 0.50 and 0.99
6. Confirm preserve_types includes at minimum: system_prompt
7. Confirm decay_weights are defined for at least 3 message types
8. Confirm `quality` is null
9. Confirm body <= 4096 bytes
10. Cross-check: is this a compression strategy? If this is a token allocation it belongs in `token_budget`. If this is state persistence it belongs in `session_backend`. If this is long-term memory it belongs in memory config. This artifact specifies HOW to compress, not HOW MUCH to allocate or WHERE to store.
11. If score < 8.0: revise in the same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify compression
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | compression config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_memory_scope]] | sibling | 0.45 |
| [[bld_instruction_retriever_config]] | sibling | 0.44 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.42 |
| [[bld_instruction_output_validator]] | sibling | 0.42 |
| [[bld_instruction_context_doc]] | sibling | 0.42 |
| [[bld_instruction_session_backend]] | sibling | 0.41 |
| [[bld_instruction_trace_config]] | sibling | 0.41 |
| [[p03_sp_compression_config_builder]] | related | 0.41 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.41 |
| [[bld_instruction_prompt_version]] | sibling | 0.40 |
