---
kind: config
id: bld_config_edit_format
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for edit_format production
quality: null
title: "Config Edit Format"
version: "1.0.0"
author: wave1_builder_gen
tags: [edit_format, builder, config]
tldr: "Naming, paths, limits for edit_format production"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
Pattern: `p06_ef_{{name}}.md`  
Examples:  
- `p06_ef_report.md`  
- `p06_ef_summary.md`  

## Paths  
Storage: `/artifacts/p06/{{name}}.md`  

## Limits  
- max_bytes: 4096  
- max_turns:  
- effort_level:  

## Hooks  
- pre_build: null  
- post_build: null  
- on_error: null  
- on_quality_fail: null
