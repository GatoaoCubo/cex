---
id: n00_code_executor_manifest
kind: knowledge_card
8f: F3_inject
pillar: P04
nucleus: n00
title: "Code Executor -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, code_executor, p04, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_schema_code_executor
  - p03_sp_code_executor_builder
  - bld_architecture_code_executor
  - bld_schema_sandbox_spec
  - bld_schema_sandbox_config
  - code-executor-builder
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_usage_report
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A code_executor provides a sandboxed runtime environment for executing LLM-generated code safely, capturing output, errors, and side effects as structured observations. It supports Docker containers, E2B cloud sandboxes, and Jupyter kernels as backends, with resource limits, timeout enforcement, and output serialization. The output is a tool that lets agents verify code correctness without risking host system contamination.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `code_executor` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| runtime | string | yes | Backend: docker, e2b, jupyter, subprocess |
| languages | list | yes | Supported languages: python, javascript, bash, sql |
| timeout_seconds | integer | yes | Maximum execution time before sandbox kill |
| resource_limits | map | no | CPU, memory, and network access constraints |

## When to use
- When N03 Engineering generates code that must be validated by execution before committing
- When building a bugloop that requires iterative code generation and test execution
- When the agent pipeline includes data analysis that requires running Python or SQL

## Builder
`archetypes/builders/code_executor-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind code_executor --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ce_python_e2b_sandbox
kind: code_executor
pillar: P04
nucleus: n05
title: "Python E2B Sandbox Executor"
version: 1.0
quality: null
---
runtime: e2b
languages: [python, bash]
timeout_seconds: 30
resource_limits:
  memory_mb: 512
  network: blocked
```

## Related kinds
- `cli_tool` (P04) -- simpler subprocess wrapper when sandboxing is not required
- `bugloop` (P11) -- iterative code fix loop that drives code_executor repeatedly
- `scoring_rubric` (P07) -- rubric that evaluates code_executor output quality
- `function_def` (P04) -- LLM-callable interface wrapping the code_executor

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_code_executor]] | downstream | 0.46 |
| [[p03_sp_code_executor_builder]] | related | 0.42 |
| [[bld_architecture_code_executor]] | downstream | 0.41 |
| [[bld_schema_sandbox_spec]] | downstream | 0.41 |
| [[bld_schema_sandbox_config]] | downstream | 0.40 |
| [[code-executor-builder]] | related | 0.40 |
| [[bld_schema_reranker_config]] | downstream | 0.40 |
| [[bld_schema_benchmark_suite]] | downstream | 0.39 |
| [[bld_schema_integration_guide]] | downstream | 0.39 |
| [[bld_schema_usage_report]] | downstream | 0.38 |
