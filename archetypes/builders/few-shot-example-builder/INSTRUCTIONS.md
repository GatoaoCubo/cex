---
pillar: P03
llm_function: REASON
purpose: Step-by-step execution protocol for few-shot-example-builder
---

# Instructions: few-shot-example-builder

## Phase 1: DESIGN

1. Identify the task/format to exemplify — what artifact kind or prompt pattern are you teaching?
2. Determine domain (knowledge_card, validator, rag_source, etc.)
3. Select difficulty level: easy (canonical), medium (realistic variation), hard (edge case)
4. Plan edge cases: what boundary condition could break naive implementations?
5. Check brain_query: `brain_query("few_shot_example [domain]")` — avoid duplicates
6. Confirm: is this format teaching (few_shot_example) or quality evaluation (golden_test)?

## Phase 2: COMPOSE

1. Read SCHEMA.md — internalize all required fields and constraints
2. Read OUTPUT_TEMPLATE.md — use exact template structure
3. Fill frontmatter:
   - id: p01_fse_{topic_slug} (must match filename stem)
   - kind: few_shot_example
   - quality: null (never self-score)
   - input: realistic task request the user would send
   - output: ideal response demonstrating the target format
4. Craft input field: concrete, specific, realistic — not "write something"
5. Craft output field: complete format demonstration — not abstract description
6. Write Explanation section: WHY this input/output pair teaches the format
7. Write Variations section: 2-3 alternative inputs that test different aspects
8. Write Edge Cases section: boundary inputs and how output handles them

## Phase 3: VALIDATE

1. Check QUALITY_GATES.md — run all 7 HARD gates manually
2. HARD gates checklist:
   - [ ] H01: YAML frontmatter parses without error
   - [ ] H02: id matches `^p01_fse_[a-z][a-z0-9_]+$`
   - [ ] H03: id == filename stem (p01_fse_topic.md)
   - [ ] H04: kind == "few_shot_example"
   - [ ] H05: quality == null
   - [ ] H06: input field non-empty string
   - [ ] H07: output field non-empty string
3. SOFT gates checklist (score contribution):
   - [ ] S01: tldr <= 160 chars
   - [ ] S02: tags list >= 3 items
   - [ ] S03: Explanation section present
   - [ ] S04: input is a realistic task request
   - [ ] S05: output demonstrates format clearly
   - [ ] S06: body <= 1024 bytes
   - [ ] S07: no scoring rubric present
4. Cross-check: is this still a format example? Not becoming evaluation/test?
5. If any HARD gate fails: fix before publish. If SOFT fails: fix to improve score.
