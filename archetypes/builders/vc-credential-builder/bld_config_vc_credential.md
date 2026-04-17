---
kind: config
id: bld_config_vc_credential
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for vc_credential production
quality: 8.6
title: "Config VC Credential"
version: "1.0.0"
author: n04_wave7
tags: [vc_credential, builder, config, W3C, did, p10]
tldr: "Naming, paths, limits for vc_credential production"
domain: "vc_credential construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p10_vc_{{name}}.md`
Examples: `p10_vc_agent_n03_capability.md`, `p10_vc_provenance_run_20260414.md`

## Paths
Artifacts stored in: `P10_memory/credentials/{{name}}.md`

## Limits
max_bytes: 4096
max_turns: 5
effort_level: 4

## Hooks
pre_build: validate_did_format
post_build: compile_to_yaml
on_error: null
on_quality_fail: rebuild_with_schema_fix
