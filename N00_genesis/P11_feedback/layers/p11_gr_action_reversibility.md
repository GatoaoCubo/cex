---
id: p11_gr_action_reversibility
kind: guardrail
8f: F7_govern
pillar: P11
title: "Guardrail: Action Reversibility Check"
version: 1.0.0
quality: 9.0
severity: high
enforcement: confirm
tags: [guardrail, reversibility, safety, destructive, confirmation]
tldr: "Safety guardrail requiring confirmation before irreversible or high-risk actions. Classifies actions by reversibility and enforces appropriate gates."
domain: "feedback"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.92
related:
  - p03_ins_action_protocol
  - bld_examples_guardrail
  - p09_perm_stella_allow_block
  - p12_wf_auto_rollback
  - p01_kc_git_worktree_isolation
  - kc_git_workflow_for_agents
  - p12_wf_auto_ship
  - p12_wf_auto_security
  - p12_wf_auto_health
  - p04_ct_changelog_gen
---

# Action Reversibility Guardrail

## Classification Matrix

| Action Type | Reversibility | Gate |
|------------|---------------|------|
| Read file, search code | None needed | ALLOW |
| Create new file | Easy (git rm) | ALLOW |
| Edit existing file | Easy (git restore) | ALLOW |
| Git commit | Medium (git revert) | ALLOW |
| Delete file | Hard (may lose untracked) | CONFIRM |
| Git push | Hard (others may pull) | CONFIRM |
| Force push | Very hard (rewrites history) | BLOCK unless explicit |
| Git reset --hard | Very hard (loses uncommitted) | BLOCK unless explicit |
| Drop database table | Irreversible | BLOCK |
| Send external message | Irreversible | CONFIRM |
| Publish content | Hard to retract | CONFIRM |

## Enforcement Rules

### ALLOW Actions
- Proceed without confirmation
- Log action for audit trail

### CONFIRM Actions
- Present action description to user
- Show what will be affected (files, systems, people)
- Wait for explicit approval before proceeding
- If denied, suggest safer alternative

### BLOCK Actions
- Do not execute under any circumstances
- Explain why the action is blocked
- Suggest reversible alternative
- Exception: user explicitly uses override language ("force push", "yes delete")

## Safe Alternatives

| Risky Action | Safe Alternative |
|-------------|-----------------|
| git reset --hard | git stash |
| rm -rf directory | git clean -n (dry run first) |
| force push | Regular push + PR |
| DROP TABLE | Rename table + verify before drop |
| Overwrite file | Create backup copy first |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_action_protocol]] | upstream | 0.41 |
| [[bld_examples_guardrail]] | upstream | 0.27 |
| [[p09_perm_stella_allow_block]] | upstream | 0.25 |
| [[p12_wf_auto_rollback]] | downstream | 0.22 |
| [[p01_kc_git_worktree_isolation]] | upstream | 0.22 |
| [[kc_git_workflow_for_agents]] | upstream | 0.21 |
| [[p12_wf_auto_ship]] | downstream | 0.20 |
| [[p12_wf_auto_security]] | downstream | 0.18 |
| [[p12_wf_auto_health]] | downstream | 0.17 |
| [[p04_ct_changelog_gen]] | upstream | 0.17 |
