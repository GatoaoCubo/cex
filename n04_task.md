---
id: n04_task_git_workflow
kind: knowledge_card
type: task
pillar: P05
title: "Git Workflow for Agents — Structured Operations for Collaborative Development"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: git
quality: 9.1
tags: [git, p05, operations, task]
tldr: "Standardized Git operations with phase-based workflows, branch strategies, and CI/CD integration for collaborative development"
when_to_use: "Implementing, reviewing, or reasoning about Git workflows for agent-based development"
keywords: [git, workflow, branch, ci/cd, collaboration, merge, commit, pull]
feeds_kinds: [task]
density_score: 8.9
---

# Git Workflow for Agents

## Spec
```yaml
kind: task
pillar: P05
llm_function: TOOL
max_bytes: 4096
naming: p05_task_git_workflow.md + .yaml
core: true
```

## What It Is
A Git workflow for agents is a structured, repeatable process for managing code changes in collaborative environments. It defines specific operations for branching, committing, merging, and integrating code across distributed teams. This workflow ensures consistency, reduces merge conflicts, and enables seamless integration with CI/CD pipelines.

## Cross-Tool Map
| Tool/Provider | Operation | Notes |
|-------------------|-----------|-------|
| Git CLI | `git checkout -b feature` | Create new feature branch |
| GitHub | Pull Request | Code review and merge automation |
| GitLab | Merge Request | CI/CD pipeline integration |
| Bitbucket | Branch Management | Access control and merge strategies |
| Azure DevOps | Git Repository | CI/CD pipeline integration |
| GitHub Actions | CI/CD | Automated testing and deployment |
| GitLab CI/CD | Pipeline | Automated testing and deployment |
| Bitbucket Pipelines | CI/CD | Automated testing and deployment |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| branch_strategy | enum | "feature" | feature (isolated changes) vs trunk-based (continuous integration) |
| commit_convention | enum | "conventional" | conventional (semantic commits) vs simple (plain text) |
| ci_integration | bool | true | automated testing vs manual review |
| merge_strategy | enum | "rebase" | rebase (linear history) vs merge (preserves history) |
| pull_request_template | string | "PR_TEMPLATE.md" | standardized PR format vs free-form |
| code_review_required | bool | true | quality assurance vs speed |
| squash_commits | bool | false | cleaner history vs detailed audit trail |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| branch | Create development branch | main branch | feature branch |
| commit | Record changes | working directory | commit hash |
| review | Code inspection | commit hash | approval status |
| test | CI/CD validation | commit hash | test results |
| merge | Integrate changes | feature branch | main branch |
| deploy | Release to production | merged branch | deployment status |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| Pull Request | "refs/heads/main" | GitHub/GitLab event |
| Git Hook | "pre-commit" | Local CLI execution |
| CI/CD | "push" | Pipeline trigger |
| Manual | "merge" | User-initiated action |
| Scheduled | "cron" | Periodic execution |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_branch_defined | branch_strategy in allowed values | Cannot create branch |
| H02_commit_valid | commit_convention matches format | Invalid commit history |
| H03_ci_enabled | ci_integration true | No automated testing |
| H04_merge_valid | merge_strategy in allowed values | Invalid merge |
| H05_pr_template | pull_request_template exists | Missing PR format |
| H06_review_required | code_review_required true | No code inspection |
| H07_squash_valid | squash_comm
```