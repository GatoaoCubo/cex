---
kind: architecture
id: bld_architecture_collaboration_pattern
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of collaboration_pattern -- inventory, dependencies
quality: 9.0
title: "Architecture Collaboration Pattern"
version: "1.0.0"
author: wave1_builder_gen
tags: [collaboration_pattern, builder, architecture]
tldr: "Component map of collaboration_pattern -- inventory, dependencies"
domain: "collaboration_pattern construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_architecture_action_paradigm
  - collaboration-pattern-builder
  - bld_architecture_api_reference
  - bld_architecture_compliance_framework
  - bld_architecture_app_directory_entry
  - bld_architecture_discovery_questions
  - bld_architecture_visual_workflow
  - bld_architecture_benchmark_suite
  - bld_architecture_crew_template
  - bld_architecture_fintech_vertical
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| Pattern Orchestrator | Coordinates pattern execution | Collaboration Team | Active |
| Validator | Ensures pattern compliance | Rules Team | Active |
| UI Builder | Generates collaboration interfaces | UX Team | Under Development |
| Data Modeler | Defines pattern data schemas | Data Team | Active |
| Integration Hub | Connects to external systems | CEX Integration | Active |
| Logger | Tracks pattern usage | Ops Team | Active |

## Dependencies
| From | To | Type |
|------|----|------|
| Orchestrator | Validator | Control Flow |
| UI Builder | Data Modeler | Data Flow |
| Integration Hub | CEX API | External Dependency |
| Logger | Orchestrator | Event Subscription |

## Architectural Position
collaboration_pattern sits in P12 (Orchestration layer) as the structural specification for
multi-agent coordination topology. It is consumed by dispatch systems and agent orchestration
frameworks that instantiate agent roles and channels. It sits above individual agent definitions
(P02 agent) and alongside workflow (sequential execution) and dispatch_rule (task routing).

## Properties

| Property | Value |
|----------|-------|
| Kind | `architecture` |
| Pillar | P08 |
| Domain | collaboration_pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_action_paradigm]] | sibling | 0.40 |
| [[collaboration-pattern-builder]] | downstream | 0.31 |
| [[bld_architecture_api_reference]] | sibling | 0.31 |
| [[bld_architecture_compliance_framework]] | sibling | 0.30 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.30 |
| [[bld_architecture_discovery_questions]] | sibling | 0.29 |
| [[bld_architecture_visual_workflow]] | sibling | 0.29 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.29 |
| [[bld_architecture_crew_template]] | sibling | 0.28 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.28 |
