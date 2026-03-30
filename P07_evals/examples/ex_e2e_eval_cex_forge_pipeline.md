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
- Forge with empty seeds: generic prompt, low-density output
- LLM ignores max_bytes hint: output oversized, trim required
- Missing template for type: forge outputs schema-only prompt
