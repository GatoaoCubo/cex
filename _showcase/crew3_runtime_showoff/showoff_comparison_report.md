---
id: showcase_showoff_comparison
kind: benchmark
pillar: P07
title: "Showoff Comparison: Naked Opus vs CEXAI Opus"
version: "1.0.0"
created: "2026-04-22"
updated: "2026-04-22"
author: "n07_orchestrator"
domain: "framework_leverage_benchmark"
quality: 8.9
tags: [benchmark, showoff, naked-vs-cexai, agent, framework-leverage]
tldr: "Same LLM (Opus), same task (support triage agent), same time budget. Naked=verbose prose. CEXAI=typed, compiled, governed."
density_score: 0.92
related:
  - run_a_naked_opus
  - run_b_cexai_opus
  - p12_ct_four_runtime_showoff
  - p01_kc_agent
  - bld_schema_agent
  - bld_architecture_agent
  - bld_knowledge_card_agent
  - p11_qg_agent
  - bld_instruction_kind
  - spec_plateau
---

## Experiment Design

| Parameter | Value |
|-----------|-------|
| Task | "Build a customer support triage agent with RAG, escalation, multi-language" |
| Model | Claude Opus 4.6 (both runs) |
| Run A | Naked -- no ISOs, no schema, no 8F, no builder |
| Run B | CEXAI -- 8 builder ISOs, 8F pipeline, quality gates, compiled output |
| Scoring | cex_evolve.py heuristic (L1 structural 50% + L2 rubric 50%) |

## Structural Comparison

| Dimension | Run A (Naked) | Run B (CEXAI) | Delta |
|-----------|---------------|---------------|-------|
| Heuristic score | 8.0 | 8.8 | **+0.8** |
| Lines | 430 | 158 | -63% (denser) |
| Bytes | 19,275 | 6,176 | -68% (cheaper) |
| Table rows | 101 | 50 | -50% (structured) |
| Sections (##) | 25 | 13 | -48% (focused) |
| Frontmatter fields | 9 | 24 | **+167%** |
| Has pillar | NO | YES (P02) | schema-typed |
| Has llm_function | NO | YES (BECOME) | pipeline-aware |
| Has agent_group | NO | YES (support-engine) | fleet-manageable |
| Has capabilities_count | NO | YES (6) | machine-auditable |
| Has tools_count | NO | YES (8) | machine-auditable |
| Has iso_files_count | NO | YES (10) | self-documenting |
| Has linked_artifacts | NO | YES (10 refs) | graph-connected |
| Has density_score | YES (1.0 invalid) | YES (0.91 valid) | calibrated |
| Compiled to YAML | NO | YES | machine-readable |
| Quality gates run | 0 | 18 (8H + 10S) | governed |

## Qualitative Analysis

### What Naked Opus Produced

A well-written 430-line document with embedded system prompt, tool definitions, routing tables, error handling prose, and example conversations. Human-readable. But:

- No pillar assignment -- invisible to the 12P taxonomy
- No llm_function -- pipeline cannot route it
- No agent_group -- fleet management blind spot
- No linked_artifacts -- graph orphan (no connections)
- No compilation target -- stays as markdown forever
- No quality gates -- zero governance signal
- density_score 1.0 is invalid (no artifact has perfect density)
- 19KB for one agent -- context budget blow (3x over 5120B body limit)

### What CEXAI Opus Produced

A 158-line governed artifact with 24 frontmatter fields, structured tables, escalation rules (T0-T3), RAG config parameters, and 10 cross-references. But:

- 68% smaller -- 3x context efficiency
- Schema-typed -- every field validated
- Graph-connected -- 10 linked artifacts enable navigation
- Compiled -- YAML output enables tooling
- Governed -- 18 gates caught the id prefix issue BEFORE delivery
- Fleet-ready -- agent_group enables multi-agent orchestration

## The Real Delta

The heuristic score delta (+0.8) understates the framework leverage because:

1. **Heuristic scoring caps at ~9.0** -- it measures structure and rubric, not semantic depth
2. **Context cost** -- Run A costs 3.1x more tokens to inject (19K vs 6K)
3. **Composability** -- Run B plugs into 300 kinds, 12 pillars, 8 nuclei. Run A is standalone prose.
4. **Governance** -- Run B caught its own quality issues (gate H03 exception documented). Run A has no self-correction mechanism.
5. **Machine readability** -- Run B compiled to YAML. Run A requires human parsing.

| Leverage Dimension | Naked | CEXAI | Winner |
|--------------------|-------|-------|--------|
| Token cost (inject) | 19,275 B | 6,176 B | CEXAI (3.1x) |
| Schema compliance | 0 gates | 18 gates | CEXAI |
| Cross-references | 0 | 10 | CEXAI |
| Compilation | impossible | automatic | CEXAI |
| Fleet management | manual | agent_group | CEXAI |
| Human readability | excellent | good | Naked (slightly) |
| Machine readability | poor | excellent | CEXAI |
| Reusability | copy-paste | import | CEXAI |

## Verdict

Same LLM, same task. CEXAI produces a **typed, governed, compiled, graph-connected** artifact that is 68% smaller and passes 18 quality gates. The naked version is a well-written document that cannot be composed, validated, or compiled.

**CEXAI is not about making the LLM smarter. It is about making the LLM's output infrastructure.**
