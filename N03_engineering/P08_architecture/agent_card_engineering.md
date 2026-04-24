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
tldr: Deployment spec -- capabilities matrix, resource needs, SLA, failure modes.
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
| Single artifact build | Expert (99/99 kinds) |
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

## Quality Metrics

| Metric | Value | Threshold |
|--------|-------|-----------|
| Structural completeness | High | ≥ 8.5 |
| Domain specificity | engineering | Verified |
| Cross-reference density | Adequate | ≥ 3 refs |
| Actionability | Verified | Pass |

### Key Principles

- Agent identity persists across sessions via filesystem state
- Capabilities declared explicitly; implicit inference prohibited
- Constraint violations logged and escalated to N07 orchestrator
- Version pinning ensures reproducible agent behavior across deploys

### Usage Reference

```yaml
# agent_card integration
artifact: agent_card_engineering
nucleus: N03
domain: engineering
quality_threshold: 9.0
```

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
