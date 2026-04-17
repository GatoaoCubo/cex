---
kind: architecture
id: bld_architecture_compression_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of compression_config — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Compression Config"
version: "1.0.0"
author: n03_builder
tags: [compression_config, builder, examples]
tldr: "Golden and anti-examples for compression config construction, demonstrating ideal structure and common pitfalls."
domain: "compression config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| strategy | Primary compression approach: summarize, truncate_oldest, rolling_window, priority_keep, tiered | compression-config-builder | required |
| trigger_ratio | Context fullness threshold (0.50-0.99) that activates compression | compression-config-builder | required |
| preserve_types | Message types never compressed: system_prompt, tool_definition, pinned | compression-config-builder | required |
| max_summary_tokens | Maximum token count for summarized content after compression | compression-config-builder | required |
| min_context_tokens | Minimum tokens that must remain after compression (floor) | compression-config-builder | required |
| decay_weights | Priority multipliers per message type, decayed by age | compression-config-builder | required |
| compression_pipeline | Ordered list of compression stages for tiered strategy | compression-config-builder | conditional |
| target_ratio | Desired context utilization after compression (e.g., 0.60) | compression-config-builder | recommended |
| metadata | config id, version, pillar, scope, author, created date | compression-config-builder | required |
## Dependency Graph
```
token_budget (P10) --feeds--> compression_config (provides total budget that triggers compression)
compression_config --consumed_by--> cex_token_budget.py (reads trigger_ratio to decide when to compress)
compression_config --consumed_by--> cex_memory_types.py (reads preserve_types to protect typed memories)
compression_config --consumed_by--> p04_skill_compact (Wire 6) (uses strategy and decay_weights)
compression_config --consumed_by--> cex_crew_runner.py (applies compression before prompt assembly)
session_backend (P10) --independent-- compression_config (session_backend persists state; compression reduces it)
memory_config (P10) --independent-- compression_config (memory_config defines what to remember; compression defines what to drop)
prompt_template (P05) --independent-- compression_config (prompt_template structures output; compression reduces input)
```
| From | To | Type | Data |
|------|----|------|------|
| token_budget | compression_config | feeds | total token budget, per-section allocations |
| compression_config | cex_token_budget.py | consumed_by | trigger_ratio, min_context_tokens |
| compression_config | cex_memory_types.py | consumed_by | preserve_types, decay_weights per memory type |
| compression_config | p04_skill_compact | consumed_by | strategy, pipeline stages, max_summary_tokens |
| compression_config | cex_crew_runner.py | consumed_by | full config for pre-assembly compression |
## Boundary Table
| compression_config IS | compression_config IS NOT |
|----------------------|---------------------------|
| A specification of HOW to reduce context tokens when budget is reached | A token_budget (P10) — token_budget allocates HOW MANY tokens per section |
| Covers strategy selection, trigger thresholds, and preservation rules | A session_backend (P10) — session_backend persists WHERE state is stored |
| Follows graceful degradation: preserve critical, summarize medium, drop low | A memory config (P10) — memory config defines WHAT to remember long-term |
| Declares preserve_types that are structurally immune to compression | A prompt_template (P05) — prompt_template defines output structure |
| Specifies decay weights for age-based priority scoring | A runtime_rule (P09) — runtime_rule governs timeouts and retries |
| Defines tiered pipelines with ordered compression stages | A feature_flag (P09) — feature_flag is an on/off toggle |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Trigger | trigger_ratio, min_context_tokens | Detect when compression is needed |
| Strategy | strategy, compression_pipeline | Define how compression executes |
| Preservation | preserve_types, decay_weights | Protect critical context from loss |
| Accounting | max_summary_tokens, target_ratio | Measure compression effectiveness |
