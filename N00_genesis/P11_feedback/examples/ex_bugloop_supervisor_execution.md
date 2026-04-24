---
id: p11_bl_agent_group_execution
kind: bugloop
8f: F7_govern
pillar: P11
title: "Bugloop: Agent_group Execution Resilience"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
quality: 9.0
tags: [agent_group, resilience, bugloop, feedback]
tldr: "3-retry bugloop for agent_group task execution — never stop on first error, skip after 3 failures, always commit partial work"
density_score: 0.90
source: organization-core/.claude/rules/agent_group-execution.md
related:
  - p12_wf_auto_debug
  - p12_wf_stella_dispatch
  - p01_kc_handoff
  - p01_kc_feedback_loops
  - bld_knowledge_card_handoff
  - p01_kc_bugloop
  - p11_qg_skill
  - p01_kc_self_healing_skill
  - p08_pat_3phase_build_protocol
  - bld_instruction_handoff
---

# Bugloop: Agent_group Execution Resilience

## Trigger

| Property | Value |
|----------|-------|
| Detect | Any error during agent_group task execution (file not found, command failed, import error, git conflict, permission denied, timeout) |
| Condition | `organization_AGENT_GROUP` is set and NOT stella |
| Frequency | Every task step, checked after each action |

## Cycle

```
[DETECT] --> [ANALYZE] --> [FIX] --> [VERIFY] --> [COMMIT]
                |                       |
           [root cause]          [RETRY if fail]
                                   (max 3)
```

### Phase 1: Detect
- Signal: Non-zero exit code, exception, missing file, tool error
- Data: stderr output, error message, file paths involved

### Phase 2: Analyze
- Root cause method: Read stderr, check path existence, verify dependencies
- Context needed: Current working directory, git status, installed packages

### Phase 3: Fix
- Strategy: Adjust command, fix path, create missing file, install dependency
- Fallback: Try completely different approach (alternative command, different path, simplify scope)
- Scope: Same files as original task

### Phase 4: Verify
- Command: Re-run the original action that failed
- Expected: Zero exit code, expected output file exists
- Timeout: 300s max per retry

### Phase 5: Commit
- Message: `"feat: T1+T2 complete, T3 failed (file not found after 3 attempts)"`
- Files: All work completed so far (even partial)

## Limits

| Limit | Value | On Exceed |
|-------|-------|-----------|
| Max retries | 3 | Skip task, move to next, log failure |
| Max duration | 5 min per retry | Move to next task |
| Max files touched | per scope fence | Respect SOMENTE/NAO TOQUE boundaries |

## Escalation

- After 3 failures: Register error, SKIP to next task, continue execution
- Owner: orchestrator (reviews via signal + git log after agent_group completes)

---
*Migrated from: organization-core/.claude/rules/agent_group-execution.md (Resilience Protocol)*

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_auto_debug]] | downstream | 0.29 |
| [[p12_wf_stella_dispatch]] | downstream | 0.28 |
| [[p01_kc_handoff]] | downstream | 0.27 |
| [[p01_kc_feedback_loops]] | upstream | 0.23 |
| [[bld_knowledge_card_handoff]] | upstream | 0.23 |
| [[p01_kc_bugloop]] | related | 0.22 |
| [[p11_qg_skill]] | related | 0.22 |
| [[p01_kc_self_healing_skill]] | upstream | 0.21 |
| [[p08_pat_3phase_build_protocol]] | upstream | 0.21 |
| [[bld_instruction_handoff]] | upstream | 0.21 |
