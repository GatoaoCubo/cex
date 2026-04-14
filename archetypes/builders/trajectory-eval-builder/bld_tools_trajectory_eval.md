---
kind: tools
id: bld_tools_trajectory_eval
pillar: P04
llm_function: CALL
purpose: Tools available for trajectory_eval production
quality: null
title: "Tools Trajectory Eval"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [trajectory_eval, builder, tools]
tldr: "Tools available for trajectory_eval production"
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| cex_compile.py | Compiles trajectory data into standardized format | Pre-processing |  
| cex_score.py | Calculates evaluation metrics (e.g., smoothness, accuracy) | Post-processing |  
| cex_retriever.py | Retrieves relevant trajectory data from storage | Data analysis |  
| cex_doctor.py | Diagnoses inconsistencies in trajectory logs | Validation phase |  
| cex_validator.py | Validates data integrity and format compliance | Quality checks |  
| cex_visualizer.py | Visualizes trajectories for debugging | Reporting |  

## Validation Tools  
| Tool | Purpose | When |  
|------|---------|------|  
| cex_linter.py | Checks syntax and structure of trajectory files | Code review |  
| cex_consistency_checker.py | Ensures temporal and spatial data consistency | Validation |  
| cex_performance_analyzer.py | Analyzes computational efficiency of trajectory algorithms | Optimization |  

## External References  
- TrajectoryEval Framework (official library for trajectory evaluation)  
- Waymo Open Dataset (standardized trajectory data format)  
- CARLA Simulation (for testing trajectory algorithms in virtual environments)
