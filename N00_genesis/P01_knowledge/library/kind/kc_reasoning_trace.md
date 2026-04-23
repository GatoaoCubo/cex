---
id: p01_kc_reasoning_trace
kind: knowledge_card
type: kind
pillar: P03
title: "Reasoning Trace -- Deep Knowledge for reasoning_trace"
version: 1.0.0
created: 2026-04-05
updated: 2026-04-05
author: n07-orchestrator
domain: reasoning_trace
quality: 9.1
tags: [reasoning_trace, p03, CONSTRAIN, kind-kc, reasoning, chain-of-thought]
tldr: "Structured record of an agent's step-by-step reasoning -- captures the WHY behind decisions for audit and learning"
when_to_use: "Building reasoning-capture systems, debugging agent decisions, or training from past reasoning"
keywords: [reasoning, trace, chain-of-thought, CoT, audit, decision, scratchpad]
feeds_kinds: [reasoning_trace]
density_score: null
related:
  - bld_collaboration_reasoning_trace
  - reasoning-trace-builder
  - bld_knowledge_card_reasoning_trace
  - p03_sp_reasoning_trace_builder
  - bld_memory_reasoning_trace
  - bld_config_reasoning_trace
  - bld_tools_reasoning_trace
  - p03_ins_reasoning_trace_builder
  - bld_architecture_reasoning_trace
  - bld_schema_reasoning_trace
---

# Reasoning Trace

## Spec
```yaml
kind: reasoning_trace
pillar: P03
llm_function: CONSTRAIN
max_bytes: 8192
naming: p03_rt_{{agent}}_{{timestamp}}.yaml
core: false
```

## Purpose

A reasoning trace captures the step-by-step thought process an agent follows when making decisions. Unlike the final output (which shows WHAT was decided), the trace shows WHY and HOW -- which alternatives were considered, what evidence was weighed, and where confidence was high or low.

## Anatomy

| Field | Purpose | Example |
|-------|---------|---------|
| agent | Which agent produced this trace | `n03-agent-builder` |
| intent | What triggered the reasoning | `create sales agent` |
| steps | Ordered reasoning steps | list of {step, thought, evidence, confidence} |
| conclusion | Final decision | `Build agent with 4 tools, sales persona` |
| alternatives_rejected | Options considered but discarded | `[generic agent, template clone]` |
| confidence | Overall reasoning confidence | `0.85` |
| duration_ms | Reasoning time | `3400` |

## Key Patterns

1. **Scratchpad**: Agent writes intermediate reasoning to a scratchpad section, then produces clean output
2. **Step-Evidence-Confidence**: Each reasoning step cites evidence and self-assesses confidence
3. **Branching**: Record decision trees where multiple paths were evaluated before choosing
4. **Audit trail**: Traces enable post-hoc review of why an agent made a specific choice
5. **Learning fuel**: Low-confidence traces feed back to builder memory for future improvement

## Anti-Patterns

- Verbose traces (more tokens in trace than in output)
- Traces without confidence scores (can't identify uncertain decisions)
- Reasoning in output instead of trace (pollutes deliverable)
- No trace at all (debugging becomes guesswork)

## CEX Integration

- F4 REASON in `cex_8f_runner.py` produces `state.reasoning` (proto-trace)
- `cex_sdk/reasoning/tracer.py` provides structured trace capture
- Traces stored per-session; high-value traces promote to builder memory
- GDP decisions reference traces to show users WHY a question was asked

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_reasoning_trace]] | upstream | 0.69 |
| [[reasoning-trace-builder]] | related | 0.65 |
| [[bld_knowledge_card_reasoning_trace]] | sibling | 0.63 |
| [[p03_sp_reasoning_trace_builder]] | related | 0.62 |
| [[bld_memory_reasoning_trace]] | downstream | 0.62 |
| [[bld_config_reasoning_trace]] | downstream | 0.57 |
| [[bld_tools_reasoning_trace]] | downstream | 0.55 |
| [[p03_ins_reasoning_trace_builder]] | related | 0.51 |
| [[bld_architecture_reasoning_trace]] | downstream | 0.49 |
| [[bld_schema_reasoning_trace]] | downstream | 0.47 |
