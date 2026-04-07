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
