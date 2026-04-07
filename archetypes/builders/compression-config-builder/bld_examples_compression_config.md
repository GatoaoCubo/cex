---
kind: examples
id: bld_examples_compression_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of compression_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Compression Config"
version: "1.0.0"
author: n03_builder
tags: [compression_config, builder, examples]
tldr: "Golden and anti-examples for compression config construction, demonstrating ideal structure and common pitfalls."
domain: "compression config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: compression-config-builder
## Golden Example
INPUT: "Define a balanced compression strategy for a long-running research agent"
OUTPUT:
```yaml
id: p10_cc_balanced_research
kind: compression_config
pillar: P10
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "builder_agent"
strategy: tiered
trigger_ratio: 0.85
preserve_types:
  - system_prompt
  - tool_definition
  - pinned
max_summary_tokens: 2048
min_context_tokens: 4096
decay_weights:
  system_prompt: 1.0
  tool_definition: 1.0
  pinned: 0.95
  tool_result: 0.80
  user: 0.70
  assistant: 0.50
  observation: 0.40
target_ratio: 0.60
quality: 8.9
tags: [compression_config, research, tiered, P10, balanced]
tldr: "Tiered compression at 85% trigger: preserve system+tools, summarize then truncate oldest, target 60%"
description: "Balanced compression for research agents with large context needs and frequent tool use"
scope: "research_agent"
tier_count: 3
```
## Strategy Specification
Tiered 3-stage compression for research agents that accumulate large context through
iterative tool calls. Triggers at 85% context utilization. Target: reduce to 60%.
Stage order: semantic dedup → summarize old assistant messages → truncate oldest observations.
## Preserve Types
- system_prompt: structural identity — never compressed
- tool_definition: function schemas required for tool calls — never compressed
- pinned: user-flagged messages with persistent relevance — never compressed
## Decay Weights
| Message Type | Base Priority | Age Decay (per 1K tokens of distance) | Rationale |
|-------------|--------------|---------------------------------------|-----------|
| system_prompt | 1.00 | 0.00 (no decay) | Structural — always relevant |
| tool_definition | 1.00 | 0.00 (no decay) | Required for function calling |
| pinned | 0.95 | 0.01 | User-flagged, slow decay |
| tool_result | 0.80 | 0.05 | Recent results critical, old results less so |
| user | 0.70 | 0.03 | User messages provide task context |
| assistant | 0.50 | 0.08 | Responses can be reconstructed from context |
| observation | 0.40 | 0.10 | Superseded by newer observations |
## Compression Pipeline
1. **Semantic Dedup** (target: -10%): remove near-duplicate assistant responses and repeated observations
2. **Summarize** (target: -15%): condense assistant messages older than 4K tokens into summaries (max 2048 tokens)
3. **Truncate Oldest** (target: remaining): drop lowest-priority messages by decay_weight * age_factor until target_ratio reached
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p10_cc_ pattern (H02 pass)
- kind: compression_config (H04 pass)
- All 6 core fields present: strategy, trigger_ratio, preserve_types, max_summary_tokens, min_context_tokens, decay_weights (H06 pass)
- preserve_types includes system_prompt (H07 pass)
- trigger_ratio 0.85 within 0.50-0.99 (H08 pass)
- strategy "tiered" is valid enum (H09 pass)
- Pipeline ordered least-lossy to most-lossy
- Decay weights cover all 7 message types with rationale
## Anti-Example
INPUT: "Create compression config for chat agent"
BAD OUTPUT:
```yaml
id: chat-compression
kind: compression
pillar: memory
strategy: delete_all
trigger_ratio: 0.30
preserve_types: []
quality: 8.5
tags: [compression]
```
Just delete old messages when context is full.
FAILURES:
1. id: "chat-compression" uses hyphens and no `p10_cc_` prefix -> H02 FAIL
2. kind: "compression" not "compression_config" -> H04 FAIL
3. pillar: "memory" not "P10" -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. strategy: "delete_all" not a valid enum -> H09 FAIL
6. trigger_ratio: 0.30 below minimum 0.50 -> H08 FAIL
7. preserve_types: empty list, missing system_prompt -> H07 FAIL
8. Missing fields: max_summary_tokens, min_context_tokens, decay_weights, version, created, author -> H06 FAIL
9. tags: only 1 item, missing "compression_config" -> S02 FAIL
10. Body missing Strategy Specification, Preserve Types, Decay Weights, Compression Pipeline -> structural FAIL
11. No decay weights defined -> S03 FAIL
