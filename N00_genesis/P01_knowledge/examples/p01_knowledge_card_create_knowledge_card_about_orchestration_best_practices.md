---
id: p01_kc_orchestration_best_practices
kind: knowledge_card
pillar: P01
title: "LLM Multi-Agent Orchestration Best Practices"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
domain: multi_agent_orchestration
quality: 9.2
tags: [orchestration, multi-agent, dispatch, handoff, nucleus, coordination, knowledge]
tldr: "Orchestrators route, never build; dispatch via handoff files; GDP gates grid; Gemini nuclei require N07 consolidation for git."
when_to_use: "Designing or debugging multi-nucleus dispatch pipelines and agent coordination protocols"
keywords: [orchestration, dispatch, handoff, nucleus, consolidate, signal]
long_tails:
  - How to dispatch multiple agents in parallel without race conditions
  - When to use solo dispatch vs grid dispatch in multi-agent systems
  - How to consolidate Gemini nucleus output that cannot git commit
axioms:
  - ALWAYS write handoff file before dispatch — never pass task as CLI arg
  - NEVER build artifacts as orchestrator — route all construction to N03
  - IF nucleus is Gemini THEN N07 must consolidate (git commit + signal) after completion
  - ALWAYS run GDP before any grid dispatch — manifest before autonomous execution
linked_artifacts:
  primary: p03_system_prompt_create_system_prompt_for_orchestration_nucleus
  related: [p12_workflow_create_agent_for_orchestration_nucleus]
density_score: 0.88
data_source: "CEX .claude/rules/n07-orchestrator.md + _spawn/dispatch.sh protocol"
---
# LLM Multi-Agent Orchestration Best Practices

## Quick Reference
```yaml
topic: multi_agent_orchestration
scope: N07 CEX orchestrator + general LLM agent coordination
owner: builder_agent
criticality: high
dispatch_modes: [solo, grid, status, stop]
coordination: handoff_files + signals + git_log
```

## Key Concepts
- **Orchestrator role**: Routes and monitors — never builds artifacts directly
- **Handoff file**: `.cex/runtime/handoffs/{MISSION}_{nucleus}.md` — task contract
- **GDP**: User decides WHAT before autonomous execution; manifest = source of truth
- **Signal**: Nucleus emits `complete|retry|fail` to `.cex/runtime/signals/`
- **Consolidation**: N07 post-dispatch verify + git commit (Gemini only) + archive
- **Nucleus autonomy**: After dispatch with manifest, nucleus NEVER re-asks user

## Dispatch Modes
| Mode | Command | Use Case | Parallel |
|------|---------|----------|---------|
| solo | `dispatch.sh solo n03 "task"` | 1 nucleus, 1 task | No |
| grid | `dispatch.sh grid MISSION` | Up to 6 nuclei | Yes |
| status | `dispatch.sh status` | Monitor live nuclei | — |
| stop | `dispatch.sh stop` | Kill all + clear PIDs | — |

## Nucleus Capability Matrix
| Nucleus | CLI | Can Git | Can Signal | Sub-Agents |
|---------|-----|---------|-----------|-----------|
| N03 | claude opus | YES | YES | 5 |
| N02 | claude sonnet | YES | YES | 5 |
| N06 | claude sonnet | YES | YES | 5 |
| N01 | gemini 2.5-pro | NO | NO | — |
| N04 | gemini 2.5-pro | NO | NO | — |
| N05 | codex GPT | NO | NO | — |

## Strategy Phases
1. **GDP gate**: Identify subjective decisions → present to user → write manifest
2. **Handoff**: Write `.cex/runtime/handoffs/{MISSION}_{nucleus}.md` with decisions
3. **Dispatch**: `bash _spawn/dispatch.sh solo|grid MISSION_NAME`
4. **Monitor**: Check `git log` + `.cex/runtime/signals/` + `dispatch.sh status`
5. **Consolidate**: Verify → stop → commit Gemini output → signal → archive

## Golden Rules
- ROUTE: build → N03, research → N01/N04, copy → N02, code → N05, sales → N06
- HANDOFF: task as file content, NEVER as CLI arg (quote-hell on CMD)
- MANIFEST: `decision_manifest.yaml` is single source of truth for all choices
- GEMINI: N01/N04 produce output but cannot git/signal — N07 MUST consolidate
- AUTONOMY: dispatched nucleus reads manifest, executes, signals — no questions

## Flow
```text
[Goal] -> [GDP: user decides WHAT] -> [Write decision_manifest.yaml]
       -> [Write handoff files per nucleus]
       -> [dispatch.sh grid MISSION]
              |-> [N03: build artifacts] -> [git commit] -> [signal: complete]
              |-> [N01: research]        -> [output only] -> [N07 consolidates]
              |-> [N05: code review]     -> [output only] -> [N07 consolidates]
       -> [Monitor: signals + git log]
       -> [Consolidate: verify + git + archive]
```

## Anti-Patterns
| Anti-Pattern | Consequence |
|-------------|-------------|
| Orchestrator builds artifact | 8F bypassed; quality ungated |
| Task passed as CLI arg | CMD quote-hell; nucleus starts without task |
| Grid without manifest | Nuclei diverge; subjective choices unresolved |
| Skip consolidation for Gemini | Work lost; no git history; no signals |
| Nucleus re-asks user post-dispatch | GDP violated; autonomous loop breaks |
| PIDs not tracked | `stop` misses orphan processes |

## References
- Source: https://docs.anthropic.com/en/docs/agents-and-tools/orchestration
- Related: p03_system_prompt_create_system_prompt_for_orchestration_nucleus
- Related: p12_workflow_create_agent_for_orchestration_nucleus
- CEX rules: `.claude/rules/n07-orchestrator.md` + `.claude/rules/guided-decisions.md`