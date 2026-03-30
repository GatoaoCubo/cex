---
id: p09_perm_stella_allow_block
kind: permission
pillar: P09
description: "Permission rules for orchestrator orchestrator — what it can and cannot do directly"
scope: stella
version: 1.0.0
created: 2026-03-24
author: edison
quality: 9.0
tags: [permission, stella, allow, block, orchestration]
---

# Permission: orchestrator Allow/Block

## Allow List (execute directly)
| Category | Operations |
|----------|-----------|
| Status | git status, git log, git diff |
| Diagnostic | pwd, ls, cat, head, tail, echo |
| Spawn | spawn_solo.ps1, spawn_grid.ps1, spawn_monitor.ps1 |
| Read | Read, Glob, Grep tools |
| Maintenance | del, rm, mkdir, copy, move |
| Signals | read .claude/signals/, write completion signals |

## Block List (route to agent_nodes)
| Domain | Route To |
|--------|----------|
| Research, market analysis | research_agent |
| Marketing, copy, ads | marketing_agent |
| Code, components, infra | builder_agent |
| Knowledge, indexing, RAG | knowledge_agent |
| Deploy, test, debug | operations_agent |
| Courses, pricing | commercial_agent |

## Confirm Required
Delete files, force push, production deploy, API key changes, payment operations.

## Principle
orchestrator orchestrates, NEVER executes. If a task produces artifacts, it must be dispatched.
