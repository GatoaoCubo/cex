---
id: p08_ac_builder_nucleus
kind: agent_card
8f: F2_become
pillar: P08
title: Agent Card -- Builder Nucleus
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [agent-card, builder, N03]
tldr: "N03 deployment spec: Opus 1M context, 10-120s latency per artifact, 300+ kind coverage, 7-gate quality SLA >= 8.0, 4 failure modes with automatic recovery."
density_score: 0.88
related:
  - agent_card_engineering_nucleus
  - p12_sig_builder_nucleus
  - p12_dr_builder_nucleus
  - p06_if_builder_nucleus
  - p03_pt_builder_construction
  - p04_fd_builder_toolkit
  - p08_pat_builder_construction
  - p07_bm_builder_nucleus
  - p02_agent_builder_nucleus
  - bld_architecture_kind
---

# Agent Card: Builder Nucleus

## Summary

| Field | Value |
|-------|-------|
| Name | Builder Nucleus (N03) |
| Domain | Meta-construction |
| Model | opus default, sonnet/haiku by complexity |
| Input | Natural language or explicit kind |
| Output | Validated artifact (.md + .yaml) |
| Latency | 10-120s per artifact |
| Quality SLA | >= 8.0 on all outputs |

## Capabilities

| Capability | Level |
|------------|-------|
| Single artifact build | Expert (99/300 kinds) |
| Multi-kind crew | Advanced (235 crews) |
| Nucleus bootstrap | Advanced (7+ sequential) |
| Kind registration | Expert (4-file atomic) |
| Quality validation | Expert (7 gates) |

## Failure Modes

| Mode | Detection | Recovery |
|------|-----------|----------|
| Kind not found | Motor empty | Suggest closest |
| Builder missing | F2 load fail | Doctor report |
| Quality < 8.0 | F7 reject | Retry 2x then abort |
| Timeout | Process killed | Error signal |

## Resource Requirements

| Resource | Minimum | Recommended | Notes |
|----------|---------|-------------|-------|
| Model | Sonnet (simple kinds) | Opus (multi-kind, bootstrap) | Routed via nucleus_models.yaml |
| Context window | 128K | 1M | Multi-artifact crews need 500K+ |
| API key | ANTHROPIC_API_KEY | Same | Required for non-dry-run |
| Disk | 50MB (builders) | 200MB (full N03) | Read-only access to archetypes/ |
| MCP servers | 0 | 0 | N03 uses only local Python tools |

## SLA Guarantees

| Metric | Target | Measurement |
|--------|--------|-------------|
| Kind resolution accuracy | 99/99 (100%) | cex_8f_motor.py --validate |
| Quality floor adherence | 100% of published artifacts >= 8.0 | F7 GOVERN gate |
| Signal delivery | < 5s after completion | File write to .cex/runtime/signals/ |
| Recovery from soft failure | <= 2 retry cycles | F6-F7 loop with targeted fixes |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_engineering_nucleus]] | sibling | 0.38 |
| [[p12_sig_builder_nucleus]] | downstream | 0.37 |
| [[p12_dr_builder_nucleus]] | downstream | 0.32 |
| [[p06_if_builder_nucleus]] | upstream | 0.31 |
| [[p03_pt_builder_construction]] | upstream | 0.30 |
| [[p04_fd_builder_toolkit]] | upstream | 0.28 |
| [[p08_pat_builder_construction]] | related | 0.28 |
| [[p07_bm_builder_nucleus]] | upstream | 0.27 |
| [[p02_agent_builder_nucleus]] | upstream | 0.27 |
| [[bld_architecture_kind]] | related | 0.27 |
