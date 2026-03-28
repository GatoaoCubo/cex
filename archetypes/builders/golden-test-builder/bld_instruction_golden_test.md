---
kind: instruction
id: bld_instruction_golden_test
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for golden_test
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a golden_test

## Phase 1: RESEARCH

1. Identify the target artifact kind to calibrate — which kind needs a 9.5+ reference case?
2. Find existing 9.5+ quality examples as candidates — locate actual artifacts of that kind scoring at the top of the range
3. Study the target kind's quality gates — read its QUALITY_GATES.md to understand what makes an artifact excellent vs merely acceptable
4. Map rationale to specific gate IDs — for each gate, identify what the golden artifact does to satisfy it completely
5. Determine what distinguishes a 9.5 from an 8.0 — articulate the exact delta, not vague praise
6. Check existing golden_tests for the same kind — avoid producing a duplicate calibration reference

## Phase 2: COMPOSE

1. Read SCHEMA.md — source of truth for all required fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all required fields, quality: null (never self-score), quality_threshold: 9.5 or higher
4. Write Input section: the complete input that would produce this golden artifact — verbatim, no abbreviation
5. Write Expected Output section: the full 9.5+ quality artifact — complete, not summarized
6. Write Rationale section: per-gate explanation of why this artifact scores 9.5+ — cite gate IDs explicitly
7. Write Gate Mapping section: table of which quality gates this golden satisfies and how each is met
8. Write Boundary Notes section: what a near-miss 8.0 version would look like — the specific gaps that drop the score

## Phase 3: VALIDATE

1. Check QUALITY_GATES.md — run all HARD gates for this builder manually
2. HARD gates:
   - [ ] id matches `p07_gt_[a-z][a-z0-9_]+`
   - [ ] kind == `golden_test`
   - [ ] quality == null
   - [ ] quality_threshold >= 9.5
   - [ ] input section is complete
   - [ ] expected output is present and unabbreviated
   - [ ] rationale maps to specific gate IDs
3. SOFT gates: gate mapping table present, boundary notes distinguish 9.5 from 8.0, reviewer assigned
4. Cross-check: calibration reference not format example (that is few_shot_example)? Not pass/fail assertion (that is unit_eval)? Not performance measurement (that is benchmark)? Rationale is gate-specific not generic praise?
5. Verify the expected output passes ALL HARD gates of the target kind's own builder before finalizing
6. If score < 8.0: revise in the same pass before outputting
