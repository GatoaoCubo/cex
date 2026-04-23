---
kind: architecture
id: bld_architecture_repo_map
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of repo_map -- inventory, dependencies
quality: 8.9
title: "Architecture Repo Map"
version: "1.0.0"
author: wave1_builder_gen
tags: [repo_map, builder, architecture]
tldr: "Component map of repo_map -- inventory, dependencies"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_architecture_fintech_vertical
  - bld_architecture_onboarding_flow
  - bld_architecture_discovery_questions
  - bld_architecture_legal_vertical
  - bld_architecture_pricing_page
  - bld_architecture_roi_calculator
  - bld_architecture_api_reference
  - bld_architecture_app_directory_entry
  - bld_architecture_quickstart_guide
  - bld_architecture_healthcare_vertical
---

## Component Inventory  
| Name          | Role                     | Owner         | Status    |  
|---------------|--------------------------|---------------|-----------|  
| RepoScanner   | Scans repos for metadata | Infrastructure| Active    |  
| DependencyResolver | Resolves dependencies | Data          | In Dev    |  
| MapperEngine  | Builds repo maps         | Analytics     | Active    |  
| RepoStorage   | Stores mapped data       | Operations    | Stable    |  
| Visualizer    | Renders repo maps        | UI/UX         | In Dev    |  
| ConfigManager | Manages builder configs  | DevOps        | Active    |  

## Dependencies  
| From          | To            | Type       |  
|---------------|---------------|------------|  
| RepoScanner   | GitAPI        | External   |  
| DependencyResolver | RepoScanner | Internal   |  
| MapperEngine  | DependencyResolver | Internal |  
| Visualizer    | MapperEngine  | Internal   |  
| ConfigManager | MapperEngine  | Internal   |  

## Architectural Position  
repo_map is a foundational component in the CEX ecosystem, enabling repository structure analysis and dependency tracking. It integrates with Git systems, feeds analytics pipelines, and ensures consistent mapping for CI/CD and governance tools, acting as a bridge between raw code data and actionable insights.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_fintech_vertical]] | sibling | 0.28 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.28 |
| [[bld_architecture_discovery_questions]] | sibling | 0.28 |
| [[bld_architecture_legal_vertical]] | sibling | 0.28 |
| [[bld_architecture_pricing_page]] | sibling | 0.27 |
| [[bld_architecture_roi_calculator]] | sibling | 0.27 |
| [[bld_architecture_api_reference]] | sibling | 0.27 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.26 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.26 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.26 |
