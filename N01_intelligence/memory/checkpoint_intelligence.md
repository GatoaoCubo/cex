---
id: p10_ck_research_checkpoint
title: "Checkpoint Intelligence — Research Session State"
kind: checkpoint
pillar: P10
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n01_intelligence
name: Research Session Checkpoint
workflow_ref: p12_wf_research_pipeline
step: checkpoint_research_state
quality: 8.9
tags: [checkpoint, research, intelligence, n01, session, resumable]
tldr: "Freezes N01 research session state — sources gathered, claims verified, outputs pending — so interrupted research can resume without re-gathering data."
description: "Stores research pipeline state to resume interrupted analysis without losing source catalog, verification status, or partial outputs."
state:
  research_phase: string              # discovery|gathering|verification|synthesis|output
  research_topic: string              # active research question
  sources_gathered: int               # count of sources found
  sources_verified: int               # count of sources passing quality gate
  claims_pending: int                 # unverified claims remaining
  claims_verified: int                # claims with 3+ source triangulation
  output_type: string                 # competitive_grid|swot|market_snapshot|trend_report|benchmark|executive_summary
  output_draft_path: string           # path to partial output file
  output_completeness: float          # 0.0-1.0 (% of sections filled)
  mcp_servers_used: list[string]      # which MCP servers were queried
  schema_contracts_loaded: list[string] # which contracts are active
  freshness_cutoff: string            # ISO date for data staleness threshold
  blockers: list[string]              # what's preventing progress
  next_action: string                 # specific next step to take on resume
  quality_estimate: float             # projected quality if completed now
  time_elapsed_minutes: int           # total research time so far
resumable: true
ttl: 48h
parent_checkpoint: null
retry_count: 0
error: null
domain: research-intelligence
density_score: 0.93
---

# Overview

This checkpoint captures the state of an N01 research session mid-execution, enabling safe resume after interruption (context window limit, rate limit, session timeout, or orchestrator preemption). Unlike N05's deploy checkpoint which tracks infrastructure state, this tracks intellectual state — what's been found, what's verified, what's still needed.

## State Contract

| Key | Type | Description |
|-----|------|-------------|
| `research_phase` | string | Current phase: `discovery`, `gathering`, `verification`, `synthesis`, `output` |
| `research_topic` | string | The active research question or intent |
| `sources_gathered` | int | Total sources found (all quality levels) |
| `sources_verified` | int | Sources passing `source_quality_contract.md` gate |
| `claims_pending` | int | Claims awaiting triangulation (< 3 sources) |
| `claims_verified` | int | Claims with 3+ independent source confirmation |
| `output_type` | string | Target output kind (competitive_grid, swot, etc.) |
| `output_draft_path` | string | Path to work-in-progress output file |
| `output_completeness` | float | Fraction of output sections completed (0.0-1.0) |
| `mcp_servers_used` | list[string] | MCP servers already queried this session |
| `schema_contracts_loaded` | list[string] | Active schema contracts governing this research |
| `freshness_cutoff` | string | ISO date — data older than this is flagged STALE |
| `blockers` | list[string] | Issues preventing forward progress |
| `next_action` | string | Exact next step for resume — actionable, not vague |
| `quality_estimate` | float | Projected quality score if output were finalized now |
| `time_elapsed_minutes` | int | Cumulative research time |

## Resume Protocol

1. Load this checkpoint
2. Verify `mcp_servers_used` are still accessible
3. Check `freshness_cutoff` against current date — if >7 days since checkpoint, re-verify time-sensitive sources
4. Resume from `next_action` — do not restart from `discovery` unless `research_phase` is `discovery`
5. If `blockers` is non-empty, report blockers to N07 before proceeding

## Comparison to N05 Checkpoint

| Dimension | N01 (Research) | N05 (Deploy) |
|-----------|----------------|--------------|
| State tracked | Intellectual (sources, claims) | Infrastructure (services, health) |
| TTL | 48h (research freshness) | 72h (deploy stability) |
| Resume risk | Data staleness | Service drift |
| Rollback | Re-gather stale sources | Revert deploy |
| Criticality | Medium (rework) | High (downtime) |

## Boundary

Estado salvo. NAO eh signal.


## 8F Pipeline Function

Primary function: **GOVERN**
