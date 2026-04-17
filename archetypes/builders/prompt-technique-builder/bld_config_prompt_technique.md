---
kind: config
id: bld_config_prompt_technique
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for prompt_technique production
quality: 8.6
title: "Config Prompt Technique"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_technique, builder, config]
tldr: "Naming, paths, limits for prompt_technique production"
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p03_pt_{{name}}.md`
Examples:
- `p03_pt_summarization.md`
- `p03_pt_qa.md`

## Paths
Artifacts stored in: `/opt/cex/techniques/p03/{{name}}.md`

## Limits
- max_bytes: 4096
- max_turns: 5
- effort_level: 3

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null
