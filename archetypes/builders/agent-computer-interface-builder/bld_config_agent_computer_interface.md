---
kind: config
id: bld_config_agent_computer_interface
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for agent_computer_interface production
quality: 8.6
title: "Config Agent Computer Interface"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_computer_interface, builder, config]
tldr: "Naming, paths, limits for agent_computer_interface production"
domain: "agent_computer_interface construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention
Pattern: p08_aci_{{name}}.md
Examples:
- p08_aci_auth_module.md
- p08_aci_data_parser.md

## Paths
Artifacts: ./artifacts/p08_aci/

## Limits
max_bytes: 5120
max_turns: 15
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
