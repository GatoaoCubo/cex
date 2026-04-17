---
kind: config
id: bld_config_consolidation_policy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for consolidation_policy production
quality: 8.7
title: "Config: consolidation_policy-builder"
version: "2.0.0"
author: n06_commercial
tags: [consolidation_policy, builder, config]
tldr: "Naming convention p10_cp_*, pillar P10, max 6144 bytes, stored in P10_memory/ or agent-specific subdirectory"
domain: "LLM agent memory consolidation"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

## Naming Convention

Pattern: `p10_cp_[a-z][a-z0-9_]+`
Examples:
- `p10_cp_customer_support_pro`
- `p10_cp_research_agent_enterprise`
- `p10_cp_minimal_ttl_only`

## Paths

Artifacts stored in pillar directory:
`P10_memory/policies/`

Or co-located with parent memory_architecture:
`N0{x}_*/memory/p10_cp_*.md`

## Limits

- max_bytes: 6144
- max_turns: null (static policy spec)
- effort_level: 4 (high -- requires reading parent memory_architecture first)
- quality_floor: 8.0
- quality_target: 9.0

## Hooks

- pre_build: read parent memory_architecture artifact to determine active layers + tier
- post_build: `python _tools/cex_compile.py {path}`
- on_quality_fail: check domain accuracy first (D04 contamination is most common failure)
- on_error: verify consolidation_async: true is set and no OS/GC terminology present
