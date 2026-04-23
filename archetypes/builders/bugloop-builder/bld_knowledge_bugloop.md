---
kind: knowledge_card
id: bld_knowledge_card_bugloop
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for bugloop production — automated correction cycles
sources: Google SRE Book ch.13, DORA MTTR metric, chaos engineering principles
quality: 9.1
title: "Knowledge Card Bugloop"
version: "1.0.0"
author: n03_builder
tags: [bugloop, builder, examples]
tldr: "Golden and anti-examples for bugloop construction, demonstrating ideal structure and common pitfalls."
domain: "bugloop construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_bugloop
  - p10_lr_bugloop_builder
  - bld_instruction_bugloop
  - bld_examples_bugloop
  - p03_sp_bugloop_builder
  - bld_architecture_bugloop
  - bugloop-builder
  - p01_kc_feedback_loops
  - p11_qg_bugloop
  - bld_config_bugloop
---

# Domain Knowledge: bugloop
## Executive Summary
Bugloops implement automated detect-fix-verify cycles that minimize Mean Time To Recovery (MTTR) for known failure patterns. They apply fix strategies calibrated by confidence level, verify via test suites, and escalate to humans when automation confidence is low. Bugloops differ from quality gates (pass/fail barriers), optimizers (metric-driven improvement), and guardrails (safety prevention).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P11 (governance/safety) |
| Core cycle | detect → fix → verify → commit/escalate |
| Fix strategies | patch_and_retry, rollback_first, isolate_then_fix |
| Escalation trigger | max_attempts reached or confidence below threshold |
| Rollback | optional, triggered on fix failure when enabled |
| Frontmatter fields | 15+ |
## Patterns
- **Detect-Fix-Verify cycle**: signal fires → apply fix strategy → run test suite → commit on pass or escalate on fail
```
DETECT (pattern match) → FIX (strategy, attempt N)
  ├─ success → VERIFY (test_suite)
  │             ├─ pass → COMMIT
  │             └─ fail → retry or ESCALATE
  ├─ max_attempts → ESCALATE
  └─ rollback_enabled → ROLLBACK then ESCALATE
```
- **Confidence calibration**: match confidence to domain risk
| Domain | Confidence | Rationale |
|--------|-----------|-----------|
| Linting/style errors | 0.95 | Deterministic, no side effects |
| Test fixture failures | 0.85 | Known patterns, low blast radius |
| API schema drift | 0.75 | Requires schema diffing accuracy |
| Runtime memory leaks | 0.55 | Non-deterministic, prefer manual |
| Data corruption | 0.30 | High stakes, always manual |
- **Detection methods**: static_analysis (on_commit), test_failure (on_commit), runtime_trace (continuous), log_scan (scheduled)
- **Fix strategy selection**: patch_and_retry for known deterministic bugs; rollback_first for unknown root cause; isolate_then_fix for modular failures
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Inflated confidence (0.95 for non-deterministic) | Silent bad fixes; worse than no fix |
| escalation.threshold > cycle_count | Escalation becomes unreachable |
| rollback strategy + rollback disabled | Contradiction blocks recovery |
| detect.pattern=".*" | Catches everything, fixes nothing useful |
| Empty verify.assertions | Verification has no pass criteria |
| No max_attempts limit | Infinite retry loop on unfixable bug |
## Application
1. Identify failure pattern: what known signal triggers this bugloop?
2. Select detection method: static analysis, test failure, log scan, or runtime trace
3. Calibrate confidence: what is the probability this fix is correct? (see table)
4. Choose fix strategy: patch_and_retry vs rollback_first vs isolate_then_fix
5. Define verification: test suite, assertions, timeout bounds
6. Set escalation: max_attempts, target (human/queue), rollback policy
## References
- Google SRE Book ch.13: emergency response and toil reduction
- DORA: MTTR as key metric for recovery performance
- Chaos engineering: known failure modes should have automated recovery
- Netflix Hystrix: circuit breaker pattern for cascading failure prevention

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_bugloop]] | sibling | 0.57 |
| [[p10_lr_bugloop_builder]] | downstream | 0.47 |
| [[bld_instruction_bugloop]] | downstream | 0.46 |
| [[bld_examples_bugloop]] | downstream | 0.45 |
| [[p03_sp_bugloop_builder]] | downstream | 0.43 |
| [[bld_architecture_bugloop]] | downstream | 0.42 |
| [[bugloop-builder]] | downstream | 0.40 |
| [[p01_kc_feedback_loops]] | sibling | 0.34 |
| [[p11_qg_bugloop]] | downstream | 0.34 |
| [[bld_config_bugloop]] | downstream | 0.34 |
