---
kind: config
id: bld_config_memory_summary
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
title: "Config Memory Summary"
version: "1.0.0"
author: n03_builder
tags: [memory_summary, builder, examples]
tldr: "Golden and anti-examples for memory summary construction, demonstrating ideal structure and common pitfalls."
domain: "memory summary construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_memory_scope
  - bld_collaboration_memory_summary
  - memory-summary-builder
  - p10_lr_memory_summary_builder
  - bld_knowledge_card_memory_summary
  - p03_sp_memory_summary_builder
  - bld_instruction_memory_summary
  - p01_kc_memory_summary
  - bld_knowledge_card_memory_scope
  - bld_examples_memory_summary
---
# Config: memory_summary Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_summary_{scope}.md` | `p10_summary_session_onboarding.md` |
| Builder directory | kebab-case | `memory-summary-builder/` |
| Frontmatter fields | snake_case | `source_type`, `compression_method` |
| Summary slug | snake_case, lowercase, no hyphens | `session_onboarding`, `conv_support_q3` |
| Scope names | snake_case, descriptive | `session_build_sprint`, `conv_debug_auth` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P10_memory/examples/p10_summary_{scope}.md`
- Compiled: `cex/P10_memory/compiled/p10_summary_{scope}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4096 bytes
- Density: >= 0.80 (no filler)
## Source Type Enum
| Value | When to use |
|-------|-------------|
| conversation | Single conversation thread (one user + one agent turn sequence) |
| session | Full session with multiple conversations or tool uses |
| multi_session | Spans multiple sessions — cross-session memory compression |
| document | Non-conversational text (docs, notes, knowledge cards) |
## Compression Method Enum
| Value | Description | Best for |
|-------|-------------|----------|
| abstractive | LLM rewrites in compressed form — may lose literal phrasing | Long conversations, high compression ratios |
| extractive | Key sentences lifted verbatim — preserves exact wording | Short windows, precision-critical content |
| hybrid | Abstractive for narrative + extractive for decisions/facts | General purpose sessions |
| sliding_window | Rolling buffer with oldest content summarized first | Continuous long-running conversations |
## Freshness Decay Rules
| Range | Interpretation |
|-------|---------------|
| 0.0 | No decay — summary stays equally weighted forever |
| 0.01-0.05 | Slow decay — long-lived reference summaries |
| 0.06-0.15 | Moderate decay — typical session memory |
| 0.16-0.30 | Fast decay — ephemeral or context-specific summaries |
| > 0.30 | Very fast — treat as near-disposable cache |
Rule: freshness_decay must be a float in [0, 1]. Default 0.1.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_memory_scope]] | sibling | 0.35 |
| [[bld_collaboration_memory_summary]] | downstream | 0.35 |
| [[memory-summary-builder]] | downstream | 0.33 |
| [[p10_lr_memory_summary_builder]] | downstream | 0.31 |
| [[bld_knowledge_card_memory_summary]] | upstream | 0.30 |
| [[p03_sp_memory_summary_builder]] | downstream | 0.29 |
| [[bld_instruction_memory_summary]] | upstream | 0.29 |
| [[p01_kc_memory_summary]] | downstream | 0.27 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.27 |
| [[bld_examples_memory_summary]] | upstream | 0.27 |
