---
kind: config
id: bld_config_signal
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
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
quality: 9.1
title: "Config Signal"
version: "1.0.0"
author: n03_builder
tags: [signal, builder, examples]
tldr: "Golden and anti-examples for signal construction, demonstrating ideal structure and common pitfalls."
domain: "signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_examples_signal
  - bld_knowledge_card_signal
  - bld_output_template_signal
  - p03_sp_signal_builder
  - p03_ins_signal_builder
  - signal-builder
  - bld_config_session_state
  - bld_schema_signal
  - bld_config_dispatch_rule
  - bld_tools_signal
---
# Config: signal Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p12_sig_{event}.json` | `p12_sig_agent_group_complete.json` |
| Builder directory | kebab-case | `signal-builder/` |
| Payload fields | snake_case | `quality_score`, `commit_hash` |
| Status values | lowercase enum | `complete`, `error`, `progress` |
| Agent_group values | lowercase slug | `codex`, `edison`, `atlas` |
Rule: use `.json` only for this builder.
## File Paths
1. Output: `cex/P12_orchestration/compiled/p12_sig_{event}.json`
2. Human reference: `cex/P12_orchestration/examples/p12_sig_{event}.md`
## Size Limits
1. Preferred payload size: <= 1024 bytes
2. Absolute max: 4096 bytes
3. Optional fields should remain sparse and compact
## Payload Restrictions
1. Required fields must appear exactly as defined in SCHEMA.md
2. Omit optional null/unknown fields instead of writing placeholders
3. `progress_pct` allowed only when `status=progress`
4. `artifacts_count` should match `artifacts` length when both exist
5. `quality_score` must stay numeric; never quote it as text
## Boundary Restrictions
1. No markdown, prose sections, or frontmatter inside the JSON payload
2. No task lists, scope fences, or commit instructions
3. No routing tables, keywords arrays for dispatch, or model selection logic

## Metadata

```yaml
id: bld_config_signal
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-signal.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | signal construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_signal]] | upstream | 0.47 |
| [[bld_knowledge_card_signal]] | downstream | 0.43 |
| [[bld_output_template_signal]] | upstream | 0.41 |
| [[p03_sp_signal_builder]] | upstream | 0.39 |
| [[p03_ins_signal_builder]] | upstream | 0.39 |
| [[signal-builder]] | downstream | 0.37 |
| [[bld_config_session_state]] | sibling | 0.35 |
| [[bld_schema_signal]] | upstream | 0.34 |
| [[bld_config_dispatch_rule]] | sibling | 0.34 |
| [[bld_tools_signal]] | upstream | 0.34 |
