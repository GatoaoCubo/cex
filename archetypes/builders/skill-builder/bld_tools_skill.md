---
kind: tools
id: bld_tools_skill
pillar: P04
llm_function: CALL
purpose: Tools available to skill-builder during construction
pattern: what external tools this builder can invoke
quality: 9.0
title: "Tools Skill"
version: "1.0.0"
author: n03_builder
tags: [skill, builder, examples]
tldr: "Golden and anti-examples for skill construction, demonstrating ideal structure and common pitfalls."
domain: "skill construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_builder
  - bld_tools_quality_gate
  - bld_tools_citation
  - bld_tools_cli_tool
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_path_config
  - bld_tools_prompt_version
  - bld_tools_constraint_spec
  - bld_tools_context_window_config
---

# Tools: skill-builder

## Available Tools

| Tool | Purpose | When |
|------|---------|------|
| `cex_query.py` | Find existing skills and patterns | F3 INJECT — discover similar skills |
| `cex_compile.py` | Validate frontmatter + compile to YAML | F8 COLLABORATE — after writing |
| `cex_doctor.py` | Check builder spec completeness | F7 GOVERN — verify all 13 specs |
| `cex_index.py` | Update search index | F8 COLLABORATE — after compile |
| `signal_writer.py` | Signal completion | F8 COLLABORATE — after commit |

## Tool Usage Pattern
```
F3: cex_query.py --kind skill → find similar skills
F5: List tools above → ready for use
F7: cex_compile.py {path} → validate
F8: cex_compile.py + cex_doctor.py + signal_writer.py → ship
```

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_builder]] | sibling | 0.48 |
| [[bld_tools_quality_gate]] | sibling | 0.48 |
| [[bld_tools_citation]] | sibling | 0.48 |
| [[bld_tools_cli_tool]] | sibling | 0.46 |
| [[bld_tools_retriever_config]] | sibling | 0.45 |
| [[bld_tools_memory_scope]] | sibling | 0.45 |
| [[bld_tools_path_config]] | sibling | 0.44 |
| [[bld_tools_prompt_version]] | sibling | 0.43 |
| [[bld_tools_constraint_spec]] | sibling | 0.43 |
| [[bld_tools_context_window_config]] | sibling | 0.43 |
