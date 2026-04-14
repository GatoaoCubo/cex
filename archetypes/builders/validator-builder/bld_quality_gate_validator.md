---
id: p11_qg_validator
kind: quality_gate
pillar: P06
title: "Gate: Validator"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: validator
quality: 9.0
density_score: 0.85
tags:
  - quality-gate
  - validator
  - rules
  - P06
tldr: "Validates technical pass/fail rules for artifact checking: condition structure, severity, and target kind."
llm_function: GOVERN
---
## Definition
A validator defines one or more pass/fail rules applied to an artifact. Each rule has a condition (field, operator, value), a severity (error, warning, or info), and a target artifact kind. Validators do not score — they pass or fail. This gate ensures every validator is structurally sound, has actionable error messages, and is safe to run automatically.
## HARD Gates
Failure on any HARD gate causes immediate REJECT. No score is computed.
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter is valid and complete with no syntax errors |
| H02 | ID matches namespace | `id` matches pattern `^p06_val_[a-z][a-z0-9_]+$` |
| H03 | ID equals filename | `id` slug matches the parent directory or filename stem |
| H04 | Kind matches literal | `kind` is exactly `validator` |
| H05 | Quality is null | `quality` field is `null` (not yet scored) |
| H06 | Required fields present | `target_kind`, `conditions`, `severity` all defined and non-empty |
| H07 | Condition structure valid | Each condition has `field`, `operator`, and `value` keys |
| H08 | Severity is valid enum | `severity` is one of: `error`, `warning`, `info` |
| H09 | Target artifact kind identified | `target_kind` names a specific artifact kind, not a generic scope |
| H10 | No scoring logic | Validator body contains no weighted scores, rubrics, or 0-10 scales |
## SOFT Scoring
Score each dimension 0 or 10. Multiply by weight. Divide total by sum of weights, scale to 0-10.
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Density >= 0.80 | 1.0 | No prose restating what the condition table shows |
| Standard operators only | 1.0 | Operators from: `eq`, `neq`, `gt`, `lt`, `gte`, `lte`, `regex`, `in`, `not_in` |
| Severity justification present | 0.5 | Each severity level has a brief reason |
| Auto_fix feasibility noted | 0.5 | `auto_fix: true` conditions describe what the fix does |
| Bypass policy present | 0.5 | Body includes a bypass section, even if `bypass: null` |
| Tags include validator | 0.5 | `tags` contains `"validator"` |
| Pipeline position documented | 1.0 | Body states when this runs (pre-commit, post-generate, pre-publish) |
| Error messages are actionable | 1.0 | Each message tells the developer what to fix, not just what is wrong |
| Performance impact minimal | 0.5 | Conditions require no external calls, file reads, or LLM inference |
| No scoring in validator | 1.0 | Pass/fail outcomes only; no weighted scores or rubrics |
Sum of weights: 7.5. `soft_score = sum(weight * gate_score) / 7.5 * 10`
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — archive to pool as reference validator |
| >= 8.0 | PUBLISH — safe to run in automated pipelines |
| >= 7.0 | REVIEW — runnable but error messages or pipeline placement needs clarification |
| < 7.0 | REJECT — do not run; conditions are ambiguous or severity is unjustified |
## Bypass
| Field | Value |
|-------|-------|
| condition | Validator targets a new artifact kind whose field structure is still being finalized; conditions may be temporarily incomplete |
| approver | Engineer who owns the target artifact kind |
| audit_log | Entry required in `.claude/bypasses/validator_{date}.md` listing which conditions are not yet enforced |
| expiry | Until target kind's QUALITY_GATES.md reaches PUBLISH score; validator must be updated at that point |
H01 (frontmatter parses) and H05 (quality is null) cannot be bypassed under any condition.
