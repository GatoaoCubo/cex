---
kind: instruction
id: bld_instruction_golden_test
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for golden_test
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Golden Test"
version: "1.0.0"
author: n03_builder
tags: [golden_test, builder, examples]
tldr: "Golden and anti-examples for golden test construction, demonstrating ideal structure and common pitfalls."
domain: "golden test construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_action_prompt
  - bld_instruction_output_validator
  - bld_instruction_retriever_config
  - bld_instruction_memory_scope
  - bld_instruction_few_shot_example
  - bld_instruction_kind
  - p03_sp_golden_test_builder
  - bld_instruction_prompt_version
  - bld_instruction_chunk_strategy
  - bld_instruction_handoff_protocol
---

# Instructions: How to Produce a golden_test
## Phase 1: RESEARCH
1. Identify the target artifact kind to calibrate — which kind needs a 9.5+ reference case?
2. Find existing 9.5+ quality examples as candidates — locate actual artifacts of that kind scoring at the top of the range
3. Study the target kind's quality gates — read its QUALITY_GATES.md to understand what makes an artifact excellent vs merely acceptable
4. Map rationale to specific gate IDs — for each gate, identify what the golden artifact does to satisfy it completely
5. Determine what distinguishes a 9.5 from an 8.0 — articulate the exact delta, not vague forise
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
4. Cross-check: calibration reference not format example (that is few_shot_example)? Not pass/fail assertion (that is unit_eval)? Not performance measurement (that is benchmark)? Rationale is gate-specific not generic forise?
5. Verify the expected output passes ALL HARD gates of the target kind's own builder before finalizing
6. If score < 8.0: revise in the same pass before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify golden
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | golden test construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_action_prompt]] | sibling | 0.38 |
| [[bld_instruction_output_validator]] | sibling | 0.37 |
| [[bld_instruction_retriever_config]] | sibling | 0.36 |
| [[bld_instruction_memory_scope]] | sibling | 0.35 |
| [[bld_instruction_few_shot_example]] | sibling | 0.35 |
| [[bld_instruction_kind]] | sibling | 0.35 |
| [[p03_sp_golden_test_builder]] | related | 0.35 |
| [[bld_instruction_prompt_version]] | sibling | 0.35 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.34 |
| [[bld_instruction_handoff_protocol]] | sibling | 0.34 |
