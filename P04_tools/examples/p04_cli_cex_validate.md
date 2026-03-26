---
id: p04_cli_cex_validate
kind: cli_tool
name: cex_validate
pillar: P04
version: 1.0.0
created: 2026-03-24
author: edison
quality: 9.0
tags: [cli, validation, schema, compiler, cex]
---

# CLI Tool: cex_validate

## Purpose
Two-part CLI for CEX quality enforcement: validates schema integrity and compiles examples to machine-readable YAML/JSON.

## Usage
```bash
python _tools/validate_schema.py          # 267 checks across 12 LPs
python _tools/validate_examples.py        # Frontmatter + size + density
python _tools/cex_compile.py --all        # Compile all .md to .yaml/.json
python _tools/cex_compile.py --lp P04     # Compile single LP
```

## Inputs / Outputs
- Input: P*/_schema.yaml + P*/examples/*.md
- Output: P*/compiled/*.yaml (or .json for json machine_format)
- Exit codes: 0=pass, 1=warnings, 2=failures

## Guardrails
- Safe default: validate-only (no file mutations)
- Dangerous flag: `--all` recompiles everything (overwrites compiled/)
