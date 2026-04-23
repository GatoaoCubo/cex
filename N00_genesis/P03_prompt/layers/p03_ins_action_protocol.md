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
related:
  - p11_gr_action_reversibility
  - p01_kc_git_hooks_ci
  - kc_git_workflow_for_agents
  - p12_wf_auto_security
  - p01_kc_git_worktree_isolation
  - p12_wf_auto_ship
  - bld_examples_guardrail
  - kc_aider_integration_patterns
  - bld_output_template_contributor_guide
  - bld_examples_skill
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_gr_action_reversibility]] | downstream | 0.47 |
| [[p01_kc_git_hooks_ci]] | upstream | 0.27 |
| [[kc_git_workflow_for_agents]] | upstream | 0.26 |
| [[p12_wf_auto_security]] | downstream | 0.24 |
| [[p01_kc_git_worktree_isolation]] | upstream | 0.22 |
| [[p12_wf_auto_ship]] | downstream | 0.21 |
| [[bld_examples_guardrail]] | downstream | 0.21 |
| [[kc_aider_integration_patterns]] | upstream | 0.20 |
| [[bld_output_template_contributor_guide]] | downstream | 0.20 |
| [[bld_examples_skill]] | downstream | 0.19 |
