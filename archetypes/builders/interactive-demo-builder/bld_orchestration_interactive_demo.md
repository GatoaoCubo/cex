---
kind: collaboration
id: bld_collaboration_interactive_demo
pillar: P12
llm_function: COLLABORATE
purpose: How interactive_demo-builder works in crews with other builders
quality: 8.9
title: "Collaboration Interactive Demo"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [interactive_demo, builder, collaboration]
tldr: "How interactive_demo-builder works in crews with other builders"
domain: "interactive_demo construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_product_tour
  - bld_collaboration_reranker_config
  - bld_collaboration_reward_model
  - bld_collaboration_ab_test_config
  - bld_collaboration_white_label_config
  - interactive-demo-builder
  - bld_collaboration_sandbox_spec
  - bld_collaboration_sdk_example
  - bld_collaboration_subscription_tier
  - bld_collaboration_integration_guide
---

## Crew Role  
Creates interactive demo scripts by integrating user stories, technical specs, and design assets into cohesive, executable demo flows. Acts as a bridge between content creators and engineers.  

## Receives From  
| Builder | What | Format |  
|---|---|---|  
| Content Writer | Script outline & user flows | Markdown |  
| Design Team | Visual assets & UI components | ZIP (images, Figma files) |  
| Engineering Team | Technical constraints & API specs | JSON (schema, endpoints) |  

## Produces For  
| Builder | What | Format |  
|---|---|---|  
| Content Writer | Demo script with annotated interactions | Markdown |  
| Engineering Team | Interactive element definitions | JSON (event handlers, state logic) |  
| QA Team | Demo preview link & test scenarios | URL + CSV (test cases) |  

## Boundary  
Does NOT handle hosting/deployment (DevOps), user testing (QA Team), or asset storage management (Design Team).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_product_tour]] | sibling | 0.41 |
| [[bld_collaboration_reranker_config]] | sibling | 0.36 |
| [[bld_collaboration_reward_model]] | sibling | 0.35 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.35 |
| [[bld_collaboration_white_label_config]] | sibling | 0.34 |
| [[interactive-demo-builder]] | upstream | 0.34 |
| [[bld_collaboration_sandbox_spec]] | sibling | 0.32 |
| [[bld_collaboration_sdk_example]] | sibling | 0.31 |
| [[bld_collaboration_subscription_tier]] | sibling | 0.31 |
| [[bld_collaboration_integration_guide]] | sibling | 0.31 |
