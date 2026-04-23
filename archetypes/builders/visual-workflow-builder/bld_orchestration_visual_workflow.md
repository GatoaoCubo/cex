---
kind: collaboration
id: bld_collaboration_visual_workflow
pillar: P12
llm_function: COLLABORATE
purpose: How visual_workflow-builder works in crews with other builders
quality: 8.9
title: "Collaboration Visual Workflow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [visual_workflow, builder, collaboration]
tldr: "How visual_workflow-builder works in crews with other builders"
domain: "visual_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - visual-workflow-builder
  - kc_visual_workflow
  - bld_collaboration_workflow
  - bld_collaboration_workflow_node
  - bld_collaboration_ab_test_config
  - workflow-builder
  - bld_collaboration_eval_metric
  - bld_collaboration_schedule
  - p03_sp_visual_workflow_builder
  - bld_collaboration_agentic_rag
---

## Crew Role  
Enables non-technical team members to design, visualize, and iterate on workflow logic through drag-and-drop interfaces, ensuring alignment with business goals and technical constraints.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Data Source   | Raw input data        | JSON        |  
| Logic Builder | Rule definitions      | YAML        |  
| UI Builder    | UI component specs    | XML         |  
| Validation    | Constraint rules      | CSV         |  

## Produces For  
| Builder           | What                  | Format      |  
|-------------------|-----------------------|-------------|  
| Deployment        | Visual workflow diagram | SVG/PNG     |  
| Documentation     | Workflow description  | Markdown    |  
| Testing           | Testable workflow spec| JSON        |  
| Version Control   | Workflow file         | YAML        |  

## Boundary  
Does NOT execute workflows (Code Executor), store data (Data Storage Manager), validate logic (Validation Engine), or deploy workflows (Deployment Manager).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[visual-workflow-builder]] | related | 0.37 |
| [[kc_visual_workflow]] | upstream | 0.31 |
| [[bld_collaboration_workflow]] | sibling | 0.28 |
| [[bld_collaboration_workflow_node]] | sibling | 0.28 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.27 |
| [[workflow-builder]] | related | 0.27 |
| [[bld_collaboration_eval_metric]] | sibling | 0.27 |
| [[bld_collaboration_schedule]] | sibling | 0.26 |
| [[p03_sp_visual_workflow_builder]] | upstream | 0.25 |
| [[bld_collaboration_agentic_rag]] | sibling | 0.25 |
