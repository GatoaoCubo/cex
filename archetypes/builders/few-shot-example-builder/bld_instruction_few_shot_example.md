---
kind: instruction
id: bld_instruction_few_shot_example
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for few_shot_example
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a few_shot_example

## Phase 1: RESEARCH

1. Identify the target format to exemplify — which artifact kind or output structure are you teaching?
2. Determine difficulty level: easy (canonical happy path), medium (realistic variation), hard (edge case or boundary input)
3. Select realistic input data — concrete, specific, the kind of request a real user would send
4. Craft the expected output matching the exact target format — no abbreviations, no abstractions
5. Identify edge cases to cover — what unusual input or boundary condition does this example exercise?
6. Check existing examples for the same format — avoid producing a duplicate that teaches the same lesson

## Phase 2: COMPOSE

1. Read SCHEMA.md — source of truth for all required fields and constraints
2. Read OUTPUT_TEMPLATE.md — use exact template structure
3. Fill frontmatter:
   - id: `p01_fse_{topic_slug}` (must match filename stem)
   - kind: `few_shot_example`
   - quality: null (never self-score)
   - difficulty: easy | medium | hard
4. Write Input section: realistic data matching the target schema — not "write something", but a fully specified request
5. Write Output section: correctly formatted result demonstrating the target format without deviation
6. Write Difficulty section: calibration level with one-line justification
7. Write Edge Cases section: which unusual inputs this example covers and how
8. Write Format Notes section: which structural element or rule this example is specifically teaching
9. Check body size — must stay at or below 1024 bytes

## Phase 3: VALIDATE

1. Check QUALITY_GATES.md — run all HARD gates manually before outputting
2. HARD gates:
   - [ ] id matches `p01_fse_[a-z][a-z0-9_]+`
   - [ ] kind == `few_shot_example`
   - [ ] quality == null
   - [ ] input field is non-empty
   - [ ] output field is non-empty
   - [ ] difficulty is labeled
   - [ ] body <= 1024 bytes
3. SOFT gates: tldr <= 160 chars, tags >= 3, Format Notes present, input is realistic, output demonstrates format clearly
4. Cross-check: teaches FORMAT not evaluates quality (that is golden_test)? Not assertion-based (that is unit_eval)? No `{{vars}}` placeholders (that is prompt_template)?
5. If score < 8.0: revise in the same pass before outputting
