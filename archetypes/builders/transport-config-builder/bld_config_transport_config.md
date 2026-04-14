---
kind: config
id: bld_config_transport_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for transport_config production
quality: 8.6
title: "Config Transport Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [transport_config, builder, config]
tldr: "Naming, paths, limits for transport_config production"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
Pattern: `p09_tc_<name>.yaml`  
Examples:  
- `p09_tc_ship.yaml`  
- `p09_tc_drone.yaml`  

## Paths  
Artifacts stored in: `/artifacts/p09/transport_configs/`  

## Limits  
- `max_bytes`: 2048  
- `max_turns`: 10  
- `effort_level`: 3  

## Hooks  
- `pre_build`: null  
- `post_build`: null  
- `on_error`: null  
- `on_quality_fail`: null
