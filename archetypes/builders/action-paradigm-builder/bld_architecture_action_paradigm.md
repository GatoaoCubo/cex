---
kind: architecture
id: bld_architecture_action_paradigm
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of action_paradigm -- inventory, dependencies
quality: null
title: "Architecture Action Paradigm"
version: "1.0.0"
author: wave1_builder_gen
tags: [action_paradigm, builder, architecture]
tldr: "Component map of action_paradigm -- inventory, dependencies"
domain: "action_paradigm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
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
action_paradigm sits at the core of CEX operations, enabling automated, policy-driven execution of user actions while ensuring compliance, scalability, and auditability across trading, settlement, and risk management workflows.
