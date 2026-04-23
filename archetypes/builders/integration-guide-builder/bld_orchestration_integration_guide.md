---
kind: collaboration
id: bld_collaboration_integration_guide
pillar: P12
llm_function: COLLABORATE
purpose: How integration_guide-builder works in crews with other builders
quality: 8.9
title: "Collaboration Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, collaboration]
tldr: "How integration_guide-builder works in crews with other builders"
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_subscription_tier
  - bld_collaboration_sdk_example
  - bld_collaboration_contributor_guide
  - bld_collaboration_cohort_analysis
  - bld_collaboration_reranker_config
  - bld_collaboration_white_label_config
  - bld_collaboration_product_tour
  - bld_collaboration_ab_test_config
  - bld_collaboration_sandbox_spec
  - bld_collaboration_api_reference
---

## Crew Role  
Creates and maintains comprehensive integration guides, ensuring alignment with product capabilities and developer needs. Collaborates with API, product, and support teams to validate accuracy and completeness.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| API Team      | API specifications    | JSON        |  
| Product Team  | Integration scenarios | Markdown    |  
| Support Team  | Common user issues    | Ticket system |  

## Produces For  
| Builder           | What                  | Format      |  
|-------------------|-----------------------|-------------|  
| Product Team      | Integration guides    | Markdown    |  
| Developer Portal  | Diagrams and workflows| SVG         |  
| Support Team      | Troubleshooting notes | Markdown    |  

## Boundary  
Does NOT handle code implementation (dev teams), quickstart tutorials (quickstart_guide-builder), or API schema details (api_reference-builder).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_subscription_tier]] | sibling | 0.36 |
| [[bld_collaboration_sdk_example]] | sibling | 0.36 |
| [[bld_collaboration_contributor_guide]] | sibling | 0.32 |
| [[bld_collaboration_cohort_analysis]] | sibling | 0.32 |
| [[bld_collaboration_reranker_config]] | sibling | 0.31 |
| [[bld_collaboration_white_label_config]] | sibling | 0.30 |
| [[bld_collaboration_product_tour]] | sibling | 0.30 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.30 |
| [[bld_collaboration_sandbox_spec]] | sibling | 0.29 |
| [[bld_collaboration_api_reference]] | sibling | 0.28 |
