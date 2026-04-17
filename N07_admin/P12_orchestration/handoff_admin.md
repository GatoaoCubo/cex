---
id: p12_ho_admin_template
title: "Handoff Admin"
kind: handoff
pillar: P12
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
agent_group: orchestrator
mission: admin_operations
autonomy: full
quality_target: 9.0
domain: orchestration
quality: 9.1
tags: [handoff, orchestration, N07, template, dispatch]
tldr: "Handoff template and protocol for N07 — required fields, structure, commit convention, and signal instructions."
dependencies: []
seeds: [handoff, dispatch, task, context, scope_fence, commit, signal, autonomy, quality]
keywords: [handoff, delegation, dispatch, task-packaging]
linked_artifacts:
  primary: "N07_admin/P12_orchestration/dispatch_rule_admin.md"
  related: [N07_admin/P12_orchestration/workflow_admin.md, N07_admin/P12_orchestration/signal_admin.md]
density_score: 0.91
---

# N07 Handoff Protocol

**Full Autonomy** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## Handoff Structure

Every handoff written by N07 MUST contain these sections:

| Section | Purpose | Required |
|---------|---------|----------|
| Header | Mission name, nucleus, autonomy level, quality target | YES |
| Context | Why this task exists and what it unblocks | YES |
| Tasks | Numbered steps with action verbs and acceptance criteria | YES |
| Scope Fence | Allowed paths (SOMENTE) and forbidden paths (NAO TOQUE) | YES |
| Commit | Exact git add pattern and commit message format | YES |
| Signal | Completion signal command with quality score | YES |
| Seeds | Domain keywords for context retrieval (5-10) | RECOMMENDED |
| Dependencies | Other handoffs that must complete first | IF APPLICABLE |

## Template

```markdown
# {NUCLEUS} Task: {Title}
**{Autonomy} Autonomy** | **Quality {target}+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
{Why this task exists. What it unblocks. Relevant references.}

## REFERENCIAS
- {Golden reference path}
- {Schema or KC path}

## TAREFAS
1. {Action verb}: {specific deliverable with acceptance criteria}
2. {Action verb}: {specific deliverable with acceptance criteria}

## SCOPE FENCE
- SOMENTE: {allowed paths}
- NAO TOQUE: {forbidden paths}

## COMMIT
git add {specific paths}
git commit -m "[{NUCLEUS}] {description}"

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('{nucleus}', 'complete', {score}, '{mission}')"
```

## Handoff Rules

1. **One handoff per nucleus per mission** — never bundle tasks for multiple nuclei in one file
2. **Autonomy levels**: full (no human review), supervised (human reviews before commit), assisted (human co-pilots)
3. **Quality target**: minimum 9.0 for production artifacts, 8.0 for operational files
4. **Scope fence is mandatory** — builders must not touch files outside their scope
5. **Commit before pause** — builders must commit and signal before any interruption
6. **Signal on complete** — every handoff must specify the exact signal command

## File Naming

Pattern: `.cex/runtime/handoffs/{mission}_{nucleus}_{seq}.md`

Examples:
- `.cex/runtime/handoffs/bootstrap_f1_n03_01.md`
- `.cex/runtime/handoffs/research_market_n01_01.md`
- `.cex/runtime/handoffs/deploy_v2_n05_01.md`

## Lifecycle

1. N07 writes handoff to `.cex/runtime/handoffs/`
2. Builder reads handoff, executes tasks
3. Builder commits and signals
4. N07 validates quality
5. If accepted: move handoff to `_instances/codexa/N07_admin/archive/`
6. If rejected: update handoff with feedback, re-dispatch

## Example: Bootstrap F1 Handoff

```markdown
# N03 Task: Rebuild N07 Orchestrator
**Full Autonomy** | **Quality 9.0+**

## CONTEXTO
N07 artefatos com quality: null. Reconstruir com identidade real do orquestrador.

## TAREFAS
1. Build agent_admin.md — complete N07 identity
2. Build system_prompt_admin.md — orchestrator rules
3. Build knowledge_card_admin.md — dispatch knowledge

## COMMIT
git add -A && git commit -m "[N03] rebuild N07 artefatos batch 1/4"

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('n03', 'complete', 9.0, 'bootstrap_f1')"
```

## References

- Dispatch rules: N07_admin/P12_orchestration/dispatch_rule_admin.md
- Signal protocol: N07_admin/P12_orchestration/signal_admin.md
- Grid ops (recovery, fallbacks): N07_admin/P10_memory/grid_orchestration_mastery.md
