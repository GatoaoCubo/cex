---
kind: tools
id: bld_tools_dual_loop_architecture
pillar: P04
parent: dual-loop-architecture-builder
llm_function: CALL
purpose: Tools the dual_loop_architecture builder invokes -- scheduler, bridge, critic, router
quality: 9.0
title: "Tools Dual Loop Architecture"
version: "1.0.0"
author: wave1_builder_gen
tags: [dual_loop_architecture, builder, tools, scheduler, memory_bridge]
keywords: [tick_scheduler, memory_bridge, critic, trajectory_log, plan_slot, router]
tldr: "Tools for building dual-loop agents: tick scheduler, memory bridge, trajectory log, critic, model router."
domain: "dual_loop_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_config_dual_loop_architecture
  - bld_architecture_dual_loop_architecture
  - bld_collaboration_dual_loop_architecture
  - p03_sp_dual_loop_architecture_builder
  - bld_knowledge_card_dual_loop_architecture
  - p10_lr_dual_loop_architecture_builder
  - dual-loop-architecture-builder
  - kc_dual_loop_architecture
  - bld_instruction_dual_loop_architecture
  - p08_qg_dual_loop_architecture
---

## Runtime Tools (what the produced artifact consumes)

This ISO applies to the dual loop pattern, coordinating an outer orchestrator with one or more inner worker loops.

| Tool | Purpose | When | Owner loop |
|------|---------|------|------------|
| tick_scheduler | Drives InnerLoopRunner at fixed tick_ms cadence; also fires outer cadence_s | boot | both |
| memory_bridge | Read/write shared state: PlanSlot, trajectory, scratchpad | every tick + every plan | both |
| trajectory_log | Append-only ring buffer of (obs, action, reward) for critic/planner | per inner tick | inner w, outer r |
| plan_slot_swap | Atomic pointer swap so inner never reads a half-written plan | on outer plan commit | outer w, inner r |
| critic_fn | Scores trajectory window, emits regret signal to trigger early re-plan | outer cadence or on-demand | outer |
| model_router | Routes inner calls to fast tier (Sonnet/Haiku/mini), outer to reasoning tier (Opus/o1) | every LLM call | both |
| budget_governor | Halts outer loop when token/cost/time cap hit; inner keeps running on last plan | outer cadence | outer |
| signal_bus | mpsc channel for outer -> inner plan pushes and inner -> outer critique asks | async | both |

## Build-time Tools (what the builder uses to PRODUCE the artifact)

| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile produced .md spec to runnable yaml + stub code | F8 COLLABORATE |
| cex_score.py | 5D quality scoring (density, specificity, correctness, completeness, consistency) | F7 GOVERN |
| cex_retriever.py | Pull similar dual-loop specs + KCs (Reflexion, OODA, SoT) for F3 INJECT | F3 INJECT |
| cex_doctor.py | Check frontmatter, ID pattern p08_dl_*, byte budget, required fields | F7 GOVERN |
| cex_schema_hydrate.py | Expand bld_schema into full frontmatter template | F1 CONSTRAIN |
| signal_writer.py | Emit completion signal with quality score to N07 | F8 COLLABORATE |

## External References

- LangGraph (graph-based dual-loop: supervisor + worker)
- AutoGen (GroupChat with fast responder + slow reviewer)
- Reflexion codebase (github.com/noahshinn/reflexion)
- OpenAI o1/o3 (reasoning tier for outer loop)
- Anthropic extended thinking (slow outer-loop mode on Opus)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_dual_loop_architecture]] | downstream | 0.67 |
| [[bld_architecture_dual_loop_architecture]] | downstream | 0.64 |
| [[bld_collaboration_dual_loop_architecture]] | downstream | 0.58 |
| [[p03_sp_dual_loop_architecture_builder]] | upstream | 0.55 |
| [[bld_knowledge_card_dual_loop_architecture]] | upstream | 0.55 |
| [[p10_lr_dual_loop_architecture_builder]] | downstream | 0.52 |
| [[dual-loop-architecture-builder]] | downstream | 0.47 |
| [[kc_dual_loop_architecture]] | upstream | 0.46 |
| [[bld_instruction_dual_loop_architecture]] | upstream | 0.46 |
| [[p08_qg_dual_loop_architecture]] | downstream | 0.45 |
