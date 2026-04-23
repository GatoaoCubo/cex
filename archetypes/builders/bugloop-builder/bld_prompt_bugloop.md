---
kind: instruction
id: bld_instruction_bugloop
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for bugloop
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Bugloop"
version: "1.0.0"
author: n03_builder
tags: [bugloop, builder, examples]
tldr: "Golden and anti-examples for bugloop construction, demonstrating ideal structure and common pitfalls."
domain: "bugloop construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_bugloop_builder
  - p11_qg_bugloop
  - bld_examples_bugloop
  - bld_knowledge_card_bugloop
  - bld_output_template_bugloop
  - bld_instruction_golden_test
  - bugloop-builder
  - bld_config_bugloop
  - p01_kc_bugloop
  - p10_lr_bugloop_builder
---

# Instructions: How to Produce a bugloop
## Phase 1: RESEARCH
1. Identify the target system or test suite this loop monitors
2. Catalog detection triggers: list concrete failure signatures — specific regex patterns, named test failure strings, or log scan patterns — not vague descriptions
3. Define fix strategies per failure class: assign auto_fix=true only where confidence >= 0.7, use auto_fix=false for non-deterministic or high-risk failures
4. Specify verification assertions: what must be true after a fix attempt — at minimum one named assertion with a timeout bound
5. Determine escalation thresholds: the number of failed fix attempts that triggers escalation, and the target (human role, queue name, or named system)
6. Map rollback policies: if fix strategy is rollback_first, rollback.enabled must be true — these must be consistent
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all required fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Fill frontmatter: all required fields (quality: null, never self-score)
4. Write Detection section: list each trigger with its concrete pattern (regex or named signature) and the signal source (test runner output, log file, static analysis report)
5. Write Fix Strategy section: max_attempts value, auto_fix flag with rationale tied to confidence level, and the named strategy (patch_and_retry, rollback_first, or isolate_then_fix)
6. Write Verification section: test suite path or name, list of assertions that must pass, and timeout in seconds
7. Write Escalation section: threshold (must be <= cycle_count), target name, and payload content sent on escalation
8. Write Rollback section: enabled flag, strategy name (git_revert, snapshot_restore, or blue_green), and trigger condition
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. HARD gate: id matches `p11_bl_` pattern
3. HARD gate: kind == bugloop
4. HARD gate: quality == null
5. HARD gate: detection contains at least one concrete trigger with a pattern (not a description)
6. HARD gate: max_attempts is defined as an integer between 1 and 10
7. HARD gate: verification contains at least one assertion
8. HARD gate: if auto_fix == true, confidence must be >= 0.7 — reject if not
9. HARD gate: if fix strategy is rollback_first, rollback.enabled must be true — reject contradiction
10. Cross-check: is this a detect-fix-verify cycle? If it only blocks on pass/fail without attempting fixes, it is a quality_gate not a bugloop
11. Cross-check: is this driven by failure correction, not metric optimization? Metric-driven improvement is an optimizer artifact
12. If score < 8.0: revise before outputting


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_bugloop_builder]] | downstream | 0.42 |
| [[p11_qg_bugloop]] | downstream | 0.39 |
| [[bld_examples_bugloop]] | downstream | 0.36 |
| [[bld_knowledge_card_bugloop]] | upstream | 0.35 |
| [[bld_output_template_bugloop]] | downstream | 0.34 |
| [[bld_instruction_golden_test]] | sibling | 0.34 |
| [[bugloop-builder]] | downstream | 0.32 |
| [[bld_config_bugloop]] | downstream | 0.32 |
| [[p01_kc_bugloop]] | downstream | 0.31 |
| [[p10_lr_bugloop_builder]] | downstream | 0.31 |
