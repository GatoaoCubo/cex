---
kind: config
id: bld_config_handoff_protocol
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
title: "Config Handoff Protocol"
version: "1.0.0"
author: n03_builder
tags: [handoff_protocol, builder, examples]
tldr: "Golden and anti-examples for handoff protocol construction, demonstrating ideal structure and common pitfalls."
domain: "handoff protocol construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: handoff_protocol Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_handoff_{slug}.md` | `p02_handoff_example.md` |
| Builder directory | kebab-case | `handoff-protocol-builder/` |
| Frontmatter fields | snake_case | id, kind, pillar |
| Slug | snake_case, lowercase, no hyphens | `example_config` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
1. Output: `cex/P02_model/examples/p02_handoff_{slug}.md`
2. Compiled: `cex/P02_model/compiled/p02_handoff_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 2048 bytes
2. Total (frontmatter + body): ~3048 bytes
3. Density: >= 0.8 (no filler)

## Metadata

```yaml
id: bld_config_handoff_protocol
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-handoff-protocol.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | handoff protocol construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
