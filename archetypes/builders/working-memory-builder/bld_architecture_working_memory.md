---
kind: architecture
id: bld_architecture_working_memory
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of working_memory -- inventory, dependencies, and cognitive science context
quality: null
title: "Architecture Working Memory"
version: "1.0.0"
author: n03_builder
tags: [working_memory, builder, architecture]
tldr: "working_memory is the innermost P10 memory tier: task-scoped, short-lived, cleared on completion."
domain: "working memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| task_id | Task instance binding | working_memory | required |
| context_slots | Typed intermediate state | working_memory | required |
| capacity_limit | Max memory allocation | working_memory | required |
| expiry | TTL or completion trigger | working_memory | required |
| clear_on_complete | Post-task disposal policy | working_memory | required |
| promote_targets | Persistent memory kinds to receive promoted slots | working_memory | optional |
| session_state | Session-wide persistence -- sibling, not same | P10 | sibling |
| entity_memory | Long-term entity facts -- receives promoted data | P10 | sibling |
| episodic_memory | Episode history -- receives promoted interaction summaries | P10 | sibling |
| memory_summary | Compression output from episodic/entity memory | P10 | sibling |

## Dependency Graph
```
task_dispatch       --creates-->  working_memory (task_id bound at spawn)
context_slots       --holds-->    task intermediate state
capacity_limit      --bounds-->   context_slots size
expiry              --governs-->  working_memory lifecycle
clear_on_complete   --governs-->  post-task disposal
working_memory      --promotes_to--> entity_memory (when clear_on_complete: promote)
working_memory      --promotes_to--> episodic_memory (when clear_on_complete: promote)
working_memory      --discards-->    on clear_on_complete: clear
```

## P10 Memory Tier Model
```
                    [session_state]     <-- session-wide, persists turns
                          |
                    [working_memory]    <-- task-scoped, cleared on complete
                          |
            +-------------+-------------+
            |                           |
     [entity_memory]            [episodic_memory]
     (long-term facts)           (episode history)
            |                           |
            +----------+----------------+
                       |
                [memory_summary]
                (compressed context)
```

## Boundary Table
| working_memory IS | working_memory IS NOT |
|-------------------|-----------------------|
| Task-scoped, cleared on completion | Session-wide state (that is session_state) |
| Short-term intermediate task state | Long-term entity facts (that is entity_memory) |
| Single task binding (task_id) | Past interaction history (that is episodic_memory) |
| Configurable capacity with hard limit | Prompt context (that is the LLM's context window) |
| May promote slots to persistent memory | Permanent store (cleared on complete) |
