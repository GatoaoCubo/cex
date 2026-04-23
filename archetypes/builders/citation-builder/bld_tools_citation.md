---
kind: tools
id: bld_tools_citation
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for citation production
quality: 9.0
title: "Tools Citation"
version: "1.0.0"
author: n03_builder
tags: [citation, builder, examples]
tldr: "Golden and anti-examples for citation construction, demonstrating ideal structure and common pitfalls."
domain: "citation construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_retriever_config
  - bld_tools_multi_modal_config
  - bld_tools_context_window_config
  - bld_tools_prompt_cache
  - bld_tools_quality_gate
  - bld_tools_memory_scope
  - bld_tools_chunk_strategy
  - bld_tools_cli_tool
  - bld_tools_prompt_version
  - bld_tools_path_config
---

# Tools: citation-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile .md to .yaml | Phase 3 | ACTIVE |
| cex_retriever.py | Search existing citations | Phase 1 | ACTIVE |
| brain_query [MCP] | Search knowledge pool | Phase 1 | CONDITIONAL |
## Data Sources
| Source | Path | Data |
|--------|------|------|
| CEX Schema | P01_knowledge/_schema.yaml | Citation field definitions |
| Kind KC | P01_knowledge/library/kind/kc_citation.md | Deep knowledge about citation |
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

## Metadata

```yaml
id: bld_tools_citation
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-citation.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_retriever_config]] | sibling | 0.61 |
| [[bld_tools_multi_modal_config]] | sibling | 0.61 |
| [[bld_tools_context_window_config]] | sibling | 0.60 |
| [[bld_tools_prompt_cache]] | sibling | 0.60 |
| [[bld_tools_quality_gate]] | sibling | 0.58 |
| [[bld_tools_memory_scope]] | sibling | 0.58 |
| [[bld_tools_chunk_strategy]] | sibling | 0.58 |
| [[bld_tools_cli_tool]] | sibling | 0.58 |
| [[bld_tools_prompt_version]] | sibling | 0.56 |
| [[bld_tools_path_config]] | sibling | 0.56 |
