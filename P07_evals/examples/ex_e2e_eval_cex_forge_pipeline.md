---
id: p07_e2e_cex_forge_pipeline
kind: e2e_eval
pillar: P07
description: "End-to-end test of CEX artifact generation pipeline"
pipeline: forge_validate_compile
version: 1.0.0
created: 2026-03-24
author: operations_agent
quality: 9.0
tags: [e2e, cex, forge, pipeline, validation]
updated: "2026-04-07"
domain: "evaluation"
title: "E2E Eval Cex Forge Pipeline"
density_score: 0.92
tldr: "Defines e2e eval for e2e eval cex forge pipeline, with validation gates and integration points."
---

# E2E Eval: CEX Forge Pipeline

## Pipeline
```
cex_forge.py --lp P01 --type knowledge_card --seeds "test"
  -> generated_example.md
    -> validate_examples.py (frontmatter + size + density)
      -> cex_compile.py (md -> yaml)
        -> compiled output
```

## Test Steps
1. **Generate**: Run forge with known seeds, capture output prompt
2. **Create**: Feed prompt to LLM, save response as example .md
3. **Validate**: Run validate_examples.py on generated file
4. **Compile**: Run cex_compile.py, verify YAML output parseable
5. **Quality**: Check density >= 0.8, size <= max_bytes, all required fields

## Pass Criteria
| Step | Criterion |
|------|-----------|
| Generate | Prompt < 20KB, no {{PLACEHOLDER}} remaining |
| Validate | 0 FAIL checks |
| Compile | Valid YAML output, no parse errors |
| Quality | density >= 0.8, score >= 7.0 |

## Known Failure Modes
1. Forge with empty seeds: generic prompt, low-density output
2. LLM ignores max_bytes hint: output oversized, trim required
3. Missing template for type: forge outputs schema-only prompt

## Properties

| Property | Value |
|----------|-------|
| Kind | `e2e_eval` |
| Pillar | P07 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
