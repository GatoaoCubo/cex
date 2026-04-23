---
id: p01_kc_git_worktree_isolation
kind: knowledge_card
pillar: P01
title: "Git Worktree Isolation — Parallel Agent Workspaces Without Conflict"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: dev_tooling
quality: 9.1
tags: [git-worktree, isolation, parallel-agents, branch-management, workspace]
tldr: "Git worktrees give each parallel agent an isolated directory and branch, eliminating merge conflicts in concurrent work"
when_to_use: "Multiple agents or developers need to work on the same repo simultaneously without interference"
keywords: [git-worktree, parallel-development, branch-isolation, multi-agent]
long_tails:
  - "How to use git worktrees for parallel agent development"
  - "How to avoid merge conflicts with multiple agents on one repo"
axioms:
  - "NEVER start implementation on main without explicit user consent"
  - "ALWAYS verify test baseline passes before starting work in a worktree"
linked_artifacts:
  primary: null
  related: []
density_score: null
data_source: "https://git-scm.com/docs/git-worktree"
related:
  - kc_git_workflow_for_agents
  - batch
  - bld_output_template_contributor_guide
  - p11_gr_action_reversibility
  - p03_ins_action_protocol
  - bld_examples_skill
  - p11_qg_tdd_compliance
  - p12_wf_auto_ship
  - p01_kc_orchestration_best_practices
  - p04_ct_changelog_gen
---

## TL;DR

Git worktrees create multiple working directories for one repository, each on a separate branch. For parallel LLM agents, this eliminates file conflicts, preserves clean git history, and isolates failures — one agent's crash never pollutes another's work.

## Conceito Central

A worktree is a physical checkout of a branch in a separate directory, sharing the same `.git` object store. Unlike cloning, worktrees share history and objects with zero duplication. Each agent operates in its own directory with its own branch — changes are invisible to other agents until explicit merge or PR.

The lifecycle has 3 phases: setup (create branch + worktree + verify baseline), implementation (normal commits in isolation), and finalization (merge/PR/cleanup with 4 explicit user options).

## Arquitetura / Patterns

| Phase | Command | Purpose |
|-------|---------|---------|
| Create | `git worktree add ../feat-x feat/x` | New directory + branch |
| Create (new) | `git worktree add -b feat/x ../feat-x` | Create branch + worktree |
| List | `git worktree list` | See all active worktrees |
| Work | `cd ../feat-x && git commit` | Isolated commits |
| Finish | `git worktree remove ../feat-x` | Cleanup after merge |

Multi-agent layout:

```
repo/
├── main/                 <- trunk (protected)
├── ../feature-auth/      <- Agent A workspace
├── ../feature-payments/  <- Agent B workspace
└── ../bugfix-login/      <- Agent C workspace
```

All share git history but have independent working directories.

Finalization options:

| Option | Merge | Push | Keep Worktree | Delete Branch |
|--------|-------|------|---------------|---------------|
| Merge local | yes | no | no | yes |
| Push + PR | no | yes | yes | no |
| Keep branch | no | no | yes | no |
| Discard | no | no | no | yes (force) |

Discard requires explicit user confirmation (type "discard"). Push + PR keeps the worktree alive until PR merges.

Safe parallelism requires: features are independent (no shared file edits), each agent owns exactly one worktree, integration happens via merge/PR after completion.

## Exemplos Praticos

```bash
# Setup: isolated worktree for a feature
git worktree add -b feature/auth ../auth-work
cd ../auth-work
npm install && npm test  # verify baseline FIRST

# Implementation: normal git workflow
git add . && git commit -m "feat: add auth module"

# Finalization: merge and cleanup
cd ../main
git merge feature/auth
git worktree remove ../auth-work
git branch -d feature/auth
```

## Anti-Patterns

- Work on main without a worktree (contaminates trunk)
- Merge without running tests on the merge result
- Remove worktree before PR is created (loses context)
- Force-push without explicit user request
- Discard work without typed confirmation
- Skip baseline test check (hides pre-existing failures)

## Referencias

- source: https://git-scm.com/docs/git-worktree
- pattern: subagent-driven-development workflow

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_git_workflow_for_agents]] | sibling | 0.43 |
| [[batch]] | downstream | 0.38 |
| [[bld_output_template_contributor_guide]] | downstream | 0.26 |
| [[p11_gr_action_reversibility]] | downstream | 0.25 |
| [[p03_ins_action_protocol]] | downstream | 0.23 |
| [[bld_examples_skill]] | downstream | 0.21 |
| [[p11_qg_tdd_compliance]] | downstream | 0.19 |
| [[p12_wf_auto_ship]] | downstream | 0.18 |
| [[p01_kc_orchestration_best_practices]] | sibling | 0.18 |
| [[p04_ct_changelog_gen]] | downstream | 0.18 |
