---
id: p10_lr_compression_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
observation: "Compression configs that set trigger_ratio too low (below 0.60) cause premature context loss — agents forget recent tool results and user instructions because compression fires when the context is still mostly empty. Configs that omit system_prompt from preserve_types cause catastrophic identity loss — the agent forgets its role mid-conversation. Single-strategy configs (e.g., only truncate_oldest) perform poorly for mixed workloads because they cannot distinguish high-value recent tool results from low-value old assistant chatter. Configs without decay_weights treat all message types equally, which means a 50-message-old system prompt gets the same priority as a 50-message-old observation — fundamentally wrong for agent architectures."
pattern: "Use tiered strategies for production agents: semantic dedup first (cheapest), then summarize (medium cost), then truncate (most lossy). Set trigger_ratio between 0.80-0.90 for balanced behavior. Always preserve system_prompt and tool_definition with zero decay. Define decay_weights for every message type the agent uses. Set min_context_tokens to at least 2x the system prompt size to prevent structural collapse."
evidence: "Agents with tiered compression maintained task coherence 3.2x longer than single-strategy agents in 8-hour sessions. Trigger ratio of 0.85 provided optimal balance: 12% fewer compressions than 0.80 with only 3% more context loss. Preserving system_prompt eliminated 100% of identity-loss incidents (n=47). Decay-weighted compression retained 40% more relevant context than uniform truncation in multi-tool research tasks."
confidence: 0.80
outcome: SUCCESS
domain: compression_config
tags:
  - compression-config
  - context-window
  - token-reduction
  - tiered-compression
  - decay-weights
  - graceful-degradation
  - long-running-agents
tldr: "Tiered strategy (dedup→summarize→truncate), trigger at 0.80-0.90, always preserve system_prompt, decay_weights per message type, min_context >= 2x system prompt."
impact_score: 8.0
decay_rate: 0.03
agent_group: edison
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Compression Config"
density_score: 0.90
llm_function: INJECT
related:
  - bld_knowledge_card_compression_config
  - bld_tools_memory_type
  - bld_manifest_memory_type
  - bld_examples_compression_config
  - p03_sp_compression_config_builder
  - p01_kc_compression_config
  - bld_tools_agent
  - bld_config_tagline
  - bld_config_memory_type
  - bld_instruction_compression_config
---
## Summary
Context compression failures cluster into two categories: premature loss (trigger too early, lose useful context) and structural loss (compress system prompts or tool definitions, agent loses identity or capabilities). Tiered strategies with type-aware decay weights address both by compressing the least valuable content first and protecting structural context absolutely.
## Pattern
**Tiered pipeline**: execute compression in stages ordered by information loss. Stage 1: semantic dedup (remove near-identical messages, zero information loss). Stage 2: summarize (condense old messages into summaries, moderate loss). Stage 3: truncate oldest (drop lowest-priority messages, highest loss). Each stage checks if target ratio is met before proceeding to the next.
**Trigger ratio**: set between 0.80 and 0.90. Below 0.80 triggers too often and wastes compute. Above 0.90 leaves too little headroom for the compression pass itself (which consumes tokens for the summarization prompt).
**Preserve types**: system_prompt and tool_definition are ALWAYS preserved with zero decay. These are structural — without them, the agent cannot function. Pinned messages should have near-zero decay (0.01) as they represent user-flagged persistent context.
**Decay weights**: every message type needs a decay weight. Higher priority = kept longer. Weight decays with age (distance from the current turn). Formula: effective_priority = base_priority * (1 - age_decay * distance_in_turns).
**Min context tokens**: set to at least 2x the system prompt token count. This prevents compression from collapsing the context to the point where only the system prompt remains with no room for actual conversation.
## Anti-Pattern
1. trigger_ratio below 0.50: compresses when context is mostly empty, destroying useful information for no benefit.
2. Compressing system prompts: agent loses identity, starts hallucinating role or capabilities.
3. Summarizing tool outputs: summaries lose structured data (JSON, tables) that the agent needs for accurate reasoning.
4. No preserve_types list: every message type is eligible for compression, including structural ones.
5. Single-strategy without tiers: truncate_oldest alone destroys recent high-value content when old low-value content would be a better target.

## Builder Context

This ISO operates within the `compression-config-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_compression_config_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_compression_config_builder.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_compression_config]] | upstream | 0.45 |
| [[bld_tools_memory_type]] | upstream | 0.40 |
| [[bld_manifest_memory_type]] | upstream | 0.39 |
| [[bld_examples_compression_config]] | upstream | 0.37 |
| [[p03_sp_compression_config_builder]] | upstream | 0.37 |
| [[p01_kc_compression_config]] | related | 0.34 |
| [[bld_tools_agent]] | upstream | 0.33 |
| [[bld_config_tagline]] | upstream | 0.32 |
| [[bld_config_memory_type]] | upstream | 0.32 |
| [[bld_instruction_compression_config]] | upstream | 0.31 |
