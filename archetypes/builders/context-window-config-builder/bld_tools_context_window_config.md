---
kind: tools
id: bld_tools_context_window_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for context_window_config production
quality: 9.0
title: "Tools Context Window Config"
version: "1.0.0"
author: n03_builder
tags: [context_window_config, builder, examples]
tldr: "Golden and anti-examples for context window config construction, demonstrating ideal structure and common pitfalls."
domain: "context window config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Tools: context-window-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_token_budget.py | Token counting + budget allocation | Phase 1-2 | ACTIVE |
| cex_compile.py | Compile .md to .yaml | Phase 3 | ACTIVE |
| cex_retriever.py | Search existing configs | Phase 1 | ACTIVE |
## cex_token_budget.py Usage
```bash
python _tools/cex_token_budget.py --model claude-opus --sections system,context,examples,query,output
```
## Data Sources
| Source | Path | Data |
|--------|------|------|
| CEX Schema | P03_prompt/_schema.yaml | Config field definitions |
| Kind KC | P01_knowledge/library/kind/kc_context_window_config.md | Deep knowledge |
| Model configs | .cex/config/nucleus_models.yaml | Model limits |
## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | — |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target
