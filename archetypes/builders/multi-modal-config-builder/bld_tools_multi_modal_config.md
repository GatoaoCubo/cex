---
kind: tools
id: bld_tools_multi_modal_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for multi_modal_config production
quality: 9.0
title: "Tools Multi Modal Config"
version: "1.0.0"
author: n03_builder
tags: [multi_modal_config, builder, examples]
tldr: "Golden and anti-examples for multi modal config construction, demonstrating ideal structure and common pitfalls."
domain: "multi modal config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_context_window_config
  - bld_tools_prompt_cache
  - bld_tools_citation
  - bld_tools_retriever_config
  - bld_tools_path_config
  - bld_tools_cli_tool
  - bld_tools_memory_scope
  - bld_tools_boot_config
  - bld_tools_chunk_strategy
  - bld_tools_hook_config
---

# Tools: multi-modal-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile .md to .yaml | Phase 3 | ACTIVE |
| cex_retriever.py | Search existing configs | Phase 1 | ACTIVE |
| cex_token_budget.py | Estimate token costs per modality | Phase 2 | ACTIVE |
## Data Sources
| Source | Path | Data |
|--------|------|------|
| CEX Schema | P04_tools/_schema.yaml | Config field definitions |
| Kind KC | P01_knowledge/library/kind/kc_multi_modal_config.md | Deep knowledge |
| Model configs | .cex/config/nucleus_models.yaml | Model capabilities |
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

## Metadata

```yaml
id: bld_tools_multi_modal_config
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-multi-modal-config.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_context_window_config]] | sibling | 0.70 |
| [[bld_tools_prompt_cache]] | sibling | 0.58 |
| [[bld_tools_citation]] | sibling | 0.55 |
| [[bld_tools_retriever_config]] | sibling | 0.52 |
| [[bld_tools_path_config]] | sibling | 0.49 |
| [[bld_tools_cli_tool]] | sibling | 0.49 |
| [[bld_tools_memory_scope]] | sibling | 0.47 |
| [[bld_tools_boot_config]] | sibling | 0.47 |
| [[bld_tools_chunk_strategy]] | sibling | 0.46 |
| [[bld_tools_hook_config]] | sibling | 0.46 |
