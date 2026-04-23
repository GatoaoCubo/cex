---
kind: collaboration
id: bld_collaboration_judge_config
pillar: P12
llm_function: COLLABORATE
purpose: How judge_config-builder works in crews with other builders
quality: 8.9
title: "Collaboration Judge Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [judge_config, builder, collaboration]
tldr: "How judge_config-builder works in crews with other builders"
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - judge-config-builder
  - llm-judge-builder
  - bld_collaboration_llm_judge
  - p01_kc_llm_judge
  - p03_sp_judge_config_builder
  - p07_llm_judge
  - bld_tools_judge_config
  - bld_architecture_llm_judge
  - p10_lr_llm_judge_builder
  - p03_sp_llm_judge_builder
---

## Crew Role  
Defines and maintains judge configuration parameters, rules, and constraints for consistent evaluation.  

## Receives From  
| Builder       | What                  | Format  |  
|---------------|-----------------------|---------|  
| config_spec   | Configuration spec    | YAML    |  
| judge_spec    | Judge instance spec   | JSON    |  
| ruleset       | Evaluation rules      | YAML    |  

## Produces For  
| Builder       | What                      | Format  |  
|---------------|---------------------------|---------|  
| judge_config  | Judge configuration file  | YAML    |  
| config_report | Validation report         | JSON    |  
| config_schema | Configuration schema      | JSON    |  

## Boundary  
Does NOT handle LLM judge instances (llm_judge) or human-generated rubrics (scoring_rubric). LLM judge instances are managed by llm_judge, and rubrics are handled by scoring_rubric.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[judge-config-builder]] | upstream | 0.51 |
| [[llm-judge-builder]] | upstream | 0.48 |
| [[bld_collaboration_llm_judge]] | sibling | 0.46 |
| [[p01_kc_llm_judge]] | upstream | 0.45 |
| [[p03_sp_judge_config_builder]] | upstream | 0.43 |
| [[p07_llm_judge]] | upstream | 0.31 |
| [[bld_tools_judge_config]] | upstream | 0.31 |
| [[bld_architecture_llm_judge]] | upstream | 0.29 |
| [[p10_lr_llm_judge_builder]] | upstream | 0.28 |
| [[p03_sp_llm_judge_builder]] | upstream | 0.27 |
