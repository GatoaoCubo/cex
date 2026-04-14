---
kind: collaboration
id: bld_collaboration_procedural_memory
pillar: P12
llm_function: COLLABORATE
purpose: How procedural_memory-builder works in crews with other builders
quality: null
title: "Collaboration Procedural Memory"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [procedural_memory, builder, collaboration]
tldr: "How procedural_memory-builder works in crews with other builders"
domain: "procedural_memory construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Manages procedural memory tasks, such as skill acquisition, habit formation, and motor pattern encoding. Coordinates with other builders to ensure seamless integration of learned procedures into autonomous systems.  

## Receives From  
| Builder          | What                          | Format      |  
|------------------|-------------------------------|-------------|  
| knowledge_card_builder | Declarative steps for procedures | JSON        |  
| entity_memory_builder  | Contextual entity references   | YAML        |  
| task_scheduler_builder | Action sequences to memorize   | ProtocolBuf |  
| sensor_data_processor  | Real-time feedback for refinement | CSV        |  

## Produces For  
| Builder          | What                          | Format      |  
|------------------|-------------------------------|-------------|  
| action_executor_builder | Encoded procedural routines   | Binary      |  
| habit_former_builder    | Reinforcement triggers        | JSON        |  
| skill_assessor_builder  | Proficiency metrics           | XML         |  
| feedback_loop_builder   | Error correction protocols    | ProtocolBuf |  

## Boundary  
Does NOT handle declarative knowledge (knowledge_card), entity facts (entity_memory), or high-level decision-making (planning_builder). Those are managed by respective builders.
