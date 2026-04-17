---
id: p11_gr_action_reversibility
kind: guardrail
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
