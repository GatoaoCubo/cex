---
kind: instruction
id: bld_instruction_output_validator
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for output_validator
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.1
title: "Instruction Output Validator"
version: "1.0.0"
author: n03_builder
tags: [output_validator, builder, examples]
tldr: "Golden and anti-examples for output validator construction, demonstrating ideal structure and common pitfalls."
domain: "output validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a output_validator
## Phase 1: RESEARCH
1. Identify the use case and target system
2. Determine which pattern fits (Schema validation, Regex check, LLM-as-judge, Fix-and-retry)
3. List required parameters with concrete values
4. Check for existing output_validator artifacts to avoid duplicates
5. Confirm slug for id: snake_case, lowercase, no hyphens
6. Review KNOWLEDGE.md for domain patterns and anti-patterns
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (id, kind, pillar, version, created, updated, author, name, checks, on_fail, quality, tags, tldr), quality: null
4. Write Overview section: what it does, who uses it
5. Write Checks section: core definition with concrete values
6. Write Failure Actions section: parameter table with value and rationale columns
7. Write Integration section: upstream/downstream connections
8. Verify body <= 2048 bytes
9. Verify id matches `^p05_oval_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p05_oval_`
4. Confirm kind == output_validator
5. Confirm all required body sections present: Overview, Checks, Failure Actions, Integration
6. HARD gates: frontmatter valid, id pattern matches, kind correct, required fields present
7. SOFT gates: score against QUALITY_GATES.md dimensions
8. Cross-check boundary: is this truly a output_validator and not validation_schema (P06?
9. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify output
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | output validator construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
