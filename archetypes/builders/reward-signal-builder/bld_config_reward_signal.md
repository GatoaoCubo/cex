---
kind: config
id: bld_config_reward_signal
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Reward Signal"
version: "1.0.0"
author: n03_builder
tags: [reward_signal, builder, examples]
tldr: "Golden and anti-examples for reward signal construction, demonstrating ideal structure and common pitfalls."
domain: "reward signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_reward_signal
  - p03_sp_reward_signal_builder
  - bld_schema_reward_signal
  - bld_knowledge_card_reward_signal
  - bld_output_template_reward_signal
  - bld_config_llm_judge
  - bld_config_memory_scope
  - bld_architecture_reward_signal
  - bld_collaboration_reward_signal
  - p11_qg_reward_signal
---
# Config: reward_signal Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p11_reward_{scope}.md` | `p11_reward_response_quality.md` |
| Builder directory | kebab-case | `reward-signal-builder/` |
| Frontmatter fields | snake_case | `signal_type`, `baseline` |
| Signal slug | snake_case, lowercase, no hyphens | `response_quality`, `preference_helpfulness` |
| Criteria names | snake_case, noun or noun_phrase | `factual_accuracy`, `tone_alignment` |
| Scale string | hyphen-range or keyword | `"0-1"`, `"0-10"`, `"binary"`, `"-1_to_1"` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P11_feedback/examples/p11_reward_{scope}.md`
- Compiled: `cex/P11_feedback/compiled/p11_reward_{scope}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~3500 bytes
- Density: >= 0.80 (no filler)
## Signal Type Enum
| Value | When to use |
|-------|-------------|
| scalar | Single numeric score from LLM judge or regression model |
| preference | Binary choice between two outputs (A > B or B > A) |
| critique | LLM produces critique text + revised output + score |
| comparative | Ranked list of N outputs by quality |
| implicit | Inferred from behavioral signals (clicks, edits, time-on-task) |
## Scale Conventions
| Scale | Use case | Baseline guidance |
|-------|----------|-------------------|
| 0-1 | Normalized quality scores, probabilities | >= 0.7 |
| 0-10 | Human rating rubrics | >= 6.0 |
| binary | Pass/fail, approved/rejected | 1 (pass) |
| -1_to_1 | Sentiment, preference direction | >= 0.0 |
Rule: baseline MUST fall within declared scale range.
## Frequency Rules
| Value | Trigger |
|-------|---------|
| per_turn | After every LLM generation |
| per_task | After a multi-turn task complete |
| per_session | End-of-session rollup |
| on_demand | Human-triggered evaluation |
## Aggregation Rules
- mean: default for stable scalar signals
- weighted_mean: when criteria have unequal importance
- min: safety signals — weakest dimension gates overall quality
- max: capability discovery — track best achievable performance
- last: recency-weighted; use for fast-evolving signals

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_reward_signal]] | upstream | 0.38 |
| [[p03_sp_reward_signal_builder]] | downstream | 0.34 |
| [[bld_schema_reward_signal]] | downstream | 0.33 |
| [[bld_knowledge_card_reward_signal]] | upstream | 0.32 |
| [[bld_output_template_reward_signal]] | upstream | 0.32 |
| [[bld_config_llm_judge]] | sibling | 0.32 |
| [[bld_config_memory_scope]] | sibling | 0.30 |
| [[bld_architecture_reward_signal]] | upstream | 0.29 |
| [[bld_collaboration_reward_signal]] | downstream | 0.29 |
| [[p11_qg_reward_signal]] | downstream | 0.28 |
