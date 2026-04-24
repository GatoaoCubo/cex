---
id: p09_perm_stella_allow_block
kind: permission
8f: F1_constrain
pillar: P09
description: "Permission rules for orchestrator orchestrator — what it can and cannot do directly"
scope: stella
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [permission, stella, allow, block, orchestration]
updated: "2026-04-07"
domain: "config"
title: "Permission Stella Allow Block"
density_score: 0.92
tldr: "Defines permission for permission stella allow block, with validation gates and integration points."
related:
  - tpl_validation_schema
  - research_then_build
  - skill
  - bld_tools_prompt_cache
  - bld_tools_quality_gate
  - bld_tools_citation
  - bld_tools_spawn_config
  - bld_tools_retriever_config
  - bld_tools_multi_modal_config
  - bld_tools_memory_scope
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

## Block List (route to agent_groups)
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

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: p09_perm_stella_allow_block
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p09-perm-stella-allow-block.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[tpl_validation_schema]] | upstream | 0.30 |
| [[research_then_build]] | upstream | 0.30 |
| [[skill]] | upstream | 0.30 |
| [[bld_tools_prompt_cache]] | upstream | 0.28 |
| [[bld_tools_quality_gate]] | upstream | 0.28 |
| [[bld_tools_citation]] | upstream | 0.27 |
| [[bld_tools_spawn_config]] | upstream | 0.27 |
| [[bld_tools_retriever_config]] | upstream | 0.27 |
| [[bld_tools_multi_modal_config]] | upstream | 0.27 |
| [[bld_tools_memory_scope]] | upstream | 0.27 |
