---
id: p01_kc_checkpoint
kind: knowledge_card
type: kind
pillar: P12
title: "Checkpoint — Deep Knowledge for checkpoint"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: checkpoint
quality: 9.1
tags: [checkpoint, P12, GOVERN, kind-kc]
tldr: "Point-in-time saved state of a workflow enabling resume-on-failure without full restart"
when_to_use: "Building, reviewing, or reasoning about checkpoint artifacts"
keywords: [resume, snapshot, fault-tolerance]
feeds_kinds: [checkpoint]
density_score: null
related:
  - bld_collaboration_checkpoint
  - checkpoint-builder
  - bld_architecture_checkpoint
  - p03_sp_checkpoint_builder
  - bld_instruction_checkpoint
  - bld_examples_checkpoint
  - bld_knowledge_card_checkpoint
  - p12_checkpoint
  - bld_schema_checkpoint
  - bld_output_template_checkpoint
---

# Checkpoint

## Spec
```yaml
kind: checkpoint
pillar: P12
llm_function: GOVERN
max_bytes: 2048
naming: p12_ckpt.md
core: true
```

## What It Is
A checkpoint is a point-in-time saved state of a running workflow — completed steps, current inputs, intermediate outputs — that enables resume-on-failure without full restart. It is written atomically after each committed step. It is NOT signal (P12 — event notification between agents; checkpoint is state, not event) nor session_state (P10 — ephemeral; checkpoint is specifically for fault recovery and persists until the workflow completes).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableConfig` checkpointer (LangGraph) | LangGraph natively supports memory checkpointers (SQLite, Redis) |
| LlamaIndex | `Workflow` event state persistence | Serialize workflow `ctx` between steps for fault recovery |
| CrewAI | `Flow` state + `@persist` decorator | Flow state can be persisted; resume from last @listen event |
| DSPy | Module `save()` / `load()` methods | Compiled DSPy programs can be saved; resume from compilation |
| Haystack | `Pipeline.to_dict()` serialization | Serialize full pipeline state; deserialize for resume |
| OpenAI | Thread state + message continuity | Thread ID enables resume; messages persist server-side |
| Anthropic | Custom YAML state file + step counter | Write step counter + outputs to YAML; read on restart |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| step | int | required | Current step number; enables precise resume point |
| total_steps | int | required | Progress indicator; detects completion vs interruption |
| outputs | map | {} | Intermediate outputs by step; avoid storing large blobs |
| checkpoint_id | string | uuid | Unique per workflow run; prevents collision on parallel runs |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Post-commit checkpoint | After each irreversible action | Write checkpoint after git commit; never before |
| Incremental output reference | Large intermediate outputs | Store output paths not content: `step_3_output: outputs/step3.json` |
| Checkpoint-then-signal | Multi-agent workflows | Write checkpoint → emit signal; downstream reads checkpoint on signal |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Checkpoint before commit | Resume replays non-atomic operations; duplicates | Write checkpoint only after successful commit |
| Storing full outputs in checkpoint | Exceeds 2048 bytes; injection overhead | Reference output file paths; keep checkpoint minimal |
| Single global checkpoint file | Concurrent workflows overwrite each other | One checkpoint per checkpoint_id (uuid per run) |

## Integration Graph
```
[workflow] --> [checkpoint] --> [resume / workflow]
[signal] --------^       |
                     [handoff]
```

## Decision Tree
- IF workflow step commits successfully THEN write checkpoint with step+1
- IF workflow interrupted THEN read checkpoint → resume from step N
- IF workflow completes THEN delete checkpoint (cleanup)
- DEFAULT: Write checkpoint after every commit; never skip on "quick" workflows

## Quality Criteria
- GOOD: Has checkpoint_id, step, total_steps, outputs (by reference), timestamp; under 2048 bytes
- GREAT: Post-commit timing enforced; output paths not inline data; cleanup on completion
- FAIL: Written before commit; stores full outputs inline; single global file; never cleaned up

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_checkpoint]] | related | 0.62 |
| [[checkpoint-builder]] | related | 0.62 |
| [[bld_architecture_checkpoint]] | upstream | 0.61 |
| [[p03_sp_checkpoint_builder]] | upstream | 0.59 |
| [[bld_instruction_checkpoint]] | upstream | 0.53 |
| [[bld_examples_checkpoint]] | upstream | 0.52 |
| [[bld_knowledge_card_checkpoint]] | sibling | 0.52 |
| [[p12_checkpoint]] | related | 0.51 |
| [[bld_schema_checkpoint]] | upstream | 0.49 |
| [[bld_output_template_checkpoint]] | upstream | 0.46 |
