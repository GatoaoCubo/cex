---
kind: config
id: bld_config_thinking_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for thinking_config production
quality: 8.9
title: "Config Thinking Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [thinking_config, builder, config]
tldr: "Naming, paths, limits for thinking_config production"
domain: "thinking_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention

This ISO configures a thinking budget: how many tokens the model may spend on internal reasoning before emitting.
Pattern: `p09_thk_{{name}}.yaml`
Examples: `p09_thk_report.yaml`, `p09_thk_analysis.yaml`

## Paths
Artifacts stored in: `/artifacts/p09/{{name}}/`

## Limits
max_bytes: 2048
max_turns: 5
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | thinking_config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
