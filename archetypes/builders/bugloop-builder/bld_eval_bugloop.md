---
kind: quality_gate
id: p11_qg_bugloop
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of bugloop artifacts
quality: 9.0
title: "Gate: bugloop"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, bugloop, P11, correction-cycle, auto-fix, verification]
tldr: "Pass/fail gate for bugloop artifacts: correction cycle completeness, fix strategy safety, and verification assertion coverage."
domain: "automated correction cycles — detect, fix, verify loops for regression prevention"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.92
related:
  - bld_examples_bugloop
  - bld_instruction_bugloop
  - bugloop-builder
  - p01_kc_bugloop
  - p03_sp_bugloop_builder
  - bld_collaboration_bugloop
  - p10_lr_bugloop_builder
  - p11_qg_chunk_strategy
  - bld_knowledge_card_bugloop
  - bld_output_template_bugloop
---

## Quality Gate

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

## Examples

# Examples: bugloop-builder
## Golden Example
INPUT: "Create bugloop for detectar e corrigir failss de validation no KC pipeline automaticamente"
OUTPUT:
```yaml
id: p11_bl_kc_pipeline
kind: bugloop
pillar: P11
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "orchestrator"
domain: "knowledge_card_pipeline"
quality: null
tags: [bugloop, knowledge-card, test-failure, auto-fix]
tldr: "Auto-correct KC validation failures: detect test failure > patch frontmatter > re-run suite"
scope: "KC pipeline — validate_kc.py execution on pre-commit and scheduled runs"
detect:
  method: "test_failure"
  trigger: "on_commit"
  pattern: "FAILED tests/test_validate_kc\\.py::test_[a-z_]+"
fix:
  strategy: "patch_and_retry"
  auto_fix: true
  max_attempts: 3
verify:
  test_suite: "tests/test_validate_kc.py"
  assertions:
    - "exit_code == 0"
    - "no FAILED lines in stdout"
    - "validate_kc.py returns score >= 8.0"
  timeout: 120
cycle_count: 5
auto_fix: true
escalation:
  threshold: 3
  target: "signal_bus:bugloop_escalation"
confidence: 0.88
test_suite: "tests/test_validate_kc.py"
rollback:
  enabled: false
  strategy: "git_revert"
## Detection
Trigger fires on every commit via pre-commit hook calling validate_kc.py.
Pattern `FAILED tests/test_validate_kc\.py::test_[a-z_]+` matches pytest output.
Sources: pytest stdout, pre-commit hook exit code != 0.
Known failure classes: missing required frontmatter fields, id/filename mismatch,
quality != null, body sections absent, byte limit exceeded.
## Fix Strategy
Auto-fix is enabled (confidence 0.88) because KC failures are deterministic and
all known failure classes have reversible patch actions:
- missing field: inject default value from SCHEMA.md
- id mismatch: rename file to match id stem
- quality != null: set quality to null
- byte limit: truncate body at 4096 bytes preserving all sections
Max 3 attempts before escalation. patch_and_retry chosen because KC artifacts
are idempotent — re-applying patch is safe.
## Verification
Suite: tests/test_validate_kc.py (full suite, not subset).
Pass: all 3 assertions must hold. Timeout 120s covers full suite on slow CI.
If verify fails after successful fix attempt: increment cycle, try again.
## Escalation
Fires at cycle 3 (of 5 max). Target: signal_bus:bugloop_escalation.
Payload includes: artifact_id, failure_pattern matched, attempts made,
last pytest stdout, fix patches applied.
Human review required when escalation fires.
## Rollback
Disabled for KC pipeline — patch_and_retry strategy is reversible.
git_revert defined as fallback if rollback is manually enabled.
Trigger condition: N/A (rollback.enabled = false).
```
## Anti-Example
```yaml
id: fix_kc_bugs
kind: bugloop
quality: 9.5
This bugloop will find and fix any bugs in the KC system.
Run tests, if they fail fix them and try again.
```
FAILURES:
1. [H02] id: missing p11_bl_ prefix — id must start with p11_bl_
2. [H05] pillar: missing — P11 required
3. [H06] quality: self-scored 9.5 — must be null always
4. [H07] detect object: missing entirely — method, trigger, pattern all absent
5. [H08] fix object: missing — no strategy, auto_fix, or max_attempts defined
6. [H11] confidence: missing — cannot assess auto-fix safety without confidence float
7. [H13] verify.assertions: missing — no pass criteria means verification is undefined
8. [H14] rollback object: missing — no rollback policy for failure recovery
9. [H09] cycle_count: missing — escalation threshold cannot be validated
10. [INVARIANT] "fix any bugs": non-specific detect.pattern matches everything, fixes nothing reliably

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
