---
kind: collaboration
id: bld_collaboration_product_tour
pillar: P12
llm_function: COLLABORATE
purpose: How product_tour-builder works in crews with other builders
quality: 8.9
title: "Collaboration Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, collaboration]
tldr: "How product_tour-builder works in crews with other builders"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_interactive_demo
  - bld_collaboration_reward_model
  - bld_collaboration_sandbox_spec
  - bld_collaboration_integration_guide
  - bld_collaboration_reranker_config
  - bld_collaboration_cohort_analysis
  - bld_collaboration_white_label_config
  - bld_collaboration_contributor_guide
  - bld_collaboration_subscription_tier
  - bld_collaboration_ab_test_config
---

## Crew Role  
Designs and manages non-interactive product tours to educate users on key features without sales or activation focus.  

## Receives From  
| Builder     | What                  | Format      |  
|-------------|-----------------------|-------------|  
| Content Team| Feature descriptions  | Markdown    |  
| Design Team | Visual assets         | PNG/SVG     |  
| Engineering | Technical constraints | JSON spec   |  

## Produces For  
| Builder     | What                  | Format      |  
|-------------|-----------------------|-------------|  
| Engineering | Tour implementation   | JSON        |  
| Design Team | Storyboard            | Figma       |  
| Support Team| User guide            | PDF         |  

## Boundary  
Does NOT handle interactive demos (sales) or onboarding flows (activation). Interactive demos are managed by `interactive_demo-builder`; onboarding flows by `onboarding_flow-builder`. Technical implementation is handled by Engineering, not this builder.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_interactive_demo]] | sibling | 0.43 |
| [[bld_collaboration_reward_model]] | sibling | 0.37 |
| [[bld_collaboration_sandbox_spec]] | sibling | 0.35 |
| [[bld_collaboration_integration_guide]] | sibling | 0.34 |
| [[bld_collaboration_reranker_config]] | sibling | 0.32 |
| [[bld_collaboration_cohort_analysis]] | sibling | 0.31 |
| [[bld_collaboration_white_label_config]] | sibling | 0.31 |
| [[bld_collaboration_contributor_guide]] | sibling | 0.30 |
| [[bld_collaboration_subscription_tier]] | sibling | 0.28 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.28 |
