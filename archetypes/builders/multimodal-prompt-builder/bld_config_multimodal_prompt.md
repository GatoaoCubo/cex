---
kind: config
id: bld_config_multimodal_prompt
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for multimodal_prompt production
quality: 8.6
title: "Config Multimodal Prompt"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [multimodal_prompt, builder, config]
tldr: "Naming, paths, limits for multimodal_prompt production"
domain: "multimodal_prompt construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: p03_mmp_<project>_<module>.md
Examples: p03_mmp_cex_core.md, p03_mmp_ai_vision.md

## Paths
Artifacts: /mnt/data/cex/p03/mmp/<project>/artifacts
Logs: /var/log/cex/p03/mmp/<project>

## Limits
max_bytes: 4096
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
