---
kind: config
id: bld_config_prompt_version
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
title: "Config Prompt Version"
version: "1.0.0"
author: n03_builder
tags: [prompt_version, builder, examples]
tldr: "Golden and anti-examples for prompt version construction, demonstrating ideal structure and common pitfalls."
domain: "prompt version construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: prompt_version Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_pv_{slug}.md` | `p03_pv_example.md` |
| Builder directory | kebab-case | `prompt-version-builder/` |
| Frontmatter fields | snake_case | id, kind, pillar |
| Slug | snake_case, lowercase, no hyphens | `example_config` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
1. Output: `cex/P03_prompt/examples/p03_pv_{slug}.md`
2. Compiled: `cex/P03_prompt/compiled/p03_pv_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
1. Body: max 2048 bytes
2. Total (frontmatter + body): ~3048 bytes
3. Density: >= 0.8 (no filler)

## Metadata

```yaml
id: bld_config_prompt_version
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-prompt-version.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | prompt version construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
