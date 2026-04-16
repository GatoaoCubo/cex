---
kind: config
id: bld_config_workflow_node
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for workflow_node production
quality: 8.6
title: "Config Workflow Node"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [workflow_node, builder, config]
tldr: "Naming, paths, limits for workflow_node production"
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p12_wn_{{name}}.md`
Examples: `p12_wn_data_processing.md`, `p12_wn_user_auth.md`

## Paths
Artifacts: `/mnt/artifacts/p12/workflow_nodes/{{name}}/`
Logs: `/var/log/p12/workflow_nodes/{{name}}/`

## Limits
max_bytes: 4096
max_turns: 5
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
