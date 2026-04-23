---
kind: collaboration
id: bld_collaboration_content_filter
pillar: P12
llm_function: COLLABORATE
purpose: How content_filter-builder works in crews with other builders
quality: 8.9
title: "Collaboration Content Filter"
version: "1.0.0"
author: wave1_builder_gen
tags: [content_filter, builder, collaboration]
tldr: "How content_filter-builder works in crews with other builders"
domain: "content_filter construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - content-filter-builder
  - p03_sp_content_filter_builder
  - bld_instruction_content_filter
  - p05_output_validator
  - bld_collaboration_safety_policy
  - bld_architecture_content_filter
  - kc_guardrail
  - bld_collaboration_parser
  - p11_qg_content_filter
  - bld_collaboration_compliance_framework
---

## Crew Role  

This ISO defines a content filter -- the moderation rules that gate output or input.
Filters content based on predefined criteria, ensuring compliance with policies and removing inappropriate or irrelevant material.  

## Receives From  
| Builder          | What              | Format  |  
|------------------|-------------------|---------|  
| Content Generator| Raw content       | JSON    |  
| Policy Manager   | Filtering rules   | YAML    |  
| Analytics Module | Metadata          | CSV     |  

## Produces For  
| Builder           | What              | Format  |  
|-------------------|-------------------|---------|  
| Content Processor | Filtered content  | JSON    |  
| Compliance Checker| Filtering reports | XML     |  
| Monitoring System | Logs              | Log files |  

## Boundary  
Does not enforce broad safety constraints (Guardrail) or validate output schemas (Output Validator). Those are handled by respective components.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[content-filter-builder]] | upstream | 0.37 |
| [[p03_sp_content_filter_builder]] | upstream | 0.32 |
| [[bld_instruction_content_filter]] | upstream | 0.26 |
| [[p05_output_validator]] | upstream | 0.26 |
| [[bld_collaboration_safety_policy]] | sibling | 0.25 |
| [[bld_architecture_content_filter]] | upstream | 0.24 |
| [[kc_guardrail]] | upstream | 0.22 |
| [[bld_collaboration_parser]] | sibling | 0.22 |
| [[p11_qg_content_filter]] | upstream | 0.22 |
| [[bld_collaboration_compliance_framework]] | sibling | 0.21 |
