---
kind: collaboration
id: bld_collaboration_transport_config
pillar: P12
llm_function: COLLABORATE
purpose: How transport_config-builder works in crews with other builders
quality: 8.9
title: "Collaboration Transport Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [transport_config, builder, collaboration]
tldr: "How transport_config-builder works in crews with other builders"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  
Defines transport layer protocols, endpoints, and security settings for system communication. Ensures compatibility and reliability across network boundaries.  

## Receives From  
| Builder           | What                  | Format  |  
|-------------------|-----------------------|---------|  
| network_policy_builder | Network policy rules  | JSON    |  
| security_policy_builder | Security constraints  | YAML    |  
| service_discovery_builder | Service discovery specs | JSON  |  

## Produces For  
| Builder           | What                  | Format  |  
|-------------------|-----------------------|---------|  
| transport_layer   | Transport config spec | JSON    |  
| api_gateway       | API gateway config    | YAML    |  
| load_balancer     | Load balancer settings| JSON    |  

## Boundary  
Does NOT handle session lifecycle (realtime_session_builder) or LLM streaming (streaming_config_builder). Higher-level orchestration is managed by orchestration_engine.
