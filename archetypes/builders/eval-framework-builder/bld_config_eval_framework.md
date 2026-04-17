---
kind: config
id: bld_config_eval_framework
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for eval_framework production
quality: 8.6
title: "Config Eval Framework"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_framework, builder, config]
tldr: "Naming, paths, limits for eval_framework production"
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p07_efw_{{name}}.md`
Examples: `p07_efw_chatbot.md`, `p07_efw_summarizer.md`

## Paths
Artifacts: `/mnt/artifacts/p07/efw/{{name}}`
Logs: `/var/log/eval_framework/p07/{{name}}`

## Limits
max_bytes: 5120
max_turns: 20
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
