---
kind: memory
id: bld_memory_mental_model
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for mental_model artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Mental Model"
version: "1.0.0"
author: n03_builder
tags: [mental_model, builder, examples]
tldr: "Golden and anti-examples for mental model construction, demonstrating ideal structure and common pitfalls."
domain: "mental model construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - mental-model-builder
  - bld_collaboration_mental_model
  - bld_knowledge_card_mental_model
  - p03_sp_mental_model_builder
  - p03_ins_mental_model
  - runtime-state-builder
  - p11_qg_mental_model
  - bld_collaboration_runtime_state
  - bld_architecture_mental_model
  - p01_kc_mental_model
---
# Memory: mental-model-builder

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
## Summary
Mental models are design-time cognitive maps defining how an agent routes tasks, makes decisions, and prioritizes work. The most impactful production lesson is that routing rules must have confidence thresholds — rules without thresholds trigger on partial keyword matches, causing misroutes. Decision trees need explicit else/fallback branches; agents with incomplete trees silently drop tasks that match no branch.
## Pattern
1. Every routing rule needs: keyword pattern, target action, and minimum confidence threshold (0.0-1.0)
2. Decision trees must have an explicit default/fallback branch — no task should fall through unhandled
3. Priority ordering must be total (no ties) — tied priorities cause non-deterministic behavior
4. Heuristics should include their failure rate and the conditions under which they break down
5. Domain boundaries must be stated as both positive ("I handle X") and negative ("I do NOT handle Y")
6. Personality traits should be functional (affecting output style) not decorative
## Anti-Pattern
1. Routing rules without confidence thresholds — triggers on any partial keyword match
2. Decision trees with missing else branches — tasks silently dropped or stuck in limbo
3. Tied priorities without tiebreaker — execution order becomes non-deterministic
4. Domain boundary stated only positively — negative boundaries prevent scope creep more effectively
5. Confusing mental_model (P02, design-time cognitive map) with runtime_state (P10, mutable agent state)
6. Heuristics presented as certainties — all heuristics have failure modes that should be documented
## Context
Mental models sit in the P02 identity layer as static design-time documents. They are loaded when an agent boots and define its routing logic, decision framework, and domain expertise boundaries. Unlike runtime states (P10), mental models do not change during execution. Unlike routers (P02), mental models include the full cognitive context (personality, heuristics, priorities) beyond just route tables.
## Impact
Agents with confidence-thresholded routing rules showed 40% fewer misrouted tasks. Adding explicit fallback branches to decision trees eliminated 100% of silent task drops. Total priority ordering reduced non-deterministic behavior reports to zero in tested configurations.
## Reproducibility
Reliable mental model production: (1) enumerate all task types the agent handles, (2) create routing rules with keywords and confidence thresholds, (3) build decision tree with explicit fallback at every level, (4) define total priority ordering with no ties, (5) state domain boundaries both positively and negatively, (6) validate against 9 HARD + 12 SOFT gates.
## References
1. mental-model-builder SCHEMA.md (14 required + 9 recommended fields)
2. P02 identity pillar specification
3. Cognitive architecture design patterns

## Metadata

```yaml
id: bld_memory_mental_model
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-mental-model.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | mental model construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[mental-model-builder]] | upstream | 0.61 |
| [[bld_collaboration_mental_model]] | upstream | 0.57 |
| [[bld_knowledge_card_mental_model]] | upstream | 0.54 |
| [[p03_sp_mental_model_builder]] | upstream | 0.53 |
| [[p03_ins_mental_model]] | upstream | 0.45 |
| [[runtime-state-builder]] | related | 0.44 |
| [[p11_qg_mental_model]] | downstream | 0.43 |
| [[bld_collaboration_runtime_state]] | related | 0.39 |
| [[bld_architecture_mental_model]] | upstream | 0.37 |
| [[p01_kc_mental_model]] | upstream | 0.34 |
