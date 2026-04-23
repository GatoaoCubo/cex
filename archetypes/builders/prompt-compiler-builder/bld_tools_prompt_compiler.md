---
kind: tools
id: bld_tools_prompt_compiler
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for prompt_compiler production
quality: 9.1
title: "Tools Prompt Compiler"
version: "1.0.0"
author: n03_builder
tags: [prompt_compiler, builder, tools, P03]
tldr: "Tools for building prompt_compiler artifacts: kinds registry, transmutation rules, retriever, compiler."
domain: "prompt_compiler construction"
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
related:
  - bld_tools_context_window_config
  - bld_tools_prompt_cache
  - bld_tools_prompt_version
  - bld_tools_citation
  - bld_tools_action_prompt
  - bld_tools_multi_modal_config
  - bld_tools_kind
  - bld_tools_retriever_config
  - bld_tools_knowledge_graph
  - bld_tools_constraint_spec
---

# Tools: prompt-compiler-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile .md to .yaml | Phase 4 (validate) | ACTIVE |
| cex_doctor.py | Health check | Phase 4 (validate) | ACTIVE |
| cex_query.py | TF-IDF kind discovery | Phase 1 (research) | ACTIVE |
| cex_retriever.py | Semantic similarity search | Phase 1 (research) | ACTIVE |
| cex_prompt_layers.py | Verify prompt layer loading | Phase 4 (validate) | ACTIVE |
## Data Sources
| Source | Path | Data |
|--------|------|------|
| Kind registry | .cex/kinds_meta.json | All 124 kinds with pillar, function, boundary |
| Transmutation rules | .claude/rules/n07-input-transmutation.md | Existing user-to-kind mapping tables |
| Intent resolution KC | N03_engineering/P01_knowledge/kc_intent_resolution_map.md | Exhaustive 124-kind intent map |
| P03 schema | P03_prompt/_schema.yaml | Pillar-level schema for prompt kinds |
| Existing compilers | P03_prompt/layers/ | Existing prompt layer artifacts |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | - |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Pipeline Integration

1. Created via 8F pipeline from F1 through F8
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Loaded by cex_prompt_layers as a runtime prompt layer
5. Evolved by cex_evolve when quality regresses below target

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_context_window_config]] | sibling | 0.49 |
| [[bld_tools_prompt_cache]] | sibling | 0.48 |
| [[bld_tools_prompt_version]] | sibling | 0.48 |
| [[bld_tools_citation]] | sibling | 0.48 |
| [[bld_tools_action_prompt]] | sibling | 0.46 |
| [[bld_tools_multi_modal_config]] | sibling | 0.46 |
| [[bld_tools_kind]] | sibling | 0.44 |
| [[bld_tools_retriever_config]] | sibling | 0.44 |
| [[bld_tools_knowledge_graph]] | sibling | 0.43 |
| [[bld_tools_constraint_spec]] | sibling | 0.43 |
