---
kind: memory
id: p10_lr_contributor_guide_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for contributor_guide construction
quality: null
title: "Learning Record Contributor Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [contributor_guide, builder, learning_record]
tldr: "Learned patterns and pitfalls for contributor_guide construction"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Observation  
Common issues include missing dev setup steps, vague PR flow descriptions, and inconsistent coding standard enforcement. Contributor guides often omit CLA requirements or fail to align with project-specific workflows.  

## Pattern  
Effective guides use structured sections with clear, actionable steps. Examples include code snippets for setup, explicit checklists for PRs, and links to style guides.  

## Evidence  
Reviewed guides from Kubernetes and React show alignment with spec sections, though some lack CLA details.  

## Recommendations  
- Include explicit dev setup commands and dependency installation steps.  
- Define PR flow with labeled workflows (e.g., "draft," "ready for review").  
- Reference external style guides (e.g., Prettier, ESLint) in coding standards.  
- Outline review process expectations (e.g., required approvals, testing).  
- Clearly state CLA requirements and provide direct links to sign.
