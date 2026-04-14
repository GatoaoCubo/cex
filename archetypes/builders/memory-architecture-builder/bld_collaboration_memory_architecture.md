---
kind: collaboration
id: bld_collaboration_memory_architecture
pillar: P12
llm_function: COLLABORATE
purpose: How memory_architecture-builder works in crews with other builders
quality: null
title: "Collaboration Memory Architecture"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_architecture, builder, collaboration]
tldr: "How memory_architecture-builder works in crews with other builders"
domain: "memory_architecture construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Designs memory system hierarchy, integrates components, ensures compatibility, and optimizes performance across storage, cache, and interface layers.  

## Receives From  
| Builder           | What                  | Format      |  
|-------------------|-----------------------|-------------|  
| memory_controller_builder | Controller specs      | JSON        |  
| storage_builder     | Storage capacity reqs | YAML        |  
| interface_builder   | Bus protocol details  | XML         |  
| performance_analyzer | Benchmark data        | CSV         |  

## Produces For  
| Builder           | What                  | Format      |  
|-------------------|-----------------------|-------------|  
| memory_controller_builder | Design constraints doc | PDF         |  
| storage_builder     | Integration roadmap   | Markdown    |  
| interface_builder   | Compatibility report  | JSON        |  
| validation_team     | System spec           | XML         |  

## Boundary  
Does NOT handle memory_type (e.g., DRAM, SSD) or memory_scope (e.g., cache vs. main memory). These are handled by memory_type_builder and memory_scope_builder, respectively. Physical layout and fabrication details are managed by layout_engineers.
