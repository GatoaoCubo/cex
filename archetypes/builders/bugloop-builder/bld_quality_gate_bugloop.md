---
id: p11_qg_bugloop
kind: quality_gate
pillar: P11
title: "Gate: bugloop"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "automated correction cycles — detect, fix, verify loops for regression prevention"
quality: 9.0
tags: [quality-gate, bugloop, P11, correction-cycle, auto-fix, verification]
tldr: "Pass/fail gate for bugloop artifacts: correction cycle completeness, fix strategy safety, and verification assertion coverage."
density_score: 0.92
llm_function: GOVERN
---
# Gate: bugloop
## Definition
| Field | Value |
|---|---|
| metric | bugloop artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: bugloop` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | `id: my_loop` but file is `other_loop.md` |
| H04 | Kind equals literal `bugloop` | `kind: workflow` or any other value |
| H05 | Quality field is null | `quality: 8.5` or any non-null value |
| H06 | All required fields present | Missing `detection`, `fix_strategy`, or `verification` |
| H07 | Detection section has at least one trigger | `triggers: []` or triggers field absent |
| H08 | Fix strategy has `max_attempts` defined | `max_attempts` absent or zero |
| H09 | Verification section has at least one assertion | `assertions: []` or assertions field absent |
| H10 | Escalation threshold defined | No escalation target when `max_attempts` exhausted |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Detection precision | 1.0 | Triggers are specific (regex patterns, error signatures) not vague strings |
| Fix strategy safety | 1.0 | `auto_fix` calibrated by confidence; destructive ops require high confidence threshold |
| Max attempts boundary | 0.5 | `max_attempts` is finite and reasonable (1-10 range) |
| Verification coverage | 1.0 | Assertions cover the fix target, not just smoke checks |
| Assertion timeout bounds | 0.5 | Each assertion has explicit timeout or global timeout defined |
| Rollback policy | 1.0 | Rollback defined for each fix strategy that mutates state |
| Escalation targets | 1.0 | Escalation target is actionable (human queue, alert channel, system endpoint) |
| Scope isolation | 0.5 | Loop scope bounded — does not modify unrelated system state |
| Error classification | 0.5 | Distinguishes transient errors (retry) from permanent errors (escalate) |
| Idempotency guarantee | 1.0 | Re-running the loop on an already-fixed state is safe and documented |
| Domain specificity | 1.0 | Detection triggers and assertions are specific to the declared domain |
| Documentation | 0.5 | Rationale for `max_attempts` value and confidence thresholds explained |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Emergency hotfix loop for production incident already verified manually |
| approver | Senior engineer on-call + team lead sign-off |
| audit_trail | Bypass reason logged in artifact comment block with incident ID |
| expiry | 72h — artifact must reach >= 7.0 within 72h or be retired |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |
