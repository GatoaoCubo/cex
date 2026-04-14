---
id: p11_qg_unit_eval
kind: quality_gate
pillar: P07
title: "Gate: Unit Eval"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: unit_eval
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - unit-eval
  - testing
  - P07
tldr: "Validates unit tests for agents and prompts: input, expected output, target component, and isolation."
llm_function: GOVERN
---
## Definition
A unit eval tests a single agent, prompt, or component in isolation. It defines an input, an expected output or assertion, the component under test, and setup and teardown steps. Unit evals must be deterministic, fast, and independent of external services. This gate ensures every unit eval is traceable, executable, and covers meaningful behavior rather than trivial cases.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p07_ue_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `unit_eval` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `target`, `target_kind`, `assertions` all defined and non-empty |
| H07 | Input defined | Body or frontmatter contains a concrete, non-empty `input` value |
| H08 | Expected output or assertion | At least one assertion specifies a concrete expected result or a checkable condition |
| H09 | Target component identified | `target` names a specific artifact (not "the system" or "the model") |
| H10 | No pipeline testing | Eval tests one component only; no chained multi-step workflows |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | Eval is tight; no filler prose or restatements of the obvious |
| Setup and teardown documented | 0.5 | `setup` and `teardown` steps are present even if empty (explicit null is acceptable) |
| Assertions are deterministic | 1.0 | Each assertion produces the same pass/fail result on every run |
| Coverage mapped to quality gates | 1.0 | Each assertion references at least one gate ID from the target's QUALITY_GATES.md |
| Isolation from external dependencies | 1.0 | No live API calls, file system writes, or database reads in the eval body |
| Tags include unit-eval | 0.5 | `tags` list contains `"unit-eval"` |
| Edge cases included | 0.5 | At least one assertion targets a boundary or failure condition |
| Regression tracking enabled | 0.5 | `regression_id` or equivalent field links this eval to a known past failure |
| Execution time reasonable | 0.5 | Expected runtime is documented and is under 30 seconds |
| Assertions are specific | 1.0 | No vague assertions like "output is correct" or "response is good" |
Sum of weights: 7.5. `soft_score = sum(weight * gate_score) / 7.5 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as reference unit eval |
| >= 8.0 | PUBLISH — safe to run in CI and quality pipelines |
| >= 7.0 | REVIEW — runnable but coverage or isolation needs improvement |
| < 7.0 | REJECT — do not run; assertions are ambiguous or component not isolated |
## Bypass
| Field | Value |
|-------|-------|
| condition | Target component is under active construction and its interface is not yet stable; eval is written speculatively |
| approver | Engineer who owns the target component |
| audit_log | Entry required in `.claude/bypasses/unit_eval_{date}.md` with the expected stabilization date |
| expiry | Until the target component reaches PUBLISH score; eval must be updated and re-gated at that point |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.
