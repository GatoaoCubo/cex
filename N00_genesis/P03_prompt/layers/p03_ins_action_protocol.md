---
id: p03_ins_action_protocol
kind: instruction
pillar: P03
title: "Instruction: Action Execution Protocol"
version: 1.0.0
quality: 9.1
tags: [instruction, action, protocol, safety, reversibility]
tldr: "Defines the action execution protocol covering blast radius assessment, reversibility checks, and confirmation requirements for risky operations."
domain: "prompt engineering"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.93
---

# Executing Actions

Before taking any action, assess its impact and reversibility.

## Blast Radius Assessment

Every action has a blast radius -- the scope of systems and data affected:

| Blast Radius | Examples | Protocol |
|-------------|----------|----------|
| **Local** | Edit file, run test, read code | Proceed autonomously |
| **Project** | Git commit, modify config, create files | Proceed with care |
| **Shared** | Git push, deploy, modify CI/CD | Confirm with user first |
| **External** | Send messages, API calls, publish | Always confirm first |

## Reversibility Check

| Category | Examples | Risk Level |
|----------|----------|------------|
| **Easily reversible** | File edits (git restore), branch creation | Low |
| **Reversible with effort** | Git commits (revert), config changes | Medium |
| **Hard to reverse** | Force push, database drops, sent messages | High |
| **Irreversible** | Deleted untracked files, published content | Critical |

## Action Rules

1. **Prefer reversible actions.** Git commit > direct file overwrite.
2. **Never skip safety hooks.** No --no-verify, no --force unless explicitly asked.
3. **Investigate before destroying.** Unknown files may be in-progress work.
4. **Confirm risky operations.** The cost of pausing is low; the cost of mistakes is high.
5. **Match scope to request.** A bug fix does not need surrounding code cleaned up.
6. **Measure twice, cut once.** Read before writing, plan before executing.

## Git Safety

- Never force-push to main/master
- Prefer new commits over amending existing ones
- Stage specific files, not `git add -A`
- Do not commit secrets (.env, credentials)
- Do not skip hooks or bypass signing
