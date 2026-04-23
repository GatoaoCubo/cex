---
id: p04_ct_validate_schema
kind: cli_tool
pillar: P04
title: "Validate Schema — Structural integrity checker for _schema.yaml"
version: 1.0.0
created: 2026-03-28
author: builder_agent
tags: [cli, tool, cex, qa, schema, validation]
cli_command: "python _tools/validate_schema.py"
cli_args: []
inputs: ["all P*/_schema.yaml files (auto-scanned)"]
outputs: ["pass/fail report per schema: required fields, type structure, LP consistency"]
dependencies: ["pyyaml"]
category: qa
quality: 9.0
tldr: "Golden and anti-examples for tool integration, demonstrating ideal structure and common pitfalls."
domain: "tool integration"
updated: "2026-04-07"
density_score: 0.90
related:
  - p04_ct_cex_doctor
  - p04_ct_cex_compile
  - p04_ct_fix_frontmatter
  - validate
  - bld_output_template_input_schema
  - bld_instruction_builder
  - p04_ct_cex_forge
  - bld_instruction_input_schema
  - p01_gl_taxonomy
  - bld_examples_workflow_primitive
---

## Purpose
Validates each P*/_schema.yaml for structural integrity: required top-level fields (lp, name, description), LP code consistency with directory name, and correct kinds section with required type fields (description, naming, constraints).

## Usage
```bash
# Scan all schemas (no arguments needed)
python _tools/validate_schema.py
```

## Arguments
No arguments. Scans all P*/_schema.yaml files automatically.

## Pipeline Position
**8F Function**: CONSTRAIN (F1) — validates the constraint layer that all other tools depend on.
**Stage**: Infrastructure validation. Run after modifying any _schema.yaml. Upstream of cex_forge, cex_pipeline, and cex_compile which all read schemas.

## Dependencies
1. `P*/_schema.yaml` files in each LP directory
2. Required top-level fields: lp, name, description
3. Required per-type fields: description, naming, constraints

## Properties

| Property | Value |
|----------|-------|
| Kind | `cli_tool` |
| Pillar | P04 |
| Domain | tool integration |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ct_cex_doctor]] | sibling | 0.31 |
| [[p04_ct_cex_compile]] | sibling | 0.30 |
| [[p04_ct_fix_frontmatter]] | sibling | 0.26 |
| [[validate]] | downstream | 0.25 |
| [[bld_output_template_input_schema]] | downstream | 0.23 |
| [[bld_instruction_builder]] | upstream | 0.20 |
| [[p04_ct_cex_forge]] | sibling | 0.20 |
| [[bld_instruction_input_schema]] | upstream | 0.20 |
| [[p01_gl_taxonomy]] | upstream | 0.20 |
| [[bld_examples_workflow_primitive]] | downstream | 0.19 |
