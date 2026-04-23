---
kind: config
id: bld_config_builder
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints for the meta-builder
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: high
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: global
quality: 9.1
title: "Config Builder"
version: "1.0.0"
author: n03_builder
tags: [_builder, builder, examples]
tldr: "Golden and anti-examples for _builder construction, demonstrating ideal structure and common pitfalls."
domain: "_builder construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - _builder-builder
  - bld_config_kind
  - bld_architecture_kind
  - bld_collaboration_builder
  - kind-builder
  - bld_output_template_builder
  - bld_architecture_builder
  - bld_knowledge_card_builder
  - bld_examples_builder
  - bld_knowledge_card_kind
---
# Config: _builder-builder Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Meta-templates | `bld_meta_{iso_type}_builder.md` | `bld_meta_manifest_builder.md` |
| Builder directory | kebab-case + `-builder` suffix | `agent-builder/` |
| Frontmatter fields | snake_case | `llm_function`, `file_position` |
| builder specs | `bld_{iso_type}_{kind}.md` | `bld_manifest_agent.md` |

Rule: id MUST equal filename stem.
Rule: Every builder directory MUST contain exactly 13 builder spec files.

## File Paths
1. Output: `archetypes/builders/{kind}-builder/bld_{iso}_{kind}.md`
2. Meta-templates: `archetypes/builders/_builder-builder/bld_meta_{iso}_builder.md`

## Size Limits
1. Standard ISOs: max 4096 bytes
2. Instruction ISOs: max 6144 bytes
3. Meta-templates: max 6144 bytes (include comments/examples)
4. Density: >= 0.85

## Builder Generation Constraints
1. MUST generate all 13 builder specs per builder (manifest, instruction, config, memory, tools, collaboration, architecture, schema, output_template, examples, quality_gate, knowledge_card, system_prompt)
2. MUST include universal fields in generated ISOs (keywords, triggers, capabilities in manifest; memory_scope, observation_types in memory; effort, max_turns, hooks, permission_scope in config; Tool Permissions in tools)
3. MUST respect non-default overrides table for specific builders
4. NEVER generate ISOs that exceed size limits
5. ALWAYS validate generated builder with cex_doctor.py before commit

## Metadata

```yaml
id: bld_config_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | _builder construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[_builder-builder]] | upstream | 0.51 |
| [[bld_config_kind]] | sibling | 0.51 |
| [[bld_architecture_kind]] | upstream | 0.50 |
| [[bld_collaboration_builder]] | downstream | 0.47 |
| [[kind-builder]] | upstream | 0.47 |
| [[bld_output_template_builder]] | upstream | 0.39 |
| [[bld_architecture_builder]] | upstream | 0.39 |
| [[bld_knowledge_card_builder]] | upstream | 0.38 |
| [[bld_examples_builder]] | upstream | 0.37 |
| [[bld_knowledge_card_kind]] | upstream | 0.37 |
