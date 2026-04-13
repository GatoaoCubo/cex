---
kind: config
id: bld_config_incident_report
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for incident_report production
quality: null
title: "Config Incident Report"
version: "1.0.0"
author: wave1_builder_gen
tags: [incident_report, builder, config]
tldr: "Naming, paths, limits for incident_report production"
domain: "incident_report construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
Pattern: `p11_ir_{{name}}.md` (e.g., `p11_ir_inc001.md`). {{name}} replaced with incident identifier. ASCII-only, lowercase.  

## Paths  
Artifacts stored in `/artifacts/incident_reports/`.  

## Limits  
max_bytes: 5120  
max_turns: 0  
effort_level: low  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null
