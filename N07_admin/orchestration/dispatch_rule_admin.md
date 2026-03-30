---
id: p12_dr_admin
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2023-10-12
updated: 2023-10-12
author: dispatch-rule-builder
domain: administration
quality: null
tags: [dispatch, admin, management, governance]
tldr: Routes administrative and governance tasks to the admin agent_node
scope: admin
keywords: [administração, administration, política, policy, supervisao, oversight, gerenciar, manage]
agent_node: governance_agent_node
model: sonnet
priority: 7
confidence_threshold: 0.70
fallback: operations_agent_node
conditions: 
load_balance: false
routing_strategy: keyword_match
---

# Admin Dispatch Rule

## Purpose
Routes tasks related to administrative oversight, policy updates, and other governance activities to the admin agent_node. This routing ensures tasks are processed by specialists in administrative functions, improving efficiency and accuracy in handling governance responsibilities.

## Keyword Rationale
The selected keywords cover typical administrative themes in both English and Portuguese, ensuring comprehensive triggering across language boundaries. This includes major areas of administration such as policy and management tasks, enabling effective routing for tasks in these domains.

## Fallback Logic
In cases where tasks do not meet the confidence threshold, they are routed to the operations agent_node. This fallback ensures that essential governance tasks are not missed and can still be processed, albeit with broader operational capabilities.