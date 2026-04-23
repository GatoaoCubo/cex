---
id: p01_kc_handoff
kind: knowledge_card
type: kind
pillar: P12
title: "Handoff — Deep Knowledge for handoff"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: handoff
quality: 9.1
tags: [handoff, P12, COLLABORATE, kind-kc]
tldr: "Complete task transfer package containing context, tasks, scope fence, commit instruction, and signal protocol for autonomous agent_group execution"
when_to_use: "Building, reviewing, or reasoning about handoff artifacts"
keywords: [task-transfer, context, autonomous]
feeds_kinds: [handoff]
density_score: null
related:
  - bld_knowledge_card_handoff
  - handoff-builder
  - p03_sp_handoff_builder
  - bld_collaboration_handoff
  - bld_instruction_handoff
  - bld_architecture_handoff
  - p12_ho_admin_template
  - bld_config_handoff
  - p10_lr_handoff_builder
  - bld_schema_handoff
---

# Handoff

## Spec
```yaml
kind: handoff
pillar: P12
llm_function: COLLABORATE
max_bytes: 4096
naming: p12_ho_{{task}}.md
core: true
```

## What It Is
A handoff is a complete, self-contained task transfer document written by an orchestrator for a agent node to execute autonomously. It includes mission context, seed keywords, ordered tasks, scope fence (what to touch / not touch), commit instruction, and signal protocol. It is NOT action_prompt (P03 — single execution prompt without transfer context or commit/signal protocol) nor signal (P12 — event notification; handoff is a complete instruction set, not an event).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Context passing via `RunnableConfig` + custom state | Pass task context between chain steps via config metadata |
| LlamaIndex | `AgentWorkflow` event with task payload | Events carry structured task data between workflow steps |
| CrewAI | `Task(context=[other_task], description=...)` | Task context from other tasks = handoff equivalent; no file |
| DSPy | Module chaining via `forward()` arguments | Pass state dict between modules as explicit keyword arguments |
| Haystack | Pipeline component output → next component input | Structured data flows through pipeline connections |
| OpenAI | Thread continuation + system instruction update | New system message with full context = handoff equivalent |
| Anthropic | System prompt injection + full context block | Handoff content injected into system prompt for agent_group session |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| autonomy_level | string | TOTAL | TOTAL/SUPERVISED — total = no confirmation; supervised = ask before destructive ops |
| quality_target | float | 9.0 | Higher target = more retries; lower = faster completion |
| scope_fence | map | required | ONLY/NEVER paths; prevents scope creep and file collisions |
| seeds | list | required | 5-10 domain keywords; activates brain_query context retrieval |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| OPEN_VARIABLES | Agent_group decides implementation details | `Generate [TEMPLATE_TYPE] for [DOMAIN] using best approach` |
| Batch handoff | >5 tasks for same agent_group | `p12_ho_mission_batch_1_shaka.md`, `p12_ho_mission_batch_2_shaka.md` |
| Dependency chain | Task B needs Task A output | Handoff B includes: `## DEPENDS_ON: p12_sig_task_a_complete.json` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Inline prompt >200 chars | TSP `-p` flag hangs on long prompts | Write handoff file; prompt says only "Read [file] and execute" |
| No scope fence | Agent_group modifies unintended files; git conflicts | Always define SOMENTE/NAO TOQUE paths |
| Missing commit instruction | Agent_group completes work but never commits | Last section always: git add + git commit with message template |

## Integration Graph
```
[dispatch_rule] --> [handoff] --> [spawn_config]
[dag] -------------^       |
                      [session_state]
                      [signal: complete]
```

## Decision Tree
- IF task has >5 steps THEN use batch handoffs (batch_1, batch_2, ...)
- IF agent_group needs browser THEN include `--add browser` spawn modifier
- IF task is destructive THEN set autonomy_level: SUPERVISED
- DEFAULT: autonomy_level: TOTAL; quality_target: 9.0; always include commit + signal sections

## Quality Criteria
- GOOD: Has CONTEXTO, SEEDS, TAREFAS, SCOPE FENCE, COMMIT, SIGNAL sections; under 4096 bytes
- GREAT: OPEN_VARIABLES for agent_group discretion; batch structure for large missions; dependency chain explicit
- FAIL: Missing commit section; no scope fence; >4096 bytes; inline task descriptions >200 chars for TSP

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_handoff]] | sibling | 0.46 |
| [[handoff-builder]] | related | 0.44 |
| [[p03_sp_handoff_builder]] | upstream | 0.44 |
| [[bld_collaboration_handoff]] | related | 0.43 |
| [[bld_instruction_handoff]] | upstream | 0.41 |
| [[bld_architecture_handoff]] | upstream | 0.40 |
| [[p12_ho_admin_template]] | related | 0.38 |
| [[bld_config_handoff]] | upstream | 0.36 |
| [[p10_lr_handoff_builder]] | upstream | 0.35 |
| [[bld_schema_handoff]] | upstream | 0.34 |
