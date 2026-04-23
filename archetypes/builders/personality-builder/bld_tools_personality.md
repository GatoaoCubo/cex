---
quality: 8.2
quality: 7.8
kind: tools_config
id: bld_tools_personality
pillar: P04
llm_function: CALL
purpose: Tools used by personality-builder during 8F pipeline execution
title: "Tools: personality-builder"
version: "1.0.0"
author: n03_builder
tags: [personality, builder, tools, P04, hermes_origin]
tldr: "personality-builder tools: cex_compile.py, cex_score.py, cex_doctor.py. No external APIs needed."
domain: "persona construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.85
related:
  - bld_tools_model_architecture
  - doctor
  - p11_qg_knowledge
  - bld_tools_training_method
  - bld_tools_kind
  - p01_kc_cex_tooling_master
  - bld_tools_consolidation_policy
  - bld_tools_knowledge_graph
  - bld_tools_procedural_memory
  - p04_ct_cex_compile
---

# Tools: personality-builder

## Build Pipeline Tools

| Tool | Phase | Purpose | Command |
|------|-------|---------|---------|
| cex_compile.py | F8 | Compile .md -> .yaml | `python _tools/cex_compile.py {{path}}` |
| cex_score.py | F7 | Peer-review scoring | `python _tools/cex_score.py --apply {{path}}` |
| cex_doctor.py | F8 | Health check | `python _tools/cex_doctor.py` |
| cex_retriever.py | F3 | Find similar personalities | `python _tools/cex_retriever.py "personality"` |
| signal_writer.py | F8 | Completion signal | `from _tools.signal_writer import write_signal` |

## Discovery Tools

| Tool | Purpose | Notes |
|------|---------|-------|
| cex_query.py | Find existing personalities | `python _tools/cex_query.py personality` |
| cex_8f_runner.py | Run full pipeline | `python _tools/cex_8f_runner.py "personality" --kind personality --execute` |

## No External APIs Required
personality artifacts are pure specification -- voice parameters, values, and examples.
No external API calls, web fetches, or database queries are needed during construction.

## Validation Tools

```bash
# Validate JSON after kinds_meta.json update
python -m json.tool .cex/kinds_meta.json

# Compile after save
python _tools/cex_compile.py N00_genesis/P02_model/tpl_personality.md

# Doctor check
python _tools/cex_doctor.py
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_model_architecture]] | related | 0.34 |
| [[doctor]] | downstream | 0.33 |
| [[p11_qg_knowledge]] | downstream | 0.32 |
| [[bld_tools_training_method]] | related | 0.31 |
| [[bld_tools_kind]] | related | 0.31 |
| [[p01_kc_cex_tooling_master]] | upstream | 0.30 |
| [[bld_tools_consolidation_policy]] | related | 0.29 |
| [[bld_tools_knowledge_graph]] | related | 0.29 |
| [[bld_tools_procedural_memory]] | related | 0.28 |
| [[p04_ct_cex_compile]] | related | 0.27 |
