---
kind: knowledge_card
id: bld_knowledge_card_reasoning_trace
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for reasoning_trace production — atomic searchable facts
sources: reasoning-trace-builder schema + cex_sdk/reasoning/tracer.py
quality: 9.1
title: "Knowledge Card Reasoning Trace"
version: "1.0.0"
author: n03_builder
tags: [reasoning_trace, builder, examples]
tldr: "Golden and anti-examples for reasoning trace construction, demonstrating ideal structure and common pitfalls."
domain: "reasoning trace construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_reasoning_trace_builder
  - p03_ins_reasoning_trace_builder
  - bld_memory_reasoning_trace
  - p11_qg_reasoning_trace
  - bld_collaboration_reasoning_trace
  - bld_schema_reasoning_trace
  - p01_kc_reasoning_trace
  - bld_config_reasoning_trace
  - bld_output_template_reasoning_trace
  - reasoning-trace-builder
---

# Domain Knowledge: reasoning_trace
## Executive Summary
Reasoning traces are structured YAML decision records — the audit mechanism for WHY agents choose specific paths. Each trace captures a complete chain-of-thought: what was considered, what evidence existed, how confident the agent was at each step, what alternatives were rejected and why, and what conclusion was reached. Unlike instructions (execution directives) or system_prompts (identity definitions), traces carry only decision rationale — no action items, no persona rules, no workflow steps.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 (prompt) |
| Format | YAML |
| Naming | `p03_rt_{agent}_{timestamp}.yaml` |
| Max bytes | 8192 |
| Required fields | 6: agent, intent, steps, conclusion, confidence, timestamp |
| Optional fields | 4: alternatives_rejected, duration_ms, context, trigger |
| Step structure | triplet: step (int), thought (str), evidence (str), confidence (0.0-1.0) |
| Confidence range | 0.0-1.0 (overall = geometric mean of step confidences) |
| Timestamp format | ISO 8601 datetime |
| Scope | one trace = one decision chain = one agent |
## Patterns
| Pattern | Rule |
|---------|------|
| Step-evidence-confidence triplet | Every step has thought + concrete evidence + calibrated confidence |
| Confidence calibration | 0.0-0.3 low (flag for review), 0.3-0.7 medium, 0.7-1.0 high |
| Evidence concreteness | Cite specific metrics, file paths, benchmark numbers — never vague claims |
| Geometric mean confidence | Overall confidence = (c1 * c2 * ... * cn)^(1/n) — penalizes weak links |
| Alternatives rejected | At least 1 rejected path with evidence-based reason for complete audit trail |
| Immutability | Never mutate an existing trace — emit a new trace for corrections |
| Memory feedback loop | Traces with confidence < 0.5 trigger learning record creation |
| Scratchpad pattern | Agent reasons in structured steps then distills to conclusion |
| Branching decision tree | Complex decisions produce traces with multiple comparison steps |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague evidence ("it seemed better") | Zero audit value — reviewer cannot verify the reasoning |
| Confidence clustering at 0.8-0.9 | Indicates uncalibrated self-assessment regardless of evidence strength |
| Execution instructions in trace | Traces record WHY, not WHAT — instructions belong in instruction artifacts |
| Missing alternatives_rejected | Proves no decision analysis occurred — trace is a post-hoc rationalization |
| Single-step trace | One step = assertion, not reasoning chain (minimum 2 steps required) |
| Verbose traces (> output size) | Reasoning audit should be concise, not longer than the artifact it explains |
| Confidence as string ("high") | Must be numeric 0.0-1.0 for geometric mean calculation |
| No timestamp | Traces cannot be ordered, deduplicated, or correlated with builds |
## Application
1. Identify the decision being traced: what did the agent need to decide?
2. Set `agent` to the agent or agent_group slug
3. Set `intent` to the specific decision question
4. Build the step chain: for each consideration, record thought + evidence + confidence
5. Calibrate confidence: match score to evidence strength, not gut feeling
6. Record all alternatives considered, with evidence-based rejection reasons
7. Write conclusion that directly references the strongest evidence from steps
8. Compute overall confidence as geometric mean of step confidences
9. Add timing data (duration_ms) if available
10. Name file `p03_rt_{agent}_{timestamp}.yaml`, validate size <= 8192 bytes
## References
- Schema: reasoning_trace schema (P06)
- Runtime: cex_8f_runner.py F4 REASON state, cex_sdk/reasoning/tracer.py
- Pillar: P03 (prompt)
- Boundary: instruction (execution), system_prompt (identity), workflow_primitive (steps) — all distinct from reasoning_trace

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_reasoning_trace_builder]] | downstream | 0.68 |
| [[p03_ins_reasoning_trace_builder]] | downstream | 0.68 |
| [[bld_memory_reasoning_trace]] | downstream | 0.66 |
| [[p11_qg_reasoning_trace]] | downstream | 0.61 |
| [[bld_collaboration_reasoning_trace]] | downstream | 0.60 |
| [[bld_schema_reasoning_trace]] | downstream | 0.60 |
| [[p01_kc_reasoning_trace]] | sibling | 0.60 |
| [[bld_config_reasoning_trace]] | downstream | 0.56 |
| [[bld_output_template_reasoning_trace]] | downstream | 0.55 |
| [[reasoning-trace-builder]] | downstream | 0.55 |
