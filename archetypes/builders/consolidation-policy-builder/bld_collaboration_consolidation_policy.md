---
kind: collaboration
id: bld_collaboration_consolidation_policy
pillar: P12
llm_function: COLLABORATE
purpose: How consolidation_policy-builder works in crews with other builders
quality: null
title: "Collaboration Consolidation Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [consolidation_policy, builder, collaboration]
tldr: "How consolidation_policy-builder works in crews with other builders"
domain: "consolidation_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Coordinates memory lifecycle policy consolidation across systems, ensuring alignment with retention rules, eviction priorities, and resource constraints.  

## Receives From  
| Builder         | What                  | Format  |  
|-----------------|-----------------------|---------|  
| memory_monitor  | Real-time usage data  | JSON    |  
| policy_validator| Validated rules       | YAML    |  
| config_manager  | System parameters     | TOML    |  

## Produces For  
| Builder          | What                    | Format  |  
|------------------|-------------------------|---------|  
| memory_allocator | Policy-ready rules      | JSON    |  
| policy_enforcer  | Consolidated policy     | YAML    |  
| logging_system   | Audit logs              | CSV     |  

## Boundary  
Does NOT handle memory_scope (access rules) or compression_config (token compression).  
Memory_scope handled by access_rule_builder; compression_config handled by token_compressor.
