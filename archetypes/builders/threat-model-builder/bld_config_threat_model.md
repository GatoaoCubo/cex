---
kind: config
id: bld_config_threat_model
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for threat_model production
quality: 8.6
title: "Config Threat Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [threat_model, builder, config]
tldr: "Naming, paths, limits for threat_model production"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.
Pattern: `p11_tm_{{name}}.md`  
Examples: `p11_tm_webapp.md`, `p11_tm_api.md`  

## Paths  
Artifacts stored in: `/artifacts/p11/{{name}}/`  

## Limits  
max_bytes: 5120  
max_turns: 10  
effort_level: medium  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null
