---
kind: config
id: bld_config_legal_vertical
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for legal_vertical production
quality: 8.6
title: "Config Legal Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [legal_vertical, builder, config]
tldr: "Naming, paths, limits for legal_vertical production"
domain: "legal_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

p01_lv_{{name}}.md
## Naming Convention
Pattern: p01_lv_{{name}}.md
Examples: p01_lv_compliance_policy.md, p01_lv_data_privacy.md

## Paths
/mnt/artifacts/p01/legal_vertical/{{name}}
/mnt/logs/p01/{{name}}_build.log

## Limits
max_bytes: 6144
max_turns: 5
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
