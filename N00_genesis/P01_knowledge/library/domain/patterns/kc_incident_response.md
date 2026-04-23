---
id: p01_kc_incident_response
kind: knowledge_card
type: domain
pillar: P01
title: "Incident Response"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n01_research
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, incident, response, triage, sre, postmortem, recovery]
tldr: "Detect, triage, mitigate, resolve, postmortem. P1=auto-rollback, P2=auto-debug, P3=next session, P4=backlog. Every incident produces a learning record."
when_to_use: "When a tool crashes, a pipeline fails, quality drops below threshold, or user reports a regression."
keywords: [incident, response, triage, sre, postmortem, rollback, recovery]
density_score: 0.95
related:
  - p01_kc_self_healing_skill
  - p10_lr_bugloop_builder
  - p12_wf_auto_debug
  - p01_kc_feedback_loops
  - bld_knowledge_card_bugloop
  - p01_kc_orchestration_best_practices
  - p12_wf_auto_diagnose
  - p12_wf_auto_review
  - p01_kc_cex_orchestration_architecture
  - p12_wf_orchestration_pipeline
---

# Incident Response

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | Structured response to failures: detect → triage → mitigate → resolve → learn |
| Trigger | Tool crash, pipeline failure, quality regression, user report |
| Benefit | Minimizes blast radius, captures learnings, prevents recurrence |
| Risk if skipped | Cascading failures, repeated incidents, no institutional memory |

## Priority Levels

| Level | Impact | Response Time | Strategy | Example |
|-------|--------|--------------|----------|---------|
| P1 | System down / data loss | Immediate | Auto-rollback via git | `cex_compile.py` crashes on all files |
| P2 | Feature broken | Same session | Auto-debug + targeted fix | Builder produces invalid YAML |
| P3 | Quality degraded | Next session | Schedule improvement pass | Scores drop from 9.0 to 8.5 |
| P4 | Cosmetic / minor | Backlog | Track for batch fix | Formatting inconsistency |

## Response Protocol

| Phase | Action | Output | Owner |
|-------|--------|--------|-------|
| 1. Detect | Monitor signals, parse errors, check quality | Incident ticket | Automated / User |
| 2. Triage | Classify priority (P1-P4), assess blast radius | Priority + scope | N07 or active nucleus |
| 3. Mitigate | Stop bleeding (rollback, disable, isolate) | Stable state | Assigned nucleus |
| 4. Diagnose | Root cause analysis (logs, diffs, reproduce) | Root cause statement | N01 or N05 |
| 5. Resolve | Apply fix, validate, deploy | Fixed artifact | N03 or N05 |
| 6. Postmortem | Document what happened, why, prevention | Learning record | N01 |

## Mitigation Strategies

| Strategy | When | Command |
|----------|------|---------|
| Git rollback | Bad commit broke artifacts | `git revert HEAD` |
| Nucleus kill | Stuck/looping nucleus | `bash _spawn/dispatch.sh stop n03` |
| Signal override | Wrong signal propagated | `signal_writer.py` → manual signal |
| Config disable | Feature flag causing issues | Edit `P09_config/` |
| Isolate scope | Blast radius spreading | Process only affected pillar |

## Postmortem Template

```yaml
incident_id: INC_YYYYMMDD_NNN
priority: P2
detected: 2026-04-07T15:00:00
resolved: 2026-04-07T15:30:00
root_cause: "UTF-8 encoding mismatch in cex_compile.py"
impact: "12 artifacts failed compilation"
fix: "Added encoding='utf-8' to all file opens"
prevention: "Pre-commit hook validates encoding"
learning_record: ".cex/learning_records/lr_encoding_fix.md"
```

## Escalation Matrix

| Condition | Escalate To |
|-----------|------------|
| P1 not resolved in 5 min | User (immediate) |
| P2 not resolved in 1 session | User (end of session) |
| Same incident 3x | Architecture review (N07) |
| Cross-nucleus impact | N07 orchestrator |
| Data loss suspected | User + git forensics |

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| Hero debugging | One nucleus works alone, no visibility |
| Fix without postmortem | Same incident recurs next week |
| Over-triaging P4s as P1 | Everything urgent = nothing urgent |
| Rollback without diagnosis | Fixes symptom, root cause persists |
| Skipping mitigation for fix | Blast radius expands while debugging |

## Linked Artifacts

- `p01_kc_self_healing_skill` — automated fix attempts before escalation
- `p01_kc_gap_detection` — find structural causes of recurring incidents
- `p01_kc_test_automation` — prevent incidents through automated testing

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_self_healing_skill]] | sibling | 0.27 |
| [[p10_lr_bugloop_builder]] | downstream | 0.26 |
| [[p12_wf_auto_debug]] | downstream | 0.26 |
| [[p01_kc_feedback_loops]] | sibling | 0.26 |
| [[bld_knowledge_card_bugloop]] | sibling | 0.24 |
| [[p01_kc_orchestration_best_practices]] | sibling | 0.24 |
| [[p12_wf_auto_diagnose]] | downstream | 0.22 |
| [[p12_wf_auto_review]] | downstream | 0.22 |
| [[p01_kc_cex_orchestration_architecture]] | sibling | 0.22 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.22 |
