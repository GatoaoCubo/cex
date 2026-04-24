---
id: p01_kc_feedback_loops
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Feedback Loops — Bug Loops, Lifecycle Rules for Continuous Improvement"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: feedback_loops
origin: manual
quality: 9.1
tags: [feedback, bugloop, lifecycle, self-healing, regression, continuous-improvement, hooks]
tldr: "Feedback loops encode detect-diagnose-fix cycles and lifecycle rules that drive autonomous self-improvement in agent systems"
when_to_use: "Implementing automated bug detection, self-healing code, lifecycle hooks, or continuous improvement pipelines"
keywords: [bugloop, lifecycle-rule, self-healing, regression, feedback, detect-fix, hook]
long_tails:
  - "How to implement autonomous detect-diagnose-fix cycles for agent self-healing"
  - "Which lifecycle hook patterns enable continuous improvement without human intervention"
axioms:
  - "Every failure is a learning opportunity — bugloops must capture the fix pattern, not just the fix"
  - "Lifecycle rules are event-driven — hooks fire on state transitions, never on polling intervals"
linked_artifacts:
  primary: null
  related: [p01_kc_eval_testing, p01_kc_memory_persistence, p01_kc_reward_and_alignment]
feeds_kinds:
  - bugloop          # Detect-diagnose-fix cycles with automated regression prevention
  - lifecycle_rule   # Event-driven hooks for state transitions (pre/post tool, session start/end)
density_score: 0.86
related:
  - bugloop-builder
  - p10_lr_bugloop_builder
  - p01_kc_self_healing_skill
  - p12_wf_auto_debug
  - p01_kc_bugloop
  - bld_architecture_bugloop
  - p01_kc_git_hooks_ci
  - bld_collaboration_bugloop
  - bld_examples_bugloop
  - bld_knowledge_card_bugloop
---

# Feedback Loops

## Quick Reference
```yaml
topic: Feedback Loops (bugloops, lifecycle rules)
scope: Detect-diagnose-fix cycles, automated regression, lifecycle hooks, self-healing
source: manual (organization bugloop, Claude Code hooks, test-guardian patterns)
criticality: high
```

## Key Concepts

| Concept | Domain | CEX Kind | Role |
|---------|--------|----------|------|
| Bug Loop | Self-Healing | bugloop | Autonomous detect -> diagnose -> fix -> validate -> commit cycle |
| Lifecycle Rule | Event Hooks | lifecycle_rule | Pre/post event hooks that enforce constraints or trigger actions |

## Bug Loop Pattern

```text
[DETECT] -> [DIAGNOSE] -> [FIX] -> [VALIDATE] -> [COMMIT] -> [LEARN]
  error      root cause    patch     test pass     git add     record
  signal     5-Why         minimal   regression    commit      learning_record
```

### Stages

| Stage | Input | Output | Max Duration |
|-------|-------|--------|-------------|
| Detect | Error signal, test failure, exception | Classified error type + stack trace | 10s |
| Diagnose | Error context | Root cause + affected files + fix hypothesis | 30s |
| Fix | Diagnosis | Minimal code patch (smallest possible change) | 60s |
| Validate | Patched code | Test suite pass + no new regressions | 120s |
| Commit | Validated fix | Git commit with structured message | 10s |
| Learn | Commit + diagnosis | learning_record with pattern + anti-pattern | 10s |

## Lifecycle Rules

| Event | Hook Type | Example Rule |
|-------|-----------|-------------|
| SessionStart | pre-session | Load mental model, check stale indexes, verify MCP connections |
| PreToolUse | pre-action | RLM probe on large files, permission check, budget validation |
| PostToolUse | post-action | Confidence scoring, token tracking, result validation |
| Stop | pre-exit | Signal write, commit uncommitted work, resource cleanup |
| SubagentStop | post-child | Collect results, update parent state, check quality gate |
| PermissionRequest | pre-approve | Scope fence validation, dangerous action blocking |

## Patterns

| Trigger | Action |
|---------|--------|
| Test failure detected | Initiate bugloop: classify error -> diagnose -> generate fix -> run tests |
| 3 consecutive failures on same file | Escalate: mark file as high-risk, require human review |
| Lifecycle event fires | Execute all registered hooks in priority order, fail-fast on critical |
| Fix validated successfully | Record learning_record with fix pattern for future similar errors |
| Regression detected post-fix | Revert fix, re-enter diagnose with expanded context |

## Anti-Patterns

- Fixing symptoms instead of root causes (patch without diagnosis)
- Bugloops without max retry limits (infinite fix loops)
- Lifecycle rules that modify state in pre-hooks (side effects before action)
- Missing regression validation after fix (fix one bug, introduce another)
- Learning records without the failing context (can't reproduce to verify)

## organization Integration

| Component | Role | Kind |
|-----------|------|------|
| `/bugloop` command | Orchestrates detect-fix-validate cycle | bugloop |
| Claude Code hooks | 10 lifecycle events in `.claude/settings.json` | lifecycle_rule |
| test-guardian-agent | Periodic test patrol + auto-fix trivial errors | bugloop |
| self-healing-code-agent | Iterative test-fix-validate loops | bugloop |
| signal_writer.py | Completion/failure signals for lifecycle monitoring | lifecycle_rule |

## References

- related: p01_kc_eval_testing, p01_kc_reward_and_alignment
- patterns: organization bugloop, Claude Code hooks, self-healing code, test guardian

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bugloop-builder]] | downstream | 0.36 |
| [[p10_lr_bugloop_builder]] | downstream | 0.36 |
| [[p01_kc_self_healing_skill]] | sibling | 0.35 |
| [[p12_wf_auto_debug]] | downstream | 0.33 |
| [[p01_kc_bugloop]] | sibling | 0.33 |
| [[bld_architecture_bugloop]] | downstream | 0.33 |
| [[p01_kc_git_hooks_ci]] | sibling | 0.32 |
| [[bld_collaboration_bugloop]] | downstream | 0.32 |
| [[bld_examples_bugloop]] | downstream | 0.32 |
| [[bld_knowledge_card_bugloop]] | sibling | 0.32 |
