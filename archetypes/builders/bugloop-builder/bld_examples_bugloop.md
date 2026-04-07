---
kind: examples
id: bld_examples_bugloop
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of bugloop artifacts
quality: 9.0
title: "Examples Bugloop"
version: "1.0.0"
author: n03_builder
tags: [bugloop, builder, examples]
tldr: "Golden and anti-examples for bugloop construction, demonstrating ideal structure and common pitfalls."
domain: "bugloop construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

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
