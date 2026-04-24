---
id: p10_ms_n07_orchestration
kind: memory_summary
8f: F3_inject
pillar: P10
nucleus: N07
title: "N07 Orchestrator -- 30-Day Mission Memory"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "memory-summary-builder"
name: "N07 Orchestration History Summary"
source_type: multi_session
compression_method: hybrid
quality: 8.4
tags: [memory_summary, orchestration, n07, missions, routing]
tldr: "Compressed 30-day N07 orchestration log: 5 missions, routing decisions, process lessons, token spend. Inject at boot."
max_tokens: 1800
trigger: time_based
source_window: 30
retain_entities: true
retain_timestamps: true
freshness_decay: 0.05
description: "Hybrid-compressed orchestration history for N07 boot context. Covers missions N00-N07, routing decisions, dispatch lessons, and token economy."
last_updated: "2026-04-17"
staleness_flag: "auto-flag if updated > 7 days ago"
related:
  - p01_kc_orchestration_best_practices
  - p03_sp_orchestration_nucleus
  - p01_kc_cex_orchestration_architecture
  - p12_wf_orchestration_pipeline
  - agent_card_engineering_nucleus
  - p08_ac_orchestrator
  - p02_agent_admin_orchestrator
  - p12_wf_create_orchestration_agent
  - p02_agent_creation_nucleus
  - n07_output_orchestration_audit
---
<!-- 8F PIPELINE
F1 CONSTRAIN: kind=memory_summary, pillar=P10, max_bytes=2048, naming=p10_summary_n07.md
F2 BECOME: memory-summary-builder ISOs loaded (13 ISOs). Identity: compression specialist.
F3 INJECT: kc pattern from bld_memory -- hybrid method, explicit retention, freshness_decay<=0.1 for multi_session
F4 REASON: 6 sections, approach=hybrid (narrative flow + extractive for decisions/lessons)
F5 CALL: compile ready
F6 PRODUCE: artifact written (~1700 bytes body)
F7 GOVERN: quality:null, enums valid, 4+ sections present, no session_state contamination
F8 COLLABORATE: compiled to YAML
-->

## Overview

Compressed orchestration memory for N07 boot context injection. Covers the last 30 days of
multi-session mission activity. Consumed by N07 at session start instead of replaying
hundreds of individual handoffs and signal files. Fires after each mission consolidation
or every 7 days, whichever is sooner. Staleness guard: if `last_updated` is more than
7 days before today, treat all routing decisions as provisional until re-verified.

## Compression

Method: hybrid -- abstractive narrative for mission flow; extractive lift for routing decisions, blockers, and lessons  
Ratio: ~40:1 (approx 72000 tokens of handoffs + signals -> 1800 tokens output)  
Preserved: mission names, nucleus assignments, quality outcomes, blockers, routing decisions, token spend, process lessons  
Dropped: raw handoff prose, repeated clarification loops, intermediate signal payloads, git commit messages

## Trigger

Condition: time_based >= 7 days OR explicit (after mission consolidation)  
Threshold: 7 days since last_updated OR consolidation signal received  
On fire: rebuild this file via memory-summary-builder, replace in place, bump updated date

## Retention

Entities: retained -- mission IDs, nucleus IDs (N01-N07), tool names, quality scores, blocker descriptions  
Decisions: retained -- routing choices, model tier assignments, dispatch mode selections  
Action items: retained -- open blockers with owning nucleus; pending missions  
Timestamps: retained -- mission start/end dates, last_updated marker

## Active Missions

| Mission | Status | Owning Nuclei | Blocker |
|---------|--------|--------------|---------|
| VERTICAL_DENSIFICATION W1 | in-progress | N03, N05 | 18 stale P0x paths patched; W2 not started |
| SELF_IMPROVEMENT_LOOP | in-progress | N05 | compiled artifact exists; integration pending |

## Completed Missions (Last 30 Days)

| Mission | Waves | Nuclei Used | Outcome | Artifacts |
|---------|-------|-------------|---------|-----------|
| SELF_ASSEMBLY W1 | 1 | N01-N06 | PASS | 37 new artifacts, 7 pillars |
| BROWSER_CDP | 2 | N03, N05 | PASS | Chrome CDP stack proven end-to-end |
| BORIS_MERGE | 1 | N03, N05 | PASS | 21 items assimilated, 5 out-of-scope dropped |
| CONSOLIDATE_272 | 1 | N03, N07 | PASS | 272 files, 36K lines, cross-synthesis complete |
| SPEC_VERTICAL_DENSIFICATION | 1 | N07 | PASS | architecture self-audit + Karpathy sweep |

## Routing Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Default model tier | Opus for N03+N07, Sonnet for N01,N02,N04,N05,N06 | Cost vs depth tradeoff |
| Dispatch mode | solo sequential preferred over grid for <3 artifacts | Each spawn costs ~30k boot tokens |
| Gemini routing | SKIP until API upgrade | Free tier locks at "Thinking..." 25min+ |
| Ollama routing | llama3.1:8b for agentic tasks, qwen3:14b for N03+N04 | Bench 2026-04-15 |
| Local model max concurrency | 2-3 Ollama instances max | 6 competing = TPS collapse |
| Stop method | taskkill /F /PID <pid> /T only | Stop-Process orphans claude.exe + node.exe |

## Process Lessons

| Lesson | Anti-pattern | Correct Pattern |
|--------|-------------|----------------|
| Kill orphans before/after dispatch | Skip cleanup | Always run dispatch.sh stop + verify PIDs before new grid |
| Task files | Pass task as CLI arg | Write handoff to n0X_task.md; boot reads file |
| Blocking poll | cex_signal_watch.py inline | git log --since + dispatch.sh status (non-blocking) |
| N07 idle during grid | ScheduleWakeup sleep | Maintain work backlog; poll every 60-90s via bg bash |
| GDP before grid | Dispatch then ask | Collect all subjective decisions; write manifest FIRST |
| 8F-strict prompt on Ollama | Applied universally | Reserve strict 8F phase prompt for Claude/Gemini only |

## Token Budget (Last 30 Days)

| Category | Approx Spend | Value Signal |
|----------|-------------|--------------|
| Grid missions (6 nuclei) | ~180k tokens/grid | HIGH -- full artifact sets |
| Solo builds | ~30k tokens/build | HIGH -- focused output |
| Preflight (Ollama/Haiku) | ~5k tokens/run | HIGH -- ~70% main-token reduction |
| Failed Gemini attempts | ~40k tokens wasted | ZERO -- skip until paid tier |
| Orchestration overhead (N07) | ~15k tokens/session | MEDIUM -- compress via this artifact |

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory_summary` |
| Pillar | P10 |
| Nucleus | N07 |
| Domain | orchestration history |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Update trigger | time_based 7d OR mission consolidation |
| Quality target | null (never self-score) |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_orchestration_best_practices]] | upstream | 0.36 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.36 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.35 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.34 |
| [[agent_card_engineering_nucleus]] | upstream | 0.33 |
| [[p08_ac_orchestrator]] | upstream | 0.33 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.32 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.31 |
| [[p02_agent_creation_nucleus]] | upstream | 0.30 |
| [[n07_output_orchestration_audit]] | downstream | 0.30 |
