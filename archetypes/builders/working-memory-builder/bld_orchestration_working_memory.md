---
quality: 8.8
quality: 8.2
kind: collaboration
id: bld_collaboration_working_memory
pillar: P12
llm_function: COLLABORATE
purpose: How working-memory-builder works in crews with other builders
title: "Collaboration Working Memory"
version: "1.0.0"
author: n03_builder
tags: [working_memory, builder, collaboration]
tldr: "working-memory-builder provides active task context within the P10 memory layer."
domain: "working memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_collaboration_memory_scope
  - bld_collaboration_memory_type
  - bld_collaboration_instruction
  - bld_collaboration_action_prompt
  - bld_collaboration_memory_summary
  - bld_manifest_memory_type
  - p01_kc_memory_scope
  - bld_collaboration_builder
  - memory-scope-builder
  - bld_knowledge_card_memory_scope
---

# Collaboration: working-memory-builder

## My Role in Crews
I am a SPECIALIST. I design the short-term context store for ONE active task.
I do not store session state. I do not store long-term facts. I do not record past episodes.
I provide the typed slot schema that a task uses while running, and define what survives completion.

## Crew Compositions

### Crew: "P10 Memory System"
```
  1. working-memory-builder -> "task context schema (short-term)"
  2. entity-memory-builder -> "promoted facts from task completion"
  3. episodic-memory-builder -> "promoted episode summaries"
  4. memory-summary-builder -> "compressed context from accumulated episodes"
```

### Crew: "Task Pipeline Design"
```
  1. agent-builder -> "agent definition with tool bindings"
  2. working-memory-builder -> "task context store for agent runs"
  3. prospective-memory-builder -> "scheduled follow-up actions from task"
  4. episodic-memory-builder -> "record of completed task episodes"
```

## Handoff Protocol

### I Receive
- seeds: task_id pattern, task complexity, expected intermediate state
- optional: nucleus context (n01-n07)
- optional: promote targets if task produces persistent knowledge

### I Produce
- working_memory artifact (.md with YAML frontmatter)
- committed to: `N0x_{domain}/P10_memory/p10_wm_{scope}.md`

### I Signal
- signal: complete with quality score
- if quality < 8.0: retry (common failure: untyped slots, missing capacity)

## Builders I Depend On
| Builder | Why |
|---------|-----|
| agent-builder | Agent definitions specify which tasks run and what state they need |
| entity-memory-builder | Promote targets -- facts discovered during task go here |
| episodic-memory-builder | Episode summaries promoted on task completion |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agents reference working_memory in their tool bindings |
| instruction-builder | Task instructions reference slot names for state handoffs |
| prospective-memory-builder | Scheduled follow-ups may read promoted task results |

## Conflict Resolution
| Scenario | Resolution |
|----------|-----------|
| Working memory vs session_state | working_memory = sub-session (one task). session_state = session-wide (multiple tasks). |
| Working memory vs entity_memory | working_memory = temporary; entity_memory = permanent. Promote before clear. |
| Slots that outlast task | Don't store them in working_memory -- put them in entity_memory from the start. |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_scope]] | sibling | 0.49 |
| [[bld_collaboration_memory_type]] | sibling | 0.39 |
| [[bld_collaboration_instruction]] | sibling | 0.34 |
| [[bld_collaboration_action_prompt]] | sibling | 0.34 |
| [[bld_collaboration_memory_summary]] | sibling | 0.34 |
| [[bld_manifest_memory_type]] | upstream | 0.32 |
| [[p01_kc_memory_scope]] | upstream | 0.31 |
| [[bld_collaboration_builder]] | sibling | 0.30 |
| [[memory-scope-builder]] | upstream | 0.30 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.30 |
