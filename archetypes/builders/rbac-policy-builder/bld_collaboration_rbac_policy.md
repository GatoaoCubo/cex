---
kind: collaboration
id: bld_collaboration_rbac_policy
pillar: P12
llm_function: COLLABORATE
purpose: How rbac_policy-builder works in crews with other builders
quality: null
title: "Collaboration Rbac Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [rbac_policy, builder, collaboration]
tldr: "How rbac_policy-builder works in crews with other builders"
domain: "rbac_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Designs, validates, and maintains Role-Based Access Control (RBAC) policies to enforce least-privilege access models across systems.  

## Receives From  
| Builder        | What                  | Format      |  
|----------------|-----------------------|-------------|  
| Security Architect | Policy templates      | YAML        |  
| Compliance Officer | Regulatory requirements | JSON        |  
| System Administrator | Existing role definitions | Text doc  |  

## Produces For  
| Builder        | What                  | Format      |  
|----------------|-----------------------|-------------|  
| Security Architect | Policy drafts        | YAML        |  
| Compliance Officer | Compliance reports   | PDF         |  
| System Administrator | Role manifests       | JSON        |  

## Boundary  
Does NOT handle permission assignments (handled by Permission Manager) or identity configuration (handled by Identity Provider). Policy enforcement is managed by Access Control Engine.
