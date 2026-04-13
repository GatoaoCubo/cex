---
kind: config
id: bld_config_prompt_compiler
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: high
max_turns: 40
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Prompt Compiler"
version: "1.0.0"
author: n03_builder
tags: [prompt_compiler, builder, config, P03]
tldr: "Production rules for prompt_compiler: naming, paths, size limits, language requirements."
domain: "prompt_compiler construction"
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
---
# Config: prompt_compiler Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p03_pc_{slug}.md` | `p03_pc_cex_universal.md` |
| Builder directory | kebab-case | `prompt-compiler-builder/` |
| Frontmatter fields | snake_case | `kind_resolution`, `verb_table` |
| Compiler slug | snake_case, lowercase | `cex_universal`, `edtech_domain` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `P03_prompt/p03_pc_{slug}.md`
- Compiled: `P03_prompt/compiled/p03_pc_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 16384 bytes (largest kind in CEX)
- Total (frontmatter + body): ~18000 bytes
- Density: >= 0.85
## Language Requirements
| Requirement | Minimum | Target |
|-------------|---------|--------|
| Languages supported | 2 (PT-BR + EN) | 2+ |
| PT coverage of EN patterns | 80% | 95% |
| Verbs per language | 15 | 30+ |
| Patterns per kind | 1 | 2-5 |
## Kind Coverage Requirements
| Scope | Minimum | Target |
|-------|---------|--------|
| Total kinds mapped | 120 | 124 (all) |
| Kinds with boundary notes | 100 | 124 |
| Kinds with nucleus assignment | 120 | 124 |
## Effort Profile
This is the HIGHEST effort artifact in CEX due to:
- 124 kinds requiring individual pattern authoring
- Bilingual requirement (PT-BR + EN independently)
- max_turns: 40 (vs typical 25)
- Body size: 16384 bytes (vs typical 4096)
