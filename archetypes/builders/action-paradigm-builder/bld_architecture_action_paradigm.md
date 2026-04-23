---
kind: architecture
id: bld_architecture_action_paradigm
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of action_paradigm -- inventory, dependencies
quality: 9.0
title: "Architecture Action Paradigm"
version: "1.0.0"
author: wave1_builder_gen
tags: [action_paradigm, builder, architecture]
tldr: "Component map of action_paradigm -- inventory, dependencies"
domain: "action_paradigm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_architecture_collaboration_pattern
  - bld_architecture_compliance_framework
  - bld_architecture_discovery_questions
  - bld_architecture_sdk_example
  - bld_architecture_api_reference
  - bld_architecture_roi_calculator
  - bld_architecture_github_issue_template
  - bld_architecture_benchmark_suite
  - bld_architecture_legal_vertical
  - action-paradigm-builder
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| Action Orchestrator | Coordinates workflow execution | Core Dev | Active |
| Validation Engine | Enforces compliance rules | Risk Team | Active |
| State Manager | Tracks system state | Infrastructure | Under Development |
| API Gateway | Exposes external interfaces | UX Team | Active |
| Audit Logger | Records all actions | Compliance | Active |
| Rule Compiler | Translates policies to code | Core Dev | Active |
| Error Handler | Manages failures gracefully | SRE | Active |

## Dependencies
| From | To | Type |
|------|----|------|
| Action Orchestrator | Validation Engine | API |
| State Manager | Action Orchestrator | Message Queue |
| API Gateway | Rule Compiler | Database |
| Audit Logger | Error Handler | File System |
| Validation Engine | Rule Compiler | Configuration |

## Architectural Position
action_paradigm sits in P04 (Tools layer) as the behavioral specification for autonomous agent
execution. It is consumed by execution engines (robotics middleware, agent frameworks, simulation
platforms) that instantiate the paradigm at runtime. It sits above protocol interfaces (cli_tool,
api_client) and below orchestration sequences (workflow, dispatch_rule).

## Properties

| Property | Value |
|----------|-------|
| Kind | `architecture` |
| Pillar | P08 |
| Domain | action_paradigm construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_collaboration_pattern]] | sibling | 0.46 |
| [[bld_architecture_compliance_framework]] | sibling | 0.34 |
| [[bld_architecture_discovery_questions]] | sibling | 0.33 |
| [[bld_architecture_sdk_example]] | sibling | 0.32 |
| [[bld_architecture_api_reference]] | sibling | 0.31 |
| [[bld_architecture_roi_calculator]] | sibling | 0.31 |
| [[bld_architecture_github_issue_template]] | sibling | 0.31 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.30 |
| [[bld_architecture_legal_vertical]] | sibling | 0.29 |
| [[action-paradigm-builder]] | upstream | 0.29 |
