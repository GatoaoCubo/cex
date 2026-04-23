---
kind: schema
id: bld_schema_code_executor
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for code_executor
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Code Executor"
version: "1.0.0"
author: n03_builder
tags: [code_executor, builder, examples]
tldr: "Golden and anti-examples for code executor construction, demonstrating ideal structure and common pitfalls."
domain: "code executor construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_memory_scope
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_smoke_eval
  - bld_schema_sandbox_config
  - bld_schema_golden_test
  - bld_schema_unit_eval
  - bld_schema_sandbox_spec
  - bld_schema_constraint_spec
---

# Schema: code_executor
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p04_exec_{runtime_slug}) | YES | - | Namespace compliance |
| kind | literal "code_executor" | YES | - | Type integrity |
| pillar | literal "P04" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable executor name |
| runtime | enum: python, node, bash, r, julia, go, multi | YES | - | Primary language runtime |
| sandbox_type | enum: docker, e2b, wasm, vm, process | YES | - | Isolation mechanism |
| languages | list[string], len >= 1 | YES | - | Supported programming languages |
| timeout | integer (seconds) | YES | 30 | Max execution time per invocation |
| resource_limits | object | REC | - | CPU, memory, disk constraints |
| network_access | boolean | REC | false | Whether sandbox has network |
| file_io | boolean | REC | true | Whether sandbox supports file I/O |
| persistent_session | boolean | REC | false | Whether state persists between calls |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "code_executor" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the executor does |
## ID Pattern
Regex: `^p04_exec_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what runtime this provides, use case, isolation guarantee
2. `## Sandbox` — isolation mechanism, security boundary, escape prevention
3. `## Languages` — supported languages with version constraints
4. `## Limits` — timeout, CPU, memory, disk, network policy
## Constraints
- max_bytes: 2048 (body only)
- naming: p04_exec_{runtime_slug}.md + .yaml (compiled)
- machine_format: yaml (compiled artifact)
- id == filename stem
- timeout MUST be > 0 seconds
- quality: null always
- NO implementation code in body — spec only

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.64 |
| [[bld_schema_memory_scope]] | sibling | 0.64 |
| [[bld_schema_handoff_protocol]] | sibling | 0.64 |
| [[bld_schema_output_validator]] | sibling | 0.64 |
| [[bld_schema_smoke_eval]] | sibling | 0.63 |
| [[bld_schema_sandbox_config]] | sibling | 0.63 |
| [[bld_schema_golden_test]] | sibling | 0.63 |
| [[bld_schema_unit_eval]] | sibling | 0.63 |
| [[bld_schema_sandbox_spec]] | sibling | 0.63 |
| [[bld_schema_constraint_spec]] | sibling | 0.62 |
