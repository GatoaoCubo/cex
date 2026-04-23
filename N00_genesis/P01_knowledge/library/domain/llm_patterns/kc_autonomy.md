---
id: p01_kc_autonomy
kind: knowledge_card
type: domain
pillar: P01
title: "LLM Agent Autonomy Patterns"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: llm_patterns
quality: 9.1
tags: [autonomy, agent, react, plan-execute, reflexion]
tldr: "Autonomy levels L0-L4. ReAct (reason+act), plan-execute, reflexion. CEX maps: /guide=L2, /grid=L3, auto-workflows=L4."
when_to_use: "Designing agent systems with varying degrees of human oversight"
keywords: [autonomy, react, agent-loop, plan-execute, reflexion, levels]
density_score: 0.93
updated: "2026-04-07"
related:
  - spec_n07_operational_intelligence
  - p01_kc_pattern_extraction
  - p01_kc_distillation_pipeline
  - p01_kc_anti_patterns_general
  - p01_kc_coordination
  - p01_kc_anti_file_storage
  - p01_kc_anti_full_context
  - p08_pat_3phase_build_protocol
  - p01_kc_tool_use
  - p01_kc_refinement
---

# LLM Agent Autonomy Patterns

## Autonomy Levels

| Level | Name | Human Role | LLM Role |
|-------|------|-----------|----------|
| L0 | Tool | Full control | Single call |
| L1 | Assistant | Decides what | Multi-step in session |
| L2 | Co-pilot | Reviews/approves | Plans + checkpoints |
| L3 | Supervised | Monitors | Plans + executes + validates |
| L4 | Autonomous | Intervenes on failure | Full loop |

## Core Patterns

### ReAct (Reason + Act)
```
THOUGHT → ACTION → OBSERVATION → THOUGHT → ACTION → ...
```
Interleaves reasoning with tool calls. Most common agent pattern.

### Plan-Execute
```
PLAN: [step1, step2, step3]
EXECUTE each → VALIDATE all → DONE
```
Upfront planning, then sequential execution.

### Reflexion
```
ATTEMPT → EVALUATE → REFLECT → IMPROVED ATTEMPT
```
Self-critique and improvement between attempts.

## CEX Autonomy Map
- `/guide` = L2 co-pilot (user decides WHAT)
- `/grid` dispatch = L3 supervised (nuclei execute, N07 monitors)
- Auto-workflows = L4 autonomous (hydrate, review, evolve)
- Decision Manifest = bridge from L2 to L3/L4
- GDP = the protocol that manages level transitions

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_n07_operational_intelligence]] | downstream | 0.21 |
| [[p01_kc_pattern_extraction]] | sibling | 0.21 |
| [[p01_kc_distillation_pipeline]] | sibling | 0.21 |
| [[p01_kc_anti_patterns_general]] | sibling | 0.21 |
| [[p01_kc_coordination]] | sibling | 0.20 |
| [[p01_kc_anti_file_storage]] | sibling | 0.20 |
| [[p01_kc_anti_full_context]] | sibling | 0.20 |
| [[p08_pat_3phase_build_protocol]] | downstream | 0.20 |
| [[p01_kc_tool_use]] | sibling | 0.20 |
| [[p01_kc_refinement]] | sibling | 0.20 |
