---
id: p10_lr_hook_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: builder_agent
observation: "hook_config artifacts must declare hooks, not implement them. Mixing declaration with implementation causes tight coupling and breaks the 8F pipeline."
pattern: "Declare all hooks with phase, event, action, and condition. Validate against SCHEMA.md. Keep body under 4096 bytes."
evidence: "Pattern extracted from pre-commit hooks, GitHub Actions event triggers, Webpack plugin lifecycle, and 8F pipeline phase transitions."
confidence: 0.7
outcome: SUCCESS
domain: hook_config
tags: [hook-config, P04, type-builder]
tldr: "Declare hooks, never implement. Validate against schema. Stay under 4096 bytes."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [hook config, pre-build, post-build, on-error, quality-fail, lifecycle, event]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Hook Config"
density_score: 0.90
llm_function: INJECT
related:
  - bld_knowledge_card_hook_config
  - p03_sp_hook_config_builder
  - bld_instruction_hook_config
  - bld_examples_hook_config
  - hook-config-builder
  - p01_kc_hook_config
  - bld_architecture_hook_config
  - p11_qg_hook_config
  - bld_collaboration_hook_config
  - bld_collaboration_hook
---
## Summary
Hook lifecycle configuration — declares which hooks fire at each build phase. The difference between a useful hook_config and a useless one is clean declaration
with conditions versus embedded implementation code.
## Pattern
**Declaration with conditions.**
Every hook must have: phase, event, action, and condition.
Required body sections: Overview, Hooks, Lifecycle, Integration.
Body budget: 4096 bytes max.
## Anti-Pattern
1. Embedding implementation: hook_config declares WHAT fires; hook implements HOW it runs
2. Missing conditions: Hooks without conditions fire unconditionally, causing noise
3. Phase mismatch: Declaring post-build hooks in pre-build phase breaks execution order
4. Overlapping events: Multiple hooks on same event without priority causes race conditions
## Context
The 4096-byte body limit keeps hook_config artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.

## Metadata

```yaml
id: p10_lr_hook_config_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-hook-config-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | hook_config |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_hook_config]] | upstream | 0.58 |
| [[p03_sp_hook_config_builder]] | upstream | 0.53 |
| [[bld_instruction_hook_config]] | upstream | 0.52 |
| [[bld_examples_hook_config]] | upstream | 0.51 |
| [[hook-config-builder]] | upstream | 0.49 |
| [[p01_kc_hook_config]] | upstream | 0.49 |
| [[bld_architecture_hook_config]] | upstream | 0.47 |
| [[p11_qg_hook_config]] | downstream | 0.42 |
| [[bld_collaboration_hook_config]] | downstream | 0.41 |
| [[bld_collaboration_hook]] | downstream | 0.35 |
