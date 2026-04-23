---
kind: tools
id: bld_tools_reasoning_trace
pillar: P04
llm_function: CALL
purpose: Tools and runtime surfaces relevant to reasoning_trace production
quality: 9.0
title: "Tools Reasoning Trace"
version: "1.0.0"
author: n03_builder
tags: [reasoning_trace, builder, examples]
tldr: "Golden and anti-examples for reasoning trace construction, demonstrating ideal structure and common pitfalls."
domain: "reasoning trace construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_reasoning_trace
  - p01_kc_reasoning_trace
  - reasoning-trace-builder
  - bld_collaboration_reasoning_trace
  - p03_sp_reasoning_trace_builder
  - bld_knowledge_card_reasoning_trace
  - bld_architecture_reasoning_trace
  - bld_memory_reasoning_trace
  - p03_ins_reasoning_trace_builder
  - bld_tools_trace_config
---

# Tools: reasoning-trace-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| `cex_8f_runner.py` | 8F pipeline runner — F4 REASON produces reasoning state | Trace capture during build | ACTIVE |
| `cex_sdk/reasoning/tracer.py` | SDK tracer that captures live reasoning into trace format | Runtime trace generation | ACTIVE |
| `cex_compile.py` | Compiles .md/.yaml to indexed artifacts | Post-save compilation | ACTIVE |
| `cex_doctor.py` | Builder health check — validates trace structure | Validation phase | ACTIVE |
| `cex_memory_update.py` | Memory append for low-confidence trace feedback | Feedback loop trigger | CONDITIONAL |
| `cex_score.py` | Peer review scoring (--apply) | Quality assessment | CONDITIONAL |
## Runtime Interfaces
| Interface | Path | Use |
|-----------|------|-----|
| Trace output directory | `P03_prompt/compiled/` | write compiled YAML trace files |
| P03 schema | `P03_prompt/_schema.yaml` | naming, format, limits |
| Trace template | `P03_prompt/templates/tpl_reasoning_trace.md` | human reference for trace structure |
| Memory feedback | `.cex/learning_records/` | write learning records for low-confidence traces |
| SDK tracer | `cex_sdk/reasoning/tracer.py` | runtime trace capture integration |
| 8F state | `cex_8f_runner.py` state.reasoning | F4 REASON state that feeds traces |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
Until a dedicated reasoning_trace validator exists, validate manually:
- filename matches `p03_rt_{agent}_{timestamp}.yaml`
- YAML parses without errors
- required fields present: agent, intent, steps, conclusion, confidence, timestamp
- each step has thought, evidence, confidence
- confidence values in range 0.0-1.0
- overall confidence is geometric mean of step confidences
- no execution instructions or workflow logic in trace body
- total size <= 8192 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_reasoning_trace]] | downstream | 0.58 |
| [[p01_kc_reasoning_trace]] | upstream | 0.56 |
| [[reasoning-trace-builder]] | upstream | 0.55 |
| [[bld_collaboration_reasoning_trace]] | upstream | 0.55 |
| [[p03_sp_reasoning_trace_builder]] | upstream | 0.48 |
| [[bld_knowledge_card_reasoning_trace]] | upstream | 0.48 |
| [[bld_architecture_reasoning_trace]] | downstream | 0.48 |
| [[bld_memory_reasoning_trace]] | downstream | 0.48 |
| [[p03_ins_reasoning_trace_builder]] | upstream | 0.41 |
| [[bld_tools_trace_config]] | sibling | 0.39 |
