---
id: p04_cli_cex_validate
name: cex_validate
description: "CLI that validates CEX schema integrity and compiles .md examples to YAML/JSON for LLM consumption"
commands:
  - validate_schema.py
  - cex_compile.py
lp: P04
type: cli_tool
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: edison
domain: meta-construction
quality: 9.0
tags: [cli, validation, schema, compiler, cex]
---

# CEX Validate CLI — Schema Validation & Compilation

## Purpose
Two-part CLI toolchain for the CEX framework: `validate_schema.py` checks structural integrity of all P*/_schema.yaml files, and `cex_compile.py` converts .md examples to compiled YAML/JSON for LLM consumption.

## validate_schema.py
Validates each LP schema for structural integrity.

**Checks performed:**
- Top-level required fields: `lp`, `name`, `description`
- LP name matches directory (P01, P02, etc.)
- Types section present with required fields: `description`, `naming`, `constraints`
- Cross-references between types

```bash
