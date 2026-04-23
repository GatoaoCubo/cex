---
kind: collaboration
id: bld_collaboration_repo_map
pillar: P12
llm_function: COLLABORATE
purpose: How repo_map-builder works in crews with other builders
quality: 8.9
title: "Collaboration Repo Map"
version: "1.0.0"
author: wave1_builder_gen
tags: [repo_map, builder, collaboration]
tldr: "How repo_map-builder works in crews with other builders"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_contributor_guide
  - repo-map-builder
  - p12_wf_code_review
  - bld_collaboration_component_map
  - bld_architecture_repo_map
  - bld_collaboration_knowledge_graph
  - kind-builder
  - bld_architecture_kind
  - bld_collaboration_benchmark_suite
  - bld_collaboration_workflow_node
---

## Crew Role  
Creates and maintains a consistent, cross-repo context map for navigation and dependency tracking. Ensures alignment between repo structures, ownership, and purpose.  

## Receives From  
| Builder | What | Format |  
|---|---|---|  
| Repo configurer | Repo metadata (name, owner, purpose) | YAML |  
| Dependency tracker | Cross-repo dependency graph | JSON |  
| CI/CD system | Repo event triggers (create, delete) | Webhook |  

## Produces For  
| Builder | What | Format |  
|---|---|---|  
| Repo navigator | Visual repo map (graph, hierarchy) | JSON |  
| Documentation team | Repo context summary | Markdown |  
| Dependency analyzer | Normalized dependency graph | DOT |  

## Boundary  
Does NOT handle system architecture (component_map-builder), search index (knowledge_index-builder), or CI/CD pipeline orchestration (CI/CD team).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_contributor_guide]] | upstream | 0.25 |
| [[repo-map-builder]] | upstream | 0.23 |
| [[p12_wf_code_review]] | related | 0.21 |
| [[bld_collaboration_component_map]] | sibling | 0.20 |
| [[bld_architecture_repo_map]] | upstream | 0.20 |
| [[bld_collaboration_knowledge_graph]] | sibling | 0.20 |
| [[kind-builder]] | upstream | 0.20 |
| [[bld_architecture_kind]] | upstream | 0.19 |
| [[bld_collaboration_benchmark_suite]] | sibling | 0.19 |
| [[bld_collaboration_workflow_node]] | sibling | 0.19 |
