---
kind: config
id: bld_config_memory_benchmark
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for memory_benchmark production
quality: 8.6
title: "Config Memory Benchmark"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_benchmark, builder, config]
tldr: "Naming, paths, limits for memory_benchmark production"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

p07_mb_{{name}}.md
## Naming Convention
Pattern: `p07_mb_{{name}}.md`
Examples: `p07_mb_memory_test.md`, `p07_mb_cache_check.md`

## Paths
Artifacts: `/mnt/artifacts/p07/memory_benchmarks/`
Logs: `/var/log/p07/memory_benchmark-builder/`

## Limits
max_bytes: 5120
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
