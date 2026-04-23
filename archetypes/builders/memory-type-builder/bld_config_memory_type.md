---
kind: config
id: bld_config_memory_type
pillar: P09
llm_function: CONSTRAIN
effort: medium
max_turns: 15
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: pillar
quality: 9.1
title: "Config Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_manifest_memory_type
  - bld_tools_memory_type
  - bld_collaboration_memory_type
  - bld_output_template_builder
  - bld_config_tagline
  - bld_collaboration_memory_scope
  - bld_output_template_signal
  - bld_tools_agent
  - bld_config_memory_scope
  - memory-scope-builder
---

# Config: memory_type

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_mt_{type_name}.md` → `.yaml` | `p10_mt_user.yaml` |
| Builder directory | kebab-case | `memory-type-builder/` |
| Frontmatter fields | snake_case | `observation_types`, `decay_rate` |

1. output_dir: P10_memory/compiled/
2. naming: p10_mt_{type_name}.md → p10_mt_{type_name}.yaml
3. max_bytes: 2048
4. machine_format: yaml
5. id == filename stem
6. One artifact per memory type (max 4 total)

## Metadata

```yaml
id: bld_config_memory_type
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-memory-type.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | memory type construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Builder Context

This ISO operates within the `memory-type-builder` stack, one of 125
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_manifest_memory_type]] | upstream | 0.72 |
| [[bld_tools_memory_type]] | upstream | 0.50 |
| [[bld_collaboration_memory_type]] | downstream | 0.47 |
| [[bld_output_template_builder]] | upstream | 0.41 |
| [[bld_config_tagline]] | sibling | 0.40 |
| [[bld_collaboration_memory_scope]] | downstream | 0.40 |
| [[bld_output_template_signal]] | upstream | 0.38 |
| [[bld_tools_agent]] | upstream | 0.37 |
| [[bld_config_memory_scope]] | sibling | 0.35 |
| [[memory-scope-builder]] | upstream | 0.32 |
