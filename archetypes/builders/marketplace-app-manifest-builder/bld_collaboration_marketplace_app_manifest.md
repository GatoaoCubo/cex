---
kind: collaboration
id: bld_collaboration_marketplace_app_manifest
pillar: P12
llm_function: COLLABORATE
purpose: How marketplace_app_manifest-builder works in crews with other builders
quality: 8.7
title: "Collaboration Marketplace App Manifest"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [marketplace_app_manifest, builder, collaboration]
tldr: "How marketplace_app_manifest-builder works in crews with other builders"
domain: "marketplace_app_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Generates and validates marketplace app manifests, ensuring compliance with marketplace schema and metadata requirements.  

## Receives From  
Builder | What | Format  
--- | --- | ---  
App Developer | App metadata | JSON  
Config Manager | Marketplace schema | YAML  
Dependency Tracker | External service references | CSV  

## Produces For  
Builder | What | Format  
--- | --- | ---  
Marketplace Validator | Parsed manifest | JSON  
Documentation Team | Manifest summary | Markdown  
Deployment System | Validated manifest | XML  

## Boundary  
Does NOT handle plugin loading or app directory entries. Plugin loading is managed by `plugin_loader`, and app directory entries are handled by `app_directory_manager`.
