---
kind: config
id: bld_config_code_executor
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
title: "Config Code Executor"
version: "1.0.0"
author: n03_builder
tags: [code_executor, builder, examples]
tldr: "Golden and anti-examples for code executor construction, demonstrating ideal structure and common pitfalls."
domain: "code executor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_code_executor
  - p03_sp_code_executor_builder
  - bld_config_memory_scope
  - bld_config_retriever_config
  - bld_config_prompt_version
  - bld_instruction_code_executor
  - bld_config_output_validator
  - p11_qg_code_executor
  - bld_config_handoff_protocol
  - bld_config_constraint_spec
---
# Config: code_executor Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_exec_{runtime_slug}.md` | `p04_exec_python_docker.md` |
| Compiled files | `p04_exec_{runtime_slug}.yaml` | `p04_exec_python_docker.yaml` |
| Builder directory | kebab-case | `code_executor-builder/` |
| Frontmatter fields | snake_case | `sandbox_type`, `resource_limits` |
| Runtime slug | snake_case, lowercase, no hyphens | `python_docker`, `e2b_cloud` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_exec_{runtime_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_exec_{runtime_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4000 bytes
- Density: >= 0.80 (no filler)
## Sandbox Type Enum
| Value | Isolation Level | When to use |
|-------|----------------|-------------|
| docker | container | Standard isolation, good language support |
| e2b | cloud VM | Maximum isolation, cloud-hosted, persistent sessions |
| wasm | browser/WASM | Lightweight, client-side, limited language support |
| vm | full VM | Maximum isolation, hardware-level separation |
| process | OS process | Minimal isolation, fast startup, development only |
## Timeout Conventions
| Use Case | Recommended Timeout |
|----------|-------------------|
| Simple computation | 10-30s |
| Data analysis | 30-120s |
| File processing | 60-300s |
| Complex ML/training | 300-600s |
Rule: timeout MUST be > 0. Default: 30s.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_code_executor]] | upstream | 0.34 |
| [[p03_sp_code_executor_builder]] | upstream | 0.32 |
| [[bld_config_memory_scope]] | sibling | 0.31 |
| [[bld_config_retriever_config]] | sibling | 0.30 |
| [[bld_config_prompt_version]] | sibling | 0.30 |
| [[bld_instruction_code_executor]] | upstream | 0.30 |
| [[bld_config_output_validator]] | sibling | 0.30 |
| [[p11_qg_code_executor]] | downstream | 0.30 |
| [[bld_config_handoff_protocol]] | sibling | 0.29 |
| [[bld_config_constraint_spec]] | sibling | 0.28 |
