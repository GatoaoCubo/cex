---
kind: instruction
id: bld_instruction_validator_builder_codex
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for validator
pattern: 3-phase pipeline (classify -> compose -> validate)
---

# Instructions: How to Produce a validator

## Phase 1: CLASSIFY
1. Identify the rule target: file glob, field path, or artifact family
2. Define the exact boundary being enforced
3. Gather source constraints from schema, law, or existing template
4. Check for an existing `p06_val_*` artifact to avoid duplication
5. Confirm this is objective pass/fail, not weighted scoring

## Phase 2: COMPOSE
1. Read `SCHEMA.md` first
2. Fill `OUTPUT_TEMPLATE.md` without inventing fields
3. Set frontmatter with `id`, `kind`, `pillar`, `trigger`, `severity`
4. Set `quality: null`
5. Write `## Rule` with target, condition, threshold, `action_on_fail`
6. Write `## Checks` with concrete expressions
7. Write `## Error Messages`, `## Pass Example`, `## Fail Example`

## Phase 3: VALIDATE
1. Check `QUALITY_GATES.md` manually
2. HARD gates: naming, type integrity, required fields, trigger/severity enums
3. SOFT gates: density, concise errors, examples, no rubric drift
4. Cross-check compiled YAML can be derived from the markdown
5. If score < 8.0, revise in the same pass before publishing
