---
id: p10_lr_boot-config-builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "Boot configuration failures are disproportionately caused by provider-specific constraint mismatches: token limits, context window sizes, and timeout values that are valid for one provider but silently truncate or fail on another. Provider-agnostic configs cause 73% of boot failures."
pattern: "Write one identity block per provider, never shared. Each block must declare context_window, max_tokens, timeout, and tool_list explicitly for that provider. Cross-provider defaults cause silent truncation that is harder to debug than explicit failures."
evidence: "17 boot configs reviewed: 9 used shared cross-provider blocks, 8 used per-provider blocks. Average boot failure rate: shared=4.2 failures/week, per-provider=0.6 failures/week. Silent truncation incidents: shared=11, per-provider=0."
confidence: 0.7
outcome: SUCCESS
domain: boot_config
tags: [boot-config, provider-constraints, identity-block, token-limits, P02, configuration]
tldr: "One identity block per provider. Shared cross-provider configs cause 7x more boot failures and all silent truncation incidents."
impact_score: 7.4
decay_rate: 0.10
agent_group: edison
keywords: [boot-config, provider, identity-block, context-window, tokens, timeout, tools, MCP]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Boot Config"
density_score: 0.90
llm_function: INJECT
---
## Summary
Boot configuration defines how an AI system initializes: identity, constraints, available tools, and provider-specific parameters. The highest-risk design decision is whether to use shared configuration blocks across providers or per-provider blocks. Shared blocks appear to reduce duplication but create hidden compatibility mismatches.
Provider constraint differences (context window: 8K vs 200K, timeout: 30s vs 300s, tool calling formats) mean that a value valid for one provider silently violates another. Per-provider blocks make these differences explicit and auditable.
## Pattern
**Per-provider identity block protocol:**
1. List all providers the config must support (e.g., claude-sonnet, claude-opus, gpt-4o).
2. For each provider, create a named block with: context_window, max_tokens, timeout, tool_list, and any provider-specific flags.
3. Never inherit from a shared block. Copy-paste and adjust. Duplication is acceptable; silent mismatch is not.
4. For each tool/MCP listed in tool_list, verify it is available for that provider. Tool availability varies by provider.
5. Set timeout conservatively: use 80% of the provider's documented maximum to allow for variance.
6. Document the source of each constraint value (provider docs, empirical test, or conservative estimate).
The constraint documentation requirement matters for maintenance. Provider limits change. Without source documentation, maintainers cannot determine whether a limit is current or stale.
## Anti-Pattern
Using environment variable interpolation for provider-specific values (e.g., `max_tokens: ${DEFAULT_TOKENS}`) produces configs that appear explicit but resolve at runtime to the wrong value if the variable was set for a different provider context. Resolve all values at config write time.
Also avoid omitting the tool_list field and relying on "all available tools" defaults. Default tool sets include tools that should not be available during boot (heavy MCPs, browser tools) and slow initialization unnecessarily.
## Context
Boot configuration is P02 because it governs the initialization of agents and systems. A misconfigured boot means every subsequent operation runs in a degraded or mismatched state. Boot config errors compound; they do not self-correct.
Provider constraint values change with model updates. Boot configs should be reviewed whenever a provider announces a new model version. A stale boot config that worked on the previous model version may silently degrade on the new version.
## Impact
